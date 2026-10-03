#!/usr/bin/env node
const fs = require("fs");
const path = require("path");

const reportArg = process.argv[2];
if (!reportArg || ["-h", "--help"].includes(reportArg)) {
  console.log("Usage: node validate-visual-qa.js <visual-qa.json>");
  process.exit(reportArg ? 0 : 2);
}
const reportPath = path.resolve(reportArg);
const root = path.dirname(reportPath);
const data = JSON.parse(fs.readFileSync(reportPath, "utf8"));
const errors = [];
const warnings = [];
const allowed = new Set(["PASS", "FAIL", "NOT_APPLICABLE", "SKIPPED_BY_USER"]);
if (!data.schemaVersion) errors.push("Thiếu schemaVersion.");
if (!data.output) errors.push("Thiếu output.");
else if (!fs.existsSync(path.resolve(root, data.output))) errors.push(`Output không tồn tại: ${data.output}.`);
if (data.inputStatus === "STALE" || data.inputStatus === "STALE_INPUT") errors.push("Input của visual QA đã stale.");
const required = new Set(data.requiredChecks || []);
const checks = data.checks || {};
for (const name of required) if (!checks[name]) errors.push(`Thiếu check REQUIRED: ${name}.`);
for (const [name, raw] of Object.entries(checks)) {
  const check = typeof raw === "string" ? { status: raw } : raw;
  if (!allowed.has(check.status)) errors.push(`${name}: status không hợp lệ.`);
  if (check.status === "FAIL" && !check.evidence) errors.push(`${name}: FAIL thiếu evidence.`);
  if (check.status === "FAIL" && !check.remediation) warnings.push(`${name}: FAIL chưa có remediation.`);
  if (check.status === "SKIPPED_BY_USER" && (!check.reason || !check.scope)) errors.push(`${name}: SKIPPED_BY_USER cần reason và scope.`);
}
const dependencies = data.continuityDependencies || {};
for (const key of ["mustNotChange", "forbidden"]) {
  for (const item of dependencies[key] || []) {
    const id = typeof item === "string" ? item : item.key;
    const checkName = `${key}:${id}`;
    if (!checks[checkName]) errors.push(`Thiếu continuity check: ${checkName}.`);
  }
}
if (data.continuityEventCommitted === true) errors.push("Visual QA không được commit continuity event.");
const result = { status: errors.length ? "FAIL" : "PASS", errors, warnings };
console.log(JSON.stringify(result, null, 2));
process.exit(errors.length ? 1 : 0);
