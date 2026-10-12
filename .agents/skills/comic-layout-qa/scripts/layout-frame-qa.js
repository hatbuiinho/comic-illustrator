#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");
const { verify: verifyTextReflow } = require("./verify-text-reflow");

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
      if (meta.width !== canvas.width || meta.height !== canvas.height) warn(`${scope}/layout`, `Kích thước raster ${meta.width}×${meta.height} khác canvas ${canvas.width}×${canvas.height}; overlay sẽ scale.`);
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

  const artworks = spread.artworks || spread.frames || [];
  const legacyFrames = !spread.artworks && Array.isArray(spread.frames);
  for (const frame of artworks) {
    const frameScope = `${scope}/${frame.id || "frame-khong-ten"}`;
    const legacyHardMask = legacyFrames && ["ellipse", "circle", "oval", "irregular"].includes(frame.shape);
    const hardFrame = frame.hardFrame || (legacyHardMask ? frame.box : null);
    const briefRegion = frame.briefRegion || (legacyFrames && !legacyHardMask ? frame.box : null);
    const layoutMode = frame.layoutMode || (!briefRegion && !hardFrame ? "GENERATION_LAYOUT_INTEGRATION" : "GUIDED");
    const placement = frame.placement || hardFrame || { x: 0, y: 0, width: 1, height: 1 };
    const textZones = frame.proposedTextFrames || frame.textZones || frame.textReserve || [];
    const exclusionZones = frame.subjectExclusionZones || textZones;
    const subjects = frame.subjectBounds || frame.critical || [];
    if (briefRegion && !boxValid(briefRegion)) fail(`${frameScope}/briefRegion`, "briefRegion không hợp lệ.");
    else if (briefRegion) pass(`${frameScope}/briefRegion`, "briefRegion hợp lệ và chỉ được dùng làm guide.");
    if (hardFrame) evaluate("hardFrame", frame, spread, frameScope, boxValid(hardFrame), "Hard frame/mask không hợp lệ.", "Hard frame/mask hợp lệ.");
    for (const [index, area] of textZones.entries()) if (!boxValid(area)) fail(`${frameScope}/textZones/${index}`, "Text zone không hợp lệ.");
    for (const [index, area] of exclusionZones.entries()) if (!boxValid(area)) fail(`${frameScope}/subjectExclusionZones/${index}`, "Subject exclusion zone không hợp lệ.");
    if (frame.spine && !boxValid(frame.spine)) fail(`${frameScope}/spine`, "Spine box không hợp lệ.");
    let output = null;
    if (frame.output) {
      const file = resolve(frame.output);
      if (!fs.existsSync(file)) fail(frameScope, `Không tìm thấy output: ${frame.output}`);
      else try {
        const meta = imageSize(file);
        output = { ...meta, uri: dataUri(file, meta.mime) };
        if (hardFrame && boxValid(hardFrame)) {
          const expected = hardFrame.width * canvas.width / (hardFrame.height * canvas.height);
          const actual = meta.width / meta.height;
          const error = Math.abs(actual / expected - 1);
          evaluate("ratio", frame, spread, `${frameScope}/ratio`, error <= (frame.ratioTolerance ?? manifest.defaults?.ratioTolerance ?? 0.015), `Sai tỷ lệ ${(error * 100).toFixed(2)}%.`, `Tỷ lệ khớp, lệch ${(error * 100).toFixed(2)}%.`);
        } else skip(`${frameScope}/ratio`, "ratio: N/A vì artwork không có hard frame/mask.");
        if (frame.contentFrame) warn(`${frameScope}/contentFrame`, "contentFrame là field legacy; không dùng nó làm briefRegion hoặc hard frame khi migrate.");
      } catch (error) { fail(frameScope, error.message); }
    } else warn(frameScope, "Chưa có output; chỉ kiểm guide.");

    for (const critical of subjects) {
      const criticalScope = `${frameScope}/${critical.id || "critical"}`;
      if (!boxValid(critical.box)) { fail(criticalScope, "Critical box không hợp lệ."); continue; }
      if (hardFrame && boxValid(hardFrame)) {
        const inMask = frame.shape === "ellipse"
          ? insideEllipse(hardFrame, critical.box)
          : contains(hardFrame, critical.box);
        evaluate("hardFrame", frame, spread, criticalScope, inMask, "Chi tiết nằm ngoài hard frame/mask.", "Chi tiết nằm trong hard frame/mask.");
      }
      if (safe) evaluate("printSafe", frame, spread, `${criticalScope}/printSafe`, contains(safe, critical.box), "Chi tiết vượt critical-safe.", "Chi tiết nằm trong critical-safe.");
      else if (checkStatus("printSafe", frame, spread) === "REQUIRED") fail(`${criticalScope}/printSafe`, "Thiếu defaults.printTrim.criticalSafePercent.");
      const textHit = exclusionZones.some(area => intersects(critical.box, area));
      evaluate("subjectExclusion", frame, spread, `${criticalScope}/subjectExclusion`, !textHit, "Chủ thể/chi tiết kể chuyện đè vùng chữ.", "Chủ thể/chi tiết kể chuyện không đè vùng chữ.");
      const spineHit = frame.spine && intersects(critical.box, frame.spine);
      evaluate("spine", frame, spread, `${criticalScope}/spine`, !spineHit, "Chi tiết rơi vào gáy.", "Chi tiết không rơi vào gáy.");
    }
    const cleanPreview = frame.layerPackage?.layoutPreview;
    if (cleanPreview && !fs.existsSync(resolve(cleanPreview))) fail(`${frameScope}/layoutPreview`, `Không tìm thấy clean layout preview: ${cleanPreview}`);
    else if (cleanPreview) pass(`${frameScope}/layoutPreview`, "Đã có clean layout preview với chữ thật.");
    const readabilityConfigured = !legacyFrames || frame.textReadability || manifest.defaults?.checks?.textReadability;
    const readabilityPassed = frame.textReadability?.status === "PASS" && frame.textReadability?.evidence;
    if (readabilityConfigured) evaluate("textReadability", frame, spread, `${frameScope}/textReadability`, Boolean(readabilityPassed), "Thiếu kết quả review clean preview hoặc chữ chưa đọc tốt trên background.", "Clean preview xác nhận chữ đọc tốt trên background.");
    else skip(`${frameScope}/textReadability`, "Legacy manifest chưa khai báo textReadability; cần migrate để bật check này.");
    if (["GENERATION_LAYOUT_INTEGRATION", "TEXT_FIRST_AUTO_LAYOUT", "AUTO_LAYOUT"].includes(layoutMode)) {
      const proof = typeof frame.textCapacityProof === "string"
        ? verifyTextReflow(resolve(frame.textCapacityProof))
        : { status: "FAIL", errors: ["Thiếu đường dẫn textCapacityProof; cần bổ sung dữ liệu reflow."] };
      evaluate("textCapacity", frame, spread, `${frameScope}/textCapacity`, proof.status === "PASS", proof.errors.join("; "), "Dữ liệu reflow giữ nguyên chữ, typography và vừa vùng dòng đã xuất.");
      const textIntegrityPassed = frame.textIntegrity?.status === "PASS" && frame.textIntegrity?.evidence;
      const hasReadingOrder = Array.isArray(frame.readingOrder) && frame.readingOrder.length > 0;
      evaluate("textIntegrity", frame, spread, `${frameScope}/textIntegrity`, Boolean(textIntegrityPassed && hasReadingOrder), "Layout chưa chứng minh nguyên văn và thứ tự đọc được giữ.", "Nội dung và thứ tự đọc được giữ sau reflow.");
      if (["GENERATION_LAYOUT_INTEGRATION", "TEXT_FIRST_AUTO_LAYOUT"].includes(layoutMode)) {
        const typographyIntegrityPassed = frame.typographyIntegrity?.status === "PASS" && frame.typographyIntegrity?.evidence;
        const hasTypographyLock = frame.typographyLock && typeof frame.typographyLock === "object";
        evaluate("typographyIntegrity", frame, spread, `${frameScope}/typographyIntegrity`, Boolean(typographyIntegrityPassed && hasTypographyLock), `${layoutMode} thiếu typographyLock hoặc đã thay đổi typography để ép chữ vừa.`, "Typography khớp layout gốc; chỉ text frame và wrap path thay đổi.");
      }
    } else skip(`${frameScope}/textIntegrity`, "textIntegrity: N/A vì layout không dùng auto layout.");
    prepared.push({ frame, output, hardFrame, briefRegion, placement, textZones, exclusionZones, subjects, cleanPreview, layoutMode });
  }

  let overlay = null;
  if (background) {
    const guides = [];
    const art = [];
    for (const { frame, output, hardFrame, briefRegion, placement, textZones, exclusionZones, subjects } of prepared) {
      if (output && legacyFrames && hardFrame && boxValid(frame.contentFrame) && boxValid(frame.box)) {
        const cf = frame.contentFrame;
        const sx = frame.box.width * canvas.width / (cf.width * output.width);
        const sy = frame.box.height * canvas.height / (cf.height * output.height);
        art.push(`<image href="${output.uri}" x="${frame.box.x * canvas.width - cf.x * output.width * sx}" y="${frame.box.y * canvas.height - cf.y * output.height * sy}" width="${output.width * sx}" height="${output.height * sy}" preserveAspectRatio="none" opacity="0.86"/>`);
      } else if (output) art.push(`<image href="${output.uri}" x="${placement.x * canvas.width}" y="${placement.y * canvas.height}" width="${placement.width * canvas.width}" height="${placement.height * canvas.height}" preserveAspectRatio="xMidYMid slice" opacity="0.86"/>`);
      if (hardFrame && frame.shape === "ellipse") {
        guides.push(`<ellipse cx="${(hardFrame.x + hardFrame.width / 2) * canvas.width}" cy="${(hardFrame.y + hardFrame.height / 2) * canvas.height}" rx="${hardFrame.width * canvas.width / 2}" ry="${hardFrame.height * canvas.height / 2}" fill="none" stroke="#00b7ff" stroke-width="3" stroke-dasharray="10 7"/>`);
      } else if (hardFrame) guides.push(rect(hardFrame, canvas, 'fill="none" stroke="#00b7ff" stroke-width="3" stroke-dasharray="10 7"'));
      if (briefRegion) guides.push(rect(briefRegion, canvas, 'fill="#3b82f6" fill-opacity="0.08" stroke="#3b82f6" stroke-dasharray="5 7"'));
      for (const area of textZones) guides.push(rect(area, canvas, 'fill="#ffd400" fill-opacity="0.12" stroke="#bd8d00"'));
      for (const area of exclusionZones) guides.push(rect(area, canvas, 'fill="#ff8c42" fill-opacity="0.08" stroke="#d65a00" stroke-dasharray="8 5"'));
      if (frame.spine) guides.push(rect(frame.spine, canvas, 'fill="#ef3340" fill-opacity="0.22" stroke="#b5121b"'));
      for (const item of subjects) guides.push(rect(item.box, canvas, 'fill="#75ff62" fill-opacity="0.15" stroke="#178c23"'));
    }
    if (safe) guides.push(rect(safe, canvas, 'fill="none" stroke="#20a840" stroke-width="4"'));
    const base = path.join(outputDir, `${scope.replace(/[^a-zA-Z0-9_-]/g, "_")}-overlay`);
    const overlaySvg = `${base}.svg`;
    const overlayPng = `${base}.png`;
    fs.writeFileSync(overlaySvg, `<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" width="${canvas.width}" height="${canvas.height}" viewBox="0 0 ${canvas.width} ${canvas.height}">${background}${art.join("")}${guides.join("")}</svg>\n`);
    const raster = spawnSync("rsvg-convert", ["-o", overlayPng, overlaySvg], { encoding: "utf8" });
    if (raster.status !== 0) fail(`${scope}/overlay`, `Không rasterize được PNG overlay: ${(raster.stderr || "lỗi không rõ").trim()}`);
    else overlay = overlayPng;
    report.spreads.push({ id: scope, sourceLayout: spread.pageImage || null, overlay: overlay ? path.relative(outputDir, overlay) : null, overlaySource: path.relative(outputDir, overlaySvg) });
  }
  if (!background) report.spreads.push({ id: scope, sourceLayout: spread.pageImage || null, overlay: null, overlaySource: null });
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
