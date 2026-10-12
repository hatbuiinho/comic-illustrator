# Contract text reflow

Áp dụng cho trang có chữ ôm minh họa. Giữ khóa 2D, provenance và override của
project. Các quy tắc dưới đây làm rõ workflow page-aware hiện có.

## Canvas và phạm vi cảnh

Với page/spread không hard frame, áp mục **Phạm vi cảnh khác kích thước canvas**
trong [text-artwork-integration.md](text-artwork-integration.md). Canvas chuẩn
không buộc cảnh phủ trang; footprint cảnh và phần nền giấy theo `sceneExtentPlan`.

- Không chia canvas thành “dải chữ” và “dải hình”; không yêu cầu để trống một tỷ
  lệ cố định ở phía trên, dưới, trái hoặc phải.
- Text zone không phải vùng cấm artwork. Trong footprint, giữ context/process
  evidence cần thiết và nền dưới chữ; ngoài footprint được giữ nền giấy chủ ý.
- `WHITE_OPAQUE` chỉ mô tả khả năng che của knockout trong page preview. Raw
  candidate, master và clean plate giữ cảnh bên dưới trong footprint đã khóa,
  không tự expand bối cảnh sang vùng giấy ngoài cảnh.
- Nhân vật chính được phép đi vào hình học text frame ban đầu. Chữ phải reflow
  nghệ thuật quanh silhouette của đầu, tóc, vai, tay, y phục và đạo cụ.
- Chỉ glyph bounds cộng khoảng thở mới là vùng loại trừ bắt buộc đối với mặt,
  mắt, tay và gesture kể chuyện; không biến toàn bộ text frame thành subject
  exclusion zone.
- Không mặc định đẩy nhân vật xuống dưới, thu nhỏ nhân vật hoặc đổi camera để
  bảo vệ text frame cũ.
- Khi chữ và nhân vật xung đột, xử lý theo thứ tự: đổi text-frame geometry, độ
  rộng dòng và wrap contour; tinh chỉnh knockout/overlap; điều chỉnh nhẹ
  scale/placement/crop trong shot đã khóa; chỉ quay lại composition khi toàn bộ
  chữ không thể vừa mà vẫn giữ nguyên content và typography.

## Chế độ trình bày và cấu trúc trang

Ghi `presentationMode` theo layout/brief có provenance:
- `WHITE_EDITORIAL`: nền trang trắng, silhouette hòa vào trang, không tự thêm
  khung ảnh chữ nhật. Artwork có thể nền trắng hoặc alpha theo deliverable.
- `SCENIC_INTEGRATED`: giữ context/process evidence trong phạm vi cảnh; cho phép
  cảnh hòa mềm về giấy, không đồng nghĩa full-page scenic background.

Các chỉ dẫn giữ background/location trong workflow dùng theo SCENIC_INTEGRATED;
WHITE_EDITORIAL chỉ giữ tín hiệu bối cảnh thực sự bắt buộc trong brief, không
tự dựng full-page scenic background. Nếu nguồn bắt buộc bối cảnh nhưng mode
trắng không thể biểu đạt đủ, giải quyết xung đột trước generation.

Đây là chế độ trình bày, không thay thế `layoutMode` hay hard mask. Nếu nguồn
chưa quyết định, làm rõ trước generation. Quy tắc full-bleed cho artwork trong
hard mask vẫn áp dụng; không dùng WHITE_EDITORIAL để bỏ nền của frame đó.

Khóa kích thước trang, lề, gáy, safe zone, fixed element, số cột, thứ tự đọc và
typography. Cho phép reflow/đổi contour và độ rộng trong phạm vi nguồn cho phép;
không tự đổi số cột. Override ghi `SKIPPED_BY_USER` cùng phạm vi và lý do.

## Nguồn text và dàn chữ

