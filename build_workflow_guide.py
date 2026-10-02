from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path('/workspace')
OUT = ROOT / 'Huong-dan-thuc-hanh-workflow-ve-mot-hinh-truyen-tranh.docx'
EP = ROOT / 'Tap 53'

BLUE = '2E74B5'
DARK = '1F4D78'
INK = '17324D'
LIGHT = 'E8EEF5'
PALE = 'F4F6F9'
GREEN = 'E7F3EC'
GOLD = 'FFF4CE'
RED = 'FCE8E6'
MUTED = '5F6B76'


def set_cell_shading(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.find(qn('w:shd'))
    if shd is None:
        shd = OxmlElement('w:shd')
        tcPr.append(shd)
    shd.set(qn('w:fill'), fill)


def set_cell_margins(cell, top=100, start=120, bottom=100, end=120):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = tcPr.first_child_found_in('w:tcMar')
    if tcMar is None:
        tcMar = OxmlElement('w:tcMar')
        tcPr.append(tcMar)
    for m, v in [('top', top), ('start', start), ('bottom', bottom), ('end', end)]:
        node = tcMar.find(qn(f'w:{m}'))
        if node is None:
            node = OxmlElement(f'w:{m}')
            tcMar.append(node)
        node.set(qn('w:w'), str(v))
        node.set(qn('w:type'), 'dxa')


def set_repeat_table_header(row):
    trPr = row._tr.get_or_add_trPr()
    tblHeader = OxmlElement('w:tblHeader')
    tblHeader.set(qn('w:val'), 'true')
    trPr.append(tblHeader)


def set_table_widths(table, widths):
    table.autofit = False
    tblPr = table._tbl.tblPr
    tblW = tblPr.find(qn('w:tblW'))
    if tblW is None:
        tblW = OxmlElement('w:tblW')
        tblPr.append(tblW)
    total = sum(widths)
    tblW.set(qn('w:w'), str(total))
    tblW.set(qn('w:type'), 'dxa')
    tblInd = tblPr.find(qn('w:tblInd'))
    if tblInd is None:
        tblInd = OxmlElement('w:tblInd')
        tblPr.append(tblInd)
    tblInd.set(qn('w:w'), '120')
    tblInd.set(qn('w:type'), 'dxa')
    grid = table._tbl.tblGrid
    for child in list(grid):
        grid.remove(child)
    for w in widths:
        col = OxmlElement('w:gridCol')
        col.set(qn('w:w'), str(w))
        grid.append(col)
    for row in table.rows:
        for i, cell in enumerate(row.cells):
            tcPr = cell._tc.get_or_add_tcPr()
            tcW = tcPr.find(qn('w:tcW'))
            if tcW is None:
                tcW = OxmlElement('w:tcW')
                tcPr.append(tcW)
            tcW.set(qn('w:w'), str(widths[i]))
            tcW.set(qn('w:type'), 'dxa')
            set_cell_margins(cell)
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


def add_page_field(paragraph):
    paragraph.add_run('Trang ')
    run = paragraph.add_run()
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = 'PAGE'
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'end')
    run._r.extend([fldChar1, instrText, fldChar2])


def font_run(run, size=None, bold=None, color=None, italic=None):
    run.font.name = 'Calibri'
    run._element.get_or_add_rPr().rFonts.set(qn('w:ascii'), 'Calibri')
    run._element.get_or_add_rPr().rFonts.set(qn('w:hAnsi'), 'Calibri')
    if size: run.font.size = Pt(size)
    if bold is not None: run.bold = bold
    if italic is not None: run.italic = italic
    if color: run.font.color.rgb = RGBColor.from_string(color)


def add_numbering(doc):
    numbering = doc.part.numbering_part.element
    existing_abs = [int(x.get(qn('w:abstractNumId'))) for x in numbering.findall(qn('w:abstractNum'))]
    existing_num = [int(x.get(qn('w:numId'))) for x in numbering.findall(qn('w:num'))]
    abs_id = max(existing_abs, default=0) + 1
    num_id = max(existing_num, default=0) + 1
    abstract = OxmlElement('w:abstractNum')
    abstract.set(qn('w:abstractNumId'), str(abs_id))
    multi = OxmlElement('w:multiLevelType'); multi.set(qn('w:val'), 'singleLevel'); abstract.append(multi)
    lvl = OxmlElement('w:lvl'); lvl.set(qn('w:ilvl'), '0'); abstract.append(lvl)
    start = OxmlElement('w:start'); start.set(qn('w:val'), '1'); lvl.append(start)
    numFmt = OxmlElement('w:numFmt'); numFmt.set(qn('w:val'), 'decimal'); lvl.append(numFmt)
    lvlText = OxmlElement('w:lvlText'); lvlText.set(qn('w:val'), '%1.'); lvl.append(lvlText)
    suff = OxmlElement('w:suff'); suff.set(qn('w:val'), 'tab'); lvl.append(suff)
    pPr = OxmlElement('w:pPr')
    tabs = OxmlElement('w:tabs'); tab = OxmlElement('w:tab'); tab.set(qn('w:val'), 'num'); tab.set(qn('w:pos'), '540'); tabs.append(tab); pPr.append(tabs)
    ind = OxmlElement('w:ind'); ind.set(qn('w:left'), '540'); ind.set(qn('w:hanging'), '270'); pPr.append(ind)
    lvl.append(pPr)
    numbering.append(abstract)
    num = OxmlElement('w:num'); num.set(qn('w:numId'), str(num_id))
    absEl = OxmlElement('w:abstractNumId'); absEl.set(qn('w:val'), str(abs_id)); num.append(absEl)
    numbering.append(num)
    return num_id


