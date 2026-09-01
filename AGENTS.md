# Comic Illustration Project

## Phạm vi

File này áp dụng cho toàn bộ repository và mọi tập truyện hiện tại hoặc được
thêm sau này. Mỗi thư mục tập là một đơn vị nội dung độc lập. Không mặc định
rằng quy tắc, nhân vật, bối cảnh hoặc tài sản của một tập được dùng cho tập khác.

## Nguồn hướng dẫn của từng tập

Trước khi phân tích page, viết scene, chọn shot, viết prompt hoặc tạo/chỉnh ảnh:

1. Xác định chính xác thư mục tập đang được yêu cầu, ví dụ `Tap 53/`.
2. Đọc đầy đủ `<thu-muc-tap>/notes.md` nếu file tồn tại.
3. Đọc đầy đủ `<thu-muc-tap>/shot_notes.md` nếu file tồn tại.
4. Đọc phần kịch bản liên quan và ngữ cảnh ngay trước/sau scene.
5. Kiểm tra file dàn trang, profile nhân vật và các tài sản liên quan trong
   chính thư mục tập đó.

`notes.md` là nguồn sự thật chính của tập về dàn trang, frame, tỷ lệ, gáy sách,
profile, bối cảnh, phong cách và quy trình. `shot_notes.md` là nguồn sự thật về
storyboard, ngôn ngữ điện ảnh, điểm nhìn, nhịp shot và quan hệ giữa hình với chữ.

Nếu một tập chưa có một trong hai file, vẫn áp dụng quy tắc chung trong file
này và nói rõ hướng dẫn cấp tập nào đang thiếu trước khi làm công việc phụ thuộc
vào nó. Không tự lấy `notes.md`, `shot_notes.md`, profile hoặc layout từ tập khác
để thay thế.

## Thứ tự ưu tiên

Khi có xung đột, áp dụng theo thứ tự:

1. Yêu cầu trực tiếp mới nhất của người dùng.
2. `notes.md` của đúng tập đang làm.
3. `shot_notes.md` của đúng tập đang làm.
4. Quy tắc chung trong `AGENTS.md` này.
5. Giả định sáng tạo của Codex.

Không bỏ qua hướng dẫn chỉ vì một phương án khác trông đẹp, hoành tráng hoặc
điện ảnh hơn.

## Khóa phong cách: thuần 2D animation

Phong cách mặc định và bắt buộc của toàn project là **thuần 2D animation**:

- nét viền rõ, sạch và nhất quán;
- hình khối được diễn đạt bằng mảng màu phẳng;
- cel-shading giới hạn, thường 1-2 cấp, cạnh bóng rõ;
- khuôn mặt, tóc, da, vải và đạo cụ giữ ngôn ngữ tạo hình đồ họa 2D;
- background phải cùng ngôn ngữ nét vẽ, màu và độ giản lược với nhân vật;
- chiều sâu được tạo bằng bố cục, chồng lớp và giảm chi tiết, không bằng hiệu
  ứng ống kính hoặc render 3D.

Các đặc điểm sau bị xem là sai style, kể cả khi hình trông đẹp:

- 2.5D, 3D render hoặc bán hiện thực;
- tạo khối mềm kiểu CGI hoặc digital painting;
- da có lỗ chân lông, texture chân thực hoặc độ bóng vật liệu;
- soft airbrush shading, gradient-heavy shading hoặc ánh sáng bóng bẩy;
- volumetric light, god rays, bloom, lens flare;
- depth of field, bokeh hoặc background mờ kiểu máy ảnh;
- nhân vật 2D đặt trên background bán thực/3D;
- tỷ lệ, khuôn mặt hoặc trang phục bị "realistic hóa" so với profile.

Không dùng ảnh trong `outputs/` làm style reference mặc định. Chỉ dùng một ảnh
output làm mẫu khi người dùng đã xác nhận rõ ảnh đó đạt style. Khi có thư mục
`style_refs/approved/` và `style_refs/rejected/`, ưu tiên đối chiếu cả hai:
khớp nhóm approved và tránh các đặc điểm của nhóm rejected.

## Storyboard và focus

- Mỗi ảnh là một shot storyboard, không phải bản tóm tắt cả đoạn văn.
- Mỗi shot chỉ có một trọng tâm kịch tính và một focus thị giác chính.
- Chọn một khoảnh khắc cụ thể: trước, trong hoặc sau hành động.
- Chỉ giữ nhân vật, phản ứng và chi tiết phụ thực sự hỗ trợ focus.
- Không nhồi nhiều thời điểm, nhiều hành động nối tiếp hoặc mọi tình tiết vào
  cùng một scene.
- Hình nên bổ sung cho chữ: có thể cho thấy cảm xúc, dư âm, hệ quả hoặc dấu vết
  thay vì lặp lại nguyên văn sự kiện đã được kể.
- Dùng khoảng trống như một phần của nhịp kể chuyện.
- Các shot liên tiếp cần thay đổi hợp lý về cự ly, hướng nhìn hoặc điểm nhìn,
  nhưng không hy sinh tính liên tục của nhân vật và không gian.

