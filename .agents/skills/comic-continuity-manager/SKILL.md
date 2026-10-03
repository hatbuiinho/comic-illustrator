---
name: comic-continuity-manager
description: Biên dịch, truy vấn, kiểm tra và cập nhật context continuity theo tập, scene, page hoặc frame bằng provenance và dependency; dùng để tránh đọc lại toàn bộ nguồn. Không thiết kế shot, tạo ảnh hoặc tự duyệt canon sáng tạo.
---

# Quản lý continuity context

Tạo một lớp context có thể truy xuất theo phạm vi để các skill chỉ đọc phần
liên quan. Context biên dịch giúp định tuyến tới nguồn gốc; nó không thay thế
profile, layout, script, `notes.md` hoặc `shot_notes.md`.

Đọc [artifact-model.md](references/artifact-model.md) khi tạo hoặc cập nhật
episode canon, scene packet, page state hay continuity ledger. Đọc
[resolution-policy.md](references/resolution-policy.md) khi truy vấn context,
phát hiện xung đột hoặc đánh dấu artifact stale.

## Các chế độ

- `COMPILE`: tạo/cập nhật canon hoặc scene packet trực tiếp từ nguồn gốc.
- `RESOLVE`: trả context tối thiểu cho một page/frame và danh sách nguồn cần mở.
- `CHECK`: kiểm tra provenance, dependency, fingerprint và xung đột.
- `COMMIT_EVENT`: ghi một thay đổi đã được nguồn hoặc người dùng xác nhận vào
  ledger sau đúng mốc; không suy ra sự kiện mới từ ảnh chưa được duyệt.
- `INVALIDATE`: đánh dấu artifact downstream stale khi dependency thay đổi;
  không xóa hoặc âm thầm tái duyệt artifact.

Dùng `scripts/comic-context.py` cho validate, fingerprint, resolve,
check-stale, invalidate, `invalidate-dependents` và commit-event. Các lệnh ghi
dữ liệu mặc định là dry-run; chỉ thêm `--write` sau khi đã kiểm kết quả. Dùng
`scripts/audit-project.py <episode-dir>` để audit read-only trước khi tiếp tục
một project lâu ngày.

## Bất biến

- Mỗi tập là một namespace độc lập; mọi đường dẫn trong artifact là tương đối.
- Mỗi fact quan trọng có `sourceFact`, `userConfirmed` hoặc
  `assistantInference` và trỏ tới bằng chứng.
- `assistantInference` không tạo hard lock, không được ghi thành canon event và
  không được dùng làm bằng chứng cho suy luận tiếp theo.
- Không tạo canon bằng cách tóm tắt một bản tóm tắt. Khi cần tái biên dịch, đi
  từ nguồn gốc hoặc dữ kiện `userConfirmed` còn hiệu lực.
- Output chỉ chứng minh điều nhìn thấy trong chính output. Output chưa được QA
  và chọn rõ không được thay đổi continuity ledger.
- Không sửa profile, script, layout hoặc nguồn gốc trong skill này.

## Kết quả truy vấn

Trả một `context resolution` gồm target, facts/locks tối thiểu, dependency đã
đọc, dữ kiện bị cấm xuất hiện sớm, provenance, trạng thái freshness và một
trong các kết luận:

- `COMPLETE`: đủ bằng chứng để tiếp tục;
- `NEEDS_SOURCE_EXPANSION`: nêu đúng field và nguồn cần đọc thêm;
- `CONFLICT`: nêu các giá trị mâu thuẫn, bằng chứng và authority áp dụng;
- `STALE`: nêu dependency đã đổi và artifact downstream cần tái tạo hoặc QA lại.

Thiếu context biên dịch không tự động là blocker: đọc cửa sổ nguồn tối thiểu,
hoàn thành deliverable nếu đủ bằng chứng, rồi chỉ tạo artifact mới khi nó có giá
trị tái sử dụng qua page hoặc phiên sau.
