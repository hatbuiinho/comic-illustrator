#!/usr/bin/env node
/*
 * Layout-frame QA — dependency-free geometry checks plus SVG review overlays.
 *
 * Usage:
 *   node layout-frame-qa.js <manifest.json> [output-directory]
 *
 * Coordinates in the manifest are normalised (0..1), relative to the spread.
 * The script deliberately does not try to recognise a character or an object.
 * Put every face, hand, prop, or other critical story element in `critical` so
 * its position can be checked against the frame mask, text reserve and gutter.
 */

const fs = require("fs");
const path = require("path");

const [manifestArg, outputArg] = process.argv.slice(2);
if (!manifestArg || manifestArg === "--help" || manifestArg === "-h") {
  console.log("Usage: node layout-frame-qa.js <manifest.json> [output-directory]");
  process.exit(manifestArg ? 0 : 2);
}

const manifestPath = path.resolve(manifestArg);
const manifestDir = path.dirname(manifestPath);
const outputDir = path.resolve(outputArg || path.join(manifestDir, "..", "qa"));
const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
const tolerance = manifest.defaults?.ratioTolerance ?? 0.015;
const report = { manifest: manifestPath, failures: [], warnings: [], passes: [], optionAlignment: [], spreads: [] };

function resolve(file) {
  return path.resolve(manifestDir, file);
}
function fail(scope, message) { report.failures.push({ scope, message }); }
function warn(scope, message) { report.warnings.push({ scope, message }); }
function pass(scope, message) { report.passes.push({ scope, message }); }
function n(value) { return Number(value.toFixed(4)); }
function boxValid(box) {
  return box && [box.x, box.y, box.width, box.height].every(Number.isFinite) &&
    box.x >= 0 && box.y >= 0 && box.width > 0 && box.height > 0 &&
    box.x + box.width <= 1 && box.y + box.height <= 1;
}
function frameBoxValid(frame) {
  const box = frame?.box;
  if (!box || ![box.x, box.y, box.width, box.height].every(Number.isFinite) ||
      box.x < 0 || box.y < 0 || box.width <= 0 || box.height <= 0 || box.x + box.width > 1) return false;
  return frame.bleedBottom === true ? box.y + box.height <= 1.15 : box.y + box.height <= 1;
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
function insetBox(horizontal, vertical) {
  return { x: horizontal, y: vertical, width: 1 - horizontal * 2, height: 1 - vertical * 2 };
}
function formatPercent(lock, key) {
  return `x ${(lock[key].x * 100).toFixed(3)}% · y ${(lock[key].y * 100).toFixed(3)}%`;
}
function printGeometry(scope) {
  const lock = manifest.defaults?.printTrim;
  const required = ["trimPercent", "criticalSafePercent"];
  const validPair = value => value && Number.isFinite(value.x) && Number.isFinite(value.y);
  if (!lock || required.some(key => !validPair(lock[key]))) {
    fail(`${scope}/printTrimLock`, `Thiếu defaults.printTrim hoặc trường bắt buộc: ${required.join(", ")} (mỗi trường cần x và y).`);
    return null;
  }
  const trim = lock.trimPercent;
  const safe = lock.criticalSafePercent;
  if (trim.x <= 0 || trim.y <= 0 || safe.x < trim.x || safe.y < trim.y || safe.x * 2 >= 1 || safe.y * 2 >= 1) {
    fail(`${scope}/printTrimLock`, "printTrim không hợp lệ: tỷ lệ phải dương, critical-safe không nhỏ hơn trim và nhỏ hơn nửa vùng kiểm tra.");
    return null;
  }
  const trimBox = insetBox(trim.x, trim.y);
  const safeBox = insetBox(safe.x, safe.y);
  pass(`${scope}/printTrimLock`, `Trim ${formatPercent(lock, "trimPercent")}; critical-safe ${formatPercent(lock, "criticalSafePercent")}.`);
  return { lock, trim: trimBox, safe: safeBox };
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
  // PNG
  if (data.subarray(0, 8).equals(Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]))) {
    return { width: data.readUInt32BE(16), height: data.readUInt32BE(20), mime: "image/png" };
  }
  // JPEG: find a Start Of Frame marker.
  if (data[0] === 0xff && data[1] === 0xd8) {
    for (let i = 2; i < data.length - 9; i += 1) {
      if (data[i] === 0xff && data[i + 1] >= 0xc0 && data[i + 1] <= 0xc3) {
        return { width: data.readUInt16BE(i + 5), height: data.readUInt16BE(i + 7), mime: "image/jpeg" };
      }
    }
  }
  throw new Error("Only PNG and JPEG are supported by this dependency-free checker.");
}
function asDataUri(file, mime) {
  return `data:${mime};base64,${fs.readFileSync(file).toString("base64")}`;
}
function svgBox(box, canvas, attributes = "") {
  return `<rect x="${box.x * canvas.width}" y="${box.y * canvas.height}" width="${box.width * canvas.width}" height="${box.height * canvas.height}" ${attributes}/>`;
}
function maskShape(frame, canvas) {
  const b = frame.box;
  if (frame.shape === "ellipse") {
    return `<ellipse cx="${(b.x + b.width / 2) * canvas.width}" cy="${(b.y + b.height / 2) * canvas.height}" rx="${b.width * canvas.width / 2}" ry="${b.height * canvas.height / 2}"/>`;
  }
  return svgBox(b, canvas);
}
function frameClip(frame, canvas, id) {
  return `<clipPath id="${id}">${maskShape(frame, canvas)}</clipPath>`;
}
function makeOverlay(spread, prepared, background, print) {
  const c = spread.canvas || { width: 1410, height: 1000 };
  const defs = [];
  const art = [];
  const guides = [];
  guides.push(svgBox(print.trim, c, "fill=\"none\" stroke=\"#e02020\" stroke-width=\"4\""));
  guides.push(svgBox(print.safe, c, "fill=\"none\" stroke=\"#20a840\" stroke-width=\"4\""));
  guides.push(`<text x="${(print.trim.x + 0.006) * c.width}" y="${(print.trim.y + 0.025) * c.height}" fill="#b31515" font-family="sans-serif" font-size="16">TRIM ${formatPercent(print.lock, "trimPercent")}</text>`);
  guides.push(`<text x="${(print.safe.x + 0.006) * c.width}" y="${(print.safe.y + 0.025) * c.height}" fill="#137b2b" font-family="sans-serif" font-size="16">CRITICAL SAFE ${formatPercent(print.lock, "criticalSafePercent")}</text>`);
  for (const item of prepared) {
    const { frame, output } = item;
    const clipId = `clip-${spread.id}-${frame.id}`.replace(/[^a-zA-Z0-9_-]/g, "_");
    defs.push(frameClip(frame, c, clipId));
    if (output?.uri) {
      if (boxValid(frame.contentFrame)) {
        const cf = frame.contentFrame;
        const sx = frame.box.width * c.width / (cf.width * output.width);
        const sy = frame.box.height * c.height / (cf.height * output.height);
        const x = frame.box.x * c.width - cf.x * output.width * sx;
        const y = frame.box.y * c.height - cf.y * output.height * sy;
        art.push(`<image href="${output.uri}" x="${x}" y="${y}" width="${output.width * sx}" height="${output.height * sy}" preserveAspectRatio="none" clip-path="url(#${clipId})" opacity="0.86"/>`);
      } else {
        art.push(`<image href="${output.uri}" x="${frame.box.x * c.width}" y="${frame.box.y * c.height}" width="${frame.box.width * c.width}" height="${frame.box.height * c.height}" preserveAspectRatio="xMidYMid slice" clip-path="url(#${clipId})" opacity="0.86"/>`);
      }
    }
    guides.push(maskShape(frame, c).replace("/>", ` fill="none" stroke="#00b7ff" stroke-width="3" stroke-dasharray="10 7"/>`));
    guides.push(`<text x="${(frame.box.x + 0.01) * c.width}" y="${(frame.box.y + 0.025) * c.height}" fill="#006a96" font-family="sans-serif" font-size="18">${frame.id}</text>`);
    for (const area of frame.textReserve || []) {
      guides.push(svgBox(area, c, "fill=\"#ffd400\" fill-opacity=\"0.18\" stroke=\"#bd8d00\" stroke-width=\"2\""));
    }
    if (frame.spine) {
      guides.push(svgBox(frame.spine, c, "fill=\"#ef3340\" fill-opacity=\"0.22\" stroke=\"#b5121b\" stroke-width=\"2\""));
    }
    for (const critical of frame.critical || []) {
      guides.push(svgBox(critical.box, c, "fill=\"#75ff62\" fill-opacity=\"0.15\" stroke=\"#178c23\" stroke-width=\"2\""));
      guides.push(`<text x="${(critical.box.x + 0.003) * c.width}" y="${(critical.box.y + 0.018) * c.height}" fill="#126d1b" font-family="sans-serif" font-size="15">${critical.id}</text>`);
    }
  }
  return `<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="${c.width}" height="${c.height}" viewBox="0 0 ${c.width} ${c.height}"><defs>${defs.join("")}</defs>${background}${art.join("")}${guides.join("")}</svg>\n`;
}

