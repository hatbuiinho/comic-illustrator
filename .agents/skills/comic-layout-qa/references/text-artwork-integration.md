# Tích hợp chữ–hình theo art direction

Mọi yêu cầu proof schema 3 bên dưới được nâng lên schema 4 theo
[contract đo typography](proxy-typography-measurement.md): giữ artifact binding,
bổ sung phép đo độc lập PDF→canvas, font, leading, glyph và diện tích render.
Schema 3 chỉ là lịch sử và không mở cổng composition khi chạy lại workflow.

Đọc reference này khi page không dùng hard frame và hình cần hòa với vùng chữ.
Chọn contract từ source hoặc xác nhận người dùng; không tự suy một mode thành
chuẩn cho mọi tập.

## Ba contract chữ

### `FINAL_TEXT_REFLOW`

Dùng khi chữ thật phải được chứng minh trước generation. Áp dụng đầy đủ
`text-reflow-contract.md`, tạo `textCapacityProof` và chỉ báo
`REFLOW_PREFLIGHT_PASS` khi proof hợp lệ.

### `TEXT_PROXY_INTEGRATION`

Dùng khi typography cuối thuộc InDesign và người dùng chưa cần chữ thật trong
workflow ảnh.

- Proxy text chỉ mô phỏng mật độ, số dòng, nhịp đoạn, trọng lượng thị giác và
  hình dáng cột dự kiến; không phải nội dung hay typography cuối.
- Proxy là overlay tách khỏi artwork, không bake vào raw candidate/master.
- Không tạo `textCapacityProof`, không báo `REFLOW_PREFLIGHT_PASS` và không tuyên
  bố chữ thật vừa. Dùng `PROXY_COMPOSITION_PASS` cùng
  `exactTextCapacity: DEFERRED_TO_INDESIGN`.
- Giữ đủ reserve và mutation latitude cho InDesign: text-frame geometry, line
  break, column width và wrap contour chưa bị khóa cứng.
- Proxy phải gần production về tỷ lệ thị giác; không thu nhỏ chữ hoặc mảng chữ
  chỉ để option trông thoáng hơn.

### `BAKED_TEXT_PROXY_CONCEPT`

Dùng khi chữ chính xác được hoàn thiện ở InDesign nhưng artwork cần được AI
thiết kế trực tiếp cùng text mass. Đây là contract ưu tiên cho page/spread có
mục tiêu hình–chữ hòa quyện và người dùng chấp nhận chữ concept không chính xác.

- Dựng proxy từ cùng `textBurdenModel` và vượt các gate burden/layout/artifact
  binding như `TEXT_PROXY_INTEGRATION` trước generation.
- Composition preview là mockup toàn trang có proxy ở scale gần production;
  khóa footprint, reading order, paragraph rhythm, vùng tương tác hình–chữ và
  vùng cần clean plate, nhưng không khóa nội dung glyph.
- Ở generation, proxy được phép xuất hiện trong `integratedTextConcept` như một
  element thị giác để model tổ chức silhouette, negative space, value, detail
  density và eye path quanh nó. Chữ model sinh chỉ là vật liệu concept, không
  phải typography cuối và không được đưa vào artwork bàn giao cho InDesign.
- Sau khi người dùng chọn đích danh concept, khóa mọi pixel artwork ngoài vùng
  glyph/repair đã khai báo, rồi edit/inpaint đúng concept đó để tạo
  `cleanArtworkMaster`. Không fresh-generate clean master và không cho model dàn
  lại shot ở bước làm sạch.
- Exact text capacity vẫn là `DEFERRED_TO_INDESIGN`; chỉ bàn giao khi clean
  master giữ được silhouette, khoảng âm, edge rhythm, background continuity và
  footprint đủ để đặt text production.

Không dùng mode này khi text phải đúng ngay trong ảnh, khi glyph là một phần
không thể tháo khỏi key visual, hoặc vùng dưới chữ quá phức tạp để phục hồi clean
plate có kiểm soát. Khi đó chọn `FINAL_TEXT_REFLOW` hoặc
`TEXT_PROXY_INTEGRATION`.

#### Hai gate riêng của proxy

Không dùng một trạng thái PASS chung để đánh đồng “đủ lượng chữ” với “có thể
dàn trang thực tế”. Mỗi proxy phải vượt hai gate theo thứ tự:

- `PROXY_BURDEN_PASS`: đủ content units, visual weight và scale đọc;
- `PROXY_LAYOUT_PASS`: paragraph rhythm, line measure, leading, column logic,
  reading order và wrap review đều khả thi gần production.

