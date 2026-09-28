#!/usr/bin/env node
const fs = require("fs");
const path = require("path");

const [manifestArg, outputArg] = process.argv.slice(2);
if (!manifestArg || ["-h", "--help"].includes(manifestArg)) {
  console.log("Usage: node layout-frame-qa.js <manifest.json> [output-directory]");
  process.exit(manifestArg ? 0 : 2);
}

const allowed = new Set(["REQUIRED", "NOT_APPLICABLE", "SKIPPED_BY_USER"]);
const manifestPath = path.resolve(manifestArg);
const manifestDir = path.dirname(manifestPath);
const outputDir = path.resolve(outputArg || path.join(manifestDir, "qa"));
const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
const report = { manifest: manifestPath, status: "PASS", failures: [], warnings: [], passes: [], skipped: [], spreads: [] };

function resolve(file) { return path.resolve(manifestDir, file); }
function add(bucket, scope, message) { report[bucket].push({ scope, message }); }
function fail(scope, message) { add("failures", scope, message); }
function warn(scope, message) { add("warnings", scope, message); }
function pass(scope, message) { add("passes", scope, message); }
function skip(scope, message) { add("skipped", scope, message); }
function boxValid(box) {
  return box && [box.x, box.y, box.width, box.height].every(Number.isFinite) &&
    box.x >= 0 && box.y >= 0 && box.width > 0 && box.height > 0 &&
    box.x + box.width <= 1 && box.y + box.height <= 1;
}
function intersects(a, b) {
  return a.x < b.x + b.width && a.x + a.width > b.x &&
    a.y < b.y + b.height && a.y + a.height > b.y;
}
function contains(outer, inner) {
  return inner.x >= outer.x && inner.y >= outer.y &&
    inner.x + inner.width <= outer.x + outer.width &&
    inner.y + inner.height <= outer.y + outer.height;
}
function insideEllipse(outer, inner) {
  const cx = outer.x + outer.width / 2;
  const cy = outer.y + outer.height / 2;
  const rx = outer.width / 2;
  const ry = outer.height / 2;
  return [[inner.x, inner.y], [inner.x + inner.width, inner.y],
    [inner.x, inner.y + inner.height], [inner.x + inner.width, inner.y + inner.height]]
    .every(([x, y]) => ((x - cx) ** 2) / (rx ** 2) + ((y - cy) ** 2) / (ry ** 2) <= 1);
}
function imageSize(file) {
  const data = fs.readFileSync(file);
  if (data.subarray(0, 8).equals(Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]))) {
    return { width: data.readUInt32BE(16), height: data.readUInt32BE(20), mime: "image/png" };
  }
  if (data[0] === 0xff && data[1] === 0xd8) {
    for (let i = 2; i < data.length - 9; i += 1) {
      if (data[i] === 0xff && data[i + 1] >= 0xc0 && data[i + 1] <= 0xc3) {
        return { width: data.readUInt16BE(i + 5), height: data.readUInt16BE(i + 7), mime: "image/jpeg" };
      }
    }
  }
  throw new Error("Chỉ hỗ trợ PNG hoặc JPEG.");
}
function dataUri(file, mime) { return `data:${mime};base64,${fs.readFileSync(file).toString("base64")}`; }
function rect(box, canvas, attrs = "") {
  return `<rect x="${box.x * canvas.width}" y="${box.y * canvas.height}" width="${box.width * canvas.width}" height="${box.height * canvas.height}" ${attrs}/>`;
}
function rawStatus(value) { return typeof value === "string" ? value : value?.status; }
function checkStatus(name, frame, spread) {
  const candidates = [
    frame?.checks?.[name], spread?.checks?.[name], manifest.overrides?.[name],
    manifest.defaults?.checks?.[name]
  ];
  const found = candidates.find(value => rawStatus(value));
  const status = rawStatus(found) || "REQUIRED";
  if (!allowed.has(status)) {
    fail(`checks/${name}`, `Trạng thái không hợp lệ: ${status}.`);
    return "REQUIRED";
  }
  return status;
}
function reasonFor(name, frame, spread) {
  const item = [frame?.checks?.[name], spread?.checks?.[name], manifest.overrides?.[name]].find(value => value?.reason);
  return item?.reason || "Không áp dụng theo cấu hình.";
}
function evaluate(name, frame, spread, scope, test, failureMessage, successMessage) {
  const status = checkStatus(name, frame, spread);
  if (status === "NOT_APPLICABLE") return skip(scope, `${name}: N/A.`);
  if (status === "SKIPPED_BY_USER") return skip(scope, `${name}: bỏ qua theo yêu cầu người dùng — ${reasonFor(name, frame, spread)}`);
  if (test) pass(scope, successMessage);
  else fail(scope, failureMessage);
}

