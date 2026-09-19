# Page 24 — reprocess with profile lock

## Profile lock H1: five identity anchors

| Mã | File profile | Vị trí bắt buộc | Dấu hiệu không được đổi |
| --- | --- | --- | --- |
| A | `Lao dao truong.png` | foreground trái, mặt trung-trái | tóc và râu dài màu trắng, búi tóc trắng cao, khăn cam, y be/xám rách, chuỗi hạt nâu |
| B | `Dao si tre gay go.png` | sau A, trái-trung | người gầy, mặt dài lo âu, tóc đen búi cao, ria mảnh + chòm râu nhỏ, áo nâu vàng với khăn gỉ sét |
| C | `Ga dao si xoa man suon.png` | trung cảnh | ria mép đen dày, dáng trung bình, y nâu cam, tay trái xoa mạn sườn trái |
| D | `Dao si cao to tho kech.png` | phải-trung | thân hình to rộng/cơ bắp, ria mép xoắn và chòm râu nhọn, y nâu-rỉ sét, silhouette lớn nhất sau lão |
| E | `Dao si ngoi gan cua.png` | sát cửa ở nền phải | râu ngắn đầy hơn C, tóc búi + tóc dài, y nâu sẫm với dải kem nhạt chéo ngực |

**Cổng QA profile:** H1 fail nếu một trong năm anchor thiếu, hoán đổi vị trí, vay đặc điểm của nhân vật khác, hoặc không nhìn ra ít nhất hai dấu hiệu riêng trong bảng. QA này diễn ra trước QA layout. H2 không có nhân vật.

## Context lock chung

- Cuối cuộc họp bí mật trong điện thờ đá cũ, sau đề nghị cuối; năm người im bặt.
- H1: đèn dầu còn cháy nhỏ. H2: gió qua tường đá nứt làm đèn vừa tắt.
- Cấm: người thứ sáu, hoàng cung, tinh xá, phụ nữ trong mưu kế, nhân vật Phật giáo, vũ khí và bất kỳ kế hoạch nào được thực hiện.
- Hai frame 2.57:1 ở đáy spread; gáy `x=0.47–0.53` chỉ là nền an toàn.

## Option A — nắm tay, profile theo hàng sâu

- H1: nắm tay A ở foreground trái → mặt A → B, C, D, E lần lượt chạy từ trái sang phải ở các lớp sâu. Mỗi người nhìn thấy mặt và torso đủ để đối chiếu profile; không ai bị che bởi người khác.
- H2: tim đèn đen → khói ngang → khe tường nứt.
- Ưu điểm: giữ nhịp truyện đã chọn trước đây và cho phép kiểm đủ năm profile trong một khung hẹp.
- Đánh đổi: giảm độ lớn của nắm tay một chút để không giấu B/C.

## Option B — vòng họp mở một phía

- H1: góc cao nhẹ; A ở giữa vòng, B–E tạo nửa vòng mở về phía người đọc. Nắm tay A đặt trên đầu gối, nhỏ hơn nhưng cả năm nhận dạng rõ nhất.
- H2: giống Option A.
- Ưu điểm: ít chồng hình nhất, kiểm profile dễ nhất.
- Đánh đổi: lực kịch tính của nắm tay yếu hơn Option A.

## Prompt protocol sau khi duyệt

1. Hiển thị lại ngay đủ năm profile làm tham chiếu trong phiên tạo ảnh.
2. Prompt gọi từng mã A–E, vị trí và dấu hiệu bắt buộc; cấm hoán đổi đặc điểm giữa mã.
3. Sau tạo, đối chiếu lần lượt A–E bằng bảng trên trước khi duyệt bố cục, background và style.
