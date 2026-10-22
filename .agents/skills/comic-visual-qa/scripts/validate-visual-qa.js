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
let data;
try {
  data = JSON.parse(fs.readFileSync(reportPath, "utf8"));
  if (!data || typeof data !== "object" || Array.isArray(data)) throw new Error("Report phải là object.");
} catch (error) {
  console.log(JSON.stringify({ reportValidity: "FAIL", qaOutcome: "UNDETERMINED", eligibleForNextStep: false, errors: [error.message], warnings: [] }, null, 2));
  process.exit(1);
}
const errors = [];
const warnings = [];
const allowed = new Set(["PASS", "FAIL", "NOT_APPLICABLE", "SKIPPED_BY_USER"]);
const hasText = value => typeof value === "string" && value.trim().length > 0;
const presets = {
  "studio-profile": ["style", "profile"],
  "studio-image": ["style"],
  "concept-test": ["style"],
  "technical-asset": ["style"],
  "comic-page": ["style", "focus", "emotionalImpact", "visualVitality", "selectedCompositionFidelity", "context", "storytelling"]
};
if (!Object.hasOwn(presets, data.deliverableType)) errors.push("Thiếu/sai deliverableType; xem references/report-contract.md.");
if (typeof data.hasCharacters !== "boolean") errors.push("hasCharacters phải là boolean.");
if (data.deliverableType === "studio-profile" && data.hasCharacters !== true) errors.push("studio-profile phải có hasCharacters=true.");
if (!data.schemaVersion) errors.push("Thiếu schemaVersion.");
if (!hasText(data.output)) errors.push("Thiếu/sai output.");
else if (!fs.existsSync(path.resolve(root, data.output))) errors.push(`Output không tồn tại: ${data.output}.`);
if (data.inputStatus === "STALE" || data.inputStatus === "STALE_INPUT") errors.push("Input của visual QA đã stale.");
if (data.requiredChecks !== undefined && (!Array.isArray(data.requiredChecks) || data.requiredChecks.some(v => !hasText(v)))) errors.push("requiredChecks phải là mảng tên check.");
const required = new Set([...(presets[data.deliverableType] || []), ...(Array.isArray(data.requiredChecks) ? data.requiredChecks : [])]);
if (data.hasCharacters === true) required.add("profile");
const checks = data.checks && typeof data.checks === "object" && !Array.isArray(data.checks) ? data.checks : {};
if (!Object.keys(checks).length) errors.push("Thiếu checks.");
if (data.requiresPerformanceCoherence === true) {
  const reads = data.performanceReadByCharacter;
  if (!reads || typeof reads !== "object" || !Object.keys(reads).length) errors.push("Thiếu performanceReadByCharacter cho shot dựa vào cảm xúc.");
  else {
    for (const [actor, read] of Object.entries(reads)) {
      if (!read.intendedRead || !read.observedRead) errors.push(`performanceReadByCharacter.${actor} thiếu intendedRead hoặc observedRead.`);
      if (!allowed.has(read.status)) errors.push(`performanceReadByCharacter.${actor}: status không hợp lệ.`);
      if (read.status === "FAIL" && (!read.conflictingSignals || !read.remediation)) errors.push(`performanceReadByCharacter.${actor}: FAIL cần conflictingSignals và remediation.`);
    }
  }
  const coherence = data.groupEmotionalCoherence;
  if (!coherence || !allowed.has(coherence.status)) errors.push("Thiếu groupEmotionalCoherence hợp lệ.");
  else if (coherence.status === "FAIL" && (!coherence.evidence || !coherence.remediation)) errors.push("groupEmotionalCoherence FAIL cần evidence và remediation.");
}
for (const name of required) if (!checks[name]) errors.push(`Thiếu check REQUIRED: ${name}.`);
for (const [name, raw] of Object.entries(checks)) {
  const check = raw && typeof raw === "object" && !Array.isArray(raw) ? raw : {};
  if (!allowed.has(check.status)) errors.push(`${name}: status không hợp lệ.`);
  if (["PASS", "FAIL"].includes(check.status) && !hasText(check.evidence)) errors.push(`${name}: ${check.status} thiếu evidence.`);
  if (check.status === "FAIL" && (!hasText(check.remediation) || !hasText(check.preserve) || typeof check.retryable !== "boolean")) errors.push(`${name}: FAIL cần remediation, preserve và retryable.`);
  if (check.status === "NOT_APPLICABLE" && !hasText(check.reason)) errors.push(`${name}: NOT_APPLICABLE cần reason.`);
  if (check.status === "NOT_APPLICABLE" && (name === "style" || (name === "profile" && data.hasCharacters === true))) errors.push(`${name}: check preset bắt buộc không được NOT_APPLICABLE.`);
  if (check.status === "SKIPPED_BY_USER" && (!hasText(check.reason) || !hasText(check.scope) || !hasText(check.authorizationSource))) errors.push(`${name}: SKIPPED_BY_USER cần reason, scope và authorizationSource.`);
}
if (["PASS", "FAIL"].includes(checks.style?.status)) {
  const groups = data.styleConsistencyByElement;
  if (!groups || typeof groups !== "object" || Array.isArray(groups) || !Object.keys(groups).length) errors.push("Thiếu styleConsistencyByElement.");
  else {
    const expected = data.hasCharacters === true ? ["faceSkin", "hair", "fabric", "jewelry", "background"] : ["subject", "background"];
    for (const name of expected) if (!Object.hasOwn(groups, name)) errors.push(`Thiếu nhóm style: ${name}; không xuất hiện thì ghi NOT_APPLICABLE có reason.`);
    for (const [name, group] of Object.entries(groups)) {
      if (!["PASS", "FAIL", "NOT_APPLICABLE"].includes(group?.status)) errors.push(`styleConsistencyByElement.${name}: status không hợp lệ.`);
      else if (group.status === "NOT_APPLICABLE" ? !hasText(group.reason) : !hasText(group.evidence)) errors.push(`styleConsistencyByElement.${name}: thiếu bằng chứng/lý do.`);
      if (group?.status === "FAIL" && checks.style.status !== "FAIL") errors.push(`Style tổng không được PASS khi ${name} FAIL.`);
    }
  }
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
const failedChecks = Object.entries(checks).filter(([, v]) => v?.status === "FAIL").map(([name]) => name);
if (data.requiresPerformanceCoherence === true) {
  for (const [name, read] of Object.entries(data.performanceReadByCharacter || {})) if (read?.status === "FAIL") failedChecks.push(`performanceReadByCharacter:${name}`);
  if (data.groupEmotionalCoherence?.status === "FAIL") failedChecks.push("groupEmotionalCoherence");
}
const waivedChecks = Object.entries(checks).filter(([, v]) => v?.status === "SKIPPED_BY_USER").map(([name]) => name);
const qaOutcome = errors.length ? "UNDETERMINED" : failedChecks.length ? "FAIL" : waivedChecks.length ? "PASS_WITH_WAIVERS" : "PASS";
const eligibleForNextStep = errors.length === 0 && failedChecks.length === 0;
const result = { reportValidity: errors.length ? "FAIL" : "PASS", qaOutcome, eligibleForNextStep, failedChecks, waivedChecks, requiredChecks: [...required], errors, warnings };
console.log(JSON.stringify(result, null, 2));
// 0: đủ điều kiện QA; 1: report không hợp lệ; 2: report hợp lệ, ảnh còn FAIL.
// Không phải user selection, canon hoặc permission giao file vào approved.
process.exit(errors.length ? 1 : eligibleForNextStep ? 0 : 2);
