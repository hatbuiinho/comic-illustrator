# Điều cấm phải có trong prompt từ đầu

Nguồn: chuyển từ `AGENTS.md`.

- Áp dụng cho mọi workflow tạo/chỉnh ảnh trong toàn dự án, gồm minh họa tập,
  Character Studio và Image Playground, cả bản thử và variant.
- Trước mỗi lượt, xác định các điều cấm đang áp dụng từ yêu cầu người dùng,
  nguồn/brief, skill và policy theo thứ tự ưu tiên của project; đưa chúng thành
  ràng buộc rõ, cụ thể trong prompt thực tế trước khi gửi tạo/chỉnh ảnh.
  Không chỉ để điều cấm trong checklist QA hoặc coi tên style là đủ.
- Chỉ đưa các điều cấm phù hợp với đối tượng/vùng thực sự xuất hiện; giữ đúng
  ngoại lệ và `SKIPPED_BY_USER`, không áp lại điều người dùng đã miễn.
- Kiểm prompt trước khi gửi để bảo đảm đã có các điều cấm áp dụng. QA sau tạo
  kiểm lại cùng các ràng buộc, không thay thế bước phòng ngừa trong prompt.
  Lưu prompt thực tế theo record của workflow để có thể đối chiếu.