def numbered(doc, text, num_id):
    p = doc.add_paragraph(style='Normal')
    p.paragraph_format.space_after = Pt(4)
    pPr = p._p.get_or_add_pPr()
    numPr = OxmlElement('w:numPr')
    ilvl = OxmlElement('w:ilvl'); ilvl.set(qn('w:val'), '0')
    numId = OxmlElement('w:numId'); numId.set(qn('w:val'), str(num_id))
    numPr.extend([ilvl, numId]); pPr.append(numPr)
    p.add_run(text)
    return p


def bullet(doc, text, level=0):
    p = doc.add_paragraph(style='List Bullet' if level == 0 else 'List Bullet 2')
    p.paragraph_format.space_after = Pt(3)
    p.add_run(text)
    return p


def callout(doc, label, text, fill=PALE):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    set_table_widths(t, [9360])
    set_cell_shading(t.cell(0, 0), fill)
    p = t.cell(0, 0).paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(label + ': '); font_run(r, bold=True, color=INK)
    p.add_run(text)
    set_repeat_table_header(t.rows[0])
    doc.add_paragraph().paragraph_format.space_after = Pt(0)


def table(doc, headers, rows, widths):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    set_table_widths(t, widths)
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]
        set_cell_shading(c, LIGHT)
        p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h); font_run(r, bold=True, color=INK)
    set_repeat_table_header(t.rows[0])
    for vals in rows:
        cells = t.add_row().cells
        for i, val in enumerate(vals):
            cells[i].text = val
            for p in cells[i].paragraphs:
                p.paragraph_format.space_after = Pt(0)
                for r in p.runs: font_run(r, size=9.5)
    set_table_widths(t, widths)
    doc.add_paragraph().paragraph_format.space_after = Pt(0)
    return t


def add_picture(doc, path, caption, width=6.25):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True
    shape = p.add_run().add_picture(str(path), width=Inches(width))
    shape._inline.docPr.set('descr', caption)
    shape._inline.docPr.set('title', caption.split(' — ', 1)[0])
    c = doc.add_paragraph(); c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c.paragraph_format.space_after = Pt(8)
    r = c.add_run(caption); font_run(r, size=9, italic=True, color=MUTED)


def keep_with_next(p):
    p.paragraph_format.keep_with_next = True


doc = Document()
sec = doc.sections[0]
sec.page_width = Inches(8.5); sec.page_height = Inches(11)
sec.top_margin = sec.bottom_margin = sec.left_margin = sec.right_margin = Inches(1)
sec.header_distance = sec.footer_distance = Inches(0.492)

# Compact reference guide preset, resolved explicitly.
styles = doc.styles
normal = styles['Normal']
normal.font.name = 'Calibri'; normal.font.size = Pt(11); normal.font.color.rgb = RGBColor.from_string('222222')
normal._element.rPr.rFonts.set(qn('w:ascii'), 'Calibri'); normal._element.rPr.rFonts.set(qn('w:hAnsi'), 'Calibri')
normal.paragraph_format.space_after = Pt(6); normal.paragraph_format.line_spacing = 1.25
for name, size, color, before, after in [
    ('Heading 1', 16, BLUE, 18, 10), ('Heading 2', 13, BLUE, 14, 7), ('Heading 3', 12, DARK, 10, 5)]:
    s = styles[name]; s.font.name = 'Calibri'; s.font.size = Pt(size); s.font.bold = True; s.font.color.rgb = RGBColor.from_string(color)
    s._element.rPr.rFonts.set(qn('w:ascii'), 'Calibri'); s._element.rPr.rFonts.set(qn('w:hAnsi'), 'Calibri')
    s.paragraph_format.space_before = Pt(before); s.paragraph_format.space_after = Pt(after); s.paragraph_format.keep_with_next = True
for name in ['List Bullet', 'List Bullet 2']:
    styles[name].font.name = 'Calibri'; styles[name].font.size = Pt(11)
    styles[name].paragraph_format.space_after = Pt(4); styles[name].paragraph_format.line_spacing = 1.25

