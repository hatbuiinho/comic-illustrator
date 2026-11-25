# Nét riêng nhân vật — mỗi người một gương mặt

Người dùng chốt ngày 2026-11-02, chuyển thể cho project từ luật tạo hình nhân
vật của `signature-shot-film` (bản gốc viết cho phim/ảnh thật). Bản này viết
cho style **ttpq comic blend** thuần 2D và truyện cuộc đời Đức Phật.

**Tinh thần:** mỗi nhân vật có đặc điểm riêng, đúng người Ấn Độ thời Đức Phật,
đúng tuổi, tầng lớp và đời sống của họ. Không ai mang mặt người mẫu, không ai
đẹp chung chung như nhau, không ai giống ai.

## 1. Phạm vi

- Chỉ áp khi người dùng gọi skill `comic-character-signature`, trong đúng
  phạm vi lượt gọi đó. Không phải quy tắc mặc định của workflow nào.
- Dùng được cho profile, sheet, outline hoặc ảnh khác có người, tùy yêu cầu.
- Luật này bổ sung, không thay rule identity và tỷ lệ của workflow đang dùng.
  Khi xung đột, theo thứ tự ưu tiên của `AGENTS.md`.

## 2. Lỗi cần chặn

Máy tạo ảnh kéo mọi gương mặt về một gương mặt trung bình "đẹp":

1. **Mặt người mẫu:** mắt to hai mí, mũi thon cao, môi đầy, cằm V, mày tỉa,
   mặt cân xứng hoàn hảo, da mịn không tuổi.
2. **Trẻ hóa:** người bảy mươi trông như năm mươi; người lao động có đôi tay
   không dấu việc.
3. **Giống nhau:** các nhân vật như anh em ruột, chỉ đổi tóc và áo. Nguy cơ
   cao nhất ở chư Tăng vì cùng đầu cạo, cùng màu y.
4. **Mặt ngoại lai:** người Ấn Độ cổ đại bị vẽ theo chuẩn đẹp Đông Á (manhua,
   anime), Bollywood hiện đại hoặc Âu Mỹ.
5. **Đám đông nhân bản:** người qua đường cùng vóc, cùng dáng, cùng góc mặt.

## 3. Quan hệ với ảnh nguồn và profile

- **Ảnh nguồn/profile thắng mô tả.** Khi nhân vật có ảnh gốc hoặc profile, nét
  riêng là nét thấy trong nguồn. Không tự thêm nét (sẹo, nốt ruồi, bất đối
  xứng, dấu tuổi) mà nguồn không có.
- **Việc chính là chặn người mẫu hóa:** máy hay làm to mắt, thu mũi, gọt hàm,
  cân xứng hóa, trẻ hóa ngay cả khi có ref. Gặp vậy thì sửa cho giống nguồn,
  kể cả những nét không "đẹp" của nguồn.
- **Áp đầy đủ mục 5–6** khi nhân vật chỉ có brief, không có ảnh nguồn, hoặc
  khi người dùng yêu cầu thiết kế mới.
- **Nguồn quá giống một profile đã có:** báo người dùng kèm các trục trùng,
  đề xuất hướng tách; không tự sửa nguồn.

## 4. Bốn mức theo sự tôn kính

1. **Đức Phật — miễn hoàn toàn.** Theo dung nghi gốc và tướng tốt truyền
   thống. Không áp bất kỳ nét riêng nào của luật này. Thái tử Tất Đạt Đa chưa
   được chốt mức; hỏi người dùng khi cần.
2. **Hình thiêng khác (chư Thiên, Phạm Thiên, Đế Thích…) — miễn luật người
   đời.** Theo iconography truyền thống. Vẫn phải khác nhau giữa các vị bằng
   mão, pháp khí, vóc, dáng, màu đặc trưng; không dùng một gương mặt đẹp chung.
