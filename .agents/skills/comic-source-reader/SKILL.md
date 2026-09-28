---
name: comic-source-reader
description: Đọc và kiểm chứng nguồn cho một tập, part, page hoặc frame truyện tranh trước khi thiết kế shot, viết prompt hay tạo ảnh. Không dùng để tự thiết kế composition hoặc tạo ảnh.
---

# Đọc nguồn truyện tranh

Xác định chính xác tập, part, page và frame. Đọc `notes.md`, `shot_notes.md` nếu
có, kịch bản liên quan cùng ngữ cảnh trước/sau, layout, profile và asset thuộc
đúng tập. Không mượn nguồn từ tập khác.

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

Không biến suy luận thành hard lock. Thiếu dữ liệu chỉ chặn phần công việc thực
sự phụ thuộc vào dữ liệu đó.
