# Page 6 — Khóa nguồn và ngữ cảnh

## G1 — Đã đối chiếu nguồn

- Tập 53, Part 1, trang PDF 6, tương ứng trang sách 14–15. Một hình liên tục ở phần dưới spread.
- Nguồn: `Tap 53/notes.md`, `Tap 53/shot_notes.md`, `Tap 53/workflow.md`, `Tap 53/workflow_schema.md`, `Tap 53/workflow_templates.md`, `Tap 53/storyboard_composition_reference.md`, `Tap 53/Part 1/scripts/chapter1.md`, PDF trong `Tap 53/Part 1/layouts/`.
- Đã đọc bằng `pdfinfo`, `pdftotext` trang 5–7 và đo hình chữ nhật bằng `pdfplumber`. PDF có 24 trang, spread 810,709 × 575,433 pt. Khung xanh: x=0; y=229,606; rộng=810,708; cao=345,827 pt. Tỷ lệ 2,344258:1. Đây là số đo nguồn PDF, không phải yêu cầu kích thước output.
- Raster kiểm chứng được render trực tiếp từ trang 6 của PDF và lưu trong thư mục storyboard của page.
- Index cũ còn hai phương án page 6 nhưng các output tương ứng không tồn tại. Không kế thừa duyệt, trạng thái QA hoặc ảnh cũ. Hồ sơ mới dùng mã riêng.

## contextSnapshot và narrativeInferenceLock

- Trước: nắng đã lên cao; Visakha cảm tạ những người đến giúp; Punna đề nghị lo ăn uống đầy đủ.
- Hiện tại: một canh giờ sau, gia nhân mang bánh trái, nước tới các lán/chòi; thợ và nông dân nghỉ tay, ngồi ăn uống cạnh nhau, trò chuyện thân tình.
- Sau: buổi chiều Nalini dẫn hai gia chủ khảo sát các hố móng đang đào dở.
- Xác nhận trực tiếp: bữa nghỉ, thức ăn, nước, lán/chòi, những người trước đây chưa quen ngồi bên nhau.
- Hàm ý mạnh: nắng ban ngày, sự mệt nhọc được xoa dịu, khoảng cách người lạ giảm đi. Không gán giờ đồng hồ cụ thể.
- Chưa xác định: chính xác số người, nội dung câu chuyện, loại bánh/trái cây, hình dáng từng lán. Đây là lựa chọn tạo hình, không coi là dữ kiện kịch bản.
- Không đưa vào shot: khảo sát buổi chiều, bức tường cũ, bí quyết gạch, xe chở đá, các tỳ kheo ni, chòi mới hứa dựng ngày mai.
- Visakha, Punna và Nalini không cần hiện trong hình; đoạn hiện tại không khẳng định họ đứng cạnh bữa nghỉ.

## backgroundContinuityLock và locationIdentityLock

- Địa điểm: khu nghỉ tạm của công trường tinh xá, giai đoạn đào móng.
- Bắt buộc: lán nhẹ hở bên trên nền đất; không gian ngoài lán còn là công trường chưa hoàn thiện.
- Danh mục neo: mái lá thô buộc vào cọc mảnh; mặt đất liên tục giữa chỗ nghỉ và khu thi công; mép hố móng cùng cọc đánh dấu ngoài lán. Hai neo đầu mạnh cho trung cảnh; cảnh rộng thêm neo thứ ba.
- Neo chung: cột gỗ mảnh buộc dây dưới mái lá hở bên. Hình dáng cụ thể là thiết kế giản lược được khóa cho page này.
- Có thể có: thúng bánh trái, bình nước đất nung, bóng mái dạng mảng phẳng.
- Cấm: tường xây mới, hàng cột kiến trúc hoàn thiện, nền lát, đại sảnh hay bàn tiệc; công trường hoàn thành; gia nhân quỳ phục hoặc người nhận bố thí.
- Đối chiếu trước/sau: trước còn đào và chuyển đất; ngay sau vẫn là hố móng đào dở. Các chòi đã tồn tại ở bữa nghỉ; lời hứa dựng thêm cuối chương không xóa các chòi hiện có.
- Kiểm tra loại bỏ: không cấm toàn bộ gỗ/cọc vì sẽ xóa neo lán; chỉ cấm kiến trúc cố định chưa tồn tại.

