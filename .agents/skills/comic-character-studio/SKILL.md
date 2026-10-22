---
name: comic-character-studio
description: Tạo, phát triển hoặc chỉnh character profile và character sheet trong Character Studio, giữ style dự án; độc lập với workflow minh họa tập/page.
---

# Character Studio

Đọc và áp dụng [contract studio](../../../docs/studio-contract.md)
và [policy phong cách](../../../docs/project-style-policy.md).

## Hướng dẫn người dùng và bước tiếp theo

- Khi bắt đầu nhân vật mới từ ảnh gốc, giới thiệu ngắn một lần:
  `Ảnh gốc → chuyển trực tiếp sang style dự án, giữ nguyên chi tiết → chờ người dùng duyệt → sheet → chọn và lưu profile`.
  Với tác vụ chỉ chỉnh một phần hoặc nhân vật chỉ có brief, nêu đoạn workflow
  thực sự áp dụng, không bắt đi lại các bước đã chọn/đạt.
- Cuối mỗi lần trả kết quả, nêu bước hiện tại, trạng thái đạt/chưa đạt/chờ
  chọn, cùng bước tiếp theo được khuyến nghị và lý do ngắn. Khi cần người
  dùng chọn hướng, đưa 2–3 lựa chọn thực tế có tên rõ, phù hợp trạng thái;
  không ép đủ lựa chọn nếu chỉ có một bước hợp lệ. Mỗi câu trả lời mẫu để
  chọn/sửa đặt trong một code block riêng, thuần văn bản theo AGENTS.md.
- Sau ảnh chuyển style: trình ảnh và kết quả QA, chờ người dùng duyệt rõ
  version đó hoặc yêu cầu chỉnh; không tự dựng sheet trong cùng lượt chuyển
  style. Khi người dùng duyệt ảnh đạt kiểm, chuyển sang tạo sheet, không hỏi
  lại chỉ để xác nhận bước đã được duyệt. Duyệt ảnh chuyển style chưa phải
  duyệt sheet hay cho phép lưu profile.
- Nhánh tùy chọn: chỉ tạo nét chì/line art khi người dùng yêu cầu rõ bước nét;
  chỉ lập bảng màu và lên màu riêng khi người dùng yêu cầu rõ nhánh màu.
  Yêu cầu tạo nét không tự cho phép lập bảng màu/lên màu; không đề xuất nhánh
  này như bước bắt buộc sau ảnh chuyển style. Trong nhánh được yêu cầu, trình
  kết quả đúng phạm vi và giữ các điều kiện kiểm/chọn tương ứng bên dưới.
- Sau sheet: chọn để lưu profile khi đạt QA / chỉnh góc hoặc chi tiết cụ thể /
  tiếp tục xem xét, chưa lưu. Phân biệt duyệt một phần, chọn ảnh để bước tiếp
  và chọn toàn bộ profile; không tự suy phạm vi rộng hơn câu trả lời.
- Nếu chưa đạt QA và còn lượt tự sửa an toàn, thực hiện theo contract thay
  vì hỏi lại. Khi cần người dùng định hướng, nêu lỗi và đề xuất sửa hoặc đổi
  hướng; không đưa lên màu/dựng sheet/lưu profile như hành động đã sẵn sàng
  nếu điều kiện phụ thuộc chưa đạt, trừ override rõ có ghi phạm vi.
- Không tự tạo biến thể hoặc chạy ảnh chỉ vì có lựa chọn trong menu.
  Cổng chờ duyệt ảnh chuyển style trước sheet là bắt buộc trong luồng mặc
  định. Trong nhánh màu được yêu cầu rõ, bảng màu đã kiểm có thể dùng lên màu
  cùng lượt nếu yêu cầu bao gồm lên màu và không thuộc nhánh màu da cần chốt.

## Mục tiêu tạo hình

- Mặc định dùng st03 với cấu trúc mặt và cơ thể tự nhiên: nét/mảng 2D rõ,
  cel-shading mềm tiết chế, màu sạch không hạt.
- Không mặc định mắt lớn, mũi nhỏ, cằm ngắn, đầu to hoặc dáng người mẫu.
  Giữ tuổi, thể trạng và nét riêng theo brief.
- Vẻ đẹp và sự thanh tịnh thể hiện qua ánh mắt, biểu cảm, phong thái và sự
  chỉnh tề; không đồng nghĩa da trắng, trẻ hóa hoặc mặt hoàn hảo.
- Không suy màu da từ tầng lớp, nghề nghiệp hoặc phẩm hạnh. Khi brief cho
  phép tự chọn, ghi đó là lựa chọn thiết kế.
- Không dùng một công thức mặt đại diện mọi người Ấn Độ; không khẳng định
  nguồn gốc dân tộc chỉ từ nét mặt được vẽ.

### Cấm thay đổi tỷ lệ các bộ phận so với ảnh gốc

- Áp dụng cho mọi lượt chuyển style, nét, màu, sheet, variant và sửa lỗi có
  ảnh gốc/profile. Cấm tự thay đổi tỷ lệ bên trong từng bộ phận và tương quan
  giữa các bộ phận: dài–rộng mặt, kích thước/vị trí/khoảng cách mắt–mày–mũi–
  miệng–tai, má–hàm–cằm; đầu–cổ–vai–thân; ngực–eo–hông; chiều dài và bề rộng
  tay/chân, bàn tay/bàn chân và vị trí khớp theo nguồn đang thấy.
- Chuyển style hoặc sửa nét, tuổi, màu, hoa văn, trang phục không cho phép
  model tự cân chỉnh lại giải phẫu hay tỷ lệ. Mỗi prompt thực tế phải có cả
  yêu cầu giữ tỷ lệ và điều cấm rõ trong `Avoid/Negative constraints`, kể cả
  lượt sửa chỉ nhắm một vùng khác. Không chỉ ghi chung “giữ identity”.
- Luôn đối chiếu ảnh gốc, không lấy output đã lệch làm chuẩn tỷ lệ. Chỉ đổi
  tỷ lệ khi người dùng yêu cầu rõ đúng bộ phận/phạm vi đó và ghi
  `SKIPPED_BY_USER`; yêu cầu đổi góc/pose không tự cho phép đổi tỷ lệ cơ thể.
  Góc mới có phối cảnh/co ngắn theo góc nhìn nhưng phải giữ cấu trúc nhân vật.
- QA kiểm tỷ lệ trước style và hoa văn. Thay đổi tỷ lệ thấy rõ là FAIL, kể
  cả khi ảnh còn nhận ra nhân vật hoặc trông đẹp hơn; không hạ thành “lệch
  nhẹ” để chuyển bước. Sai biệt nét/anti-alias không đổi tỷ lệ không phải lỗi
  giải phẫu. Prompt không bảo đảm khóa hình học: nếu model vẫn đổi tỷ lệ,
  báo chưa đạt, tuân giới hạn sửa và không tự dùng làm nền dựng sheet.

Khối điều cấm cần tích hợp và cụ thể hóa theo phần cơ thể xuất hiện:

```text
Preserve the original proportions within every visible body part and the
relative proportions between body parts. Do not resize, lengthen, shorten,
widen, narrow, reposition or rebalance facial features, face, head, neck,
shoulders, torso, waist, hips, arms, legs, hands, feet or joints relative to
the original source. Style transfer and local corrections must not redesign
anatomy or adjust proportions. The original source remains the proportion
authority; previous generated outputs and style references do not replace it.
```

### Không tự lý tưởng hóa nguồn

- Khi có ảnh gốc/profile, giữ nét riêng quan sát được: độ đầy má, rộng/dài
  mặt, kích thước và khoảng cách mắt, bề rộng/độ nhô mũi, hình môi, hàm/cằm,
  tuổi, thể trạng và bất đối xứng tự nhiên đang thấy. Không tự cân xứng hóa,
  nâng mắt, thu mũi, gọt hàm, kéo cổ, làm thon dáng, làm sáng da hoặc trẻ hóa.
  Không tự thêm bất đối xứng hay dấu tuổi khi nguồn không thể hiện rõ.
- Trước mỗi lượt chuyển style, nét, màu hoặc sheet, chọn các dấu riêng thực sự có trong
  nguồn để đưa vào phần bắt buộc giữ của prompt; nêu cụ thể xu hướng không
  được đổi tương ứng. Không chỉ ghi chung “giữ identity” hoặc “không làm đẹp”.
  Mẫu style chỉ cung cấp cách thể hiện, không cung cấp chuẩn mặt/cơ thể lý tưởng.
