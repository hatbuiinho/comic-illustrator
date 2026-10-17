# Sửa có mục tiêu và giữ chất lượng

Đọc khi tự sửa, tạo variant khắc phục lỗi hoặc đổi chiến lược generation.

Giới hạn số ảnh bên dưới chỉ áp dụng cho production ảnh hoàn thiện sau khi
composition đã duyệt. Phác và revision composition thuộc `comic-shot-design`:
được tự tạo/chỉnh lại đến khi đạt, không giới hạn lượt theo số ảnh; vẫn cần
người dùng duyệt preview trước production. Các nguyên tắc sửa có mục tiêu và
giữ chất lượng trong tài liệu này có thể dùng cho composition, nhưng không
mang giới hạn hai ảnh sang vòng phác.

## Giới hạn tự động và quyết định tiếp tục

- Mỗi đợt có tối đa hai ảnh, gồm ảnh đầu và một ảnh sửa/tạo lại nếu ảnh đầu
  chưa đạt QA áp dụng. Edit và fresh generation đều tính lượt; đổi prompt,
  parent, chiến lược hoặc tiếp tục phiên không đặt lại bộ đếm.
- Ảnh nào đạt QA thì chuyển tới bước chọn version; không tạo thêm ảnh tự động
  và không tự chọn master.
- Ảnh thứ hai chưa đạt QA thì dừng ngay, hiển thị hai version, báo lỗi còn lại
  theo version và tác động. Đưa hai option có tên rõ: **Tạo lại** hoặc
  **Xác nhận qua bước tiếp theo với lỗi đã nêu**; mỗi mẫu trả lời nằm trong
  một block riêng. Chờ người dùng quyết định, không tự tạo ảnh thứ ba.
- Chọn tạo lại mở đợt mới tối đa hai ảnh theo cùng quy tắc, giữ lịch sử và mốc
  thẩm mỹ. Chỉ mở đợt mới khi người dùng yêu cầu rõ.
- Chọn đi tiếp phải xác định version và check được bỏ qua; ghi `SKIPPED_BY_USER`
  đúng version/deliverable, giữ bằng chứng lỗi, không đổi thành PASS hoặc báo
  QA đạt toàn bộ. Chỉ qua bước tiếp theo đã nêu; vẫn giữ cổng chọn master và
  bàn giao. Điều kiện QA khi bàn giao chỉ được miễn cho check có override rõ;
  các check khác vẫn phải đạt, và hồ sơ bàn giao phải nêu ngoại lệ.
- Ghi số ảnh của đợt và quyết định tiếp tục trong record production đang dùng
  để giữ giới hạn qua các phiên. Báo ngay lỗi công cụ hoặc thiếu nguồn cần thiết;
  không dùng lượt còn lại để gọi lặp mù.

## Chọn cách sửa

- Chỉ lỗi placement/scale: ưu tiên compositing/transform xác định, scale đồng
  nhất, có truy vết canvas/origin. Không dùng generative resize cho phép đặt ảnh
  thuần túy. Chỉ áp dụng nếu không đổi shot, làm nhỏ tín hiệu cảm xúc, mất context
  hoặc giảm độ phân giải dưới yêu cầu deliverable; kiểm lại layout sau transform.
- Lỗi nội dung/style cục bộ: edit mục tiêu, ghi vùng sửa và phần giữ. Dùng mask
  hoặc compositing để giữ pixel ngoài vùng sửa khi công cụ hỗ trợ; lời nhắc
  preserve không phải bằng chứng pixel lock.
- Identity/diễn xuất drift hoặc edit giảm chất lượng: quay về bản cha tốt phù
  hợp hoặc fresh generation từ profile gốc và composition đã duyệt. Không lấy
  bản xuống chất lượng làm parent tiếp theo.
- Crop/không gian sai từ composition: sửa preview, quay lại cổng composition;
  không chữa bằng fade thân vào đất hoặc thêm vật che không có nguồn.

