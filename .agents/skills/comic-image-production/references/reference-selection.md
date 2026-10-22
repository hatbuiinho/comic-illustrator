# Chọn reference

Ảnh mẫu st03 dùng chung được lưu trong [style-st03/](style-st03/README.md),
được Git theo dõi. Lấy vai trò và giới hạn từ
[định nghĩa st03](../../../../docs/style-st03.md) và
[policy phong cách](../../../../docs/project-style-policy.md).

Ưu tiên filesystem theo thứ tự:

1. Profile gốc của đúng nhân vật trong đúng tập.
2. `style_refs/approved/` của đúng tập.
3. Layout hoặc composition card đã được chọn.
4. Output đã duyệt rõ chỉ cho mục đích được người dùng xác nhận.

Đối chiếu `style_refs/rejected/` nếu tồn tại để tránh đặc điểm sai. Không lấy
asset của tập khác hoặc ảnh gần nhất trong chat khi đã có file tương ứng.

Với mỗi reference truyền vào model, ghi path, vai trò và phạm vi ảnh hưởng:
`layout` chỉ canvas/typography/geometry; `identity` chỉ nhân vật được chỉ định;
`style` chỉ ngôn ngữ tạo hình; `composition` chỉ staging/pose đã chọn. Một ảnh
có nhiều vai trò chỉ khi nguồn xác nhận rõ. Không lấy nhân vật trong layout
làm identity hay để style reference thay trang phục/profile.

Vai trò là chỉ dẫn, không bảo đảm model tách được ảnh hưởng. Kiểm thuộc tính
bị lẫn sau tạo theo [contract kiểm hình](../../../../docs/visual-review-contract.md),
không dùng việc đã truyền đúng ref làm bằng chứng identity/style PASS.
