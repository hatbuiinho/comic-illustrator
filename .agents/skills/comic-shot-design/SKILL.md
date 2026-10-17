---
name: comic-shot-design
description: Thiết kế storyboard, shot và phương án composition cho truyện tranh từ nguồn đã kiểm chứng. Dùng khi cần focus, khoảnh khắc, camera, emotional flow hoặc composition card; không dùng để tạo ảnh cuối.
---

# Thiết kế shot

Đọc [quy tắc nghệ thuật](references/art-first-policy.md). Nguồn và identity xác định điều đúng; direction xác định cảm nhận; composition quyết định cách thể hiện.

## Đánh giá không gian trước khi đề xuất shot

Thứ tự: nguồn đã xác nhận → đánh giá không gian chữ–hình → xác định ưu tiên
cảm xúc → đề xuất cỡ cảnh và hướng kể → dựng composition.

Trước khi đưa option:

- Kiểm tra canvas, lượng chữ, cỡ đọc, gáy, trim, fixed element và mask thật.
- Xác định vùng có thể vẽ: kích thước, hình dạng, độ liên tục và khả năng dàn
  lại chữ theo contract. Xét cả khoảng trống hiện có và không gian có thể tạo
  bằng dàn lại chữ.
- Chọn tín hiệu cần đọc rõ để truyền cảm xúc: ánh mắt, biểu cảm, cử chỉ, tư thế
  hoặc quan hệ nhân vật; đánh giá khả năng đọc ở kích thước trang.
- Tách nội dung thành: trọng tâm cần thấy rõ; context cần thấy đủ; chi tiết có
  thể hàm ý hoặc ngoài khung.
- Từ không gian và ưu tiên trên, chọn cỡ cảnh khả thi. Nêu đánh đổi giữa diễn
  xuất, quy mô và bối cảnh.
- Trình kết luận không gian ngắn trước các option. Mỗi option phải giải thích
  vì sao cỡ cảnh phù hợp với trang. Thiếu bằng chứng thì ghi phần chưa kiểm.

Cấm:

- Đề xuất cỡ cảnh trước khi đánh giá không gian.
- Coi khoảng trống dưới chữ hoặc `briefRegion` là khung bắt buộc khi không có
  hard frame/mask thật.
- Thu nhỏ chữ, bỏ nội dung hoặc thu nhỏ nhân vật đến mức mất tín hiệu cảm xúc
  để nhét hình.
- Đưa mọi dữ kiện nguồn vào hình với cùng mức ưu tiên.
- Khẳng định bố cục khả thi chỉ bằng câu “chữ ôm hình”.
- Khóa camera, crop, staging hoặc tọa độ trước khi người dùng chọn hướng kể.
- Báo chữ đã vừa khi chưa có bằng chứng theo contract.

Agent tự thực hiện bước đánh giá; không thêm cổng xác nhận. Kiểm proxy chi
tiết ở bước composition.

## Chọn hướng kể

- Trước lần đề xuất đầu tiên, đọc [ngôn ngữ điện ảnh](references/cinematic-language.md)
  và thực hiện sàng lọc hướng kể trong reference đó. Mỗi hướng phải chuyển ý
  nghĩa thành trải nghiệm nhìn cụ thể, đủ sức kể ngay từ lượt đầu.
- Ưu tiên cảm nhận → ý nghĩa → ý tưởng thị giác → diễn xuất/quan hệ → khoảnh khắc → nhịp hình → context vừa đủ.
- Highlight trong layout là ưu tiên kể chuyện, không phải yêu cầu thêm hiệu ứng hoặc sao chép vị trí hình.
- Đề xuất 1–3 hướng khác nhau thật sự; mỗi hướng gồm bảy mục: Cảm nhận muốn để lại, Ý nghĩa hình ảnh, Khoảnh khắc, Trọng tâm cảm xúc, Cách kể dự kiến, Cỡ cảnh dự kiến và khả năng bố trí trong layout, Đánh đổi.
- Trong **Cách kể dự kiến**, tích hợp ngắn gọn điểm nhìn của người đọc, cơ chế
  thị giác, trình tự mắt khám phá thông tin và bằng chứng cảm xúc nhìn thấy.
  Đây là giả thuyết để chọn direction; camera/crop/staging cụ thể còn mở tới
  bước composition. Không thêm mục hoặc cổng duyệt mới.