caption_style = styles.add_style('Code Sample', WD_STYLE_TYPE.PARAGRAPH)
caption_style.font.name = 'Consolas'; caption_style.font.size = Pt(9); caption_style.font.color.rgb = RGBColor.from_string('263238')
caption_style.paragraph_format.left_indent = Inches(.25); caption_style.paragraph_format.right_indent = Inches(.15)
caption_style.paragraph_format.space_before = Pt(4); caption_style.paragraph_format.space_after = Pt(8); caption_style.paragraph_format.line_spacing = 1.1

header = sec.header.paragraphs[0]
header.text = 'SỔ TAY THỰC HÀNH • COMIC ILLUSTRATION WORKFLOW'
header.alignment = WD_ALIGN_PARAGRAPH.LEFT
for r in header.runs: font_run(r, size=8.5, bold=True, color=MUTED)
footer = sec.footer.paragraphs[0]
footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
add_page_field(footer)
for r in footer.runs: font_run(r, size=9, color=MUTED)

num_id = add_numbering(doc)

# Cover
p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(78); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('SỔ TAY THỰC HÀNH'); font_run(r, size=11, bold=True, color=BLUE)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(8)
r = p.add_run('Workflow vẽ một hình\ntruyện tranh 2D'); font_run(r, size=28, bold=True, color=INK)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_after = Pt(22)
r = p.add_run('Từ khóa nguồn → composition → prompt → tạo ảnh → QA → approved'); font_run(r, size=13, color=DARK)
callout(doc, 'Dành cho', 'Người mới tham gia dự án, người vận hành workflow và người duyệt hình. Có thể đọc từ đầu hoặc mở thẳng đến checklist ở cuối tài liệu.', GREEN)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.paragraph_format.space_before = Pt(25)
r = p.add_run('Ví dụ xuyên suốt: Tập 53 • Part 2 • Chương 5 • page 008'); font_run(r, size=11, bold=True, color=BLUE)
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run('Phiên bản tài liệu: 1.0 • 28/09/2026'); font_run(r, size=9.5, color=MUTED)
doc.add_page_break()

doc.add_heading('1. Đọc nhanh trước khi bắt đầu', level=1)
doc.add_paragraph('Mục tiêu của workflow là tạo ra một ảnh đúng nội dung, đúng profile, thuần 2D, đặt được vào layout và có lịch sử quyết định rõ ràng. Một ảnh đẹp nhưng sai thời điểm, sai nhân vật hoặc không đặt được vào khung vẫn là ảnh chưa đạt.')
callout(doc, 'Nguyên tắc quan trọng nhất', 'Mỗi tập là một đơn vị độc lập. Chỉ dùng notes, script, layout, profile và asset của đúng tập/part/page đang làm. Không lấy output cũ làm profile thay thế.', GOLD)

doc.add_heading('Sơ đồ 8 bước', level=2)
steps = [
    ('1. Khóa phạm vi', 'Xác định tập, part, page, frame và deliverable.'),
    ('2. Đọc nguồn', 'Tạo source snapshot; tách dữ kiện khỏi suy luận.'),
    ('3. Chọn hướng kể', 'Thiết kế 1–3 composition thực sự khác nhau.'),
    ('4. Chốt composition', 'Xác nhận focus, moment, camera, population và vùng an toàn.'),
    ('5. Viết prompt', 'Chuyển composition contract thành prompt kỹ thuật.'),
    ('6. Tạo ảnh', 'Đọc lại profile gốc; lưu output bằng version mới.'),
    ('7. QA', 'Visual QA trước; layout QA khi ảnh gắn layout.'),
    ('8. Bàn giao', 'Chỉ chuyển bản được chọn rõ vào approved/.'),
]
table(doc, ['Bước', 'Kết quả nhìn thấy'], steps, [2100, 7260])

doc.add_heading('Ba trạng thái kiểm tra', level=2)
table(doc, ['Trạng thái', 'Dùng khi'], [
    ('REQUIRED', 'Check bắt buộc; không đạt có thể làm deliverable FAIL.'),
    ('NOT_APPLICABLE', 'Check không liên quan đến loại hình đang làm.'),
    ('SKIPPED_BY_USER', 'Người dùng chủ động bỏ qua; phải ghi lý do và phạm vi.'),
], [2200, 7160])

doc.add_heading('Cấu trúc file cần nhớ', level=2)
for s in [
    'storyboards/: source snapshot, option, composition đã xác nhận và prompt.',
    'outputs/: mọi ảnh mới/variant; mỗi lần sửa là một version mới, không ghi đè.',
    'qa/: báo cáo QA, ảnh overlay và bằng chứng đặt layout.',
    'approved/: chỉ chứa bản cuối đã QA và được người dùng chọn đích danh.',
]: bullet(doc, s)

