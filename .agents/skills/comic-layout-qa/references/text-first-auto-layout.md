# GENERATION_LAYOUT_INTEGRATION

Áp dụng cùng [text-artwork-integration.md](text-artwork-integration.md). Chỉ áp
toàn bộ [text-reflow-contract.md](text-reflow-contract.md) khi contract active
là `FINAL_TEXT_REFLOW`.

Dùng khi page không có hard frame hoặc brief bắt buộc và hình phải sống cùng
khối chữ.

## Bất biến

- Trước composition, resolve contract chữ. `FINAL_TEXT_REFLOW` khóa toàn bộ
  content/typography; `TEXT_PROXY_INTEGRATION` chỉ khóa cấu trúc trang, reserve,
  mật độ và trọng lượng thị giác dự kiến, còn chữ cuối thuộc InDesign;
  `BAKED_TEXT_PROXY_CONCEPT` khóa thêm footprint và interaction edge nhưng không
  khóa nội dung glyph.
- Layout chữ ban đầu không phải occupancy cố định. Được đổi text-frame geometry,
  độ rộng cột, line break do reflow và wrap path để nhường chỗ cho artwork.
- Thiết kế camera, cỡ cảnh, staging và silhouette trong phạm vi vừa đủ trên
  canvas chuẩn; khóa `sceneExtentPlan` theo `text-artwork-integration.md`, rồi
  dùng chữ thật/proxy. Không ép scene mở rộng bằng kích thước trang.
- Với `FINAL_TEXT_REFLOW`, mỗi option phải chứng minh `textCapacityProof`: không overflow, không mất chữ,
  không đảo reading order, không cột quá hẹp, không dòng vụn/widow-orphan nghiêm
  trọng và không vượt trim/safe/gáy.
- Với `TEXT_PROXY_INTEGRATION`, mỗi option phải có `shotMap`,
  `productionCompositionPreview` và `integrationCrop100`; trạng thái là
  `PROXY_COMPOSITION_PASS`, không phải capacity PASS.
- Với `TEXT_PROXY_INTEGRATION`, phải có thêm `proxyFidelityProof` đã qua
  `verify-proxy-fidelity.js`. Proof so text burden, visual weight, readable scale
  và reading continuity; tuyệt đối không dùng tọa độ hay bounding-box similarity
  làm tiêu chí vì chữ được tự do rẽ ở mọi vị trí.
- Với `BAKED_TEXT_PROXY_CONCEPT`, áp cùng proxy proof nhưng dùng composition có
  proxy làm generation reference. Sau selection, tháo proxy bằng edit/inpaint
  trong mask đã khai báo và chỉ tiếp tục khi `CLEAN_PLATE_PASS`.
- Sau khi người dùng chọn composition và trước generation, kế thừa typography
  lock cùng provisional reflow đã PASS; chỉ tinh chỉnh contour, knockout và
  overlap theo art direction, không thay đổi content hoặc typography.
- Được art-direct lại vị trí text frame, số cột, cấu trúc khối, độ rộng cột,
  line break và wrap path ở mọi vùng của page/spread. Layout gốc cung cấp content,
  typography và text burden, không khóa occupancy. Mọi mutation phải giữ reading
  order, scale đọc, khả năng đọc và toàn bộ nội dung; không tự đổi typography đã
  khóa hoặc co text burden để tạo đất giả cho hình.
- Reflow toàn bộ chữ thật ở composition preflight để biết text capacity; đầu ra là
  `textFlowEnvelope` có contour và các điểm co giãn, không phải các hộp khóa
  composition. Flow envelope được art-direct quanh shot đã duyệt; không thay đổi
  camera, staging hoặc tương quan chủ thể để cứu layout.
- Tách ba khái niệm: `glyphExclusion` cho mặt/tay/đạo cụ cần đọc rõ;
  `backgroundDensityMap` cho mức tương phản và mật độ nét; `sceneExtentPlan`
  cho footprint cảnh/nền giấy. `fullBleedCoverage` chỉ áp khi full-bleed hoặc
  hard mask có provenance. Không suy text zone tự động là cảnh hay vùng trống.
