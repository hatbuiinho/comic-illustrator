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
if (!data.output || !fs.existsSync(path.resolve(root, data.output))) errors.push("Output không tồn tại.");
if (data.userSelectedOutput !== true) errors.push("Chưa có userSelectedOutput: true.");
for (const [name, check] of Object.entries(data.checks || {})) {
  const status = typeof check === "string" ? check : check.status;
  if (!["PASS", "NOT_APPLICABLE", "SKIPPED_BY_USER"].includes(status)) errors.push(`${name}: trạng thái ${status || "thiếu"} chưa cho phép bàn giao.`);
  if (status === "SKIPPED_BY_USER" && (typeof check === "string" || !check.reason || !check.scope)) errors.push(`${name}: SKIPPED_BY_USER cần reason và scope.`);
}
if (!data.approvedDir) errors.push("Thiếu approvedDir.");
else if (data.output) {
  const destination = path.resolve(root, data.approvedDir, path.basename(data.output));
  if (fs.existsSync(destination)) errors.push(`Đích approved đã tồn tại: ${destination}`);
}
if (errors.length) {
  errors.forEach(message => console.error(`FAIL: ${message}`));
  process.exit(1);
}
console.log("PASS: delivery đủ điều kiện kỹ thuật để chờ thao tác chuyển file.");
