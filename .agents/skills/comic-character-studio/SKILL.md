---
name: comic-character-studio
description: Tạo, phát triển hoặc chỉnh character profile và character sheet trong Character Studio, giữ style dự án. Dùng khi người dùng @ skill kèm ảnh gốc để chuyển sang style 2D dự án, dựng sheet nhân vật, chỉnh nhân vật hoặc lưu profile; độc lập với workflow minh họa tập/page.
---

# Character Studio

> Cập nhật người dùng 2026-10-29 — `SKIPPED_BY_USER`, toàn dự án:
> style duy nhất là **ttpq comic light** (`docs/style-ttpq-comic-light.md`,
> đường dẫn từ root). Các yêu cầu rendering, bảng trang sức/ref style cũ,
> override st03 và khối prompt style cũ bên dưới đã được thay thế; không
> copy các phần đó vào prompt mới. Workflow và identity vẫn giữ; QA cũ đã
> thay bằng [qa-checklist.md](references/qa-checklist.md).
> Chỉ khi ảnh có tu sĩ mới đọc `docs/monastic-robes.md` cho màu/cách quấn y.


Đọc và áp dụng [contract studio](../../../docs/studio-contract.md)
và [policy phong cách](../../../docs/project-style-policy.md).

## Checklist lắp prompt trước khi gửi

SKILL.md giữ workflow, cổng duyệt và rule lõi. Trước mỗi lượt tạo/chỉnh,
đi qua bảng dưới theo thành phần thực sự có trong ảnh; đọc đúng file, chèn
khối tương ứng vào prompt và truyền ref cần thiết. Không đọc file không áp dụng.

| Điều kiện | Đọc | Chèn vào prompt | Ref truyền kèm |
|---|---|---|---|
| Mọi lượt chuyển style | [default-2d-prompt.md](references/default-2d-prompt.md) | khối lõi | ảnh gốc (identity) |
| Mọi lượt có ảnh gốc/profile | mục tỷ lệ, lý tưởng hóa, negative bên dưới | khối giữ tỷ lệ + khối Avoid chibi/Trung Quốc hóa + dấu riêng của nguồn | — |
| Có mặt/da nhìn thấy | [face-and-skin.md](references/face-and-skin.md) | khối Eyes/Nose/Mouth/Lower lip | — |
| Có trang phục | [fabric-jewelry.md](references/fabric-jewelry.md) | khối Fabric | — |
| Có trang sức | [fabric-jewelry.md](references/fabric-jewelry.md) | phần giữ/đổi trang sức | — (không bắt buộc ref vật liệu cũ) |
| Nhân vật nữ | mục **Trang phục nữ kín đáo** bên dưới | câu che kín bụng/eo mọi góc | — |
| Tu sĩ | [monk-standard.md](references/monk-standard.md) | đầu cạo sạch, màu y, cấu trúc y quấn | [crop màu y v002](assets/mau-y-chuan-crop-v002.png), [mẫu quấn y v001](assets/y-quan-chuan-v001.png) |
| Dựng sheet | [sheet-layout.md](references/sheet-layout.md) | bố cục, thông tin in, độ phân giải; tự mở rộng canvas khi thiếu chỗ, giữ tỷ lệ và khoảng trắng giữa các góc, cấm bóp hình để vừa sheet | ảnh chuyển style đã duyệt + ảnh gốc |
| Người dùng yêu cầu rõ nhánh nét/màu | [line-color-branch.md](references/line-color-branch.md) | theo nhánh | theo nhánh |

- Sau khi lắp, kiểm prompt có đủ các khối của mọi dòng áp dụng và các
  `SKIPPED_BY_USER` đang có hiệu lực, rồi mới gửi. Lưu prompt thực tế trong record.
- Sau khi tạo, QA duy nhất theo [qa-checklist.md](references/qa-checklist.md);
  các file reference khác chỉ dùng để lắp prompt.
- Lịch sử các quyết định người dùng đã chốt nằm tại
  [decision-log.md](references/decision-log.md); rule bên dưới là bản hiện hành.

## Công cụ tạo ảnh

- Codex: dùng skill `imagegen`/ImageGen trực tiếp theo
  [contract studio](../../../docs/studio-contract.md).
- Claude Code không có ImageGen. Khi cần tạo/chỉnh ảnh, gọi qua Codex CLI:
  `codex exec -C <repo> -i <ảnh gốc> -i <ref khác> "<prompt>"`, trong đó
  prompt nêu vai trò từng ảnh theo thứ tự `-i` và đường dẫn lưu output có
  version. Sau khi chạy, kiểm file thực sự tồn tại ở đúng đường dẫn và xem
  ảnh trước QA; không coi lời báo của Codex là bằng chứng đã tạo.