if (!Array.isArray(manifest.spreads) || manifest.spreads.length === 0) {
  fail("manifest", "Cần ít nhất một spread trong mảng spreads.");
}

fs.mkdirSync(outputDir, { recursive: true });
for (const spread of manifest.spreads || []) {
  const scope = spread.id || "spread-không-tên";
  const canvas = spread.canvas || { width: 1410, height: 1000 };
  if (!Number.isFinite(canvas.width) || !Number.isFinite(canvas.height) || canvas.width <= 0 || canvas.height <= 0) {
    fail(scope, "canvas.width và canvas.height phải là số dương.");
    continue;
  }
  const print = printGeometry(scope);
  let overlayBackground = null;
  if (typeof spread.pageImage !== "string" || !spread.pageImage.trim()) {
    fail(`${scope}/layoutQa`, "Thiếu pageImage: overlay QA bắt buộc dùng raster của chính layout gốc có text; cấm fallback nền trắng.");
  } else {
    const pageImageFile = resolve(spread.pageImage);
    if (!fs.existsSync(pageImageFile)) {
      fail(`${scope}/layoutQa`, `Không tìm thấy layout gốc: ${spread.pageImage}. Không tạo overlay nền thay thế.`);
    } else {
      try {
        const meta = imageSize(pageImageFile);
        overlayBackground = `<image href="${asDataUri(pageImageFile, meta.mime)}" width="${canvas.width}" height="${canvas.height}" preserveAspectRatio="none"/>`;
        pass(`${scope}/layoutQa`, `Đã dùng layout gốc có text làm nền overlay: ${spread.pageImage}.`);
      } catch (error) {
        fail(`${scope}/layoutQa`, `Không đọc được layout gốc ${spread.pageImage}: ${error.message}. Không tạo overlay nền thay thế.`);
      }
    }
  }
  const prepared = [];
  for (const frame of spread.frames || []) {
    const frameScope = `${scope}/${frame.id || "frame-không-tên"}`;
    // Page packages may keep storyboard/delivery in an option manifest. Merge
    // those fields for QA without copying page context into the layout file.
    let optionData = {};
    if (frame.optionManifest) {
      const optionPath = resolve(frame.optionManifest);
      if (fs.existsSync(optionPath)) {
        try { optionData = JSON.parse(fs.readFileSync(optionPath, "utf8")); }
        catch (error) { fail(frameScope, `Không đọc được optionManifest: ${error.message}`); }
      } else fail(frameScope, `Không tìm thấy optionManifest: ${frame.optionManifest}`);
    }
    const alignment = optionData.optionAlignment || frame.optionAlignment;
    const confirmed = alignment?.userConfirmed === true;
    const delivery = frame.delivery || optionData.delivery;
    if (!alignment) {
      warn(frameScope, "Chưa có optionAlignment; không được coi frame mới là brief đã được người dùng chốt.");
    } else {
      const alignmentScope = `${frameScope}/optionAlignment`;
      const requiredText = ["optionId", "selectedBrief"];
      const requiredLists = ["mustMatch", "forbidden", "layoutMapping", "sourceRead", "alignmentRationale"];
      const missing = [
        ...requiredText.filter(key => typeof alignment[key] !== "string" || !alignment[key].trim()),
        ...requiredLists.filter(key => !Array.isArray(alignment[key]) || alignment[key].length === 0)
      ];
      if (missing.length) fail(alignmentScope, `Thiếu trường bắt buộc: ${missing.join(", ")}.`);
      if (Array.isArray(alignment.sourceRead)) {
        const hasNotes = alignment.sourceRead.some(x => /(^|\/)notes\.md$/i.test(String(x)));
        const hasShotNotes = alignment.sourceRead.some(x => /(^|\/)shot_notes\.md$/i.test(String(x)));
        if (!hasNotes || !hasShotNotes) {
          fail(alignmentScope, "sourceRead phải có cả notes.md và shot_notes.md của đúng tập.");
        }
      }
      if (Array.isArray(alignment.alignmentRationale)) {
        alignment.alignmentRationale.forEach((item, index) => {
          const rationaleScope = `${alignmentScope}/alignmentRationale[${index}]`;
          const valid = item && ["optionRequirement", "manifestEvidence", "whyMatch"]
            .every(key => typeof item[key] === "string" && item[key].trim());
          if (!valid) fail(rationaleScope, "Mỗi rationale cần optionRequirement, manifestEvidence và whyMatch.");
        });
      }
      if (alignment.userConfirmed !== true) fail(alignmentScope, "Chưa có xác nhận userConfirmed: true cho Option-to-manifest QA.");
      else pass(alignmentScope, `Option ${alignment.optionId || "(không mã)"} đã được người dùng xác nhận.`);
      report.optionAlignment.push({ scope: alignmentScope, optionId: alignment.optionId, userConfirmed: alignment.userConfirmed === true, missing });
    }
    if (confirmed) {
      if (!delivery || delivery.required !== true || typeof delivery.status !== "string" || typeof delivery.output !== "string") {
        fail(`${frameScope}/delivery`, "Frame đã được user xác nhận phải có delivery.required, delivery.status và delivery.output.");
      } else {
        if (["approved", "generating", "interrupted", "generated-unfiled"].includes(delivery.status)) {
          fail(`${frameScope}/delivery`, `Delivery chưa hoàn tất (status: ${delivery.status}).`);
        }
        const frameOutput = frame.output || delivery.output;
        if (frameOutput !== delivery.output) fail(`${frameScope}/delivery`, "frame.output phải khớp delivery.output sau khi user xác nhận.");
      }
    }
    if (!frameBoxValid(frame)) { fail(frameScope, "box không hợp lệ; chỉ ellipse có bleedBottom mới được vượt đáy spread tối đa 15%."); continue; }
    if (!["rect", "ellipse"].includes(frame.shape || "rect")) fail(frameScope, "shape chỉ nhận rect hoặc ellipse.");
    const expectedRatio = frame.box.width * canvas.width / (frame.box.height * canvas.height);
    let output;
    if (!frame.output) {
      if (confirmed) fail(frameScope, "Frame đã được user xác nhận nhưng chưa có output.");
      else warn(frameScope, "Chưa có output; overlay chỉ hiển thị frame và guide.");
    } else {
      const file = resolve(frame.output);
      if (!fs.existsSync(file)) {
        fail(frameScope, `Không tìm thấy output: ${frame.output}`);
      } else {
        try {
          const meta = imageSize(file);
          const contentFrame = frame.contentFrame;
          if (contentFrame && !boxValid(contentFrame)) fail(frameScope, "contentFrame phải là box chuẩn hoá nằm hoàn toàn trong output.");
          const actualRatio = boxValid(contentFrame)
            ? (contentFrame.width * meta.width) / (contentFrame.height * meta.height)
            : meta.width / meta.height;
          const error = Math.abs(actualRatio / expectedRatio - 1);
          output = { ...meta, uri: asDataUri(file, meta.mime) };
          if (error > (frame.ratioTolerance ?? tolerance)) {
            fail(frameScope, `Sai tỷ lệ: ảnh ${n(actualRatio)}, frame ${n(expectedRatio)} (lệch ${(error * 100).toFixed(2)}%).`);
          } else {
            pass(frameScope, `${boxValid(contentFrame) ? "Tỷ lệ contentFrame" : "Tỷ lệ output"} khớp frame (${(error * 100).toFixed(2)}% lệch).`);
          }
        } catch (error) { fail(frameScope, error.message); }
      }
    }
    for (const area of [...(frame.textReserve || []), ...(frame.spine ? [frame.spine] : [])]) {
      if (!boxValid(area)) fail(frameScope, "textReserve/spine phải là box chuẩn hoá nằm trong spread.");
    }
    for (const critical of frame.critical || []) {
      const criticalScope = `${frameScope}/${critical.id || "critical-không-tên"}`;
      if (!boxValid(critical.box)) { fail(criticalScope, "critical.box không hợp lệ."); continue; }
      const contained = frame.shape === "ellipse" ? insideEllipse(frame.box, critical.box) : contains(frame.box, critical.box);
      if (!contained) fail(criticalScope, "Chi tiết quan trọng nằm ngoài frame/mask.");
      if (print && !contains(print.safe, critical.box)) {
        fail(criticalScope, `Chi tiết quan trọng vượt critical-safe (${formatPercent(print.lock, "criticalSafePercent")}) và có nguy cơ bị xén.`);
      }
      for (const area of frame.textReserve || []) if (intersects(critical.box, area)) fail(criticalScope, "Chi tiết quan trọng đè lên vùng chữ.");
      if (frame.spine && intersects(critical.box, frame.spine)) fail(criticalScope, "Chi tiết quan trọng rơi vào gáy sách.");
    }
    prepared.push({ frame, output });
  }
  if (overlayBackground && print) {
    const overlay = path.join(outputDir, `${scope.replace(/[^a-zA-Z0-9_-]/g, "_")}-overlay.svg`);
    fs.writeFileSync(overlay, makeOverlay(spread, prepared, overlayBackground, print));
    report.spreads.push({ id: scope, overlay, frames: prepared.length, sourceLayout: spread.pageImage });
  } else {
    report.spreads.push({ id: scope, overlay: null, frames: prepared.length, sourceLayout: spread.pageImage || null });
  }
}

