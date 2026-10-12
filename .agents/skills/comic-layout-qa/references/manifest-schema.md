# Manifest layout QA

Tọa độ `x`, `y`, `width`, `height` chuẩn hóa 0..1 theo spread.

```json
{
  "defaults": {
    "ratioTolerance": 0.015,
    "printTrim": {
      "trimPercent": { "x": 0.0104895, "y": 0.0147783 },
      "criticalSafePercent": { "x": 0.027972, "y": 0.0394089 }
    },
    "checks": {
      "hardFrame": "NOT_APPLICABLE",
      "ratio": "NOT_APPLICABLE",
      "subjectExclusion": "REQUIRED",
      "textReadability": "REQUIRED",
      "textIntegrity": "REQUIRED",
      "typographyIntegrity": "REQUIRED",
      "printSafe": "REQUIRED",
      "spine": "REQUIRED"
    }
  },
  "overrides": {
    "spine": {
      "status": "SKIPPED_BY_USER",
      "reason": "Người dùng yêu cầu không cần tránh gáy",
      "scope": "deliverable hiện tại"
    }
  },
  "spreads": []
}
```

Mỗi spread cần `id`, `canvas`, `pageImage`, `artworks`. Mỗi artwork có thể gồm:

- `briefRegion`: vùng xanh/brief chỉ dùng làm guide, không tạo FAIL;
- `layoutMode`: `GUIDED` hoặc `GENERATION_LAYOUT_INTEGRATION`; tự dùng
  `GENERATION_LAYOUT_INTEGRATION` khi không có `briefRegion` lẫn `hardFrame`;
  chấp nhận `TEXT_FIRST_AUTO_LAYOUT` như alias legacy khi đọc manifest cũ nhưng
  không phát sinh mode này cho artifact mới;
- `hardFrame`: frame hoặc mask thật; chỉ field này mới giới hạn artwork;
- `placement`: vị trí master trên canvas trang/spread;
- `output`: raw candidate hoặc full-page master theo trạng thái workflow;
- `textZones`: vùng chữ thật;
- `typographyLock`: font family/style/size, leading, tracking, scale,
  paragraph/inline style, màu và highlight lấy từ layout gốc;
- `textIntegrationContract`: `FINAL_TEXT_REFLOW`, `TEXT_PROXY_INTEGRATION` hoặc
  `BAKED_TEXT_PROXY_CONCEPT`;
- Với `TEXT_PROXY_INTEGRATION`: `proxyTextPlan`, `productionLayoutProxy`,
  `backgroundValueMap`, `detailDensityMap`, `integrationEdgeMap`,
  `glyphPressureMap`, `integrationModes`,
  `textIntegrationStatus: PROXY_COMPOSITION_PASS` và
  `exactTextCapacity: DEFERRED_TO_INDESIGN`;
- Với `BAKED_TEXT_PROXY_CONCEPT`: các field proxy ở trên cùng
  `bakedProxyGenerationReference`, `textFootprint`, `interactionEdges`,
  `proxyRemovalMask`, `repairContextRing`, `protectedArtworkMask`,
  `indesignTextFootprint`, `integratedTextConcept`, `cleanArtworkMaster`,
  `cleanPlateProof`; trước delivery cần cả `INTEGRATED_CONCEPT_PASS` và
  `CLEAN_PLATE_PASS`;
- `allowedTextMutations`: chỉ text-frame geometry, column width, line break do
  reflow và wrap path;
- Với `FINAL_TEXT_REFLOW`, `typographyLock`, `allowedTextMutations`, `provisionalTextFlowEnvelope` và
  `textCapacityProof` cho từng option ở shot design; chỉ option có
  `textIntegrationStatus: REFLOW_PREFLIGHT_PASS` mới được trình chọn; sau khi
  chọn mới tinh chỉnh `textFlowEnvelope`, `knockoutContour`, `overlapPlan` và
  `readingOrder` trong `generationLayoutPlan`;
