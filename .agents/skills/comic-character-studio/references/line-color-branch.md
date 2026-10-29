# Nhánh tùy chọn: nét chì/line art và bảng màu, lên màu

> Cập nhật người dùng 2026-10-29 — `SKIPPED_BY_USER`, toàn dự án:
> style duy nhất là **ttpq comic light** (`docs/style-ttpq-comic-light.md`,
> đường dẫn từ root). Các yêu cầu rendering, bảng trang sức/ref style cũ,
> override st03 và khối prompt style cũ bên dưới đã được thay thế; không
> copy các phần đó vào prompt mới. Workflow và identity vẫn giữ; QA theo qa-checklist.md.
> Chỉ khi ảnh có tu sĩ mới đọc `docs/monastic-robes.md` cho màu/cách quấn y.


Một phần của [SKILL.md](../SKILL.md) Character Studio. Chỉ đọc khi người dùng yêu cầu rõ nhánh nét hoặc nhánh màu.
QA ảnh trong nhánh theo [qa-checklist.md](qa-checklist.md).

Chỉ đọc và thực hiện các hướng dẫn chuyên biệt dưới đây khi người dùng yêu
cầu rõ nhánh tương ứng. Các từ “mặc định” về input bên dưới chỉ áp dụng trong
nhánh tô màu này, không thay workflow chuyển style trực tiếp. Yêu cầu chuyển
style, chỉnh style hoặc QA chưa đạt không tự kích hoạt nhánh nét/màu.

Rendering: các mô tả “độ mềm cục bộ”, “mềm tiết chế” trong nhánh này là
cách tô của nhánh màu đã chốt ngày 2026-10-21. Chỉ áp dụng khi người dùng
yêu cầu rõ nhánh màu; không đưa vào luồng chuyển style trực tiếp, nơi
rendering mảng phẳng của SKILL.md có hiệu lực.


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
đã ổn định trên mọi nhân vật. Style theo ttpq comic light.

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
  [user style 01](../assets/style-user-v001.png) và
  [user style 02](../assets/style-user-v002.png), trừ khi user chỉ định input khác.
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
  [record mẫu 02](../assets/style-user-v002.md). Không tự lưu mẫu thành profile.
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
  [line art user v001](../assets/line-art-user-v001.png), bản sao nguyên ảnh
  `studios/character/outputs/nu-an-do-test-2/portrait-line-v004.png`.
  Xem và dùng mẫu này cho lượt chuyển nguồn thành line art khi công cụ hỗ trợ,
  trừ khi người dùng chỉ định input khác; phân vai như trên. Lấy nền/vùng tô
  trắng, môi không vân xám, nét cấu trúc và cách giữ viền/hoa văn/phụ kiện.
  Không lấy nhiều đường sáng mảnh ở tóc, tỷ lệ đã lệch nguồn hoặc motif cụ
  thể của mẫu. Hai `style-user` tiếp tục phục vụ tô màu, không thay mẫu nét.
  Lựa chọn mẫu không duyệt profile toàn ảnh; phạm vi và giới hạn tại
  [record mẫu nét](../assets/line-art-user-v001.md). Không tự tạo mẫu hoặc thêm
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
  Áp dụng mục cấm thay đổi tỷ lệ trong [SKILL.md](../SKILL.md) cho cả nhánh này. Lệch làm đổi người, mắt lớn rõ,
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
- Màu phẳng chỉ là kiểm gán vùng, không phải đích style. Không nâng
  việc bỏ bóng ở bước nét thành yêu cầu bỏ độ mềm/chi tiết ở ảnh màu cuối.
  Chỉ truyền lại ảnh gốc vào test khi người dùng yêu cầu rõ, ghi input và
  biến thay đổi, không âm thầm quay về phương pháp cũ. Line art giản lược không khóa mức chi tiết
  tối đa. Đối chiếu nguồn để khôi phục chi tiết bị mất, không tự thêm motif.
  Không đánh giá đạt chỉ vì ảnh ít bóng hoặc ít chi tiết hơn.
