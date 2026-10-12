---
name: comic-layout-qa
description: Kiểm tra output trong layout truyện tranh về mask thật, chữ và text wrap, trim, safe zone, gáy và bộ layer InDesign khi áp dụng. Không dùng cho concept art, profile hoặc ảnh chưa gắn layout.
---

# Layout QA

Đọc [quy tắc nghệ thuật](../comic-shot-design/references/art-first-policy.md) và áp dụng theo giai đoạn của skill này.

Với mọi proxy, đọc [contract đo typography schema 4](references/proxy-typography-measurement.md).
Verifier phải đo trực tiếp PDF nguồn và SVG render ở cùng scale vật lý; proof
schema 3 hoặc PASS tự khai không đủ mở cổng. Đối chiếu PDF và preview cùng canvas.

Với text reflow, đọc [text-reflow-contract.md](references/text-reflow-contract.md).
Dùng `scripts/verify-text-reflow.js <proof.json>` để đối chiếu text nguồn với
dữ liệu xuất từ công cụ dàn trang; script không tự dàn chữ hoặc thay review thị giác.

Với page cần hòa chữ–hình, đọc
[text-artwork-integration.md](references/text-artwork-integration.md) và resolve
`FINAL_TEXT_REFLOW`, `TEXT_PROXY_INTEGRATION` hoặc
`BAKED_TEXT_PROXY_CONCEPT` trước khi tạo preview. Không
áp proof chữ thật cho mode proxy; ghi `exactTextCapacity: DEFERRED_TO_INDESIGN`.
Mode proxy mới dùng `layoutComparison: ART_DIRECTED` để không khóa số dòng/measure
theo mẫu. Vẫn cần `proxyFidelityProof` schema 4 và chạy
`scripts/verify-proxy-fidelity.js`. Proof phải trả cả `PROXY_BURDEN_PASS` và
`PROXY_LAYOUT_PASS`, đồng thời `ARTIFACT_BINDING_PASS`: gate đầu bảo toàn lượng/scale chữ; gate sau kiểm paragraph,
line measure, leading, cấu trúc cột, reading order và wrap khả thi mà không khóa
tọa độ tuyệt đối. Verifier đọc semantic SVG thật, đếm `<text>` từng region,
tính font size sau transform và đối chiếu SHA-256 của source/SVG/preview. Thiếu
occurrence, dùng abstract bars, thu nhỏ chữ hoặc sửa artifact sau proof đều FAIL.
Proof schema cũ không mở cổng duyệt.

Nếu contract active là `BAKED_TEXT_PROXY_CONCEPT`, dùng cùng proxy fidelity
gates trước composition nhưng cho phép glyph nằm trong `integratedTextConcept`.
Chạy art-direction gate trên concept này và chỉ báo `INTEGRATED_CONCEPT_PASS`
khi text mass thực sự tham gia figure–ground, rhythm và eye path. Sau selection,
kiểm `cleanPlateProof`, crop trước/sau vùng khó nhất, absence của glyph/ghost,
pixel lock và background continuity; chỉ báo `CLEAN_PLATE_PASS` khi toàn bộ đạt.

Review nghệ thuật trước khi tinh chỉnh proof cuối. Lỗi mất chữ/cỡ đọc/khả năng
bàn giao phải sửa; chênh lệch hình học so mẫu phải xét tác động, không tự tạo FAIL.
Preview raster/sketch dùng SVG text overlay đo riêng; không cần marker actor.

Đọc [layout-routing.md](references/layout-routing.md) để xác định check
nào áp dụng. Đọc [manifest-schema.md](references/manifest-schema.md) trước khi
tạo/sửa manifest. Chỉ đọc hướng dẫn loại frame liên quan:

- [spread-and-gutter.md](references/spread-and-gutter.md)
- [single-page.md](references/single-page.md)
- [inset-frame.md](references/inset-frame.md)

