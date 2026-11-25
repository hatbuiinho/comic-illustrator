# Flow tương tác và menu lệnh

Context là deliverable mặc định. Mỗi bước sau chỉ chạy khi người dùng yêu cầu.
Menu là các câu trả lời mẫu trong phản hồi: mỗi câu một code block riêng, không
thêm số hay bullet vào câu. Thay placeholder bằng đường dẫn/version thực.

## 1. Sau context: chọn cách có phương án

Agent đã đọc context khi viết nó, nên đi thẳng tới phương án:

```text
Đề xuất 2–3 phương án minh họa thật sự điện ảnh, khác nhau rõ ràng cho spread này. Chưa tạo ảnh.
```

```text
Mình gửi phương án có sẵn. Tóm tắt cách bạn hiểu và chỉ ra điểm xung đột nếu có. Chưa tạo ảnh.
```

- **Đề xuất:** agent nhập vai nhiếp ảnh gia nghệ thuật (SKILL bước 4); các
  phương án khác nhau ở khoảnh khắc, focus hoặc khung hình; mỗi
  phương án dùng đúng 5 mục ở SKILL bước 4. Cuối phản hồi, mỗi phương án một block:

  ```text
  Chọn phương án N — <tên>. Ghi vào brief và tạo clean outline.
  ```

- **Phương án của người dùng:** điền 5 mục theo ý họ, không tự đổi khoảnh
  khắc. Nếu phương án gom nhiều hành động cùng cần focus thì chỉ ra, chưa tự
  sửa. Ghi vào brief rồi đưa lệnh outline.

## 2. Tạo clean outline

Lệnh cố định của người dùng (không gửi nguyên câu này cho model ảnh):

```text
dùng style ttpq comic blend để vẽ hình minh họa và dàn trang cho page này ở dạng clean outline, chữ sẽ hòa với hình nhưng giữ nguyên khổ chữ, giữ nguyên vị trí dòng đầu tiên, chữ có thể được reflow để ôm hình 1 cách sống động, phần chữ bên phải là tiếng anh, bên trái là tiếng việt, truyện này là truyện về cuộc đời Đức Phật nên nhân vật sẽ là người Ấn Độ thời đó ạ
```

- Lệnh "Chọn phương án N … tạo clean outline" cũng kích hoạt bước này.
- Lượt nét và chỉnh outline luôn gọi Semi-Realistic Storybook Illustration
  (chỉnh outline từ 2026-11-24), bỏ qua `--style`; lượt màu không ghi là blend,
  kể cả `--recast`; `color-edit` và `swap` theo finish của ảnh đang sửa. Light và soft
  đã bỏ từ 2026-11-25; lệnh cũ ghi hai tên này thì dùng blend.
- Lượt màu ghi `ttpq storybook` (style test 40% semi-realistic storybook + 35% flat + 25% nền storybook, 2026-11-22) thì
  chạy `--style storybook`; định nghĩa ở `ttpq-comic/style/ttpq-storybook.md`.
- `ttpq real` (style test 50% semi-realistic comic + 25% flat + 25% nền storybook, 2026-11-22): lượt màu
  ghi `ttpq real` thì chạy `--style real`; định nghĩa ở `ttpq-comic/style/ttpq-real.md`.
- Viết body từ phương án active, chạy `build-prompt.py --pass outline`, rồi gọi
  ImageGen với prompt và ảnh đính kèm theo thứ tự script in ra.
- Chữ trang phải là tiếng Anh giữ chỗ do model tự sinh; không dịch.
- Image 1 là `layout-ref-canvas-v003.png` script tạo, cùng khổ 1536×1024 với
  ảnh ra; hai dải bleed xám để trống, hậu kỳ nối nền.
- Mỗi lệnh tạo một ảnh. Hiển thị và kiểm tra ảnh theo mục «Viết và chạy prompt
  ảnh» trong `SKILL.md`, rồi lưu vào `outputs/outline-vNNN.png`. Nếu công cụ
  lỗi thì báo lỗi.

### Cập nhật phương án rồi tạo lại outline

