# Khóa thuần 2D animation

> Cập nhật người dùng 2026-10-29 — `SKIPPED_BY_USER`, toàn dự án:
> style duy nhất là **ttpq comic light** (`docs/style-ttpq-comic-light.md`,
> đường dẫn từ root). Các yêu cầu rendering, bảng trang sức/ref style cũ,
> override st03 và khối prompt style cũ bên dưới đã được thay thế; không
> copy các phần đó vào prompt mới. Workflow, identity và QA fidelity vẫn giữ.
> Chỉ khi ảnh có tu sĩ mới đọc `docs/monastic-robes.md` cho màu/cách quấn y.


- Nét viền rõ, sạch và nhất quán.
- Hình khối bằng mảng màu thiết kế rõ; cel-shading làm nền tảng.
- Cho phép chuyển sắc mềm nhẹ, cục bộ ở da/tóc/vải/vật liệu theo policy chung;
  không dùng lệnh ZERO gradients hoặc hard shadows only cho mọi thành phần.
- Da, tóc, vải và đạo cụ giữ ngôn ngữ đồ họa 2D.
- Background cùng ngôn ngữ nét và màu với nhân vật; mức chi tiết thay đổi theo
  lớp sâu và vùng chữ, không mặc định đơn điệu hoặc phẳng.
- Chiều sâu bằng bố cục, chồng lớp, tỷ lệ và giảm chi tiết.
- Giữ chi tiết tinh ở mắt, tóc, nếp vải và trang sức. Vật liệu dùng biến thiên
  màu lớn và dấu nét tiết chế; không đồng nhất giản lược với chất lượng 2D.

Cấm 2.5D/3D, bán hiện thực, CGI, texture ảnh, tạo khối liên tục kiểu render,
gradient nặng, bloom, lens flare, volumetric light, DOF, bokeh và background
kiểu ảnh/render. Đọc `docs/project-style-policy.md` của project để resolve mức
độ mềm; không dùng checklist cũ để áp lại yêu cầu tuyệt đối phẳng.
