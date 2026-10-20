# Policy phong cách toàn project

Nguồn: chuyển từ `AGENTS.md`, cập nhật theo quy chuẩn và ngoại lệ người dùng xác nhận.
Đọc policy này khi thiết kế hình, viết prompt, tạo ảnh hoặc visual QA. Các skill
tham chiếu policy chung khi thực thi; cập nhật quy chuẩn tại đây để tránh các
bản sao khác nhau. Ngoại lệ cấp tập hoặc yêu cầu trực tiếp của người dùng được
áp dụng theo thứ tự ưu tiên trong `AGENTS.md`.

Policy này cũng bắt buộc cho mọi ảnh trong Character Studio và Image Playground,
kể cả bản thử, character sheet và variant. Không cần người dùng nhắc lại trong
từng prompt; reference đầu vào không tự tạo ngoại lệ phong cách.

## Phong cách mặc định

Style mặc định toàn project là **[st03 — 2D mềm, màu tự nhiên cân bằng](style-st03.md)**,
được người dùng chọn ngày 2026-10-18, thay st02. Đọc định nghĩa và vai trò ảnh mẫu
tại tài liệu đó cùng policy này. st01 và st02 được giữ làm tham chiếu lịch sử.

Áp dụng st03 cho mọi lượt tạo/chỉnh ảnh mới trong flow minh họa tập/page/frame,
Character Studio và Image Playground, gồm bản thử, character sheet và variant;
không cần người dùng gọi lại tên style. Giữ identity theo profile gốc, thể hiện
bằng st03; không tự đổi thiết kế hoặc ghi đè profile.

### Thực thi trong prompt và QA

- Resolve style hiện hành trước thiết kế, viết prompt, tạo/chỉnh ảnh và QA.
  Prompt phải mô tả các yêu cầu st03 phù hợp cảnh, không chỉ ghi tên style:
  2D mềm với nét/mảng rõ, bề mặt sạch không hạt, màu tự nhiên cân bằng,
  xanh lá dịu khi xuất hiện và ánh sáng theo thời điểm/nguồn sáng thực tế.
- QA kiểm các yêu cầu trên ở từng nhóm hình đang có, đặc biệt grain/noise,
  ám xanh lam/cyan toàn cảnh, màu bị phủ vàng/cam và cảnh đêm sáng như ban ngày;
  đánh giá theo định nghĩa st03, không coi lỗi trong ảnh mẫu là đặc điểm cần giữ.
- Khi tiếp tục tác vụ cũ, cập nhật phần style của prompt/qaLocks cho lượt mới
  theo policy hiện hành; ghi style st03 và thay đổi so với lượt trước trong
  record. Prompt cũ và output trước không khóa style cũ cho lượt mới.
- Giữ nguyên ảnh, prompt, record và kết quả duyệt trước đây; không hồi tố kết
  quả QA hoặc tự chuyển đổi tài sản cũ. Output chỉnh mới luôn có version mới
  và qua bước chọn/duyệt đang áp dụng của workflow tương ứng.
- Nếu người dùng yêu cầu ngoại lệ rõ, ghi `SKIPPED_BY_USER` cùng phạm vi theo
  AGENTS.md; reference có style khác không tự tạo ngoại lệ.

2D animation với nét và mảng màu thiết kế dẫn hình; cel-shading là nền tảng,
không bắt mọi bề mặt phải tuyệt đối phẳng hoặc chỉ có cạnh bóng cứng. Cho phép
chuyển sắc mềm nhẹ, cục bộ ở da, tóc, nếp vải và vật liệu để giữ độ tinh tế,
miễn silhouette, nét, mảng sáng–tối chính và hierarchy vẫn đọc rõ như tranh 2D.
Giữ chi tiết đồ họa có giá trị: mắt, tóc, nếp vải, hoa văn và trang sức; không
giản lược chúng chỉ để đạt nhãn “phẳng”.

Vật liệu có thể dùng biến thiên màu lớn, tiết chế và vài dấu nét đặc trưng;
không dùng vi texture dày hoặc vân mô phỏng ảnh thật. Đánh giá shading theo
hiệu quả tổng thể: một chuyển sắc nhẹ không tự tạo FAIL; tạo khối liên tục
kiểu render, bóng/highlight mô phỏng vật liệu thật hoặc airbrush lấn át nét
và mảng thiết kế mới là drift.

Cấm 2.5D/3D, CGI, bán hiện thực, texture ảnh, gradient nặng, bloom, volumetric
light, DOF và bokeh. Background cùng ngôn ngữ đồ họa với nhân vật; mức chi tiết
và độ mềm thay đổi theo lớp sâu và focus, không được bán thực hơn nhân vật.

Nguồn cập nhật: người dùng xác nhận nới nhẹ 2D để chi tiết mềm hơn và triển khai
vào workflow chung ngày 2026-10-11. Đây là mặc định mới của project, không chỉ
là override cho một page. Profile gốc tiếp tục là chuẩn identity.

## Ngoại lệ nền trời

Người dùng xác nhận ngày 2026-10-02, phạm vi toàn project:
`SKIPPED_BY_USER` đối với việc cấm tuyệt đối nền trời mềm. Nền trời được phép
có chuyển màu mềm nhẹ và tiết chế để gợi thời điểm hoặc không khí. Ngoại lệ
không tự cấp phép shading cho nhân vật hay vật thể; các thành phần đó theo
mặc định cập nhật ở trên. Ngoại lệ không cho phép tạo khối kiểu render,
gradient nặng, bloom, volumetric light, DOF, bokeh, CGI hoặc bán hiện thực.