const lines = [
  "# Layout frame QA report", "",
  `- Manifest: \`${manifestPath}\``,
  `- Kết quả: **${report.failures.length ? "FAIL" : "PASS"}**`,
  `- Fail: ${report.failures.length}; Warning: ${report.warnings.length}; Pass: ${report.passes.length}`, "",
  "## Fail", "", ...(report.failures.length ? report.failures.map(x => `- **${x.scope}** — ${x.message}`) : ["- Không có."]),
  "", "## Warning", "", ...(report.warnings.length ? report.warnings.map(x => `- **${x.scope}** — ${x.message}`) : ["- Không có."]),
  "", "## Pass", "", ...(report.passes.length ? report.passes.map(x => `- **${x.scope}** — ${x.message}`) : ["- Chưa có frame output để kiểm tra."]),
  "", "## Overlay", "", ...report.spreads.map(x => x.overlay
    ? `- ${x.id}: \`${x.overlay}\` (source layout: \`${x.sourceLayout}\`)`
    : `- ${x.id}: không tạo — source layout thiếu hoặc không đọc được.`), ""
];
fs.writeFileSync(path.join(outputDir, "frame-report.md"), lines.join("\n"));
fs.writeFileSync(path.join(outputDir, "frame-report.json"), JSON.stringify(report, null, 2) + "\n");
console.log(`QA ${report.failures.length ? "FAIL" : "PASS"}: ${report.failures.length} fail, ${report.warnings.length} warning. Report: ${path.join(outputDir, "frame-report.md")}`);
process.exitCode = report.failures.length ? 1 : 0;
