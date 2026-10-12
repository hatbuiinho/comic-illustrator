# Variant và chỉnh sửa

- Giữ nguyên các phần người dùng yêu cầu giữ.
- Chỉ sửa mục tiêu đã nêu và các lỗi phụ phát sinh trực tiếp từ thay đổi đó.
- Mỗi variant có tên/version mới.
- Với nhân vật, luôn truyền lại profile gốc dù output trước nhìn gần đúng.
- Không tiếp tục sửa nối tiếp từ output đã drift identity; quay lại profile gốc
  và composition đã duyệt.
- Không tự chọn active output khi có trade-off thực tế.

Với sửa lỗi tự động, áp [retry-quality-contract.md](retry-quality-contract.md):
chọn transform/edit/fresh generation theo loại lỗi, ghi phần đã đạt phải giữ
và kiểm regression trước khi dùng bản sửa làm parent tiếp theo.