fs.mkdirSync(outputDir, { recursive: true });
if (!Array.isArray(manifest.spreads) || manifest.spreads.length === 0) fail("manifest", "Cần ít nhất một spread.");

for (const spread of manifest.spreads || []) {
  const scope = spread.id || "spread-khong-ten";
  const canvas = spread.canvas || { width: 1410, height: 1000 };
  const prepared = [];
  let background = null;
  if (!spread.pageImage) fail(`${scope}/layout`, "Thiếu pageImage là raster layout gốc có text.");
  else {
    const file = resolve(spread.pageImage);
    if (!fs.existsSync(file)) fail(`${scope}/layout`, `Không tìm thấy layout: ${spread.pageImage}`);
    else try {
      const meta = imageSize(file);
      background = `<image href="${dataUri(file, meta.mime)}" width="${canvas.width}" height="${canvas.height}" preserveAspectRatio="none"/>`;
      pass(`${scope}/layout`, "Đã đọc layout gốc có text.");
    } catch (error) { fail(`${scope}/layout`, error.message); }
  }

  const print = manifest.defaults?.printTrim;
  const safe = print?.criticalSafePercent ? {
    x: print.criticalSafePercent.x,
    y: print.criticalSafePercent.y,
    width: 1 - 2 * print.criticalSafePercent.x,
    height: 1 - 2 * print.criticalSafePercent.y
  } : null;

  for (const frame of spread.frames || []) {
    const frameScope = `${scope}/${frame.id || "frame-khong-ten"}`;
    evaluate("frame", frame, spread, frameScope, boxValid(frame.box), "Frame box không hợp lệ.", "Frame box hợp lệ.");
    let output = null;
    if (frame.output) {
      const file = resolve(frame.output);
      if (!fs.existsSync(file)) fail(frameScope, `Không tìm thấy output: ${frame.output}`);
      else try {
        const meta = imageSize(file);
        output = { ...meta, uri: dataUri(file, meta.mime) };
        const expected = frame.box.width * canvas.width / (frame.box.height * canvas.height);
        if (frame.contentFrame && !boxValid(frame.contentFrame)) fail(frameScope, "contentFrame không hợp lệ.");
        const actual = boxValid(frame.contentFrame)
          ? frame.contentFrame.width * meta.width / (frame.contentFrame.height * meta.height)
          : meta.width / meta.height;
        const error = Math.abs(actual / expected - 1);
        evaluate("ratio", frame, spread, `${frameScope}/ratio`, error <= (frame.ratioTolerance ?? manifest.defaults?.ratioTolerance ?? 0.015), `Sai tỷ lệ ${(error * 100).toFixed(2)}%.`, `Tỷ lệ khớp, lệch ${(error * 100).toFixed(2)}%.`);
      } catch (error) { fail(frameScope, error.message); }
    } else warn(frameScope, "Chưa có output; chỉ kiểm guide.");

    for (const critical of frame.critical || []) {
      const criticalScope = `${frameScope}/${critical.id || "critical"}`;
      if (!boxValid(critical.box)) { fail(criticalScope, "Critical box không hợp lệ."); continue; }
      const inMask = frame.shape === "ellipse"
        ? insideEllipse(frame.box, critical.box)
        : contains(frame.box, critical.box);
      evaluate("frame", frame, spread, criticalScope, inMask, "Chi tiết nằm ngoài frame/mask.", "Chi tiết nằm trong frame/mask.");
      if (safe) evaluate("printSafe", frame, spread, `${criticalScope}/printSafe`, contains(safe, critical.box), "Chi tiết vượt critical-safe.", "Chi tiết nằm trong critical-safe.");
      else if (checkStatus("printSafe", frame, spread) === "REQUIRED") fail(`${criticalScope}/printSafe`, "Thiếu defaults.printTrim.criticalSafePercent.");
      const textHit = (frame.textReserve || []).some(area => intersects(critical.box, area));
      evaluate("textReserve", frame, spread, `${criticalScope}/textReserve`, !textHit, "Chi tiết đè vùng chữ.", "Chi tiết không đè vùng chữ.");
      const spineHit = frame.spine && intersects(critical.box, frame.spine);
      evaluate("spine", frame, spread, `${criticalScope}/spine`, !spineHit, "Chi tiết rơi vào gáy.", "Chi tiết không rơi vào gáy.");
    }
    prepared.push({ frame, output });
  }

  let overlay = null;
  if (background) {
    const guides = [];
    const art = [];
    for (const { frame, output } of prepared) {
      if (output && boxValid(frame.contentFrame)) {
        const cf = frame.contentFrame;
        const sx = frame.box.width * canvas.width / (cf.width * output.width);
        const sy = frame.box.height * canvas.height / (cf.height * output.height);
        art.push(`<image href="${output.uri}" x="${frame.box.x * canvas.width - cf.x * output.width * sx}" y="${frame.box.y * canvas.height - cf.y * output.height * sy}" width="${output.width * sx}" height="${output.height * sy}" preserveAspectRatio="none" opacity="0.86"/>`);
      } else if (output) art.push(`<image href="${output.uri}" x="${frame.box.x * canvas.width}" y="${frame.box.y * canvas.height}" width="${frame.box.width * canvas.width}" height="${frame.box.height * canvas.height}" preserveAspectRatio="xMidYMid slice" opacity="0.86"/>`);
      if (frame.shape === "ellipse") {
        guides.push(`<ellipse cx="${(frame.box.x + frame.box.width / 2) * canvas.width}" cy="${(frame.box.y + frame.box.height / 2) * canvas.height}" rx="${frame.box.width * canvas.width / 2}" ry="${frame.box.height * canvas.height / 2}" fill="none" stroke="#00b7ff" stroke-width="3" stroke-dasharray="10 7"/>`);
      } else guides.push(rect(frame.box, canvas, 'fill="none" stroke="#00b7ff" stroke-width="3" stroke-dasharray="10 7"'));
      for (const area of frame.textReserve || []) guides.push(rect(area, canvas, 'fill="#ffd400" fill-opacity="0.18" stroke="#bd8d00"'));
      if (frame.spine) guides.push(rect(frame.spine, canvas, 'fill="#ef3340" fill-opacity="0.22" stroke="#b5121b"'));
      for (const item of frame.critical || []) guides.push(rect(item.box, canvas, 'fill="#75ff62" fill-opacity="0.15" stroke="#178c23"'));
    }
    if (safe) guides.push(rect(safe, canvas, 'fill="none" stroke="#20a840" stroke-width="4"'));
    overlay = path.join(outputDir, `${scope.replace(/[^a-zA-Z0-9_-]/g, "_")}-overlay.svg`);
    fs.writeFileSync(overlay, `<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" width="${canvas.width}" height="${canvas.height}" viewBox="0 0 ${canvas.width} ${canvas.height}">${background}${art.join("")}${guides.join("")}</svg>\n`);
  }
  report.spreads.push({ id: scope, sourceLayout: spread.pageImage || null, overlay });
}

