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

Ví dụ chọn narrative direction nhanh, chưa tạo ảnh (dùng hàng rào ngoài khác
loại để thể hiện khối copy bên trong):

~~~text
Nguồn đã xác nhận đây là khoảnh khắc cộng đồng nhận ra hậu quả của sự việc.
Mình cần bạn chọn cảm nhận và hướng kể trước khi dựng composition:

### Direction 1 — Nhận ra cùng nhau (Đề xuất)

1. **Cảm nhận muốn để lại:** sững lại, rồi cảm giác cùng chia sẻ một nhận thức.
2. **Ý nghĩa hình ảnh:** biến chuyển thuộc về cả cộng đồng, không phải một cá nhân.
3. **Khoảnh khắc:** ngay sau sự việc, khi phản ứng bắt đầu lan qua nhóm.
4. **Trọng tâm cảm xúc:** ánh mắt và khoảng cách giữa nhóm gần với lớp người sau.
5. **Cách kể dự kiến:** observational, diễn xuất nhóm tự nhiên.
6. **Cỡ cảnh dự kiến và khả năng bố trí trong layout:** toàn cảnh vừa để đọc phản ứng nhóm và quy mô cộng đồng; nhóm gần đủ lớn để thấy hướng nhìn, lớp người sau gợi quy mô. Hình có thể mở từ vùng trống dưới lên giữa trang, chữ reflow quanh nhóm gần nếu contract cho phép; đây là đánh giá định tính từ layout đã đọc, chưa khóa tọa độ hay camera.
7. **Đánh đổi:** cảm xúc cộng đồng mạnh; biểu cảm cá nhân sẽ nhẹ hơn cận cảnh.

Trình bày Direction 2–3 theo cùng cấu trúc. Chưa tạo preview hay storyboard đầy đủ.

Bạn có thể copy một trong các block sau để trả lời:

```text
Chọn Direction 1 — Nhận ra cùng nhau; hãy dựng composition.
```

```text
Chọn Direction 2 — Khoảnh khắc cá nhân; hãy dựng composition.
```

```text
Tôi muốn chỉnh hướng kể hình; tôi sẽ mô tả thay đổi ở câu tiếp theo.
```
~~~

Sau khi direction được chọn, chỉ dựng một composition và trình preview cùng
card chín mục. Kết thúc cổng bằng các câu trả lời:

```text
Duyệt composition này; hãy tạo ảnh và chạy QA.
```

```text
Giữ direction đã chọn nhưng chỉnh composition như sau: …
```

```text
Quay lại bước chọn narrative direction.
```

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
  narrative_direction: false
  composition: false
  production_run: false
  qa_resolution: false
  final_output: false
active_direction: null
active_choice: null
pending_question: confirm_target
context_revision: {}
stale_reasons: []
```

`stage` chỉ nhận một trong: `scope`, `source`, `direction`, `composition`, `production`,
`visual_qa`, `selected_for_layout`, `layer_package`, `layout_qa`, `delivery`,
`complete`. `production` bao gồm viết prompt kỹ thuật và tạo master; tách layer
chỉ chạy ở `layer_package` sau khi người dùng chọn master.

## Diễn giải thuật ngữ

- `profile`: ảnh chuẩn giúp giữ đúng diện mạo nhân vật.
- `composition`: cách đặt nhân vật, bối cảnh và điểm nhìn trong khung.
- `visual QA`: kiểm tra ảnh có đúng nhân vật, bối cảnh, phong cách và câu chuyện.
- `layout QA`: kiểm tra ảnh khi đặt vào khung trang, vùng chữ, mép cắt và gáy.
- `selected-for-layout`: master đã được người dùng chọn; cho phép tách layer
  InDesign nhưng chưa phải bộ nguồn chuẩn cuối.
- `layer-package-ready`: bộ `master + bg + mgfg + wrap + layout-preview` đã qua
  QA kỹ thuật.
- `approved`: cả bộ cuối đã được bàn giao làm nguồn chuẩn.

Chỉ giải thích thuật ngữ khi nó xuất hiện trong câu trả lời dành cho người dùng.

## Câu trả lời đặc biệt

- “Tiếp tục”: chỉ thực hiện hành động đã mô tả ngay trước đó; không vượt thêm
  cổng kế tiếp. Nếu ngay trước đó là chọn direction, chỉ dựng composition. Nếu
  ngay trước đó là xác nhận composition, thực hiện trọn chuỗi prompt → tạo ảnh
  → visual QA → layout QA/overlay khi áp dụng.
- “Tự chọn giúp tôi”: chọn phương án được đề xuất, xác nhận lại lựa chọn bằng
  một câu và chỉ tiếp tục trong phạm vi cổng hiện tại.
- “Làm luôn”: nếu phạm vi chưa rõ, vẫn phải khóa target; nếu đã rõ, có thể tiến
  hành đến cổng sáng tạo hoặc tạo ảnh gần nhất nhưng không tự duyệt delivery.
- “Quay lại”: nêu quyết định nào sẽ bị mở lại và artifact downstream nào có thể
  cần tạo version mới; không xóa output cũ.
