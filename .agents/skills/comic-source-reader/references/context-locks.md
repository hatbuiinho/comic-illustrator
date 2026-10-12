# Khóa context có điều kiện

Chỉ lập khóa liên quan đến deliverable:

- `contextSnapshot`: thời điểm, người hiện diện, trạng thái hiện tại, việc đã
  xảy ra và chi tiết tương lai bị cấm.
- `backgroundContinuityLock`: chỉ khóa dữ kiện nền có ảnh hưởng context, gồm
  `mustMatch`, `mustNotShow` và provenance. Không dùng lock này để giới hạn độ
  phong phú, số lớp sâu, crop, nhịp mảng hoặc chi tiết phụ hợp bối cảnh.
- `geographyLock`: địa hình, đường chân trời, quy mô không gian và địa hình cấm.
- `visualComponentLock`: loại vật, tỷ lệ, silhouette, trạng thái và cách đọc sai.
- `causalStateLock`: nguyên nhân, trạng thái kết quả và khoảnh khắc được vẽ.
- `materialSemanticsLock`: lớp vật liệu, quy mô, bề mặt và trạng thái.

Nếu nguồn không xác nhận địa hình cụ thể, được thiết kế không gian hợp bối cảnh
bằng chồng lớp, tỷ lệ, cây cối, kiến trúc hoặc vật dụng phụ miễn không tạo
landmark, địa hình hay trạng thái mang ý nghĩa continuity chưa được chứng minh.
Ghi phần tự do đó trong `freeToDesign`; không biến thiếu dữ kiện thành yêu cầu
nền phẳng hoặc đường chân trời trung tính.

## Topography và đường chân trời

Khi location ảnh hưởng background, khóa riêng `topographyLock`: bằng phẳng, dốc,
đồi, núi, sông hoặc không xác định. Không suy “địa hình xa”, đồi hay núi từ một
bối cảnh ngoài trời chung. Nếu nguồn không xác nhận, ghi `UNKNOWN` và prompt
không được thêm đặc điểm địa hình nổi bật. Một correction trực tiếp của người
dùng trở thành source lock của deliverable hiện tại.
