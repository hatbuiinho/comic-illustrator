# Đo typography proxy — schema 4

Áp dụng cho `TEXT_PROXY_INTEGRATION` và `BAKED_TEXT_PROXY_CONCEPT`.
Đây là contract đo chung cho source reader, shot design và layout QA.

## Đơn vị và dữ liệu nguồn

Lưu `pdfPageSizePt`, canvas/viewBox, `fontSizePt`, `leadingPt`,
`medianGlyphHeightPt`, line widths, khoảng cách đoạn và paragraph map riêng.
Cỡ font là em size; glyph height là hộp chữ render. Không thay thế hai đại lượng.

`canvasUnitsPerPt.x = viewBoxWidth / pdfPageWidthPt`, tương tự Y. Hai tỷ lệ
phải khớp trong 0,5%; không dùng DPI mặc định của SVG để quy đổi PDF sang canvas.
Ví dụ Page 10: 1802 / 810,709 ≈ 2,223; 12 pt ≈ 26,67 canvas units;
leading 17 pt ≈ 37,79 units. `data-dpi="96"` không thay đổi tỷ lệ này.

## Proof và phép đo độc lập

Proof giữ artifact/hash và ánh xạ occurrence của schema 3, nâng `schemaVersion: 4`.
Mỗi `sourceTextRegion` bổ sung:

```json
{
  "boundsPt": [40, 60, 320, 440],
  "paragraphOrder": ["l01", "l02"],
  "paragraphLineCounts": [4, 1]
}
```

`boundsPt` là cửa sổ trích nguồn PDF [x,y,width,height], không là vùng bắt buộc
đặt chữ trong composition. Chọn đủ toàn occurrence, loại số trang và occurrence
lân cận. Paragraph map lấy từ nguồn đã kiểm chứng; mọi `<text>` proxy có
`data-paragraph-id`. Không copy số đếm tự khai vào kết quả render.

Verifier gọi `measure-proxy-typography.js`: trích PDF nguồn bằng Poppler;
render từng SVG text group bằng librsvg sang PDF có kích thước vật lý đúng trang
nguồn, rồi đo lại bằng cùng Poppler. Giữ inherited font và ancestor transforms.
Report ghi font thực đã render, cỡ font, glyph bounds, leading, độ dài dòng,
tổng diện tích hộp dòng và chiều cao khối chữ. Không so tọa độ proxy với nguồn.

Glyph height dùng nét chữ nhìn thấy trên raster PDF cùng 144 DPI; giữ riêng
`glyphDescriptorHeightPt` vì hộp metadata FontDescriptor của InDesign và Cairo
có thể khác nhau với cùng cỡ chữ. Không dùng khác biệt metadata để kết luận chữ
co hoặc tự hạ ngưỡng. `renderEnvironment.pangoCairoBackend` ghi `fc` hoặc
`coretext` khi cần; verifier và renderer preview dùng cùng backend đã khai báo.

## Dàn trang theo ý đồ

Proof mới dùng `layoutComparison: ART_DIRECTED`. Giữ font 95–105%, glyph 90–115%,
leading 95–110% và lượng ký tự đại diện 90–110% theo phép đo. Không so tọa độ.
Số dòng, số dòng mỗi đoạn, khoảng nghỉ, chiều cao/diện tích khối và median measure
là cảnh báo review, không tự FAIL vì khác mẫu. Giữ mọi occurrence và thứ tự đoạn;
review khả năng đọc, wrap và lượng nội dung của từng đoạn bằng mắt.

Proof cũ không khai mode vẫn kiểm bảo toàn nhịp nguồn để tương thích, nhưng không
bắt composition mới đi theo mode cũ. Cấm dùng mode ART_DIRECTED để bỏ chữ hoặc
thu nhỏ cỡ đọc. Script đo kỹ thuật; `PROXY_COMPOSITION_PASS` không phải art PASS.

Thiếu dependency/evidence hoặc render lỗi phải báo thiếu bằng chứng, không bịa PASS.
CSS/tspan/textLength và nhiều cột chưa có exporter phù hợp phải báo giới hạn;
không hạ chất lượng composition để né giới hạn công cụ. Raster/sketch dùng SVG
text overlay riêng để đo; artwork không cần SVG marker.

Các nhãn `readability`, `wrapReview`, `artisticIntegration` là review bằng mắt,
không thay phép đo. Verifier không đọc ý nghĩa đoạn từ PDF; source reader phải
đối chiếu paragraph map. Schema 3 được giữ để truy vết nhưng không mở cổng duyệt.

## Đối chiếu trước cổng composition

Hiển thị PDF nguồn và composition trên cùng canvas, cùng scale xem, kèm bảng
font/leading/glyph/area và crop giao chữ–silhouette. Vị trí chữ được art-direct;
không coi đáy khối nguồn là tọa độ khóa. Nếu chữ gọn hơn, phải có phép đo chứng
minh burden và rhythm vẫn đúng, không chỉ giữ đủ số dòng.
