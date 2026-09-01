# Comic Illustration Project

Project dùng để xây dựng hình minh họa truyện tranh theo file dàn trang, kịch
bản và profile nhân vật của từng tập.

Phong cách mặc định của toàn project là **thuần 2D animation**. Quy tắc bắt buộc
được lưu trong `AGENTS.md`; hướng dẫn riêng của từng tập được lưu trong
`notes.md` và `shot_notes.md` của tập đó.

## Cấu trúc project

```text
comic/
├── AGENTS.md
├── README.md
└── Tap 53/
    ├── notes.md
    ├── shot_notes.md
    ├── Part 1/
    │   ├── layouts/
    │   └── scripts/
    ├── characters/
    └── outputs/
```

Các tập sau nên giữ cấu trúc tương tự:

```text
Tap <số tập>/
├── notes.md
├── shot_notes.md
├── Part <số part>/
│   ├── layouts/
│   └── scripts/
├── characters/
└── outputs/
```

## Nguồn hướng dẫn và thứ tự ưu tiên

1. Yêu cầu mới nhất của người dùng.
2. `notes.md` của đúng tập.
3. `shot_notes.md` của đúng tập.
4. `AGENTS.md` ở gốc project.

`AGENTS.md` khóa các nguyên tắc dùng chung: thuần 2D, một focus cho mỗi shot,
đúng profile, đúng thời điểm của bối cảnh, đúng tỷ lệ frame và an toàn ở gáy
sách.

`notes.md` mô tả layout, màu đánh dấu, profile, bối cảnh và workflow riêng của
tập. `shot_notes.md` mô tả cách chọn khoảnh khắc, điểm nhìn, góc máy, khoảng
lặng và quan hệ giữa hình với chữ.

## Chuẩn bị sau khi clone

1. Clone repository về máy.
2. Đăng nhập ChatGPT/Codex bằng tài khoản có quyền tạo ảnh.
3. Mở **thư mục gốc `comic/`** làm project, không chỉ mở riêng thư mục một tập.
4. Chọn cách chạy phù hợp:
   - **Codex Local**: lựa chọn khuyến nghị.
   - **ChatGPT Work Local**: dùng được khi đã gắn thư mục `comic/`.
   - **ChatGPT Work Cloud**: không phù hợp để làm trực tiếp trên checkout local;
     phải upload hoặc kết nối lại các nguồn cần dùng.
5. Tạo task/chat mới sau khi thay đổi `AGENTS.md` để hướng dẫn được nạp lại.

## Sử dụng với Codex Local

Codex Local dùng thư mục gốc làm working directory và tự phát hiện
`AGENTS.md`. Khi yêu cầu đã chỉ rõ tập, part và page, không cần lặp lại toàn bộ
quy tắc của project trong prompt.

### Kiểm tra context lần đầu

```text
Hãy kiểm tra project này và cho mình biết:

1. File hướng dẫn nào đang được áp dụng?
2. Với Tập 53, nguồn hướng dẫn riêng của tập nằm ở đâu?
3. Quy trình bắt buộc trước khi tạo một ảnh minh họa là gì?
4. Phong cách hình ảnh nào bị cấm?

Chưa tạo hoặc chỉnh sửa ảnh.
```

Kết quả cần nhắc được ba lớp:

- `AGENTS.md`;
- `Tap <số tập>/notes.md`;
- `Tap <số tập>/shot_notes.md`.

## Sử dụng với ChatGPT Work Local

Trong app ChatGPT:

1. Tạo hoặc mở một local project.
2. Gắn thư mục `comic/`.
3. Đặt `comic/` làm thư mục chính.
4. Khi bắt đầu chat mới, yêu cầu Work đọc `AGENTS.md` một cách rõ ràng.

### Prompt khởi động cho Work Local

```text
Làm việc trực tiếp trong local project comic.

Trước khi thực hiện yêu cầu:

1. Đọc đầy đủ AGENTS.md ở thư mục gốc.
2. Xác định đúng tập đang làm.
3. Đọc đầy đủ notes.md và shot_notes.md của tập đó.
4. Chỉ sử dụng script, layout, profile và tài sản trong đúng thư mục tập.
5. Không dùng ảnh trong outputs làm style reference nếu mình chưa xác nhận ảnh
   đó đạt.

Hãy tóm tắt các nguồn hướng dẫn đã đọc. Chưa tạo ảnh.
```

Sau khi Work xác nhận đúng context, có thể dùng các mẫu prompt bên dưới.

## Thông tin nên có trong mỗi yêu cầu

Một yêu cầu tạo ảnh nên xác định rõ:

- tập;
- part;
- page vật lý trong PDF hoặc spread sách;
- frame xanh cần dùng nếu page có nhiều frame;
- đoạn script/scene cần minh họa;
- nhân vật chính xuất hiện;
- số phương án cần tạo;
- muốn duyệt storyboard trước hay tạo ảnh ngay.

Nên viết “page 3 của PDF dàn trang” hoặc “spread trang 8–9” thay vì chỉ viết
“page 3” nếu có khả năng nhầm giữa số trang PDF và số trang sách.

## Mẫu prompt: phân tích page, chưa tạo ảnh

Dùng mẫu này khi page phức tạp hoặc cần chọn kịch bản hình trước:

```text
Hãy phân tích Tập <số tập>, Part <số part>, page <số page> của file PDF dàn
trang.

Đọc AGENTS.md, notes.md và shot_notes.md của đúng tập; sau đó đọc đoạn script
liên quan cùng ngữ cảnh trước và sau.

Hãy:

1. Xác định frame xanh, tỷ lệ, vùng text, vị trí gáy và safe zone.
2. Xác định profile nhân vật cần dùng.
3. Đề xuất <số lượng> phương án storyboard.
4. Với mỗi phương án, nêu: khoảnh khắc, focus, điểm nhìn, góc máy, bố cục,
   background và lý do phù hợp với nhịp kể chuyện.

Mỗi phương án chỉ có một focus chính. Chưa tạo ảnh.
```

## Mẫu prompt: tạo ảnh sau khi chọn storyboard

```text
Mình chọn phương án <số phương án> cho Tập <số tập>, Part <số part>,
page <số page>.

Hãy dùng image generation để tạo <số lượng> biến thể của shot này.

Yêu cầu:

- bám đúng tỷ lệ frame đã đo;
- profile nhân vật là chuẩn tuyệt đối;
- thuần 2D animation theo AGENTS.md;
- mỗi ảnh chỉ có một khoảnh khắc và một focus;
- giữ mặt, mắt, tay, đạo cụ và chi tiết kể chuyện ra khỏi gáy;
- không đưa sự kiện xảy ra ở page sau vào background;
- không dùng output cũ làm style reference nếu chưa được duyệt;
- lưu file mới vào Tap <số tập>/outputs/ và không ghi đè file cũ.

Sau khi tạo, hãy tự kiểm tra profile, style 2D, context, tỷ lệ frame và vùng gáy.
```

Trong Codex có thể thêm `$imagegen` ở đầu yêu cầu để gọi rõ khả năng tạo ảnh:

```text
$imagegen Tạo ảnh theo phương án 2 đã duyệt, tuân thủ toàn bộ yêu cầu bên trên.
```

## Mẫu prompt: tạo ảnh trực tiếp

Dùng khi scene đã rõ và không cần duyệt storyboard riêng:

```text
Hãy tạo <số lượng> phương án minh họa cho Tập <số tập>, Part <số part>,
page <số page> của PDF dàn trang.

Scene cần thể hiện:
<dán hoặc mô tả ngắn đoạn cần minh họa>

Nhân vật chính:
<tên nhân vật>

Tự đọc AGENTS.md, notes.md, shot_notes.md, script, layout và profile liên quan.
Đo đúng frame xanh, xác định gáy và thiết kế bố cục theo tỷ lệ ngay từ đầu.

Mỗi ảnh là một shot storyboard riêng với một focus chính. Khóa thuần 2D,
profile và bối cảnh đúng thời điểm. Lưu vào thư mục outputs của đúng tập,
không ghi đè file cũ.
```

## Mẫu prompt: chỉnh một ảnh đã tạo

Khi chỉnh ảnh, chỉ nên thay đổi một nhóm yếu tố mỗi lần để tránh trôi profile
hoặc bố cục.

### Chỉ sửa style

```text
Giữ nguyên nhân vật, profile, bố cục, góc máy và hành động.

Chỉ sửa phong cách:

- chuyển hoàn toàn sang thuần 2D animation;
- line art rõ và nhất quán;
- màu phẳng;
- cel-shading 1–2 cấp với cạnh bóng rõ;
- background cùng ngôn ngữ 2D với nhân vật;
- bỏ toàn bộ tạo khối mềm, texture bán thực, volumetric light, bloom,
  depth of field và bokeh.
```

### Chỉ sửa vùng gáy

```text
Giữ nguyên style, profile, thời điểm và nội dung scene.

Chỉ điều chỉnh bố cục để đưa mặt, mắt, hai bàn tay và chi tiết kể chuyện chính
ra khỏi vùng gáy. Giữ đúng tỷ lệ frame và khoảng trống dành cho text.
```

### Chỉ sửa profile

```text
Giữ nguyên bố cục, background, ánh sáng phẳng và hành động.

Chỉ sửa nhân vật <tên nhân vật> để khớp chặt profile trong thư mục characters:
khuôn mặt, tuổi, tóc, trang sức, trang phục, màu vải, tỷ lệ cơ thể và
silhouette. Không thay đổi nhân vật phụ.
```

## Checklist trước khi duyệt ảnh

- Ảnh có đúng tập, part, page và đúng thời điểm trong script không?
- Tỷ lệ có bám frame xanh ngay từ đầu không?
- Focus có rõ và chỉ có một trọng tâm chính không?
- Profile có đúng khuôn mặt, tuổi, trang phục và silhouette không?
- Line art, màu phẳng và cel-shading có thực sự thuần 2D không?
- Background có cùng phong cách 2D với nhân vật không?
- Có dấu hiệu 2.5D, 3D, bán thực, blur hoặc ánh sáng thể tích không?
- Gáy sách có cắt mặt, mắt, tay, đạo cụ hoặc hành động chính không?
- Hình có để đủ khoảng thở cho text không?
- Tên file có tạo phiên bản mới thay vì ghi đè không?

## Lưu ý về output và Git

Ảnh trong các thư mục `outputs/` hiện được `.gitignore` bỏ qua. Ảnh tạo trên
một máy sẽ không tự xuất hiện khi clone project ở máy khác.

Nếu cần đồng bộ ảnh đã duyệt, hãy chọn một trong các cách:

- bỏ ignore cho các ảnh đã duyệt và quản lý chúng bằng Git/Git LFS;
- chép ảnh đã duyệt vào một thư mục reference được Git theo dõi;
- lưu ảnh thành phẩm trong kho lưu trữ dùng chung bên ngoài repository.

Không đưa ảnh chưa duyệt vào nhóm style reference chính thức.
