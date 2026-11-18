#!/usr/bin/env python3
"""Ghép prompt ttpq-comic: tự chèn khối STYLE, ảnh ref theo scene và điều cấm.

Agent chỉ viết phần cảnh (2–4 câu tiếng Anh) vào --body. Script lo phần
không được sai:
  - khối STYLE nguyên văn theo --style (không ghi: blend cho lượt màu và
    color-edit, light cho lượt nét và chỉnh outline): light (định nghĩa ở
    docs/style-ttpq-comic-light.md, khối nét ở style/ttpq-comic.md), soft
    (cả hai khối ở style/ttpq-comic-soft.md) hoặc blend (cả hai khối ở
    style/ttpq-comic-blend.md);
  - danh sách nhân vật lấy từ dòng **Profile:** của các cảnh Snn trong
    story/<tập>/scenes.md, mỗi người một dòng Image N kèm dòng prompt trong
    profile.md; số Image cố định theo thứ tự cast;
  - câu tương phản khi hai nhân vật trong "Cặp dễ nhầm" của bible.md cùng có mặt;
  - dòng Avoid từ "Cấm" của cảnh và "Avoid trong prompt" của bible.md, cộng thêm
    --avoid của lượt;
  - lượt màu thêm ánh sáng của cảnh từ "Thời điểm/ánh sáng" hoặc --light;
  - body ghi {slug} để script thay bằng số Image đúng theo cast;
  - lượt màu/color-edit dùng "Dòng nhận diện tiếng Anh" đầy đủ của profile;
    "Nét mặt cố định" (tiếng Anh) giữ biểu cảm theo sheet ở mọi lượt;
  - "Nét vẽ line art" (tiếng Anh, tùy chọn) chỉ chèn ở lượt nét và chỉnh outline:
    cách thể hiện dấu hiệu dễ sai khi chuyển sheet màu sang nét đen (râu, cổ y…);
  - --recast (lượt màu và chỉnh outline; chỉnh outline thêm câu chốt cuối prompt): nhân vật vẽ lại từ profile, ảnh
    nguồn chỉ giữ vị trí, dáng, cử chỉ, hướng nhìn;
  - --pass color-edit: sửa một nhân vật trên ảnh màu, giữ nguyên phần còn lại.

Thứ tự prompt: việc cần làm → cảnh (body) → nhân vật → STYLE → trang sách
(bleed, gáy; --across cho một vật đi liền qua gáy) → chữ → Avoid.
Body lượt màu bỏ dòng Text wrap; body lượt chỉnh
là các dòng "Change: …".

Ví dụ:
  python3 build-prompt.py --spread ttpq-comic/spreads/t53-part-1/p036-037 \\
      --scenes S12 S13 --pass outline --body prompts/v025-outline.body.txt \\
      --cast punna-vaddhana visakha godatta --no-ref gia-nhan-nha-visakha \\
      --out prompts/v025-outline.txt

Đường dẫn --body/--out tương đối được hiểu theo thư mục spread.
In danh sách ảnh cần đính kèm và cảnh báo; thoát 1 khi thiếu dữ kiện bắt buộc.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
FLOW = ROOT / "ttpq-comic"
# Mỗi style: (file định nghĩa, thứ tự khối text), (file LINE ART STAGE, thứ tự khối), câu mở lượt màu.
STYLES = {
    "light": {
        "name": "ttpq comic light",
        "def": (ROOT / "docs" / "style-ttpq-comic-light.md", 0),
        "line": (FLOW / "style" / "ttpq-comic.md", 0),
        "color_drop": "Color:",
        "color_open": "clean flat color shapes with 2–3 hard-edged cel-shading tones on skin and clothing; "
                      "keep every black outline crisp and visible; background in a few flat color planes.",
    },
    "soft": {
        "name": "ttpq comic soft",
        "def": (FLOW / "style" / "ttpq-comic-soft.md", 0),
        "line": (FLOW / "style" / "ttpq-comic-soft.md", 1),
        "color_drop": "Color and light:",
        "color_open": "a clear soft directional light with 3–4 gently blended shading tones on skin and clothing "
                      "and subtle gradients on sky and large surfaces; keep every black outline crisp and visible; "
                      "background in soft layered atmospheric depth, with characters crisper than the background.",
    },
    "blend": {
        "name": "ttpq comic blend",
        "def": (FLOW / "style" / "ttpq-comic-blend.md", 0),
        "line": (FLOW / "style" / "ttpq-comic-blend.md", 1),
        "color_drop": ("Color and light:", "Value and contrast:"),
        "color_open": "clean flat color shapes with 2–3 slightly softened cel-shading tones on skin and clothing, "
                      "under natural light suited to the scene's time and setting with a clear direction, no overall warm or golden cast unless the scene calls for it, cast shadows on the ground, deep colored shadow masses "
                      "in the environment and focal characters separated from their background by value; "
                      "keep every line clear and in place but recolor it: outer contours a very dark warm brown close to black at medium-light weight, never heavy pure black, "
                      "interior and background lines tinted a clearly darker shade of the color they sit on and still readable; "
                      "foreground and middle ground in flat color planes with only gentle color transitions, "
                      "distance and sky softly painted with subtle gradients and layered atmospheric depth, "
                      "never gradients on characters.",
    },
}


def rel(p):
    try:
        return Path(p).relative_to(ROOT)
    except ValueError:
        return p


def die(msg):
    print(f"LỖI: {msg}", file=sys.stderr)
    sys.exit(1)


def canvas_ref(spread, layout):
    """layout-ref-canvas.png: layout-ref đặt giữa canvas đúng khổ ảnh ra, hai bên là dải bleed xám nhạt.

    GPT trả ảnh 1536x1024 (tỷ lệ 1.5) trong khi spread có tỷ lệ 1.409; đưa ảnh
    layout cùng khổ để model không tự kéo giãn và tọa độ % khớp ảnh.
    """
    out = spread / "layout-ref-canvas-v003.png"  # v003: dải bleed xám trơn đậm, để trống; hậu kỳ tự nối nền
    if out.exists():
        return out
    from PIL import Image
    c = layout["canvas"]
    src = Image.open(spread / "layout-ref.png").convert("RGB")
    canvas = Image.new("RGB", (c["width"], c["height"]), (128, 128, 128))
    canvas.paste(src.resize((c["spreadWidthPx"], c["height"]), Image.LANCZOS), (c["trimEachSidePx"], 0))
    canvas.save(out)
    return out


def line_style(st):
    """Định nghĩa chuẩn bỏ đoạn màu (lượt nét chưa tô màu), rồi khối LINE ART STAGE."""
    paras = [x for x in re.split(r"\n\s*\n", text_block(*st["def"])) if not x.lstrip().startswith(st["color_drop"])]
    return "\n\n".join(paras + [text_block(*st["line"])])


def text_block(path, index=0):
    blocks = re.findall(r"```text\n(.*?)```", path.read_text(encoding="utf-8"), re.S)
    if len(blocks) <= index:
        die(f"không thấy khối ```text thứ {index + 1} trong {rel(path)}")
    return blocks[index].strip()


def join_names(xs):
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


STOP = {"a", "an", "the", "or", "and", "of", "on", "in", "at", "to", "any", "no", "with", "unless", "it", "its", "as", "from", "inside"}


def content_words(s):
    return [w for w in re.findall(r"[a-z]+", s.lower()) if w not in STOP]


def clean_avoid(raw, warnings):
    """Tách từng mục theo ';', bỏ trùng (không phân biệt hoa thường), bỏ mục nằm trọn trong mục khác,
    cảnh báo cặp mục gần trùng (chung cụm hai từ hoặc chung từ đầu) để người viết gộp lại."""
    items = [p.strip().rstrip(".;").strip() for x in raw for p in (x or "").split(";")]
    items = list({p.lower(): p for p in reversed([p for p in items if p])}.values())[::-1]
    norm = lambda s: " ".join(re.findall(r"[a-z0-9]+", s.lower()))
    items = [p for p in items
             if not any(q is not p and len(norm(q)) > len(norm(p)) and re.search(rf"\b{re.escape(norm(p))}\b", norm(q)) for q in items)]
    for i, p in enumerate(items):
        wp = content_words(p)
        for q in items[i + 1:]:
            wq = content_words(q)
            bigram = set(zip(wp, wp[1:])) & set(zip(wq, wq[1:]))
            if bigram or (wp and wq and wp[0] == wq[0]):
                warnings.append(f"Avoid có hai mục gần trùng: '{p}' ~ '{q}'; gộp thành một mục (sửa --avoid, Avoid của cảnh hoặc bible).")
    return items


def field(text, label):
    m = re.search(rf"^- {re.escape(label)}:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else None


def load_profile(token, warnings):
    slug, _, ref_override = token.partition(":")
    d = FLOW / "characters" / slug
    p = d / "profile.md"
    if not p.exists():
        die(f"không có profile {p.relative_to(ROOT)}")
    t = p.read_text(encoding="utf-8")
    status = field(t, "Trạng thái") or ""
    if not status.startswith("APPROVED"):
        warnings.append(f"{slug}: profile chưa APPROVED, cần người dùng duyệt.")
    name = field(t, "Tên trong prompt")
    line = field(t, "Dòng prompt")
    ref = ref_override or field(t, "Ref prompt")
    if not name or not line:
        die(f"{slug}: profile.md thiếu 'Tên trong prompt' hoặc 'Dòng prompt'")
    if not ref:
        refs = sorted(d.glob("ref-*.png"))
        if not refs:
            die(f"{slug}: không có ảnh ref")
        ref = refs[-1].name
    if not (d / ref).exists():
        die(f"{slug}: không có ảnh {ref}")
    # Dòng nhận diện tiếng Anh đầy đủ (mặt, da, màu trang phục) cho lượt màu; bỏ tiền tố "Tên (Image <N>):".
    idm = re.search(r"^## Dòng nhận diện tiếng Anh\s*\n+(?:```|~~~)text\n(.*?)(?:```|~~~)", t, re.M | re.S)
    idline = re.sub(r"^[^:;\n]{1,60}:\s*", "", idm.group(1).strip()).rstrip(".") if idm else None
    face = (field(t, "Nét mặt cố định") or "").rstrip(".") or None
    if face and re.search(r"[À-ỹ]", face):
        warnings.append(f"{slug}: 'Nét mặt cố định' phải viết tiếng Anh; bỏ qua.")
        face = None
    lineart = (field(t, "Nét vẽ line art") or "").rstrip(".") or None
    if lineart and re.search(r"[À-ỹ]", lineart):
        warnings.append(f"{slug}: 'Nét vẽ line art' phải viết tiếng Anh; bỏ qua.")
        lineart = None
    return {"slug": slug, "name": name, "line": line.rstrip("."), "id": idline, "face": face, "lineart": lineart,
            "ref": (d / ref).relative_to(ROOT)}


def load_scenes(story, ids, warnings):
    text = (story / "scenes.md").read_text(encoding="utf-8")
    out = []
    for sid in ids:
        m = re.search(rf"^### {sid} — (.*?)$(.*?)(?=^### S|\Z)", text, re.M | re.S)
        if not m:
            die(f"không thấy cảnh {sid} trong scenes.md")
        head, body = m.group(1), m.group(2)
        if "APPROVED" not in head and "**Duyệt theo phạm vi:** APPROVED" not in body:
            warnings.append(f"{sid} còn DRAFT; dùng khi người dùng đã duyệt cho spread này.")
        get = lambda k: (re.search(rf"^- \*\*{k}:\*\*\s*(.+)$", body, re.M) or [None, None])[1]
        prof = get("Profile")
        if prof is None:
            warnings.append(f"{sid} chưa có dòng **Profile:**; dùng --cast.")
        ban = get("Avoid")
        if ban is None and get("Cấm"):
            warnings.append(f"{sid} chỉ có **Cấm:** tiếng Việt, không chép vào prompt; thêm **Avoid:** tiếng Anh hoặc dùng --avoid nếu cần.")
        out.append({"id": sid, "light": get("Thời điểm/ánh sáng"), "ban": ban, "text": (head + body).lower(),
                    "cast": [s.strip() for s in (prof or "").split(",")
                             if s.strip() and s.strip() != "—"]})
    return out


def bible_parts(story):
    p = story / "bible.md"
    if not p.exists():
        return [], {}
    t = p.read_text(encoding="utf-8")

    def section(title):
        m = re.search(rf"^## {title}\n(.*?)(?=^## |\Z)", t, re.M | re.S)
        return m.group(1) if m else ""

    # Dòng có tiền tố "[khi: từ khóa, …]" chỉ chèn khi cảnh chứa một trong các từ khóa;
    # thêm "; trừ: từ khóa, …" để bỏ qua khi cảnh chứa một trong các từ khóa loại trừ.
    split = lambda s: [k.strip().lower() for k in s.split(",") if k.strip()]
    bans = []
    for line in re.findall(r"^- (.+)$", section("Avoid trong prompt"), re.M):
        m = re.match(r"\[khi:\s*([^\];]+)(?:;\s*trừ:\s*([^\]]+))?\]\s*(.+)$", line)
        bans.append((split(m.group(1)), split(m.group(2) or ""), m.group(3)) if m else ([], [], line))
    pairs = {}
    for a, b, s in re.findall(r"^- `?([\w-]+)`? \+ `?([\w-]+)`?:\s*(.+)$", section("Cặp dễ nhầm"), re.M):
        pairs[frozenset((a, b))] = s.strip()
    return bans, pairs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--spread", required=True)
    ap.add_argument("--scenes", nargs="+", required=True)
    ap.add_argument("--pass", dest="kind", choices=["outline", "color", "edit", "color-edit"], required=True,
                    help="edit = chỉnh outline; color-edit = chỉnh nhân vật trên ảnh màu đã có")
    ap.add_argument("--recast", nargs="+", default=[],
                    help="lượt màu hoặc chỉnh outline (--pass edit): nhân vật vẽ lại từ profile, ảnh nguồn chỉ giữ vị trí, dáng, cử chỉ, hướng nhìn, đạo cụ")
    ap.add_argument("--body", required=True, help="file chứa phần cảnh/comment agent viết")
    ap.add_argument("--style", choices=sorted(STYLES), help="style của lượt; mặc định blend cho lượt màu/color-edit, light cho lượt nét/chỉnh outline")
    ap.add_argument("--story", help="mặc định ttpq-comic/story/<tiền tố layout-slug>")
    ap.add_argument("--cast", nargs="+", help="thay danh sách Profile của cảnh (slug hoặc slug:ref.png)")
    ap.add_argument("--no-ref", nargs="+", default=[], help="nhân vật chỉ tả bằng chữ (xa, nhỏ)")
    ap.add_argument("--avoid", default="", help="điều cấm thêm của lượt (Không vẽ trong brief)")
    ap.add_argument("--light", help="ánh sáng riêng của spread (tiếng Anh), thay ánh sáng của cảnh ở lượt màu")
    ap.add_argument("--two-scenes", action="store_true", help="spread hai cảnh riêng: mỗi cảnh vẽ trọn trang mình tới gáy, không hòa, không dải trắng")
    ap.add_argument("--split", action="store_true", help="spread hai tranh tách nhau, giữa là dải giấy trắng ở gáy (cả ba lượt)")
    ap.add_argument("--across", help="vật (tiếng Anh) được vẽ liền qua gáy, ví dụ \"the long wooden beam\"; người vẫn ở trang của mình")
    ap.add_argument("--no-text", action="store_true", help="hình không có chữ")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    across = (a.across or "").strip().rstrip(".").strip()
    if across and a.split:
        die("--across không dùng chung với --split (dải giấy trắng ở gáy không cho vật nào đi qua)")
    if a.two_scenes and (across or a.split):
        die("--two-scenes không dùng chung với --across hoặc --split")
    # Từ 2026-11-16: lên màu mặc định blend; lượt nét và chỉnh outline mặc định light.
    a.style = a.style or ("blend" if a.kind in ("color", "color-edit") else "light")
    st = STYLES[a.style]
    spread = (ROOT / a.spread).resolve()
    layout = json.loads((spread / "layout.json").read_text(encoding="utf-8"))
    story = ROOT / a.story if a.story else FLOW / "story" / spread.parent.name.split("-")[0]
    warnings = []
    scenes = load_scenes(story, a.scenes, warnings)
    bans, pairs = bible_parts(story)

    tokens = a.cast or list(dict.fromkeys(s for sc in scenes for s in sc["cast"]))
    if not tokens and a.kind not in ("edit", "color-edit"):
        warnings.append("Không có nhân vật có profile trong cảnh.")
    no_ref = set(a.no_ref)
    cast = [load_profile(t, warnings) for t in tokens]
    with_ref = [c for c in cast if c["slug"] not in no_ref]
    text_only = [c for c in cast if c["slug"] in no_ref]
    # Cast của cả cảnh thường rộng hơn người có mặt trong spread; GPT cố đưa mọi ref vào hình.
    if not a.cast:
        if len(with_ref) > 3:
            die(f"cast lấy từ cả cảnh có {len(with_ref)} ảnh ref ({', '.join(c['slug'] for c in with_ref)}); "
                "chỉ định --cast đúng nhân vật có mặt trong spread")
        if tokens:
            warnings.append(f"Không có --cast; dùng cast của cảnh: {', '.join(tokens)}. Kiểm tra đúng người có mặt trong spread.")
    elif len(with_ref) > 3:
        warnings.append(f"{len(with_ref)} ảnh ref: GPT dễ lẫn nhân vật; nhân vật xa, nhỏ nên dùng --no-ref.")

    recast = list(dict.fromkeys(a.recast))
    if recast and a.kind not in ("color", "edit"):
        die("--recast chỉ dùng cho --pass color hoặc --pass edit; chỉnh từng nhân vật trên ảnh màu dùng --pass color-edit")
    bad = [s for s in recast if s not in {c["slug"] for c in with_ref}]
    if bad:
        die(f"--recast {', '.join(bad)} không có trong cast có ảnh ref")
    if len(recast) > 2:
        warnings.append(f"--recast {len(recast)} nhân vật: GPT dễ lẫn; nhân vật còn sai thì sửa từng người bằng --pass color-edit.")
    if a.kind == "color-edit":
        if not with_ref:
            die("--pass color-edit cần --cast gồm nhân vật bị sửa (có ảnh ref)")
        if len(with_ref) > 1:
            warnings.append(f"color-edit sửa {len(with_ref)} nhân vật một lượt; mỗi lượt một nhân vật giữ profile chắc hơn.")
    full_id = a.kind in ("color", "color-edit")
    if full_id:
        for c in with_ref:
            if not c["id"]:
                warnings.append(f"{c['slug']}: profile thiếu khối 'Dòng nhận diện tiếng Anh'; dùng Dòng prompt ngắn.")

    has_marks = any(par.get("marks") for pg in layout["pages"].values()
                    for b in pg.get("blocks", []) for par in b.get("paragraphs", []))
    def column(side, label):
        pg = layout["pages"].get(side) or {}
        box = pg.get("textBoxPt")
        if not box or not pg.get("lineCount"):
            return None
        c = layout["canvas"]
        s = c["spreadWidthPx"] / layout["spread"]["widthPt"]
        x0 = (c["trimEachSidePx"] + box[0] * s) / c["width"] * 100
        x1 = (c["trimEachSidePx"] + box[2] * s) / c["width"] * 100
        y0 = box[1] * s / c["height"] * 100
        return f"{label} column x {x0:.1f}–{x1:.1f}%, first line top at y {y0:.1f}%"

    cols = [x for x in (column("left", "left"), column("right", "right")) if x]
    # Lệnh cố định của người dùng chỉ khóa cỡ chữ và vị trí dòng đầu; mọi thứ khác
    # (độ dài dòng, ngắt dòng, số dòng, dáng khối) phải tự do để chữ ôm hình.
    # Chỉ giữ số đo cỡ chữ (nói "giữ cỡ chữ" thì GPT vẫn co chữ nhường chỗ tranh);
    # vị trí cột và dòng đầu để GPT bám Image 1, vì nó không đo tọa độ %.
    position = ""
    pgs = [p for p in layout["pages"].values() if p.get("sizePx") and p.get("leadingPx")]
    if cols:
        H = layout["canvas"]["height"]
        size = (f"letters about {max(p['sizePx'] for p in pgs) / H * 100:.1f}% of the image height, "
                f"one line every {max(p['leadingPx'] for p in pgs) / H * 100:.1f}%") if pgs else "as in Image 1"
        position = ("Text and picture interweave like an editorial illustrated book: parts of the picture rise into the text columns "
                    "and the lines reflow closely around them; the text is not an area the picture must avoid. "
                    "Only two things are fixed: the type size (" + size + ") and where the first line of each column starts, exactly as in Image 1. "
                    "Line length, line breaks and the number of lines follow the shapes of the picture, and a column may run longer downward. ")
    c_ = layout["canvas"]
    sc = c_["spreadWidthPx"] / layout["spread"]["widthPt"]
    left = layout["pages"]["left"]["folio"]["text"]
    right = layout["pages"]["right"]["folio"]["text"]
    w, h = layout["canvas"]["width"], layout["canvas"]["height"]
    pages = f"pages {left}–{right}"
    # Gáy: nền đi liền qua gáy; nhân vật không vượt gáy; mặt và tay chính cách gáy 30 pt (book-spec, phần cong vào gáy).
    g = c_["gutterXPx"] / w * 100
    gz = 30 * sc / w * 100
    mid = f"the middle {2 * gz:.0f}% of the width"
    body = (spread / a.body if not Path(a.body).is_absolute() else Path(a.body)).read_text(encoding="utf-8").strip()

    n0 = 2  # Image 1 luôn là layout / line art / outline
    # Body ghi {slug}; script thay bằng số Image đúng theo cast, tránh trỏ nhầm ảnh khi đổi thứ tự.
    ref_of = {c["slug"]: f"Image {n0 + i}" for i, c in enumerate(with_ref)}
    ref_of.update({c["slug"]: c["name"] for c in text_only})
    unknown = sorted(set(re.findall(r"\{([a-z0-9-]+)\}", body)) - set(ref_of))
    if unknown:
        die(f"body nhắc {', '.join('{' + u + '}' for u in unknown)} nhưng không có trong cast")
    if re.search(r"\bImage [2-9]\b", body):
        warnings.append("Body ghi cứng 'Image N'; dùng {slug} để script tự đánh số theo cast.")
    body = re.sub(r"\{([a-z0-9-]+)\}", lambda m: ref_of[m.group(1)], body)

    # Lượt chỉnh: phần đổi (Change:) và phần giữ (Keep:) tách khối riêng, theo guide GPT Image.
    keep_block = ""
    if a.kind in ("edit", "color-edit"):
        keeps = [m.strip().rstrip(".;") for m in re.findall(r"^Keep:\s*(.+)$", body, re.M)]
        body = "\n".join(l for l in body.splitlines() if not l.startswith("Keep:")).strip()
        if keeps:
            keep_block = "Keep unchanged: " + "; ".join(keeps) + "."
        changes = re.findall(r"^Change:(.*)$", body, re.M)
        if any(re.search(r"[.;]\s+(Preserve|Keep|Retain)\b", c) for c in changes):
            warnings.append("Dòng Change có câu giữ nguyên ('Preserve/Keep …'); tách thành dòng 'Keep: …' riêng.")
        if len(changes) >= 3:
            warnings.append(f"Lượt chỉnh có {len(changes)} dòng Change; mỗi lượt 1–2 thay đổi rồi soát ảnh sẽ chắc hơn.")
    if a.kind == "color-edit" and re.search(r"render the (whole |entire )?(illustration|image|picture)|\brestyle\b|in ttpq comic (blend|light|soft)", body, re.I):
        warnings.append("Body color-edit đòi vẽ lại style cả tranh, mâu thuẫn với 'giữ nguyên phần còn lại'; bỏ dòng đó "
                        "(script đã khóa finish theo Image 1). Muốn đổi style cả tranh thì chạy lại lượt màu.")

    if a.kind == "outline":
        if not re.search(r"^Mood:", body, re.M):
            warnings.append("Body lượt nét thiếu dòng 'Mood:' (template: STORY, từng trang kèm biểu cảm, Mood).")
        wrap = re.search(r"^Text wrap:(.*)$", body, re.M)
        if not a.no_text and not wrap:
            warnings.append("Body lượt nét thiếu dòng 'Text wrap:' (phần tranh nào vươn vào cột chữ, cạnh dòng nào).")
        if wrap and re.search(r"font|type size|first[- ]line|vietnamese|english|wide|plain black|highlight", wrap.group(1), re.I):
            warnings.append("Dòng 'Text wrap:' chỉ nói phần hình nào vươn vào cạnh dòng nào; cỡ chữ, dòng đầu, ngôn ngữ, màu chữ do script lo.")
        if len(body.splitlines()) < 3:
            warnings.append("Body lượt nét quá ngắn: cần câu STORY mở đầu và mỗi trang một câu có hành động chính, biểu cảm, hướng nhìn.")
    elif a.kind == "color":
        # Lượt màu không dựng lại bố cục: bỏ dòng Text wrap, nhắc nếu còn chỉ dẫn góc máy.
        body = "\n".join(l for l in body.splitlines() if not l.startswith("Text wrap:")).strip()
        if re.search(r"eye-level|worm's-eye|bird's-eye|\blens\b|wide-angle|close-up|low angle|high angle", body, re.I):
            warnings.append("Body lượt màu còn chỉ dẫn góc máy; lượt màu chỉ cần STORY, màu/ánh sáng từng trang và Mood.")
    elif a.kind == "edit":
        if not re.search(r"^Change:", body, re.M):
            warnings.append("Body lượt chỉnh nên là các dòng 'Change: …' (chỉ điều cần đổi), không chép lại cả cảnh.")
        if re.search(r"^(Left|Right) page:", body, re.M):
            warnings.append("Body lượt chỉnh có 'Left/Right page:' như lượt nét; GPT sẽ vẽ lại cả trang. Chỉ ghi điều cần đổi.")

    def desc(c):
        # Lượt màu dùng dòng nhận diện đầy đủ (có màu da, trang phục); lượt nét dùng dòng ngắn.
        s = (c["id"] if full_id and c["id"] else c["line"]) + "."
        # Lượt edit recast nhắc "In line art" ở câu chốt cuối prompt; không lặp ở dòng Image N.
        if not full_id and c["lineart"] and not (a.kind == "edit" and c["slug"] in recast):
            s += f" In line art: {c['lineart']}."
        return s + (f" Fixed face in every moment: {c['face']}." if c["face"] else "")

    img = [f"Image {n0 + i} = {c['name']}: {desc(c)}" for i, c in enumerate(with_ref)]
    txt = [f"{c['name'][0].upper()}{c['name'][1:]} (no reference image; same realistic human proportions as the other characters): {desc(c)}" for c in text_only]
    fixed = any(c["face"] for c in cast)
    expr = ("Expressions follow the moment, not the sheets, except a fixed face given below."
            if fixed else "Expressions follow the moment, not the sheets.")
    keep_act = "where each character stands, the pose and gesture, the gaze direction, the action, any held prop and the overlap with others"
    take_sheet = "the face, head shape, ears, hair and beard, skin tone, body build and proportions, and the costume with its colors"
    regrow = ("If the sheet's build is taller, broader or slimmer than the figure in Image 1, draw the sheet's build with the feet on the same ground line, "
              "and paint the background around the new silhouette to match its surroundings in Image 1.")
    # Một đoạn chung cho mọi nhân vật recast/sửa, không lặp nguyên văn từng người.
    def tagged(cs):
        return join_names([f"{c['name']} (Image {n0 + with_ref.index(c)})" for c in cs])
    rc = [c for c in with_ref if c["slug"] in recast]
    sheet = "the sheet" if len(rc) == 1 else "each sheet"
    recasts = [f"Recast {tagged(rc)}: ignore the face, head, ears, hair, beard, body proportions and costume lines drawn in Image 1. "
               f"Keep from Image 1 only {keep_act}; take {take_sheet} from {sheet}. {regrow}"] if rc else []
    # Lượt chỉnh outline: lệnh "giữ mọi thứ" của edit làm GPT chỉ sửa nhẹ mặt cũ; phải bảo xóa và vẽ lại cả đầu.
    keep_line = "where the head sits, the head turn, the gaze direction, the pose and gestures, any held prop and the overlap with others"
    recasts_line = [f"Recast {tagged(rc)}: erase and redraw the whole head, face, ears, hair or beard and neckline from {sheet}; "
                    f"ignore the face, head shape, ears, beard, body proportions and robe lines drawn in Image 1. "
                    f"Keep from Image 1 only {keep_line}; take the face, head shape, ears, hair and beard, body build and proportions, and the costume lines from {sheet}, drawn as clean black line art. "
                    "If the sheet's build is taller or broader than the figure in Image 1, draw the sheet's build with the feet on the same ground line "
                    "and redraw the background lines around the new silhouette."] if rc else []
    present = {c["slug"] for c in cast}
    contrast = [s[0].upper() + s[1:] for k, s in pairs.items() if k <= present]

    scene_text = " ".join(sc["text"] for sc in scenes)
    bible_bans = [b for keys, skip, b in bans
                  if (not keys or any(k in scene_text for k in keys)) and not any(k in scene_text for k in skip)]
    avoid = clean_avoid([a.avoid] + [sc["ban"] or "" for sc in scenes] + bible_bans, warnings)
    avoid_line = "Avoid: " + "; ".join(avoid) + "." if avoid else ""
    # GPT không có negative prompt thật: mỗi từ trong Avoid vẫn gợi ra đúng thứ đó.
    if len(avoid) > 7:
        warnings.append(f"Avoid có {len(avoid)} mục; điều muốn có nên viết thành câu khẳng định trong body, Avoid chỉ giữ lỗi model hay mắc thật.")

    parts = []
    # Thứ tự theo cách GPT đọc: việc cần làm và cảnh trước, rồi nhân vật, style, trang sách, chữ, Avoid.
    fold = (f"The center fold (book gutter) runs down the middle of the spread at x {g:.0f}%. The background continues across it,"
            " but each character stays wholly on its own page and may come close to the fold from its own side;"
            f" keep faces and the hands doing the key action out of {mid}.")
    if across:
        # Ngoại lệ theo spread: một vật (ví dụ thanh gỗ nhiều người khiêng) đi liền qua gáy; người vẫn không vượt gáy.
        fold = (f"The center fold (book gutter) runs down the middle of the spread at x {g:.0f}%. The background and {across} continue across it;"
                " each person stays wholly on their own page and may come close to the fold from their own side."
                f" Inside {mid}, {across} is a plain unbroken stretch: no hands, ropes, joints or faces there.")
    if a.split:
        fold = (f"The center fold (book gutter) runs down the middle of the spread at x {g:.0f}%. This spread holds two separate pictures,"
                f" one per page, with no frame lines: {mid} is a blank white paper band from top to bottom, and no background,"
                " body, robe or prop enters it.")
    if a.two_scenes:
        # Gáy bị đóng sách che: hai cảnh riêng không cần hòa; mỗi cảnh vẽ trọn trang mình tới sát gáy.
        fold = (f"The center fold (book gutter) runs down the middle of the spread at x {g:.0f}%. This spread holds two separate scenes,"
                " one per page: each scene's background fills its own page right up to the fold and stops there;"
                " the two backgrounds do not blend or continue into each other, and there is no white strip, gap or border at the fold."
                f" Each character stays wholly on its own page; keep faces and the hands doing the key action out of {mid}.")
    if a.kind == "outline":
        parts.append(f"Draw {pages} of an illustrated graphic novel about the life of the Buddha (ancient northern India) for adult and family readers as one {w}x{h} spread "
                     f"in \"{st['name']}\" refined editorial comic line art. Image 1 is the page layout.")
        parts.append(body)
        if img or txt:
            parts.append("\n".join(["Characters: match faces, hair and clothing to their profile sheets; body height and proportions follow the character lines below; ignore the sheets' poses, backgrounds and labels."] + img + txt + contrast))
        parts.append(line_style(st))
        frame = layout.get("frames") or []
        lay = "Page: keep the margins of Image 1."
        if any(f.get("fill") for f in frame):
            lay += " Its colored block only marks roughly where the picture goes, not its border; the picture may rise around the text."
        lay += (" The flat gray bands at the left and right edges of Image 1 are bleed: leave them completely empty, plain gray as in Image 1;"
                " the illustration stops at their inner edge, without a border line."
                " Keep faces, hands and the key action well inside the page, away from the gray bands;"
                " bodies, robes and background may run to the inner edge of the gray bands and be cut off there, like a full-bleed book page. "
                + fold)
        parts.append(lay)
        if a.no_text:
            parts.append("No text of any kind in the image.")
        else:
            parts.append(position
                         + "Left page uses the Vietnamese words of Image 1; right page is English placeholder text of similar length. "
                         + "Black text, no boxes; keep any colored highlight behind the text as in Image 1, following the reflowed lines; never over faces; no text on the center fold."
                         + (" Colored text in Image 1 is editor's marks only; draw it black." if has_marks else ""))
    elif a.kind == "color":
        open_ = f"Color Image 1, the line art of {pages}, in the style below: {st['color_open']} Any gray tones in Image 1 are not lighting; ignore them. Keep its composition, background and text."
        # Thêm 2026-11-17: lượt màu vẽ lại hình nên nhân vật hay lùn/hoạt hình hơn outline; khóa tỷ lệ theo nét.
        # Chỉ khóa tỷ lệ, không khóa cách tô ("color inside the lines / do not stylize" làm ảnh nhạt, mất bóng đổ).
        open_ += (" Keep every figure's height, head size, head-to-body ratio, face shape, eye size and turban or headdress size"
                  " as drawn in Image 1; do not enlarge heads or make figures cartoonish.")
        if recast:
            names = [c["name"] for c in with_ref if c["slug"] in recast]
            who = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]
            open_ += (f" Exception: {who} {'is' if len(names) == 1 else 'are'} recast from the profile sheets. For recast characters, Image 1 only directs the acting"
                      " (position, pose, gesture, gaze, action, props); faces, bodies and costumes are drawn fresh from the sheets, not from Image 1's lines,"
                      " still with realistic adult proportions (about 7 to 7.5 heads tall, natural head and eye size).")
        parts.append(open_)
        if a.light:
            light_line = f"Light: {a.light.strip().rstrip('.')}."
        else:
            light = " ".join(f"{sc['id']}: {sc['light']}" for sc in scenes if sc["light"])
            light_line = f"Scene light from the script: {light}" if light else ""
            if light and re.search(r"[À-ỹ]", light):
                warnings.append("Ánh sáng của cảnh là tiếng Việt nên không chèn; ghi ánh sáng tiếng Anh của spread bằng --light "
                                "(nhất là khi spread là hồi tưởng khác thời điểm cảnh).")
                light_line = ""
        parts.append(body + (f"\n{light_line}" if light_line else ""))
        if img or txt:
            parts.append("\n".join([f"Characters must match their profile sheets in face, hair and clothing colors; where Image 1 differs, follow the sheet. {expr} Ignore the sheets' poses, lighting and labels."] + img + txt + recasts + contrast))
        parts.append(text_block(*st["def"]))
        if a.split:
            parts.append("Image 1 has two separate pictures with a blank white paper band between them at the center fold: keep that band "
                         "plain white paper, unpainted, with no frame lines; the gray bleed bands at the outer edges also stay empty. "
                         "Each character stays in its own picture as in Image 1.")
        elif a.two_scenes:
            parts.append("Image 1 has two separate scenes, one per page. Paint each scene on its own page right up to the center fold;"
                         " the two backgrounds meet at the fold without blending into each other, with no white strip, gap or border there;"
                         " only the gray bleed bands at the outer edges stay empty. Each character stays on its own page as in Image 1.")
        else:
            parts.append("Paint across the center fold, transition included; only the gray bleed bands at the outer edges stay empty. "
                         "Each character stays on its own side of the fold as in Image 1."
                         + (f" {across[0].upper()}{across[1:]} runs unbroken across the fold as in Image 1." if across else ""))
        parts.append("No text of any kind in the image." if a.no_text else "Text: keep every word and line break of Image 1, crisp near-black; no new or colored text; keep any colored highlight behind the text as in Image 1. No text on the center fold.")
    elif a.kind == "color-edit":
        names = [c["name"] for c in with_ref]
        who = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]
        parts.append(f"Edit Image 1, the finished color illustration of {pages}. Correct only {who} and anything listed below; keep every other person, "
                     "the background, light, colors, line treatment and all text of Image 1 exactly as they are.")
        if body:
            parts.append(body)
        if keep_block:
            parts.append(keep_block)
        one = len(with_ref) == 1
        parts.append("\n".join([f"Redraw the corrected {'character' if one else 'characters'} to match {'the profile sheet' if one else 'their profile sheets'}; "
                                f"ignore the sheets' poses, lighting and labels. {expr}"]
                               + img
                               + [f"For {tagged(with_ref)}: keep from Image 1 {keep_act}; take {take_sheet} from {'the sheet' if one else 'each sheet'}. {regrow}"]
                               + contrast))
        parts.append(f"Style: paint the corrected character in the same \"{st['name']}\" finish as the rest of Image 1: the same outline color and weight, "
                     "cel-shading tones, light direction and shadow color; strictly 2D, no gradients or texture on the character.")
        parts.append(f"The character stays on its own page, with face and key hands out of {mid} around the center fold.")
        parts.append("No text of any kind in the image." if a.no_text else "Keep all text, folios and any highlight behind the text exactly as in Image 1; do not redraw any letters.")
    else:
        if recasts_line:
            parts.append(f"Edit Image 1, the clean outline of {pages}. Redraw the recast characters below and change what is listed; keep everything else in Image 1 unchanged.")
            if re.search(r"exactly the existing|same (location and )?\S*-?facing angle|only .{0,30}identity features", body, re.I):
                warnings.append("Body lượt chỉnh khóa cứng đầu/góc mặt ('exactly the existing', 'same angle', 'only identity features'); bỏ để --recast vẽ lại được cả đầu.")
        else:
            parts.append(f"Edit Image 1, the clean outline of {pages}. Change only what is listed below and keep everything else in Image 1 unchanged.")
        parts.append(body)
        if keep_block:
            parts.append(keep_block)
        if img:
            parts.append("\n".join(["Edited characters must match their profile sheets in face, hair and clothing; body proportions follow the character lines below, not the sheets' poses. Ignore the sheets' poses, framing and labels."] + img + recasts_line + contrast))
        parts.append(f"Style: the same \"{st['name']}\" line art as Image 1: clean black outlines with natural line weight; no color, no gray, no shading, no hatching, no sketchy lines.")
        if img:
            parts.append(f"Edited characters stay on their own page, with faces and key hands out of {mid} around the center fold.")
        if across:
            parts.append(f"{across[0].upper()}{across[1:]} may run unbroken across the center fold; no hands, ropes or joints on it within {mid}.")
        parts.append("Keep all text words, type size and first-line positions; only the lines beside the edited area may reflow to wrap around the new shapes, keeping any colored highlight behind them.")
    if avoid_line:
        parts.append(avoid_line)
    if a.kind == "edit" and recasts_line:
        # Đặt cuối prompt: lượt edit của GPT bám ảnh nguồn rất chặt, câu Recast ở giữa prompt
        # chỉ làm mặt cũ dịu đi (p206–207 v004). Câu chốt ở cuối đã đổi được cả đầu (v005).
        # Chi tiết riêng (râu, cổ áo…) lấy từ "Nét vẽ line art" của profile, không viết cứng ở đây.
        for i, c in enumerate(with_ref):
            if c["slug"] not in recast:
                continue
            final = (f"Final check for {c['name']} (Image {n0 + i}): this is a full replacement of the head and neckline, not a retouch. "
                     "The head, face, beard and collar lines drawn in Image 1 are wrong: erase them completely and draw a recognizably new head from the sheet, "
                     "even if the head silhouette changes, at the same place, head turn and gaze, with the same gestures. "
                     "Erase the old collar lines as well and draw the neckline and the robe or clothing edge at the neck as the sheet shows it, not as in Image 1.")
            if c["lineart"]:
                final += f" In line art: {c['lineart']}."
            final += " Keep every other person, all lettering and the scenery as they are."
            parts.append(final)

    out = spread / a.out if not Path(a.out).is_absolute() else Path(a.out)
    if out.exists():
        die(f"{rel(out)} đã có; dùng version mới")
    out.write_text("\n\n".join(parts) + "\n", encoding="utf-8")

    first = {"outline": canvas_ref(spread, layout) if a.kind == "outline" else None, "color": "<outline được chọn>", "edit": "<outline đang sửa>",
             "color-edit": "<ảnh màu đang sửa>"}[a.kind]
    first = rel(first) if isinstance(first, Path) else first
    print(f"Đã ghi {rel(out)} ({len(' '.join(parts).split())} từ, style {st['name']})")
    print("Đính kèm:")
    print(f"  Image 1 = {first}")
    for i, c in enumerate(with_ref):
        print(f"  Image {n0 + i} = {c['ref']}  ({c['name']})")
    for wmsg in warnings:
        print(f"CẢNH BÁO: {wmsg}")


if __name__ == "__main__":
    main()
