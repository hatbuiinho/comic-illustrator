# Comic Illustration Project

Project tổ chức workflow minh họa truyện tranh bằng các skill repo-scoped trong
`.agents/skills/`. Quy tắc chung nằm trong `AGENTS.md`; quy tắc riêng của từng
workflow nằm trong contract của workflow đó; dữ liệu và ngoại lệ nằm trong từng
thư mục tập.

## Cấu trúc

```text
.agents/skills/       Workflow dùng chung (nguồn duy nhất của skill)
.claude/skills        Symlink tới .agents/skills/ cho Claude Code
AGENTS.md             Quy tắc chung và routing workflow
CLAUDE.md             Chỉ dẫn riêng cho Claude, import AGENTS.md
comic-illustrator/    Workflow minh họa tập: contract, dữ liệu tập, tham khảo
  contract.md         Quy tắc nền của workflow
  Tap 53/             Dữ liệu riêng của Tập 53
  referrences/        Tài liệu tham khảo của tập cũ
studios/              Output của Character Studio và Image Playground
ttpq-comic/           Flow prompt spread truyện cuộc đời Đức Phật (style ttpq-comic)
docs/                 Policy dùng chung (style, toolchain, kiểm hình)
```

## Các skill

| Workflow | Skill | Tài liệu |
| --- | --- | --- |
| Minh họa tập | `comic-page-guide` (entry point) và chuỗi skill chuyên môn | [comic-illustrator/](comic-illustrator/README.md) |
| Character Studio | `comic-character-studio` | [studios/character/](studios/character/README.md) |
| Image Playground | `comic-image-playground` | [studios/playground/](studios/playground/README.md) |
| TTPQ Comic | `ttpq-comic` | [ttpq-comic/](ttpq-comic/README.md) |

Routing theo `AGENTS.md`. Gọi trực tiếp bằng `$ten-skill` (Codex) hoặc
`/ten-skill` (Claude Code).

## Chuẩn bị máy Windows

Người dùng không cần mở PowerShell hoặc tự chạy lệnh. Khi một tác vụ cần
tool local, agent tự chạy bootstrap trước rồi mới xử lý. Windows 10/11 cần có
`winget` (Microsoft App Installer) và kết nối Internet trong lần cài đầu tiên.

Lệnh dưới đây chỉ dành cho kiểm tra thủ công hoặc hỗ trợ kỹ thuật:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap-windows.ps1
```

Script kiểm tra rồi chỉ cài phần còn thiếu: Git, Node.js LTS, Python 3.12,
ripgrep, Poppler và MSYS2/librsvg. Nó tạo `.venv`, cài các gói trong
`requirements-tools.txt`, tạo shim `python3` cho các script dùng chung giữa
macOS/Linux/Windows và lưu version đã kiểm tra tại
`.tools/state.windows.json`.

State là cache theo máy và không được commit. Mỗi lần chạy, bootstrap vẫn kiểm
tra executable thật; nếu manifest hoặc requirements đổi, chỉ phần liên quan
được đồng bộ lại. Kiểm tra mà không cài:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap-windows.ps1 -CheckOnly
```

Để bắt buộc bootstrap trước một lệnh workflow:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run-with-tools.ps1 -- node .agents\skills\comic-layout-qa\scripts\run-page-qa.js "Tap 53\Part 2\pages\page-005"
```

Các tool bắt buộc và vai trò:

| Tool | Vai trò |
| --- | --- |
| Git | Quản lý source và lịch sử thay đổi |
| Node.js LTS | Chạy script composition, QA và delivery |
| Python 3.12 + `.venv` | Continuity, PDF và xử lý ảnh hỗ trợ |
| PyYAML | Đọc/ghi page state, ledger và scene packet YAML |
| Poppler | Đọc metadata/text và render PDF layout thành PNG |
| librsvg (`rsvg-convert`) | Render composition preview và QA overlay SVG thành PNG |
| ripgrep (`rg`) | Tìm nhanh source/artifact trong project |

ImageMagick và FFmpeg hiện không phải phụ thuộc của workflow. Công cụ tạo ảnh
AI cũng không được cài bởi bootstrap vì được cung cấp qua dịch vụ riêng.

## Chuẩn bị máy macOS

Người dùng không cần mở Terminal hoặc tự chạy lệnh. Khi một tác vụ cần
tool local, agent tự chạy bootstrap trước rồi mới xử lý. Nếu máy chưa có
Homebrew, bootstrap tự chạy installer chính thức; macOS có thể hiện yêu cầu
nhập mật khẩu quản trị. Máy cần kết nối Internet trong lần cài đầu tiên.

Lệnh dưới đây chỉ dành cho kiểm tra thủ công hoặc hỗ trợ kỹ thuật:

```bash
./scripts/bootstrap-macos.sh
```

Script chỉ cài formula còn thiếu: Git, Node.js, Python 3.12, ripgrep, Poppler
và librsvg. Nó dùng chung `requirements-tools.txt`, tạo `.venv` và lưu version
đã kiểm tra tại `.tools/state.macos.json`. State theo máy không được commit.

Kiểm tra mà không cài hoặc cập nhật:

```bash
./scripts/bootstrap-macos.sh --check-only
```

Ép đồng bộ lại Python packages:

```bash
./scripts/bootstrap-macos.sh --force-refresh
```

Để bắt buộc bootstrap trước một lệnh workflow:

```bash
./scripts/run-with-tools.sh node .agents/skills/comic-layout-qa/scripts/run-page-qa.js "Tap 53/Part 2/pages/page-005"
```

## Ví dụ yêu cầu

```text
Mình muốn làm minh họa cho một page nhưng chưa biết bắt đầu từ đâu.
```

```text
Phân tích Tap 53, Part 2, page 11; chưa tạo ảnh.
```

```text
Đưa ra ba phương án storyboard cho frame 1 của page 11.
```

```text
Viết prompt hoàn chỉnh theo phương án 2; chưa tạo ảnh.
```

```text
Tạo ảnh theo phương án 2, không cần tránh gáy trong deliverable này.
```

## Override kiểm tra

Kiểm tra điều kiện có ba trạng thái:

- `REQUIRED`: áp dụng và có thể làm QA thất bại.
- `NOT_APPLICABLE`: không liên quan đến deliverable.
- `SKIPPED_BY_USER`: người dùng chủ động bỏ qua trong phạm vi đã nêu.

Ví dụ “không cần tránh gáy” làm check `spine` thành `SKIPPED_BY_USER`; script
vẫn có thể vẽ guide để tham khảo nhưng không đánh FAIL vì giao với gáy.

## Layout QA

```text
node .agents/skills/comic-layout-qa/scripts/layout-frame-qa.js <manifest.json> <output-directory>
```

Hoặc với page package có `layout.json`:

```text
node .agents/skills/comic-layout-qa/scripts/run-page-qa.js <page-directory>
```

Script tạo `frame-report.md`, `frame-report.json` và overlay SVG trên raster
layout gốc có text.

## Quy tắc output

Ảnh tạo mới nằm trong `outputs/` và có version riêng. Chỉ dùng
`comic-delivery` sau khi QA phù hợp đã PASS và người dùng chọn rõ output. Không
ghi đè file đã duyệt.
