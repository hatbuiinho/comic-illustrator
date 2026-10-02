# Storyboard QA

Đối chiếu output với composition đã duyệt:

- scene meaning và reader experience;
- focus, emotional priority, moment, viewpoint và eye path;
- population plan và vai trò nhóm;
- bằng chứng cảm xúc và nguyên nhân;
- visibility priority và intentional crop;
- thông tin mới so với shot liền kề;
- negative space và điểm kết thị giác;
- profile/location anchors;
- các override được chấp nhận.

Kiểm tra thêm:

- `implicitReadability`: thông tin gián tiếp có thể được suy ra đúng từ tổng thể;
- `overstatement`: hành động, biểu cảm hoặc chi tiết phụ có bị phóng đại quá mức
  cần thiết;
- `visualCompetition`: yếu tố phụ có tranh focus với ý nghĩa chính;
- `readerSpace`: hình có để lại khoảng trống quan sát và kết nối thông tin;
- `naturalismOfPerformance`: nhân vật sống trong khoảnh khắc thay vì tạo dáng để
  giải thích nội dung.

Chạy lại `meaningPreservationCheck` và `restraintCheck`. FAIL nếu ảnh giữ focus
nhưng làm mất quy mô, quan hệ, tính tập thể hoặc cảm xúc của scene; cũng FAIL
nếu việc diễn giải quá mức làm suy yếu trọng tâm, tính tự nhiên hoặc khoảng
trống diễn giải.

Không FAIL `implicitReadable` chỉ vì không thấy trọn vẹn. Chỉ FAIL khi người đọc
không thể suy ra đúng từ tổng thể, khi tín hiệu dẫn sang cách hiểu khác hoặc khi
output mâu thuẫn với nguồn.
