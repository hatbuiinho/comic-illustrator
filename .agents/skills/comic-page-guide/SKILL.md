---
name: comic-page-guide
description: Entry point mặc định cho mọi yêu cầu tạo, tiếp tục, chỉnh sửa hoặc hoàn thiện hình minh họa truyện tranh; hướng dẫn theo từng cổng quyết định và gọi các skill chuyên môn cần thiết. Không dùng comic-production thay thế trừ khi người dùng gọi đích danh skill đó.
---

# Hướng dẫn làm một page

Đóng vai trò entry point và lớp điều phối hội thoại mặc định cho mọi yêu cầu tạo
hình minh họa truyện tranh. Tự khám phá dữ liệu có sẵn, giải thích bằng kết quả
nhìn thấy và chỉ yêu cầu người dùng quyết định phần không thể suy ra an toàn.
Không bắt họ biết manifest, schema, safe zone, tên skill hoặc cấu trúc thư mục.

## Routing bắt buộc

- Tự động chọn skill này cho yêu cầu làm mới, tiếp tục, chỉnh sửa, tạo variant
  hoặc hoàn thiện hình minh họa truyện tranh, dù người dùng đã nêu rõ page,
  frame hay deliverable.
- Skill này trực tiếp gọi các skill chuyên môn phù hợp ở từng giai đoạn; không
  cần đọc, gọi hoặc đi qua `comic-production`.
- Chỉ dùng `comic-production` khi người dùng gọi đích danh
  `$comic-production` hoặc yêu cầu rõ dùng skill đó.
- Khi người dùng yêu cầu một tác vụ chuyên môn độc lập, vẫn vào skill này trước
  rồi route thẳng sang skill chuyên môn tương ứng; không ép chạy toàn bộ wizard.

## Nguyên tắc hội thoại

- Mỗi lượt chỉ hỏi một quyết định chính; đưa tối đa 2–3 lựa chọn thực tế.
- Đánh dấu một lựa chọn là **(Đề xuất)** và nêu lý do ngắn dựa trên nguồn.
- Với câu hỏi đơn giản, mỗi lựa chọn nêu kết quả và đánh đổi trong một dòng.
  Riêng cổng chọn composition, dòng này chỉ là tóm tắt; ngay dưới preview của
  từng option phải hiển thị composition card từ `comic-shot-design`, đủ để
  người dùng kiểm tra cách AI hiểu cảnh, cảm xúc, staging, continuity và layout.
  Không bắt người dùng mở artifact kỹ thuật để xem phần còn thiếu. Cho phép trả
  lời bằng số hoặc ngôn ngữ tự nhiên.
- Không hỏi lại dữ kiện có thể đọc từ project. Nếu chỉ có một ứng viên hợp lý,
  đề xuất ứng viên đó để người dùng xác nhận thay vì bắt họ tự tìm tên file.
- Trước câu hỏi, tóm tắt điều vừa hoàn thành và điều sẽ xảy ra sau lựa chọn.
- Mỗi khi dừng để chờ người dùng, luôn kết thúc bằng các phương án trả lời/bước
  tiếp theo có thể copy; mỗi phương án phải nằm trong một code block riêng,
  không gom nhiều phương án vào cùng một block. Nội dung trong từng block phải
  tự đủ nghĩa, có thể copy nguyên khối và không buộc người dùng sửa placeholder
  kỹ thuật.
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

Gọi `comic-source-reader`; skill này resolve context qua
`comic-continuity-manager` trước khi mở rộng nguồn. Trình bày source snapshot
bằng ngôn ngữ ngắn gọn:
cảnh đang diễn ra, nhân vật/profile, cảm xúc hoặc ý chính, layout/frame liên
quan và phần chưa rõ. Không đẩy toàn bộ phân tích kỹ thuật sang người dùng.

Hỏi họ xác nhận một trong các hướng: hiểu đúng và tiếp tục; cần sửa một chi
tiết; hoặc cần xem thêm ngữ cảnh. Chỉ sang thiết kế shot sau xác nhận.

### 3. Chọn hướng kể hình

Gọi `comic-shot-design`. Nếu chỉ có một hướng có căn cứ, vẫn trình bày hướng đó
và xin xác nhận. Nếu có nhiều hướng hợp lệ, đưa 2–3 composition khác nhau đáng
kể, không tạo các biến thể giả chỉ để đủ số lượng.

Trước khi yêu cầu người dùng chọn, phải tạo một PNG composition preview riêng
cho từng phương án và hiển thị tất cả preview ngay tại cổng này. Preview phải
dùng đúng tỷ lệ/vùng khung của layout khi có, thể hiện được vị trí tương đối,
kích thước, hướng nhìn hoặc chuyển động, lớp sâu và vùng chữ/mask quan trọng;
có thể là sơ đồ hoặc thumbnail thô, không được trình bày như ảnh thành phẩm.
Không coi mô tả chữ, composition card hoặc ảnh thành phẩm của một option là
thay thế cho bộ preview. Nếu chưa tạo hoặc chưa hiển thị đủ preview, cổng chọn
composition chưa hợp lệ và không được chạy bước 4.

Thứ tự hiển thị bắt buộc cho mỗi option:

1. tên option và dòng tóm tắt;
2. preview PNG;
3. composition card dành cho người dùng;
4. đánh đổi so với các option còn lại.

Chỉ đưa các code block để người dùng chọn sau khi đã trình bày đủ mọi option.
Không rút composition card xuống một dòng.

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
khi người dùng chủ động yêu cầu xem hoặc sửa prompt. Nếu visual QA không đạt
nhưng chưa cần đổi composition đã duyệt, tự lặp `prompt delta → version mới →
visual QA` đến khi mọi check `REQUIRED` đều PASS; không dừng để hỏi người dùng.
Chỉ dừng khi phải đổi focus/khoảnh khắc/camera/composition, nguồn hoặc profile
xung đột, công cụ lỗi, hoặc cùng một lỗi không cải thiện qua 3 lượt liên tiếp.
Ở trường hợp cuối, tự đổi một lần sang prompt viết lại và tạo ảnh mới; nếu vẫn
không cải thiện thì báo blocker, giữ toàn bộ version và không chạy layout QA.

### 5. Xử lý kết quả QA

Chỉ chạy layout QA sau khi visual QA PASS. Sau chuỗi tạo ảnh và QA, cho người dùng xem output, tóm tắt visual QA bằng tác
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

Sau delivery thành công, cho phép `comic-delivery` gọi
`comic-continuity-manager` để ghi event đã được xác nhận và invalidate đúng
consumer downstream. Không dùng ảnh approved làm profile hoặc tự phát minh
thay đổi continuity không có trong nguồn/selection.

## Tiếp tục phiên dang dở

Trước khi hỏi lại, đọc `page-state` của đúng page trước, rồi scene packet và các
artifact được nó tham chiếu để xác định cổng gần nhất đã được xác nhận. Chỉ dùng
hội thoại để bổ sung quyết định chưa được ghi. Tóm tắt ngắn target, lựa chọn
active, freshness và bước đang chờ; không chạy lại giai đoạn đã chốt khi đầu
vào không đổi. Nếu dependency đã đổi, nêu artifact stale và chỉ chạy lại phần
downstream chịu ảnh hưởng.

Nếu người dùng yêu cầu một tác vụ độc lập rõ ràng như “chỉ viết prompt” hoặc
“chỉ QA ảnh này”, route thẳng sang skill tương ứng, không ép họ đi toàn wizard.
