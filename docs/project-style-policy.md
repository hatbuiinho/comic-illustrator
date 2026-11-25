# Policy phong cách toàn project

## Style hiện hành

Từ 2026-11-25, mọi lượt tạo/chỉnh ảnh mới dùng
**[ttpq comic blend](style-ttpq-comic-blend.md)**: minh họa tập/page/frame,
Character Studio, Image Playground và TTPQ Comic, kể cả bản thử, sheet và variant.
Đọc và đưa định nghĩa đầy đủ vào prompt; không chỉ ghi tên style.

`SKIPPED_BY_USER` — phạm vi toàn dự án, thay thế hoàn toàn style trước đây:
st01–st03, `ttpq comic light` (mặc định 2026-10-29 → 2026-11-24) và
`ttpq comic soft` (tùy chọn TTPQ Comic, bỏ ngày 2026-11-25), style TTPQ Comic
cũ, các override rendering cũ của studio và yêu cầu bắt buộc truyền ref đen trắng/bảng trang sức hoặc ref style cũ khác không còn
áp dụng cho lượt mới. Không kế thừa các khóa style cũ (màu, shading, texture,
ánh sáng, vật liệu) từ skill, template, output hoặc prompt lịch sử. Chỉ giữ
màu y và cách quấn y theo mục có điều kiện bên dưới.

Đây là thay đổi style, không thay workflow, identity/profile gốc, dữ kiện truyện,
layout, version hoặc cổng duyệt. Giữ nguyên tài sản và record cũ; khi tiếp tục
một tác vụ, dùng style mới cho version mới, không hồi tố QA.

## Ngoại lệ: style test của TTPQ Comic

Từ 2026-11-22, TTPQ Comic có style test
[ttpq storybook](../ttpq-comic/style/ttpq-storybook.md)
(40% Semi-Realistic Storybook Illustration + 35% flat + 25% nền storybook),
chỉ dùng cho lượt màu khi người dùng gọi tên; QA theo định nghĩa của nó.

Cũng từ 2026-11-22, TTPQ Comic có style test
[ttpq real](../ttpq-comic/style/ttpq-real.md)
(50% Semi-Realistic Comic Illustration + 25% flat + 25% nền storybook, nhánh
của blend), chỉ dùng cho lượt màu khi người dùng gọi tên (từ 2026-11-25 không
còn là mặc định của `color-edit` và `--recast`); QA theo định nghĩa của nó.

## Chỉ khi ảnh cần vẽ tu sĩ

Chỉ khi ảnh thực sự có tu sĩ, đọc và áp dụng
[quy chuẩn màu y và cách quấn y](monastic-robes.md). Không đọc/truyền các ref y
hoặc chèn khối y vào prompt/QA của ảnh không có tu sĩ. Quy chuẩn y phục là
ràng buộc đối tượng riêng, không phải thành phần của định nghĩa style độc lập.

## Prompt và QA

- Dùng đúng nét vẽ tay (viền nâu rất đậm gần đen, nét trong ngả màu), tỷ lệ
  người thật 7–7.5 đầu, mảng màu phẳng với 2–3 tông cel mép hơi dịu trên
  da/vải, ánh sáng theo cảnh, đủ dải sáng tối, nền viễn cảnh vẽ dịu và các
  điều cấm của style blend.
- Giữ identity và thiết kế theo nguồn gốc của đúng workflow; không lấy khuôn
  mặt, màu da hoặc thiết kế từ ref style/output khác. Với tu sĩ, resolve màu
  và cách quấn y theo quy chuẩn có điều kiện trước khi khóa trang phục.
- QA theo định nghĩa blend (gradient nhẹ chỉ ở trời/viễn cảnh/trung cảnh,
  không trên nhân vật), không áp lại mức shading, cấm tuyệt đối texture/
  gradient hoặc ref vật liệu của style cũ. Kiểm cả nhân vật lẫn bối cảnh.
- Ghi tên `ttpq comic blend` (hoặc style test đã dùng), input/vai trò và thay đổi style trong record.
  Ngoại lệ mới do người dùng yêu cầu ghi `SKIPPED_BY_USER` đúng phạm vi.
