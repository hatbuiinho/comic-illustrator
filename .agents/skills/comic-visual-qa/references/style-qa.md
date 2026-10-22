# Style QA

Resolve chuẩn tại `docs/project-style-policy.md` của project trước review;
reference này quy định cách đánh giá, không lập mức shading riêng.

Áp dụng [contract kiểm hình dùng chung](../../../../docs/visual-review-contract.md)
để kiểm các vùng mặt/vật liệu, ref contamination và phần cần giữ khi sửa.
Contract không thay fast gates hay mở anatomy/layout QA ở skill này.

PASS khi nét, silhouette và mảng màu thiết kế dẫn hình; shading và chi tiết
cùng ngôn ngữ 2D. Cel-shading có thể kết hợp chuyển sắc mềm nhẹ, cục bộ theo
policy. Không FAIL chỉ vì có gradient, nhiều hơn hai sắc độ hoặc vật liệu có
biến thiên màu tiết chế. Không chữa style bằng xóa nếp vải, tóc, trang sức hoặc
biến mọi đá thành khối hộp đều nhau.

FAIL khi CGI/3D/2.5D, tạo khối sáng–tối liên tục kiểu render, highlight/vân
mô phỏng vật liệu thật, texture ảnh dày, gradient nặng, bloom, volumetric light,
DOF, bokeh hoặc background bán hiện thực lấn át thiết kế 2D.

## Kiểm theo từng nhóm hình

Không cho PASS chỉ vì nhân vật có outline. Chạy `styleConsistencyByElement` cho
ít nhất: nhân vật, da/tóc/vải, đạo cụ chính, vật liệu kể chuyện (đá/gạch/gỗ),
xe/công cụ và background tự nhiên khi xuất hiện. Với mỗi nhóm, nêu bằng chứng:

- nét và các mảng chính có còn chi phối hình hay không;
- độ mềm có cục bộ, tiết chế và phục vụ hình hay đã thành tạo khối kiểu render;
- dấu nét/biến thiên màu có gợi vật liệu bằng thiết kế hay mô phỏng ảnh thật;
- mức chi tiết, tương phản và shading có nhất quán với hierarchy của cả cảnh.

Outline riêng lẻ không chứng minh 2D, cũng như màu phẳng riêng lẻ không chứng
minh hình đẹp. Trả `STYLE_2D_MATERIAL_DRIFT` hoặc
`STYLE_INCONSISTENT_BACKGROUND` khi có dấu hiệu cụ thể tương ứng. Delta sửa
chỉ nhắm vùng drift, đồng thời bảo vệ chi tiết và độ mềm còn hợp policy.