Chỉ khi cả hai gate PASS mới được ghi `PROXY_COMPOSITION_PASS` và mở cổng duyệt
composition. Proof schema cũ chỉ có burden metrics có thể nhận
`PROXY_BURDEN_PASS`, nhưng không đủ điều kiện duyệt.

Trước khi dựng proxy, tạo `textBurdenModel` từ layout thật. Model phải giữ
paragraph ID, thứ tự đọc, lượng nội dung, font scale và leading đại diện.
Ghi số dòng, line widths, khoảng nghỉ, indent/bullet và cột nguồn làm dữ liệu
tham chiếu; được thiết kế lại hình học và nhịp khi vẫn đọc tốt. Soft line break
có thể thay đổi theo contour, nhưng không được gom các đoạn thành những nhóm
dòng tùy ý hoặc tách một đoạn sang các vùng xa nhau khi không có column
continuation rõ ràng.

Mọi vùng chữ nhìn thấy trên spread là một `sourceTextRegion` riêng. Chuỗi text
giống nhau không chứng minh đó là layout variant: vẫn giữ từng occurrence, phía,
vai trò và geometry riêng. Chỉ chọn một trong nhiều layout variant khi nguồn
hoặc người dùng xác nhận rõ chúng loại trừ nhau. Vùng có vai trò
`translation-placeholder` không yêu cầu tạo bản dịch thật.

### Tự do art-direct vị trí chữ

Text frame gốc không phải occupancy map. Được chuyển chữ tới bất kỳ vị trí nào
trên page/spread, đổi số cột, hình học khối, độ dài dòng, line break và contour;
chữ có thể nằm cạnh, trên, dưới, giữa hoặc ôm quanh silhouette nếu tổng thể đẹp,
đọc tự nhiên và giữ recognition core. Không so proxy với layout bằng tọa độ,
bounding box hoặc độ phủ dọc tại từng vùng.

Tự do vị trí không cho phép làm nhẹ `text burden` hoặc phá hình thái dàn chữ.
Không so tọa độ tuyệt đối. Giữ paragraph count/order, lượng nội dung và cỡ đọc;
review leading, measure và cột theo khả năng đọc của bố cục mới, không bắt giống mẫu. Trước khi báo
`PROXY_COMPOSITION_PASS`, tạo `proxyFidelityProof` schema 4 so layout nguồn với
proxy về tổng lượng nội dung đại diện, visual weight ở scale đọc dự kiến,
typography scale, paragraph rhythm, line measure, reading continuity và khả
năng đọc. Chạy
`scripts/verify-proxy-fidelity.js <proof.json>` với `layoutComparison: ART_DIRECTED`
cho bố cục mới. Raster dùng SVG text overlay riêng; artwork không cần là SVG.
Gate không đo độ giống vị trí;
FAIL khi proxy co chữ, bỏ burden, thu nhỏ scale hoặc tạo khoảng trống giả để
dành đất cho hình.

Schema 3 chứa `artifacts.source`, `artifacts.semanticSvg` và
`artifacts.preview` kèm SHA-256; `sourceTextRegions` và ánh xạ một-một
`proxyTextRegions[].svgGroupId`. Mỗi SVG group dùng
`data-render-kind="source-text-layer"` hoặc `rendered-placeholder-text` và chứa
`<text>` có `font-size` đo được. Verifier đọc artifact, tính scale sau transform,
đếm line theo vùng và khóa preview bằng hash; không chấp nhận số copy từ JSON
hoặc thanh line trang trí làm bằng chứng.

## Phạm vi cảnh khác kích thước canvas

Với page/spread không có hard frame, kích thước file chỉ là hệ tọa độ dàn trang,
không yêu cầu cảnh phủ toàn trang. Chọn phạm vi cảnh từ emotional thesis,
khoảnh khắc và bằng chứng context tối thiểu: cảnh cần bao nhiêu dùng bấy nhiêu.
Cụm cảnh nhỏ, crop có chủ ý và biên hòa mềm vào nền giấy đều hợp lệ. Không kéo
đất, giàn giáo, đường chân trời hoặc props khắp spread để lấp diện tích còn lại.
Không mặc định cảnh nhỏ, full-page hay một tỷ lệ diện tích cố định: cảnh rộng
chỉ khi quy mô không gian/tập thể thực sự phục vụ nguồn hoặc lựa chọn người dùng.

