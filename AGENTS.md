# Comic Illustration Project

## Ngôn ngữ và cách phản hồi

- Mặc định trả lời và cập nhật file `.md` bằng tiếng Việt tự nhiên.
- Giữ nguyên tên riêng, tên file, lệnh và thuật ngữ kỹ thuật cần thiết.
- Khi có 2–3 phương án thực tế, trình bày thành danh sách đánh số ngắn; mỗi
  phương án nêu kết quả và đánh đổi trong một dòng.
- Nội dung người dùng cần copy phải đầy đủ trong code block hoặc writing block.

## Phạm vi nguồn

- Mỗi thư mục tập là một đơn vị nội dung độc lập.
- Không lấy profile, layout, bối cảnh, script hoặc asset từ tập khác để thay thế.
- Trước công việc phụ thuộc nội dung, xác định đúng tập, part, page và frame;
  đọc `notes.md`, `shot_notes.md` nếu có, kịch bản liên quan, layout và profile
  thuộc đúng tập.
- Nếu nguồn cấp tập bị thiếu, chỉ coi đó là blocker khi deliverable thật sự phụ
  thuộc vào nguồn đó.

## Thứ tự ưu tiên

1. Yêu cầu trực tiếp mới nhất của người dùng.
2. Dữ kiện và ngoại lệ trong `notes.md` của đúng tập.
3. Continuity hoặc ngoại lệ trong `shot_notes.md` của đúng tập.
4. Skill phù hợp trong `.agents/skills/`.
5. Quy tắc nền trong file này.
6. Giả định sáng tạo của Codex.

Một override rõ của người dùng phải được ghi là `SKIPPED_BY_USER`, không được
âm thầm áp lại quy tắc mặc định. Nếu người dùng không nêu phạm vi, override chỉ
áp dụng cho deliverable hiện tại.

## Routing skill

- Mọi yêu cầu tạo, tiếp tục, chỉnh sửa, tạo variant hoặc hoàn thiện hình minh
  họa truyện tranh mặc định đi qua `comic-page-guide`, kể cả khi người dùng đã
  nêu rõ page, frame hoặc deliverable.
- Chỉ dùng `comic-production` khi người dùng gọi đích danh skill đó hoặc yêu
  cầu rõ dùng `comic-production`; không tự động đọc hoặc gọi nó từ
  `comic-page-guide`.
- Đọc và kiểm chứng nguồn: `comic-source-reader`.
- Thiết kế storyboard/composition: `comic-shot-design`.
- Viết prompt: `comic-prompt-writer`.
- Tạo, chỉnh hoặc tạo variant ảnh: `comic-image-production`.
- Kiểm tra profile, style, context và storytelling: `comic-visual-qa`.
- Kiểm tra frame, text, trim, safe zone hoặc gáy: `comic-layout-qa`.
- Chuyển output đã chọn vào `approved/`: `comic-delivery`.

Chỉ dùng skill và reference cần cho deliverable. Không chạy layout QA cho
concept art, profile, style test hoặc ảnh chưa gắn layout.

## Khóa phong cách nền

Phong cách mặc định là thuần 2D animation: line art rõ, flat fills, 1–2 cấp
hard cel-shading, background cùng ngôn ngữ đồ họa. Cấm 2.5D/3D, CGI, bán hiện
thực, soft airbrush, texture thật, gradient nặng, bloom, volumetric light, DOF
và bokeh. Background chỉ được có chuyển màu rất nhẹ, tiết chế và đồ họa để gợi
thời điểm hoặc không khí.

Profile gốc trong đúng tập là chuẩn identity. Không dùng output trước làm chuẩn
thay thế và không cho nhân vật phụ mượn dấu hiệu đặc trưng của nhân vật chính.

## Quản lý file

- Dùng đường dẫn tương đối trong tài liệu và manifest nội bộ.
- Không sửa, di chuyển hoặc xóa profile, script nguồn hay layout khi chưa được yêu cầu.
- Không ghi đè output; luôn tạo version mới.
- Ảnh mới/variant nằm trong `outputs/` của đúng tập/page.
- Chỉ sau khi người dùng chọn rõ output đã QA, chuyển file đó vào `approved/`,
  cập nhật mọi đường dẫn liên quan và không giữ hai nguồn chuẩn.
- Không đưa file tạm, cache hoặc asset của tập khác vào deliverable cuối.
