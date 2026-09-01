# Tập 53 Notes

## Mục tiêu sử dụng file dàn trang

- File PDF dàn trang là bản demo để nối script chữ với chỉ dẫn minh họa, không phải bản truyện xuất bản cuối.
- Mỗi page trong file dàn trang tương ứng với một spread gồm 2 trang sách, có gáy sách ở giữa.
- Các khối xanh được xem là vùng ảnh mục tiêu để tạo minh họa và đặt vào layout.

## Cách hiểu màu sắc trong file dàn trang

- Màu xanh: nội dung liên quan đến minh họa, brief hình ảnh, hoặc vùng chờ đặt ảnh.
- Khối xanh lớn: diện tích hình ảnh chính, có thể là full spread, nửa spread, hoặc một cụm hình.
- Hình tròn xanh: vị trí chèn một hình nhỏ, điểm nhấn, hoặc cảnh chuyển.
- Chữ hồng: nhấn mạnh cảm xúc, hành động, hoặc đoạn cần ưu tiên thể hiện bằng hình.
- Highlight vàng: ý quan trọng từ kịch bản gốc, cần ưu tiên đưa vào hình hoặc bố cục.
- Ghi chú "không hình": trang đó chỉ cần chữ, không tạo minh họa.

## Nguyên tắc tạo ảnh từ frame xanh

- Luôn dựa theo kích thước và tỉ lệ của frame xanh, không tạo ảnh theo tỉ lệ tùy ý.
- Trước khi tạo ảnh, phải đo và ghi nhận tỉ lệ chính xác của frame xanh trong PDF. Prompt và bố cục phải được thiết kế trực tiếp theo tỉ lệ này ngay từ đầu, đặc biệt với các frame rất ngang hoặc rất dọc.
- Không được dựa vào việc crop ảnh đã tạo như cách chính để đưa về đúng tỉ lệ frame, vì crop có thể làm cắt mặt, tay, đạo cụ, hành động, hoặc phá bố cục. Chỉ crop rất nhẹ khi đã được tính trước và không làm thay đổi bố cục kể chuyện.
- Phong cách ảnh mặc định cho project này là 2D animation style, ưu tiên cảm giác truyện tranh hoạt hình rõ ràng, không đi theo hướng bán thực.
- Ảnh và chữ phải mix hài hòa, nghĩa là hình không được tranh chỗ toàn bộ phần chữ nếu page đó cần để text thở, title, hoặc đoạn mở đầu.
- Khi frame xanh nằm ở mép dưới, mép bên, hoặc chiếm nửa trang, cần giữ nhân vật, vật thể chính, và điểm nhìn trong vùng an toàn.
- Với frame nhỏ, hẹp, oval, tròn, hoặc hình chèn, phải nén kịch bản để tiết kiệm không gian: ưu tiên close-up, medium close-up, over-the-shoulder, một cử chỉ, một đối nhìn, hoặc một dấu vết có ý nghĩa. Tránh toàn thân, nhiều nhân vật đứng xa nhau, establishing shot, và quá nhiều hành động trong cùng một hình.
- Khi frame dàn trang là oval hoặc hình tròn, ảnh output vẫn phải là ảnh chữ nhật đầy đủ, không vẽ theo mặt nạ oval/tròn và không cắt bỏ bố cục để giả lập hình đó. Người dàn trang sẽ tự crop hoặc mask sau; vì vậy cần để subject và chi tiết chính trong vùng an toàn bên trong hình oval/tròn dự kiến, nhưng các mép ảnh vẫn là nền liền mạch và có thể dùng được.
- Không gian hẹp cần có một chủ thể chính và một phản ứng hỗ trợ. Bối cảnh chỉ nên là vai trò gợi ý bằng một vài chi tiết, không cần hiện đầy đủ.
- Không đặt mặt, tay, đạo cụ quan trọng, chữ viết trên biển hiệu, hoặc chi tiết kể chuyện quan trọng vào đúng khu gáy sách.
- Nếu ảnh trải qua cả hai trang, cần thiết kế như một spread liền mạch, nhưng tránh để subject bị cắt bởi gáy.
- Nếu bố cục là 2 hình hoặc nhiều hình trong cùng một vùng xanh, cần nghĩ từng hình như từng shot riêng có logic nối tiếp.

## Nguyên tắc storyboard và điện ảnh