3. **Đại đệ tử và Tỳ Kheo, Tỳ Kheo Ni có tên — bản tôn kính.**
   - **Chọn nét từ:** tầng 1 (khung mặt), tầng 2 ở mức nhẹ (mày, mắt, mũi,
     tai, nếp nhăn tuổi), tầng 4 (vóc, dáng), tầng 5 nhẹ (da sạm vì khất thực,
     tay gầy, chân trần quen đi bộ).
   - **Nét kể hạnh tu:** ví dụ Ca Diếp già, gầy, sạm vì hạnh đầu đà; A Nan
     trẻ, nét hiền sáng, đẹp kiểu người thật chứ không phải mặt người mẫu;
     Ưu Ba Ly có thể mang dấu tay nghề cũ.
   - **Kinh điển thắng:** mô tả ngoại hình trong kinh điển hoặc kịch bản được
     ưu tiên hơn lựa chọn của agent.
   - **Cấm:** sẹo, răng mẻ, răng hô, nét gây hài, nét khiến vị ấy trông gian,
     dữ hoặc lôi thôi.
   - **Khuyết tật:** chỉ vẽ khi có trong nguồn (ví dụ A Nậu Lâu Đà mất mắt
     thịt), vẽ với sự tôn trọng.
   - Cách đắp y theo `docs/monastic-robes.md`; không chế cách đắp y khác để
     tạo khác biệt.
4. **Tỳ Kheo trong Tăng đoàn (quần chúng) — như đám đông.** Mỗi vị 1 nét; Tăng
   đoàn có đủ lứa tuổi (sa di nhỏ, trung niên, lão Tăng), vóc khác nhau, không
   ai cùng tư thế hay cùng góc đầu.

Người đời (vua quan, Bà-la-môn, đạo sĩ, thương nhân, nông dân…) áp đầy đủ.

## 5. Nét riêng gồm những gì

### 5.1. Năm tầng

| Tầng | Chọn từ |
|---|---|
| **1. Khung mặt và xương** | Hình mặt (vuông, dài, tròn, trái xoan, tam giác ngược); gò má cao hay phẳng; hàm bạnh hay nhọn; trán rộng hay hẹp; cằm lẹm hay nhô |
| **2. Đặc điểm trên mặt** | Mày rậm, thưa, xếch, cụp, gần giao nhau, một bên cao hơn · mắt mí sụp, đuôi mắt chảy, hai mắt cách xa hay gần · mũi to bè, gồ, khoằm, sống mũi lệch · môi mỏng, khóe miệng trễ · tai vểnh, dái tai to · nốt ruồi, tàn nhang, nếp nhăn do nghề (nheo nắng, cau mày lâu năm) |
| **3. Tóc và râu** | Kiểu búi, độ dày, bạc từng mảng hay bạc đều, hói đỉnh, chân tóc lùi; râu dài, râu thưa, tóc bết của đạo sĩ khổ hạnh. Tu sĩ: đầu cạo, không dùng tầng này |
| **4. Thân và dáng** | Cao thấp, gầy đậm, bụng, vai xuôi hay khom, vai lệch; cách đứng (dồn một chân, chắp tay sau lưng), cách ngồi; bàn tay to bè, gầy guộc, chai sần |
| **5. Dấu đời và nghề** | Da sạm nắng tới đâu (gáy, vai, mu bàn tay); vật quen tay (gậy, bình nước, bát, lưỡi liềm); cách mặc (quấn vải cao, vạt vải xộc xệch, khăn bạc màu) |

Ở khâu outline chỉ tính những nét nét vẽ thể hiện được; nét chỉ có ở màu (da
sạm, mảng màu áo) chưa tính.

### 5.2. Số nét tối thiểu theo vai

| Vai | Số nét | Yêu cầu |
|---|---|---|
| Nhân vật chính | 5 trở lên | Ít nhất 2 nét đọc được khi nhìn xa (vóc, dáng, tóc, đồ mang theo) và 2 nét đọc được khi cận (trên mặt) |
| Nhân vật phụ | 3–4 | Ít nhất 1 nét xa, 1 nét gần |
| Người thoáng qua | 1–2 | Đọc được ở đúng cỡ khung người ấy xuất hiện |
| Người trong đám đông | 1 | Mỗi người khác nhau ít nhất về tuổi, vóc hay dáng |