doc.add_page_break()
doc.add_heading('2. Chuẩn bị đầu vào', level=1)
doc.add_paragraph('Trước khi thiết kế, hãy kiểm tra đủ các nhóm nguồn dưới đây. Thiếu nguồn chỉ là blocker nếu deliverable thực sự phụ thuộc vào nguồn đó.')
table(doc, ['Nhóm nguồn', 'Cần kiểm tra', 'Không được làm'], [
    ('Phạm vi', 'Episode, Part, page, frame; toàn page hay một shot.', 'Đọc nhầm trang hoặc dùng dữ kiện của Part khác.'),
    ('Nội dung', 'notes.md, shot_notes.md, script và ngữ cảnh trước/sau.', 'Đưa sự kiện xảy ra sau vào shot hiện tại.'),
    ('Hình học', 'Layout gốc, contentFrame, chữ, gáy, trim, safe zone.', 'Tự coi mọi khối xanh là một frame độc lập.'),
    ('Nhận dạng', 'Profile gốc của đúng nhân vật trong characters/.', 'Dùng output cũ hoặc nhân vật khác làm identity source.'),
    ('Phong cách', 'Khóa thuần 2D và style reference đã approved nếu có.', 'Dùng 2.5D/CGI, soft airbrush, texture thật hoặc blur.'),
], [1500, 4020, 3840])

doc.add_heading('Mẫu khóa phạm vi', level=2)
p = doc.add_paragraph(style='Code Sample')
p.add_run('Target: Tập 53 / Part 2 / Chương 5 / page 008 / Hình 2 — Người lính hy vọng.\nDeliverable: ảnh minh họa hoàn chỉnh, đặt ở nửa phải vùng hình phía dưới; có visual QA và layout QA.\nNhịp page: Hình 1 tĩnh lặng tu tập → Hình 2 hy vọng kín đáo.\nChưa được phép: chuyển approved khi chưa chọn output cuối.')

doc.add_heading('Cổng xác nhận 1', level=2)
callout(doc, 'Dừng và xác nhận', 'Chỉ tiếp tục khi target đã rõ. Nếu thiếu đúng một trường ảnh hưởng đến kết quả, hỏi một câu ngắn thay vì yêu cầu người dùng tự tìm cấu trúc thư mục.', GOLD)

doc.add_heading('3. Bước 1 — Đọc và khóa nguồn', level=1)
doc.add_paragraph('Mục đích là tạo một source snapshot ngắn, đủ để người thiết kế không vô tình sáng tác trái nguồn. Snapshot phải phân biệt dữ kiện chắc chắn, hàm ý mạnh, điều chưa rõ và lựa chọn tạo hình chưa được duyệt.')
for text in [
    'Ghi nguồn đã đọc, gồm notes, shot_notes, script, layout và profile liên quan.',
    'Tóm tắt cảnh đang diễn ra, trạng thái vật lý, nhân vật, cảm xúc và ý nghĩa.',
    'Khóa những chi tiết xảy ra sau scene và bị cấm xuất hiện sớm.',
    'Ghi các điểm chưa rõ; không biến suy luận thành hard lock.',
]: numbered(doc, text, num_id)

doc.add_heading('Ví dụ page 008 — khóa nguồn', level=2)
doc.add_paragraph('Page 008 có hai hình trong nửa dưới spread. Hình 1 kể đời sống thanh tịnh của các tỳ-kheo bên hồ sen. Hình 2 kể niềm hy vọng kín đáo của người lính kỳ cựu khi nhìn vị tỳ-kheo giảng pháp. Nội dung page sau về vua Pasenadi, món nợ, tiền kiếp hoặc nghiệp báo bị cấm xuất hiện sớm.')
add_picture(doc, EP / 'Part 2/tmp/pdfs/page-008-source/spread-08.png', 'Hình 1 — Raster layout nguồn của Tập 53, Part 2, Chương 5, page 008. Vùng chữ ở trên phải được giữ nguyên; hai hình ánh xạ vào hai nửa phía dưới.')

doc.add_page_break()
doc.add_heading('4. Bước 2 — Thiết kế shot và composition', level=1)
doc.add_paragraph('Thiết kế theo thứ tự: ý nghĩa kịch bản → trải nghiệm người đọc → bằng chứng thị giác → camera/bố cục → số người. Mỗi ảnh chỉ có một khoảnh khắc và một focus thị giác chính.')
table(doc, ['Thành phần', 'Câu hỏi phải trả lời'], [
    ('Focus', 'Người đọc nhìn thấy điều gì trước? Cá nhân, quan hệ, tập thể hay không gian?'),
    ('Moment', 'Đúng khoảnh khắc nào? Trước, đang hay sau hành động?'),
    ('Camera', 'Cự ly, độ cao, góc nhìn và hướng đọc phục vụ ý nghĩa gì?'),
    ('Population', 'Cần bao nhiêu lớp người để chứng minh quy mô? Không khóa số tùy ý.'),
    ('Evidence', 'Đạo cụ, tiếp xúc tay–vật, dấu vết và quan hệ nào bắt buộc phải đọc được?'),
    ('Layout', 'Gáy, chữ, trim/safe zone và crop chủ ý ảnh hưởng focus thế nào?'),
], [1800, 7560])
callout(doc, 'Khi có nhiều hướng', 'Chỉ đưa 2–3 phương án khác nhau đáng kể. Mỗi phương án nêu kết quả và đánh đổi trong một dòng; đánh dấu một phương án đề xuất dựa trên nguồn.', GREEN)