- Không thêm các từ như “beautiful”, “perfect”, “flawless”, “symmetrical”,
  “ideal proportions” vào prompt chuyển nguồn nếu người dùng không yêu cầu.
  “Tự nhiên”, “thanh tịnh” hoặc “2D” cũng không cho phép sửa cấu trúc nguồn.
  Nét sạch, bỏ texture và giản lược shading là thay cách vẽ, không phải xóa
  hình mí, nét tuổi, độ đầy má hoặc thay hình môi/mũi. Line art không mang
  bóng nguồn; đặc điểm nhận diện biểu đạt bằng màu được giữ cho bảng màu/lượt tô.
- QA đối chiếu các dấu riêng đã chọn, kiểm cả xu hướng lý tưởng hóa cộng dồn:
  mắt lớn hơn, mũi nhỏ hơn, mặt thon/cân xứng hơn, cổ dài hơn hoặc dáng mảnh hơn.
  Ghi điều nhìn thấy, không khẳng định mô hình đã “làm đẹp” chỉ từ cảm giác.
  Sai khác nhỏ còn giữ nhận diện được đánh giá theo mục giữ tỷ lệ; không đòi
  khớp từng pixel, không dùng vẻ đẹp của output để bù lệch identity.
- Đây là biện pháp giảm nguy cơ, không bảo đảm mô hình không tự diễn giải.
  Nếu người dùng yêu cầu làm đẹp/đổi nét riêng rõ, chỉ thay trong phạm vi đó,
  ghi thay đổi và `SKIPPED_BY_USER` theo contract, không mở rộng sang phần khác.

### Negative prompt trước tạo hình

