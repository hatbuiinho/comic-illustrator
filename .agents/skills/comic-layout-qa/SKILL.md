---
name: comic-layout-qa
description: Kiểm tra output trong layout truyện tranh về frame, mask, tỷ lệ, vùng chữ, trim, safe zone và gáy khi áp dụng. Không dùng cho concept art, profile hoặc ảnh chưa gắn layout.
---

# Layout QA

Đầu tiên đọc [layout-routing.md](references/layout-routing.md) để xác định check
nào áp dụng. Đọc [manifest-schema.md](references/manifest-schema.md) trước khi
tạo/sửa manifest. Chỉ đọc hướng dẫn loại frame liên quan:

- [spread-and-gutter.md](references/spread-and-gutter.md)
- [single-page.md](references/single-page.md)
- [inset-frame.md](references/inset-frame.md)

Chạy `scripts/layout-frame-qa.js <manifest> [output-dir]` khi manifest và raster
layout đã sẵn sàng. Overlay phải dùng chính raster layout gốc có text; không tạo
nền trắng thay thế.

Nếu frame không phải chữ nhật, thực hiện hard gate raw-output trong
[inset-frame.md](references/inset-frame.md) trước khi đọc kết quả overlay; script
hình học không thay thế check alpha/canvas này.

Nếu chưa biết manifest active, chạy `scripts/discover-layout.js <page-dir>`;
chỉ tiếp tục tự động khi kết quả là `RESOLVED`. Script QA tạo cả SVG truy vết và
PNG overlay để hiển thị. Các critical box vẫn phải được xác định từ composition
hoặc quan sát có căn cứ; geometry script không tự nhận diện nhân vật trong ảnh.

Không biến check `NOT_APPLICABLE` hoặc `SKIPPED_BY_USER` thành FAIL. Vẫn có thể
vẽ guide của check bị bỏ qua để tham khảo nếu dữ liệu hình học tồn tại.
