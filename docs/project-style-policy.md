# Policy phong cách toàn project

## Style hiện hành

Từ 2026-10-29, mọi lượt tạo/chỉnh ảnh mới dùng
**[ttpq comic light](style-ttpq-comic-light.md)**: minh họa tập/page/frame,
Character Studio, Image Playground và TTPQ Comic, kể cả bản thử, sheet và variant.
Đọc và đưa định nghĩa đầy đủ vào prompt; không chỉ ghi tên style.

`SKIPPED_BY_USER` — phạm vi toàn dự án, thay thế hoàn toàn style trước đây:
st01–st03, style TTPQ Comic cũ, các override rendering cũ của studio và yêu cầu
bắt buộc truyền ref đen trắng/bảng trang sức hoặc ref style cũ khác không còn
áp dụng cho lượt mới. Không kế thừa các khóa style cũ (màu, shading, texture,
ánh sáng, vật liệu) từ skill, template, output hoặc prompt lịch sử. Chỉ giữ
màu y và cách quấn y theo mục có điều kiện bên dưới.

Đây là thay đổi style, không thay workflow, identity/profile gốc, dữ kiện truyện,
layout, version hoặc cổng duyệt. Giữ nguyên tài sản và record cũ; khi tiếp tục
một tác vụ, dùng style mới cho version mới, không hồi tố QA.

## Chỉ khi ảnh cần vẽ tu sĩ

Chỉ khi ảnh thực sự có tu sĩ, đọc và áp dụng
[quy chuẩn màu y và cách quấn y](monastic-robes.md). Không đọc/truyền các ref y
hoặc chèn khối y vào prompt/QA của ảnh không có tu sĩ. Quy chuẩn y phục là
ràng buộc đối tượng riêng, không phải thành phần của định nghĩa style độc lập.

## Prompt và QA

- Dùng đúng nét vẽ tay, tỷ lệ tự nhiên, mảng màu phẳng, 2–3 tông cel-shading
  trên da/vải, màu hài hòa, texture tiết chế và các điều cấm của style mới.
- Giữ identity và thiết kế theo nguồn gốc của đúng workflow; không lấy khuôn
  mặt, màu da hoặc thiết kế từ ref style/output khác. Với tu sĩ, resolve màu
  và cách quấn y theo quy chuẩn có điều kiện trước khi khóa trang phục.
- QA theo định nghĩa mới, không áp lại mức shading, cấm tuyệt đối texture/
  gradient hoặc ref vật liệu của style cũ. Kiểm cả nhân vật lẫn bối cảnh.
- Ghi tên `ttpq comic light`, input/vai trò và thay đổi style trong record.
  Ngoại lệ mới do người dùng yêu cầu ghi `SKIPPED_BY_USER` đúng phạm vi.
