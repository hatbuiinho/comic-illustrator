# Layout frame QA

`layout-frame-qa.js` kiểm tra phần hình học của một output minh họa: ảnh có
đúng tỷ lệ frame, các chi tiết quan trọng có nằm trong mask, có đè vùng chữ hay
rơi vào gáy không. Script không đánh giá style, profile hoặc chất lượng diễn
xuất; overlay được tạo ra để duyệt các phần đó bằng mắt.

## Chuẩn bị manifest

Sao chép `layout_frames.example.json` thành `layout_frames.json`. Tất cả tọa độ
`x`, `y`, `width`, `height` được chuẩn hóa từ 0 đến 1 theo toàn spread, nên không
phụ thuộc vào pixel của ảnh preview.

- `box`: vùng ảnh đúng theo frame xanh đã đo/chốt.
- `shape`: `rect` hoặc `ellipse`. Với oval/tròn vẫn dùng output ảnh chữ nhật.
- `output`: đường dẫn tương đối từ file manifest tới output ảnh.
- `textReserve`: một hay nhiều vùng chữ cần giữ sạch.
- `spine`: dải gáy (hoặc `null` nếu frame không đi qua gáy).
- `critical`: bounding box của mặt, tay, đạo cụ hoặc chi tiết kể chuyện không
  được bị crop/mask, rơi vào gáy hoặc đè chữ.
- `defaults.printTrim`: bắt buộc gồm `trimPercent: {x: 0.0104895, y: 0.0147783}`
  và `criticalSafePercent: {x: 0.0279720, y: 0.0394089}`. Tỷ lệ được áp theo
  từng trục của vùng kiểm tra, nên không phụ thuộc pixel hoặc kích thước output.

`pageImage` là bắt buộc và phải là raster của chính layout gốc có đầy đủ text.
SVG overlay đặt output vào đúng frame/mask trên ảnh này. Nếu thiếu file, sai
đường dẫn hoặc định dạng không đọc được, script trả `FAIL` và không tạo overlay;
không có fallback nền trắng hay nền thay thế.

## Chạy

```bash
node "Tap 53/Part 1/scripts/layout-frame-qa.js" \
  "Tap 53/Part 1/scripts/layout_frames.json"
```

Kết quả nằm trong `Tap 53/Part 1/qa/`:

- `frame-report.md`: pass/fail có thể đọc nhanh.
- `frame-report.json`: dữ liệu cho quy trình tự động sau này.
- `<spread>-overlay.svg`: preview trực quan.

Trong overlay: đỏ liền là trim theo phần trăm từng trục; xanh lá liền là critical-safe theo phần trăm từng trục;
xanh dương đứt là frame/mask; vàng là vùng chữ; đỏ mờ là gáy; xanh lá mờ là
critical element. Nếu critical không nằm hoàn toàn trong mask và critical-safe,
hoặc đụng vùng chữ/gáy, script trả mã lỗi và báo `FAIL`.

## Giới hạn có chủ ý

Script chỉ biết vị trí do người làm khai báo, không thể tự hiểu mặt hay đạo cụ
trong ảnh AI một cách đủ tin cậy để làm điều kiện pass. Vì vậy, sau khi test
PASS, vẫn mở SVG overlay để duyệt xem subject, cử chỉ, khoảng thở và độ dễ đọc
của chữ có thật sự hợp lý không.
