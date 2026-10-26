# Contract chung cho hai studio

Character Studio và Image Playground là không gian làm việc bằng thư mục và
skill trong repository, không phải ứng dụng hoặc chat mới. Không tự tạo chat.

## Style và nguồn

- Đọc [project-style-policy.md](project-style-policy.md) trước thiết kế, prompt,
  tạo/chỉnh ảnh và QA. Policy bắt buộc cho mọi ảnh ở cả hai studio, gồm bản thử,
  sheet, edit và variant; áp dụng cả ngoại lệ nền trời hiện hành.
- Resolve style mặc định từ policy chung cùng tài liệu định nghĩa style được
  dẫn chiếu; áp dụng các yêu cầu thực thi prompt và QA tại đó cho mọi lượt mới,
  kể cả khi tiếp tục brief hoặc chỉnh output cũ. Ghi style áp dụng trong record.
- Reference cung cấp identity, trang phục, pose hoặc bố cục theo vai trò chỉ định;
  không tự nhập style trái policy. Nếu người dùng yêu cầu thay style rõ, xử lý
  theo thứ tự ưu tiên AGENTS.md và ghi `SKIPPED_BY_USER` đúng phạm vi; không suy
  ngoại lệ từ style của ảnh đính kèm.
- Resolve @mention thành file/tài nguyên thực sự truy cập được. Không đoán identity
  từ tên file hoặc chuỗi @. Nếu reference thiết yếu không truy cập được, yêu cầu
  chỉ định lại nguồn; vẫn làm phần brief độc lập có thể làm.
- Trước MỖI lượt tạo/chỉnh có nhân vật đã có profile, đọc lại mô tả gốc và xem ảnh
  reference gốc của từng nhân vật, truyền đúng reference vào lượt tạo. Output cũ
  chỉ là ảnh đích hoặc nguồn pose, không thay chuẩn identity. Riêng Character
  Studio: chỉ tạo lại từ ảnh gốc, không dùng output làm ảnh đích hay ref; xem
  mục **Chỉ tạo lại từ ảnh gốc** trong `comic-character-studio`.
- Được dùng profile từ tập khi người dùng chỉ định rõ; ghi đường dẫn nguồn,
  không tự lấy asset tập khác thay thế. Không bắt khai báo tập/part/page/frame.
  Chỉ đọc notes/script/continuity nếu yêu cầu thực sự phụ thuộc nội dung đó.

## Tạo ảnh và kiểm tra

- Áp dụng [contract kiểm hình](visual-review-contract.md) cho reference,
  QA theo vùng, điều kiện chuyển bước và giới hạn công cụ. Đây là kiểm studio,
  không gọi toàn workflow Visual QA của tập. Chân dung chì trong luồng chuyển
  ảnh gốc thành profile mới do Character Studio quy định riêng.

- Khi tạo/chỉnh raster, dùng skill `imagegen` và ImageGen trực tiếp; không gọi
  `comic-image-production`, `comic-prompt-writer`, `comic-shot-design`,
  `comic-layout-qa` hay `comic-delivery` làm chuỗi mặc định.
- Chuẩn bị công cụ theo [project-toolchain.md](project-toolchain.md) khi cần
  tạo ảnh/script/PDF/QA; trao đổi brief hoặc sửa Markdown không cần bootstrap.
- Brief đủ rõ thì bắt đầu ngay bước phù hợp của studio. Không bắt source gate,
  composition card, preview shot, page-state, layout QA hoặc InDesign. Riêng
  Character Studio chuyển ảnh gốc thành profile mới mặc định chuyển trực tiếp
  ảnh nguồn sang style dự án, giữ nguyên chi tiết → QA → chờ người dùng duyệt
  ảnh chuyển style → tạo sheet. Khi người dùng duyệt ảnh đạt kiểm thì thực
  hiện bước sheet; không tự dựng sheet trước duyệt. Nhánh nét chì/line art và
  nhánh bảng màu, lên màu được giữ nhưng chỉ thực hiện khi người dùng yêu cầu
  rõ nhánh tương ứng. Chi tiết input, reference, ngoại lệ và kiểm/chọn do
  `comic-character-studio` quản lý; không bắt tô phẳng toàn nhân vật.
- Xem ảnh kết quả, kiểm style policy, identity từng người, anatomy/pose và yêu
  cầu cụ thể; sheet phải nhất quán giữa các góc. Báo lỗi thấy được, không ghi
  PASS khi chưa xem. Với lỗi rõ sửa an toàn được và còn trong brief, tự sửa
  một lần có mục tiêu, kiểm regression; ghi số lượt và phần đã giữ.
  Trong Character Studio, lượt tự sửa chạy lại từ ảnh gốc với prompt bổ sung.
  Nếu vẫn lỗi, trình trạng thái và chờ hướng tiếp, không tự tạo vô hạn.
- Hiển thị ảnh và đường dẫn lưu. Không tuyên bố canon hoặc phê duyệt thay người dùng.

## Lưu trữ và provenance

- Character Studio: `studios/character/briefs/<character-id>.md`,
  `studios/character/outputs/<character-id>/`,
  `studios/character/profiles/<character-id>/`.
- Playground: `studios/playground/outputs/<request-id>/`.
- Tạo thư mục con khi cần; dùng tên ngắn ổn định. Mọi ảnh/prompt/record mới có
  version `v001`, `v002`…; không ghi đè (brief cũng tạo version khi thay đổi).
  Lưu ảnh thực vào workspace, không chỉ tham chiếu file cache công cụ.
- Người dùng chốt ngày 2026-10-24: mọi file output của một lượt studio phải
  được copy vào thư mục output của đúng studio đó (`studios/character/outputs/<character-id>/`
  hoặc `studios/playground/outputs/<request-id>/`), gồm ảnh tạo và ảnh crop/đệm
  nguồn (`references/`). Không để output chỉ nằm ở cache công cụ, thư mục tạm
  hay scratchpad; ảnh output trình cho người dùng phải là bản trong thư mục
  output của studio. Ảnh so sánh/overlay/zoom chỉ dùng cho QA không cần lưu. Không lưu output của studio này sang
  studio khác hoặc vào thư mục tập.
- Mỗi version có record Markdown cùng tên: yêu cầu, prompt đầy đủ, nguồn profile
  và vai trò reference (đường dẫn tương đối trong repo hoặc định danh ngoài repo),
  ảnh output, parentVersion nếu chỉnh, kết quả kiểm và override nếu có.
- Record trỏ brief revision đang có hiệu lực và thay đổi yêu cầu theo
  contract kiểm hình; không để yêu cầu mới chỉ tồn tại trong chat/prompt.
- Chỉ khi người dùng chọn rõ version và kiểm áp dụng đạt mới copy bản profile
  vào `profiles/<character-id>/` với tên có version, kèm record trỏ về output
  và nguồn gốc. Nếu còn lỗi, nêu rõ và cần lựa chọn/override cụ thể trước khi lưu
  chính thức. Không tự cập nhật profile tập, approved tập hoặc continuity.
- Dùng ảnh studio cho trang truyện sau này là tác vụ minh họa mới: route qua
  `comic-page-guide`, kiểm nguồn/QA áp dụng, không kế thừa duyệt của studio.
