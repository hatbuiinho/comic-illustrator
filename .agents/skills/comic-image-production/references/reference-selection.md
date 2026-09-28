# Chọn reference

Ưu tiên filesystem theo thứ tự:

1. Profile gốc của đúng nhân vật trong đúng tập.
2. `style_refs/approved/` của đúng tập.
3. Layout hoặc composition card đã được chọn.
4. Output đã duyệt rõ chỉ cho mục đích được người dùng xác nhận.

Đối chiếu `style_refs/rejected/` nếu tồn tại để tránh đặc điểm sai. Không lấy
asset của tập khác hoặc ảnh gần nhất trong chat khi đã có file tương ứng.