- Nếu công cụ không nhận đủ ảnh ref, ghi input thực tế đã truyền và chuyển
  phần thiếu thành mô tả chữ; không tuyên bố đã dùng ref không được truyền.

## Prompt mặc định đã chốt

Khi chỉ @ skill và đính kèm ảnh gốc, tự bắt đầu chuyển style bằng [prompt 2D mặc định](references/default-2d-prompt.md);
không yêu cầu viết lại prompt hoặc chọn workflow. Nếu chỉ gọi skill mà không
có ảnh/brief truy cập được, hỏi nguồn cần dùng. Yêu cầu chỉnh, tạo sheet,
bảo trì skill hoặc nhánh nét/màu rõ ràng vẫn route theo đúng yêu cầu đó.

- Đọc prompt 2D mặc định trước khi viết prompt cho lượt chuyển style. Giữ khối lõi
  đã chốt; chỉ bổ sung ngắn các dấu riêng và ràng buộc thực sự áp dụng.
- Rendering mặc định là `ttpq comic light` theo policy toàn dự án;
  override rendering st03 trước đây đã hết hiệu lực. Không dùng khối style
  hoặc ref vật liệu cũ để thay định nghĩa mới.
- Giữ các rule thiết kế, tỷ lệ, nét cấu trúc, đầu cạo, trang phục nữ, reference,
  QA, giới hạn tự sửa và cổng duyệt trước sheet/lưu profile. Rule màu y và
  cách quấn y chuẩn vẫn mặc định có hiệu lực; dòng giữ màu da không miễn
  rule màu y. Câu giữ thiết kế chung trong prompt không tự miễn chuẩn quấn y.
- Ngoại lệ trực tiếp mới nhất chỉ thay đúng dòng/phạm vi liên quan; không
  giữ đồng thời chỉ dẫn mâu thuẫn. Ví dụ đổi da hồng tuổi 60–70 thì thay dòng
  giữ màu da, không trẻ hóa hay đổi thiết kế. Chỉ giữ màu/cách quấn y khác
  chuẩn khi người dùng yêu cầu rõ phạm vi đó; ghi `SKIPPED_BY_USER`.

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
  vì hỏi lại; lượt tự sửa là chạy lại từ ảnh gốc theo mục **Chỉ tạo lại từ
  ảnh gốc**, không chỉnh trên output. Khi cần người dùng định hướng, nêu lỗi và đề xuất sửa hoặc đổi
  hướng; không đưa lên màu/dựng sheet/lưu profile như hành động đã sẵn sàng
  nếu điều kiện phụ thuộc chưa đạt, trừ override rõ có ghi phạm vi.
- Không tự tạo biến thể hoặc chạy ảnh chỉ vì có lựa chọn trong menu.
  Cổng chờ duyệt ảnh chuyển style trước sheet là bắt buộc trong luồng mặc
  định. Trong nhánh màu được yêu cầu rõ, bảng màu đã kiểm có thể dùng lên màu
  cùng lượt nếu yêu cầu bao gồm lên màu và không thuộc nhánh màu da cần chốt.

## Mục tiêu tạo hình

- Mặc định dùng ttpq comic light với cấu trúc mặt/cơ thể tự nhiên, nhưng rendering
  theo mục **Prompt mặc định đã chốt**: nét/mảng 2D rõ, màu phẳng sạch không hạt.
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
- Đây là biện pháp giảm nguy cơ, không bảo đảm mô hình không tự diễn giải.
  Nếu người dùng yêu cầu làm đẹp/đổi nét riêng rõ, chỉ thay trong phạm vi đó,
  ghi thay đổi và `SKIPPED_BY_USER` theo contract, không mở rộng sang phần khác.

### Negative prompt trước tạo hình

- Áp dụng quy tắc toàn dự án về
  [đưa điều cấm vào prompt từ đầu](../../../docs/prompt-constraints.md).
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


## Trang phục nữ kín đáo

Quy tắc thiết kế project, áp dụng cho mọi nhân vật nữ trong Character Studio, gồm chân dung, sheet, bản thử
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

## Bảo trì skill và kiểm thử workflow