doc.add_heading('Composition contract tối thiểu', level=2)
for s in ['Focus và moment', 'Camera/framing', 'Đường đọc và phân lớp', 'Population plan', 'Required complete / required readable / optional support / out of frame', 'Crop chủ ý và vùng an toàn', 'Điều cấm theo nguồn']: bullet(doc, s)

doc.add_heading('Ví dụ page 008 — composition contract', level=2)
doc.add_paragraph('Option 3 được chọn để tạo nhịp: tĩnh lặng tu tập → cộng đồng nghe pháp → hy vọng kín đáo. Với Hình 2, camera qua vai ba phần tư sau của người lính; vị tỳ-kheo và nhóm cư sĩ ở trung cảnh. Vai người lính tạo frame-within-frame, còn eyeline của người lính và cư sĩ hội tụ vào vị giảng sư.')
table(doc, ['Ưu tiên', 'Khóa cụ thể của Hình 2'], [
    ('Required complete', 'Đôi tay chắp của người lính; cử chỉ giảng của vị tỳ-kheo.'),
    ('Required readable', 'Khăn xếp đỏ, giáp nâu; đầu cạo/cà-sa nâu; nhóm cư sĩ lắng nghe.'),
    ('Intentional crop', 'Khuôn mặt người lính có thể ngoài khung vì shot qua vai; không dùng mặt làm profile check.'),
    ('Out of frame', 'Vua Pasenadi, biểu tượng món nợ, tiền kiếp hoặc nghiệp báo của page sau.'),
], [2100, 7260])

doc.add_page_break()
doc.add_heading('5. Bước 3 — Chốt composition và viết prompt', level=1)
doc.add_paragraph('Khi người dùng chọn rõ một composition, lựa chọn đó khóa hướng kể hình và cho phép chạy liền mạch qua viết prompt, tạo ảnh và QA. Không hỏi lại một cổng duyệt prompt trong luồng mặc định.')

doc.add_heading('Prompt phải có', level=2)
table(doc, ['Khối', 'Nội dung'], [
    ('Primary request', 'Một câu nêu scene, moment và focus.'),
    ('Composition/framing', 'Tỷ lệ, camera, đường đọc, phân lớp, vùng gáy/safe zone.'),
    ('Population', 'Mật độ, vai trò từng nhóm, mức đọc của lớp xa.'),
    ('Characters', 'Profile nào áp dụng cho ai; chống nhân bản và drift.'),
    ('Scene/backdrop', 'Địa điểm, trạng thái vật lý và chi tiết cấm xuất hiện.'),
    ('Style/medium', 'Line art, flat fills, 1–2 cấp hard cel-shading, background đồng ngôn ngữ.'),
    ('Constraints/Avoid', 'Text, watermark, anatomy lỗi, CGI/2.5D, blur, chi tiết sai nguồn.'),
], [1900, 7460])

doc.add_heading('Đoạn prompt mẫu rút gọn — page 008, Hình 2', level=2)
p = doc.add_paragraph(style='Code Sample')
p.add_run('Tạo một shot ngoài trời tại Ấn Độ cổ đại khoảng thế kỷ 5 TCN. Góc nhìn qua vai ba phần tư sau của người lính kỳ cựu đang đứng cách xa, hai tay chắp, hướng về một vị tỳ-kheo đang giảng cho nhóm cư sĩ ở trung cảnh. Vị giảng sư là focus; vai người lính tạo frame-within-frame và eyeline hội tụ vào vị tỳ-kheo. Giữ khăn xếp đỏ đính ngọc/huy hiệu vàng, tóc/râu đen, giáp nâu và y phục đỏ–vàng của người lính; vị tỳ-kheo đầu cạo, cà-sa nâu. Thuần 2D animation, line art sạch, flat fills, 1–2 cấp hard cel-shading. Không biến thành cuộc trò chuyện giữa hai thị vệ; không có vua Pasenadi, món nợ, tiền kiếp, nghiệp báo, CGI, blur, chữ hoặc watermark.')
callout(doc, 'Profile refresh gate', 'Ngay trước mỗi lượt tạo/chỉnh có nhân vật, phải mở lại profile gốc từ filesystem và truyền đúng reference trong chính lượt đó. Ảnh composition chỉ điều khiển bố cục, không điều khiển identity.', RED)