- `textKnockoutMask`: `WHITE_OPAQUE` khi preview phải che hoàn toàn background
  dưới chữ; giá trị này chỉ quy định độ che, không quy định mask là hình hộp;
- `textFlowEnvelope`: contour dàn chữ, điểm co giãn và text capacity được chứng
  minh sau khi khóa composition, ngay trước generation;
- `artDirectionReview`: bằng chứng cụ thể cho visual thesis, figure–ground,
  rhythm, eye path và page character trên clean preview;
- `selectedPageComposition`: shot composition đã được người dùng chọn; có
  text proxy khi contract là `BAKED_TEXT_PROXY_CONCEPT`;
- `generationLayoutPlan`: text flow, knockout, overlap, reading order và
  typography lock được art-direct quanh shot đã chọn;
- `sceneExtentPlan`: footprint cảnh nhìn thấy, lý do kể chuyện, context evidence
  cần giữ, vùng giấy chủ ý và biên hòa; kế thừa từ composition, không suy từ canvas;
- `flattenedPageCandidate`: raw output render theo composition đã khóa;
- `pageConceptPreview`: candidate được ghép integration treatment và lớp chữ
  ngoài model — typography gốc hoặc proxy theo contract;
- `visibleArtLockMask` và `expandMask`: vùng pixel bất biến và vùng duy nhất được
  phép phục dựng sau `SELECTED_FOR_LAYOUT`;
- `subjectExclusionZones`: vùng nhân vật, cử chỉ và đạo cụ kể chuyện không được
  giao; thường bằng text zone cộng khoảng đệm;
- `subjectBounds`: hộp hoặc silhouette của chủ thể dùng kiểm giao vùng chữ;
- `wrapPath`: đường text wrap sau `SELECTED_FOR_LAYOUT`;
- `layerPackage`: đường dẫn `master`, `bg`, `mgfg`, `wrap` và clean preview,
  tất cả cùng version/canvas/điểm gốc;
- `spine`, `critical` và override `checks` khi áp dụng.

Manifest cũ có `contentFrame` là legacy. Không chuyển nó sang `hardFrame` nếu
nguồn chỉ cho biết đó là khối xanh/brief. Khi migrate, đổi thành `briefRegion`
và đặt artwork theo toàn canvas layout.

Trạng thái hợp lệ: `REQUIRED`, `NOT_APPLICABLE`, `SKIPPED_BY_USER`.

Trong `GENERATION_LAYOUT_INTEGRATION`, hard lock chữ phụ thuộc contract.
`FINAL_TEXT_REFLOW` khóa content, reading order và typography. Với
`TEXT_PROXY_INTEGRATION`, chỉ khóa reserve, density, visual weight và
integration mode; `textIntegrity`, `typographyIntegrity` và exact capacity hoãn
sang InDesign.

Với `BAKED_TEXT_PROXY_CONCEPT`, khóa thêm footprint, reading order và
interaction edge đã duyệt; nội dung glyph vẫn không khóa. Exact text integrity,
typography integrity và capacity tiếp tục hoãn sang InDesign.

Với mọi mode `FINAL_TEXT_REFLOW` (kể cả alias legacy), `textCapacityProof` trên artwork là
đường dẫn proof JSON theo [text-reflow-contract.md](text-reflow-contract.md).
`textCapacity` mặc định REQUIRED; thiếu proof không được PASS bằng lời khai.
Override chỉ theo yêu cầu người dùng và ghi đúng phạm vi. Proof của option
không thay proof của candidate sau khi silhouette hoặc flow đã thay đổi.

`TEXT_PROXY_INTEGRATION` không được tạo proof giả hoặc nâng proxy thành PASS chữ
thật. Ghi rõ `DEFERRED_TO_INDESIGN` trong manifest và báo cáo QA.

`BAKED_TEXT_PROXY_CONCEPT` cũng không được nâng proxy thành PASS chữ thật.
Integrated concept không phải production artwork; chỉ `cleanArtworkMaster` đã
đạt `CLEAN_PLATE_PASS` mới được dùng làm nguồn cho bộ layer.
