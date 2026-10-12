#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { measure, median: measuredMedian } = require('./measure-proxy-typography.js');

const sha256 = file => crypto.createHash("sha256").update(fs.readFileSync(file)).digest("hex");
const attr = (tag, name) => tag.match(new RegExp(`\\b${name}\\s*=\\s*["']([^"']+)["']`, "i"))?.[1] || null;

function resolveArtifact(base, artifact, label, errors) {
  if (!artifact?.path) { errors.push(`Thiếu ${label}.path.`); return null; }
  const file = path.resolve(base, artifact.path);
  if (!fs.existsSync(file)) { errors.push(`${label} không tồn tại: ${artifact.path}.`); return null; }
  if (!/^[a-f0-9]{64}$/i.test(artifact.sha256 || "")) errors.push(`Thiếu ${label}.sha256 hợp lệ.`);
  else if (sha256(file) !== artifact.sha256.toLowerCase()) errors.push(`${label} đã thay đổi sau khi tạo proof (SHA-256 không khớp).`);
  return file;
}

function verify(proofPath) {
  const absoluteProof = path.resolve(proofPath);
  const base = path.dirname(absoluteProof);
  const proof = JSON.parse(fs.readFileSync(absoluteProof, "utf8"));
  const burdenErrors = [], layoutErrors = [], artifactErrors = [], warnings = [];
  const artDirected = proof.layoutComparison === "ART_DIRECTED";
  const rhythmIssues = artDirected ? warnings : layoutErrors;
  const metrics = { regions: {} };
  const thresholds = { minReadableScaleRatio: 0.95, maxLineCountDelta: 1, ...(proof.thresholds || {}) };

  if (!["TEXT_PROXY_INTEGRATION", "BAKED_TEXT_PROXY_CONCEPT"].includes(proof.contract)) burdenErrors.push("contract proxy không hợp lệ.");
  if (proof.spatialComparisonIgnored !== true) burdenErrors.push("Phải ghi spatialComparisonIgnored=true; fidelity không khóa tọa độ chữ.");
  if (Number(proof.schemaVersion) < 4) artifactErrors.push("Cần proxyFidelityProof schemaVersion 4 với typography đo trực tiếp; schema cũ không mở gate.");

  const sourceFile = resolveArtifact(base, proof.artifacts?.source, "artifacts.source", artifactErrors);
  const svgFile = resolveArtifact(base, proof.artifacts?.semanticSvg, "artifacts.semanticSvg", artifactErrors);
  resolveArtifact(base, proof.artifacts?.preview, "artifacts.preview", artifactErrors);
  if (sourceFile && proof.artifacts.source.page === undefined) artifactErrors.push("artifacts.source.page phải chỉ rõ trang PDF/layout được đo.");

  const sourceRegions = Array.isArray(proof.sourceTextRegions) ? proof.sourceTextRegions : [];
  const proxyRegions = Array.isArray(proof.proxyTextRegions) ? proof.proxyTextRegions : [];
  if (!sourceRegions.length) burdenErrors.push("sourceTextRegions phải chứa mọi occurrence chữ nhìn thấy trên spread.");
  if (!proxyRegions.length) burdenErrors.push("proxyTextRegions phải ánh xạ từng occurrence nguồn sang artifact.");
  const sourceIds = new Set(), mapped = new Map();
  for (const region of sourceRegions) {
    if (!region?.id || sourceIds.has(region.id)) burdenErrors.push(`sourceTextRegions có ID thiếu hoặc trùng: ${region?.id || "(trống)"}.`);
    else sourceIds.add(region.id);
    if (!(Number(region.lineCount) > 0)) burdenErrors.push(`Source region ${region?.id || "?"} thiếu lineCount.`);
    if (!(Number(region.medianGlyphHeightPt) > 0)) burdenErrors.push(`Source region ${region?.id || "?"} thiếu medianGlyphHeightPt.`);
  }
  for (const region of proxyRegions) {
    if (!region?.sourceRegionId || !sourceIds.has(region.sourceRegionId)) burdenErrors.push(`Proxy region ${region?.id || "?"} tham chiếu sourceRegionId không hợp lệ.`);
    mapped.set(region.sourceRegionId, (mapped.get(region.sourceRegionId) || 0) + 1);
  }
  for (const id of sourceIds) if ((mapped.get(id) || 0) !== 1) burdenErrors.push(`Source text occurrence ${id} phải được biểu diễn đúng một lần; hiện có ${mapped.get(id) || 0}.`);

  if (svgFile) {
    const svg = fs.readFileSync(svgFile, "utf8");
    for (const proxyRegion of proxyRegions) {
      const groupId = proxyRegion.svgGroupId;
      if (!groupId) { layoutErrors.push(`Proxy region ${proxyRegion.id || "?"} thiếu svgGroupId.`); continue; }
      const escaped = String(groupId).replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
      const groupMatch = svg.match(new RegExp(`<g\\b(?=[^>]*\\bid=["']${escaped}["'])[^>]*>([\\s\\S]*?)<\\/g>`, "i"));
      if (!groupMatch) { layoutErrors.push(`Không tìm thấy SVG group ${groupId}.`); continue; }
      const openTag = groupMatch[0].match(/^<g\b[^>]*>/i)?.[0] || "";
      const renderKind = attr(openTag, "data-render-kind");
      if (!["source-text-layer", "rendered-placeholder-text"].includes(renderKind)) layoutErrors.push(`SVG group ${groupId} phải là source-text-layer hoặc rendered-placeholder-text; abstract bars không đủ điều kiện review.`);
      const texts = [...groupMatch[1].matchAll(/<text\b[^>]*>/gi)].map(m => m[0]);
      if (!texts.length) { layoutErrors.push(`SVG group ${groupId} không có glyph/text render thật.`); continue; }
      const sourceRegion = sourceRegions.find(region => region.id === proxyRegion.sourceRegionId);
      metrics.regions[proxyRegion.sourceRegionId] = { declaredSvgTextCount: texts.length };
      // Nominal SVG sizes are not glyph measurements. Canonical PDF render below
      // measures font, glyph bounds, leading and burden in the same units.
      if (!artDirected && sourceRegion && Math.abs(texts.length - Number(sourceRegion.lineCount)) > thresholds.maxLineCountDelta) layoutErrors.push(`Region ${proxyRegion.sourceRegionId} có ${texts.length} dòng render, lệch quá ${thresholds.maxLineCountDelta} so với ${sourceRegion.lineCount} dòng nguồn.`);
    }
  }

  if (sourceFile && svgFile) {
    try {
      const measured = measure(svgFile, sourceFile, proof.artifacts.source.page, sourceRegions, proxyRegions, proof.renderEnvironment);
      metrics.canvasScale = measured.scale;
      for (const region of sourceRegions) {
        const m = measured.regions[region.id]; if (!m) continue;
        metrics.regions[region.id] = m;
        const a=m.source,b=m.rendered;
        for (const [key,min,max] of [['fontSizePt',.95,1.05],['glyphHeightPt',.90,1.15],['leadingPt',.95,1.10],['textAreaPt2',.90,1.20],['blockHeightPt',.90,1.20]]) {
          const ratio=b[key]/a[key];m[key+'Ratio']=ratio;
          if (!(a[key]>0) || !Number.isFinite(ratio) || ratio<min || ratio>max) (artDirected && ['textAreaPt2','blockHeightPt'].includes(key) ? warnings : layoutErrors).push(`Region ${region.id}: ${key} bị thu nhỏ/phóng lớn hoặc thiếu đo (${ratio.toFixed(3)}; cho phép ${min}–${max}).`);
        }
        const widths=measuredMedian(b.lineWidthsPt)/measuredMedian(a.lineWidthsPt);m.lineWidthRatio=widths;
        if(!Number.isFinite(widths)||widths<.85||widths>1.20)rhythmIssues.push(`Region ${region.id}: phân bố độ dài dòng lệch (${widths.toFixed(3)}).`);
        if(a.lineCount!==Number(region.lineCount))burdenErrors.push(`Region ${region.id}: lineCount khai báo không khớp PDF đo trực tiếp.`);
        if(b.lineCount!==m.svgTextCount || (!artDirected && Math.abs(a.lineCount-b.lineCount)>thresholds.maxLineCountDelta))burdenErrors.push(`Region ${region.id}: dòng render bị mất, chồng hoặc lệch lượng nguồn.`);
        if(artDirected){const ratio=b.contentUnits/a.contentUnits;m.contentUnitsRatio=ratio;
          if(!Number.isFinite(ratio)||ratio<.90||ratio>1.10)burdenErrors.push(`Region ${region.id}: lượng nội dung đại diện bị mất/thêm (${ratio.toFixed(3)}).`);}
        const actualOrder=[...new Set(m.paragraphIds)];
        if(!Array.isArray(region.paragraphOrder)||JSON.stringify(actualOrder)!==JSON.stringify(region.paragraphOrder))layoutErrors.push(`Region ${region.id}: paragraph order thiếu/sai.`);
        if(!Array.isArray(region.paragraphLineCounts)||region.paragraphLineCounts.length!==actualOrder.length||region.paragraphLineCounts.reduce((x,y)=>x+y,0)!==a.lineCount)layoutErrors.push(`Region ${region.id}: thiếu paragraphLineCounts khớp nguồn.`);
        else {
          let sourceOffset=0,proxyOffset=0;
          for(let i=0;i<actualOrder.length;i++) {
            const n=m.paragraphIds.filter(v=>v===actualOrder[i]).length;
            if(Math.abs(n-region.paragraphLineCounts[i])>1)rhythmIssues.push(`Region ${region.id}: nhịp dòng đoạn ${actualOrder[i]} lệch nguồn.`);
            if(i>0){const gapSource=a.lineTopsPt[sourceOffset]-a.lineTopsPt[sourceOffset-1],gapProxy=b.lineTopsPt[proxyOffset]-b.lineTopsPt[proxyOffset-1],ratio=gapProxy/gapSource;
              if(!Number.isFinite(ratio)||ratio<.90||ratio>1.15)rhythmIssues.push(`Region ${region.id}: khoảng nghỉ trước đoạn ${actualOrder[i]} lệch (${ratio.toFixed(3)}).`);}
            sourceOffset+=region.paragraphLineCounts[i];proxyOffset+=n;
          }
          const runs=m.paragraphIds.filter((v,i,a)=>!i||v!==a[i-1]);
          if(JSON.stringify(runs)!==JSON.stringify(actualOrder))layoutErrors.push(`Region ${region.id}: một đoạn bị chia thành các vùng không liên tục.`);
        }
      }
    } catch(error) { artifactErrors.push(`Thiếu bằng chứng typography đo trực tiếp: ${error.message}`); }
  }

  for (const field of ["readingContinuity", "readability", "paragraphRhythmReview", "typesettingFeasibility", "wrapReview"]) if (proof[field] !== "PASS") layoutErrors.push(`${field} phải PASS.`);
  const ready = !burdenErrors.length && !layoutErrors.length && !artifactErrors.length;
  return { status: ready ? "PROXY_COMPOSITION_PASS" : "LAYOUT_COMPOSITION_NEEDS_REVISION", gates: { burden: burdenErrors.length ? "FAIL" : "PROXY_BURDEN_PASS", layout: layoutErrors.length || artifactErrors.length ? "FAIL" : "PROXY_LAYOUT_PASS", artifactBinding: artifactErrors.length ? "FAIL" : "ARTIFACT_BINDING_PASS" }, metrics, thresholds, layoutComparison: artDirected ? "ART_DIRECTED" : "SOURCE_RHYTHM", warnings, artisticApproval: "NOT_EVALUATED_BY_SCRIPT", spatialComparisonIgnored: true, errors: { burden: burdenErrors, layout: layoutErrors, artifact: artifactErrors } };
}

if (require.main === module) {
  const proofArg = process.argv[2];
  if (!proofArg || ["-h", "--help"].includes(proofArg)) { console.log("Usage: node verify-proxy-fidelity.js <proxy-fidelity-proof.json>"); process.exit(proofArg ? 0 : 2); }
  try { const result = verify(proofArg); console.log(JSON.stringify(result, null, 2)); process.exit(result.status === "PROXY_COMPOSITION_PASS" ? 0 : 1); }
  catch (error) { console.error(JSON.stringify({ status: "LAYOUT_COMPOSITION_NEEDS_REVISION", error: error.message }, null, 2)); process.exit(1); }
}

module.exports = { verify };