Trước composition, ghi `sceneExtentPlan`: phạm vi cảnh nhìn thấy, lý do kể chuyện,
context/process evidence cần giữ, vùng nền giấy/khoảng thở chủ ý và cách biên
cảnh hòa với chữ. Khóa kế hoạch này cùng shot đã duyệt và truyền sang prompt,
generation và QA; không tự expand cảnh vì output dùng canvas lớn.

- `SCENIC_INTEGRATED`/`SCENIC_WASH` không đồng nghĩa full-page scenic background.
  Trong phạm vi cảnh, nền có thể tiếp tục dưới chữ rồi tan về paper tone; ngoài
  phạm vi đó, nền giấy là một quyết định thiết kế, không phải thiếu artwork.
- Raw candidate dùng đúng canvas/điểm gốc khi cần compositing. Phần ngoài cảnh
  có thể paper tone hoặc alpha theo deliverable đã chọn; không mặc định đổi alpha.
  Clean plate chỉ cần phục hồi cảnh trong footprint đã khóa, không dựng thêm
  bối cảnh ở vùng giấy hoặc expand mọi lớp sâu xuyên toàn trang.
- Không co chữ để tạo khoảng trống giả, cũng không mở rộng cảnh để lấp khoảng
  trống thật. Bảo toàn typography/text burden và recognition core như trước.
- Ngoại lệ: hard mask thật, full-bleed/overprint được nguồn hoặc người dùng chọn
  vẫn giữ coverage tương ứng. Canvas toàn spread tự nó không phải provenance
  cho yêu cầu full-bleed.

QA bằng mắt chạy `sceneExtentFidelity` và `sceneEconomy` trước hình học. FAIL
`SCENE_OVEREXPANSION` khi cảnh bị trải rộng hơn shot đã duyệt, hoặc nền/props
thừa chỉ nhằm phủ trang và làm khoảnh khắc mất trọng tâm. FAIL context loss chỉ
khi mất bằng chứng cần để hiểu đúng nơi chốn/hoạt động; không FAIL chỉ vì thấy
nền giấy. Không chữa overexpansion bằng co chữ hoặc mask hộp trắng; sửa footprint
và biên hòa cảnh. Nếu sửa làm đổi shot đã duyệt, quay lại cổng composition.

## Các mode hòa chữ–hình

Chọn một primary và tối đa hai secondary mode:

- `PAPER_FADE`: nền cảnh tan dần về paper tone; không có đường mask đọc được.
  Không dùng fade để kết thúc cơ thể giữa trang. Crop thân tại mép trang hoặc
  khung inset thật; che khuất phải có vật che nhìn thấy. Áp
  [crop-read-contract.md](../../comic-shot-design/references/crop-read-contract.md)
  ngay ở composition; footprint cảnh và biên hòa giấy không tạo biên crop mới.
- `SCENIC_WASH`: background trong phạm vi cảnh tiếp tục dưới chữ rồi giảm dần
  contrast, saturation hoặc mật độ nét về paper tone, giữ context evidence cần thiết.
- `FULL_BLEED_OVERPRINT`: chữ nằm trực tiếp trên vùng cảnh có value ổn định.
- `SILHOUETTE_WRAP`: đầu, vai, tay, y phục hoặc đạo cụ len vào hình khối chữ;
  chỉ glyph/proxy glyph cộng khoảng thở loại trừ recognition core.
- `DARK_FIELD_OVERPRINT`: chữ sáng trên artwork tối có value được kiểm soát.
- `MEMORY_VIGNETTE_SOFT_EDGE`: lớp hồi tưởng có biên tan vào atmosphere, không
  thành khung hoặc mảng cắt cứng.
- `HARD_FRAME`: chỉ khi source có frame/mask thật hoặc người dùng chọn rõ.

`WHITE_OPAQUE` chỉ là fallback cục bộ sát glyph khi mode/source yêu cầu. Không
dùng nó để che nguyên text frame trong `SCENIC_WASH` hoặc
`TEXT_PROXY_INTEGRATION`.

## Hard context và creative freedom

Mỗi option/generation plan phải tách ba nhóm:

- `contextLocks`: moment, location, nhân vật, profile, active process, causal
  state, required evidence và topography có provenance;
- `forbidden`: chi tiết tương lai, trạng thái sai, identity borrowing và
  landmark không có nguồn;
- `creativeFreedom`: lớp sâu, khoảng âm, value structure, atmospheric
  transition, secondary props hợp bối cảnh và chi tiết nền không tạo continuity
  mới.

Không biến `creativeFreedom` thành checklist bắt buộc. AI được tự thiết kế phần
này miễn output vẫn thỏa locks và không chạm forbidden.

## Production-layout proxy