Khi người dùng sửa phương án (đổi dáng, góc máy, focus…) rồi xin outline mới:

1. Sửa thẳng 5 mục trong `brief.md`, thêm ngày cập nhật; xóa các dòng
   `SKIPPED_BY_USER` chỉ áp cho lượt cũ.
2. Viết body **mới từ brief** theo mẫu body lượt nét (STORY, từng trang kèm
   hành động chính và biểu cảm, Mood). Không lấy body hay prompt cũ ra vá, không
   viết câu sửa lỗi của bản trước vào body; lỗi cũ đi vào `--avoid`.
3. Đối chiếu trước khi chạy: hành động chính (động từ), khung hình và chữ ôm hình
   của từng trang trong brief đều có trong body; không câu nào trái brief.
4. Lưu body thành `prompts/vNNN-outline.body.txt` cùng version với prompt.

## 3. Sau outline

Người dùng comment tự do để sửa, hoặc nói "tạo outline khác theo hướng …".
Luôn đưa lệnh màu cố định:

```text
dùng style ttpq comic blend để dàn trang màu, outline chỉ dùng để tham khảo scene, nhân vật phải được lấy chuẩn từ profile. Không ref lại output cũ
```

## 4. Sửa outline

- Image 1 là outline người dùng đang comment: bản vừa tạo, hoặc bản họ đính
  kèm hay gọi tên. Có nhiều bản mà không rõ bản nào thì hỏi.
- Dịch comment thành body chỉnh, chạy `build-prompt.py --pass edit` với
  `--cast` gồm nhân vật bị sửa.
- Đổi dáng lớn (thêm/bớt người, đổi tư thế gốc, đổi góc máy) vẫn sửa trên ảnh
  như yêu cầu. Nếu kết quả méo tỷ lệ, người dùng có thể xin tạo outline mới;
  khi đó cập nhật brief theo comment rồi chạy lại lượt nét.

## 5. Lên màu và chỉnh màu

- Image 1 là outline người dùng chọn. Lệnh màu đã là sự cho phép, không hỏi
  lại. Không tự lên màu chỉ vì người dùng khen outline.
- Viết body màu, chạy `build-prompt.py --pass color`, gọi ImageGen, lưu
  `outputs/color-vNNN.png`.
- Chỉnh màu: chạy lại lượt màu từ outline được chọn, thêm comment vào body.
  Không đính kèm ảnh màu cũ, trừ khi người dùng yêu cầu rõ hoặc dùng `color-edit`/`swap`.
- Nhân vật lệch profile vì outline sai (mặt, tai, chiều cao, trang phục): chạy
  lại lượt màu với `--recast <slug>` cho nhân vật đó, không bắt buộc sửa outline.
  Cần outline đúng trước khi lên màu: `--pass swap` trên outline (mục dưới).
  `--pass edit --recast` đã bỏ từ 2026-11-25.
- Ảnh màu (hoặc outline) ổn nhưng một nhân vật lệch profile: mặc định
  `--pass swap --cast <slug> --target "<người cần thay, tả theo vị trí>"`
  (từ 2026-11-24). Image 1 là ảnh ref của profile, Image 2 là ảnh đang sửa; mỗi
  lượt một nhân vật; lưu thành `color-vNNN.png` (hoặc `outline-vNNN.png`) mới.
- Swap xong còn sai một dấu hiệu cụ thể: `--pass color-edit --cast <slug>`,
  Image 1 là ảnh màu đó, body một dòng `Change:` cho đúng lỗi (bắt buộc; từ
  2026-11-25 color-edit chỉ sửa chi tiết trong `Change:`, không vẽ lại cả người).
  Trên outline, lỗi chi tiết sửa bằng `--pass edit`.
- Bảng chọn nhánh (2026-11-25):
  - đang lên màu, outline vẽ sai nhân vật → `color --recast`;
  - ảnh có sẵn (màu hoặc outline), cần thay cả nhân vật → `swap`;
  - ảnh màu, sai một chi tiết của nhân vật → `color-edit` + `Change:`;
  - outline, sửa theo comment → `edit` + `Change:`.
- Không tự phê duyệt bản cuối.
