# Comic Illustration Project

## Ngôn ngữ và cách phản hồi

- Mặc định trả lời và cập nhật file `.md` bằng tiếng Việt tự nhiên.
- Giữ nguyên tên riêng, tên file, lệnh và thuật ngữ kỹ thuật cần thiết.
- Khi có 2–3 phương án thực tế, trình bày thành danh sách đánh số ngắn; mỗi
  phương án nêu kết quả và đánh đổi trong một dòng.
- Nội dung người dùng cần copy phải đầy đủ trong code block hoặc writing block.

## Phạm vi nguồn

- Mỗi thư mục tập là một đơn vị nội dung độc lập.
- Không lấy profile, layout, bối cảnh, script hoặc asset từ tập khác để thay thế.
- Trước công việc phụ thuộc nội dung, xác định đúng tập, part, page và frame;
  ưu tiên context đã biên dịch của đúng tập theo thứ tự `page-state` → scene
  packet → episode canon/continuity ledger → nguồn gốc được tham chiếu. Chỉ mở
  rộng sang `notes.md`, `shot_notes.md`, kịch bản liên quan, layout và profile
  khi context thiếu, xung đột, stale hoặc deliverable cần bằng chứng trực tiếp.
- Context đã biên dịch phải giữ provenance; không được tóm tắt nối tiếp từ bản
  tóm tắt cũ rồi coi kết quả là nguồn gốc.
- Nếu nguồn cấp tập bị thiếu, chỉ coi đó là blocker khi deliverable thật sự phụ
  thuộc vào nguồn đó.

## Thứ tự ưu tiên

1. Yêu cầu trực tiếp mới nhất của người dùng.
2. Dữ kiện và ngoại lệ trong `notes.md` của đúng tập.
3. Continuity hoặc ngoại lệ trong `shot_notes.md` của đúng tập.
4. Skill phù hợp trong `.agents/skills/`.
5. Quy tắc nền trong file này.
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
- Đọc và kiểm chứng nguồn: `comic-source-reader`.
- Biên dịch, truy vấn và cập nhật continuity context: `comic-continuity-manager`.
- Thiết kế storyboard/composition: `comic-shot-design`.
- Viết prompt: `comic-prompt-writer`.
- Tạo, chỉnh hoặc tạo variant ảnh: `comic-image-production`.
- Kiểm tra profile, style, context và storytelling: `comic-visual-qa`.
- Kiểm tra frame, text, trim, safe zone hoặc gáy: `comic-layout-qa`.
- Chuyển output đã chọn vào `approved/`: `comic-delivery`.

Chỉ dùng skill và reference cần cho deliverable. Không chạy layout QA cho
concept art, profile, style test hoặc ảnh chưa gắn layout.

## Khóa phong cách nền

Phong cách mặc định là thuần 2D animation: line art rõ, flat fills, 1–2 cấp
hard cel-shading, background cùng ngôn ngữ đồ họa. Cấm 2.5D/3D, CGI, bán hiện
thực, soft airbrush, texture thật, gradient nặng, bloom, volumetric light, DOF
và bokeh. Background chỉ được có chuyển màu rất nhẹ, tiết chế và đồ họa để gợi
thời điểm hoặc không khí.

Ngoại lệ toàn project do người dùng xác nhận ngày 2026-10-02:
`SKIPPED_BY_USER` đối với việc cấm tuyệt đối nền trời mềm. Nền trời được phép
có chuyển màu mềm nhẹ và tiết chế để gợi thời điểm hoặc không khí. Ngoại lệ
không áp dụng cho nhân vật hay vật thể, và không cho phép soft airbrush tạo
khối, gradient nặng, bloom, volumetric light, DOF, bokeh, CGI hoặc bán hiện
thực.

Profile gốc trong đúng tập là chuẩn identity. Không dùng output trước làm chuẩn
thay thế và không cho nhân vật phụ mượn dấu hiệu đặc trưng của nhân vật chính.

## Quản lý file

- Dùng đường dẫn tương đối trong tài liệu và manifest nội bộ.
- Không sửa, di chuyển hoặc xóa profile, script nguồn hay layout khi chưa được yêu cầu.
- Không ghi đè output; luôn tạo version mới.
- Ảnh mới/variant nằm trong `outputs/` của đúng tập/page.
- Chỉ sau khi người dùng chọn rõ output đã QA, chuyển file đó vào `approved/`,
  cập nhật mọi đường dẫn liên quan và không giữ hai nguồn chuẩn.
- Không đưa file tạm, cache hoặc asset của tập khác vào deliverable cuối.

## Toolchain trên Windows

- Người dùng không cần chạy lệnh chuẩn bị. Trước tác vụ đầu tiên trong phiên có
  dùng script, PDF, composition preview, QA hoặc delivery, agent phải tự chạy
  `powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap-windows.ps1`.
- Nếu người dùng chỉ hỏi nội dung hoặc trao đổi không cần tool local thì không
  chạy bootstrap.
- Với lệnh workflow thủ công, ưu tiên chạy qua
  `powershell -ExecutionPolicy Bypass -File .\scripts\run-with-tools.ps1 -- <lệnh> <tham-số>`
  để luôn kiểm tra/cài tool trước khi thực thi.
- Bootstrap phải idempotent: chỉ cài tool còn thiếu, đồng bộ `.venv` khi
  `requirements-tools.txt` đổi và lưu snapshot version vào
  `.tools/state.windows.json`.
- Không coi state là bằng chứng duy nhất; phải kiểm tra command thực tế vì tool
  có thể đã bị gỡ hoặc PATH đã đổi. Không commit `.venv/` hay state theo máy.

## Toolchain trên macOS

- Người dùng không cần chạy lệnh chuẩn bị. Trước tác vụ đầu tiên trong phiên có
  dùng script, PDF, composition preview, QA hoặc delivery, agent phải tự chạy
  `./scripts/bootstrap-macos.sh`.
- Nếu người dùng chỉ hỏi nội dung hoặc trao đổi không cần tool local thì không
  chạy bootstrap.
- Với lệnh workflow thủ công, ưu tiên chạy qua
  `./scripts/run-with-tools.sh <lệnh> <tham-số>` để luôn kiểm tra/cài tool
  trước khi thực thi.
- Bootstrap dùng Homebrew, chỉ cài formula còn thiếu, đồng bộ `.venv` khi
  `requirements-tools.txt` đổi và lưu snapshot version vào
  `.tools/state.macos.json`.
- Nếu thiếu Homebrew, bootstrap tự chạy installer chính thức; macOS có thể yêu
  cầu người dùng nhập mật khẩu quản trị. Không ghi state READY nếu cài thất bại.
- Không coi state là bằng chứng duy nhất; phải kiểm tra command thực tế. Không
  commit `.venv/` hay state theo máy.
