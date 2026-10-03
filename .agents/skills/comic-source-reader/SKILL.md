---
name: comic-source-reader
description: Đọc và kiểm chứng nguồn cho một tập, part, page hoặc frame truyện tranh trước khi thiết kế shot, viết prompt hay tạo ảnh. Không dùng để tự thiết kế composition hoặc tạo ảnh.
---

# Đọc nguồn truyện tranh

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

Trả về một source snapshot ngắn gồm:

- nguồn thực sự đã đọc;
- dữ kiện được xác nhận;
- hàm ý mạnh;
- phần chưa rõ;
- các lựa chọn tạo hình chưa được xác nhận;
- nhân vật và profile cần dùng;
- layout/frame data có liên quan;
- chi tiết xảy ra sau scene và bị cấm xuất hiện sớm.

Kèm `context resolution` với dependency thực sự đã đọc, nguồn đã mở rộng,
freshness và một trạng thái `COMPLETE`, `NEEDS_SOURCE_EXPANSION`, `CONFLICT`
hoặc `STALE`. Khi đủ bằng chứng từ context hiện có, không đọc toàn bộ chương để
kiểm tra lại chung chung.

Không biến suy luận thành hard lock. Thiếu dữ liệu chỉ chặn phần công việc thực
sự phụ thuộc vào dữ liệu đó. Nếu phải cập nhật canon, scene packet hoặc page
state để tái sử dụng, route việc ghi qua `comic-continuity-manager`; không tạo
summary nối tiếp trực tiếp trong source snapshot.
