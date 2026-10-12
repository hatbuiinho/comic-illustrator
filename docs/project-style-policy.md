# Policy phong cách toàn project

Nguồn: chuyển từ `AGENTS.md`, cập nhật theo quy chuẩn và ngoại lệ người dùng xác nhận.
Đọc policy này khi thiết kế hình, viết prompt, tạo ảnh hoặc visual QA. Các skill
tham chiếu policy chung khi thực thi; cập nhật quy chuẩn tại đây để tránh các
bản sao khác nhau. Ngoại lệ cấp tập hoặc yêu cầu trực tiếp của người dùng được
áp dụng theo thứ tự ưu tiên trong `AGENTS.md`.

## Phong cách mặc định

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
