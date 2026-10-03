# Mẫu hội thoại và trạng thái

Chỉ đọc reference này khi cần đặt câu hỏi tại cổng quyết định hoặc tiếp tục một
page dang dở.

## Cấu trúc một lượt hỏi

1. Một câu xác nhận điều vừa biết hoặc vừa hoàn thành.
2. Một câu giải thích quyết định đang cần và tác động của nó.
3. Tối đa ba lựa chọn đánh số; đánh dấu **(Đề xuất)** cho lựa chọn phù hợp nhất.
4. Cuối câu trả lời, trình bày mỗi câu trả lời/bước tiếp theo trong một code
   block riêng để người dùng có thể copy nguyên khối. Không gom nhiều phương án
   vào cùng một block; mỗi block phải tự đủ nghĩa và đặt lựa chọn đề xuất trước.

Ví dụ chọn composition (dùng hàng rào ngoài khác loại để thể hiện khối copy
bên trong):

~~~text
Nguồn đã xác nhận đây là khoảnh khắc cộng đồng nhận ra hậu quả của sự việc.
Mình cần bạn chọn và xác nhận cách kể hình trước khi tạo ảnh:

### Option 2 — Trung cảnh theo nhóm (Đề xuất)

![Composition preview](path/to/preview.png)

- **Ý nghĩa cảnh:** cộng đồng cùng nhận ra hậu quả, không quy toàn bộ ý nghĩa
  cho một nhân vật.
- **Khoảnh khắc:** ngay sau sự việc, khi phản ứng bắt đầu lan qua nhóm.
- **Trọng tâm và eye path:** nhóm gần → dấu vết sự việc → phản ứng lớp sau.
- **Dàn cảnh:** nhóm gần đủ lớn để đọc biểu cảm; đám đông tiếp tục theo chiều
  sâu và không biến thành nền trang trí.
- **Cảm xúc:** sững lại rồi chia sẻ nhận thức; tránh đọc thành hoảng loạn.
- **Bối cảnh bắt buộc:** dấu vết nguyên nhân và bằng chứng về quy mô cộng đồng.
- **Không được xuất hiện:** hệ quả hoặc nhân vật chỉ tới ở scene sau.
- **Layout:** chủ thể chính tránh vùng chữ/gáy; silhouette nhóm còn đọc rõ khi
  đặt ở kích thước thật.
- **Đánh đổi:** cân bằng phản ứng và bối cảnh, nhưng cảm xúc cá nhân nhẹ hơn cận
  cảnh và quy mô kém áp đảo hơn toàn cảnh.

Trình bày Option 1 và Option 3 theo cùng cấu trúc trước khi hỏi người dùng chọn.

Sau khi bạn xác nhận, mình sẽ tự tạo prompt kỹ thuật, tạo ảnh và chạy QA.

Bạn có thể copy một trong các block sau để trả lời:

```text
Chọn 2 — trung cảnh theo nhóm; hãy tạo ảnh và chạy QA.
```

```text
Chọn 1 — toàn cảnh; hãy tạo ảnh và chạy QA.
```

```text
Chọn 3 — cận cảnh nhân vật chính; hãy tạo ảnh và chạy QA.
```

```text
Tôi muốn chỉnh hướng kể hình; tôi sẽ mô tả thay đổi ở câu tiếp theo.
```
~~~

Không dùng lựa chọn “Khác” chung chung nếu có thể mời người dùng mô tả tự do ở
câu kết.

## Phiếu tiến độ nội bộ

Giữ trạng thái trong artifact hiện có của page nếu workflow của page đã có nơi
lưu quyết định. Nếu workflow kéo dài qua nhiều phiên, dùng `page-state` theo mô
hình của `comic-continuity-manager`; nếu chưa cần tái sử dụng thì chỉ duy trì
trong hội thoại. Không tạo hai nguồn trạng thái song song.

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
context_revision: {}
stale_reasons: []
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
