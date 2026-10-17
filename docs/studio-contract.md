# Contract chung cho hai studio

Character Studio và Image Playground là không gian làm việc bằng thư mục và
skill trong repository, không phải ứng dụng hoặc chat mới. Không tự tạo chat.

## Style và nguồn

- Đọc [project-style-policy.md](project-style-policy.md) trước thiết kế, prompt,
  tạo/chỉnh ảnh và QA. Policy bắt buộc cho mọi ảnh ở cả hai studio, gồm bản thử,
  sheet, edit và variant; áp dụng cả ngoại lệ nền trời hiện hành.
- Reference cung cấp identity, trang phục, pose hoặc bố cục theo vai trò chỉ định;
  không tự nhập style trái policy. Nếu người dùng yêu cầu thay style rõ, xử lý
  theo thứ tự ưu tiên AGENTS.md và ghi `SKIPPED_BY_USER` đúng phạm vi; không suy
  ngoại lệ từ style của ảnh đính kèm.
- Resolve @mention thành file/tài nguyên thực sự truy cập được. Không đoán identity
  từ tên file hoặc chuỗi @. Nếu reference thiết yếu không truy cập được, yêu cầu
  chỉ định lại nguồn; vẫn làm phần brief độc lập có thể làm.
- Trước MỖI lượt tạo/chỉnh có nhân vật đã có profile, đọc lại mô tả gốc và xem ảnh
  reference gốc của từng nhân vật, truyền đúng reference vào lượt tạo. Output cũ
  chỉ là ảnh đích hoặc nguồn pose, không thay chuẩn identity.
- Được dùng profile từ tập khi người dùng chỉ định rõ; ghi đường dẫn nguồn,
  không tự lấy asset tập khác thay thế. Không bắt khai báo tập/part/page/frame.
  Chỉ đọc notes/script/continuity nếu yêu cầu thực sự phụ thuộc nội dung đó.

## Tạo ảnh và kiểm tra

- Khi tạo/chỉnh raster, dùng skill `imagegen` và ImageGen trực tiếp; không gọi
  `comic-image-production`, `comic-prompt-writer`, `comic-shot-design`,
  `comic-layout-qa` hay `comic-delivery` làm chuỗi mặc định.
- Chuẩn bị công cụ theo [project-toolchain.md](project-toolchain.md) khi cần
  tạo ảnh/script/PDF/QA; trao đổi brief hoặc sửa Markdown không cần bootstrap.
- Brief đủ rõ thì tạo ngay. Chỉ đề xuất hướng hoặc chờ chọn khi người dùng yêu
  cầu hay thiếu quyết định thiết yếu; không bắt source gate, composition card,
  preview chì, page-state, layout QA hoặc InDesign.
- Xem ảnh kết quả, kiểm style policy, identity từng người, anatomy/pose và yêu
  cầu cụ thể; sheet phải nhất quán giữa các góc. Báo lỗi thấy được, không ghi
  PASS khi chưa xem. Có thể sửa một lần có mục tiêu nếu lỗi rõ và còn trong brief;
  nếu vẫn lỗi, trình trạng thái và chờ hướng tiếp, không tự tạo vô hạn.
- Hiển thị ảnh và đường dẫn lưu. Không tuyên bố canon hoặc phê duyệt thay người dùng.

## Lưu trữ và provenance

- Character Studio: `studios/character/briefs/<character-id>.md`,
  `studios/character/outputs/<character-id>/`,
  `studios/character/profiles/<character-id>/`.
- Playground: `studios/playground/outputs/<request-id>/`.
- Tạo thư mục con khi cần; dùng tên ngắn ổn định. Mọi ảnh/prompt/record mới có
  version `v001`, `v002`…; không ghi đè (brief cũng tạo version khi thay đổi).
  Lưu ảnh thực vào workspace, không chỉ tham chiếu file cache công cụ.
- Mỗi version có record Markdown cùng tên: yêu cầu, prompt đầy đủ, nguồn profile
  và vai trò reference (đường dẫn tương đối trong repo hoặc định danh ngoài repo),
  ảnh output, parentVersion nếu chỉnh, kết quả kiểm và override nếu có.
- Chỉ khi người dùng chọn rõ version và kiểm áp dụng đạt mới copy bản profile
  vào `profiles/<character-id>/` với tên có version, kèm record trỏ về output
  và nguồn gốc. Nếu còn lỗi, nêu rõ và cần lựa chọn/override cụ thể trước khi lưu
  chính thức. Không tự cập nhật profile tập, approved tập hoặc continuity.
- Dùng ảnh studio cho trang truyện sau này là tác vụ minh họa mới: route qua
  `comic-page-guide`, kiểm nguồn/QA áp dụng, không kế thừa duyệt của studio.