Source reader cung cấp text thật cùng provenance (file/trang), paragraph ID và
style runs: font thực, size, leading, tracking, scale, bold, màu, highlight.
Giữ nguyên từ, dấu, khoảng trắng nội dung và ranh giới đoạn. Soft line break
do dàn trang không phải xuống đoạn. OCR chỉ là bản nháp cho tới khi đối chiếu.
Thiếu font/text chỉ chặn phần chứng minh reflow phụ thuộc vào chúng.

Giữ chữ ngoài image model ngay từ đầu. Reflow bằng công cụ dàn trang hỗ trợ
font và wrap cần thiết, xuất lớp chữ cùng dữ liệu đo từ chính lần render đó.
Không ghép nguyên raster chữ PDF rồi gọi đó là reflow. Nếu không reflow thì có
thể dùng lớp chữ PDF nguyên bản, nhưng phải ghi rõ chế độ cố định.

Ở mỗi option, tính chỗ cho silhouette gồm tóc, tay, quần áo, props và bóng
liên quan; ghi wrap offset bằng pt/mm và vùng được phép dàn chữ. Xem cả thumbnail
và kích thước đọc thật. Sau generation cập nhật theo silhouette thực.
Sửa flow trong phạm vi cho phép trước; nếu vẫn thiếu chỗ, sửa scale/placement/
crop trong shot. Thay pose/camera/focus có ảnh hưởng kể chuyện phải quay lại
composition. Không giảm typography hay xóa context để cứu ảnh.

## Bằng chứng kiểm được

Mỗi option/version có `textCapacityProof` là đường dẫn tương đối tới JSON:

```json
{
  "schemaVersion": 1,
  "source": "text-source.json",
  "rendered": "text-rendered.json",
  "preview": "reflow-preview.png",
  "previewSha256": "sha256:<hash của preview>",
  "wrapPath": "wrap.svg",
  "wrapSha256": "sha256:<hash của wrap>"
}
```

Đường dẫn trong proof tính từ thư mục proof. Hai file text có `paragraphs` theo
thứ tự đọc, mỗi phần tử có `id` và `runs` gồm `{text, style}`. Style phải có
`fontFamily`, `fontStyle`, `fontSizePt`, `leadingPt`, `tracking`, `scaleX`,
`scaleY`, `color`, `highlight` (null nếu không có). Export actual font, không
chỉ tên font yêu cầu. Runs có thể chia khác nhau khi wrap; không thêm newline
tại soft wrap vào nội dung logic. Không tự normalize dấu hay sửa khoảng trắng.
Source có `provenance: {path, locator}` trỏ nguồn thật. Rendered thêm:

```json
{
  "renderer": "tên công cụ và phiên bản",
  "overflowCount": 0,
  "fontSubstitutions": [],
  "lines": [
    {"paragraphId": "p1", "start": 0, "end": 12,
     "boundsPt": [20, 30, 90, 14], "availableBoundsPt": [20, 30, 95, 14]}
  ]
}
```

Offsets là Unicode code point, end exclusive; các line phải phủ hết nội dung
mỗi đoạn đúng một lần, theo thứ tự. Bounds là x/y/width/height theo pt và vùng
khả dụng của từng dòng sau khi công cụ đã tính wrap. Không viết tay số đo hoặc
chép source sang rendered để tạo PASS. Proof hash ràng buộc preview/wrap hiện tại;
thay bất kỳ đầu vào nào phải render và kiểm lại.

`verify-text-reflow.js` đối chiếu nguyên văn, style từng ký tự, thứ tự đoạn,
font substitution, coverage và bounds dòng; lỗi/missing evidence là FAIL.
Script xác minh dữ liệu export, không tự nhận diện chữ trong ảnh, không tự
tính wrap từ silhouette và không chứng minh số đo export trung thực. Layout QA
vẫn phải xem preview để kiểm khoảng thở tóc/tay/props/bóng, dòng vụn, gáy,
fixed element và art direction. Không nâng PASS dữ liệu thành PASS thị giác.

Manifest reflow mới phải có proof. Manifest cũ thiếu proof phải bổ sung khi
chạy lại QA; không nâng lời khai `status: PASS` thành bằng chứng kiểm máy.