doc.add_heading('6. Bước 4 — Tạo ảnh và quản lý version', level=1)
for text in [
    'Đọc lại profile gốc và kiểm vai trò của từng ảnh tham chiếu.',
    'Tạo từng shot/variant riêng; lưu trong outputs/ của đúng page.',
    'Đặt tên có page, option, mô tả ngắn và version; tuyệt đối không ghi đè.',
    'Nếu sửa ảnh, mô tả delta cần đổi và phần phải giữ nguyên.',
    'Không tự đánh dấu QA PASS và không chuyển approved/ ở bước này.',
]: numbered(doc, text, num_id)

doc.add_heading('Quy ước tên file gợi ý', level=2)
p = doc.add_paragraph(style='Code Sample')
p.add_run('page008-option3-hinh1-thien-ho-sen-v1.png\npage008-option3-hinh2-nguoi-linh-hy-vong-v1.png\npage008-option3-hinh2-nguoi-linh-hy-vong-v2.png  (nếu cần sửa)')
doc.add_paragraph('Trong ví dụ thực tế, hai hình được tạo thành hai output riêng. Trước Hình 2, workflow đọc lại đồng thời profile “Người lính kì cựu.png” và “Nhóm 60 tỳ kheo.png”; mỗi profile chỉ điều khiển đúng nhân vật tương ứng.')
add_picture(doc, EP / 'Part 2/pages/page-008/outputs/page008-option3-hinh2-nguoi-linh-hy-vong-v1.png', 'Hình 2 — Output Hình 2 v1: vị tỳ-kheo là focus; người lính qua vai là framing và điểm cảm xúc phụ.')

doc.add_page_break()
doc.add_heading('7. Bước 5 — Visual QA', level=1)
doc.add_paragraph('Visual QA chỉ tin vào điều nhìn thấy trong output và nguồn gốc; không lấy prompt làm bằng chứng. Kiểm tra theo đúng thứ tự dưới đây để tránh một ảnh “đẹp” che lấp lỗi quan trọng hơn.')
table(doc, ['Thứ tự', 'Check', 'Tiêu chí thực tế'], [
    ('1', 'Focus', 'Điểm nhìn chính có đúng ý nghĩa và khoảnh khắc không?'),
    ('2', 'Profile', 'Gương mặt, tóc, y phục, tỷ lệ và silhouette có đúng profile gốc?'),
    ('3', 'Thuần 2D', 'Line art rõ, flat fills, hard cel-shading; không CGI/blur/texture thật.'),
    ('4', 'Context', 'Đúng thời điểm, đạo cụ, hành động và hệ quả kịch bản?'),
    ('5', 'Location', 'Đúng địa hình/kiến trúc; không thêm landmark sai nguồn?'),
    ('6', 'Anatomy', 'Tay–vật tiếp xúc thật; không thừa/thiếu chi hoặc tỷ lệ sai?'),
    ('7', 'Storytelling', 'Bằng chứng thị giác có kể được điều cần kể ở kích thước sử dụng?'),
], [900, 1700, 6760])
callout(doc, 'Quy tắc kết luận', 'Mỗi check là PASS, FAIL, NOT_APPLICABLE hoặc SKIPPED_BY_USER. “Không chắc” đối với check REQUIRED được tính là FAIL.', GOLD)

doc.add_heading('8. Bước 6 — Layout QA', level=1)
doc.add_paragraph('Chỉ chạy khi ảnh gắn với layout. Overlay phải được tạo trên chính raster layout gốc có chữ; nền trắng thay thế không đủ làm bằng chứng.')
for s in [
    'Ảnh phủ đúng contentFrame, đúng tỷ lệ và không hở mép.',
    'Text không bị che; mask/crop hoạt động như thiết kế.',
    'Focus, mặt, tay, đạo cụ và hành động chính nằm trong vùng an toàn.',
    'Gáy không cắt chi tiết quan trọng nếu check này REQUIRED.',
    'Trim/safe zone dùng tỷ lệ chuẩn hóa phù hợp canvas, không áp số pixel cứng.',
]: bullet(doc, s)
add_picture(doc, EP / 'Part 2/pages/page-008/qa/page008-option3-v1-layout-overlay.png', 'Hình 3 — Overlay QA của option 3 v1 trên chính layout gốc có chữ; hai hình khớp frame, giữ text reserve, critical-safe và vùng gáy.')