Chạy `scripts/layout-frame-qa.js <manifest> [output-dir]` khi manifest và raster
layout đã sẵn sàng. Overlay phải dùng chính raster layout gốc có text; không tạo
nền trắng thay thế.

Phân biệt `briefRegion` với frame/mask thật. `briefRegion` chỉ vẽ như guide và
không tạo FAIL khi chủ thể, background hoặc eye path vượt ra ngoài. Chỉ
`hardFrame`/mask thật, trim, gáy và vùng chữ mới tạo ranh giới bắt buộc.

Nếu layout không có brief/mask, dùng `GENERATION_LAYOUT_INTEGRATION` và đọc
[text-first-auto-layout.md](references/text-first-auto-layout.md). Với
`FINAL_TEXT_REFLOW`, khóa content/typography và chứng minh capacity. Với
`TEXT_PROXY_INTEGRATION`, dùng proxy gần production để khóa nhịp và reserve
tương đối; không tuyên bố chữ thật vừa trước InDesign. Không gọi proxy là
“reflow”. Nếu proxy chỉ là các thanh trang trí, gom đoạn tùy ý hoặc không có
layout proof thì trả `LAYOUT_COMPOSITION_NEEDS_REVISION`.

Với mọi clean preview chữ–hình, đọc và chạy
[art-direction-gate.md](references/art-direction-gate.md) trước QA hình học.
PASS kỹ thuật không được nâng thành PASS layout nếu cổng art direction chưa đạt.
Với chủ thể bị cắt, cổng này kiểm thêm crop và mặt đất theo
[crop-read-contract.md](../comic-shot-design/references/crop-read-contract.md)
trên cả composition và clean preview; chữ/knockout không được che lỗi crop.
Kiểm phạm vi cảnh theo `sceneExtentPlan` trong `text-artwork-integration.md`:
không dùng canvas/coverage PASS để duyệt một cảnh mở rộng thừa; khoảng giấy có
chủ ý hợp lệ nếu context evidence và text burden vẫn được giữ.

Nếu frame không phải chữ nhật, thực hiện hard gate raw-output trong
[inset-frame.md](references/inset-frame.md) trước khi đọc kết quả overlay; script
hình học không thay thế check alpha/canvas này.

Nếu chưa biết manifest active, chạy `scripts/discover-layout.js <page-dir>`;
chỉ tiếp tục tự động khi kết quả là `RESOLVED`. Script QA tạo cả SVG truy vết và
PNG overlay để hiển thị. Các critical box vẫn phải được xác định từ composition
hoặc quan sát có căn cứ; geometry script không tự nhận diện nhân vật trong ảnh.

Không biến check `NOT_APPLICABLE` hoặc `SKIPPED_BY_USER` thành FAIL. Vẫn có thể
vẽ guide của check bị bỏ qua để tham khảo nếu dữ liệu hình học tồn tại.

Với workflow page-aware, clean preview phải ghép từ raw candidate và lớp chữ
ngoài model: typography thật cho `FINAL_TEXT_REFLOW`, proxy overlay cho
`TEXT_PROXY_INTEGRATION`. Không dùng chữ do model render.

Ngoại lệ là `BAKED_TEXT_PROXY_CONCEPT`: dùng chữ model render để duyệt concept,
nhưng clean preview và bộ layer bàn giao phải lấy từ `cleanArtworkMaster` không
còn glyph, sau đó mới đặt chữ production ngoài model.

Luôn tạo hai cách xem khi đủ dữ liệu: clean layout preview với chữ thật để đánh
giá hòa hình–chữ, và debug overlay chứa brief region, text zone, subject
exclusion, wrap path, trim/gáy. Không dùng debug overlay thay clean preview.

Với master ở `SELECTED_FOR_LAYOUT`, kiểm thêm bộ layer theo
`comic-image-production/references/indesign-layer-package.md`. Đây là QA kỹ
thuật hậu kỳ; không mở lại visual QA hoặc thay đổi master đã chọn.
