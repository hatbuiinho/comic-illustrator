---
name: comic-page-guide
description: Hướng dẫn người dùng ít kinh nghiệm đi từng bước để làm minh họa một page truyện tranh, đưa ra lựa chọn dễ hiểu và chờ xác nhận ở mỗi cổng quyết định. Dùng khi người dùng muốn bắt đầu, tiếp tục hoặc chưa biết cần cung cấp gì; không dùng khi họ đã yêu cầu rõ một tác vụ chuyên môn độc lập.
---

# Hướng dẫn làm một page

Đóng vai trò lớp hội thoại đứng trước `comic-production`. Tự khám phá dữ liệu có
sẵn, giải thích bằng kết quả nhìn thấy và chỉ yêu cầu người dùng quyết định phần
không thể suy ra an toàn. Không bắt họ biết manifest, schema, safe zone, tên
skill hoặc cấu trúc thư mục.

## Nguyên tắc hội thoại

- Mỗi lượt chỉ hỏi một quyết định chính; đưa tối đa 2–3 lựa chọn thực tế.
- Đánh dấu một lựa chọn là **(Đề xuất)** và nêu lý do ngắn dựa trên nguồn.
- Mỗi lựa chọn nêu kết quả và đánh đổi trong một dòng. Cho phép trả lời bằng số
  hoặc ngôn ngữ tự nhiên.
- Không hỏi lại dữ kiện có thể đọc từ project. Nếu chỉ có một ứng viên hợp lý,
  đề xuất ứng viên đó để người dùng xác nhận thay vì bắt họ tự tìm tên file.
- Trước câu hỏi, tóm tắt điều vừa hoàn thành và điều sẽ xảy ra sau lựa chọn.
- Mỗi khi dừng để chờ người dùng, luôn kết thúc bằng một khối code ngắn chứa
  các câu trả lời/bước tiếp theo có thể copy nguyên dòng. Nội dung trong khối
  phải tự đủ nghĩa; không buộc người dùng sửa placeholder kỹ thuật.
- Không tiếp tục qua một cổng khi chưa có xác nhận rõ. Không coi im lặng, câu
  trả lời mơ hồ hoặc việc duyệt bước trước là phê duyệt bước sau.
- Giữ nguyên lựa chọn đã chốt; chỉ mở lại khi đầu vào thay đổi hoặc người dùng
  yêu cầu quay lại.

Khi cần mẫu câu hỏi hoặc cách ghi nhớ tiến độ, đọc
[conversation-patterns.md](references/conversation-patterns.md).

## Luồng và cổng xác nhận

### 1. Khóa phạm vi

Kiểm tra project ở chế độ chỉ đọc rồi xác định dần `episode`, `part`, `page` và
`scope` (toàn page hay frame cụ thể). Chỉ hỏi trường còn thiếu và có ảnh hưởng.
Chờ người dùng xác nhận target trước khi đọc nguồn chuyên sâu.

### 2. Xác nhận cách hiểu nguồn

Gọi `comic-source-reader`. Trình bày source snapshot bằng ngôn ngữ ngắn gọn:
cảnh đang diễn ra, nhân vật/profile, cảm xúc hoặc ý chính, layout/frame liên
quan và phần chưa rõ. Không đẩy toàn bộ phân tích kỹ thuật sang người dùng.

Hỏi họ xác nhận một trong các hướng: hiểu đúng và tiếp tục; cần sửa một chi
tiết; hoặc cần xem thêm ngữ cảnh. Chỉ sang thiết kế shot sau xác nhận.

### 3. Chọn hướng kể hình

Gọi `comic-shot-design`. Nếu chỉ có một hướng có căn cứ, vẫn trình bày hướng đó
và xin xác nhận. Nếu có nhiều hướng hợp lệ, đưa 2–3 composition khác nhau đáng
kể, không tạo các biến thể giả chỉ để đủ số lượng.

Ngay tại cổng chọn composition, nói rõ rằng việc chọn một phương án là xác nhận
hướng kể hình và cho phép workflow chạy liền mạch qua viết prompt kỹ thuật, tạo
ảnh và QA. Khi người dùng đã chọn rõ, nhắc lại lựa chọn active bằng một câu rồi
chạy bước 4; không tạo thêm một lượt xác nhận lặp lại.

### 4. Tự động tạo prompt, ảnh và QA

Xác nhận rõ hướng kể hình ở bước 3 đồng thời là quyền chạy chuỗi sau cho đúng
composition đã chọn:

1. Gọi `comic-prompt-writer`.
2. Gọi `comic-image-production`; mỗi ảnh mới hoặc variant là một version mới
   trong `outputs/`.
3. Gọi `comic-visual-qa`.
4. Nếu deliverable gắn với layout và visual QA đạt, gọi `comic-layout-qa`, tạo
   QA overlay trên chính raster layout gốc có text, rồi hiển thị overlay cho
   người dùng cùng kết luận QA.

Không tạo thêm cổng xác nhận prompt và không hiển thị prompt tiếng Anh trong
luồng mặc định. Lưu prompt vào artifact phù hợp để truy vết; chỉ hiện đầy đủ
khi người dùng chủ động yêu cầu xem hoặc sửa prompt. Nếu visual QA không đạt,
dừng trước layout QA và đưa ra bước sửa có thể copy. Ngoài trường hợp lỗi hoặc
blocker thật sự cần quyết định của người dùng, không dừng giữa chuỗi.

### 5. Xử lý kết quả QA

Sau chuỗi tạo ảnh và QA, cho người dùng xem output, tóm tắt visual QA bằng tác
động nhìn thấy và đưa lựa chọn phù hợp: giữ bản hiện tại, sửa có mục tiêu, hoặc
tạo variant. Không yêu cầu người dùng tự đọc báo cáo QA để biết nên làm gì.

Nếu output gắn vào layout, layout QA chưa hoàn tất cho tới khi đã tạo QA overlay
bằng chính raster layout gốc có text. Hiển thị hoặc dẫn link rõ tới overlay cùng
kết luận QA; không chỉ trả báo cáo chữ. Nếu chưa có dữ liệu để tạo overlay, nêu
đúng dữ liệu còn thiếu và đưa bước tiếp theo có thể copy, không tuyên bố layout
QA đã hoàn tất. Các check bị người dùng bỏ qua phải ghi `SKIPPED_BY_USER` đúng
phạm vi.

### 6. Chọn và bàn giao bản cuối

Cho người dùng xem rõ các version còn là ứng viên và khuyến nghị một bản dựa
trên QA. Chỉ gọi `comic-delivery` khi họ chọn đích danh output/version. Không
suy ra phê duyệt cuối từ câu như “ổn”, “tiếp tục” nếu còn nhiều ứng viên.

## Tiếp tục phiên dang dở

Trước khi hỏi lại, đọc artifact của đúng page và hội thoại hiện có để xác định
cổng gần nhất đã được xác nhận. Tóm tắt ngắn target, lựa chọn active và bước
đang chờ; không chạy lại giai đoạn đã chốt khi đầu vào không đổi.

Nếu người dùng yêu cầu một tác vụ độc lập rõ ràng như “chỉ viết prompt” hoặc
“chỉ QA ảnh này”, route thẳng sang skill tương ứng, không ép họ đi toàn wizard.
