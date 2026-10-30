# Checklist tự kiểm gói prompt

Ghi kết quả từng mục (ĐẠT / SỬA / N/A) vào `record.md`.
Các mục Tin 1/Director's Notes/giới hạn ký tự thuộc nhánh gói prompt, không
ép lên câu lệnh cố định của flow tương tác; xem `interactive-flow.md`.

## Nguồn

- [ ] `layout.json` đúng file và đúng spread; cảnh báo của script đã xử lý.
- [ ] Đã đọc ít nhất một spread trước và một spread sau; bối cảnh truyện trong
      prompt khớp chữ (thời điểm, nơi chốn, đạo cụ, việc đã/chưa xảy ra).
- [ ] Nhân vật có tên dùng profile `APPROVED`, ghi version; ảnh ref tương ứng
      được liệt kê để đính kèm.
- [ ] Không có output cũ (ảnh nét/màu version trước, spread khác) trong danh
      sách đính kèm hoặc lời prompt; chỉ ngoại lệ ảnh nét đã chọn ở lượt màu.
- [ ] Mode và ý đồ điện ảnh khớp `brief.md`.

## Lượt nét

- [ ] Tin 1 là khối STYLE clean outline chép nguyên.
- [ ] Mỗi ảnh đính kèm có dòng "Image N = …"; ảnh profile chỉ để nhận diện.
- [ ] Có câu giữ cỡ chữ, leading, cho reflow ôm hình; VI trái, EN phải; chữ tô
      màu in đen; ô màu là vùng tranh.
- [ ] Chữ EN chép nguyên văn từ bản được chọn; ưu tiên bản người dùng cung cấp.
      Nếu chưa có EN: đã tự dịch đủ chữ VI, soát đối chiếu nội dung/thứ tự đoạn/
      tên riêng/thuật ngữ, lưu file EN có version và ghi nguồn agent dịch.
- [ ] Director's Notes: khoảnh khắc, vị trí theo %, gáy chỉ có nền, đường mắt,
      chữ ôm hình, bối cảnh.
- [ ] Độ dài ≤ ~4.000 ký tự (không tính chữ EN); bố cục nằm trước nhân vật/cấm.

## Lượt màu

- [ ] Có khối STYLE màu chép nguyên.
- [ ] Outline chỉ tham khảo scene và chữ; nhân vật theo profile gốc, không
      khóa contour/identity theo output cũ. Giữ chữ (vị trí, ngắt dòng, đường
      ôm), trừ yêu cầu đổi rõ. Chỉ khóa nét khi người dùng yêu cầu riêng.
- [ ] Nhận diện nhân vật theo ảnh ref; ánh sáng cảnh ghi rõ và ưu tiên hơn
      "daylight" của style khi khác thời điểm.
- [ ] Độ dài ≤ ~4.000 ký tự.

## Điều cấm

- [ ] Cả hai lượt có điều cấm áp dụng: style, era liên quan, theo bối cảnh truyện
      (việc chưa xảy ra, đạo cụ dễ hiểu sai), gáy, chữ đè mặt/tay.
- [ ] Ngoại lệ profile (ví dụ áo may của nhân vật) không bị cấm nhầm.
- [ ] Không có từ kéo về 3D/ảnh thật (octane, unreal, photoreal, volumetric, bokeh…).

## Định dạng

- [ ] Mỗi prompt trọn trong một code block; không còn `<...>` chưa thay.
- [ ] Canvas đúng mode.

## Khối bối cảnh

- [ ] Cảnh `Snn` đúng spread; ghi trạng thái (DRAFT dùng theo yêu cầu người dùng).
- [ ] Khớp cảnh trước/sau: việc đã xảy ra, chưa xảy ra; tiến độ công trình
      theo bible.
- [ ] Quyết định trong `bible.md`/`record.md` (Cần quyết, SKIPPED_BY_USER) đã áp.
- [ ] Nhân vật có profile `APPROVED`: ghi số ảnh, chỉ dùng để nhận diện.
- [ ] Mục KHÔNG ĐƯỢC có điều cấm truyện và niên đại liên quan; không cấm nhầm
      ngoại lệ profile.
- [ ] Viết tiếng Việt, trọn một code block, không còn `<...>`.
- [ ] Trình kèm link `layout-ref.png` của spread và link profile + ảnh ref của
      từng nhân vật liên quan; số ảnh khớp với khối.
- [ ] Cuối phản hồi có câu đọc context nguyên văn trong `interactive-flow.md`,
      dẫn đúng version context; chưa tự tạo ảnh.
