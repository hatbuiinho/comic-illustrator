# Crop, che khuất và biên hòa giấy

Đọc khi nhân vật bị cắt, đặc biệt với cảnh không có hard frame. Áp dụng từ
composition đến artwork; không chờ generation để giải quyết kết thúc phần thân.

## Điểm cắt và ba cơ chế khác nhau

- `cameraCrop`: phần cơ thể tiếp tục ngoài mép giấy/trang thành phẩm. Với inset
  hoặc panel có khung/mask thật, điểm cắt là biên khung/mask đó. Phải đặt chủ thể
  chạm và đi qua biên này trong composition; không tự khai báo một biên camera
  tưởng tượng giữa trang. Mép crop khi in là trim; artwork cần đủ bleed theo layout.
  `briefRegion`, footprint cảnh, text frame, safe zone và gáy không phải biên crop.
- `occlusion`: cơ thể tiếp tục phía sau vật thể/foreground nhìn thấy; ghi vật
  che và quan hệ trước–sau. Không thêm vật che trái nguồn chỉ để cứu crop.
- `paperFade`: nền cảnh hòa vào nền giấy; không phải cơ chế cắt cơ thể. Không
  làm thân biến mất giữa trang bằng fade, sương, đất, chữ hoặc mask đồ họa.
  Ngoại lệ cắt thân bằng biên đồ họa chỉ áp dụng khi người dùng yêu cầu rõ cho
  deliverable đó; ghi `SKIPPED_BY_USER` cùng phạm vi, không tự suy từ mode hòa giấy.

Khi cần cảnh gần hoặc crop eo, thiết kế placement để phần thân ngoài hình đi
qua mép trang hoặc khung inset thật. Không thêm khung để hợp thức hóa crop nếu
nguồn/người dùng chưa chọn khung. Không chuyển sang toàn thân, thêm chân hoặc
thu nhỏ nhân vật chỉ để né lỗi crop; đánh giá lại camera/staging theo cảm xúc và
không gian trang trước khi chọn cách sửa.

Với từng chủ thể bị cắt, ghi `cropReadPlan` trong storyboard và
`selectedPageComposition`: actor ID, phần còn thấy, cơ chế, biên/vật che,
loại biên (`PAGE_TRIM` hoặc `INSET_FRAME`), cạnh và tọa độ/ID khung khi camera crop,
quan hệ với mặt đất và diễn xuất phải giữ. Không gọi thân kết thúc giữa đất là
camera crop ngang eo. Không mặc định bỏ đất hoặc chuyển toàn thân cho mọi cảnh.

Nếu crop không đọc tự nhiên trong lock hiện hành, sửa composition trước prompt.
Thay camera, crop, staging hoặc cơ chế kết thúc silhouette đã duyệt cần preview
revision và xác nhận lại. Không âm thầm sửa shot trong vòng production.

## Cổng review trước production

Xem preview toàn cảnh và crop chỗ kết thúc thân, gồm nền/vật che. Kiểm:

- `cropRead`: phần thân đi qua mép trang/khung inset thật hoặc tiếp tục sau
  vật che nhìn thấy; FAIL nếu thân bị cắt giữa trang mà không có biên thật hay
  ngoại lệ rõ của người dùng, kể cả khi không đọc thành lún/chôn trong đất;
- `groundPlaneContinuity`: mặt đất, tỷ lệ và lớp sâu hợp lý; đất không chạy
  ngang eo người đứng trong cùng cảnh;
- `occlusionLogic`: vật che và quan hệ trước–sau có bằng chứng nhìn thấy;
  `NOT_APPLICABLE` nếu không dùng che khuất.

Check áp dụng thiếu bằng chứng không được PASS. Preview bị lún trả
`COMPOSITION_NEEDS_REVISION` trước cổng duyệt; render thành công hoặc nhãn shot
size không thay review. Artwork sai plan sửa production; plan sai/không khả thi
quay lại composition. Đây là storytelling/không gian, không phải anatomy QA.
Không dùng chữ, mask hay fade hậu kỳ để che lỗi.

Semantic chỉ truyền camera, staging, tỷ lệ tương đối, gesture, silhouette có ý
nghĩa và eye path. Polygon thô không phải khuôn contour production. Giữ tín hiệu
kể chuyện đã duyệt, cho phép hoàn thiện nét, nếp vải và biểu cảm theo profile;
không yêu cầu redraw inside exact semantic silhouette.
