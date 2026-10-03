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

Khi composition có `continuityDependencies`, chạy thêm:

- `continuityReadCheck`: output có đúng các physical, knowledge, relationship,
  location và temporal state đã đọc hay không;
- `continuityWriteCheck`: output có vô tình tạo thay đổi hoặc tiết lộ chi tiết
  không thuộc moment hiện tại hay không;
- `forbiddenCheck`: chi tiết bị cấm xuất hiện sớm hoặc trạng thái sai có hiện
  diện hay không.

Không lấy việc prompt bỏ sót một vật làm lý do bỏ qua check nếu vật đó nằm trong
`mustNotChange` hoặc `forbidden`. Kết quả QA chỉ báo cáo bằng chứng nhìn thấy;
không tự ghi continuity ledger.

Sau khi hoàn tất đánh giá bằng mắt, có thể lưu report JSON và chạy
`scripts/validate-visual-qa.js <visual-qa.json>` để kiểm completeness, trạng
thái input và coverage của continuity dependency. Script không thay thế đánh
giá focus, anatomy, identity hay cảm xúc.

Không đánh FAIL một yếu tố `implicitReadable` chỉ vì nó không được thể hiện
trọn vẹn. Đánh giá khả năng suy ra từ toàn bộ hình và chỉ FAIL khi tổng thể dẫn
đến cách hiểu sai, không đủ tín hiệu hoặc mâu thuẫn nguồn. Đồng thời kiểm tra
việc diễn giải quá mức: hành động, biểu cảm hay chi tiết phụ không được phóng
đại đến mức tranh focus, làm mất tự nhiên hoặc thu hẹp khoảng trống cho người
đọc.
