---
name: comic-prompt-writer
description: Viết prompt tạo hoặc chỉnh ảnh từ storyboard/composition đã chọn cho project truyện tranh 2D. Dùng khi người dùng cần prompt hoàn chỉnh; không tự tạo ảnh hoặc thay đổi shot đã duyệt.
---

# Viết prompt ảnh truyện tranh

Nhận composition contract đã chọn và chuyển thành prompt hoàn chỉnh. Không tự
đổi focus, moment, camera, population plan hoặc profile.

Luôn đọc [pure-2d-style.md](references/pure-2d-style.md). Đọc
[prompt-contract.md](references/prompt-contract.md) để cấu trúc prompt và
[negative-constraints.md](references/negative-constraints.md) để chọn điều cấm.

Chỉ đưa vào prompt các kiểm tra `REQUIRED`. Không thêm constraint thuộc
`NOT_APPLICABLE` hoặc `SKIPPED_BY_USER`. Nếu người dùng nói “không cần tránh
gáy”, prompt không được lén dịch focus khỏi gáy.

Đưa prompt hoàn chỉnh trong một code block, không dùng dấu ba chấm thay nội dung.
