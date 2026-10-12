#!/usr/bin/env node
const fs = require("fs");
const path = require("path");

const manifestArg = process.argv[2];
if (!manifestArg) {
  console.error("Usage: node validate-delivery.js <delivery.json>");
  process.exit(2);
}
const file = path.resolve(manifestArg);
const root = path.dirname(file);
const data = JSON.parse(fs.readFileSync(file, "utf8"));
const errors = [];
const outputs = Array.isArray(data.outputs) && data.outputs.length ? data.outputs : (data.output ? [data.output] : []);
if (!outputs.length) errors.push("Thiếu output hoặc outputs.");
for (const output of outputs) if (!fs.existsSync(path.resolve(root, output))) errors.push(`Output không tồn tại: ${output}.`);
if (data.userSelectedOutput !== true) errors.push("Chưa có userSelectedOutput: true.");
if (outputs.length > 1 && data.status !== "layer-package-ready") errors.push("Bộ nhiều layer cần status: layer-package-ready.");
if (outputs.length > 1 && !data.checks?.layerPackage) errors.push("Bộ nhiều layer thiếu check layerPackage.");
for (const [name, check] of Object.entries(data.checks || {})) {
  const status = typeof check === "string" ? check : check.status;
  if (!["PASS", "NOT_APPLICABLE", "SKIPPED_BY_USER"].includes(status)) errors.push(`${name}: trạng thái ${status || "thiếu"} chưa cho phép bàn giao.`);
  if (status === "SKIPPED_BY_USER" && (typeof check === "string" || !check.reason || !check.scope)) errors.push(`${name}: SKIPPED_BY_USER cần reason và scope.`);
}
if (!data.approvedDir) errors.push("Thiếu approvedDir.");
else for (const output of outputs) {
  const destination = path.resolve(root, data.approvedDir, path.basename(output));
  if (fs.existsSync(destination)) errors.push(`Đích approved đã tồn tại: ${destination}`);
}
if (errors.length) {
  errors.forEach(message => console.error(`FAIL: ${message}`));
  process.exit(1);
}
console.log("PASS: delivery đủ điều kiện kỹ thuật để chờ thao tác chuyển file.");
