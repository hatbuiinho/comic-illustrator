#!/usr/bin/env node
const fs = require("fs");
const path = require("path");

const pageArg = process.argv[2];
if (!pageArg || ["-h", "--help"].includes(pageArg)) {
  console.log("Usage: node discover-layout.js <page-directory>");
  process.exit(pageArg ? 0 : 2);
}
const pageDir = path.resolve(pageArg);
const candidates = [];
function walk(dir, depth = 0) {
  if (depth > 2) return;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const target = path.join(dir, entry.name);
    if (entry.isDirectory() && !["outputs", "approved", "tmp"].includes(entry.name)) walk(target, depth + 1);
    else if (entry.isFile() && entry.name.endsWith(".json")) {
      try {
        const data = JSON.parse(fs.readFileSync(target, "utf8"));
        if (Array.isArray(data.spreads) && data.spreads.some(spread => Array.isArray(spread.frames))) {
          candidates.push(path.relative(pageDir, target));
        }
      } catch (_) { /* Không phải JSON hợp lệ; validator khác sẽ báo khi được chọn. */ }
    }
  }
}
if (!fs.existsSync(pageDir) || !fs.statSync(pageDir).isDirectory()) {
  console.error("ERROR: page-directory không tồn tại.");
  process.exit(2);
}
walk(pageDir);
const preferred = candidates.filter(item => ["layout.json", "manifest.json"].includes(path.basename(item)));
const selected = candidates.length === 1 ? candidates[0] : (preferred.length === 1 ? preferred[0] : null);
console.log(JSON.stringify({ status: selected ? "RESOLVED" : candidates.length ? "AMBIGUOUS" : "NOT_FOUND", selected, candidates }, null, 2));
process.exit(selected ? 0 : 1);
