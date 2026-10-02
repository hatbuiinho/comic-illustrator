---
name: comic-visual-qa
description: Kiểm tra output truyện tranh về focus, profile, thuần 2D, context, location, anatomy và storytelling. Không dùng để kiểm tra hình học layout nếu ảnh chưa gắn với layout.
---

# Visual QA

Kiểm tra theo thứ tự: focus và ưu tiên cảm xúc → profile → thuần 2D → context →
location → anatomy → storytelling và mức độ tiết chế. Không lấy prompt làm
bằng chứng; chỉ dùng output nhìn thấy và nguồn gốc.

Đọc reference đúng mục tiêu:

- [style-qa.md](references/style-qa.md)
- [profile-qa.md](references/profile-qa.md) khi có nhân vật
- [location-qa.md](references/location-qa.md) khi background mang identity
- [storyboard-qa.md](references/storyboard-qa.md) khi đối chiếu composition

Mỗi check trả `PASS`, `FAIL`, `NOT_APPLICABLE` hoặc `SKIPPED_BY_USER`. “Không
chắc” với check `REQUIRED` được coi là FAIL. Không chạy layout QA ở đây.

Không đánh FAIL một yếu tố `implicitReadable` chỉ vì nó không được thể hiện
trọn vẹn. Đánh giá khả năng suy ra từ toàn bộ hình và chỉ FAIL khi tổng thể dẫn
đến cách hiểu sai, không đủ tín hiệu hoặc mâu thuẫn nguồn. Đồng thời kiểm tra
việc diễn giải quá mức: hành động, biểu cảm hay chi tiết phụ không được phóng
đại đến mức tranh focus, làm mất tự nhiên hoặc thu hẹp khoảng trống cho người
đọc.