- Khi người dùng đang cải thiện skill/workflow, ưu tiên sửa hướng dẫn tái sử
  dụng từ lỗi quan sát được. Không tự chuyển trao đổi phương pháp thành chuỗi
  chỉnh ảnh riêng lẻ. Chỉ chạy ảnh kiểm chứng khi được yêu cầu; giữ input và
  biến thử rõ, không lấy một ảnh đẹp làm bằng chứng skill đã ổn định.
- Sau mỗi lần kiểm thử hoặc phân tích lỗi workflow, đưa đề xuất hành động
  tiếp theo: sửa gì trong skill/đầu vào, kiểm chứng bằng cách nào và tiêu chí
  đạt. Nêu hướng ưu tiên cùng lý do; nếu có 2–3 phương án thực tế thì đánh số,
  ghi đánh đổi ngắn. Không dừng ở chẩn đoán hoặc để người dùng tự suy bước sau;
  phân biệt đề xuất với việc đã thực hiện, không tự coi đề xuất là phê duyệt.

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

## Sử dụng reference và chỉnh sửa

### Workflow mặc định: chuyển trực tiếp ảnh gốc sang style dự án

Luồng này thay mặc định cũ nét → bảng màu → lên màu; nhánh cũ chỉ dùng khi
được yêu cầu rõ.

- Đọc brief và xem ảnh gốc → dùng prompt 2D mặc định cùng rule thiết kế → QA theo
  [qa-checklist.md](references/qa-checklist.md) → trình ảnh, chờ người dùng duyệt → tạo sheet.
  Không tạo nét chì/line art, bảng màu hoặc lượt lên màu tách riêng ở giữa.
- Truyền ảnh gốc làm reference identity/thiết kế/màu/cấu trúc; dùng reference
  style hiện hành theo policy và định nghĩa ttpq comic light. Style ref chỉ cung cấp cách
  diễn nét/mảng, không cung cấp khuôn mặt, trang phục, màu hoặc bố cục.
  Không mặc định truyền hai user style cũ của nhánh tô màu vào luồng này.
- Giữ nguyên chi tiết quan sát được: mặt, tuổi, thể trạng, tỷ lệ, tóc/râu,
  trang phục, hoa văn, trang sức/phụ kiện, màu và vị trí vật liệu; giữ pose,
  biểu cảm, góc nhìn, crop và bố cục nguồn. Chỉ chuyển cách diễn nét, mảng
  sáng–trung–tối và bề mặt sang style dự án. Không tự thêm/bớt, thay thiết kế,
  làm đẹp, sửa trang phục hoặc đổi pose để chuẩn bị cho sheet.
- Với vải, “giữ nguyên chi tiết” giữ thiết kế nhận diện, không giữ texture
  vật liệu; áp dụng mục **Vải phẳng, sạch** trong
  [fabric-jewelry.md](references/fabric-jewelry.md) cho prompt.
- Prompt và record phải tách `Giữ nguyên theo nguồn`, `Chỉ đổi cách thể hiện`
  và `Avoid/Negative constraints`, nêu dấu riêng cụ thể và điều cấm tương ứng.
  Chi tiết không đọc rõ thì ghi giới hạn, không đoán hoặc thêm motif để bù.
- Màu da: giữ sắc độ, sắc màu và độ bão hòa theo nguồn; không mặc định tăng
  độ ấm hoặc dùng “warm skin tone” thay khóa màu nguồn. Prompt phải cấm tăng
  vàng/cam riêng trên da, kể cả khi đã cấm lớp phủ vàng/cam toàn ảnh. Không lấy
  màu da từ ref style hay ref màu y. Chỉ đổi màu da khi người dùng
  yêu cầu rõ.
- Giữ thiết kế nguồn trong phạm vi không xung đột với rule thiết kế studio:
  màu/cách quấn y chuẩn và độ phủ trang phục nữ vẫn mặc định áp dụng.
  Nếu nguồn khác chuẩn, nêu delta áp dụng trong prompt/record. Chỉ ghi
  `SKIPPED_BY_USER` cho phần người dùng yêu cầu rõ giữ khác chuẩn, không
  suy waiver từ câu giữ thiết kế chung của prompt mặc định.
- Nếu QA bị chặn, báo lỗi cụ thể, không coi ảnh sẵn sàng dựng sheet; nếu
  đạt, vẫn chờ người dùng duyệt version hiện hành.
- Khi dựng sheet sau duyệt, dùng ảnh chuyển style được chọn cùng nguồn gốc
  đúng vai trò; bố cục/góc đứng theo mục sheet. Không đổi thiết kế đã duyệt;
  phần khuất chưa có dữ kiện phải ghi là suy dựng, không giả là chi tiết nguồn.

