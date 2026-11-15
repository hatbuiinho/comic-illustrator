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

- **Đề xuất:** các phương án khác nhau ở khoảnh khắc, focus hoặc góc máy; mỗi
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
dùng style ttpq comic light để vẽ hình minh họa và dàn trang cho page này ở dạng clean outline, chữ sẽ hòa với hình nhưng giữ nguyên khổ chữ, giữ nguyên vị trí dòng đầu tiên, chữ có thể được reflow để ôm hình 1 cách sống động, phần chữ bên phải là tiếng anh, bên trái là tiếng việt, truyện này là truyện về cuộc đời Đức Phật nên nhân vật sẽ là người Ấn Độ thời đó ạ
```

- Lệnh "Chọn phương án N … tạo clean outline" cũng kích hoạt bước này.
- Lệnh ghi `ttpq comic soft` hoặc `ttpq comic blend` thay cho `ttpq comic light`
  thì chạy script với `--style soft` hoặc `--style blend`; không ghi thì là light.
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
3. Đối chiếu trước khi chạy: hành động chính (động từ), góc máy và chữ ôm hình
   của từng trang trong brief đều có trong body; không câu nào trái brief.
4. Lưu body thành `prompts/vNNN-outline.body.txt` cùng version với prompt.

## 3. Sau outline

Người dùng comment tự do để sửa, hoặc nói "tạo outline khác theo hướng …".
Luôn đưa lệnh màu cố định:

```text
dùng style ttpq comic light để dàn trang màu, outline chỉ dùng để tham khảo scene, nhân vật phải được lấy chuẩn từ profile. Không ref lại output cũ
```

Nếu người dùng muốn bản soft, đưa thêm lệnh song song (script `--style soft`;
outline light vẫn dùng được):

```text
dùng style ttpq comic soft để dàn trang màu, outline chỉ dùng để tham khảo scene, nhân vật phải được lấy chuẩn từ profile. Không ref lại output cũ
```

Nếu người dùng muốn test bản blend (script `--style blend`):

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
  Không đính kèm ảnh màu cũ, trừ khi người dùng yêu cầu rõ.
- Không tự phê duyệt bản cuối.
