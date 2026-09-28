# Mẫu hội thoại và trạng thái

Chỉ đọc reference này khi cần đặt câu hỏi tại cổng quyết định hoặc tiếp tục một
page dang dở.

## Cấu trúc một lượt hỏi

1. Một câu xác nhận điều vừa biết hoặc vừa hoàn thành.
2. Một câu giải thích quyết định đang cần và tác động của nó.
3. Tối đa ba lựa chọn đánh số; đánh dấu **(Đề xuất)** cho lựa chọn phù hợp nhất.
4. Một khối code cuối câu trả lời chứa các câu trả lời/bước tiếp theo có thể
   copy nguyên dòng. Mỗi dòng phải tự đủ nghĩa; đặt lựa chọn đề xuất trước.

Ví dụ chọn composition (dùng hàng rào ngoài khác loại để thể hiện khối copy
bên trong):

~~~text
Nguồn đã xác nhận đây là khoảnh khắc cộng đồng nhận ra hậu quả của sự việc.
Mình cần bạn chọn và xác nhận cách kể hình trước khi tạo ảnh:

1. Toàn cảnh — thấy rõ quy mô, nhưng cảm xúc cá nhân nhẹ hơn.
2. Trung cảnh theo nhóm — cân bằng phản ứng và bối cảnh. (Đề xuất)
3. Cận cảnh nhân vật chính — cảm xúc mạnh, nhưng giảm bằng chứng cộng đồng.

Sau khi bạn xác nhận, mình sẽ tự tạo prompt kỹ thuật, tạo ảnh và chạy QA.

Bạn có thể copy một dòng để trả lời:

```text
Chọn 2 — trung cảnh theo nhóm; hãy tạo ảnh và chạy QA.
Chọn 1 — toàn cảnh; hãy tạo ảnh và chạy QA.
Chọn 3 — cận cảnh nhân vật chính; hãy tạo ảnh và chạy QA.
Tôi muốn chỉnh hướng kể hình; tôi sẽ mô tả thay đổi ở câu tiếp theo.
```
~~~

Không dùng lựa chọn “Khác” chung chung nếu có thể mời người dùng mô tả tự do ở
câu kết.

## Phiếu tiến độ nội bộ

Giữ trạng thái trong artifact hiện có của page nếu workflow của page đã có nơi
lưu quyết định; nếu chưa có, chỉ duy trì trong hội thoại. Không tạo thêm file
chỉ để lưu trạng thái trừ khi việc tiếp tục qua nhiều phiên thực sự cần nó.

```yaml
target:
  episode: null
  part: null
  page: null
  scope: null
stage: scope
confirmed:
  target: false
  source_snapshot: false
  composition: false
  production_run: false
  qa_resolution: false
  final_output: false
active_choice: null
pending_question: confirm_target
```

`stage` chỉ nhận một trong: `scope`, `source`, `composition`, `production`,
`visual_qa`, `layout_qa`, `delivery`, `complete`. `production` bao gồm viết
prompt kỹ thuật và tạo ảnh; không phải một cổng xác nhận riêng.

## Diễn giải thuật ngữ

- `profile`: ảnh chuẩn giúp giữ đúng diện mạo nhân vật.
- `composition`: cách đặt nhân vật, bối cảnh và điểm nhìn trong khung.
- `visual QA`: kiểm tra ảnh có đúng nhân vật, bối cảnh, phong cách và câu chuyện.
- `layout QA`: kiểm tra ảnh khi đặt vào khung trang, vùng chữ, mép cắt và gáy.
- `approved`: bản cuối đã được người dùng chọn làm nguồn chuẩn.

Chỉ giải thích thuật ngữ khi nó xuất hiện trong câu trả lời dành cho người dùng.

## Câu trả lời đặc biệt

- “Tiếp tục”: chỉ thực hiện hành động đã mô tả ngay trước đó; không vượt thêm
  cổng kế tiếp. Nếu hành động ngay trước đó là xác nhận composition, thực hiện
  trọn chuỗi prompt → tạo ảnh → visual QA → layout QA/overlay khi áp dụng.
- “Tự chọn giúp tôi”: chọn phương án được đề xuất, xác nhận lại lựa chọn bằng
  một câu và chỉ tiếp tục trong phạm vi cổng hiện tại.
- “Làm luôn”: nếu phạm vi chưa rõ, vẫn phải khóa target; nếu đã rõ, có thể tiến
  hành đến cổng sáng tạo hoặc tạo ảnh gần nhất nhưng không tự duyệt delivery.
- “Quay lại”: nêu quyết định nào sẽ bị mở lại và artifact downstream nào có thể
  cần tạo version mới; không xóa output cũ.