- Áp dụng quy tắc toàn dự án về
  [đưa điều cấm vào prompt từ đầu](../../../AGENTS.md#điều-cấm-phải-có-trong-prompt-từ-đầu).
- Áp dụng ngay từ prompt thiết kế, line art, lên màu, sheet và variant; không
  chờ QA mới chặn chibi hoặc chuyển thiết kế sang mẫu khác. Gộp thành phần
  `Avoid/Negative constraints` trong prompt ImageGen; không giả định công cụ
  có tham số negative prompt riêng. Kết hợp mô tả tích cực về tỷ lệ/identity
  cần giữ với các loại trừ dưới đây, điều chỉnh theo nguồn và brief hiện hành.
- Mặc định không tạo chibi, super-deformed, đầu quá lớn so với thân, mắt búp
  bê quá lớn, mặt trẻ con, thân/tay/chân bị rút ngắn hoặc tỷ lệ đồ chơi. Giữ
  tỷ lệ theo tuổi và nguồn; với nhân vật trẻ em không biến loại trừ này thành
  yêu cầu cơ thể người lớn. Chỉ thay khi người dùng yêu cầu rõ.
- Không tự chuyển sang tạo hình hoạt hình/cổ trang Trung Quốc: không thay
  trang phục nguồn bằng hanfu/cổ áo giao lĩnh, tóc/búi/trâm hoặc phụ kiện cổ
  trang Trung Quốc, không thay identity bằng mẫu mặt có sẵn từ manhua/donghua
  hay ảnh style. Đây là kiểm sự thay thế thiết kế, không coi một kiểu mắt,
  màu da hoặc hình mặt là bằng chứng quốc tịch. Nếu chính nguồn/brief có các
  yếu tố đó thì giữ đúng nguồn, không loại bỏ vì danh sách mặc định.
- Khối gợi ý để tích hợp vào prompt (không thay mô tả nguồn cụ thể):

  ```text
  Avoid: chibi or super-deformed proportions; oversized head relative to the
  body; enlarged doll-like eyes; infantilized facial proportions; shortened
  torso or limbs; toy-like anatomy; beautification or symmetry correction
  that changes source identity. Do not reinterpret this character as a generic
  manhua/donghua character or replace the source costume, hairstyle, jewelry
  or accessories with Chinese historical/fantasy designs. Preserve the actual
  age, facial structure, body proportions and cultural design details supplied
  by the source/brief. These exclusions do not remove features actually present
  in that source or explicitly requested by the user.
  ```

- QA kiểm lại đầu–thân, kích thước mắt, tuổi cảm nhận, chiều dài chi và các
  thay thế cụ thể ở tóc/trang phục/phụ kiện; không chỉ ghi “không chibi” hay
  “không Trung Quốc hóa” mà thiếu bằng chứng. Negative prompt giảm nguy cơ,
  không bảo đảm mô hình tuân thủ; vẫn giữ giới hạn sửa và dung sai tỷ lệ hiện
  hành. Không tự chạy ảnh kiểm chứng khi người dùng chỉ yêu cầu sửa workflow.

### Nét đen cấu trúc trên khuôn mặt

- Áp dụng cho ảnh chuyển style, ảnh màu, sheet và mọi lượt sửa có mặt nhìn
  thấy. Prompt phải chỉ rõ vị trí cần nét đen theo cấu trúc nguồn; không chỉ
  ghi “nét rõ” hoặc dùng bóng màu sẫm thay nét. Với góc khuất hoặc chi tiết
  nguồn không có, không tự thêm nét để đủ danh sách.
- Khi biên soạn prompt thực tế, tách yêu cầu **Mũi** và **Miệng** thành hai
  mục riêng theo vùng nhìn thấy; không rút gọn thành “fine dark linework”.
  Trong `Avoid/Negative constraints` phải có câu cấm dùng bóng nâu/xám,
  đường màu môi hoặc ranh giới mảng màu thay nét mực đen/near-black. Kiểm
  câu này có trong prompt đã gửi, không chỉ trong skill hay record QA.
  “Mềm”, “dịu”, “tiết chế” mô tả độ dày/đầu nét và rìa mảng shading, không
  cho phép làm nhạt màu nét cấu trúc hoặc hòa nét vào bóng da/môi.
- Mắt: nét đen thanh ở bờ mí trên, khóe mắt và lông mi đang có; mí dưới chỉ
  nhấn đoạn cấu trúc theo nguồn, không mặc định viền đen kín mắt. Mày giữ
  hình, độ dày và màu theo identity, không ép mọi lông mày thành khối đen.
- Mũi: nét đen thanh ở lỗ mũi và đoạn ngắn chân/cánh mũi thực sự thấy trong
  nguồn. Không viền đen toàn bộ mũi, kéo nét dọc hai bên sống mũi hoặc làm
  mũi nhỏ/nhọn hơn. Không lấy ranh giới bóng sáng làm đường cấu trúc mới.
- Miệng: đường khép/tiếp giáp hai môi cần nét đen thanh, rõ theo đúng đường
  cong nguồn, nối về hai khóe khi nguồn thể hiện; khóe miệng nhấn ngắn và
  tiết chế, không thành hai mảng đen dày. Không chỉ giữ một đường nâu/xám
  hoặc bóng mềm rồi coi đã có nét đen. Không viền kín cả hai môi, tô môi
  thành đen hoặc thay hình môi/nụ cười. Miệng mở thì theo đúng mép miệng
  đang thấy, không tự thêm đường khép môi xuyên qua khoảng mở.
- Môi dưới: thêm nét đen/near-black thanh, ngắn, thu hai đầu ở đoạn bờ dưới
  thực sự đọc được theo cấu trúc nguồn; có thể ngắt, không nối thành viền
  kín môi. Phân biệt nét này với đường khép môi và bóng đổ dưới môi: không
  dùng bóng nâu thay nét, cũng không đồ toàn bộ mép bóng thành đường đen dài.
  Không tự thêm khi góc nhìn che khuất hoặc nguồn không cho thấy cấu trúc đó.
  Yêu cầu “không viền kín cả hai môi” không có nghĩa bỏ nét chọn lọc môi dưới.
- Tai, hàm/cằm và cổ: giữ nét đường bao và nét cấu trúc chọn lọc theo nguồn,
  phân cấp thanh–đậm với mắt/mũi/miệng; không đồ mọi nếp tuổi, rãnh má hoặc
  ranh giới mảng sáng–tối thành nét đen. Răng khi có theo hướng dẫn riêng
  bên dưới, không viền đen kín từng chiếc.
- Nét đen/near-black phải đọc như nét mực ở kích thước sử dụng, có đầu nét
  thu và độ dày tiết chế, không làm toàn bộ viền mặt đậm cứng. Giữ màu môi,
  màu da và mảng ánh sáng; tăng nét không cho phép đổi vị trí, kích thước,
  hình dạng hay tỷ lệ bộ phận. Màu biểu đạt riêng trong nguồn chỉ đổi khi
  người dùng yêu cầu rõ, ghi phạm vi; không tự thêm makeup.
- QA xem riêng mắt, mũi và miệng: nét có thật sự đen, đủ rõ và đúng vị trí
  không; có thiếu đường khép môi, chỉ đen ở khóe, viền kín hoặc khóe quá dày
  không. Kiểm lại hình/tỷ lệ nguồn và shading sau nhấn nét. Nét đen rõ không
  bù được tỷ lệ sai hoặc khối mặt còn giống render 3D. Ghi đúng phần chưa
  đạt, không gọi bóng màu sẫm là nét đen đã đạt.
- QA ghi kết quả mũi và miệng riêng ở kích thước sử dụng, phóng lớn để xác
  minh khi cần: mũi kiểm lỗ mũi cùng đoạn chân/cánh mũi đang thấy; miệng
  kiểm riêng đoạn giữa đường khép môi, hai khóe và nét bờ dưới môi khi nguồn
  thể hiện; không coi đường khép môi đã đạt là đủ cho nét môi dưới. Chỉ đen ở khóe
  không đủ để đạt toàn miệng; thấy rõ hình môi hoặc màu tối không chứng minh
  đã có nét đen. Nếu chưa đọc thành nét mực ở kích thước sử dụng thì ghi
  chưa đạt phần đó, không lấy nét mắt rõ hoặc tương phản tổng thể để bù.
- Ref trắng đen v002 mới là bản xem trước về nhấn nét, chưa được người dùng
  chọn thay ref chung; không tự cập nhật reference style chỉ vì đã sửa skill.

Khối gợi ý tích hợp theo góc nhìn và phần thực sự xuất hiện:

```text
Eyes: fine black or near-black tapered structural ink at the visible upper
eyelids and eye corners, following the source.
Nose: distinct fine black or near-black ink at the visible nostril apertures
and short alar/nose-base edges actually shown in the source. These must read
as ink strokes at the intended viewing size, separate from colored shading.
Mouth: a fine black or near-black actual lip-separation line, including its
central segment and its connection toward the corners where the source shows
them; restrained short corner accents alone are insufficient. For an open
mouth, follow its visible edges without adding a closed-lip seam across it.
Lower lip: where the source reveals its lower structural edge, use a short,
fine black/near-black tapered stroke, optionally broken, distinct from the
lip-separation line. Do not enclose the lip or trace the entire cast shadow.
Keep source feature shapes, positions and proportions. Softness means tapered
delicate strokes and locally soft shading edges, not faded structural ink.
Avoid/Negative constraints: do not substitute brown/gray shading, lip-colored
lines or color-patch boundaries for the required black/near-black ink. Do not
encircle the whole nose or both lips, thicken corners into black wedges, trace
every wrinkle or light/shadow boundary, or add lines on hidden features.
Preserve source anatomy and all relative proportions.
```

### Sắc vùng mắt theo identity gốc

Người dùng xác nhận ngày 2026-10-21 từ thử nghiệm Nhân vật nữ test: giữ chuyển
sắc quanh mắt theo ảnh gốc để không làm mất dấu riêng khi chuyển sang 2D.
Áp dụng khi thiết kế nhân vật Ấn Độ có nguồn tương ứng; không suy rằng mọi
người Ấn Độ đều có cùng màu hoặc mức đậm quanh mắt, không tự thêm nếu nguồn
không thể hiện. Không dùng đặc điểm này để kết luận nguồn gốc từ ảnh.

- Đọc quan hệ màu cả vùng: mí/hốc mắt, da ngay trên mí tới dưới mày, khóe mắt,
  sát mí dưới và phần chuyển về má. Không chỉ lấy màu tối ở một dải dưới mắt.
- Giữ sắc đậm riêng có trong nguồn, nhưng nối màu hợp lý với da trên mí và
  vùng xung quanh; tránh dải sáng khác hẳn ngay trên mí tối hoặc quầng dưới
  mắt tách biệt gây cảm giác thâm, mệt mỏi hay bầm mắt ngoài nguồn.
- Khi dùng bảng màu cô lập, bổ sung màu chuyển tiếp và vị trí dùng, phân biệt
  da quanh mắt với tròng mắt/lông mi. Màu tối nhất chỉ dùng đúng phạm vi nguồn;
  không phủ toàn hốc mắt hoặc tự diễn giải thành smoky makeup.
- Thể hiện bằng nét/mảng 2D với độ mềm cục bộ tiết chế; giữ biến thiên sắc
  không đồng nghĩa sao chép tạo khối ảnh thật. QA so cả vùng mắt với nguồn,
  kiểm mất sắc riêng, tăng độ đậm quá mức và sai quan hệ trên–dưới mí.
- Giữ quan hệ sắc bằng các mảng màu riêng có hình dạng rõ; “giữ chuyển sắc”
  không cho phép blend rộng từ hốc mắt sang má hoặc làm mượt toàn mặt.
  Độ mềm trên da theo giới hạn trong policy chung bên dưới.

### Giới hạn độ mềm trên da

- Áp dụng [giới hạn da của policy chung](../../../docs/project-style-policy.md#giới-hạn-độ-mềm-trên-da)
  cho prompt và QA: mảng sáng–trung–tối liền, đọc rõ hình dạng; chỉ dịu mép
  hẹp, không chuyển mượt lan rộng ôm khối má–mũi–cằm–cổ. Giữ cấu trúc và
  sắc riêng theo nguồn, không làm da lì một màu hoặc tăng tương phản gắt.
- Prompt thực tế phải có giới hạn riêng cho da, không chỉ “soft 2D” hoặc
  lệnh cấm 3D chung. Khối gợi ý:

  ```text
  Skin: use coherent light/midtone/shadow color shapes with clean, continuous
  interiors and readable boundaries. Allow only a narrow local softening at
  selected edges, preserving each shape. Keep source anatomy and regional
  skin colors, including eye-area colors, through designed color shapes.
  Avoid/Negative constraints: no broad blended transitions wrapping around
  cheeks, nose, chin or neck; no airbrushed or spherical skin shading, diffuse
  glow patches or continuous volumetric ramps. Do not flatten all skin to one
  color, sharpen every edge, deepen shadows or redesign anatomy to compensate.
  ```
- QA da ở kích thước sử dụng và phóng lớn khi cần: kiểm riêng má, mũi, cằm,
  cổ và quanh mắt; mảng có còn đọc rõ hay hòa thành khối mượt. Chuyển sắc
  rộng tạo cảm giác 3D là chưa đạt dù nét đen rõ. Không dùng kết quả nét môi
  hoặc vải để bù lỗi da; không tự nâng ảnh minh họa mới thành ref style chung.

## Trang phục nữ kín đáo

Quy tắc thiết kế project do người dùng xác nhận ngày 2026-10-21, áp dụng
cho mọi nhân vật nữ trong Character Studio, gồm chân dung, sheet, bản thử
và variant; không phải khẳng định về mọi trang phục lịch sử.

- Trang phục phải che kín bụng và eo ở mọi góc nhìn và tư thế. Với sari,
  áo trong và lớp vải quấn phải phủ/chồng liên tục, không có dải da hở giữa
  gấu áo và cạp hoặc mép sari ở chính diện, 3/4, nghiêng hay sau lưng.
- Không tự diễn giải sari thành áo crop top hoặc kiểu quấn hở bụng/eo
  gợi cảm hiện đại. Giữ màu, nhận diện và thiết kế nguồn; nếu ref hoặc output
  trước có khoảng hở, điều chỉnh độ phủ của áo/vải để khép kín khoảng đó,
  không sao chép lỗi hoặc tự đổi bảng màu để xử lý.
- Prompt phải nêu rõ áo che kín bụng/eo và các lớp vải chồng liên tục ở mọi
  góc; không chỉ ghi chung “kín đáo” hoặc “modest”. Khi dựng góc mới, kiểm
  lại độ phủ thay vì suy từ góc chính diện đã kín.
- QA kiểm riêng vùng dưới ngực–bụng–eo và mép áo/sari ở từng hình, đặc biệt
  góc nghiêng và phía sau. Một khoảng da hở ở bụng/eo là chưa đạt, dù mặt,
  màu và các góc còn lại đúng; không khóa bản đó thành profile chuẩn.

## Chuyển style và mức chi tiết

- Khi ảnh có trang sức, bắt buộc xem và truyền kèm
  [bảng trang sức v003](../comic-image-production/references/style-st03/jewelry-board-v003.png)
  trong mỗi lượt tạo/chỉnh theo [policy chung](../../../docs/project-style-policy.md#vật-liệu-và-giới-hạn-rendering).
  Áp dụng cả chuyển style, sheet, bản thử, variant và sửa lỗi; không chỉ mô
  tả bằng chữ. Phân vai ref vật liệu giảm bóng, giữ thiết kế/màu theo nguồn;
  ghi input thực tế và kiểm nhiễm thiết kế từ bảng. Không tự tạo ảnh chỉ vì
  đang cập nhật quy tắc này.

- **Vải phẳng, sạch:** áp dụng cho chuyển style, ảnh màu, sheet và lượt sửa
  có trang phục. Giữ silhouette, cách quấn, mép chồng, nếp gấp chính và màu
  theo nguồn; diễn bề mặt bằng mảng màu rộng, liền và ít chia vụn. Bóng theo
  nếp chính, chênh sắc vừa, rìa mềm tiết chế theo st03; không làm từng nếp
  nhỏ thành khối nổi hoặc phủ các vệt sáng–tối li ti lên toàn mặt vải.
- Phân biệt **hoa văn thiết kế** với **texture vật liệu** trước viết prompt:
  giữ hình, vị trí và nhịp lặp của viền/motif nhận diện đọc được; bỏ vân dệt,
  sợi vải, lưới nhỏ, hatching, nét xước, hạt và vệt loang mô phỏng bề mặt.
  Không hiểu “giữ nguyên chi tiết” là sao chép hoặc tăng rõ mọi vân vật liệu.
  Hoa văn thân vải thực sự có trong nguồn được diễn bằng nét/mảng 2D tiết chế,
  không tăng mật độ hay độ tương phản để lấp vùng trống. Chi tiết không đọc
  rõ thì ghi giới hạn, không đoán motif, biến vân dệt thành họa tiết mới hoặc
  xóa viền nhận diện để làm phẳng vải.
- Prompt thực tế phải nêu riêng phần giữ và phần bỏ ở vải; đưa các texture
  bị loại vào `Avoid/Negative constraints` ngay từ đầu. Khối gợi ý, điều chỉnh
  theo trang phục đang có:

  ```text
  Fabric: preserve the source garment silhouette, wrap, overlaps, main folds,
  colors and readable identifying border/motif shapes and spacing. Use broad,
  clean, uninterrupted 2D color areas and restrained designed shadow shapes
  following the main folds, with moderate contrast and locally soft edges.
  Avoid/Negative constraints: no woven microtexture, visible threads, fine
  crosshatch/grid, grain, scratches, mottling, dense tiny crease lines or
  fragmented highlight/shadow streaks across the fabric. Do not turn weave
  texture into invented motifs, amplify faint patterns, add decoration, or
  erase/change identifying borders and motifs to obtain a flatter surface.
  ```
- QA vải ở toàn hình/kích thước sheet và vùng phóng lớn: bề mặt đọc thành
  mảng sạch, nếp chính và lớp quấn còn rõ; không có vân dày, lưới sợi hoặc
  mảng vụn làm nhiễu. Kiểm riêng viền/motif với nguồn để phát hiện mất/đổi/thêm
  hoa văn. Phẳng hơn không có nghĩa xóa toàn bộ bóng, nếp hoặc thiết kế;
  giảm texture không cho phép thay tỷ lệ cơ thể hay các vùng khác.
- Trước lượt tạo đầu, tách thiết kế cần giữ khỏi cách thể hiện cần chuyển:
  identity, silhouette, cấu trúc trang phục/trang sức theo nguồn; nét, màu,
  shading và mức nhấn theo policy. Không chờ output lệch rồi mới bổ sung
  yêu cầu vật liệu vào prompt.
- Trang sức phải phục vụ nhận diện và địa vị nhưng không tranh trọng tâm với
  mặt. Giữ hình chính, vị trí và dấu riêng theo nguồn; không tự tăng mật độ
  hạt, viền, nét khắc hay hoa văn để diễn đạt “giàu có”, “tinh xảo” hoặc “2D”.
  Chi tiết nhỏ cần đọc ở kích thước sheet, không chỉ khi phóng lớn.
- Khi giảm cảm giác render, đổi cách chia sáng/tối trên cùng thiết kế.
  Không thay bóng sáng bằng họa tiết trang trí, thêm hình lá/hoa, hoặc hiểu
  “giữ chi tiết” là phải viền/vẽ rõ mọi hạt. Cũng không xóa dấu riêng hay
  làm toàn ảnh phẳng và nhạt. Nếu cần giảm chính thiết kế trang sức đã khóa,
  nêu đó là thay đổi thiết kế, không âm thầm gọi là chỉnh style.
- Prompt nêu cụ thể phần giữ, phần đổi và mức chi tiết theo vùng đang có;
  tránh các yêu cầu chung như “rich details”, “intricate” khiến mô hình
  tự trang trí thêm. QA so cả độ bóng lẫn mật độ chi tiết với nguồn và
  hierarchy mặt–phụ kiện; sửa được style nhưng thêm hoa văn vẫn là regression.
- Khi người dùng đang cải thiện skill/workflow, ưu tiên sửa hướng dẫn tái sử
  dụng từ lỗi quan sát được. Không tự chuyển trao đổi phương pháp thành chuỗi
  chỉnh ảnh riêng lẻ. Chỉ chạy ảnh kiểm chứng khi được yêu cầu; giữ input và
  biến thử rõ, không lấy một ảnh đẹp làm bằng chứng skill đã ổn định.
- Sau mỗi lần kiểm thử hoặc phân tích lỗi workflow, đưa đề xuất hành động
  tiếp theo: sửa gì trong skill/đầu vào, kiểm chứng bằng cách nào và tiêu chí
  đạt. Nêu hướng ưu tiên cùng lý do; nếu có 2–3 phương án thực tế thì đánh số,
  ghi đánh đổi ngắn. Không dừng ở chẩn đoán hoặc để người dùng tự suy bước sau;
  phân biệt đề xuất với việc đã thực hiện, không tự coi đề xuất là phê duyệt.

## Bố cục sheet tổng hợp mặc định

- Một ảnh tổng hợp ngang trên nền trắng.
- Vùng trái khoảng 35–40% ngang: một chân dung chính diện từ ngực lên thật
  lớn, thông tin cơ bản bên dưới. Vùng phải khoảng 60–65%: bốn góc đứng
  một hàng, gồm chính diện, 3/4, nghiêng và sau lưng.
- Điều chỉnh hai vùng theo silhouette và độ dài chữ. Giữ khoảng cách rõ;
  tránh chỗ trống lớn trong khi vùng khác chen chúc.
- Chân dung thấy trọn đầu, tóc hoặc khăn, vai và ngực; đủ lớn để nhận diện mặt.
- Các góc đứng cùng tỷ lệ, đường chân và chiều cao tương ứng; thấy trọn đầu/chân.
- Thông tin gồm tên, tuổi, giới tính, chiều cao, vai trò và xuất thân theo
  brief/nguồn; chỉ in trường có dữ kiện, không tự thêm tuổi, chiều cao,
  quê quán, tầng lớp hoặc tiểu sử.
- Không mặc định thêm biểu cảm, bảng màu, đạo cụ hoặc ô chi tiết.
- Khi brief có chiều cao, mặc định in trường `Chiều cao` trong phần thông tin
  trên ảnh profile/sheet, ví dụ `Chiều cao: 1,65 m`; giữ đúng giá trị người
  dùng cung cấp và đồng bộ với brief hiện hành. Nếu chưa có thì bỏ trường,
  không suy từ hình hoặc tự đặt số. Không thêm thước đo/vạch chiều cao nếu
  chưa được yêu cầu. Người dùng yêu cầu ẩn chiều cao thì giữ nội bộ và không in.
- Giữ bố cục đã chốt. Việc nhắc lại danh sách thành phần không tự là yêu cầu
  đổi bố cục; chỉ đổi khi người dùng yêu cầu rõ.

## Tỷ lệ và anatomy

- Dựng mặt/cơ thể theo tuổi, chiều cao, thể trạng; số đầu chỉ là mốc kiểm,
  không là chuẩn đẹp bắt buộc.
- Không bóp chân, phóng đầu hoặc kéo giãn hình để vừa bố cục; điều chỉnh
  bố cục hoặc thu nhỏ đồng đều khi thiếu chỗ.
- Mắt, mí, mũi, môi, hàm, cằm có cấu trúc rõ bằng nét/mảng 2D; giữ dấu tuổi
  vừa đủ, không trẻ hóa hay làm khắc khổ ngoài brief.
- Tư thế có trọng lượng/điểm tựa tự nhiên; vai, khuỷu, cổ tay, khung chậu,
  đầu gối và bàn chân liên kết hợp lý.
- Giữ hộp sọ, độ nhô mũi, hàm, thể trạng và chiều dài các phần qua mọi góc.
- Không kết luận tỷ lệ tự nhiên chỉ vì hình không phải chibi.

## Quy chuẩn tỳ-kheo

Đây là lựa chọn thiết kế project, không khẳng định mọi y phục lịch sử giống nhau.

### Đầu và diện mạo

- Đầu cạo sạch hoàn toàn ở mọi góc, cả thái dương/gáy; không chân tóc,
  chấm nang tóc, tóc lún phún hoặc mảng xám/xanh mô phỏng tóc mới cạo.
  Giữ lông mày theo identity.
- Râu/ria theo brief/profile, không tự thêm. Tuổi/thần thái theo từng người,
  không dùng chung mặt thanh niên lý tưởng hóa cho mọi vị.

### Màu y

- Nâu đỏ đất trầm, đỏ gạch pha nâu; midtone tham khảo khoảng `#8F4933`,
  không khóa mọi vùng sáng/tối vào một mã.
- Không tự đổi sang nâu vàng/ochre, cam tươi hay đỏ rực; giữ sắc nhất quán
  qua các góc dưới ánh sáng trung tính.
- Reference mới về cách quấn không tự thay màu đã chốt.

### Cấu trúc y quấn

- Y phủ cả hai vai/ngực trên; không trần một vai hoặc khoét sâu nếu chưa yêu cầu.
- Vải mềm ở chân cổ, vắt chéo ngực, gom về vai; mép gấp/tà buông theo trọng lực.
- Quanh tay đọc là vải quấn/mép chồng mở, không ống tay may, cổ tay bo hay tay chuông.
- Cẳng tay có thể lộ theo cách quấn/tư thế; không mặc định phủ tới cổ tay.
- Tránh cổ áo tròn may, cổ đứng hoặc khối khăn cowl dày quanh cổ.
- Lớp vải liên tục hợp lý trước/bên/sau; không sao chép họa tiết nếp lên từng góc.
- Chuyển ref ngồi sang đứng phải dựng lại nếp theo trọng lực/tay/chân,
  không bê nguyên nếp đầu gối/lòng đùi.
- Chọn reference cách quấn cụ thể khi cần; không coi output thử chưa chọn là chuẩn.
- Mẫu quấn y chung do người dùng chọn ngày 2026-10-19:
  [ảnh mẫu v001](assets/y-quan-chuan-v001.png). Xem ảnh trước khi tạo/chỉnh
  tỳ-kheo và dùng làm reference cấu trúc y khi công cụ/yêu cầu cho phép.
- Theo mẫu: y phủ hai vai/ngực, nếp mềm quanh chân cổ và rủ qua ngực;
  mép vải ngoài gấp dọc từ vai, tà trên buông quanh hông, lớp dưới dài gần
  cổ chân có nếp dọc. Vải quanh tay phủ mềm theo cánh tay, bàn tay ra khỏi
  mép vải mở; không diễn giải thành ống tay may hoặc cổ tay bo. Đối chiếu
  đồng thời chính diện, 3/4, nghiêng và sau lưng trong mẫu.
- Mẫu này chỉ khóa cách quấn và quan hệ các lớp vải; không sao chép mặt,
  tuổi, tai, màu da, thể trạng hoặc chữ của Gavampati sang nhân vật khác.
  Màu y tiếp tục theo mục Màu y; style theo policy st03 hiện hành.
- Đây là mẫu thiết kế được chọn, không phải bằng chứng y phục lịch sử hoặc
  phê duyệt toàn bộ profile Gavampati. Không tự chuyển ảnh vào profiles.
  Nguồn: ảnh người dùng đính kèm trực tiếp; lưu bản gốc không chỉnh sửa.
- Khi không được dùng ảnh ref, chuyển cấu trúc trên thành mô tả chữ;
  không truyền ảnh mẫu trái yêu cầu. Reference mới hơn được người dùng
  chỉ định rõ vẫn ưu tiên theo phạm vi yêu cầu.

## Sử dụng reference và chỉnh sửa

### Workflow mặc định: chuyển trực tiếp ảnh gốc sang style dự án

Người dùng cập nhật ngày 2026-10-22: luồng này thay mặc định nét → bảng màu
→ lên màu ngày 2026-10-21; giữ nhánh cũ chỉ để dùng khi được yêu cầu rõ.

- Đọc brief và xem ảnh gốc → chuyển chính ảnh đó sang st03 hiện hành → QA
  đối chiếu trực tiếp nguồn → trình ảnh, chờ người dùng duyệt → tạo sheet.
  Không tạo nét chì/line art, bảng màu hoặc lượt lên màu tách riêng ở giữa.
- Truyền ảnh gốc làm reference identity/thiết kế/màu/cấu trúc; dùng reference
  style hiện hành theo policy và định nghĩa st03. Style ref chỉ cung cấp cách
  diễn nét/mảng, không cung cấp khuôn mặt, trang phục, màu hoặc bố cục.
  Không mặc định truyền hai user style cũ của nhánh tô màu vào luồng này.
- Giữ nguyên chi tiết quan sát được: mặt, tuổi, thể trạng, tỷ lệ, tóc/râu,
  trang phục, hoa văn, trang sức/phụ kiện, màu và vị trí vật liệu; giữ pose,
  biểu cảm, góc nhìn, crop và bố cục nguồn. Chỉ chuyển cách diễn nét, mảng
  sáng–trung–tối và bề mặt sang style dự án. Không tự thêm/bớt, thay thiết kế,
  làm đẹp, sửa trang phục hoặc đổi pose để chuẩn bị cho sheet.
- Với vải, “giữ nguyên chi tiết” giữ thiết kế nhận diện, không giữ texture
  vật liệu; áp dụng mục **Vải phẳng, sạch** ở trên trong prompt và QA.
- Prompt và record phải tách `Giữ nguyên theo nguồn`, `Chỉ đổi cách thể hiện`
  và `Avoid/Negative constraints`, nêu dấu riêng cụ thể và điều cấm tương ứng.
  Chi tiết không đọc rõ thì ghi giới hạn, không đoán hoặc thêm motif để bù.
- Với yêu cầu giữ nguyên chi tiết ở luồng này, ghi `SKIPPED_BY_USER` đúng phạm
  vi nếu quy chuẩn thiết kế mặc định về trang phục nữ hoặc y tỳ-kheo đòi đổi
  thiết kế đang có trong nguồn; không âm thầm sửa nguồn theo quy chuẩn đó.
  Style policy vẫn áp dụng. Thay đổi thiết kế khác chỉ làm khi người dùng
  yêu cầu rõ, ghi phạm vi và provenance, không mở rộng sang phần khác.
- QA kiểm đồng thời identity, hình học, chi tiết/màu và style trên toàn ảnh;
  áp dụng dung sai tỷ lệ và giới hạn tự sửa hiện hành. Không lấy nét 2D sạch
  làm lý do bỏ chi tiết nguồn. Nếu chưa đạt, báo lỗi cụ thể, không coi ảnh
  sẵn sàng dựng sheet; nếu đạt, vẫn chờ người dùng duyệt version hiện hành.
- Khi dựng sheet sau duyệt, dùng ảnh chuyển style được chọn cùng nguồn gốc
  đúng vai trò; bố cục/góc đứng theo mục sheet. Không đổi thiết kế đã duyệt;
  phần khuất chưa có dữ kiện phải ghi là suy dựng, không giả là chi tiết nguồn.

### Nhánh tùy chọn: nét chì/line art và bảng màu, lên màu

Chỉ đọc và thực hiện các hướng dẫn chuyên biệt dưới đây khi người dùng yêu
cầu rõ nhánh tương ứng. Các từ “mặc định” về input bên dưới chỉ áp dụng trong
nhánh tô màu này, không thay workflow chuyển style trực tiếp. Yêu cầu chuyển
style, chỉnh style hoặc QA chưa đạt không tự kích hoạt nhánh nét/màu.


#### Khi người dùng chỉ định màu da trước khi lên màu

- Nếu người dùng đưa màu da mong muốn bằng mã màu, ảnh mẫu hoặc mô tả trước
  lượt tô, lập bảng màu theo vùng và trình người dùng xem trước; không tạo
  chân dung màu trong cùng lượt khi bảng chưa được chốt. Nếu màu da đã chốt
  từ trước và còn hiệu lực thì tái sử dụng, không hỏi duyệt lại.
- Ghi màu da người dùng chọn là yêu cầu thiết kế ưu tiên hơn màu da ảnh gốc;
  cập nhật brief revision/activeBrief và provenance. Nếu thay màu da nguồn,
  ghi `SKIPPED_BY_USER` đúng phạm vi màu da, không mở quyền đổi identity,
  thể trạng, trang phục hoặc màu các vật liệu khác. Ref màu da chỉ cung cấp
  màu, không cung cấp mặt, cấu trúc cơ thể, shading hay texture.
- Trình bảng ô màu có nhãn vị trí dùng, gồm màu da nền và các sắc chuyển tiếp
  cần thiết cho vùng thực sự có: má, môi, mí–trên mí–dưới mày và dưới mắt–má;
  phân biệt màu người dùng cung cấp với màu agent đề xuất/ước lượng. Giữ quan
  hệ sắc quanh mắt theo nguồn khi có, điều chỉnh hài hòa với màu da mới,
  không sao chép hình học bóng từ ảnh mẫu. Đặt màu tóc, vải, phụ kiện liên quan
  cạnh nhóm da để người dùng đánh giá quan hệ màu; không tự đổi chúng.
- Bảng là các ô màu để xem trước, không phải tô phẳng toàn nhân vật và không
  thay bước kiểm nét. Nêu đây là đề xuất màu quan sát dưới ánh sáng trung tính,
  không cam kết một mã màu giữ nguyên ở mọi vùng sáng/tối của ảnh cuối.
- Sau khi trình bảng, khuyến nghị chốt để lên màu hoặc chỉnh vùng màu cụ thể;
  mỗi câu chọn trong block riêng. Chỉ lên màu khi người dùng chốt rõ bảng
  version hiện hành và line art đủ điều kiện. Yêu cầu chỉnh bảng chưa phải
  duyệt tô; tạo version bảng mới và trình lại nếu thay màu chưa được chốt.

Phương pháp nhánh màu được chốt ngày 2026-10-21, thay phương pháp tạm truyền
ảnh gốc vào lượt tô riêng. Đây là lựa chọn workflow, không miễn QA hoặc xác nhận phương pháp
đã ổn định trên mọi nhân vật. Policy st03 vẫn có hiệu lực.

- Khi người dùng yêu cầu trọn nhánh nét và màu: đọc brief và ảnh gốc → tạo/kiểm chân dung
  line art sạch → lập/kiểm bảng màu theo vùng → tô mới bằng line art + bảng
  màu + hai user style → QA đối chiếu ảnh gốc → người dùng chọn chân dung
  màu → dựng sheet theo contract. Bảng màu là các ô màu có nhãn, không phải
  bản tô phẳng toàn nhân vật; không bắt thêm bước tô phẳng toàn hình.
- Ảnh gốc: chuẩn identity, màu, vị trí vật liệu, trang phục và thiết kế; đọc
  trước mỗi lượt và dùng kiểm line art/bảng màu/output. Mặc định không truyền
  toàn ảnh, crop ảnh thật hoặc output màu cũ vào lượt tô mới để hạn chế ảnh
  hưởng rendering. Không thay chuẩn identity bằng line art hoặc mẫu style.
- Input line art sạch đã kiểm: chuẩn cấu trúc và bố cục đã chọn,
  không phải chuẩn tô phẳng hoặc giới hạn tối đa chi tiết. Chi tiết có giá trị
  bị lược cần đối chiếu ảnh gốc, không tự thêm motif để bù.
- Input bảng màu đã kiểm: chỉ gồm vùng/vật liệu thực sự có trong nhân vật;
  gắn mỗi ô với vị trí dùng và nguồn. Giữ biến thiên sắc da, môi, quanh mắt,
  tóc, vải và phụ kiện cần cho nhận diện; không ép mọi nhân vật về cùng bảng.
  Nếu lấy mẫu pixel, ghi tọa độ/vùng, phương pháp và màu; tránh điểm bóng,
  cháy sáng, bóng quá sâu hoặc viền đen làm màu nền. Màu quan sát chịu ánh sáng
  nguồn, không tự coi là albedo. Phần không lấy mẫu được phải ghi là ước lượng.
- Kiểm cả quan hệ màu và gán vùng trước khi tô: sắc má, môi, mí–trên mí–dưới
  mày và dưới mắt–má khi xuất hiện; phân biệt da/vải, vàng/đá/ngọc. Bảng màu
  cung cấp sắc và chuyển tiếp, không cung cấp hình học bóng hay thay cấu trúc
  nét. Không đạt thì sửa bảng/mô tả vùng trước, không lấy prompt làm bằng chứng.
- Reference style — xem và truyền đồng thời cả hai mẫu người dùng chọn:
  [user style 01](assets/style-user-v001.png) và
  [user style 02](assets/style-user-v002.png), trừ khi user chỉ định input khác.
  Người dùng xác nhận bổ sung mẫu 02 và dùng cả hai ngày 2026-10-21, không thay
  mẫu 01. Input tô mới mặc định là line art, bảng màu và cả hai mẫu style;
  ghi rõ từng file và vai trò, không cố định workflow vào tên “ba reference”.
  Lấy nét có chủ ý, mảng cel-shadow rõ,
  độ mềm cục bộ, cách chia cụm tóc/nếp vải và mức nhấn vật liệu; không lấy mặt,
  màu da, tuổi, tóc/râu, trang phục, trang sức hoặc góc nhìn của nhân vật mẫu.
  Nét/mảng và chi tiết vẫn rõ, không tô phẳng tuyệt đối hoặc đánh bóng từng hạt.
- Bản mẫu là bản sao nguyên ảnh người dùng chỉ định, nguồn gốc
  `studios/character/outputs/punna-vaddhana/references/style-user-v001.png`.
  Đây là asset style dùng chung của studio được người dùng cho phép cho các
  profile tiếp theo; không phải profile identity hay output Punna được duyệt.
- Người dùng xác nhận ngày 2026-10-21: cách tô tóc theo mẫu
  `assets/style-user-v001.png` (user style 01) là hướng chuẩn. Lấy quan hệ
  khối đen chính–mảng charcoal trong cụm, nét cấu trúc có chủ ý và độ mềm
  tiết chế của mẫu; giữ kiểu tóc, độ dài, silhouette và màu riêng theo identity.
  Không thay mảng tô bằng nhiều dải sáng mảnh chạy đều từng lọn hoặc bóng từng
  sợi. Không sao chép kiểu tóc/identity nhân vật nam trong mẫu; tóc màu khác
  không bị ép thành đen. Việc chọn cách tô tóc không duyệt toàn ảnh thử.
- User style 02 là bản sao nguyên ảnh
  `studios/character/outputs/nhan-vat-nu-test/portrait-color-v014.png`.
  Lấy phối sắc vùng mặt, chuyển sắc quanh mắt liền trên mí–dưới mày và dịu về
  má, môi đỏ khi phù hợp nguồn, cùng ngôn ngữ nét/mảng 2D. User style 01 tiếp
  tục ưu tiên cho cách tô tóc. Hai mẫu bổ trợ, không tự trộn mặt, màu da, tuổi,
  giới tính, kiểu tóc, bindi, trang phục hoặc trang sức vào nhân vật mới;
  không áp vùng mắt đậm hay môi đỏ cho nguồn không có đặc điểm đó.
- Prompt phân vai từng mẫu; QA kiểm nhiễm chéo từ cả hai. Chọn làm style không
  xác nhận mọi chi tiết mẫu là chuẩn: không kế thừa lệch identity, motif/khuyên,
  nét răng còn thiếu hoặc ám màu ngoài policy. Nguồn/phạm vi tại
  [record mẫu 02](assets/style-user-v002.md). Không tự lưu mẫu thành profile.
- Prompt khai báo rõ các vai trò và gán màu/vật liệu theo vị trí. QA đối chiếu
  identity/thiết kế với ảnh gốc, style với mẫu và policy, cấu trúc với line art.
  Kiểm cả lẫn mặt/râu/da/costume từ mẫu, màu da hở, vàng–đá–ngọc, mất nét,
  quá phẳng, bóng cầu và tăng mật độ trang trí. Báo giới hạn thay vì tự sửa vô hạn.
- Nhân vật mới chỉ có brief thì thiết kế identity từ brief; không mượn mặt của
  mẫu style và không bắt có ảnh gốc trước. Sau khi có thiết kế được chọn, dùng
  nó đúng vai trò reference nhân vật, giữ provenance theo contract. Bảng màu
  theo thiết kế đã chọn phải ghi phần tự thiết kế, không giả là trích ảnh gốc.

### Chuẩn line art và chẩn đoán trong nhánh tùy chọn

#### Tách chi tiết thiết kế khỏi shading trước tạo nét

- Ảnh gốc quyết định nét mặt, tỷ lệ, đường bao, trang phục, hoa văn, phụ kiện,
  pose và crop. Brief chỉ bổ sung dữ kiện hoặc thay đổi người dùng yêu cầu rõ.
  Mô tả do agent suy từ ảnh phải ghi là quan sát, không dùng làm lệnh sửa hình.
- Prompt yêu cầu chuyển chính ảnh nguồn thành nét, không dựng lại nhân vật
  từ mô tả. Không viết lại công thức khuôn mặt, đổi crop/pose, chỉnh dáng hoặc
  giản lược thiết kế nếu chưa được yêu cầu. Mẫu nét chỉ hướng dẫn cách đi nét,
  không thay hình học hay thiết kế nguồn. Ngoại lệ đã chốt chỉ áp đúng phạm vi.
- Trước tạo line art từ nguồn, ghi theo các vùng thực sự xuất hiện hai nhóm
  trong prompt và record: `Giữ thiết kế` và `Bỏ cách render`. Không chỉ dùng
  yêu cầu chung “clean”, “simple” hoặc “ít chi tiết”.
- `Giữ thiết kế`: cấu trúc mặt và nét nhận diện, silhouette/cụm tóc, nếp vải
  chính, hình/vị trí/mật độ motif, họa tiết viền và cấu trúc phụ kiện theo nguồn.
  Nêu riêng những dấu dễ mất, như viền sari hoặc tầng/hạt khuyên, khi có.
  Không tự giản lược, xóa, thay hoặc thêm chi tiết thiết kế để làm nét sạch.
  Chi tiết nguồn không đọc rõ thì ghi giới hạn, không tự đoán hoặc bù motif.
- `Bỏ cách render`: bóng xám, gradient, hatching, vân da/môi, phản chiếu và
  đường bao chỉ do ranh giới sáng–tối. Da, môi và vải giữ trắng bên trong;
  đường mí, mũi, môi và nếp vải có giá trị cấu trúc vẫn giữ. Tóc/mày có thể
  dùng khối đen phẳng màu bản thân, không dùng dải sáng mảnh để mô phỏng bóng sợi.
- Làm sạch nét không đồng nghĩa làm nghèo thiết kế. Kiểm riêng hai kết quả:
  vân xám/shading còn sót và chi tiết nguồn bị mất/đổi/thêm. Không tăng tương
  phản hoặc threshold toàn ảnh mặc định để chữa xám vì có thể mất nét mảnh,
  dính phụ kiện; nếu xử lý pixel phải kiểm lại cả hai nhóm. Không tính viền
  anti-alias hẹp của nét là bóng xám nếu không có mảng/vân shading thực sự.

#### Ảnh mẫu line art

- Có thể dùng một mẫu line art sạch được người dùng chọn để cụ thể hóa cách
  đi nét. Mẫu cần nền/vùng tô trắng, nét cấu trúc rõ, không vân xám/hatching;
  ưu tiên có mặt, tóc, vải và phụ kiện để thấy cách giữ chi tiết mà không render.
  Mẫu chỉ có mặt không cung cấp bằng chứng cho cách vẽ vải hoặc trang sức.
- Khi có mẫu được chọn, xem ảnh và truyền cùng nguồn vào lượt nét nếu công cụ
  hỗ trợ. Phân vai rõ: ảnh gốc quyết định identity, tỷ lệ, pose, bố cục và
  thiết kế; mẫu nét chỉ cung cấp độ dày/phân cấp nét, cách gom cụm và diễn đạt
  chi tiết. Không lấy mặt, dáng, tóc, costume, motif, phụ kiện hoặc bố cục mẫu.
  Prompt phải nêu cả phần được lấy và cấm lẫn thiết kế; QA kiểm nhiễm chéo.
- Lưu mẫu nguyên bản có version trong `assets/`, kèm record nguồn, lựa chọn
  của người dùng, phạm vi được lấy và lỗi/giới hạn nếu có. Không tự nâng output
  được chấp nhận về tỷ lệ thành mẫu nét sạch hoặc profile chuẩn.
- Mẫu nét hiện hành do người dùng chọn ngày 2026-10-21:
  [line art user v001](assets/line-art-user-v001.png), bản sao nguyên ảnh
  `studios/character/outputs/nu-an-do-test-2/portrait-line-v004.png`.
  Xem và dùng mẫu này cho lượt chuyển nguồn thành line art khi công cụ hỗ trợ,
  trừ khi người dùng chỉ định input khác; phân vai như trên. Lấy nền/vùng tô
  trắng, môi không vân xám, nét cấu trúc và cách giữ viền/hoa văn/phụ kiện.
  Không lấy nhiều đường sáng mảnh ở tóc, tỷ lệ đã lệch nguồn hoặc motif cụ
  thể của mẫu. Hai `style-user` tiếp tục phục vụ tô màu, không thay mẫu nét.
  Lựa chọn mẫu không duyệt profile toàn ảnh; phạm vi và giới hạn tại
  [record mẫu nét](assets/line-art-user-v001.md). Không tự tạo mẫu hoặc thêm
  lượt test khi chỉ đang sửa skill.
- Khi người dùng yêu cầu kiểm chứng lợi ích của mẫu, giữ nguồn/pose/crop và
  prompt nền ổn định, chỉ thay input mẫu nét và phần phân vai tương ứng;
  kiểm đồng thời độ sạch, chi tiết, tỷ lệ và lẫn identity. Một ảnh đẹp hơn
  không đủ để kết luận workflow đã ổn định.

#### Giữ tỷ lệ khi chuyển từ ảnh gốc

- Mặc định đây là chuyển cách thể hiện, không phải thiết kế lại hoặc làm đẹp.
  Giữ tỷ lệ canvas, crop, góc nhìn, biểu cảm, tư thế và phần cơ thể đang thấy
  trong nguồn. Không tự bỏ tay khoanh, dựng lại vai/ngực, làm thẳng người hoặc
  đổi sang chân dung chính diện chỉ để vừa bố cục sheet; bố cục sheet xử lý sau.
  Nếu người dùng yêu cầu đổi pose/crop, ghi riêng phần được đổi và phần giữ.
- Ảnh gốc là input cấu trúc/identity cho lượt nét đầu; không lấy bản nét lệch
  hoặc mẫu style làm chuẩn hình học. Prompt ưu tiên giữ hình học nguồn trước,
  rồi mới mô tả nét sạch. Không dùng chỉ dẫn làm đẹp, cân đối hóa mặt, làm
  thon, mắt to, cổ thanh/dài hoặc dáng lý tưởng. Không dùng mô tả hình mặt
  do agent suy ra thay cho cấu trúc trực tiếp trong ảnh.
- Trước tạo, xác định các mốc đang nhìn thấy: đỉnh đầu/chân tóc, mắt, mũi,
  miệng, cằm, chân cổ, đầu vai và đường bao thân/tay. Prompt nêu quan hệ cần
  giữ: dài–rộng mặt, vị trí/kích thước ngũ quan, đầu so với vai/thân và
  dài–rộng cổ. Có thể bổ sung tọa độ tương đối khi hữu ích, nhưng không bịa
  số đo hoặc coi tọa độ trong prompt là cơ chế khóa hình học.
- Sau tạo, kiểm hình học trước chi tiết trang trí: xem nguồn và nét ở cùng
  kích thước canvas bằng thu phóng đồng đều; khi nghi lệch, dùng chồng hình
  hoặc đo mốc để xác minh. Không kéo giãn, warp hoặc căn riêng từng bộ phận
  để che sai lệch. Phân biệt lệch vị trí toàn hình với thay đổi tỷ lệ nội bộ;
  giữ crop không tự chứng minh mặt/cơ thể đúng tỷ lệ.
- Không đòi trùng từng pixel; chỉ chấp nhận sai khác cách đi nét không làm
  đổi tỷ lệ. Còn nhận diện, tuổi hoặc thể trạng không bù được tỷ lệ đã đổi.
  Áp dụng mục cấm thay đổi tỷ lệ cho cả nhánh này. Lệch làm đổi người, mắt lớn rõ,
  mặt dài/thon rõ, đầu lớn so với thân hoặc cổ bị kéo dài cần nêu và sửa theo
  giới hạn lượt hiện hành. Không đặt ngưỡng phần trăm khi chưa có phép đo và
  tiêu chí được xác lập. Người dùng chấp nhận lệch cụ thể thì ghi phạm vi
  version theo contract; không biến thành miễn kiểm cho các nhân vật sau.
- Nếu lệch lặp lại, không chỉ tăng lời nhắc “giữ đúng” rồi hứa chắc kết quả.
  Nêu giới hạn model vẽ lại; đề xuất dựng nét cấu trúc trực tiếp trên lớp nguồn
  trong công cụ phù hợp nếu cần độ chính xác cao hơn. Chỉ gọi là tracing/khóa
  cấu trúc khi thực sự thao tác và kiểm được lớp nét đó. Không tự đổi công cụ,
  tạo thêm lượt ảnh hoặc reset giới hạn sửa trái workflow hiện hành.

- Trước chuyển style, ghi cho từng input: identity, thiết kế, màu, bố cục
  và shading; thuộc tính được lấy/không lấy. Ảnh đơn sắc còn mảng xám,
  highlight hoặc bóng vật liệu không phải line art thuần. Gán vai trò bằng
  chữ không bảo đảm mô hình cô lập ảnh hưởng.
- Trong nhánh nét được yêu cầu rõ, khi cần loại ảnh hưởng rendering nguồn,
  dùng chân dung line art sạch làm bước nét: đường cấu trúc mặt, silhouette,
  nếp vải chính và dấu riêng của phụ kiện; nền/vùng tô trắng, không mảng
  bóng xám, chuyển sắc, hatching, vân chì hoặc đường bao highlight.
  Tóc/mày/ria có thể có mảng đen phẳng chỉ màu bản thân, không bóng sợi.
  Không đồ mỗi biên sáng–tối thành nét mới, không thêm hoa văn để lấp vùng trắng.
- So line art với identity gốc và hình mặt đã chọn; kiểm riêng mặt, tóc,
  vải, trang sức và mật độ nét. Chỉ dùng làm nền màu khi các phần này đạt;
  không gọi ảnh “sạch” chỉ vì đã bỏ màu. Model vẽ lại không phải pixel-lock.
- Khi lên màu từ line art đạt, dựng cel-shading mới bằng input mặc định ở
  trên. Giữ biến thiên sắc vùng và nét/mảng có chủ ý; không làm da lì một màu
  để giảm rendering. Mềm cục bộ không đồng nghĩa tạo khối liên tục ảnh thật.
- Prompt tách phần bắt buộc giữ khỏi phần cần tiết chế. Với nụ cười thấy răng,
  giữ nét đen có chủ ý ở mép đầu răng và ít nét kẽ ngắn theo cấu trúc, giảm
  shading men răng; không biến “ít chi tiết” thành xóa hết nét hoặc viền kín
  mọi chiếc. Không thêm răng/chi tiết miệng khi nguồn không có.
- Tô lại nhiều vùng hoặc đổi phương pháp thì dùng line art đã chọn, không
  mặc định sửa chồng output màu mới nhất. Chỉnh nhỏ dùng đúng bản user chỉ
  định và kiểm regression; không hứa pixel-lock. Khi user chọn nền nét còn
  lệch, ghi phạm vi SKIPPED_BY_USER và lỗi kế thừa, không tự coi đạt identity.
- Mô tả màu riêng phải gắn vật liệu với vị trí/thành phần cụ thể, nhất là
  khi nhiều phần cùng hình oval/tròn: phân biệt miếng vàng, đá và hạt ngọc.
  Không dùng “các oval là đá đỏ” hoặc “viền hạt là ngọc trai” nếu nguồn không
  xác nhận. Khi cần, dùng bản đồ màu phẳng đã kiểm thay mô tả mơ hồ; bản đồ
  màu không cung cấp shading và không miễn kiểm màu/identity sau tạo.
- Nếu test lên màu bị nhầm vùng da–vải hoặc vàng–đá–ngọc, trước hết kiểm cách
  phân vai/gán vùng và bảng màu với ảnh gốc. Bản tô phẳng toàn nhân vật là test
  riêng khi người dùng chọn, không phải bảng màu bắt buộc mặc định. Khi test, đối chiếu
  nguồn, lấy mẫu màu nền đại diện khi có thể
  (không lấy highlight/bóng/viền), định vị vùng da hở và từng nhóm phụ kiện.
  Kiểm màu phẳng với nguồn trước khi thêm cel-shading; không dùng tên màu
  chung hoặc một mã màu để suy toàn bộ vật liệu. Đây là bước kiểm có điều
  kiện, không bảo đảm model giữ pixel hay tự động tô đúng mọi vùng.
- Màu phẳng chỉ là kiểm gán vùng, không phải đích style st03. Không nâng
  việc bỏ bóng ở bước nét thành yêu cầu bỏ độ mềm/chi tiết ở ảnh màu cuối.
  Chỉ truyền lại ảnh gốc vào test khi người dùng yêu cầu rõ, ghi input và
  biến thay đổi, không âm thầm quay về phương pháp cũ. Line art giản lược không khóa mức chi tiết
  tối đa. Đối chiếu nguồn để khôi phục chi tiết bị mất, không tự thêm motif.
  QA giữ cả nét/mảng dẫn hình lẫn độ mềm cục bộ theo policy; không đánh giá
  đạt chỉ vì ảnh ít bóng hoặc ít chi tiết hơn.

- Xác định tạo mới hay chỉnh nhân vật; nhân vật mới được thiết kế từ brief,
  không bắt có profile trước.
- Khi cần khám phá hoặc được yêu cầu, đề xuất 2–3 hướng; dùng đầu dòng có nhãn
  diện mạo, silhouette/tỷ lệ, trang phục/màu, tính cách qua hình, đánh đổi.
  Không mặc định mở gate khi brief đủ rõ.
- Ghi vai trò từng ảnh: identity, cách quấn/trang phục, màu, pose, bố cục, ảnh đích.
- Ref trang phục không tự cung cấp mặt, tuổi, thể trạng, màu da hoặc style.
- Chỉ sửa y thì giữ mặt, tuổi, da, tỷ lệ, bố cục và phần đã chốt; ghi phạm vi trong prompt.
- Đọc lại brief và xem identity gốc mỗi lượt chỉnh; output trước là ảnh đích,
  không thay nguồn identity gốc.
- Nếu cấm output cũ, chỉ dùng nguồn được phép. Khi không dùng ref ảnh, chuyển
  đặc điểm cần giữ thành chữ; không truyền ảnh mẫu/output cũ trái yêu cầu.
- Phân biệt chữ trong ảnh với chỉ dẫn người dùng.
- Yêu cầu mới thay lựa chọn cũ thì ghi `SKIPPED_BY_USER` đúng phạm vi;
  không âm thầm áp lại lựa chọn cũ.

## Độ phân giải

- Sheet ngang ưu tiên mục tiêu 3840 × 2560 px hoặc tương đương khi công cụ hỗ trợ.
- Kiểm khả năng trước khi cam kết, xác minh pixel file sau tạo; ghi riêng mục tiêu/thực tế.
- Kích thước trong prompt không chứng minh output đạt; upscale không tạo chi tiết gốc.
- Chưa đạt thì báo giới hạn, không tuyên bố hoàn tất yêu cầu độ phân giải.

## Kiểm tra và bàn giao

- Dùng [contract kiểm hình](../../../docs/visual-review-contract.md): kiểm mặt
  và từng vật liệu đang có, tách identity/style, ghi lỗi kế thừa và điều kiện
  chuyển bước. Một lệch nhận diện trọng yếu đủ không đạt; không dùng mẫu style
  hay bản phác chưa đạt thay identity gốc. Không bắt mọi nhân vật qua chì→màu.

- Kiểm chân dung, từng góc và sự nhất quán: identity, tuổi cảm nhận, anatomy,
  màu, cấu trúc trang phục, đầu sạch khi áp dụng, chữ/bố cục.
- Đối chiếu đúng vai trò ref; nêu lỗi thấy được, không ghi đạt khi chưa xem.
- Phân biệt duyệt bố cục, duyệt bộ phận và chọn toàn ảnh làm profile;
  không suy duyệt phần thành duyệt toàn bộ.
- Lưu version mới/record theo contract, không ghi đè.
- Chỉ đưa bản được chọn rõ và đạt kiểm áp dụng vào profiles; bàn giao ảnh,
  mô tả nhận diện tái sử dụng, nguồn và trạng thái. Không tự thay profile trong tập.