## Layout, frame và gáy sách

- Luôn đọc file dàn trang và đo đúng tỷ lệ frame mục tiêu trước khi tạo ảnh.
- Thiết kế bố cục theo tỷ lệ đó ngay từ prompt; không dựa vào crop mạnh để sửa
  một ảnh tạo sai tỷ lệ.
- Xác định frame là full spread, nửa spread, hình chen hay cụm nhiều hình.
- Xác định chính xác vị trí gáy và vùng an toàn.
- Không đặt mặt, mắt, bàn tay, đạo cụ, chữ trong cảnh hoặc chi tiết kể chuyện
  quan trọng vào gáy sách.
- Nếu ảnh trải qua hai trang, coi đó là một spread liên tục nhưng giữ focus ra
  khỏi vùng gáy.
- Nếu một vùng xanh chứa nhiều ảnh, coi từng ảnh là một shot riêng có logic nối
  tiếp; không biến chúng thành montage trong một ảnh.
- Giữ khoảng thở cần thiết cho text và ưu tiên khả năng dàn trang hơn một bố cục
  đẹp nhưng khó sử dụng.

## Profile và tính liên tục của nhân vật

- Profile trong thư mục tập là chuẩn tuyệt đối cho đúng nhân vật đó.
- Giữ ổn định khuôn mặt, tuổi, tỷ lệ cơ thể, tóc, trang sức, trang phục, màu vải
  và silhouette xuyên suốt các shot.
- Không cho nhân vật phụ mượn khuôn mặt, tóc, khăn, trang sức, bảng màu hoặc
  silhouette đặc trưng của nhân vật chính.
- Không tự thiết kế lại, hiện đại hóa, fantasy hóa hoặc đổi nguồn gốc hình thể
  của nhân vật.
- Khi thiếu góc nhìn/profile cần thiết cho nhân vật xuất hiện lặp lại, nói rõ
  phần còn thiếu trước khi tạo hàng loạt ảnh liên tiếp.

## Bối cảnh và tính đúng thời điểm

- Đọc ngữ cảnh trước/sau để biết đúng thời điểm, ánh sáng, trạng thái không gian
  và nhân vật đang có mặt.
- Background chỉ chứa những chi tiết phù hợp với đúng thời điểm của scene.
- Không đưa một hành động, công trình, đạo cụ hoặc trạng thái xảy ra ở page sau
  vào scene hiện tại.
- Bối cảnh có nhiệm vụ hỗ trợ focus, không phải phô bày toàn bộ world-building.
- Tuân thủ bối cảnh lịch sử và văn hóa được quy định trong `notes.md` của tập.

## Quy trình bắt buộc khi tạo ảnh

1. Xác định tập, part, page và frame cần làm.
2. Đọc `notes.md` và `shot_notes.md` của tập.
3. Đọc kịch bản liên quan cùng ngữ cảnh trước/sau.
4. Kiểm tra dàn trang; ghi nhận tỷ lệ frame, vùng text, gáy và safe zone.
5. Kiểm tra profile của tất cả nhân vật chính xuất hiện.
6. Xác định một câu mô tả focus, khoảnh khắc và điểm nhìn của shot.
7. Viết prompt khóa tỷ lệ, profile, thuần 2D và các chi tiết phải tránh.
8. Tạo từng shot/variant riêng; không dùng một ảnh nhiều cảnh thay cho nhiều
   deliverable khác nhau.
9. Kiểm tra output theo thứ tự: focus -> profile -> thuần 2D -> context -> tỷ lệ
   và gáy -> khả năng đặt cùng text.
10. Lưu ảnh được chọn vào `<thu-muc-tap>/outputs/` với tên không ghi đè file cũ,
    trừ khi người dùng yêu cầu thay thế.

## Kiểm tra thuần 2D trước khi bàn giao

Trước khi coi ảnh là đạt, trả lời tất cả câu hỏi sau:

- Line art có rõ và đồng nhất với profile không?
- Màu và bóng có phải mảng phẳng/cel-shading không?
- Da, tóc và vải có tránh cảm giác render 3D không?
- Background có cùng ngôn ngữ 2D với nhân vật không?
- Có hiệu ứng ánh sáng, blur hoặc texture nào đẩy ảnh sang 2.5D không?
- Profile, focus, tỷ lệ frame và vùng gáy có đúng không?

Nếu bất kỳ câu trả lời nào không chắc chắn, ảnh chưa đạt và cần sửa trước khi
đề xuất làm phương án chính.

## Quản lý file

- Dùng đường dẫn tương đối bên trong repository trong tài liệu và quy trình.
- Không sửa, di chuyển hoặc xóa profile, script hay layout nguồn nếu người dùng
  không yêu cầu rõ.
- Không ghi đè output đã có; tạo phiên bản mới.
- Giữ tài sản và output của từng tập trong đúng thư mục tập đó.
- Không đưa file tạm, cache hoặc tài sản của tập khác vào deliverable cuối.
