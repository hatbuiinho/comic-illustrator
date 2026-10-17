---
name: comic-page-guide
description: Entry point mặc định cho mọi yêu cầu tạo, tiếp tục, chỉnh sửa hoặc hoàn thiện hình minh họa truyện tranh; hướng dẫn theo từng cổng quyết định và gọi các skill chuyên môn cần thiết. Không dùng comic-production thay thế trừ khi người dùng gọi đích danh skill đó.
---

# Hướng dẫn làm một page

Entry point cho tạo, tiếp tục, sửa, variant và hoàn thiện minh họa. Đọc [quy tắc nghệ thuật](../comic-shot-design/references/art-first-policy.md). Route tác vụ độc lập thẳng tới skill chuyên môn; không tự gọi `comic-production`.

## Hội thoại và trạng thái

- Tự đọc dữ kiện có sẵn; mỗi lượt chỉ hỏi một quyết định chính, tối đa 2–3 phương án thật.
- Không hỏi lại bước đã chốt khi nguồn còn hiệu lực; đọc page-state và artifact được tham chiếu trước khi tiếp tục.
- Không vượt gate khi chưa xác nhận rõ; không suy im lặng hoặc duyệt direction thành duyệt composition.
- Khi chờ quyết định, đưa câu trả lời đầy đủ trong từng code block riêng.
- Ghi override rõ là `SKIPPED_BY_USER` đúng phạm vi; không âm thầm áp lại mặc định.

## 1. Phạm vi và nguồn

Khóa tập/part/page/scope; chỉ hỏi phần chưa rõ. Gọi `comic-source-reader` và resolve continuity. Trình snapshot ngắn: cảnh, người/profile, cảm xúc/ý chính, layout và điều chưa rõ. Chờ xác nhận nguồn trước thiết kế shot.

Layout mẫu cung cấp nội dung, typography, canvas và mask/fixed element thật; không khóa tọa độ chữ hoặc vùng tranh. Không có hard frame thì dùng `GENERATION_LAYOUT_INTEGRATION`.

## 2. Hướng kể và composition

Gọi `comic-shot-design`: thực hiện mục **Đánh giá không gian trước khi đề xuất
shot**, rồi xác định ưu tiên cảm xúc và đề xuất direction bằng bảy mục. Trình
kết luận không gian ngắn trước các option; cỡ cảnh và khả năng bố trí phải dựa
trên đánh giá đó. Không thêm cổng xác nhận cho bước đánh giá; chưa tạo preview
hoặc khóa camera/crop/staging. Trước lần đề xuất đầu tiên, áp bước sàng lọc
hướng kể và reference ngôn ngữ điện ảnh của `comic-shot-design`: mỗi option
có điểm nhìn, cách khám phá thông tin và bằng chứng cảm xúc cụ thể; các hướng
khác nhau về trải nghiệm đọc. Sau chọn, dựng một composition cho direction đó.

Thiết kế ý tưởng thị giác và diễn xuất trước, art-direct chữ–hình cùng nhau, rồi kiểm kỹ thuật. Resolve [text-artwork-integration.md](../comic-layout-qa/references/text-artwork-integration.md); đọc reference proxy/reflow chỉ theo mode áp dụng. Không làm yếu hình để giống phép đo layout mẫu.

Review ý đồ kể chuyện trước proof cuối. Mặc định dùng ImageGen tạo phác chì tối giản theo [pencil-composition-preview.md](../comic-shot-design/references/pencil-composition-preview.md), trình PNG toàn trang cùng card chín mục. SVG chỉ dùng khi người dùng chọn rõ; đây là preview để duyệt composition, chưa phải production ảnh hoàn thiện. Kiểm camera, staging, cử chỉ chính, nhịp và khả năng đọc ở mức phác; chất lượng hoàn thiện kiểm ở production. Proxy cần burden, layout và artifact binding đủ bằng chứng; chữ chính xác hoãn InDesign khi contract cho phép. Cấm dùng debug-box hoặc pose chung làm bằng chứng diễn xuất.

Khi người dùng phản hồi, phân loại chi tiết / diễn xuất / cấu trúc bố cục. Nếu ý nghĩa hành động hoặc nghệ thuật yếu, xét lại camera/staging trước khi vá chi tiết. Giữ direction đã chọn trừ khi focus/cảm nhận/moment đổi.

`selectedPageComposition: PROPOSED` tới khi preview được duyệt; sau đó `CONFIRMED`. Nói rõ duyệt composition cho phép tự chạy prompt → ảnh → QA, chưa phải chọn master hoặc duyệt delivery.