- Không mặc định dùng knockout trắng. Integration mode quyết định paper fade,
  scenic wash, full-bleed overprint, silhouette wrap hay dark field. Background
  chỉ cần tiếp tục dưới chữ/proxy trong footprint cảnh, có thể tan về paper tone;
  `WHITE_OPAQUE` chỉ là fallback cục bộ khi
  source hoặc mode yêu cầu.
- Hình mask phải được thiết kế như một phần của composition: biên mask đi theo
  nhịp dòng chữ và silhouette, có chỗ mở–khép để dẫn mắt và không mặc định là
  các hình chữ nhật đối xứng. `text frame` là vùng tính toán; không được dùng
  nguyên hình hộp của frame làm hình mask nếu tạo mép cứng, bậc vuông hoặc hai
  cột soi gương máy móc.
- Reflow được phép tạo độ dài dòng khác nhau để hình khối đoạn văn ôm nhân vật,
  miễn giữ nguyên typography, thứ tự đọc và độ dài dòng vẫn dễ đọc. Khoảng trắng
  phải có nhịp lớn–nhỏ có chủ ý; tránh bốn khối chữ có cùng chiều rộng/cạnh thẳng.
- Thứ tự preview của reflow/overlay: raw artwork → integration treatment ngoài
  model → chữ thật hoặc proxy overlay. Với mode baked: composition có proxy →
  `integratedTextConcept` → selection → `cleanArtworkMaster` → chữ production
  trong InDesign. Nếu người dùng khóa `WHITE_OPAQUE`, giữ knockout; nếu chọn
  scenic mode, không được tự đổi thành mảng trắng.
- Recognition core, cử chỉ và đạo cụ kể chuyện phải tránh knockout mask; wrap
  path có thể ôm silhouette nhưng không làm lộ background bên dưới chữ.
- Trước QA kỹ thuật, xem preview ở kích thước thumbnail. Nếu mắt đọc thấy các
  hộp trắng trước khi thấy quan hệ chữ–nhân vật–cử chỉ, kết luận
  `LAYOUT_COMPOSITION_NEEDS_REVISION` dù mọi text frame vẫn hợp lệ kỹ thuật.
- Cổng chọn hiển thị artifact theo contract active. Proxy phải gần production
  về scale/density và không được dùng box giả hoặc chữ bị thu nhỏ để chứng minh
  khoảng trống.
- Sau generation được tinh chỉnh flow contour và wrap offset theo silhouette
  thật trong giới hạn text capacity đã chứng minh. Không đổi typography hoặc
  đảo reading order để cứu một ảnh không vừa.

## Kết luận

- `PASS`: chữ nguyên vẹn, typography khớp nguồn, đọc liên tục và không giao
  recognition core/cử chỉ kể chuyện.
- `IMAGE_NEEDS_REVISION`: có thể sửa scale, placement hoặc crop mà vẫn giữ shot.
- `COMPOSITION_NEEDS_REVISION`: khoảng trống không đủ nếu giữ typography; quay
  lại thiết kế shot.
- `TYPOGRAPHY_DRIFT`: font, size, leading, tracking, scale hoặc style thay đổi;
  preflight không hợp lệ.
- `PROXY_COMPOSITION_PASS`: nhịp chữ mô phỏng, integration mode và khoảng thở
  đạt; exact text capacity được hoãn sang InDesign.
- `INTEGRATED_CONCEPT_PASS`: proxy bake và artwork tạo thành một composition
  thống nhất, vẫn giữ burden/footprint gần production.
- `CLEAN_PLATE_PASS`: glyph proxy đã được tháo sạch, artwork được bảo vệ không
  đổi và footprint đặt chữ trong InDesign vẫn khả thi.
- `BACKGROUND_CONTEXT_LOSS`: chữ vẫn đọc được nhưng việc làm rỗng/đơn giản hóa
  khiến location hoặc hoạt động không còn đúng; phải sửa background, không sửa
  typography hoặc tự mở rộng vùng chủ thể.
- `SCENE_OVEREXPANSION`: cảnh/nền/props trải rộng chỉ để phủ trang hoặc vượt
  footprint đã duyệt; sửa phạm vi và biên hòa, không co chữ. Nền giấy ngoài cảnh
  không tự tạo `BACKGROUND_CONTEXT_LOSS`.

Luôn xuất clean preview có chữ thật và debug overlay có text frame, wrap path,
subject exclusion, gáy và print-safe.
