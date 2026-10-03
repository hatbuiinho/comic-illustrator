#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const receiptArg = process.argv[2];
if (!receiptArg || ["-h", "--help"].includes(receiptArg)) {
  console.log("Usage: node reconcile-delivery.js <receipt.json>");
  process.exit(receiptArg ? 0 : 2);
}
const receiptPath = path.resolve(receiptArg);
const receipt = JSON.parse(fs.readFileSync(receiptPath, "utf8"));
const projectRoot = path.resolve(path.dirname(receiptPath), receipt.projectRootFromReceipt || ".");
const manifestPath = path.resolve(projectRoot, receipt.manifest);
const destination = path.resolve(projectRoot, receipt.destination);
if (!fs.existsSync(destination)) {
  console.error("ERROR: File approved trong receipt không tồn tại; cần xử lý thủ công.");
  process.exit(1);
}
const errors = [];
for (const update of receipt.pathUpdates || []) {
  try {
    const file = path.resolve(path.dirname(manifestPath), update.file);
    const original = fs.readFileSync(file, "utf8");
    if (!original.includes(update.from) && !original.includes(update.to)) throw new Error("không tìm thấy from/to");
    if (original.includes(update.from)) {
      const temporary = `${file}.${process.pid}.tmp`;
      fs.writeFileSync(temporary, original.split(update.from).join(update.to));
      fs.renameSync(temporary, file);
    }
    if (!receipt.completedUpdates.includes(update.file)) receipt.completedUpdates.push(update.file);
  } catch (error) { errors.push(`${update.file}: ${error.message}`); }
}
if (receipt.continuity && !receipt.continuityCommitted) {
  const contextScript = path.resolve(__dirname, "../../comic-continuity-manager/scripts/comic-context.py");
  const ledger = path.resolve(path.dirname(manifestPath), receipt.continuity.ledger);
  const event = path.resolve(path.dirname(manifestPath), receipt.continuity.event);
  const result = spawnSync("python3", [contextScript, "commit-event", ledger, event, "--write"], { encoding: "utf8" });
  if (result.status === 0) receipt.continuityCommitted = true;
  else errors.push((result.stderr || result.stdout).trim());
}
receipt.errors = errors;
receipt.status = errors.length ? "CONTEXT_PENDING" : "COMPLETED";
const temporary = `${receiptPath}.${process.pid}.tmp`;
fs.writeFileSync(temporary, `${JSON.stringify(receipt, null, 2)}\n`);
fs.renameSync(temporary, receiptPath);
console.log(JSON.stringify({ status: receipt.status, errors }, null, 2));
process.exit(errors.length ? 1 : 0);
