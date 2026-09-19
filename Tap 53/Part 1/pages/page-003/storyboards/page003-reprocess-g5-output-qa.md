# G5 — QA output: Page 3, phương án 3

## Artifacts đã kiểm

- `Tap 53/Part 1/pages/page-003/outputs/page003-option3-h1-nalini-holds-elder-hand-v1.png`
- `Tap 53/Part 1/pages/page-003/outputs/page003-option3-h2-nalini-warmed-by-volunteers-v1.png`
- Card đối chiếu: `Tap 53/Part 1/pages/page-003/qa/page003-option3-g5-comparison-card.png`
- Overlay layout: `Tap 53/Part 1/pages/page-003/qa/part1-page003-nalini-volunteers-overlay.svg`

## Layout QA

- **PASS Page 3.** Hai output đều 1536 × 1024 (3:2); lệch so với frame mục tiêu 3:2 là 0,65%, trong ngưỡng 1,5%.
- Overlay dùng chính `page003-layout-source.png` có chữ làm nền.
- H1: hai bàn tay nằm trọn trong frame trái và critical-safe; miếng vá còn đọc được; không có chi tiết kể chuyện ở dải gap/gáy.
- H2: mặt/turban Nalini và cuộn bản vẽ/bàn tay nằm trọn trong frame phải, ngoài critical-safe và cách dải gap; ba silhouette chỉ là support xa.
- Lần chạy toàn manifest báo 13 lỗi thuộc các page khác có output thiếu/sai; Page 3 không có lỗi. Chúng không làm thay đổi kết quả layout của hai frame Page 3.

## Style QA — PASS

- Cả hai khung giữ line art rõ, mảng màu phẳng và cel-shading cứng tiết chế.
- H1 không có render da/vải, blur hay texture thật; nền đất là mảng đồ họa đơn giản.
- H2 chỉ có chuyển sắc trời rất nhẹ để gợi tờ mờ sáng; không có DOF, bloom, glow hay cảm giác CGI/2.5D.

## Location QA — PASS

- H1 dùng đất ướt sương, gốc cây thưa và vạt áo làm nền tối giản phù hợp insert; không lộ công trường, kiến trúc hay địa hình cấm.
- H2 giữ khoảng đất trống ướt sương, chân trời thấp và ba người chờ chưa làm việc; không có hố đào, cọc, dụng cụ, xe ngựa, núi, sông hoặc rừng dày.

## Storyboard QA — PASS

- H1: mắt đọc hai bàn tay trước, rồi miếng vá vai; hai khuôn mặt chủ động ngoài khung, nên cử chỉ không biến thành bắt tay xã giao.
- H2: mắt đọc gương mặt/hướng nhìn Nalini và cuộn bản vẽ trước; ba silhouette trái xa là dư âm, khoảng đất trống giữ nhịp chờ.
- Nalini khớp profile gốc về turban cam có dải hạt, tóc xoăn đen, ria/râu và bảng màu y phục; silhouette nền không mượn nhận diện của Nalini hoặc bà lão.
- H1 là insert cận còn H2 là medium-wide, có biến thiên cỡ cảnh/nhịp theo card đã xác nhận.

## Visual delta QA — PASS

- So với card xác nhận: H1 giữ vị trí cử chỉ trung tâm, miếng vá góc trên trái và phần mặt ngoài khung; H2 giữ Nalini phía phải, ba người chờ bên trái và negative space ở giữa.
- Không có hard lock nào bị đổi: số silhouette là ba, bà lão ngoài H2, không có chi tiết công trường hoặc phong cách render.

## Trạng thái

- Hai output là ứng viên `qa-passed`, chờ người dùng chốt output trước G6.
- Chưa chuyển file nào sang `approved/`.