- Mỗi scene được xây dựng như một shot trong storyboard, không chỉ là một ảnh minh họa chung chung.
- Mỗi shot cần rõ 4 thứ: chủ thể chính, hành động, góc máy, và cảm xúc.
- Hướng của hành động phải đúng với ý nghĩa trong kịch bản: nếu nhân vật cầu nguyện, cử chỉ, ánh mắt và hướng thân người phải hướng đến đối tượng được cầu nguyện, không hướng thẳng vào người đọc, trừ khi kịch bản chủ ý phá vỡ góc nhìn thứ tư.
- Ưu tiên ngôn ngữ điện ảnh: establishing shot, medium shot, close-up, over-the-shoulder, low angle, high angle, cutaway, transition shot khi phù hợp.
- Hình phải phục vụ nhịp kể chuyện: mở cảnh, nhấn cảm xúc, mở rộng không gian, đối nhìn, nhấn vào hành động, hoặc chuyển cảnh.
- Không cần minh họa tất cả các hành động theo từng bước. Ưu tiên chọn khoảnh khắc có dư âm, kết quả, hoặc dấu vết của hành động đã xảy ra để người đọc tự suy ra; tránh biến ảnh thành sơ đồ kể việc và làm cạn cảm xúc.
- Khi một hành động chăm sóc, hy sinh, hay quyết định đã được kể bằng chữ, có thể thể hiện tác động của nó lên con người và không khí thay vì lặp lại toàn bộ hành động. Nhân vật khởi xướng có thể chỉ xuất hiện nhẹ, như một sự hiện diện âm thầm, nếu như vậy sâu sắc hơn.
- Khi viết brief cho scene, cần nghĩ nó sẽ đứng cạnh cảnh nào trước và sau để tránh các shot bị lặp lại.
- Không để tất cả ảnh đều ở cùng một cự ly và cùng một hướng nhìn. Cần có sự thay đổi để tập truyện có nhịp.

## Nguyên tắc tham chiếu nhân vật

- Nhân vật được ref từ ảnh profile trong `Tap 53/characters/`.
- Bối cảnh nhân vật của project này là Ấn Độ cổ đại, xấp xỉ thế kỷ 5 TCN, trong mạch truyện về cuộc đời Đức Phật, các vị Thánh, các vị tín chủ, và con người sống ở Ấn Độ thời đó.
- Không được để nhân vật, gương mặt, dáng người, hoặc thần thái bị lai sang kiểu Việt Nam, Trung Hoa, hoặc fantasy Đông Á.
- Trang phục phải phù hợp bối cảnh Ấn Độ cổ đại: ưu tiên y phục quấn, draped garments, vải mộc, cấu trúc đơn giản, không dùng trang phục mang hướng Trung Hoa hoặc các kiểu dáng thời kỳ muộn hơn nếu không có lý do rõ ràng.
- Phụ nữ trong tập truyện này cần được thể hiện kín đáo hơn: y phục phù hợp bối cảnh và phép tắc, không để hở bụng, không tạo cảm giác gợi cảm hiện đại.
- Khi tạo ảnh có nhân vật, phải ưu tiên giữ ổn định khuôn mặt, tuổi tác, thần thái, trang phục, và silhouette theo ảnh profile.
- Profile của nhân vật chính chỉ được dùng cho đúng nhân vật đó. Không mượn khuôn mặt, tóc, turban, màu y phục, trang sức, hoặc silhouette đặc trưng của Nalini, Visakha, Punna hay nhân vật chính khác cho gia nhân, thợ, dân làng, trẻ em, hoặc nhân vật nền.
- Nhân vật phụ phải được thiết kế như nhân vật riêng: gương mặt và trang phục đa dạng nhưng đúng bối cảnh Ấn Độ cổ đại; tránh lặp lại nhận dạng của nhân vật chính trong cùng shot hoặc các shot liên tiếp.
- Nếu kịch bản cần một nhân vật phụ xuất hiện lặp lại và cần nhận diện, phải tạo profile riêng trong `Tap 53/characters/` trước khi đưa họ vào nhiều hình.
- Nếu một nhân vật xuất hiện lặp lại qua nhiều shot, cần giữ tính liên tục về góc tóc, trang sức, màu vải, và tỉ lệ cơ thể.
- Khi chưa đủ ảnh ref cho nhân vật, cần ghi rõ thiếu gì trước khi tạo nhiều ảnh liên tiếp.

## Quy trình làm việc cho mỗi lần tạo ảnh

- Đọc script chapter liên quan.
- Đối chiếu PDF dàn trang để xác định spread, frame xanh, tỉ lệ, và vị trí gáy sách.
- Xác định frame đó là full spread, nửa spread, hình chèn, hay nhiều hình.
- Rút ra brief scene theo logic storyboard.
- Kiểm tra nhân vật nào cần lấy ref từ `characters/`.
- Tạo prompt với ưu tiên bố cục, góc máy, nhân vật, ánh sáng, không khí, và vùng an toàn quanh gáy.
- Sau khi tạo ảnh, đối chiếu lại với frame xanh để xem có hợp cho dàn trang và text hay không.

## Mặc định cần nhớ khi hợp tác trong project này

- Ưu tiên sự rõ ràng khi dàn trang hơn là làm ảnh đẹp nhưng khó đặt vào bố cục.
- Ưu tiên tính liền mạch giữa các shot trong cùng một chapter.
- Nếu có xung đột giữa ảnh đẹp và khoảng trống cho text, ưu tiên khả năng đọc và dàn trang.
- Nếu có xung đột giữa bố cục spread và chi tiết nhân vật, ưu tiên tránh lỗi ở khu gáy sách.
- Ảnh output mặc định sẽ được lưu vào `Tap 53/outputs/`.
