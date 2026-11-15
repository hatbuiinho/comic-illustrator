# Mẫu story bible và scene sheet

Lưu tại `ttpq-comic/story/<tập>/`. Mọi dữ kiện ghi nguồn `Ch<n> L<dòng>` theo
`script.md`; điều suy luận ghi "(suy ra)". Viết tiếng Việt, ngắn, dễ quét.

## bible.md

~~~markdown
# Story bible — Tập <n>

- Trạng thái: DRAFT | APPROVED (theo từng mục nếu người dùng duyệt từng phần)
- Nguồn: script.md (<ngày nhận>)

## Tóm tắt mạch truyện
<3–6 dòng theo chương>

## Mốc thời gian
| Ngày | Chương | Cảnh | Ghi chú |

## Nhân vật
| Nhân vật | Vai trò | Xuất hiện (cảnh) | Profile | Ghi chú hình |

## Địa điểm
### <Tên địa điểm>
- Vùng/khu: …
- Đặc điểm cố định: …
- Thay đổi theo thời gian: …

## Tiến độ / trạng thái thay đổi
| Mốc | Cảnh | Trạng thái | Nguồn |

## Đạo cụ xuyên suốt
- <đạo cụ>: <mô tả, cảnh, nguồn>

## Điều cấm chung của tập
- <cấm>: <lý do>

## Avoid trong prompt
- <điều cấm chung, tiếng Anh ngắn, dùng cho mọi prompt ảnh>
- [khi: <từ khóa tiếng Việt có trong cảnh>, …] <điều cấm chỉ áp cho cảnh có các từ khóa đó>

## Cặp dễ nhầm
- <slug-a> + <slug-b>: <một câu tiếng Anh nêu điểm khác nhau>

## Cần quyết
| # | Chi tiết trong kịch bản | Vấn đề | Đề xuất | Quyết định |
~~~

## scenes.md

~~~markdown
### S<nn> — <tên cảnh> · Ch<n> L<a>–<b> · DRAFT
- **Thời điểm/ánh sáng:** <ngày thứ mấy, giờ, thời tiết, nguồn sáng>
- **Nơi:** <địa điểm, khu>
- **Nhân vật:** <ai, trạng thái, đạo cụ cầm>
- **Profile:** <slug, slug:ref-khác.png, … hoặc —>
- **Diễn biến:** <hành động chính, khoảnh khắc có thể vẽ>
- **Được phép:** <bối cảnh, đạo cụ, quần chúng hợp cảnh>
- **Cấm:** <việc chưa/không xảy ra, sai niên đại liên quan>
- **Avoid:** <bản tiếng Anh ngắn của Cấm, dùng cho prompt; không có thì script dùng Cấm>
- **Continuity:** <phải khớp với cảnh trước/sau>
~~~
