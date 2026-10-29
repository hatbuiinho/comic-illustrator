# Comic Illustration Project

File này chỉ giữ chỉ dẫn chung của project và điểm vào từng workflow. Quy tắc
riêng của mỗi workflow nằm trong contract của workflow đó; các bước thực hiện,
schema, cổng xác nhận và tiêu chí QA được quản lý trong skill tương ứng. Không
sao chép các chi tiết đó vào đây khi cập nhật workflow.

## Ngôn ngữ và cách phản hồi

- Mặc định trả lời và cập nhật file `.md` bằng tiếng Việt tự nhiên.
- Giữ nguyên tên riêng, tên file, lệnh và thuật ngữ kỹ thuật cần thiết.
- Khi có 2–3 phương án thực tế, đánh số và đặt tên rõ cho từng phương án;
  phần tóm tắt ngắn nêu kết quả và đánh đổi.
- Khi trình bày chi tiết một option, tách từng ý thành một đầu dòng riêng với
  nhãn dễ quét, kể cả khi chỉ có một option; không nối các mục thành một đoạn
  văn dài. Giữ các mục theo skill đang áp dụng.
- Nội dung người dùng cần copy phải đầy đủ trong code block hoặc writing block.
  Với mẫu câu trả lời để chọn hoặc duyệt bước tiếp theo, đặt mỗi mẫu trong một
  block riêng, giữ câu trả lời thuần văn bản, không thêm bullet hoặc số thứ tự
  vào trước câu hay trước block. Quy tắc đầu dòng cho chi tiết option ở trên
  chỉ áp dụng cho phần giải thích, không thay thế các block có thể copy.

## Workflow và routing

| Workflow | Khi nào | Entry point | Contract |
| --- | --- | --- | --- |
| Minh họa tập | Tạo/chỉnh minh họa theo tập/part/page/frame | `comic-page-guide` | [comic-illustrator/contract.md](comic-illustrator/contract.md) |
| Character Studio | Tạo/phát triển/chỉnh character profile, character sheet | `comic-character-studio` | [docs/studio-contract.md](docs/studio-contract.md) |
| Image Playground | Ảnh tự do, concept, poster, thử pose/cảnh ngoài minh họa tập | `comic-image-playground` | [docs/studio-contract.md](docs/studio-contract.md) |

- Yêu cầu gọi rõ một workflow/skill được ưu tiên. Trước khi làm, đọc contract
  của workflow đã chọn.
- Chỉ đọc skill và reference cần cho deliverable. Việc bảo trì project hoặc
  trao đổi chung không cần khởi động workflow nào.

## Thứ tự ưu tiên trong project

Thứ tự dưới đây dùng để giải quyết xung đột giữa tài liệu nội bộ, trong phạm vi
các chỉ dẫn hệ thống và môi trường đang có hiệu lực. Contract của từng workflow
có thể chi tiết hóa cấp 2.

1. Yêu cầu trực tiếp mới nhất của người dùng.
2. Dữ kiện và ngoại lệ của workflow hoặc nguồn đang áp dụng.
3. Skill phù hợp trong `.agents/skills/`.
4. Contract workflow, quy tắc nền trong file này và policy chung được dẫn chiếu.
5. Giả định sáng tạo của agent.

Một override rõ của người dùng phải được ghi là `SKIPPED_BY_USER`, không được
âm thầm áp lại quy tắc mặc định. Nếu người dùng không nêu phạm vi, override chỉ
áp dụng cho deliverable hiện tại.

## Phong cách và nhân vật

- Phong cách nền là thuần 2D animation, bắt buộc cho mọi ảnh trong mọi workflow,
  kể cả bản thử và variant. Trước thiết kế hình, viết prompt, tạo ảnh hoặc
  visual QA, đọc [policy phong cách](docs/project-style-policy.md).
- Mọi prompt tạo/chỉnh ảnh phải có điều cấm áp dụng ngay từ đầu, theo
  [điều cấm trong prompt](docs/prompt-constraints.md).
- Profile gốc do contract của workflow xác định là chuẩn identity. Không dùng
  output trước làm chuẩn thay thế và không cho nhân vật phụ mượn dấu hiệu đặc
  trưng của nhân vật chính. Trước mỗi lần chỉnh sửa ảnh có nhân vật, luôn đọc
  lại profile reference gốc của từng nhân vật xuất hiện.

## Quản lý file

- Dùng đường dẫn tương đối trong tài liệu và manifest nội bộ.
- Không sửa, di chuyển hoặc xóa profile, script nguồn hay layout khi chưa được yêu cầu.
- Không ghi đè output; luôn tạo version mới. Nơi lưu output do contract của
  workflow quy định.
- Không đưa file tạm hoặc cache vào deliverable cuối.

## Môi trường công cụ

- Agent tự chuẩn bị công cụ trước tác vụ đầu tiên trong phiên có dùng script,
  PDF, composition preview, QA hoặc delivery, theo
  [hướng dẫn toolchain](docs/project-toolchain.md).
- Đọc/sửa tài liệu Markdown hoặc trao đổi nội dung đơn thuần không cần bootstrap.
- Ưu tiên wrapper của project khi chạy workflow; kiểm tra công cụ thực tế,
  không chỉ dựa vào state đã lưu. Không commit `.venv/` hay state theo máy.