Mức 3 ở mục 4 vẫn tính số nét theo vai, nhưng chỉ chọn trong phạm vi đã nêu.

### 5.3. Nét phải kể được đời người

Nét tốt kể một điều về người ấy, không chỉ để khác: vai khom vì đời cúi lưng
cày ruộng, đuôi mắt nhăn vì nheo nắng, thân gầy guộc vì khổ hạnh, bàn tay
chai vì kéo lưới. Ưu tiên nét đi ra từ kịch bản hơn một nốt ruồi đặt ngẫu nhiên.

## 6. Các nhân vật phải khác nhau

- **Khác ít nhất 3 trên 6 trục:** tuổi, vóc, hình mặt, tóc, kiểu và màu trang
  phục, dáng đứng.
- **Chư Tăng mất hai trục** (tóc, trang phục), nên phải khác ở ít nhất 3 trong
  4 trục còn lại: tuổi, vóc, hình mặt, dáng. Thêm được vật mang theo và cách
  cầm (bát, gậy, cách chắp tay).
- **Phép thử bóng đen:** tô đen mọi nhân vật thành bóng, vẫn phải biết ai là
  ai nhờ vóc, tóc, dáng và đồ mang theo. Bắt buộc với nhân vật chính và những
  nhân vật hay đứng cạnh nhau.
- **Đối chiếu cast:** khi tạo profile mới, so với các profile đã có cùng nhóm
  (cùng giới, cùng lứa tuổi, cùng là tu sĩ) theo 6 trục; nêu kết quả trong
  phản hồi.
- **Đa dạng trong một cộng đồng:** khác tầng lớp, vùng và nghề (Bà-la-môn,
  Sát-đế-lợi, thương nhân, nông dân, người miền rừng…), không ai cùng một khuôn.

## 7. Đúng người, đúng tuổi, không xấu hóa

- **Người Ấn Độ thời Đức Phật:** theo era guide và nguồn; không vay chuẩn đẹp
  Đông Á, Bollywood hay mặt quảng cáo. Không dùng một công thức mặt cho mọi
  người Ấn Độ.
- **Tuổi hiện ra ở mặt, cổ, tay, dáng,** không chỉ ở tóc bạc. Không trẻ hóa
  hay làm đẹp người già, người nghèo.
- **Không xấu hóa:** không phóng nét riêng thành biếm họa hay biến dạng; không
  lấy khuyết tật làm "nét" khi nguồn không có; không để nét riêng đổi phe
  nhân vật (người thiện đọc thành ác) trừ khi kịch bản muốn thế.
- **Nhân vật có biến chuyển:** ví dụ Ương Quật Ma La trước và sau xuất gia.
  Nét nhận diện phải nằm ở khung mặt, mày, tai, vóc từ lúc làm profile, vì tóc
  sẽ mất. Sau xuất gia không được còn đọc thành người ác.
- **Phản diện** (Đề Bà Đạt Đa…) được có nét hợp vai, nhưng không biếm họa.
  **Ma vương** không áp luật người đời, nhưng cần thiết kế riêng, không dùng
  mặt "phản diện đẹp" chung chung.
- **Trẻ em:** nét nhẹ và lành (răng sún, tóc vểnh, mũi tẹt, tai hơi to). Không
  sẹo, không thương tích, không mặt búp bê.

## 8. Đám đông và người qua đường

- Mỗi người khác nhau về tuổi, vóc, mặt, cử chỉ, trang phục. Một đám đông có
  ít nhất ba lứa tuổi; không hai người cùng tư thế, cùng góc đầu.
- Viết cụ thể từng người hoặc từng cụm, không chỉ "a crowd of villagers".
- Người ở xa vẫn khác nhau bằng dáng và silhouette: người cao gầy, người thấp
  đậm, người khom, người bế con, người đội giỏ.
- Nhóm quần chúng có profile: dùng ảnh ref nhóm, mô tả thêm theo cảnh để các
  thành viên không thành bản sao của nhau.

## 9. Cách viết vào prompt (2D)

- **Chữ vẽ được, cụ thể, khẳng định:** "a broad flat nose", "thick eyebrows
  that almost meet". Không dựa vào "unique", "distinctive", "characterful".