Composition được tự tạo/chỉnh lại đến khi đạt tiêu chí nghệ thuật, nội dung và
QA áp dụng, không giới hạn số lượt và không hỏi mở đợt mới chỉ vì đã tạo hai
ảnh. Khi lỗi lặp, xem lại camera/staging hoặc đổi cách sửa thay vì gọi lặp cùng
prompt; giữ version, phần đã đạt và cập nhật tiến triển. Chỉ dừng khi có preview
đạt để trình người dùng duyệt, người dùng yêu cầu dừng, cần quyết định đổi hướng
kể/nguồn hoặc công cụ bị lỗi. Không tự duyệt composition để sang production.

## 3. Prompt, ảnh và QA

- Gọi `comic-layout-qa` preflight theo contract active, không tự đổi shot đã duyệt.
- Gọi `comic-prompt-writer`; lưu prompt để truy vết, không thêm gate prompt hoặc hiển thị tiếng Anh trừ khi được yêu cầu.
- Gọi `comic-image-production`; mỗi candidate/edit là version mới, đọc lại profile gốc, giữ qaLocks và ý đồ đã duyệt. Cho phép hoàn thiện nét/pose/mảng trong ý đồ, không sao chép contour preview.
- Gọi `comic-visual-qa`: kiểm fast gates và nghệ thuật riêng. Fast FAIL vẫn giữ mốc thẩm mỹ tốt nhất để retry không làm xấu phần đã đạt.
- Gọi `comic-layout-qa` khi visual đạt; clean preview phải dùng chữ/proxy đúng mode, không dùng debug thay review nghệ thuật. Không tuyên bố layout in cuối khi mới kiểm proxy; bộ layer chỉ là check bắt buộc nếu người dùng yêu cầu bộ layer.

Áp [retry-quality-contract.md](../comic-image-production/references/retry-quality-contract.md). Phân loại lỗi ảnh / flow / text capacity / composition trước sửa. Flow sai thì sửa layout, không regenerate ảnh đúng; không xếp placement FAIL chỉ vì nhân vật vào text frame cũ.

Chỉ với production ảnh hoàn thiện sau khi composition đã duyệt, mỗi đợt tự động
chỉ tạo tối đa hai ảnh: ảnh đầu chưa đạt QA thì tự sửa/tạo ảnh thứ hai trong
composition đã duyệt và chạy lại QA áp dụng. Nếu ảnh thứ hai chưa đạt, dừng và
báo lỗi; không tự tạo ảnh production thứ ba. Đưa hai lựa chọn: tạo lại hoặc xác
nhận qua bước tiếp theo với lỗi đã nêu, theo retry contract. Giới hạn này không
áp dụng cho phác hoặc revision composition ở bước 2. Dừng sớm khi phải đổi
focus/moment/camera/composition, nguồn/profile xung đột hoặc công cụ lỗi. Không
lấy kỹ thuật PASS để bỏ qua hình vô cảm.

## 4. Chọn master và bàn giao

Hiển thị candidate và tác động QA nhìn thấy. Chờ người dùng chọn rõ version; ghi `SELECTED_FOR_LAYOUT`, không suy từ lời “ổn” khi còn nhiều ứng viên.

Sau khi chọn rõ và QA áp dụng đạt (hoặc check còn lỗi đã được người dùng bỏ qua rõ theo retry contract), gọi `comic-delivery` để đưa đúng hình đã tạo
vào `approved/`, giữ version và cập nhật đường dẫn. Không tự tách, expand, tạo
clean plate hoặc wrap; chọn master không đồng nghĩa yêu cầu bộ layer.

Sau bàn giao, đề xuất tác vụ bổ sung theo `comic-delivery`, chẳng hạn tách nhân
vật chính hoặc background bằng ImageGen. Chỉ chạy khi người dùng yêu cầu rõ.
Nếu họ yêu cầu bộ InDesign, lúc đó mới gọi production hậu kỳ và layout QA cho
bộ đồng phiên bản. Continuity event chỉ ghi từ nguồn hoặc selection/delivery
được xác nhận, không tự phát minh canon.

## Mode đặc biệt và reference

- `TEXT_PROXY_INTEGRATION`: proxy là overlay tách artwork; giữ burden/cỡ đọc, không tạo panel trắng hoặc báo exact capacity PASS.
- `BAKED_TEXT_PROXY_CONCEPT`: composition gate vẫn bắt buộc; concept đã chọn được lưu đúng vai trò. Chỉ tháo proxy khi người dùng yêu cầu artwork sạch; khi đó dùng edit/inpaint pixel lock và cần CLEAN_PLATE_PASS, không fresh-generate clean master.
- `FINAL_TEXT_REFLOW`: proof chữ thật theo [text-reflow-contract.md](../comic-layout-qa/references/text-reflow-contract.md).
- Crop theo [crop-read-contract.md](../comic-shot-design/references/crop-read-contract.md).
- Mẫu hội thoại: [conversation-patterns.md](references/conversation-patterns.md).
- Workflow flattened: [page-aware-flattened-workflow.md](references/page-aware-flattened-workflow.md).
