# Page 12 — G1: nguồn và khóa ngữ cảnh

Trạng thái: `G1 PASS · storyboard-pending`.

## Nguồn đã đọc

- `Tap 53/notes.md`
- `Tap 53/shot_notes.md`
- `Tap 53/workflow.md`
- `Tap 53/workflow_schema.md`
- `Tap 53/workflow_templates.md`
- `Tap 53/storyboard_composition_reference.md`
- `Tap 53/Part 1/scripts/chapter1.md`, dòng 64–75 (đoạn trước, scene và đoạn sau)
- `Tap 53/Part 1/layouts/TẬP 53 _ PART 1 _ DEMO DÀN TRANG_PTg full 12.08.26.pdf`, PDF page 12 / trang sách 26–27; đã kiểm bằng `pdfinfo`, `pdftotext` và raster layout gốc.
- `Tap 53/characters/Punna.png`
- `Tap 53/characters/Bác Nalini.png`
- `Tap 53/characters/Visakha.png`
- `Tap 53/characters/thợ phụ.png`

## contextSnapshot

- **Thời điểm:** ban ngày, ngay sau khi Nalini nhận phải sắp xếp lại các hạng mục và ba người đã đi tới rìa công trường giáp cánh đồng.
- **Có mặt:** Punna, Nalini, Visakha; ở xa có thợ đào hố móng và những phụ nữ khiêng bao đất.
- **Đang diễn ra:** Punna nhìn khu đất rộng, quay sang Nalini và yêu cầu thêm khu vệ sinh kín đáo, riêng cho nam và nữ cư sĩ.
- **Đã xảy ra:** trao đổi về đá cho hương thất, khu cột chính, lời đề nghị dành khu cho ni chúng và nhà tu tập cho cư sĩ.
- **Cấm đưa sớm:** người đàn ông chiên đà la với quang gánh, câu hỏi/xúc động của Visakha về chất thải, cuộc tranh luận giai cấp, chòi lá mới dựng, đuốc chiều tối, xe ngựa về Savatthi và công trình hoàn thiện.
- **Bằng chứng:** chương 1 dòng 64–70; dòng 71 mở scene kế tiếp nên không thuộc frame này.

## narrativeInferenceLock

- **Explicit:** Punna quan sát công trường, nói với Nalini về nhu cầu vệ sinh; Nalini nể phục sự chu đáo ấy.
- **Hàm ý mạnh:** sự quan tâm của Punna là thực tế, có trách nhiệm và hướng đến phẩm hạnh của người tu, không phải lời ra lệnh phô trương.
- **Chưa biết:** vị trí chính xác của Visakha trong khoảnh khắc nói, biểu cảm đầy đủ của Nalini, số công nhân nhìn thấy trong frame; không biến chúng thành sự kiện xác nhận.

## backgroundContinuityLock và geographyLock

- **Giai đoạn vật lý:** công trường nền móng, chưa có kiến trúc cố định hoàn thiện.
- **Phải có:** nền đất mở rộng, hố móng đang đào dở, một nhịp người thợ ở xa và/hoặc một phụ nữ khiêng bao đất; chân trời đồng bằng thoáng ở rìa công trường.
- **Có thể có:** cọc đánh dấu, đất đào thành đống thấp, gỗ thô hoặc một dải cây thưa ở rất xa.
- **Cấm:** nhà cầu/khu vệ sinh đã xây, chòi lá mới dựng, tường/cột/mái/nền hoàn thiện, xe ngựa, người chiên đà la, núi/đồi/vách/sông/hồ hoặc rừng dày không có bằng chứng.
- **Neo nhận diện địa điểm:** (1) hố móng và cọc định vị; (2) đất đào cùng bao đất; (3) rìa công trường mở ra cánh đồng phẳng, lộng gió.
- **Neo chung giữa các shot:** đất công trường đang đào dở và cọc/hố móng; với cận cảnh chỉ cần một neo này cùng tín hiệu đồng bằng mở.
- **Nguy cơ đọc sai:** biến thành sân làng đã hoàn thiện, đồng ruộng thuần túy không còn dấu công trường, hoặc cảnh đồi núi ngoạn mục.

## visualComponentLock

| Thành phần | Vai trò | Cách đọc đúng | Cách đọc sai cần tránh |
| --- | --- | --- | --- |
| Punna | trọng tâm quan hệ | trưởng giả đúng profile, trang phục vàng–xanh, quay về phía Nalini | tư thế ra lệnh/gia trưởng áp chế hoặc lẫn với Nalini |
| Nalini | đối tượng lời nói | thợ cả lớn tuổi, tóc/râu đúng profile; có thể chỉ là vai/silhouette nếu frame quá chật | thay thành người hầu hoặc thiếu nhận diện nghề thợ |
| Hố móng + bao đất | bằng chứng công trường | hố nông, đất đào, bao nặng do phụ nữ khiêng | công trình đã hoàn thiện hoặc lao động mơ hồ không chỉ đúng giai đoạn |

## Causal, material và print-trim lock

- **causalStateLock:** `applicable: false` — không phải aftermath có trạng thái vật lý đã chốt.
- **materialSemanticsLock:** `applicable: true` — bao đất phải đọc là bao nặng đang được khiêng; hố móng là hố đào dở, không phải mương trang trí.
- **Quy đổi trim theo tỷ lệ từng trục:** xén mỗi cạnh là `1,049%` chiều rộng (`3/286`) và `1,478%` chiều cao (`3/203`); critical-safe inset là `2,797%` chiều rộng (`8/286`) và `3,941%` chiều cao (`8/203`). Áp dụng các tỷ lệ này lên đúng `contentFrame`/canvas của từng output, không dùng một kích thước pixel hay mm cố định.
- **Phân loại sơ bộ:** Punna (gương mặt/đường nhìn về Nalini) là `requiredComplete`; Nalini là `requiredReadable` hoặc `outOfFrame` tùy option; hố móng/bao đất là `requiredReadable`; thợ xa, cọc, đất, trời và cây xa là `optionalSupport`/crop buffer.
- **Nguyên tắc gáy:** khung tròn chồng lên gáy; vùng gáy chỉ dành cho đất/nền trống. Không để mặt, mắt, tay, cử chỉ, bao đất hoặc miệng hố móng quan trọng ở đó.

## Kết luận G1

Nguồn, timeline, nhân vật, bối cảnh công trường và các chi tiết bị cấm đã đủ rõ để sang G2. Chưa có frame map/manifest, composition option hay output; các mục đó thuộc gate tiếp theo.