- **Nét quan trọng nhất đặt đầu đoạn mô tả người.** Profile tả dài; prompt
  cảnh chỉ nhắc nét hợp cỡ khung, phần còn lại giao cho ảnh ref.
- **Nét lệch một bên ghi theo cơ thể nhân vật** ("his left eyebrow"), không
  theo màn hình; soát lại khi đổi góc hoặc lật ảnh.
- **Chỉ dùng ngôn ngữ nét vẽ:** không dùng từ ảnh thật như `open pores`,
  `skin texture`, `street-cast actor`, `photographic`. Tuổi và dấu đời diễn
  bằng nét và mảng, không bằng texture da.
- **Câu phủ định gom vào `Avoid/Negative constraints`,** theo
  `docs/prompt-constraints.md`.

### Kho câu mẫu

```text
FACE STRUCTURE: a long narrow face with a heavy jaw · a round face with high flat cheekbones · a square face with a broad jaw · a small receding chin
FEATURES: thick straight eyebrows that almost meet · one eyebrow sitting slightly higher than the other · heavy-lidded eyes set wide apart · a broad flat nose · a large hooked nose · a slightly crooked nose bridge · thin lips with downturned corners · ears that stand out from the head · long earlobes · a mole beside the left nostril · a few drawn crease lines at the eye corners from squinting into the sun
HAIR & BEARD: a loose topknot of coarse matted hair · grey only at the temples · thinning at the crown · a long uneven grey beard · a sparse chin beard
BODY & STANCE: slightly stooped at the shoulders · one shoulder lower than the other · a heavy belly over a knotted waist cloth · thin wrists and big knuckled hands · stands with weight on one leg, hands clasped behind the back
LIFE & TRADE: rope-worn calloused hands drawn with a few short lines · bony ascetic frame with visible collarbones · a faded cloth wrapped high on the head · a walking staff worn smooth at the grip
AGE (2D): a few drawn wrinkle lines on the forehead and around the mouth · loose skin at the throat shown by two soft lines · visible knuckles and tendons on the hands · slightly sunken cheeks
MONK (respectful): a narrow oval face with deep-set calm eyes · a broad square face with a strong brow · a lean, slightly stooped elderly frame · a tall, straight-backed young frame · large gentle hands holding the alms bowl low
CHILD: a gap where a milk tooth fell out · a stubborn tuft of hair · a small flat nose · ears a little large for the head
CROWD: an old woman leaning on a staff, two boys sharing one basket, a heavy-set farmer with a cloth over one shoulder, a young mother carrying a baby on her hip (every person different in age, build, face and gesture)
FACE LOCK (2D): a specific, ordinary, slightly asymmetric face drawn in clean 2D linework, true to its source or brief — not a generic, idealised, pretty anime or model-like face
AVOID (thêm vào khối điều cấm): no model faces, no generic pretty anime faces, no symmetry correction, no age-smoothing, no identical faces, no cloned figures
```

`FACE LOCK` và `AVOID` là câu phụ, đi sau nét cụ thể, không thay cho chúng.
Với nhân vật có ảnh nguồn, không chèn câu mẫu mô tả nét mà nguồn không có.

## 10. Soát ảnh có người

1. Có gương mặt nào ra kiểu người mẫu hoặc mặt anime đẹp chung không?
2. Có hai người nào trong khung, hoặc giữa các profile, giống nhau như anh em không?
3. Nét riêng đã ghi có hiện ra ở cỡ khung đó không, có đúng bên không?
4. Tuổi có bị trẻ hóa không?
5. Gương mặt có đúng người Ấn Độ cổ đại theo nguồn, không bị Đông Á hóa hay
   Bollywood hóa không?

Soát thêm: mức tôn kính đúng (mục 4); hành động hợp với người ấy; đám đông
không nhân bản.

**Xử lý:** người thoáng qua lệch thì ghi lỗi, sửa từng người khi người dùng
yêu cầu; nhân vật có profile bị người mẫu hóa thì sửa theo profile gốc; đám
đông nhân bản thì viết lại mô tả đám đông.
