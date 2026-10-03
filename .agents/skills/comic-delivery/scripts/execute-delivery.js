#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const args = process.argv.slice(2);
const execute = args.includes("--execute");
const manifestArg = args.find(arg => arg !== "--execute");
if (!manifestArg || ["-h", "--help"].includes(manifestArg)) {
  console.log("Usage: node execute-delivery.js <delivery.json> [--execute]");
  process.exit(manifestArg ? 0 : 2);
}
const manifestPath = path.resolve(manifestArg);
const manifestDir = path.dirname(manifestPath);
const data = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
const projectRoot = path.resolve(manifestDir, data.projectRoot || ".");
const confined = raw => {
  const target = path.resolve(manifestDir, raw);
  if (target !== projectRoot && !target.startsWith(`${projectRoot}${path.sep}`)) throw new Error(`Đường dẫn vượt projectRoot: ${raw}`);
  return target;
};
const source = confined(data.output || "");
const approvedDir = confined(data.approvedDir || "approved");
const destination = path.join(approvedDir, path.basename(source));
const receiptDir = path.join(approvedDir, ".delivery-receipts");
const receiptPath = path.join(receiptDir, `${path.basename(source)}.json`);
function atomicJson(file, value) {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  const temporary = path.join(path.dirname(file), `.${path.basename(file)}.${process.pid}.tmp`);
  fs.writeFileSync(temporary, `${JSON.stringify(value, null, 2)}\n`);
  fs.renameSync(temporary, file);
}
function preflight() {
  const errors = [];
  if (!fs.existsSync(source)) errors.push("Output không tồn tại.");
  if (!data.approvedDir) errors.push("Thiếu approvedDir.");
  if (data.userSelectedOutput !== true) errors.push("Chưa có userSelectedOutput: true.");
  if (fs.existsSync(destination)) errors.push("Đích approved đã tồn tại.");
  for (const [name, raw] of Object.entries(data.checks || {})) {
    const check = typeof raw === "string" ? { status: raw } : raw;
    if (!["PASS", "NOT_APPLICABLE", "SKIPPED_BY_USER"].includes(check.status)) errors.push(`${name}: chưa cho phép delivery.`);
    if (check.status === "SKIPPED_BY_USER" && (!check.reason || !check.scope)) errors.push(`${name}: thiếu reason/scope.`);
  }
  return errors;
}
try {
  const errors = preflight();
  if (errors.length) throw new Error(errors.join("; "));
  const plan = {
    projectRootFromReceipt: path.relative(receiptDir, projectRoot) || ".",
    manifest: path.relative(projectRoot, manifestPath),
    source: path.relative(projectRoot, source),
    destination: path.relative(projectRoot, destination),
    receipt: path.relative(projectRoot, receiptPath),
    pathUpdates: data.pathUpdates || [],
    continuity: data.continuity || null
  };
  if (!execute) {
    console.log(JSON.stringify({ status: "DRY_RUN", plan }, null, 2));
    process.exit(0);
  }
  const receipt = { schemaVersion: 1, status: "PREPARED", ...plan, completedUpdates: [], errors: [] };
  atomicJson(receiptPath, receipt);
  fs.mkdirSync(approvedDir, { recursive: true });
  fs.renameSync(source, destination);
  receipt.status = "FILED";
  atomicJson(receiptPath, receipt);
  for (const update of data.pathUpdates || []) {
    const file = confined(update.file);
    const original = fs.readFileSync(file, "utf8");
    if (!original.includes(update.from) && !original.includes(update.to)) throw new Error(`Không tìm thấy path cần cập nhật trong ${update.file}.`);
    if (original.includes(update.from)) {
      const temporary = `${file}.${process.pid}.tmp`;
      fs.writeFileSync(temporary, original.split(update.from).join(update.to));
      fs.renameSync(temporary, file);
    }
    receipt.completedUpdates.push(update.file);
    atomicJson(receiptPath, receipt);
  }
  if (data.continuity) {
    const contextScript = path.resolve(__dirname, "../../comic-continuity-manager/scripts/comic-context.py");
    const result = spawnSync("python3", [contextScript, "commit-event", confined(data.continuity.ledger), confined(data.continuity.event), "--write"], { encoding: "utf8" });
    if (result.status !== 0) throw new Error(`Continuity pending: ${(result.stderr || result.stdout).trim()}`);
    receipt.continuityCommitted = true;
  }
  receipt.status = "COMPLETED";
  atomicJson(receiptPath, receipt);
  console.log(JSON.stringify({ status: "COMPLETED", destination: plan.destination, receipt: plan.receipt }, null, 2));
} catch (error) {
  if (fs.existsSync(receiptPath)) {
    const receipt = JSON.parse(fs.readFileSync(receiptPath, "utf8"));
    receipt.status = fs.existsSync(destination) ? "CONTEXT_PENDING" : "FAILED";
    receipt.errors = [...(receipt.errors || []), error.message];
    atomicJson(receiptPath, receipt);
    console.error(`ERROR: ${error.message}\nReceipt: ${receiptPath}`);
  } else console.error(`ERROR: ${error.message}`);
  process.exit(1);
}
