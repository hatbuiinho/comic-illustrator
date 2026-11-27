#!/usr/bin/env python3
"""Ghép prompt ttpq-comic: tự chèn khối STYLE, ảnh ref theo scene và điều cấm.

Agent chỉ viết phần cảnh (2–4 câu tiếng Anh) vào --body. Script lo phần
không được sai:
  - khối STYLE nguyên văn theo --style ở lượt màu (không ghi: blend, kể cả
    --recast, từ 2026-11-25); lượt nét không chèn khối STYLE, chỉ gọi tên
    Semi-Realistic Storybook Illustration ở câu mở, chỉnh outline gọi cùng tên
    đó (từ 2026-11-24); color-edit và swap không gọi tên style, finish theo
    ảnh đang sửa (từ 2026-11-25); các lượt này bỏ qua --style. Style: blend (docs/style-ttpq-comic-blend.md), storybook hoặc real
    (style/ttpq-*.md); light và soft đã bỏ từ 2026-11-25;
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
  - lượt nét (từ 2026-11-22) và chỉnh outline (từ 2026-11-24) lọc cụm
    "about N heads tall" khỏi dòng prompt và bỏ câu tỷ lệ chung;
  - "Nét vẽ line art" (tiếng Anh, tùy chọn) chèn ở lượt nét và chỉnh outline
    (lượt nét chèn lại từ 2026-11-22, sau lỗi râu quai nón p048-049 v066/v067):
    cách thể hiện dấu hiệu dễ sai khi chuyển sheet màu sang nét đen (râu, cổ y…);
  - --recast (chỉ lượt màu; từ 2026-11-25 bỏ ở chỉnh outline, thay bằng swap):
    nhân vật vẽ lại từ profile, ảnh nguồn chỉ giữ vị trí, dáng, cử chỉ, hướng nhìn;
  - --pass color-edit: chỉ sửa các dòng Change: trên một nhân vật của ảnh màu,
    sheet là nguồn cho chi tiết được sửa; phần còn lại giữ nguyên (từ 2026-11-25
    không còn recast cả người; thay cả người dùng swap);
  - --pass swap (từ 2026-11-24): thay một nhân vật trong ảnh có sẵn bằng nhân vật
    trong ảnh ref, theo prompt ngắn người dùng kiểm chứng: Image 1 = ref identity,
    Image 2 = ảnh cảnh; chỉ cần --cast <slug> và --target (người cần thay, tả
    theo vị trí); không chèn dòng nhận diện, STYLE, Avoid của cảnh; từ 2026-11-25
    thêm câu SCALE: cả khối đầu thật người cũ trong Image 2 (cao, ngang mặt, tai,
    cằm, khoảng cổ; trang sức theo cỡ cảnh) là mốc scale, thân dựng theo tỷ
    lệ đầu-thân và vóc dáng của Image 1, khăn/mũ được cao hơn đầu cũ; khối
    FINISH (từ 2026-11-25): cách vẽ theo Image 2, Image 1 chỉ cho identity;
  - --pass pose (từ 2026-11-27, sau lỗi đầu to khi xoay bà Matika p196-197 v029
    viết tay): đổi tư thế, hướng xoay hoặc vị trí của một nhân vật trên ảnh màu
    theo dòng Change:; Image 1 = ảnh màu, Image 2 = sheet. Script chèn khối SCALE
    lấy chính nhân vật trong Image 1 làm mốc (khối đầu kể cả búi/khăn, vai, chiều
    cao, đường đất), tỷ lệ từ hình toàn thân của sheet, chân dung chỉ cho nét mặt,
    cấm tỷ lệ chibi; khối FINISH theo Image 1; nền lộ ra quanh dáng cũ vẽ lại;
  - --effect (lượt màu và color-edit): ngoại lệ cho vùng hiệu ứng thần thông,
    nới gradient/glow chỉ trong vùng đó, sửa Exclusions và bỏ mục Avoid cấm
    glow/magic effect cho lượt này; không ghi thì style giữ nguyên.

Thứ tự prompt: việc cần làm → cảnh (body) → nhân vật → STYLE → trang sách
(bleed, gáy; --across cho một vật đi liền qua gáy) → chữ → Avoid.
Với --effect, đoạn Supernatural effect đứng ngay sau STYLE.
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
# Lượt nét (từ 2026-11-22): chỉ gọi tên style này ở câu mở, không chèn định nghĩa, không rule head tall; vẫn chèn "Nét vẽ line art" của profile.
# Chỉnh outline (từ 2026-11-24) gọi cùng tên này để đồng nhất với lượt nét.
OUTLINE_STYLE = "Semi-Realistic Storybook Illustration"
PHOTO_WORDS = re.compile(r"\b(?:photo\w*|camera lens|lens(?:es)?|\d+\s?mm|bokeh|depth of field|f-?stop|f/\d+(?:\.\d+)?|shutter|aperture)\b", re.I)
HEADS_TALL = re.compile(r",?\s*(?:about|around|roughly|nearly)?\s*\d+(?:\.\d+)?(?:\s*(?:to|–|-)\s*\d+(?:\.\d+)?)?\s*heads?\s+(?:tall|high)\b", re.I)
# Mỗi style: (file định nghĩa, thứ tự khối text), câu mở lượt màu. Lượt nét không chèn khối style (từ 2026-11-19).
STYLES = {
    "blend": {
        "name": "ttpq comic blend",
        "def": (ROOT / "docs" / "style-ttpq-comic-blend.md", 0),
        "color_open": "clean flat color shapes with 2–3 slightly softened cel-shading tones on skin and clothing, "
                      "under natural light suited to the scene's time and setting with a clear direction, no overall warm or golden cast unless the scene calls for it, cast shadows on the ground, deep colored shadow masses "
                      "in the environment and focal characters separated from their background by value; "
                      "keep every line clear and in place but recolor it: outer contours a very dark warm brown close to black at medium-light weight, never heavy pure black, "
                      "interior and background lines tinted a clearly darker shade of the color they sit on and still readable; "
                      "foreground and middle ground in flat color planes with only gentle color transitions, "
                      "distance and sky softly painted with subtle gradients and layered atmospheric depth, "
                      "never gradients on characters.",
    },
    # Nhánh test 2026-11-22: 40% Semi-Realistic Storybook Illustration + 35% Flat Illustration + 25% nền storybook.
    "storybook": {
        "name": "ttpq storybook",
        "def": (FLOW / "style" / "ttpq-storybook.md", 0),
        "color_open": "semi-realistic storybook rendering on characters, with gently modeled forms in 3–4 smoothly blended shading tones on skin and clothing "
                      "and natural matte skin, never glossy or airbrushed, "
                      "under natural light suited to the scene's time and setting with a clear direction, no overall warm or golden cast unless the scene calls for it, cast shadows on the ground, deep colored shadow masses "
                      "in the environment and focal characters separated from their background by value; "
                      "keep every line clear and in place but recolor it: outer contours a very dark warm brown close to black at medium-light weight, never heavy pure black, "
                      "interior and background lines tinted a clearly darker shade of the color they sit on and still readable; "
                      "foreground and middle ground in clean flat color planes, "
                      "distance and sky softly painted in a gouache-like storybook manner with subtle gradients and layered atmospheric depth, "
                      "restrained paper-like texture in the background only, never on characters.",
    },
    # Nhánh test 2026-11-22: blend với 50% comic đổi thành 50% Semi-Realistic Comic Illustration.
    "real": {
        "name": "ttpq real",
        "def": (FLOW / "style" / "ttpq-real.md", 0),
        "color_open": "semi-realistic comic rendering on characters, with accurate anatomy and real adult bone structure, "
                      "3 cel-shading tones on skin and clothing that model the form clearly, a crisp main shadow edge and gently softened secondary transitions, "
                      "natural matte skin, never glossy or airbrushed, "
                      "under natural light suited to the scene's time and setting with a clear direction, no overall warm or golden cast unless the scene calls for it, cast shadows on the ground, deep colored shadow masses "
                      "in the environment and focal characters separated from their background by value; "
                      "keep every line clear and in place but recolor it: outer contours a very dark warm brown close to black at medium-light weight, never heavy pure black, "
                      "interior and background lines tinted a clearly darker shade of the color they sit on and still readable; "
                      "foreground and middle ground in flat color planes with only gentle color transitions, "
                      "distance and sky softly painted with subtle gradients and layered atmospheric depth, "
                      "never smooth gradients on characters.",
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


def text_block(path, index=0):
    blocks = re.findall(r"```text\n(.*?)```", path.read_text(encoding="utf-8"), re.S)
    if len(blocks) <= index:
        die(f"không thấy khối ```text thứ {index + 1} trong {rel(path)}")
    return blocks[index].strip()



# Thêm 2026-11-18: style chặn gradient/glow làm hiệu ứng thần thông bị tô phẳng một dải (test Mục Kiền Liên v002);
# --effect nới riêng vùng hiệu ứng, phần còn lại giữ style. Câu khẳng định, không liệt kê thêm điều cấm.
EFFECT_BAN = re.compile(r"\bglow|\bbloom|\bgradient|magic effect|light rays", re.I)


def effect_def(text):
    """Khối STYLE cho lượt có --effect: Exclusions chỉ cấm gradient/glow ngoài vùng hiệu ứng."""
    out = "outside the supernatural effect"
    def fix(m):
        line = m.group(0)
        line = line.replace("excessive gradients", f"excessive gradients {out}")
        line = line.replace("strong bloom or glow", f"bloom or glow {out}")
        return line
    return re.sub(r"^Exclusions:.*$", fix, text, flags=re.M)


def effect_para(effect):
    return (f"Supernatural effect, the one exception to the gradient and glow limits above: {effect}. "
            "Paint it as luminous translucent light in the same 2D book-illustration finish: soft transparent gradients "
            "from a bright near-white core out to its own color, a gentle soft bloom only at its edges, a thin layer of luminous mist, "
            "and fine light particles at several depths, crisp near the viewer and softer farther away; "
            "it may tint nearby ground, objects and robe edges with a faint reflected light of its color. "
            "The effect is the brightest part of the picture and stays inside its own area, framed by mid and deep tones; "
            "it never covers faces or key hands and never changes skin, hair or robe colors; "
            "it is painted light, not neon, photographic, lens-flare or video-game spell light, with no halo behind any head. "
            "Everything else, characters included, keeps the style above: flat cel-shaded color with no gradients on skin or clothing.")


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
    # Từ 2026-11-27 nhận cả tiêu đề "## Dòng nhận diện (tiếng Anh, …)" của profile mẫu cũ (trước đó 27 profile rơi về Dòng prompt ngắn).
    idm = re.search(r"^## Dòng nhận diện(?: tiếng Anh| \(tiếng Anh[^\n]*)\s*\n+(?:```|~~~)text\n(.*?)(?:```|~~~)", t, re.M | re.S)
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


def swap(a):
    """Thay một nhân vật bằng ảnh ref (từ 2026-11-24, theo prompt người dùng kiểm chứng hiệu quả).

    Cố ý ngắn: không tả lại nhân vật bằng chữ (chữ lệch ảnh làm model trộn hai nguồn),
    không khối STYLE (finish lấy từ ảnh cảnh), biểu cảm/góc đầu/hướng nhìn lấy từ ảnh cảnh.
    Câu SCALE (từ 2026-11-25, sau lỗi đầu to khi swap vua Pasenadi): cỡ mặt người cũ là
    mốc scale, thân dựng theo tỷ lệ đầu-thân và vóc dáng profile, khăn/mũ được cao hơn đầu cũ.
    Từ 2026-11-25 (sau lỗi đầu Visakha to ~10-15%, chủ yếu theo bề ngang): mốc là cả khối đầu
    thật dưới khăn (cao + ngang mặt, tai, cằm), không to hơn so với người cạnh, giữ góc đầu,
    giữ khoảng cổ, trang sức theo cỡ cảnh; tỷ lệ lấy từ hình toàn thân, chân dung chỉ cho nét mặt.
    """
    unused = [f for f, v in (("--scenes", a.scenes), ("--body", a.body), ("--recast", a.recast), ("--style", a.style),
                             ("--no-ref", a.no_ref), ("--light", a.light), ("--effect", a.effect), ("--across", a.across),
                             ("--split", a.split), ("--two-scenes", a.two_scenes), ("--no-text", a.no_text)) if v]
    if unused:
        die(f"--pass swap không dùng {', '.join(unused)}; chỉ cần --cast <slug> và --target")
    if not a.cast or len(a.cast) != 1:
        die("--pass swap cần --cast đúng một slug (mỗi lượt thay một người)")
    target = (a.target or "").strip().rstrip(".").strip()
    if not target:
        die("--pass swap cần --target: người cần thay, tả theo vị trí trong ảnh")
    warnings = []
    c = load_profile(a.cast[0], warnings)
    spread = (ROOT / a.spread).resolve()
    vi = bool(re.search(r"[À-ỹ]", target))
    if vi:
        task = f"Thay {target} trong Image 2 bằng nhân vật trong Image 1."
        keep = "Không thay đổi các chi tiết khác."
    else:
        task = f"Replace {target} in Image 2 with the character in Image 1."
        keep = "Do not change any other details."
    if re.search(r"\b(face|hair|beard|robe|skin|eyes?)\b|mặt|tóc|râu|da |mắt", target, re.I):
        warnings.append("--target nên chỉ vị trí/quan hệ của người cần thay; đặc điểm nhận diện đã nằm trong Image 1.")
    parts = [
        "Perform identity-preserving character replacement.",
        "REFERENCE ROLES:\n"
        f"- Image 1: Source identity and character design reference ({c['name']}); identity and design only, not its drawing style or lighting.\n"
        "- Image 2: Target scene, pose, facial expression, head angle, gaze direction, and composition reference.",
        "TASK:\n" + task,
        "SCALE:\n"
        "Use the original character's whole head in Image 2 as the scale anchor: face height (brow to chin), "
        "face width, ear position and chin point, measured on the real head under any head drape or headwear. "
        "The new head must match that size and position and must not be larger relative to the neighboring "
        "figures than the original was. Keep the same head turn as Image 2, not more frontal. Keep the visible "
        "neck length between chin and neckline or necklace as in Image 2. Scale jewelry and accessories to the "
        "figure size in Image 2, with the same detail density as the surrounding figures, not the close-up "
        "portrait in Image 1. Build the body from that anchor using the head-to-body proportions and build of "
        "the full-body views in Image 1; use the portrait view only for facial features. Keep the position and "
        "pose from Image 2. Headwear may extend above the original head outline.",
        "FINISH:\n"
        "Draw the new character in the same finish as the rest of Image 2: the same line color and weight, shading, "
        "light direction and shadow color, so it reads as part of the original picture.",
        keep,
    ]
    if a.avoid.strip():
        parts.append("Avoid: " + a.avoid.strip().rstrip(".") + ".")
    out = spread / a.out if not Path(a.out).is_absolute() else Path(a.out)
    if out.exists():
        die(f"{rel(out)} đã có; dùng version mới")
    out.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"Đã ghi {rel(out)} ({len(' '.join(parts).split())} từ, swap, không khối STYLE)")
    print("Đính kèm:")
    print(f"  Image 1 = {c['ref']}  ({c['name']})")
    print("  Image 2 = <ảnh cần thay nhân vật (ảnh màu hoặc outline)>")
    for wmsg in warnings:
        print(f"CẢNH BÁO: {wmsg}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--spread", required=True)
    ap.add_argument("--scenes", nargs="+", default=[], help="bắt buộc trừ --pass swap")
    ap.add_argument("--pass", dest="kind", choices=["outline", "color", "edit", "color-edit", "pose", "swap"], required=True,
                    help="edit = chỉnh outline; color-edit = sửa chi tiết theo dòng Change: của một nhân vật trên ảnh màu; "
                         "pose = đổi tư thế/hướng xoay/vị trí một nhân vật trên ảnh màu, có khóa tỷ lệ; "
                         "swap = thay một nhân vật trong ảnh có sẵn bằng ảnh ref (prompt ngắn, giữ mọi chi tiết khác)")
    ap.add_argument("--target", help="--pass swap: người cần thay trong ảnh, tả theo vị trí/quan hệ, "
                    "ví dụ \"người đàn ông đứng cạnh cô gái ở tiền cảnh\" hoặc \"the man standing next to the girl in the foreground\"")
    ap.add_argument("--recast", nargs="+", default=[],
                    help="chỉ lượt màu: nhân vật vẽ lại từ profile, outline chỉ giữ vị trí, dáng, cử chỉ, hướng nhìn, đạo cụ; thay nhân vật trên ảnh có sẵn dùng --pass swap")
    ap.add_argument("--body", help="file chứa phần cảnh/comment agent viết (bắt buộc trừ --pass swap)")
    ap.add_argument("--style", choices=sorted(STYLES), help="style của lượt màu (mặc định blend, kể cả --recast); lượt nét và chỉnh outline gọi Semi-Realistic Storybook Illustration, color-edit và swap theo finish của ảnh đang sửa, các lượt này bỏ qua --style")
    ap.add_argument("--story", help="mặc định ttpq-comic/story/<tiền tố layout-slug>")
    ap.add_argument("--cast", nargs="+", help="thay danh sách Profile của cảnh (slug hoặc slug:ref.png)")
    ap.add_argument("--no-ref", nargs="+", default=[], help="nhân vật chỉ tả bằng chữ (xa, nhỏ)")
    ap.add_argument("--avoid", default="", help="điều cấm thêm của lượt (Không vẽ trong brief)")
    ap.add_argument("--light", help="ánh sáng riêng của spread (tiếng Anh), thay ánh sáng của cảnh ở lượt màu")
    ap.add_argument("--two-scenes", action="store_true", help="spread hai cảnh riêng: mỗi cảnh vẽ trọn trang mình tới gáy, không hòa, không dải trắng")
    ap.add_argument("--split", action="store_true", help="spread hai tranh tách nhau, giữa là dải giấy trắng ở gáy (cả ba lượt)")
    ap.add_argument("--across", help="vật (tiếng Anh) được vẽ liền qua gáy, ví dụ \"the long wooden beam\"; người vẫn ở trang của mình")
    ap.add_argument("--effect", help="hiệu ứng thần thông (tiếng Anh) được nới gradient/glow ở lượt màu và color-edit, "
                    "ví dụ \"the jade-green psychic force swirling around the floating beams and earth slab\"")
    ap.add_argument("--no-text", action="store_true", help="hình không có chữ")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if a.kind == "swap":
        swap(a)
        return
    if not a.scenes or not a.body:
        die("--scenes và --body bắt buộc với lượt này")

    across = (a.across or "").strip().rstrip(".").strip()
    if across and a.split:
        die("--across không dùng chung với --split (dải giấy trắng ở gáy không cho vật nào đi qua)")
    if a.two_scenes and (across or a.split):
        die("--two-scenes không dùng chung với --across hoặc --split")
    effect = (a.effect or "").strip().rstrip(".").strip()
    if effect and a.kind not in ("color", "color-edit", "pose"):
        die("--effect chỉ dùng ở lượt color, color-edit và pose; lượt nét vẽ vùng hiệu ứng bằng vài nét mảnh trong body")
    # Từ 2026-11-16: lên màu mặc định blend; từ 2026-11-25 bỏ light/soft, lượt nét và chỉnh outline gán blend (bỏ qua style).
    # Từ 2026-11-25: lượt màu mặc định blend kể cả --recast (bỏ mặc định real của 2026-11-22);
    # color-edit không gọi tên style, finish theo Image 1, để không mâu thuẫn với style thật của ảnh.
    style_given = bool(a.style)
    a.style = a.style or "blend"
    st = STYLES[a.style]
    spread = (ROOT / a.spread).resolve()
    layout = json.loads((spread / "layout.json").read_text(encoding="utf-8"))
    story = ROOT / a.story if a.story else FLOW / "story" / spread.parent.name.split("-")[0]
    warnings = []
    if style_given and a.kind in ("outline", "edit"):
        warnings.append(f"--style {a.style} bị bỏ qua: lượt nét và chỉnh outline luôn gọi style {OUTLINE_STYLE}.")
    if style_given and a.kind in ("color-edit", "pose"):
        warnings.append(f"--style {a.style} bị bỏ qua: {a.kind} vẽ theo finish của Image 1; muốn đổi style thì chạy lại lượt màu.")
    scenes = load_scenes(story, a.scenes, warnings)
    bans, pairs = bible_parts(story)

    tokens = a.cast or list(dict.fromkeys(s for sc in scenes for s in sc["cast"]))
    if not tokens and a.kind not in ("edit", "color-edit", "pose"):
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
    if recast and a.kind != "color":
        die("--recast chỉ dùng cho --pass color; thay cả nhân vật trên outline hoặc ảnh màu dùng --pass swap")
    bad = [s for s in recast if s not in {c["slug"] for c in with_ref}]
    if bad:
        die(f"--recast {', '.join(bad)} không có trong cast có ảnh ref")
    if len(recast) > 2:
        warnings.append(f"--recast {len(recast)} nhân vật: GPT dễ lẫn; nhân vật còn sai thì thay từng người bằng --pass swap.")
    if a.kind == "color-edit":
        if not with_ref:
            die("--pass color-edit cần --cast gồm nhân vật bị sửa (có ảnh ref)")
        if len(with_ref) > 1:
            warnings.append(f"color-edit sửa {len(with_ref)} nhân vật một lượt; mỗi lượt một nhân vật giữ profile chắc hơn.")
    if a.kind == "pose" and len(with_ref) != 1:
        die("--pass pose cần --cast đúng một nhân vật có ảnh ref (mỗi lượt đổi dáng một người)")
    full_id = a.kind in ("color", "color-edit", "pose")
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
    if a.kind in ("edit", "color-edit", "pose"):
        keeps = [m.strip().rstrip(".;") for m in re.findall(r"^Keep:\s*(.+)$", body, re.M)]
        body = "\n".join(l for l in body.splitlines() if not l.startswith("Keep:")).strip()
        if keeps:
            keep_block = "Keep unchanged: " + "; ".join(keeps) + "."
        changes = re.findall(r"^Change:(.*)$", body, re.M)
        if any(re.search(r"[.;]\s+(Preserve|Keep|Retain)\b", c) for c in changes):
            warnings.append("Dòng Change có câu giữ nguyên ('Preserve/Keep …'); tách thành dòng 'Keep: …' riêng.")
        if len(changes) >= 3:
            warnings.append(f"Lượt chỉnh có {len(changes)} dòng Change; mỗi lượt 1–2 thay đổi rồi soát ảnh sẽ chắc hơn.")
    if a.kind in ("color-edit", "pose") and not re.search(r"^Change:", body, re.M):
        die(f"--pass {a.kind} cần body có dòng 'Change: …' (điều cần sửa); thay cả nhân vật dùng --pass swap")
    # Từ 2026-11-27: đổi dáng ở color-edit bị câu "keep pose" chặn; đổi dáng dùng lượt pose có khóa tỷ lệ.
    if a.kind == "color-edit" and re.search(r"\b(turn|rotate|re-?pose|pose|move|shift|relocate|face (toward|away)|three-quarter|rear view|lean|bow)", body, re.I):
        warnings.append("Body color-edit có vẻ đổi tư thế/hướng/vị trí; color-edit khóa pose theo Image 1. Đổi dáng dùng --pass pose (có khóa tỷ lệ).")
    if a.kind in ("color-edit", "pose") and re.search(r"render the (whole |entire )?(illustration|image|picture)|\brestyle\b|in ttpq (comic )?(blend|storybook|real)", body, re.I):
        warnings.append(f"Body {a.kind} đòi vẽ lại style cả tranh, mâu thuẫn với 'giữ nguyên phần còn lại'; bỏ dòng đó "
                        "(script đã khóa finish theo Image 1). Muốn đổi style cả tranh thì chạy lại lượt màu.")

    # Từ 2026-11-22: agent chọn khung hình như nhiếp ảnh gia, nhưng từ nhiếp ảnh trong body làm GPT vẽ ra ảnh chụp thật.
    photo = sorted({m.group(0).lower() for m in PHOTO_WORDS.finditer(body)})
    if photo:
        warnings.append("Body có từ nhiếp ảnh (" + ", ".join(photo) + "); GPT dễ vẽ ra ảnh chụp thật. "
                        "Viết lại bằng lời bố cục: điểm nhìn, cỡ cảnh, vật tiền cảnh, đường dẫn mắt, khoảng trống.")
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
        s = (c["id"] if full_id and c["id"] else c["line"])
        if a.kind in ("outline", "edit"):
            # Từ 2026-11-22: lượt nét bỏ rule head tall (lọc "about N heads tall" khỏi dòng profile, profile giữ nguyên);
            # chỉnh outline bỏ theo từ 2026-11-24 để đồng nhất với lượt nét.
            s = HEADS_TALL.sub("", s).strip(" ,;")
        s += "."
        # Lượt nét và chỉnh outline chèn "In line art"; thiếu nó lượt nét vẽ râu thành râu quai nón (p048-049 v066).
        if a.kind in ("outline", "edit") and c["lineart"]:
            s += f" In line art: {c['lineart']}."
        return s + (f" Fixed face in every moment: {c['face']}." if c["face"] else "")

    img = [f"Image {n0 + i} = {c['name']}: {desc(c)}" for i, c in enumerate(with_ref)]
    no_ref = "no reference image" if a.kind in ("outline", "edit") else "no reference image; same realistic human proportions as the other characters"
    txt = [f"{c['name'][0].upper()}{c['name'][1:]} ({no_ref}): {desc(c)}" for c in text_only]
    fixed = any(c["face"] for c in cast)
    expr = ("Expressions follow the moment, not the sheets, except a fixed face given below."
            if fixed else "Expressions follow the moment, not the sheets.")
    keep_act = "where each character stands, the pose and gesture, the gaze direction, the action, any held prop and the overlap with others"
    take_sheet = "the face, head shape, ears, hair and beard, skin tone, body build and proportions, and the costume with its colors"
    # Thêm 2026-11-24: tỷ lệ lấy từ khối STYLE ở lượt màu; script chỉ neo cỡ theo cảnh cho nhân vật recast, vì không còn nét để bám.
    redraw_prop = ("Their height follows their character line, and their head is the same size as the heads of other people "
                   "standing at the same depth in Image 1.")
    regrow = ("If the sheet's build is taller, broader or slimmer than the figure in Image 1, draw the sheet's build with the feet on the same ground line, "
              "and paint the background around the new silhouette to match its surroundings in Image 1.")
    # Một đoạn chung cho mọi nhân vật recast/sửa, không lặp nguyên văn từng người.
    def tagged(cs):
        return join_names([f"{c['name']} (Image {n0 + with_ref.index(c)})" for c in cs])
    rc = [c for c in with_ref if c["slug"] in recast]
    sheet = "the sheet" if len(rc) == 1 else "each sheet"
    recasts = [f"Recast {tagged(rc)}: ignore the face, head, ears, hair, beard, body proportions and costume lines drawn in Image 1. "
               f"Keep from Image 1 only {keep_act}; take {take_sheet} from {sheet}. {regrow}"] if rc else []
    present = {c["slug"] for c in cast}
    contrast = [s[0].upper() + s[1:] for k, s in pairs.items() if k <= present]

    scene_text = " ".join(sc["text"] for sc in scenes)
    bible_bans = [b for keys, skip, b in bans
                  if (not keys or any(k in scene_text for k in keys)) and not any(k in scene_text for k in skip)]
    avoid = clean_avoid([a.avoid] + [sc["ban"] or "" for sc in scenes] + bible_bans, warnings)
    if effect:
        dropped = [x for x in avoid if EFFECT_BAN.search(x)]
        avoid = [x for x in avoid if x not in dropped]
        if dropped:
            warnings.append("--effect bỏ khỏi Avoid các mục cấm hiệu ứng sáng: " + "; ".join(dropped)
                            + ". Hào quang sau đầu vẫn bị chặn trong đoạn Supernatural effect.")
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
        # Từ 2026-11-19: bỏ khối style (định nghĩa + LINE ART STAGE) khỏi lượt nét theo yêu cầu người dùng.
        # Từ 2026-11-22: lượt nét gọi tên style Semi-Realistic Storybook Illustration; bỏ rule head tall và quy định nét.
        # Từ 2026-11-22 (sau): bỏ "ONE finished black and white" khỏi câu mở; cụm này làm GPT đánh bóng xám, nét tối đậm.
        parts.append(f"Use case: illustration-story. Create an outline illustration in a {OUTLINE_STYLE} style, pure white background. "
                     "Image 1 is the page layout.")
        parts.append(body)
        if img or txt:
            parts.append("\n".join(["Characters: match faces, hair and clothing to their profile sheets; ignore the sheets' poses, backgrounds and labels."] + img + txt + contrast))
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
        if effect:
            open_ += f" The one exception is the supernatural effect ({effect}), painted with translucent gradients and soft glow as described after the style."
        # Thêm 2026-11-17: lượt màu vẽ lại hình nên nhân vật hay lùn/hoạt hình hơn outline; khóa tỷ lệ theo nét.
        # Chỉ khóa tỷ lệ, không khóa cách tô ("color inside the lines / do not stylize" làm ảnh nhạt, mất bóng đổ).
        open_ += (" Keep every figure's height, head size, head-to-body ratio, face shape, eye size and turban or headdress size"
                  " as drawn in Image 1; do not enlarge heads or make figures cartoonish.")
        if recast:
            names = [c["name"] for c in with_ref if c["slug"] in recast]
            who = names[0] if len(names) == 1 else ", ".join(names[:-1]) + " and " + names[-1]
            open_ += (f" Exception: {who} {'is' if len(names) == 1 else 'are'} recast from the profile sheets. For recast characters, Image 1 only directs the acting"
                      " (position, pose, gesture, gaze, action, props); faces, bodies and costumes are drawn fresh from the sheets, not from Image 1's lines. "
                      + redraw_prop)
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
        parts.append(effect_def(text_block(*st["def"])) if effect else text_block(*st["def"]))
        if effect:
            parts.append(effect_para(effect))
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
        parts.append(f"Edit Image 1, the finished color illustration of {pages}. Change only what is listed below on {who}; keep every other person, "
                     "the background, light, colors, line treatment and all text of Image 1 exactly as they are.")
        if body:
            parts.append(body)
        if keep_block:
            parts.append(keep_block)
        one = len(with_ref) == 1
        sheet = "the profile sheet" if one else "their profile sheets"
        # Từ 2026-11-25: color-edit chỉ sửa chi tiết trong Change:, không recast cả người (việc đó của swap).
        parts.append("\n".join([f"Use {sheet} only as the reference for the details being changed; keep the rest of {who} "
                                 "(face, hair, body, size, pose, expression and every costume part not listed) exactly as in Image 1. "
                                 "Ignore the sheets' poses, lighting, labels and drawing style. Take proportions only from the sheets' full-body views; "
                                 "the portrait view is for facial features only."]
                                + img + contrast))
        # Không gọi tên style: tên có thể trái với style thật của ảnh; finish và tỷ lệ bám Image 1.
        parts.append("Style: paint the changed parts in the same finish as the rest of Image 1: the same outline color and weight, "
                     "cel-shading tones, colors, light direction and shadow color; take only identity and design from the sheet, not its rendering; strictly 2D."
                     + (f" Keep the supernatural effect of Image 1 ({effect}) with its translucent gradients, soft glow and light particles exactly as it is;"
                        " where it lit the changed parts, light them the same way." if effect else ""))
        parts.append(f"The character stays on its own page, with face and key hands out of {mid} around the center fold.")
        parts.append("No text of any kind in the image." if a.no_text else "Keep all text, folios and any highlight behind the text exactly as in Image 1; do not redraw any letters.")
    elif a.kind == "pose":
        # Từ 2026-11-27: đổi dáng vẽ lại cả người; không có mốc thì GPT phóng to đầu theo chân dung của sheet (Matika p196-197 v029).
        c0 = with_ref[0]
        who = c0["name"]
        parts.append(f"Edit Image 1, the finished color illustration of {pages}. Change only the pose, turn or position of {who} as listed below; "
                     "keep every other person, the background, light, colors, line treatment and all text of Image 1 exactly as they are.")
        parts.append(body)
        if keep_block:
            parts.append(keep_block)
        parts.append("\n".join([f"Keep {who}'s identity, face, hair, costume and colors as in Image 1. Use the profile sheet only to see how the hair "
                                 "and costume look from the new angle; ignore the sheet's poses, lighting, labels and drawing style."]
                                + img + contrast))
        parts.append("SCALE:\n"
                     f"{who} as drawn in Image 1 is the scale anchor. The whole head (crown to chin, including any hair bun or headwear), "
                     "the shoulder width and the full standing height stay the same size as in Image 1, and no larger relative to the people "
                     "at the same depth; a turned, rear or bowed view must not make the head or hair mass bigger. "
                     "Build the body with the head-to-body proportions of the full-body views in the sheet, realistic and age-accurate "
                     "(an adult about 7 to 7.5 heads tall); use the portrait view only for facial features. "
                     "The feet stay on the same ground line as in Image 1 unless a Change line moves them. "
                     "No chibi or cartoon proportions, no oversized head, no shortened body.")
        parts.append("Paint the background revealed around the old silhouette to match its surroundings in Image 1; "
                     f"leave no ghost outline or duplicate of {who}.")
        parts.append("FINISH:\nDraw the re-posed figure in the same finish as the rest of Image 1: the same outline color and weight, "
                     "cel-shading tones, colors, light direction and shadow color; take only identity and design from the sheet, not its rendering; strictly 2D."
                     + (f" Keep the supernatural effect of Image 1 ({effect}) exactly as it is; where it lit the figure, light it the same way." if effect else ""))
        parts.append(f"The character stays on its own page, with face and key hands out of {mid} around the center fold.")
        parts.append("No text of any kind in the image." if a.no_text else "Keep all text, folios and any highlight behind the text exactly as in Image 1; do not redraw any letters.")
    else:
        parts.append(f"Edit Image 1, the clean outline of {pages}. Change only what is listed below and keep everything else in Image 1 unchanged.")
        parts.append(body)
        if keep_block:
            parts.append(keep_block)
        if img:
            parts.append("\n".join(["Edited characters must match their profile sheets in face, hair and clothing; ignore the sheets' poses, framing and labels."] + img + contrast))
        # Từ 2026-11-24: chỉnh outline gọi cùng tên style với lượt nét (OUTLINE_STYLE), không theo --style.
        parts.append(f"Style: the same \"{OUTLINE_STYLE}\" line art as Image 1: clean black outlines with natural line weight; no color, no gray, no shading, no hatching, no sketchy lines.")
        if img:
            parts.append(f"Edited characters stay on their own page, with faces and key hands out of {mid} around the center fold.")
        if across:
            parts.append(f"{across[0].upper()}{across[1:]} may run unbroken across the center fold; no hands, ropes or joints on it within {mid}.")
        parts.append("Keep all text words, type size and first-line positions; only the lines beside the edited area may reflow to wrap around the new shapes, keeping any colored highlight behind them.")
    if avoid_line:
        parts.append(avoid_line)
    out = spread / a.out if not Path(a.out).is_absolute() else Path(a.out)
    if out.exists():
        die(f"{rel(out)} đã có; dùng version mới")
    out.write_text("\n\n".join(parts) + "\n", encoding="utf-8")

    first = {"outline": canvas_ref(spread, layout) if a.kind == "outline" else None, "color": "<outline được chọn>", "edit": "<outline đang sửa>",
             "color-edit": "<ảnh màu đang sửa>", "pose": "<ảnh màu đang sửa>"}[a.kind]
    first = rel(first) if isinstance(first, Path) else first
    style_label = OUTLINE_STYLE if a.kind in ("outline", "edit") else "theo finish của Image 1" if a.kind in ("color-edit", "pose") else st["name"]
    print(f"Đã ghi {rel(out)} ({len(' '.join(parts).split())} từ, style {style_label})")
    print("Đính kèm:")
    print(f"  Image 1 = {first}")
    for i, c in enumerate(with_ref):
        print(f"  Image {n0 + i} = {c['ref']}  ({c['name']})")
    for wmsg in warnings:
        print(f"CẢNH BÁO: {wmsg}")


if __name__ == "__main__":
    main()
