# Contract workflow minh họa tập

Áp dụng cho mọi yêu cầu tạo, tiếp tục, chỉnh sửa, variant hoặc hoàn thiện minh
họa theo tập/part/page/frame. Không áp dụng cho Character Studio và Image
Playground; hai studio dùng [contract studio](../docs/studio-contract.md).

Tài liệu này giữ quy tắc nền riêng của workflow minh họa tập. Các bước thực
hiện, schema, cổng xác nhận và tiêu chí QA được quản lý trong skill tương ứng;
không sao chép các chi tiết đó vào đây khi cập nhật workflow. Quy tắc chung của
project vẫn theo [AGENTS.md](../AGENTS.md).

## Entry point

- Yêu cầu minh họa theo tập/page/frame mặc định đi qua `comic-page-guide`, kể
  cả khi người dùng đã nêu rõ deliverable.
- Chỉ dùng `comic-production` khi người dùng gọi đích danh skill đó hoặc yêu
  cầu rõ dùng `comic-production`; không tự động đọc hoặc gọi nó từ
  `comic-page-guide`.
- `comic-page-guide` điều phối các skill chuyên môn; đọc mô tả và hướng dẫn của
  skill phù hợp cho tác vụ độc lập.
- Mention profile trong một tập không tự biến yêu cầu studio thành minh họa tập.

## Phạm vi nguồn

- Mỗi thư mục tập là một đơn vị nội dung độc lập.
- Không lấy profile, layout, bối cảnh, script hoặc asset từ tập khác để thay thế.
- Trước công việc phụ thuộc nội dung tập, xác định đúng tập, part, page và frame.
  Tái sử dụng context còn hiệu lực; cách truy xuất và kiểm chứng nguồn thuộc
  `comic-source-reader` và `comic-continuity-manager`.
- Context đã biên dịch phải giữ provenance; không được tóm tắt nối tiếp từ bản
  tóm tắt cũ rồi coi kết quả là nguồn gốc.
- Nếu nguồn cấp tập bị thiếu, chỉ coi đó là blocker khi deliverable thật sự phụ
  thuộc vào nguồn đó.

## Thứ tự ưu tiên

Chi tiết hóa thứ tự ưu tiên chung trong `AGENTS.md` cho workflow minh họa tập:

1. Yêu cầu trực tiếp mới nhất của người dùng.
2. Dữ kiện và ngoại lệ trong `notes.md` của đúng tập.
3. Continuity hoặc ngoại lệ trong `shot_notes.md` của đúng tập.
4. Skill phù hợp trong `.agents/skills/`.
5. Contract này, quy tắc nền trong `AGENTS.md` và policy chung được dẫn chiếu.
6. Giả định sáng tạo của agent.

## Identity nhân vật

- Profile gốc trong đúng tập là chuẩn identity. Không dùng output trước làm
  chuẩn thay thế.
- Trước mỗi lần tạo/chỉnh ảnh có nhân vật, đọc lại profile reference gốc trong
  tập của từng nhân vật xuất hiện, kể cả khi ảnh nguồn hoặc revision trước đã
  được kiểm.

## Trình bày lựa chọn

Quy tắc trình bày option trong `AGENTS.md` áp dụng cả cho hướng kể và
composition card: tách từng mục như cảm nhận, ý nghĩa, khoảnh khắc, trọng tâm,
cách kể, cỡ cảnh/bố trí và đánh đổi thành đầu dòng riêng, giữ các mục theo
skill đang áp dụng.

## Output và bàn giao

- Ảnh minh họa mới/variant nằm trong `outputs/` của đúng tập/page.
- Chỉ đưa output vào `approved/` sau khi người dùng chọn rõ và đạt QA áp dụng;
  thực hiện bàn giao và cập nhật đường dẫn theo `comic-delivery`.
- Không đưa asset của tập khác vào deliverable cuối.

## Vị trí dữ liệu

- Thư mục tập mới tạo tại `comic-illustrator/Tap XX/`; tài liệu tham khảo của
  workflow đặt trong `comic-illustrator/referrences/`.
- Đường dẫn dạng `Tap XX/...` trong record, manifest và delivery receipt tính
  từ `comic-illustrator/`; `projectRoot` của manifest delivery trỏ về đây.