## geographyLock và visualComponentLock

- Ngoại cảnh: nền công trường rộng, tương đối bằng phẳng; chân trời thấp, trung tính. Không tự thêm núi, vách, hồ, sông hoặc rừng dày.
- Lán là kết cấu tạm nhẹ, không biến thành cung điện hoặc nhà hoàn thiện. Nền đất là mảng màu, không texture ảnh.
- Thúng là đồ đan giản lược, bánh và trái cây chỉ vài hình khối rõ; bình và cốc đất nung không bóng gương. Không có chai nhựa, khay kim loại hiện đại hoặc dao nĩa.
- Người, vật và nền cùng ngôn ngữ thuần 2D: nét rõ, màu phẳng, tối đa hai cấp bóng cứng; không blur, CGI hoặc ánh sáng render.

## Profile và điều kiện

- Đã xem `Tap 53/characters/thợ phụ.png`: chọn người số 3 cho người thợ — khăn nâu đỏ, tóc đen chạm vai, râu đen, áo kem, đai vàng, vải quấn nâu. Khi ngồi vẫn giữ tỷ lệ và nhận diện; dụng cụ lao động ngoài khung vì đang nghỉ.
- Đã kiểm tra `Tap 53/characters/Gia nhân.png`: đây là gia nhân của bà Matika ở câu chuyện khác, không dùng cho người phục vụ gia đình Visakha.
- Nông dân và hai gia nhân là nhân vật phụ vô danh chỉ cho shot này: không sao chép nhận diện nhân vật chính. Nông dân tóc ngắn hoa râm, mặt gầy, áo quấn xám tím; hai gia nhân lần lượt áo xanh xám/vải be và áo nâu nhạt/vải xám, tóc ngắn, không khăn đỏ/cam. Chưa có profile riêng; nếu dùng lặp lại ở shot sau phải lập profile trước.
- characterProportionLock: toàn người dùng cùng một tỷ lệ theo profile; không phóng đầu, ép vai, rút ngắn thân/tay để né gáy.
- causalStateLock: áp dụng cho hậu quả của việc lo ăn uống — người lao động đã nghỉ và thức ăn đã đến; không vẽ họ vừa đào đất vừa ăn. Không tự thêm tai nạn, đói lả hoặc kiệt sức.
- materialSemanticsLock: áp dụng cho lán tạm, bình đất và thúng; không có khối đá/gạch cần chứng minh trọng lượng.
- relationalFocusLock: hai người cùng ngồi, quan hệ ngang hàng, nhìn nhau; không quỳ nhận, chắp tay cảm tạ hoặc nhìn ra khán giả.
- gestureSemanticsLock: cốc/bánh là dấu hiệu bữa nghỉ; cử chỉ trò chuyện tiết chế, không lễ nghi hoặc tranh giành.

## printTrimLock

- Tỷ lệ xén theo trục khung: x=0,0104895; y=0,0147783. Critical-safe: x=0,0279720; y=0,0394089.
- Gáy dự phòng: x=0,47–0,53 toàn spread, chỉ dành nền đất/mái phụ; không để mặt, tay/cốc hoặc thúng kể chuyện đi qua.
- Vùng chữ nằm trên khung, giữ nguyên toàn bộ; không dùng nền ảnh mới phủ chữ.
- Cấp hiển thị do phương án quyết định. Mặt/đối nhìn cặp chính cần trọn; tay cầm thức ăn cần đọc; chân và dụng cụ có thể ngoài khung theo cỡ máy.

G1 đủ nguồn để thiết kế G2. Hình cuối chưa được tạo, chưa có kết luận QA output.

```text
Tiếp tục G2: page-006 / rest-meal
```
