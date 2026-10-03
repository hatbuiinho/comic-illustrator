---
name: comic-prompt-writer
description: Viết prompt tạo hoặc chỉnh ảnh từ storyboard/composition đã chọn cho project truyện tranh 2D. Dùng khi người dùng cần prompt hoàn chỉnh; không tự tạo ảnh hoặc thay đổi shot đã duyệt.
---

# Viết prompt ảnh truyện tranh

Nhận composition contract đã chọn và chuyển thành prompt hoàn chỉnh. Không tự
đổi focus, moment, camera, population plan hoặc profile.

Trước khi viết, kiểm tra composition không bị `STALE` so với dependency revision
đã ghi. Bảo toàn `mustNotChange` và `forbidden`; không biến
`writesIfApproved` thành sự kiện đã xảy ra ngoài đúng moment của shot.

Bảo toàn thứ bậc kể chuyện của composition: `emotionalPriority` →
`explicitRequired` → `implicitReadable` → `optionalSupport`. Không chuyển mọi
dữ kiện thành checklist chi tiết có độ nhấn như nhau.

Luôn đọc [pure-2d-style.md](references/pure-2d-style.md). Đọc
[prompt-contract.md](references/prompt-contract.md) để cấu trúc prompt và
[negative-constraints.md](references/negative-constraints.md) để chọn điều cấm.

Chỉ đưa vào prompt các kiểm tra `REQUIRED`. Không thêm constraint thuộc
`NOT_APPLICABLE` hoặc `SKIPPED_BY_USER`. Nếu người dùng nói “không cần tránh
gáy”, prompt không được lén dịch focus khỏi gáy.

Đưa prompt hoàn chỉnh trong một code block, không dùng dấu ba chấm thay nội dung.

Với thông tin `implicitReadable`, mô tả ấn tượng tổng thể và các tín hiệu tối
thiểu thay vì liệt kê dày đặc dấu hiệu cơ học. Không tự yêu cầu toàn thân, hành
động cường điệu, biểu cảm lớn hoặc thêm vật thể chỉ để tăng độ rõ. Nếu prompt
khiến thông tin phụ cạnh tranh với cảm xúc hoặc focus, phải giản lược trước khi
tạo ảnh.

Với mỗi `criticalAnatomy`, mô tả pose và cấu trúc nhìn thấy; không chỉ ghi
“correct anatomy”. Yêu cầu đúng số bộ phận, đúng khớp, kết nối tự nhiên và
silhouette phân biệt được. Tránh từ ngữ dễ làm nhập hình như “fingers together”;
dùng “các ngón ở gần nhau nhưng từng ngón vẫn phân biệt rõ”.

Khi nhận remediation từ QA, viết prompt delta chỉ sửa các check FAIL, nhắc lại
những gì phải giữ và không đổi composition đã duyệt. Với lỗi style, nêu đúng
dấu hiệu sai đang thấy và ngôn ngữ đồ họa thay thế; không chỉ ghi “thuần 2D”.