doc.add_page_break()
doc.add_heading('9. Bước 7 — Xử lý kết quả QA', level=1)
doc.add_paragraph('Sau QA, không bắt người dùng tự đọc báo cáo dài để đoán bước tiếp theo. Hiển thị output/overlay, tóm tắt tác động nhìn thấy và đưa lựa chọn cụ thể.')
table(doc, ['Tình huống', 'Cách xử lý'], [
    ('PASS', 'Đề nghị giữ bản hiện tại hoặc tạo variant nếu có mục tiêu rõ.'),
    ('FAIL có thể sửa cục bộ', 'Tạo version mới; mô tả phần đổi và phần phải giữ.'),
    ('FAIL làm thay đổi hướng kể', 'Quay lại composition; không vá prompt để che lỗi nền tảng.'),
    ('Thiếu dữ liệu layout', 'Nêu đúng dữ liệu còn thiếu; không tuyên bố layout QA hoàn tất.'),
], [2600, 6760])

doc.add_heading('Mẫu câu cho người duyệt', level=2)
p = doc.add_paragraph(style='Code Sample')
p.add_run('Chọn output Hình 2: page008-option3-hinh2-nguoi-linh-hy-vong-v1.png\n\nChỉnh output Hình 2: giữ shot qua vai, eyeline và profile; sửa <nội dung cụ thể>\n\nTạo variant Hình 2: giữ focus vị giảng sư; thử khoảng cách người lính xa hơn một nhịp.')

doc.add_heading('10. Bước 8 — Chọn và bàn giao bản cuối', level=1)
doc.add_paragraph('Chỉ bàn giao khi output tồn tại, visual QA bắt buộc đã PASS, layout QA đã PASS/NOT_APPLICABLE hoặc được ghi SKIPPED_BY_USER, và người dùng đã chọn đúng filename/version.')
for text in [
    'Xác nhận chính xác output được chọn khi còn nhiều ứng viên.',
    'Chuyển file từ outputs/ sang approved/; giữ tên version.',
    'Nếu file đích đã tồn tại, tạo version mới — không ghi đè.',
    'Cập nhật manifest và mọi đường dẫn tiêu thụ.',
    'Không để hai bản sao cùng đóng vai trò nguồn chuẩn.',
]: numbered(doc, text, num_id)
callout(doc, 'Lưu ý', 'Câu “ổn” hoặc “tiếp tục” không đủ để suy ra phê duyệt cuối nếu vẫn còn nhiều output ứng viên.', RED)

doc.add_page_break()
doc.add_heading('11. Ca mẫu xuyên suốt — Part 2, Chương 5, page 008', level=1)
table(doc, ['Giai đoạn', 'Quyết định/đầu ra thực tế'], [
    ('Phạm vi', 'Tập 53, Part 2, Chương 5, page 008; hai hình ở nửa dưới spread.'),
    ('Nhịp page', 'Tĩnh lặng tu tập → cộng đồng nghe pháp → hy vọng kín đáo của người lính.'),
    ('Hình 1', 'Hoa sen dẫn mắt tới 3–5 tỳ-kheo thiền; thêm dáng người giản lược phía sau.'),
    ('Hình 2', 'Qua vai người lính; vị tỳ-kheo là focus; eyeline hội tụ vào người giảng.'),
    ('Profile', 'Nhóm 60 tỳ kheo; Người lính kì cựu. Đọc lại ngay trước generation.'),
    ('Output', 'Hai file v1 riêng trong outputs/; không ghi đè và chưa vào approved/.'),
    ('Visual QA', 'PASS cả hai hình: focus, profile, 2D, context/location, anatomy, storytelling.'),
    ('Layout QA', 'PASS: 21 check, 0 fail/warning/skipped; lệch tỷ lệ 1,56% trong dung sai 2%.'),
    ('Khóa nội dung', 'Không có vua Pasenadi, món nợ, tiền kiếp, nghiệp báo hoặc chữ phát sinh.'),
    ('Trạng thái', 'qa-passed; vẫn cần người dùng chọn rõ output trước khi chuyển approved/.'),
], [1900, 7460])

doc.add_heading('Điều ví dụ này dạy', level=2)
for s in [
    'Một page có thể gồm nhiều hình: mỗi hình có focus riêng nhưng phải cùng phục vụ nhịp trang.',
    'Intentional crop qua vai khiến khuôn mặt người lính không phải check profile bắt buộc; khăn, giáp, tóc/râu và silhouette vẫn phải đúng.',
    'Hai profile được truyền đúng vai trò; cư sĩ không được mượn dấu hiệu đặc trưng của người lính.',
    'Mỗi hình phải vượt visual QA riêng, sau đó cả hai được kiểm trong cùng layout.',
    'PASS kỹ thuật không tự động đồng nghĩa approved; quyền chọn cuối thuộc người dùng.',
]: bullet(doc, s)

