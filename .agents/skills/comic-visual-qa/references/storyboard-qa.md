# Storyboard QA

Đối chiếu output với composition đã duyệt:

- `readerFeeling`, `emotionalThesis`, dư vị và scene meaning;
- `emotionalAnchor`, `performanceSubtext` và quan hệ nhìn thấy;
- `performanceReadByCharacter`: intended read so với gaze, hand gesture,
  posture, spacing và `forbiddenReads` nhìn thấy của từng nhân vật;
- `groupEmotionalCoherence`: các sắc thái có cùng phục vụ emotional thesis hay
  một nhân vật đang tạo cách đọc mâu thuẫn;
- `beautyIntent`: page character, rhythm và living detail;
- focus, emotional priority, moment, viewpoint và eye path;
- `sceneExtentPlan`: phạm vi cảnh và phần giấy chủ ý có còn đúng; không mở rộng
  bối cảnh để phủ canvas hoặc làm khoảnh khắc intimate thành cảnh quy mô lớn;
- population plan và vai trò nhóm; với `activeProcessAgents`, phải thấy ít nhất
  số đại diện tối thiểu đang thực hiện đúng hành động, không chỉ thấy hậu quả;
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

Chạy hai check trước context chi tiết:

- `emotionalImpact`: trong một giây có đọc được đúng cảm xúc/quan hệ và dư vị
  không; FAIL nếu chỉ đúng sự việc nhưng vô cảm hoặc performance chung chung;
- `visualVitality`: hình có đẹp, có nhịp, điểm hút, lớp sâu và sức sống không;
  FAIL nếu mọi dữ kiện ngang hàng, bố cục khô hoặc đọc như sơ đồ minh họa.

Đối chiếu `selectiveEvidence`: `mustShow` phải đủ rõ, `canImply` chỉ cần suy ra
đúng, còn `omitToProtectEmotion` không được quay lại và tranh focus. Việc có đủ
nhiều vật thể không bù được một emotionalImpact hoặc visualVitality FAIL.

Chạy lại `meaningPreservationCheck` và `restraintCheck`. FAIL nếu ảnh giữ focus
nhưng làm mất quy mô, quan hệ, tính tập thể hoặc cảm xúc của scene; cũng FAIL
nếu việc diễn giải quá mức làm suy yếu trọng tâm, tính tự nhiên hoặc khoảng
trống diễn giải.

Không FAIL `implicitReadable` chỉ vì không thấy trọn vẹn. Chỉ FAIL khi người đọc
không thể suy ra đúng từ tổng thể, khi tín hiệu dẫn sang cách hiểu khác hoặc khi
output mâu thuẫn với nguồn.

## Continuity dependency

Nếu composition khai báo dependency:

- đối chiếu `reads` với trạng thái nhìn thấy cần thiết cho shot;
- kiểm tra mọi `mustNotChange` không bị ảnh tự ý biến đổi;
- kiểm tra `forbidden` không xuất hiện;
- với `writesIfApproved`, chỉ xác nhận output có thể hiện đúng event dự kiến,
  không kết luận event đã trở thành canon.

Nếu dependency revision đã stale, trả kết luận `STALE_INPUT` trước khi dùng QA
đó làm điều kiện delivery. Chỉ những check thực sự phụ thuộc dữ kiện đã đổi mới
cần chạy lại.
