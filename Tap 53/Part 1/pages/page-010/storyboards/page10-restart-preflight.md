# Page 10 — Restart preflight

Trạng thái: `storyboard-pending`. Process này bắt đầu lại từ cổng 1; option,
composition card và output trước đây chỉ là lịch sử, không phải brief hiện hành.

## Source read

- `Tap 53/notes.md`
- `Tap 53/shot_notes.md`
- `Tap 53/workflow.md`
- `Tap 53/Part 1/scripts/chapter1.md` (ngữ cảnh trước, scene và ngay sau scene)
- `Tap 53/Part 1/layouts/TẬP 53 _ PART 1 _ DEMO DÀN TRANG_PTg full 12.08.26.pdf`, spread PDF page 10 / trang sách 22–23
- `Tap 53/characters/Bác Nalini.png`
- `Tap 53/characters/Visakha.png`

## Frame map

| Frame | Shape | Box (normalized spread) | Layout meaning |
| --- | --- | --- | --- |
| H1 | ellipse | `x=.3346, y=.5774, w=.3305, h=.4221` | Oval lớn ở đáy spread, khoảng 804×729 px trên canvas 2433×1727; cắt qua gáy. |

- Gáy: `x=.47–.53`, từ `y=.5774` xuống đáy; chỉ là nền/negative space.
- Không có `textReserve` bên trong oval; phần chữ nằm phía trên/trái ngoài frame.
- Safe zone: hai gương mặt và cử chỉ chính nằm an toàn trong hai nửa oval, không sát biên ellipse hoặc gáy.

## Context and background locks

### contextSnapshot

- **Time:** buổi chiều, sau đoạn trao đổi về gạch/vữa và ngay khi xe vật liệu đến.
- **Present:** Nalini, Visakha, Punna và người thợ báo tin; shot có thể chỉ thấy Nalini + Visakha để giữ focus.
- **Happening:** hai xe bò chở gạch chưa bốc; thợ chuyển các tảng đá dư vào một góc; Nalini đang cân nhắc chi phí; Visakha chỉ về đá và xin dùng cho hương thất.
- **Forbidden future:** Nalini đã đồng ý/xây lại hương thất; khu cột chính, tỳ kheo ni đến thăm, quyết định về ni chúng/cư sĩ/vệ sinh hoặc công trình hoàn thiện.

### backgroundContinuityLock

- **Physical stage:** bãi tập kết vật liệu trong công trường đang thi công ban đầu.
- **Must show:** đất công trường thô, vài tảng đá xanh nguyên khối; dấu hiệu rất phụ của xe bò/gạch chưa bốc nếu còn đủ khoảng thở.
- **May show:** một hoặc hai worker nhỏ, không nhận diện, đang chuyển đá ở sâu nền.
- **Forbidden:** hương thất đã xây, tường/cột/mái hoàn thiện, công trường gọn sạch, tỳ kheo ni, nội thất hay cảnh lễ bái.
- **Proof:** Chương 1: xe vừa đến, hai xe bò gạch chưa bốc và thợ đang chuyển đá; chi tiết cột chính/tỳ kheo ni xảy ra sau khi ba người tiếp tục đi.

### narrativeInferenceLock

- **Explicit:** Visakha chỉ các tảng đá nặng và xin dành cho hương thất; Nalini đang tính toán giữ/trả vật liệu dư.
- **Strongly implied:** Visakha chọn giá trị thanh tịnh, không phô bày; Nalini bắt đầu chuyển từ logic chi phí sang sự kính trọng.
- **Unknown:** vị trí chính xác của từng người quanh xe, lượng đá cụ thể, hướng nhìn trước đó và phản ứng lời nói của Punna; không được tự khóa chúng thành fact.

Không cần `causalStateLock`: đây là khoảnh khắc đang diễn ra, không phải aftermath của một biến cố đổi trạng thái.
