# G5 — QA ảnh v1: Chim gọi ngày trên mái lều

- `outputId`: `part1-page001-option11-birds-over-quiet-roof-v1`.
- `output`: `Tap 53/Part 1/pages/page-001/outputs/part1-page001-option11-birds-over-quiet-roof-v1.png`.
- `overlay`: `Tap 53/Part 1/qa/part1-spread01-chapter1-opening-overlay.svg`.
- `sourceLayout`: `Tap 53/Part 1/pages/page-001/storyboards/page001-layout-source.png`.

## Kết quả

- Layout: PASS. Output dọc `1051 × 1497`; tỷ lệ `contentFrame` lệch `0,34%` so với frame. Overlay dùng đúng raster layout gốc; toàn bộ mái lều, chim và tán cây nằm về phía phải gáy.
- Focus/storyboard: PASS. Mắt đọc bốn chim nhỏ trước, rồi hạ về mái lều; không xuất hiện người, silhouette người, đám đông, công trường hoặc hành động tương lai.
- Location: PASS. Ba neo nhận diện còn đọc được là mái lều tre, liếp tre và mảng trời sớm có sương; địa hình giữ phẳng, chân trời thấp. Cây xa chỉ là hàng cây thưa, không đọc thành rừng dày.
- Style: PASS. Line art, mảng màu phẳng và bóng cel rõ; sương và trời là mảng đồ họa nhẹ. Không có hiệu ứng 3D, ánh sáng thể tích, blur, bloom hoặc texture ảnh thật.
- Spine/trim: PASS. Dải trái gần gáy chỉ có trời, sương và đất nền; phần tán cây và mái có thể ra mép phải như crop buffer, còn recognition core vẫn nằm an toàn trong frame.
- Visual delta: PASS. Ảnh giữ đúng composition card: bầu trời chiếm phần lớn frame, chim là focus, mái lều thấp bên phải, tán cây vào từ góc trên phải. Không có thay đổi nào làm lệch timeline, location hoặc focus.

## Lưu ý báo cáo tổng

`Part 1/qa/frame-report.md` vẫn FAIL vì 12 output thiếu ở các trang khác. Mục riêng `part1-spread01-chapter1-opening/page001-chapter1-opening-dawn` PASS toàn bộ kiểm tra áp dụng.