Trước generation, tạo `productionLayoutProxy` tách lớp gồm:

1. map trên canvas chuẩn, phân biệt footprint cảnh với nền giấy chủ ý;
2. silhouette và recognition core của composition đã chọn;
3. proxy text overlay;
4. `backgroundValueMap` và `detailDensityMap` dưới vùng chữ;
5. `integrationEdgeMap` cho fade/wash/overlap;
6. `glyphPressureMap` chỉ để art-direct khoảng thở, không phải hard mask.

Raw artwork không chứa proxy glyph. Model phải render cảnh đầy đủ dưới overlay,
trong `sceneExtentPlan`; ngoài footprint được giữ nền giấy. Không tạo khoảng
trống giả bằng co proxy và không tự vẽ chữ đọc được.

Quy tắc raw artwork không chứa glyph ở trên chỉ áp dụng cho
`TEXT_PROXY_INTEGRATION`. Với `BAKED_TEXT_PROXY_CONCEPT`, cùng bộ map được gộp
thành `bakedProxyGenerationReference`; output đầu là
`integratedTextConcept`, có thể chứa glyph/pseudo-glyph. Generation plan khai
báo thêm:

- `proxyRemovalMask`: vùng glyph dự kiến được phép sửa sau selection;
- `repairContextRing`: vùng biên tối thiểu để nối line, fill, wash và texture;
- `protectedArtworkMask`: recognition core và artwork không được đổi khi làm sạch;
- `indesignTextFootprint`: footprint, reading order và khoảng thở cần bảo toàn.

## Preview bắt buộc ở cổng chọn

Với `TEXT_PROXY_INTEGRATION`, mỗi option có:

- `shotMap`: camera, staging, eye path và lớp sâu;
- `productionCompositionPreview`: artwork/value proxy + proxy text gần trang
  cuối;
- `integrationCrop100`: crop vùng chữ giao silhouette/background để thấy mép
  hòa và khoảng thở.

Không cho chọn nếu preview đọc thành “hộp chữ trên tranh”, proxy bị thu nhỏ vô
lý, background mất context hoặc hard edge xuất hiện ngoài ý đồ.

Không cho chọn nếu thiếu đồng thời `PROXY_BURDEN_PASS` và
`PROXY_LAYOUT_PASS`, kể cả preview đẹp và render semantic thành công.
`exactTextCapacity: DEFERRED_TO_INDESIGN` chỉ hoãn proof chữ thật; không hoãn
bằng chứng proxy đang đại diện trung thực text burden và hình thái dàn chữ.

Với `BAKED_TEXT_PROXY_CONCEPT`, composition gate vẫn diễn ra trước generation
và dùng `productionCompositionPreview` có proxy. Sau generation, người dùng chọn
trên `integratedTextConcept`; trước delivery phải có thêm `cleanPlateProof`
gồm crop trước/sau ở vùng khó nhất. Proof chỉ PASS khi không còn glyph/ghost,
không đổi protected artwork và trang vẫn giữ nhịp hình khi proxy được tháo ra.

## QA

Kiểm bằng mắt trước hình học:

- `proxyScaleFidelity`;
- `integrationModeFidelity`;
- `edgeVisibility`;
- `backgroundContinuation`;
- `sceneExtentFidelity` và `sceneEconomy` theo phạm vi cảnh đã duyệt;
- `recognitionCoreProtection`;
- `productionReadiness`.
- `proxyFidelityProof`: text burden, scale, reading continuity và readability;
  vị trí tuyệt đối chủ ý không được so sánh.

Không dùng từ “reflow”, “chữ đã vừa” hoặc `REFLOW_*` cho proxy. Chỉ gọi là
“text-burden proxy” sau gate burden, hoặc “proxy gần production” sau cả hai
gate. “Chữ thật đã reflow” chỉ dùng với `REAL_REFLOW_PASS` từ
`FINAL_TEXT_REFLOW`.

Không FAIL chỉ vì proxy không đúng câu chữ. Không PASS text integrity,
typography integrity hoặc exact capacity cho đến khi InDesign có chữ thật.

Riêng `BAKED_TEXT_PROXY_CONCEPT`, QA chia hai cổng:

- `INTEGRATED_CONCEPT_PASS`: hình và proxy đọc thành một composition, không phải
  hộp chữ đặt lên tranh;
- `CLEAN_PLATE_PASS`: proxy đã được tháo sạch mà không làm composition sụp,
  recognition core đổi hoặc background xuất hiện vết vá.

Thiếu một trong hai cổng thì chưa được tạo bộ layer hoặc chuyển `approved/`.