- Các option phải khác về trải nghiệm đọc hoặc quan hệ thị giác; chỉ đổi cỡ
  cảnh/góc máy hay đặt tên cảm xúc khác cho cùng cách kể chưa tạo hướng mới.
- Mỗi option dùng kết quả đánh giá không gian ở trên để đề xuất cỡ cảnh, mức
  chiếm trang/tỷ lệ nhân vật và cách bố trí chữ–hình dự kiến. Nêu tín hiệu cảm
  xúc đọc được và đánh đổi về quy mô, bối cảnh.
- Cỡ cảnh ở bước option là đề xuất để chọn hướng, chưa phải composition đã chốt. Chưa dựng preview hoặc khóa camera, crop, staging hay tọa độ trước khi người dùng chọn direction; triển khai và kiểm chứng chúng ở bước composition.
- Sau chọn, ghi page-state `confirmed.narrativeDirection: true`, `confirmed.composition: false`.

## Dựng composition đã chọn

- Dùng lượng chữ và cỡ đọc làm ngân sách từ đầu; thiết kế nhịp hình trước, rồi art-direct chữ quanh hình. Cấm lấy khoảng trống layout nguồn làm khuôn staging.
- Chọn cỡ cảnh và crop theo tín hiệu cần đọc, không mặc định toàn thân hoặc medium close-up.
- Diễn xuất phải riêng cho cảnh: gaze, tay, posture, khoảng cách và subtext. Hỏi điều gì khiến hành động này khác hành động thông thường; cấm thay ý nghĩa bằng danh sách đạo cụ.
- Tách hiện diện trong truyện, bằng chứng cần thấy và phần có thể hàm ý. Hoạt động đang diễn ra cần đủ tín hiệu để hiểu đúng, không mặc định mọi người phải hiện trọn trong khung.
- Chọn `sceneExtentPlan` theo ý nghĩa và context tối thiểu; canvas lớn không buộc cảnh phủ trang.
- Ghi `contextLocks`, `forbidden`, `creativeFreedom` riêng. Mỗi hard lock phải có nguồn hoặc xác nhận; inference không tạo hard lock.
- Đánh giá ít nhất một cách kể cạnh tranh trong nội bộ khi bố cục đầu tiên quá thông thường; không tạo option giả hoặc ép người dùng qua thêm gate.

## Preview và QA

