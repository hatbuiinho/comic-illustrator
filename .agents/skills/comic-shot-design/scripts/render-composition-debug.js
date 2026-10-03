#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const [contractArg, outputArg] = process.argv.slice(2);
if (!contractArg || ["-h", "--help"].includes(contractArg)) {
  console.log("Usage: node render-composition-debug.js <geometry.json> [output.png]");
  process.exit(contractArg ? 0 : 2);
}
const contractPath = path.resolve(contractArg);
const data = JSON.parse(fs.readFileSync(contractPath, "utf8"));
const canvas = data.canvas || { width: 1200, height: 800 };
const output = path.resolve(outputArg || path.join(path.dirname(contractPath), `${data.optionId || "composition"}-debug.png`));
const svgPath = output.replace(/\.png$/i, ".svg");
const validBox = box => box && [box.x, box.y, box.width, box.height].every(Number.isFinite) && box.x >= 0 && box.y >= 0 && box.width > 0 && box.height > 0 && box.x + box.width <= 1 && box.y + box.height <= 1;
const rect = (box, attrs) => `<rect x="${box.x * canvas.width}" y="${box.y * canvas.height}" width="${box.width * canvas.width}" height="${box.height * canvas.height}" ${attrs}/>`;
if (!validBox(data.frame)) {
  console.error("FAIL: frame không hợp lệ.");
  process.exit(1);
}
const elements = [`<rect width="100%" height="100%" fill="#f5f1e8"/>`, rect(data.frame, 'fill="#dce6ec" stroke="#19252d" stroke-width="5"')];
for (const box of data.textReserve || []) if (validBox(box)) elements.push(rect(box, 'fill="#ffd84a" fill-opacity="0.3" stroke="#a87900"'));
if (validBox(data.safeZone)) elements.push(rect(data.safeZone, 'fill="none" stroke="#249644" stroke-width="4" stroke-dasharray="14 9"'));
if (validBox(data.spine)) elements.push(rect(data.spine, 'fill="#d92d3a" fill-opacity="0.24" stroke="#a21320"'));
for (const subject of data.subjects || []) {
  if (!validBox(subject.box)) continue;
  elements.push(rect(subject.box, 'rx="10" fill="#5689a6" fill-opacity="0.8" stroke="#17232c" stroke-width="3"'));
  elements.push(`<text x="${(subject.box.x + subject.box.width / 2) * canvas.width}" y="${(subject.box.y + subject.box.height / 2) * canvas.height}" text-anchor="middle" font-family="sans-serif" font-size="18" fill="white">${subject.id || "subject"}</text>`);
}
const svg = `<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" data-render-mode="debug-box" width="${canvas.width}" height="${canvas.height}" viewBox="0 0 ${canvas.width} ${canvas.height}">${elements.join("")}</svg>\n`;
fs.mkdirSync(path.dirname(output), { recursive: true });
fs.writeFileSync(svgPath, svg);
const render = spawnSync("rsvg-convert", ["-o", output, svgPath], { encoding: "utf8" });
if (render.status !== 0) process.exit(render.status || 1);
console.log(JSON.stringify({ optionId: data.optionId, renderMode: "debug-box", pngPath: output, svgPath }, null, 2));
