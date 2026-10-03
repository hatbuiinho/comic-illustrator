#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const [svgArg, contractArg, outputArg] = process.argv.slice(2);
if (!svgArg || !contractArg || ["-h", "--help"].includes(svgArg)) {
  console.log("Usage: node render-composition-preview.js <semantic.svg> <composition.json> [output.png]");
  process.exit(svgArg ? 0 : 2);
}
const svgPath = path.resolve(svgArg);
const contractPath = path.resolve(contractArg);
const contract = JSON.parse(fs.readFileSync(contractPath, "utf8"));
const svg = fs.readFileSync(svgPath, "utf8");
const output = path.resolve(outputArg || path.join(path.dirname(svgPath), `${contract.optionId || path.basename(svgPath, ".svg")}-composition.png`));
const errors = [];
const warnings = [];
const escaped = value => String(value).replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const has = (name, value) => new RegExp(`${name}=["']${escaped(value)}["']`, "i").test(svg);
if (!contract.optionId) errors.push("Contract thiếu optionId.");
if (!/<svg\b/i.test(svg) || !/viewBox=["'][^"']+["']/i.test(svg)) errors.push("SVG cần root <svg> và viewBox.");
if (has("data-render-mode", "debug-box")) errors.push("Debug-box SVG không được dùng làm preview chính.");
if (!has("data-preview-type", "semantic-composition")) errors.push("SVG thiếu data-preview-type=semantic-composition.");

const actors = contract.actors || [];
if (!actors.length && !contract.allowNoActors) errors.push("Composition có nhân vật nhưng contract không khai báo actors.");
for (const actor of actors) {
  if (!actor.id) { errors.push("Actor thiếu id."); continue; }
  if (!has("data-actor-id", actor.id)) errors.push(`Thiếu silhouette actor: ${actor.id}.`);
  if (!actor.profileReference) errors.push(`Actor ${actor.id} thiếu profileReference.`);
  else {
    if (!fs.existsSync(path.resolve(path.dirname(contractPath), actor.profileReference))) errors.push(`Profile reference không tồn tại: ${actor.profileReference}.`);
    if (!has("data-profile-ref", actor.profileReference)) errors.push(`SVG chưa ghi profile provenance cho ${actor.id}.`);
  }
  for (const part of actor.requiredParts || ["head", "torso", "gesture"]) {
    const pattern = new RegExp(`data-owner=["']${escaped(actor.id)}["'][^>]*data-part=["']${escaped(part)}["']|data-part=["']${escaped(part)}["'][^>]*data-owner=["']${escaped(actor.id)}["']`, "i");
    if (!pattern.test(svg)) errors.push(`Actor ${actor.id} thiếu semantic part: ${part}.`);
  }
  const colors = Object.values(actor.palette || {}).filter(value => typeof value === "string");
  if (!colors.length) errors.push(`Actor ${actor.id} thiếu palette lấy từ profile.`);
  for (const color of colors) if (!svg.toLowerCase().includes(color.toLowerCase())) errors.push(`SVG chưa dùng màu ${color} của actor ${actor.id}.`);
}
for (const anchor of contract.requiredLocationAnchors || []) if (!has("data-location-anchor", anchor)) errors.push(`Thiếu location anchor: ${anchor}.`);
for (const interaction of contract.requiredInteractions || []) if (!has("data-interaction", interaction)) errors.push(`Thiếu interaction: ${interaction}.`);
if (contract.layoutBasis?.pageImage && !has("data-role", "layout-raster")) errors.push("Có pageImage nhưng SVG thiếu layout raster layer.");
if (!has("data-role", "background") && (contract.requiredLocationAnchors || []).length) warnings.push("Không có background layer tổng; chỉ tìm thấy anchor riêng lẻ.");
if ((svg.match(/data-role=["']actor["']/gi) || []).length < actors.length) errors.push("Số actor semantic trong SVG ít hơn contract.");

if (errors.length) {
  console.error(JSON.stringify({ previewStatus: "BLOCKED", reason: "SEMANTIC_RENDER_INSUFFICIENT", errors, warnings }, null, 2));
  process.exit(1);
}
fs.mkdirSync(path.dirname(output), { recursive: true });
const render = spawnSync("rsvg-convert", ["-o", output, svgPath], { encoding: "utf8" });
if (render.status !== 0) {
  console.error(render.stderr || "Không rasterize được semantic SVG.");
  process.exit(render.status || 1);
}
console.log(JSON.stringify({ optionId: contract.optionId, renderMode: "semantic-svg", svgPath, pngPath: output, previewStatus: "READY", warnings }, null, 2));
