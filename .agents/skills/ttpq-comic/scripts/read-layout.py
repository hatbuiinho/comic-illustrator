#!/usr/bin/env python3
"""Đọc một spread trong PDF layout và xuất layout.json cho flow ttpq-comic.

Mỗi trang PDF là một spread: nửa trái là trang tiếng Việt, nửa phải là trang
tiếng Anh. Script tách chữ thân bài theo từng trang, gom thành đoạn, đọc ô hình
(rect tô màu) cùng ghi chú "Hình N" bên trong, và quy đổi kích thước/vị trí sang
canvas tạo ảnh.

Ví dụ:
  python3 read-layout.py "ttpq-comic/layouts/T53_Part 2.pdf" --page 3 \
      --out "ttpq-comic/spreads/t53-part-2/p054-055"
"""
import argparse
import json
import re
import statistics
import subprocess
import sys
from pathlib import Path

import pdfplumber

CANVAS_W, CANVAS_H = 1536, 1024  # ChatGPT Image, khổ ngang 3:2
VI_CHARS = set("ăâđêôơưàảãáạằẳẵắặầẩẫấậèẻẽéẹềểễếệìỉĩíịòỏõóọồổỗốộờởỡớợùủũúụừửữứựỳỷỹýỵ")
COLOR_NAMES = {(1, 0, 0, 0): "cyan", (0, 1, 0, 0): "magenta", (0, 0, 1, 0): "yellow",
               (1, 1, 0, 0): "blue", (0, 1, 1, 0): "red", (1, 0, 1, 0): "green"}
FRAME_LABEL = re.compile(r"^\s*Hình\s*(\d+)\b", re.IGNORECASE)


def lang_of(text):
    letters = [c for c in text.lower() if c.isalpha()]
    if not letters:
        return "unknown"
    ratio = sum(c in VI_CHARS for c in letters) / len(letters)
    return "vi" if ratio > 0.03 else "en"


def color_name(color):
    """Tên màu đánh dấu của ký tự; None nếu là chữ đen/xám thường."""
    if not color:
        return None
    c = tuple(round(float(v), 2) for v in color)
    if len(c) == 4 and c[:3] == (0, 0, 0) or len(c) in (1, 3) and max(c) == min(c):
        return None
    return COLOR_NAMES.get(c, str(c))


def group_lines(chars, tol=2.0):
    lines = []
    for ch in sorted(chars, key=lambda c: (round(c["top"]), c["x0"])):
        for line in lines:
            if abs(line["top"] - ch["top"]) <= tol:
                line["chars"].append(ch)
                break
        else:
            lines.append({"top": ch["top"], "chars": [ch]})
    out = []
    for line in lines:
        cs = sorted(line["chars"], key=lambda c: c["x0"])
        text, runs = "", []
        for prev, cur in zip([None] + cs[:-1], cs):
            piece = (" " if prev is not None and cur["x0"] - prev["x1"] > cur["size"] * 0.2 else "") + cur["text"]
            text += piece
            color = color_name(cur.get("non_stroking_color"))
            if runs and runs[-1][0] == color:
                runs[-1][1] += piece
            else:
                runs.append([color, piece])
        fonts = {c["fontname"].split("+")[-1] for c in cs}
        # Lời thoại "- ...": vị trí chữ đầu sau dấu gạch, dùng nhận dòng thụt treo.
        hang_x = None
        if cs[0]["text"] in "-–—":
            rest = [c for c in cs[1:] if c["text"].strip()]
            hang_x = rest[0]["x0"] if rest else None
        out.append({
            "hangX": hang_x,
            "x0": min(c["x0"] for c in cs), "x1": max(c["x1"] for c in cs),
            "top": min(c["top"] for c in cs), "bottom": max(c["bottom"] for c in cs),
            "size": statistics.median(c["size"] for c in cs),
            "font": sorted(fonts)[0], "bold": any("Bold" in f for f in fonts),
            "text": re.sub(r"\s+", " ", text).strip(),
            "runs": runs,
        })
    return sorted(out, key=lambda l: l["top"])


def inside(line, rect):
    cx, cy = (line["x0"] + line["x1"]) / 2, (line["top"] + line["bottom"]) / 2
    return rect["x0"] <= cx <= rect["x1"] and rect["top"] <= cy <= rect["bottom"]


