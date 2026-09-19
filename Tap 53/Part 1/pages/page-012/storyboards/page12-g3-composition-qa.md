# Page 12 — G3: Composition QA

Trạng thái: `G3 PASS về storyboard · chờ xác nhận composition`.

## Phương án đã chọn

- **Option:** `page12-option2-punna-ots-nalini`
- **userAction:** `Chọn option: page12-option2-punna-ots-nalini`
- **Card xác nhận:** `page12-option2-confirmed-composition-in-layout.png`

## Composition contract ở mức storyboard

- **Điểm nhìn:** người đọc đứng cùng Punna, qua vai ông nhìn Nalini.
- **Focus đầu tiên:** phản ứng lắng nghe, nể phục của Nalini ở nửa phải ellipse; viền vàng trong card đánh dấu vùng focus.
- **Điểm đọc thứ hai:** đường nhìn/lời nói từ khối vai Punna bên trái; đường vàng cho biết eye path.
- **Dấu vết bối cảnh:** dải hố móng/bao đất thấp ở bên phải (khung xanh dương), chỉ đủ xác nhận công trường đang đào dở.
- **Thông tin chủ động ngoài khung:** Visakha, toàn bộ đội thợ và người chiên đà la; không đưa event sau vào inset.
- **Gáy và bleed:** dải đỏ ở giữa chỉ chứa nền; phần dưới vòng tròn chỉ là đất crop buffer.

## Gate

- **semanticThumbnailGate:** PASS — ở kích thước layout, khối vai Punna dẫn mắt đến Nalini; sau đó mới đọc nền công trường. Không cần chữ để hiểu Nalini đang đón nhận lời nói.
- **backgroundOnlyGate:** PASS ở mức medium close-up — còn một neo mạnh là hố móng/đất đào, cộng tín hiệu đồng bằng công trường; không có kiến trúc hoàn thiện, núi, nước, người chiên đà la hay scene tương lai.
- **Profile và anatomy:** card là schematic, chưa phải chứng cứ QA profile cuối; placement giữ Punna là foreground `requiredReadable`, Nalini là `requiredComplete`, không ép riêng đầu–thân–tay.
- **Composition strategy:** `frame within frame` bằng vai Punna; supporting `negative space`. Không dùng guide trong output cuối.