report.status = report.failures.length ? "FAIL" : "PASS";
const section = (title, items, empty) => [`## ${title}`, "", ...(items.length ? items.map(x => `- **${x.scope}** — ${x.message}`) : [`- ${empty}`]), ""];
const lines = ["# Báo cáo Layout QA", "", `- Kết quả: **${report.status}**`, `- Fail: ${report.failures.length}; Warning: ${report.warnings.length}; Pass: ${report.passes.length}; Skipped: ${report.skipped.length}`, "",
  ...section("Fail", report.failures, "Không có."), ...section("Warning", report.warnings, "Không có."),
  ...section("Skipped / N/A", report.skipped, "Không có."), ...section("Pass", report.passes, "Chưa có."),
  "## Overlay", "", ...report.spreads.map(x => `- ${x.id}: ${x.overlay ? `\`${x.overlay}\`` : "không tạo"}`), ""];
fs.writeFileSync(path.join(outputDir, "frame-report.md"), lines.join("\n"));
fs.writeFileSync(path.join(outputDir, "frame-report.json"), `${JSON.stringify(report, null, 2)}\n`);
console.log(`QA ${report.status}: ${report.failures.length} fail, ${report.warnings.length} warning, ${report.skipped.length} skipped.`);
process.exitCode = report.failures.length ? 1 : 0;
