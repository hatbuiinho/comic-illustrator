# Comic Illustration Project

File này giữ chỉ dẫn chung của project và điểm vào workflow. Các bước thực hiện,
schema, cổng xác nhận và tiêu chí QA được quản lý trong skill tương ứng; không
sao chép các chi tiết đó vào đây khi cập nhật workflow.

## Ngôn ngữ và cách phản hồi

- Mặc định trả lời và cập nhật file `.md` bằng tiếng Việt tự nhiên.
- Giữ nguyên tên riêng, tên file, lệnh và thuật ngữ kỹ thuật cần thiết.
- Khi có 2–3 phương án thực tế, đánh số và đặt tên rõ cho từng phương án;
  phần tóm tắt ngắn nêu kết quả và đánh đổi.
- Khi trình bày chi tiết một option/hướng kể hoặc composition card, tách từng
  ý thành một đầu dòng riêng với nhãn dễ quét, kể cả khi chỉ có một option.
  Không nối các mục như cảm nhận, ý nghĩa, khoảnh khắc, trọng tâm, cách kể,
  cỡ cảnh/bố trí và đánh đổi thành một đoạn văn dài. Giữ các mục theo skill
  đang áp dụng; đây là quy tắc trình bày chung cho mọi người dùng project.
- Nội dung người dùng cần copy phải đầy đủ trong code block hoặc writing block.

## Phạm vi nguồn

- Mỗi thư mục tập là một đơn vị nội dung độc lập.
- Không lấy profile, layout, bối cảnh, script hoặc asset từ tập khác để thay thế.
- Trước công việc phụ thuộc nội dung, xác định đúng tập, part, page và frame.
  Tái sử dụng context còn hiệu lực; cách truy xuất và kiểm chứng nguồn thuộc
  `comic-source-reader` và `comic-continuity-manager`.
- Context đã biên dịch phải giữ provenance; không được tóm tắt nối tiếp từ bản
  tóm tắt cũ rồi coi kết quả là nguồn gốc.
- Nếu nguồn cấp tập bị thiếu, chỉ coi đó là blocker khi deliverable thật sự phụ
  thuộc vào nguồn đó.

## Thứ tự ưu tiên trong project

Thứ tự dưới đây dùng để giải quyết xung đột giữa tài liệu nội bộ, trong phạm vi
các chỉ dẫn hệ thống và môi trường đang có hiệu lực.

1. Yêu cầu trực tiếp mới nhất của người dùng.
2. Dữ kiện và ngoại lệ trong `notes.md` của đúng tập.
3. Continuity hoặc ngoại lệ trong `shot_notes.md` của đúng tập.
4. Skill phù hợp trong `.agents/skills/`.
5. Quy tắc nền trong file này và policy chung được dẫn chiếu.
6. Giả định sáng tạo của Codex.

Một override rõ của người dùng phải được ghi là `SKIPPED_BY_USER`, không được
âm thầm áp lại quy tắc mặc định. Nếu người dùng không nêu phạm vi, override chỉ
áp dụng cho deliverable hiện tại.

## Routing skill

- Mọi yêu cầu tạo, tiếp tục, chỉnh sửa, tạo variant hoặc hoàn thiện hình minh
  họa truyện tranh mặc định đi qua `comic-page-guide`, kể cả khi người dùng đã
  nêu rõ page, frame hoặc deliverable.
- Chỉ dùng `comic-production` khi người dùng gọi đích danh skill đó hoặc yêu
  cầu rõ dùng `comic-production`; không tự động đọc hoặc gọi nó từ
  `comic-page-guide`.
- `comic-page-guide` điều phối các skill chuyên môn; đọc mô tả và hướng dẫn của
  skill phù hợp cho tác vụ độc lập. Việc bảo trì project hoặc trao đổi chung
  không cần khởi động workflow minh họa.

Chỉ đọc skill và reference cần cho deliverable. Phạm vi áp dụng và quy trình
chuyên môn do từng skill quy định.

## Khóa phong cách nền

Phong cách mặc định là thuần 2D animation. Trước thiết kế hình, viết prompt,
tạo ảnh hoặc visual QA, đọc [policy phong cách](docs/project-style-policy.md),
bao gồm ngoại lệ nền trời đã được người dùng xác nhận. Đây là nguồn chung cho
quy chuẩn phong cách; skill phụ trách cách thực thi và kiểm tra.

Profile gốc trong đúng tập là chuẩn identity. Không dùng output trước làm chuẩn
thay thế và không cho nhân vật phụ mượn dấu hiệu đặc trưng của nhân vật chính.
Trước mỗi lần chỉnh sửa ảnh có nhân vật, luôn đọc lại profile reference gốc của
từng nhân vật xuất hiện, kể cả khi ảnh nguồn hoặc revision trước đã được kiểm.

## Quản lý file

- Dùng đường dẫn tương đối trong tài liệu và manifest nội bộ.
- Không sửa, di chuyển hoặc xóa profile, script nguồn hay layout khi chưa được yêu cầu.
- Không ghi đè output; luôn tạo version mới.
- Ảnh mới/variant nằm trong `outputs/` của đúng tập/page.
- Chỉ đưa output vào `approved/` sau khi người dùng chọn rõ và đạt QA áp dụng;
  thực hiện bàn giao và cập nhật đường dẫn theo `comic-delivery`.
- Không đưa file tạm, cache hoặc asset của tập khác vào deliverable cuối.

## Môi trường công cụ

- Agent tự chuẩn bị công cụ trước tác vụ đầu tiên trong phiên có dùng script,
  PDF, composition preview, QA hoặc delivery, theo
  [hướng dẫn toolchain](docs/project-toolchain.md).
- Đọc/sửa tài liệu Markdown hoặc trao đổi nội dung đơn thuần không cần bootstrap.
- Ưu tiên wrapper của project khi chạy workflow; kiểm tra công cụ thực tế,
  không chỉ dựa vào state đã lưu. Không commit `.venv/` hay state theo máy.
