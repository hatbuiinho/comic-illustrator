---
name: comic-visual-qa
description: Kiểm tra output truyện tranh về focus, profile, thuần 2D, context, location, anatomy và storytelling. Không dùng để kiểm tra hình học layout nếu ảnh chưa gắn với layout.
---

# Visual QA

Kiểm tra theo thứ tự: focus → profile → thuần 2D → context → location → anatomy
→ storytelling. Không lấy prompt làm bằng chứng; chỉ dùng output nhìn thấy và
nguồn gốc.

Đọc reference đúng mục tiêu:

- [style-qa.md](references/style-qa.md)
- [profile-qa.md](references/profile-qa.md) khi có nhân vật
- [location-qa.md](references/location-qa.md) khi background mang identity
- [storyboard-qa.md](references/storyboard-qa.md) khi đối chiếu composition

Mỗi check trả `PASS`, `FAIL`, `NOT_APPLICABLE` hoặc `SKIPPED_BY_USER`. “Không
chắc” với check `REQUIRED` được coi là FAIL. Không chạy layout QA ở đây.