Không đổi edit pixel-lock thành fresh generation trong hậu kỳ master đã chọn;
vẫn tuân thủ contract layer/clean plate hiện hành.

## Prompt và input

Mỗi attempt dùng prompt hiện hành gọn: mục tiêu sửa, phạm vi thay đổi, phần giữ
và lock còn hiệu lực. Không cộng dồn nguyên prompt với nhiều CRITICAL REVISION;
bỏ lệnh lỗi thời/mâu thuẫn. Style delta theo policy active, chỉ loại texture ảnh
hoặc shading kiểu render ở vùng drift. Giữ độ mềm tiết chế, đường nét và chi
tiết đồ họa có giá trị; không chuyển thành lệnh ép phẳng toàn ảnh.

Khai báo input phải khớp file thực sự truyền. Khi công cụ giới hạn reference,
chuẩn bị reference packet có vai trò rõ hoặc đổi chiến lược; không khai model
đã nhận full-page proxy khi chỉ truyền shot map. Semantic không được nâng thành
chuẩn identity/style hay contour polygon phải sao chép.

## Review giữa các attempt

Giữ `bestAestheticVersion` cùng lý do và các phẩm chất đáng giữ. Đây là mốc
so chất lượng, có thể còn lỗi kỹ thuật; không tự biến nó thành bản đã duyệt,
profile identity hoặc parent hợp lệ cho mọi sửa đổi. Mốc đầu tiên lấy từ output
đã thực sự xem; chỉ đổi khi bản mới tốt hơn về các phẩm chất liên quan, ưu tiên
nhận xét trực tiếp của người dùng. Không mặc định bản mới nhất là tốt nhất.
Lưu đường dẫn version, lý do chọn và các phẩm chất cần giữ trong state/record
production active để mốc này còn truy xuất được khi tiếp tục phiên.

Trước sửa, ghi `parentVersion`, `strategy`, `observedDefect`, `remediationDelta`,
`bestAestheticVersion`, `preservationTargets` và input thực tế. Targets lấy từ
phần đã đạt: identity,
diễn xuất, đường nét/silhouette, trang phục, nhịp hình và context; không bảo vệ
lỗi chỉ vì nó có trong bản cha.

Mỗi lượt sửa so ba bản: mốc thẩm mỹ tốt nhất, bản cha và bản mới ở cùng kích
thước đọc; thêm crop tương ứng khi cần. Khi fast gate FAIL, vẫn kiểm regression
nhanh để chọn parent an toàn cho lượt sau, không chạy QA sâu/layout hoặc mở
cổng selection. Sau fast gates PASS, ghi `qualityPreservation` với
`comparedVersions`, evidence theo target và lỗi mới trước khi dùng bản sửa làm
parent. Không lấy fast gate làm lý do bỏ qua mất chất lượng qua nhiều lượt.

Kiểm mặt/identity, diễn xuất, nếp vải/tóc/trang sức, nét/silhouette, lớp sâu và
sức sống theo phần áp dụng. Đối chiếu identity với profile gốc; mốc thẩm mỹ
không thay profile. Nếu khác camera/shot, so phẩm chất tương ứng, không ép
pixel match. Footprint/style đạt không bù suy giảm diễn xuất, độ đọc hoặc vẻ
đẹp. Loại texture drift đúng policy không tự là regression, nhưng nếu đồng
thời làm hình khô, thô hoặc mất chi tiết có giá trị thì phải ghi nhận.

Nếu regression, lưu version nhưng không dùng làm parent tiếp theo; quay về
bản có chất lượng tốt phù hợp với phép sửa và đổi cách sửa. Nếu mốc tốt nhất
sai identity/context hoặc khác shot active, không dùng nó làm parent; lấy
profile gốc và composition active để phục hồi các phẩm chất tốt. Nếu giới hạn
công cụ ngăn giữ chất lượng, báo blocker.
Giữ giới hạn hai ảnh mỗi đợt ở trên, không mở vòng retry vô hạn. Sửa
làm đổi shot hoặc trade-off cần người dùng quyết định quay lại cổng tương ứng.
