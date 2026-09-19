# G2 — Storyboard: PDF page 3

## Option đã khóa theo lựa chọn của người dùng

- **ID:** `page003-optionA-hands-then-warmth`
- **Cấu trúc:** hai frame ngang độc lập, đặt hai bên gáy; không có chi tiết kể
  chuyện nào đi vào dải gáy.
- **Cinematic intent:** chữ kể lời cam kết của bà lão; hình không lặp lời nói mà
  cho thấy sự đón nhận qua một cái chạm và dư âm trong Nalini. Người đọc đi từ
  sự tiếp xúc cụ thể sang nhận ra nội tâm.

### Frame trái — `h1-nalini-holds-elder-hand`

- **Khoảnh khắc/focus:** Nalini vừa cầm lấy bàn tay chai gầy của bà lão; mảng
  vai có miếng vá được thấy rõ phía sau bàn tay.
- **Camera:** cận cảnh ngang, góc chéo ngang thắt lưng; không thấy mặt đầy đủ
  của ai để tránh cạnh tranh với cử chỉ.
- **Không gian:** bàn tay là midground; mép áo/miếng vá là lớp sau; đất ẩm và
  gốc cây tối giản là lớp nền. Không thêm vật che khung chỉ để tạo lớp.
- **Ý nghĩa/crop:** cả hai bàn tay `requiredComplete`, phải có khoảng thở;
  phần tay áo có thể ra khung tự nhiên, không cắt ở cổ tay hay khuỷu tay.

### Frame phải — `h2-nalini-warmed-by-volunteers`

- **Khoảnh khắc/focus:** ngay sau cái chạm, Nalini đứng yên cầm cuộn bản vẽ,
  gương mặt dịu lại khi nhìn về đoàn người ngoài khung.
- **Camera:** medium ngang, ba phần tư từ vị trí của bà lão; bà chỉ có thể là
  một viền vai mờ bằng mảng phẳng ở mép trái frame, không thấy mặt.
- **Không gian:** vai áo bà lão ở lớp gần; Nalini là lớp giữa; đất ẩm, gốc cây
  và vài silhouette chờ xa là lớp nền. Eye path: vai áo vá → tay/cuộn bản vẽ →
  gương mặt Nalini → khoảng người chờ ngoài hình.
- **Ý nghĩa/crop:** gương mặt, turban, cuộn bản vẽ và tư thế Nalini đều
  `requiredComplete`, cách xa dải gáy. Đám đông chỉ là `optionalSupport`.

## Kiểm tra G2

- `anatomySilhouetteGate`: PASS ở card; không ép tỷ lệ đầu–thân–tay để né gáy.
- `priorityConflictGate`: PASS; frame trái dành toàn bộ hierarchy cho cử chỉ,
  frame phải dành hierarchy cho phản ứng Nalini.
- `shotVariationCheck`: PASS; shot 1 là cận cảnh xúc giác, shot 2 là medium
  reaction, có chuyển cự ly và điểm nhìn rõ ràng.
- `backgroundOnlyGate` sơ bộ: PASS ở cỡ medium/cận; nền chỉ là dấu hiệu không
  gian sáng sớm, không tự nhận là cảnh công trường rộng hoặc địa điểm khác.

**Trạng thái G2: PASS — chờ xác nhận Storyboard QA ở G3.**

![Composition card](page003-g2-optionA-composition.png)
