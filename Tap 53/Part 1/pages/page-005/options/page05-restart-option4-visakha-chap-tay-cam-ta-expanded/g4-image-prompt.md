# Prompt tạo ảnh — page 5

Use case: illustration-story

Asset type: Minh họa truyện tranh 2D cho page 5, Tập 53; canvas mở rộng để dàn trang trong InDesign.

Input images:

- `Tap 53/Part 1/pages/page-005/storyboards/page05-restart-option4-foreground-depth-canvas.png`: reference bố cục xa–gần đã được xác nhận.
- `Tap 53/characters/Visakha.png`: reference nhận diện, khuôn mặt, saree xanh lục, áo xanh lam và trang sức của Visakha.
- `Tap 53/characters/Bác Nalini.png`: reference nhận diện, khuôn mặt, turban và trang phục của Nalini.
- `Tap 53/characters/thợ phụ.png`: reference thiết kế người lao động và dụng cụ thời cổ đại; không sao chép nhận dạng của Nalini hay Visakha.

Primary request: Minh họa đúng khoảnh khắc Visakha chắp hai tay trước ngực, hướng về những người dân đang làm việc và bày tỏ lòng biết ơn. Nalini đứng cạnh bà, cầm cuộn bản vẽ, mỉm cười hiền. Người lao động vui vẻ, hợp tác và vẫn đang thực sự làm việc.

Scene/backdrop: Công trường tinh xá ở Ấn Độ cổ đại, giai đoạn mới đào móng: đất nện, hố móng nông, cọc định vị, gỗ thô và thúng đất. Không có công trình hoàn thiện.

Main content region: Dải ngang thấp ở khoảng 51%–86% chiều cao canvas, tương ứng khung xanh trong composition. Visakha và Nalini là hai khối nhân vật lớn ở tiền cảnh bên phải, nhìn sang trái vào công trường; Visakha chắp tay biết ơn, Nalini cầm cuộn bản vẽ. Khoảng 9–12 người lao động ở trung cảnh, nhỏ hơn rõ rệt nhưng vẫn đọc được như một tập thể; chia thành ba cụm chồng lớp tự nhiên: đào đất/hố móng, chuyền hoặc khiêng thúng đất, và vận chuyển gỗ thô. Một số dáng quay lưng, nghiêng hoặc bị vật liệu che một phần để tạo chiều sâu và giảm chi tiết giải phẫu nhỏ. Nhiều nhịp người ở hậu cảnh được gợi bằng lưng, vai, thúng và cán cuốc. Khoảng giữa, nơi gáy sách đi qua, chỉ có đất nện, rãnh móng nông và cọc nhỏ; không có mặt, tay hay hành động quan trọng.

Blend extension: Khoảng 60% phía trên là bầu trời thoáng, chuyển sắc rất nhẹ và mang tính đồ họa; hai mép và dải nhỏ phía dưới chỉ có nền đất/cảnh phụ liên tục. Không đặt người, mặt, bàn tay, động tác, đạo cụ kể chuyện hoặc chi tiết nhận diện thiết yếu trong vùng mở rộng. Vùng này phải sạch để mask hoặc hòa gradient trong InDesign.

Crowd suggestion: Dùng bố cục chồng lớp và thu nhỏ theo chiều sâu. Chỉ dùng vài dáng lưng, vai áo, miệng thúng và cán cuốc ở hậu cảnh để gợi rất nhiều người. Các dáng xa không có mặt, mắt, bàn tay hoặc chi tiết giải phẫu nhỏ. Không tạo đám đông người tí hon có chi tiết.

Style/medium: Thuần 2D animation; line art rõ và đồng nhất; mảng màu phẳng; 1–2 cấp cel-shading cạnh cứng. Background cùng ngôn ngữ 2D với nhân vật.

Emotion: Ấm áp, biết ơn, vui vẻ và cùng chung tay; không tạo dáng nhìn vào máy ảnh.

Constraints: Khóa nhận diện Visakha và Nalini theo profile. Visakha mặc kín đáo đúng profile, chắp hai bàn tay trọn vẹn và tự nhiên. Các nhân vật trung cảnh có cơ thể, tay chân và dụng cụ đọc tự nhiên ở kích thước layout; không trùng khuôn mặt/trang phục đặc trưng của nhân vật chính. Không xếp thành hàng đều, không sao chép cùng một gương mặt hoặc tư thế. Toàn bộ chi tiết chính nằm trong dải nội dung đã định.

Avoid: photorealistic, 2.5D, 3D, CGI, painterly rendering, soft airbrush shading, realistic skin texture, bloom, volumetric light, lens flare, depth of field, blur, tiny detailed background people, malformed faces, extra limbs, fused hands, modern objects, East Asian costume, mountains, water, dense forest, completed walls, roofs, columns, meal/rest scene, monks or nuns, carriage as focus, text, captions, labels, watermark.

## Lượt v5 — đọc lại profile và đổi framing

- Đọc và truyền lại trực tiếp ba file gốc: `Tap 53/characters/Visakha.png`,
  `Tap 53/characters/Bác Nalini.png`, `Tap 53/characters/thợ phụ.png`.
- Visakha và Nalini dùng profile gốc làm authority nhận diện; ảnh trung gian chỉ
  là edit target cho bố cục, không phải baseline khuôn mặt hoặc trang phục.
- Thu nhỏ đồng nhất toàn cảnh, không co ép riêng cơ thể; mở rộng canvas chỉ bằng
  trời phía trên và đất phía dưới.
- Dải nội dung dùng để ánh xạ vào frame xanh: `x=0–1536, y=420–786`.
- Nhóm người công quả giữ bên trái; Visakha và Nalini giữ bên phải; vùng
  `x=47%–53%` chỉ có đất, rãnh móng và cọc.
- Giữ 9–12 người đọc được ở trung cảnh cùng lớp người xa giản lược; hoạt động
  gồm đào đất, chuyền thúng và cùng vận chuyển gỗ.

## Lượt v9 — sửa quan hệ hướng thân và khóa lại địa hình

- Đọc và truyền lại trực tiếp profile gốc của Visakha, Bác Nalini và thợ phụ.
- Visakha và Nalini ở tiền cảnh phải nhưng đầu, mắt, vai, ngực và thân đều xoay
  ba phần tư sang trái, trực tiếp hướng về nhóm người công quả; không chỉ quay
  đầu trong khi thân quay ngược và không nhìn vào máy ảnh.
- Thu nhỏ đồng nhất toàn cảnh thành dải panorama thấp; vùng nội dung dùng để
  ánh xạ vào frame xanh là `x=0–1536, y=400–766`.
- Phần trên chỉ là trời và nền xa để hòa lấp; mặt, tay chắp, cuộn bản vẽ và các
  thao tác lao động chính nằm trong vùng nội dung.
- Đường chân trời phẳng, chỉ có đồng đất và hàng cây thấp; cấm núi và đồi xa.
