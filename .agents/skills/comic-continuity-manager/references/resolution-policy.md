# Chính sách resolve và invalidation

## Fast path

Với target đã rõ, đọc theo thứ tự và dừng khi đủ bằng chứng:

1. `page-state` hiện có;
2. scene packet chứa target;
3. ledger events có hiệu lực trước target;
4. các entry cần thiết trong episode canon;
5. profile/layout bắt buộc và cửa sổ nguồn được packet tham chiếu;
6. `notes.md`, `shot_notes.md` và nguồn thô rộng hơn khi thiếu hoặc mâu thuẫn.

Không nạp profile của nhân vật không xuất hiện, location bible không liên quan
hoặc toàn bộ chương chỉ để đề phòng chung chung.

## Source expansion

Mở rộng nguồn khi field `REQUIRED` còn thiếu; provenance chỉ là inference nhưng
cần hard lock; nguồn cùng authority mâu thuẫn; fingerprint không khớp; target
nằm ngoài packet; hoặc frame trước/sau làm đổi causal, emotional hay physical
state. Nêu chính xác field và nguồn cần đọc.

## Authority khi xung đột

Áp dụng thứ tự ưu tiên của `AGENTS.md`. Trong cùng một cấp, ưu tiên nguồn có
scope cụ thể hơn và hiệu lực gần target hơn. Không tự giải quyết hai xác nhận rõ
của người dùng; báo `CONFLICT` và hỏi một quyết định chính.

## Invalidation

- profile đổi: prompt/output/visual QA có nhân vật đó;
- scene fact hoặc ledger event đổi: source snapshot, composition và downstream
  có khai báo đọc fact đó;
- layout đổi: composition preview và layout QA; visual output chỉ stale nếu crop,
  tỷ lệ hoặc vùng bắt buộc ảnh hưởng nội dung;
- composition đổi: prompt, output và mọi QA downstream;
- prompt đổi: output và QA;
- output đổi: visual QA, layout QA và delivery selection.

Chỉ invalidate consumer có dependency liên quan. Không chạy lại cả tập. Giữ
artifact cũ để truy vết và tạo version mới theo policy hiện hành.

## Context resolution tối thiểu

```yaml
target: {}
status: COMPLETE
facts: []
locks: []
forbidden: []
dependenciesRead: []
expandedSources: []
unresolved: []
conflicts: []
staleArtifacts: []
```

Đây là hợp đồng dữ liệu, không bắt buộc tạo file riêng nếu page-state hoặc
source snapshot đã chứa các trường tương đương.