def paragraphs(lines, leading, margin_left):
    paras, cur = [], None
    for line in lines:
        prev = cur["lines"][-1] if cur else None
        dialogue = line["hangX"] is not None
        gap = prev is not None and line["top"] - prev["top"] > leading * 1.15
        if cur is None or dialogue or gap:
            new = True
        elif cur["lines"][0]["hangX"] is not None:
            # Trong đoạn thoại: dòng tiếp thẳng hàng chữ sau dấu gạch (thụt treo).
            new = abs(line["x0"] - cur["lines"][0]["hangX"]) > 2
        else:
            # Trong đoạn kể: dòng tiếp sát lề, dòng thụt vào là đoạn mới.
            new = line["x0"] - margin_left > line["size"] * 0.8
        if new:
            cur = {"lines": [], "spaceBefore": bool(gap)}
            paras.append(cur)
        cur["lines"].append(line)
    result = []
    for p in paras:
        ls = p["lines"]
        text = " ".join(l["text"] for l in ls)
        text = re.sub(r"(\w)- (\w)", r"\1\2", text)  # nối từ bị gạch nối cuối dòng
        # Cụm chữ tô màu trong layout (thường là dấu biên tập), gộp qua các dòng.
        marks = []
        for l in ls:
            for i, (color, piece) in enumerate(l["runs"]):
                piece = piece if i else " " + piece
                if marks and marks[-1]["color"] == color:
                    marks[-1]["text"] += piece
                else:
                    marks.append({"color": color, "text": piece})
        marks = [{"color": m["color"], "text": re.sub(r"\s+", " ", m["text"]).strip()}
                 for m in marks if m["color"] and m["text"].strip()]
        result.append({
            "text": text,
            "marks": marks,
            "lines": len(ls),
            "bbox": [min(l["x0"] for l in ls), ls[0]["top"], max(l["x1"] for l in ls), ls[-1]["bottom"]],
            "spaceBefore": p["spaceBefore"],
        })
    return result


def blocks(paras, leading):
    out, cur = [], None
    for p in paras:
        if cur and p["bbox"][1] - cur["bbox"][3] <= leading * 1.6:
            cur["paragraphs"].append(p)
            cur["bbox"] = [min(cur["bbox"][0], p["bbox"][0]), cur["bbox"][1],
                           max(cur["bbox"][2], p["bbox"][2]), p["bbox"][3]]
        else:
            cur = {"bbox": list(p["bbox"]), "paragraphs": [p]}
            out.append(cur)
    return out


def to_canvas(bbox, page_w, page_h):
    """Quy đổi bbox (pt) sang % spread và px trên canvas 1536x1024.

    Spread (tỉ lệ ~1.41) đặt giữa canvas 3:2 theo chiều cao; hai bên dư
    phần bleed sẽ cắt sau khi tạo ảnh.
    """
    scale = CANVAS_H / page_h
    offset_x = (CANVAS_W - page_w * scale) / 2
    x0, y0, x1, y1 = bbox
    return {
        "pct": [round(x0 / page_w * 100, 1), round(y0 / page_h * 100, 1),
                round(x1 / page_w * 100, 1), round(y1 / page_h * 100, 1)],
        "px": [round(offset_x + x0 * scale), round(y0 * scale),
               round(offset_x + x1 * scale), round(y1 * scale)],
    }


