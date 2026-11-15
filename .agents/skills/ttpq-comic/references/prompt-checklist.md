# Checklist nhanh trước khi gửi

Tự kiểm trong đầu, không cần ghi từng mục vào `record.md`.

## Mọi lượt ảnh

- [ ] Prompt do `build-prompt.py` ghép, không có cảnh báo chưa xử lý (cảnh
      DRAFT chưa duyệt, profile chưa APPROVED, thiếu dòng Profile).
- [ ] Luôn truyền `--cast` đúng người có mặt trong spread; người ở xa hoặc
      quần chúng dùng `--no-ref`; tối đa 3 ảnh ref.
- [ ] Body trỏ tới ảnh ref bằng `{slug}`, không ghi cứng `Image N`.
- [ ] Ảnh đính kèm đúng thứ tự Image script in ra; không có output cũ ngoài
      outline được chọn hoặc outline đang sửa.
- [ ] Body ngắn, là văn xuôi, một focus mỗi scene, không tả lại mặt hay màu
      của nhân vật có ref.
- [ ] "Không vẽ" của brief đã đưa vào `--avoid`.
- [ ] Lượt nét: body có STORY, Mood và biểu cảm từng nhân vật; hành động chính
      và góc máy của mỗi trang khớp brief; body đã lưu `.body.txt`.
- [ ] Lượt nét: body có dòng `Text wrap:` theo "Chữ ôm hình" của brief; đoạn
      Text chỉ khóa cỡ chữ và vị trí dòng đầu, không khóa số dòng/dáng khối.
      `Text wrap:` không nhắc cỡ chữ, dòng đầu, ngôn ngữ, màu chữ.
- [ ] Điều muốn có viết thành câu khẳng định trong body; Avoid chỉ giữ lỗi model
      hay mắc thật.

## Lượt màu

- [ ] Ánh sáng trong body khớp cường độ của chữ nguồn (nắng gắt vẫn là gắt).
- [ ] Body màu chỉ có STORY, màu/ánh sáng từng trang, Mood; không góc máy.

## Lượt chỉnh

- [ ] Body chỉ gồm các dòng `Change:`; không chép `Left/Right page:` của lượt nét.

## Khối bối cảnh

- [ ] Cảnh `Snn` đúng spread; việc đã/chưa xảy ra khớp cảnh trước và sau.
- [ ] THỜI ĐIỂM & ÁNH SÁNG giữ đúng cường độ của chữ nguồn.
- [ ] KHÔNG ĐƯỢC có điều cấm truyện và niên đại liên quan; không cấm nhầm
      ngoại lệ của profile.
- [ ] Trọn một code block, không còn `<...>`; trình kèm link layout và profile.
