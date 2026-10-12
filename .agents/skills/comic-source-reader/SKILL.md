---
name: comic-source-reader
description: Đọc và kiểm chứng nguồn cho một tập, part, page hoặc frame truyện tranh trước khi thiết kế shot, viết prompt hay tạo ảnh. Không dùng để tự thiết kế composition hoặc tạo ảnh.
---

# Đọc nguồn truyện tranh

Đọc [quy tắc nghệ thuật](../comic-shot-design/references/art-first-policy.md) và áp dụng theo giai đoạn của skill này.

Xác định chính xác tập, part, page và frame. Gọi
`comic-continuity-manager` ở chế độ `RESOLVE` để đi fast path: `page-state` →
scene packet → ledger/canon → nguồn gốc được tham chiếu. Chỉ mở rộng sang
`notes.md`, `shot_notes.md`, kịch bản trước/current/sau, layout, profile và asset
khi context thiếu, xung đột, stale hoặc cần bằng chứng trực tiếp. Không mượn
nguồn từ tập khác.

Đọc [source-provenance.md](references/source-provenance.md) để phân loại bằng
chứng. Khi công việc liên quan timeline, location hoặc trạng thái vật lý, đọc
[context-locks.md](references/context-locks.md).

## Kết quả

Mỗi snapshot xuất thêm `qaLocks` gọn để downstream không đọc lại nguồn:
`style2D`, `topography`, `activeProcess`. Chỉ ghi lock có provenance; field không
áp dụng thì bỏ, không tạo checklist rỗng.

Trả về một source snapshot ngắn gồm:

- nguồn thực sự đã đọc;
- dữ kiện được xác nhận;
- hàm ý mạnh;
- phần chưa rõ;
- các lựa chọn tạo hình chưa được xác nhận;
- nhân vật và profile cần dùng;
- `populationEvidence`: tách người chỉ hiện diện, người đang trực tiếp thực hiện
  hành động được nguồn mô tả (`activeProcessAgents`) và người có thể crop. Không
  bỏ ý nghĩa hoạt động chỉ vì nó không phải focus. Phân biệt dữ kiện đúng với
  bằng chứng bắt buộc nhìn thấy; cho phép crop, hàm ý hoặc ngoài khung khi đủ hiểu đúng;
- dữ liệu layout để shot-design đánh giá không gian: canvas, lượng chữ, cỡ đọc,
  các vùng chữ, gáy, trim, fixed element, mask thật và phạm vi được dàn lại chữ
  theo contract; tách dữ kiện đã kiểm với phần chưa rõ. Không tự chọn cỡ cảnh;
- `visualPriorityFromLayout`: mọi highlight, màu nhấn hoặc chỉ dấu biên tập trong
  layout, gồm nội dung được nhấn và mức ưu tiên hình ảnh mà source xác nhận;
- chi tiết xảy ra sau scene và bị cấm xuất hiện sớm.

Khi location hoặc hoạt động trong background góp phần làm người đọc hiểu cảnh,
snapshot phải tách rõ bốn lớp `locationContext`: **identity** của nơi chốn,
**activeProcess** đang diễn ra, **visibleConsequences** còn nhìn thấy và
**spatialLayers** từ xa đến gần. Không rút background thành danh sách 2–3 danh
từ chung như “đá, xe, nền đất”; phải ghi tín hiệu nào khiến cảnh này khác một
bãi trống hoặc location tương tự. Đồng thời ghi `genericFailureMode`: cách hiểu
sai nếu chỉ minh họa vật thể neo mà thiếu quan hệ và dấu vết hoạt động.

Kèm `context resolution` với dependency thực sự đã đọc, nguồn đã mở rộng,
freshness và một trạng thái `COMPLETE`, `NEEDS_SOURCE_EXPANSION`, `CONFLICT`
hoặc `STALE`. Khi đủ bằng chứng từ context hiện có, không đọc toàn bộ chương để
kiểm tra lại chung chung.

Không biến suy luận thành hard lock. Thiếu dữ liệu chỉ chặn phần công việc thực
sự phụ thuộc vào dữ liệu đó. Nếu phải cập nhật canon, scene packet hoặc page
state để tái sử dụng, route việc ghi qua `comic-continuity-manager`; không tạo
summary nối tiếp trực tiếp trong source snapshot.

## Contract chữ–hình

Khi deliverable có chữ reflow quanh minh họa, đọc [text-reflow-contract.md](../comic-layout-qa/references/text-reflow-contract.md). Đây là
nguồn chung cho text chuẩn, presentation mode, cấu trúc cột, reference role và
bằng chứng reflow; không áp chế độ này cho concept/profile hoặc hard frame độc lập.

### Text-region occurrence trên spread

Khi đo text để dựng proxy, đọc [contract đo typography](../comic-layout-qa/references/proxy-typography-measurement.md).
Trích riêng cỡ font, leading và glyph bounds từ PDF; lưu boundsPt từng occurrence
và paragraph map cho verifier schema 4. Không dùng glyph height thay cỡ font.

Khi đọc layout trang đôi, lập `sourceTextRegions` từ mọi occurrence chữ nhìn
thấy. Mỗi vùng có ID ổn định, phía/trang, vai trò biên tập, line count,
paragraph map và median glyph height đo từ layout. Nội dung giống nhau ở hai
phía vẫn là hai occurrence độc lập, trừ khi người dùng yêu cầu rõ bỏ một vùng;
không tự deduplicate theo chuỗi text.

Nhãn `translation-placeholder` chỉ mô tả vai trò vùng chữ, không tạo yêu cầu
dịch thuật hay đòi bản dịch tiếng Anh chính thức. Với Page 10 Tập 53 Part 1,
vùng trái và phải phải ghi riêng dù placeholder giống nhau; `briefRegion` giữa
gáy vẫn là guide chung của toàn spread.
