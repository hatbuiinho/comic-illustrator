---
name: comic-delivery
description: Hoàn tất và lưu bản minh họa truyện tranh đã được QA và người dùng chọn, gồm version, approved và cập nhật đường dẫn. Chỉ dùng sau xác nhận rõ; không dùng để tự chọn output.
---

# Bàn giao output

Đọc [status-model.md](references/status-model.md) và
[approval-policy.md](references/approval-policy.md).

Chỉ thực hiện khi:

- output bắt buộc tồn tại;
- visual QA bắt buộc đã PASS;
- layout QA đã PASS, hoặc là `NOT_APPLICABLE`, hoặc các check liên quan được
  người dùng ghi rõ `SKIPPED_BY_USER`;
- người dùng đã chọn đúng output khi có variant.

Chuyển file đã chọn từ `outputs/` sang `approved/` trong đúng page/tập. Giữ tên
version; nếu đích tồn tại, dừng và tạo version mới, không ghi đè. Cập nhật mọi
manifest và đường dẫn tiêu thụ. Không để hai bản sao cùng đóng vai trò nguồn chuẩn.