### Chỉ tạo lại từ ảnh gốc

Người dùng chốt ngày 2026-10-24 sau khi chuỗi chỉnh nối tiếp trên output làm
ảnh giảm chất lượng nghiêm trọng.

- Mọi lượt tạo lại, tự sửa sau QA hoặc chỉnh theo yêu cầu người dùng đều chạy
  từ ảnh gốc (và crop của ảnh gốc), không lấy output trước làm ảnh đầu vào để
  chỉnh, làm ảnh đích edit hay làm ref identity/mặt/màu. Lỗi của lượt trước
  được sửa bằng cách bổ sung yêu cầu vào prompt rồi chạy lại từ ảnh gốc.
- Không tự ý chỉnh trực tiếp trên file output, kể cả tô/vẽ thêm bằng script,
  inpaint hay chỉnh màu cục bộ. Chỉ làm khi người dùng yêu cầu rõ thao tác đó
  trên đúng version; ghi `SKIPPED_BY_USER` cùng phạm vi.
- Output cũ chỉ dùng để so sánh trong QA và record (ghi `previousVersion`
  thay cho `parentVersion` khi không phải ảnh đầu vào).
- Ngoại lệ duy nhất theo luồng mặc định: khi dựng sheet, được truyền ảnh
  chuyển style người dùng đã duyệt rõ cùng ảnh gốc. Sửa sheet chưa đạt thì
  chạy lại từ cùng bộ input đó, không chỉnh trên sheet lỗi.
- Khi có nhiều ảnh gốc (ví dụ ảnh gốc thật và sheet AI tạo từ nó), ghi vai trò
  từng ảnh trong brief; tất cả vẫn là nguồn gốc, không phải output của studio.

### Quy tắc reference chung khi tạo/chỉnh

- Xác định tạo mới hay chỉnh nhân vật; nhân vật mới được thiết kế từ brief,
  không bắt có profile trước.
- Khi cần khám phá hoặc được yêu cầu, đề xuất 2–3 hướng; dùng đầu dòng có nhãn
  diện mạo, silhouette/tỷ lệ, trang phục/màu, tính cách qua hình, đánh đổi.
  Không mặc định mở gate khi brief đủ rõ.
- Ghi vai trò từng ảnh: identity, cách quấn/trang phục, màu, pose, bố cục.
- Ref trang phục không tự cung cấp mặt, tuổi, thể trạng, màu da hoặc style.
- Chỉ sửa y thì giữ mặt, tuổi, da, tỷ lệ, bố cục và phần đã chốt; ghi phạm vi trong prompt.
- Đọc lại brief và xem identity gốc mỗi lượt chỉnh; chạy lại từ ảnh gốc theo
  mục **Chỉ tạo lại từ ảnh gốc**, không truyền output trước làm input.
- Đặc điểm cần giữ hoặc sửa từ lượt trước được chuyển thành chữ trong prompt;
  không truyền ảnh mẫu/output cũ trái yêu cầu.
- Phân biệt chữ trong ảnh với chỉ dẫn người dùng.
- Yêu cầu mới thay lựa chọn cũ thì ghi `SKIPPED_BY_USER` đúng phạm vi;
  không âm thầm áp lại lựa chọn cũ.

### Nhánh tùy chọn: nét chì/line art và bảng màu, lên màu

Chỉ đọc và thực hiện [line-color-branch.md](references/line-color-branch.md)
khi người dùng yêu cầu rõ nhánh tương ứng. Yêu cầu chuyển style, chỉnh
style hoặc QA chưa đạt không tự kích hoạt nhánh nét/màu.

## Kiểm tra và bàn giao

- QA theo [qa-checklist.md](references/qa-checklist.md), thay cho contract
  kiểm hình chung; không chạy thêm bảng kiểm style theo vùng hay zoom từng vùng.
- Phân biệt duyệt bố cục, duyệt bộ phận và chọn toàn ảnh làm profile;
  không suy duyệt phần thành duyệt toàn bộ.
- Lưu version mới/record theo contract, không ghi đè. Copy output của lượt
  (ảnh tạo, crop nguồn) vào `studios/character/outputs/<character-id>/` theo
  contract; chỉ trình người dùng bản trong thư mục đó. Ảnh so sánh QA không cần lưu.
- Chỉ đưa bản được chọn rõ và đạt kiểm áp dụng vào profiles; bàn giao ảnh,
  mô tả nhận diện tái sử dụng, nguồn và trạng thái. Không tự thay profile trong tập.