def read_spread(pdf_path, page_no):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_no - 1].dedupe_chars(tolerance=1)
        W, H = float(page.width), float(page.height)
        chars = list(page.chars)
        rects = [r for r in page.rects if (r["x1"] - r["x0"]) * (r["bottom"] - r["top"]) > W * H * 0.02]
    mid = W / 2

    # Dòng chữ chạy qua cả hai trang nên tách ký tự theo nửa spread trước khi gom dòng.
    def side_lines(side):
        return group_lines([c for c in chars if ((c["x0"] + c["x1"]) / 2 < mid) == (side == "left")])

    def is_folio(l):
        return l["top"] > H * 0.9 and re.fullmatch(r"\d+", l["text"]) is not None

    all_lines = [l for l in side_lines("left") + side_lines("right") if not is_folio(l)]
    scale = CANVAS_H / H
    spread = {
        "source": {"pdf": str(pdf_path), "page": page_no},
        "spread": {"widthPt": round(W, 2), "heightPt": round(H, 2), "aspect": round(W / H, 3),
                   "gutterXPt": round(mid, 2)},
        "canvas": {"width": CANVAS_W, "height": CANVAS_H,
                   "spreadWidthPx": round(W * scale), "trimEachSidePx": round((CANVAS_W - W * scale) / 2),
                   "gutterXPx": round((CANVAS_W - W * scale) / 2 + mid * scale)},
        "pages": {}, "frames": [], "warnings": [],
    }

    for r in sorted(rects, key=lambda r: (r["x0"], r["top"])):
        rb = {"x0": r["x0"], "top": r["top"], "x1": r["x1"], "bottom": r["bottom"]}
        notes = sorted((l for l in all_lines if inside(l, rb)), key=lambda l: l["top"])
        figs, cur = [], None
        for l in notes:
            m = FRAME_LABEL.match(l["text"])
            if m:
                cur = {"label": f"Hình {m.group(1)}", "text": []}
                figs.append(cur)
            elif cur:
                cur["text"].append(l["text"])
        spread["frames"].append({
            "bbox": [round(v, 1) for v in (r["x0"], r["top"], r["x1"], r["bottom"])],
            "fill": color_name(r.get("non_stroking_color")),
            "side": "left" if r["x1"] <= mid + 1 else "right" if r["x0"] >= mid - 1 else "cross-gutter",
            "figures": [{"label": f["label"], "note": " ".join(f["text"]).strip()} for f in figs],
            "notes": [l["text"] for l in notes],
            **to_canvas((r["x0"], r["top"], r["x1"], r["bottom"]), W, H),
        })

    for side in ("left", "right"):
        ls = side_lines(side)
        frames_b = [dict(zip(("x0", "top", "x1", "bottom"), f["bbox"])) for f in spread["frames"]]
        folio = [{"text": l["text"], **to_canvas((l["x0"], l["top"], l["x1"], l["bottom"]), W, H),
                  "sizePx": round(l["size"] * scale, 1)} for l in ls if is_folio(l)]
        body = [l for l in ls if not is_folio(l) and not any(inside(l, fb) for fb in frames_b)]
        if not body:
            spread["pages"][side] = {"folio": folio[0] if folio else None, "blocks": []}
            continue
        tops = [b["top"] - a["top"] for a, b in zip(body, body[1:]) if 0 < b["top"] - a["top"] < body[0]["size"] * 2]
        # Leading = cụm khoảng cách dòng nhỏ nhất; khoảng cách đoạn lớn hơn nên loại ra.
        tight = [t for t in tops if t <= min(tops) * 1.08] if tops else []
        leading = round(statistics.median(tight), 2) if tight else round(body[0]["size"] * 1.4, 2)
        margin_left = min(l["x0"] for l in body)
        size = statistics.median(l["size"] for l in body)
        font = statistics.mode(l["font"] for l in body)
        paras = paragraphs(body, leading, margin_left)
        text_all = " ".join(p["text"] for p in paras)
        lang = lang_of(text_all)
        bl = blocks(paras, leading)
        for b in bl:
            b.update(to_canvas(b["bbox"], W, H))
            b["bbox"] = [round(v, 1) for v in b["bbox"]]
            for p in b["paragraphs"]:
                p["bbox"] = [round(v, 1) for v in p["bbox"]]
        spread["pages"][side] = {
            "folio": folio[0] if folio else None,
            "lang": lang,
            "font": font, "sizePt": size, "leadingPt": leading,
            "sizePx": round(size * scale, 1), "leadingPx": round(leading * scale, 1),
            "textBoxPt": [round(min(l["x0"] for l in body), 1), round(body[0]["top"], 1),
                          round(max(l["x1"] for l in body), 1), round(body[-1]["bottom"], 1)],
            "lineCount": len(body), "charCount": len(text_all),
            "blocks": bl,
        }
        expected = "vi" if side == "left" else "en"
        if lang != expected:
            spread["warnings"].append(
                f"Trang {'trái' if side == 'left' else 'phải'} đang là '{lang}', cần '{expected}'.")
    if not spread["frames"]:
        spread["warnings"].append("Không thấy ô hình (rect) trong spread; vùng tranh suy từ khoảng trống ngoài khối chữ.")
    return spread


def find_page_by_folio(pdf_path, folio):
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            W, H = float(page.width), float(page.height)
            words = page.extract_words()
            if any(w["text"] == str(folio) and w["top"] > H * 0.9 and w["x1"] < W / 2 for w in words):
                return i
    raise SystemExit(f"Không tìm thấy spread có số trang trái {folio}.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    target = ap.add_mutually_exclusive_group(required=True)
    target.add_argument("--page", type=int, help="Số trang PDF (1-based) của spread")
    target.add_argument("--folio", type=int, help="Số trang sách của trang trái spread, ví dụ 54")
    ap.add_argument("--out", help="Thư mục spread; ghi layout.json, layout.png và layout-ref.png")
    args = ap.parse_args()
    if args.folio is not None:
        args.page = find_page_by_folio(args.pdf, args.folio)
    data = read_spread(Path(args.pdf), args.page)
    text = json.dumps(data, ensure_ascii=False, indent=2)
    if not args.out:
        print(text)
        return
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "layout.json").write_text(text + "\n", encoding="utf-8")
    # layout.png để xem nhanh; layout-ref.png đủ nét để đính kèm vào ChatGPT Image.
    for dpi, name in (("96", "layout"), ("200", "layout-ref")):
        try:
            subprocess.run(["pdftoppm", "-f", str(args.page), "-l", str(args.page), "-r", dpi, "-png",
                            "-singlefile", args.pdf, str(out / name)], check=True)
        except (OSError, subprocess.CalledProcessError) as err:
            print(f"Không tạo được {name}.png: {err}", file=sys.stderr)
    print(f"Đã ghi {out / 'layout.json'}")
    for w in data["warnings"]:
        print(f"CẢNH BÁO: {w}")


if __name__ == "__main__":
    main()