- Mặc định dùng ImageGen phác chì tối giản theo [pencil-composition-preview.md](references/pencil-composition-preview.md); đọc reference này trước mỗi lượt tạo/chỉnh preview. Lưu prompt, reference map, artwork và PNG toàn trang với version mới. SVG chỉ dùng khi người dùng chọn rõ, theo [semantic-preview.md](references/semantic-preview.md).
- Ngay lượt đầu, truyền mẫu mức giản nét v02 trong reference trên và đặt yêu cầu khớp mức phác trước nội dung cảnh; so trực tiếp với mẫu trước khi trình. Mẫu chỉ hướng dẫn mật độ nét/mức hoàn thiện, không thay profile, shot hoặc composition hiện tại.
- Preview phải đọc được camera, tỷ lệ, crop, hướng nhìn, cử chỉ chính, lớp sâu và quan hệ chữ–hình ở kích thước trang. Dùng silhouette và nét giản lược riêng cho cảnh; hình hộp/debug hoặc pose chung chỉ là draft nội bộ. Không yêu cầu nét, ánh sáng, chất liệu hoặc biểu cảm hoàn thiện như production.
- ImageGen tạo phác sau khi direction được chọn thuộc bước thiết kế composition, không phải production artwork cuối. Không cần duyệt composition trước khi tạo chính preview đó; vẫn phải duyệt preview trước production ảnh hoàn thiện.
- Tự tạo/chỉnh lại composition đến khi đạt, không giới hạn lượt theo số ảnh và không áp giới hạn hai ảnh của production. Giữ version và phần đã đạt; khi lỗi lặp, đổi cách sửa hoặc xem lại staging/camera trong direction đã chọn. Chỉ trình duyệt khi preview đạt nghệ thuật và QA áp dụng; cần đổi direction/nguồn, công cụ lỗi hoặc người dùng yêu cầu dừng thì báo đúng nguyên nhân. Không coi số lần thử hoặc im lặng là duyệt composition.
- Review nghệ thuật trước khi tinh chỉnh proof kỹ thuật. Nếu hình vô cảm, chia ô hoặc diễn xuất chưa rõ, sửa staging/camera; không bù bằng thêm đạo cụ hay mô tả.
- Với chữ–hình, resolve [contract](../comic-layout-qa/references/text-artwork-integration.md). Proxy giữ lượng/cỡ chữ và nhịp đoạn, cho phép dàn khác mẫu. Sau khi hình đạt, kiểm burden và khả năng dàn chữ trước cổng duyệt.
- Với crop, đọc [crop-read-contract.md](references/crop-read-contract.md); thân phải tiếp tục ngoài trim/khung thật hoặc sau vật che có nghĩa, không fade thân giữa trang.
- Dùng renderer để kiểm artifact; marker đủ không chứng minh ý đồ kể chuyện đã đọc được. Nếu tín hiệu diễn xuất chưa kiểm chứng được bằng nét phác, ghi hạn chế và phần cần kiểm ở production; không tự ghi PASS hoặc thêm mắt/lông mày để làm phác thành ảnh hoàn thiện.
- Mỗi kết luận nghệ thuật phải có dấu hiệu nhìn thấy và hạn chế; kiểm ở thumbnail, kích thước đọc và crop. Cấm tự ghi PASS để mở gate.

## Duyệt và bàn giao

Lưu storyboard và preview riêng theo [storyboard-schema.md](references/storyboard-schema.md), version mới không ghi đè. Artifact chỉ giữ field áp dụng; không tạo placeholder cho đủ schema.

Trình PNG toàn trang và card đúng chín mục: Ý nghĩa cảnh; Khoảnh khắc; Trọng tâm và eye path; Dàn cảnh; Cảm xúc; Bối cảnh bắt buộc; Không được xuất hiện; Ràng buộc layout; Đánh đổi. Không bắt người dùng đọc JSON để hiểu composition.

`selectedPageComposition` là `PROPOSED` tới khi người dùng duyệt preview. Khóa ý nghĩa, moment, camera, quan hệ, hierarchy, crop và nhịp bố cục; placement/scale là định hướng, không khóa từng contour/tọa độ. Chỉ `CONFIRMED` mới sang prompt/production. Chưa tách layer hoặc ghi canon.

Phản hồi về chi tiết: sửa cục bộ. Phản hồi về hành động/cảm xúc: xét lại diễn xuất và camera. Phản hồi hình khô/chia ô: dựng lại staging và nhịp chữ–hình. Giữ direction trừ khi người dùng đổi cảm nhận, focus hoặc khoảnh khắc.

## Reference theo nhu cầu

- [cinematic-language.md](references/cinematic-language.md): bắt buộc trước đề xuất direction; điểm nhìn, khám phá thông tin và sàng lọc hướng kể.
- [emotional-flow.md](references/emotional-flow.md): chuỗi nhiều hình.
- [composition-strategy.md](references/composition-strategy.md): tổ chức nhịp và chiều sâu.
- [proxy typography](../comic-layout-qa/references/proxy-typography-measurement.md): đo kỹ thuật sau thiết kế.