doc.add_heading('12. Checklist thao tác nhanh', level=1)
checks = [
    ('Trước thiết kế', ['Đúng tập/part/page/frame', 'Đã đọc notes + shot_notes + script', 'Đã xem layout và profile gốc']),
    ('Trước tạo ảnh', ['Composition đã chọn rõ', 'Prompt không đổi shot đã duyệt', 'Profile gốc vừa được đọc lại', 'Đường dẫn output/version mới']),
    ('Trước kết luận QA', ['Đã xem ảnh ở kích thước sử dụng', 'Visual QA đủ trạng thái', 'Overlay dùng raster layout gốc nếu áp dụng']),
    ('Trước approved', ['Đúng filename được chọn', 'QA bắt buộc đã PASS', 'Không ghi đè', 'Manifest/đường dẫn đã cập nhật']),
]
for title, items in checks:
    p = doc.add_paragraph(); keep_with_next(p)
    r = p.add_run(title); font_run(r, bold=True, color=INK)
    for item in items: bullet(doc, '☐ ' + item)

doc.add_heading('Bảng lỗi thường gặp', level=2)
table(doc, ['Lỗi', 'Dấu hiệu', 'Cách sửa đúng tầng'], [
    ('Sai thời điểm', 'Nhân vật/đạo cụ của cảnh sau xuất hiện sớm.', 'Quay lại source snapshot và khóa timeline.'),
    ('Sai profile', 'Mặt/tóc/y phục drift hoặc nhân vật bị nhân bản.', 'Đọc lại profile gốc, tạo version mới.'),
    ('Sai phong cách', 'Soft shading, CGI, blur, texture thật.', 'Sửa prompt style/avoid và tái tạo; không “lọc màu” chữa cháy.'),
    ('Mất ý nghĩa', 'Ảnh đông nhưng không đọc được hành động/quan hệ.', 'Quay lại composition và evidence plan.'),
    ('Không đặt layout', 'Focus vào gáy, chữ bị che, hở khung.', 'Sửa framing/canvas; chạy lại layout QA.'),
    ('Ghi đè lịch sử', 'Không còn phân biệt v1/v2/v3.', 'Khôi phục versioning; mọi sửa đổi sinh file mới.'),
], [1800, 3500, 4060])

doc.add_heading('13. Mẫu ghi chép dùng lại', level=1)
for title, content in [
    ('A. Source snapshot', 'Target:\nNguồn đã đọc:\nDữ kiện xác nhận:\nHàm ý mạnh:\nPhần chưa rõ:\nChi tiết cảnh sau bị cấm:\nProfile/layout liên quan:'),
    ('B. Composition contract', 'Focus + moment:\nCamera/framing:\nĐường đọc + phân lớp:\nPopulation plan:\nRequired complete:\nRequired readable:\nOptional support:\nOut of frame:\nCrop/safe zone/gáy:'),
    ('C. Nhật ký tạo ảnh', 'Output/version:\nProfile vừa refresh:\nReference mapping:\nYêu cầu thay đổi:\nPhần phải giữ:\nOverride/SKIPPED_BY_USER:'),
    ('D. Kết luận QA', 'Visual QA: PASS/FAIL\nLayout QA: PASS/FAIL/NOT_APPLICABLE\nLỗi nhìn thấy:\nTác động:\nBước sửa đề xuất:\nOutput đang là ứng viên:'),
]:
    doc.add_heading(title, level=2)
    p = doc.add_paragraph(style='Code Sample'); p.add_run(content)

doc.add_heading('14. Thuật ngữ ngắn', level=1)
table(doc, ['Thuật ngữ', 'Hiểu đơn giản'], [
    ('Source snapshot', 'Bản khóa nguồn ngắn trước khi thiết kế.'),
    ('Composition contract', 'Cam kết về focus, moment, camera, population và vùng an toàn.'),
    ('Profile', 'Nguồn nhận dạng gốc của nhân vật.'),
    ('Output', 'Ảnh đang trong quá trình làm/chọn; chưa phải bản chuẩn cuối.'),
    ('Overlay', 'Ảnh QA đặt artwork lên layout gốc cùng guide hình học.'),
    ('Approved', 'Bản cuối đã QA và được người dùng chọn rõ.'),
    ('Drift', 'Sai lệch dần khỏi profile, bối cảnh hoặc phong cách đã khóa.'),
], [2100, 7260])

doc.add_paragraph()
callout(doc, 'Kết quả mong đợi', 'Một người mới có thể nhìn cấu trúc thư mục, đi qua từng cổng quyết định, biết khi nào được tiếp tục, biết phải lưu artifact nào và không tự ý phê duyệt output.', GREEN)

# Document properties
doc.core_properties.title = 'Sổ tay thực hành workflow vẽ một hình truyện tranh 2D'
doc.core_properties.subject = 'Hướng dẫn từng bước kèm ví dụ Tập 53, Part 2, Chương 5, page 008'
doc.core_properties.author = 'Comic Illustration Project'
doc.core_properties.keywords = 'comic, workflow, 2D, storyboard, prompt, QA, layout'

doc.save(OUT)
print(OUT)
