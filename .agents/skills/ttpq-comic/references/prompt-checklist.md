# Checklist tự kiểm gói prompt

Ghi kết quả từng mục (ĐẠT / SỬA / N/A) vào `record.md`.
Áp cho prompt ImageGen agent viết, không áp lên câu lệnh cố định của người
dùng. Quy tắc viết nằm ở `prompt-template.md`; checklist chỉ đối chiếu.

## Nguồn

- [ ] `layout.json` đúng file và đúng spread; cảnh báo của script đã xử lý.
- [ ] Đã đọc ít nhất một spread trước và một spread sau; bối cảnh truyện trong
      prompt khớp chữ (thời điểm, nơi chốn, đạo cụ, việc đã/chưa xảy ra).
- [ ] Nhân vật có tên dùng profile `APPROVED`, ghi version; ảnh ref tương ứng
      được liệt kê để đính kèm.
- [ ] Không có output cũ (ảnh nét/màu version trước, spread khác) trong danh
      sách đính kèm hoặc lời prompt; chỉ ngoại lệ ảnh nét đã chọn ở lượt màu.
- [ ] Prompt viết từ khối active của `brief.md` (5 mục), không từ lịch sử.

## Lượt nét

- [ ] Khối STYLE clean outline chép nguyên ở đầu.
- [ ] Chỉ có các khối của mẫu: Image, STORY, INTENT, TEXT, DO NOT, chữ EN.
- [ ] INTENT: cảm xúc + mỗi trang/scene một focus và góc máy; scene chính ghi rõ.
- [ ] TEXT giữ khổ chữ và vị trí dòng đầu, reflow ôm hình trong cột; VI trái,
      EN phải.
- [ ] Chữ EN chép nguyên văn từ bản được chọn; ưu tiên bản người dùng cung cấp.
      Nếu chưa có EN: đã tự dịch đủ chữ VI, soát đối chiếu nội dung/thứ tự đoạn/
      tên riêng/thuật ngữ, lưu file EN có version và ghi nguồn agent dịch.
- [ ] Không luật vá, không mô tả lại identity của nhân vật có profile, không
      nhắc output cũ.

## Lượt màu

- [ ] Khối STYLE màu chép nguyên; theo mẫu lượt màu.
- [ ] Outline chỉ tham khảo scene và chữ; nhân vật theo profile gốc. Chỉ khóa
      nét khi người dùng yêu cầu riêng.

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
- [ ] DIỄN BIẾN TRONG CHỮ tách beat từng dòng, có câu "chỉ vẽ một khoảnh
      khắc"; KHOẢNH KHẮC ĐƯỢC VẼ chép 5 mục của phương án
      active, hoặc "Chưa chọn" khi chưa có. CON NGƯỜI chỉ có nhận diện tĩnh.
- [ ] Nhân vật có profile `APPROVED`: ghi số ảnh, chỉ dùng để nhận diện.
- [ ] Mục KHÔNG ĐƯỢC có điều cấm truyện và niên đại liên quan; không cấm nhầm
      ngoại lệ profile.
- [ ] Viết tiếng Việt, trọn một code block, không còn `<...>`.
- [ ] Trình kèm link `layout-ref.png` của spread và link profile + ảnh ref của
      từng nhân vật liên quan; số ảnh khớp với khối.
- [ ] Cuối phản hồi có câu đọc context nguyên văn trong `interactive-flow.md`,
      dẫn đúng version context; chưa tự tạo ảnh.
