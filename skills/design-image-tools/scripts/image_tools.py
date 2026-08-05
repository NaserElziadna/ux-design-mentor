#!/usr/bin/env python3
"""
image_tools.py — design-focused image utilities. Requires Pillow (pip install pillow)
except `contrast` and `placeholder --svg`, which are pure stdlib.

Commands:
  palette     Extract dominant colors from an image (for harmonizing UI colors)
                python image_tools.py palette hero.jpg --colors 6
  contrast    WCAG 2.2 contrast ratio between two colors
                python image_tools.py contrast "#1a1a2e" "#e0e0f0"
  resize      Resize/crop to exact size (smart center-crop, web-optimized output)
                python image_tools.py resize hero.jpg --size 1600x900 --out hero-web.jpg
  optimize    Compress images for web (quality 82, strips metadata, optional webp)
                python image_tools.py optimize ./assets --webp
  placeholder Generate a branded placeholder (SVG or PNG) — gradient + label
                python image_tools.py placeholder --size 800x450 --text "Hero image" --color "#4f46e5" --out ph.svg
  analyze     Report image facts a designer needs: size, aspect, mean luminance,
              is-it-busy (edge density), palette, and text-overlay safety advice
                python image_tools.py analyze hero.jpg
  favicon     Generate favicon set (16/32/48/180/512 PNG + .ico) from a source image
                python image_tools.py favicon logo.png --out ./favicons

All commands print JSON so results are easy to consume programmatically.
"""

import argparse
import json
import math
import os
import sys


# ------------------------------------------------------------------ helpers
def hex_to_rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def rel_luminance(rgb):
    def chan(c):
        c /= 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (chan(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(c1, c2):
    l1, l2 = sorted((rel_luminance(c1), rel_luminance(c2)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def parse_size(s):
    w, h = s.lower().split("x")
    return int(w), int(h)


def need_pil():
    try:
        from PIL import Image  # noqa
        return True
    except ImportError:
        print(json.dumps({"error": "Pillow required: pip install pillow"}), file=sys.stderr)
        sys.exit(1)


# ------------------------------------------------------------------ commands
def cmd_contrast(args):
    c1, c2 = hex_to_rgb(args.color1), hex_to_rgb(args.color2)
    ratio = contrast_ratio(c1, c2)
    print(json.dumps({
        "color1": args.color1, "color2": args.color2,
        "ratio": round(ratio, 2),
        "wcag": {
            "AA_normal_text": ratio >= 4.5,
            "AA_large_text": ratio >= 3.0,
            "AAA_normal_text": ratio >= 7.0,
            "AA_ui_components": ratio >= 3.0,
        },
        "verdict": ("passes AA for all text" if ratio >= 4.5 else
                    "large text / UI components only" if ratio >= 3.0 else
                    "FAILS WCAG — do not pair these for text"),
    }, indent=2))


def get_palette(img, n):
    small = img.convert("RGB").resize((100, 100))
    q = small.quantize(colors=n, method=2)
    pal = q.getpalette()[:n * 3]
    counts = sorted(q.getcolors(10000) or [], reverse=True)
    out = []
    for count, idx in counts[:n]:
        rgb = tuple(pal[idx * 3: idx * 3 + 3])
        out.append({
            "hex": rgb_to_hex(rgb),
            "share": round(count / 10000.0, 3),
            "luminance": round(rel_luminance(rgb), 3),
            "contrast_vs_white": round(contrast_ratio(rgb, (255, 255, 255)), 2),
            "contrast_vs_black": round(contrast_ratio(rgb, (0, 0, 0)), 2),
        })
    return out


def cmd_palette(args):
    need_pil()
    from PIL import Image
    with Image.open(args.image) as img:
        print(json.dumps({"image": args.image,
                          "palette": get_palette(img, args.colors)}, indent=2))


def cmd_resize(args):
    need_pil()
    from PIL import Image
    tw, th = parse_size(args.size)
    with Image.open(args.image) as img:
        img = img.convert("RGB") if args.out.lower().endswith((".jpg", ".jpeg")) else img
        sw, sh = img.size
        scale = max(tw / sw, th / sh)
        img = img.resize((round(sw * scale), round(sh * scale)), Image.LANCZOS)
        left, top = (img.width - tw) // 2, (img.height - th) // 2
        img = img.crop((left, top, left + tw, top + th))
        img.save(args.out, quality=85, optimize=True)
    print(json.dumps({"out": args.out, "size": f"{tw}x{th}",
                      "bytes": os.path.getsize(args.out)}, indent=2))


def cmd_optimize(args):
    need_pil()
    from PIL import Image
    paths = []
    if os.path.isdir(args.path):
        for f in os.listdir(args.path):
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                paths.append(os.path.join(args.path, f))
    else:
        paths = [args.path]
    report = []
    for p in paths:
        before = os.path.getsize(p)
        with Image.open(p) as img:
            if args.max_width and img.width > args.max_width:
                r = args.max_width / img.width
                img = img.resize((args.max_width, round(img.height * r)), Image.LANCZOS)
            if args.webp:
                out = os.path.splitext(p)[0] + ".webp"
                img.save(out, "WEBP", quality=82, method=6)
            else:
                out = p
                fmt = "JPEG" if p.lower().endswith((".jpg", ".jpeg")) else None
                img = img.convert("RGB") if fmt == "JPEG" else img
                img.save(out, fmt, quality=82, optimize=True)
        report.append({"file": out, "before_kb": before // 1024,
                       "after_kb": os.path.getsize(out) // 1024})
    print(json.dumps(report, indent=2))


def cmd_placeholder(args):
    w, h = parse_size(args.size)
    base = hex_to_rgb(args.color)
    darker = rgb_to_hex(tuple(max(0, c - 60) for c in base))
    text = args.text or f"{w}×{h}"
    text_color = "#ffffff" if contrast_ratio(base, (255, 255, 255)) >= 3 else "#111111"
    if args.out.lower().endswith(".svg"):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
               f'viewBox="0 0 {w} {h}"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
               f'<stop offset="0" stop-color="{args.color}"/><stop offset="1" stop-color="{darker}"/>'
               f'</linearGradient></defs><rect width="{w}" height="{h}" fill="url(#g)"/>'
               f'<text x="50%" y="50%" fill="{text_color}" font-family="system-ui,sans-serif" '
               f'font-size="{max(14, min(w, h) // 12)}" text-anchor="middle" '
               f'dominant-baseline="middle">{text}</text></svg>')
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(svg)
    else:
        need_pil()
        from PIL import Image, ImageDraw
        img = Image.new("RGB", (w, h))
        d = ImageDraw.Draw(img)
        dk = hex_to_rgb(darker)
        for y in range(h):
            t = y / max(1, h - 1)
            d.line([(0, y), (w, y)],
                   fill=tuple(round(base[i] + (dk[i] - base[i]) * t) for i in range(3)))
        d.text((w / 2, h / 2), text, fill=text_color, anchor="mm")
        img.save(args.out)
    print(json.dumps({"out": args.out, "size": f"{w}x{h}", "text_color": text_color}, indent=2))


def cmd_analyze(args):
    need_pil()
    from PIL import Image, ImageFilter, ImageStat
    with Image.open(args.image) as img:
        w, h = img.size
        gcd = math.gcd(w, h)
        gray = img.convert("L").resize((200, round(200 * h / w) or 1))
        mean_lum = ImageStat.Stat(gray).mean[0] / 255.0
        edges = gray.filter(ImageFilter.FIND_EDGES)
        busyness = ImageStat.Stat(edges).mean[0] / 255.0
        palette = get_palette(img, 5)
    advice = []
    if busyness > 0.15:
        advice.append("Busy image: add a scrim/overlay (e.g. rgba(0,0,0,.45)) before overlaying text.")
    advice.append("Prefer white overlay text." if mean_lum < 0.45
                  else "Prefer dark overlay text." if mean_lum > 0.6
                  else "Mid-luminance: overlay text needs a scrim either way.")
    print(json.dumps({
        "image": args.image, "width": w, "height": h,
        "aspect_ratio": f"{w // gcd}:{h // gcd}",
        "mean_luminance": round(mean_lum, 3),
        "busyness": round(busyness, 3),
        "palette": palette,
        "text_overlay_advice": advice,
    }, indent=2))


def cmd_favicon(args):
    need_pil()
    from PIL import Image
    os.makedirs(args.out, exist_ok=True)
    files = []
    with Image.open(args.image) as img:
        img = img.convert("RGBA")
        side = min(img.size)
        img = img.crop(((img.width - side) // 2, (img.height - side) // 2,
                        (img.width + side) // 2, (img.height + side) // 2))
        for s in (16, 32, 48, 180, 512):
            p = os.path.join(args.out, f"favicon-{s}x{s}.png")
            img.resize((s, s), Image.LANCZOS).save(p)
            files.append(p)
        ico = os.path.join(args.out, "favicon.ico")
        img.resize((48, 48), Image.LANCZOS).save(ico, sizes=[(16, 16), (32, 32), (48, 48)])
        files.append(ico)
    print(json.dumps({"files": files}, indent=2))


def main():
    ap = argparse.ArgumentParser(description="Design-focused image utilities")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("palette"); p.add_argument("image"); p.add_argument("--colors", type=int, default=6); p.set_defaults(fn=cmd_palette)
    p = sub.add_parser("contrast"); p.add_argument("color1"); p.add_argument("color2"); p.set_defaults(fn=cmd_contrast)
    p = sub.add_parser("resize"); p.add_argument("image"); p.add_argument("--size", required=True); p.add_argument("--out", required=True); p.set_defaults(fn=cmd_resize)
    p = sub.add_parser("optimize"); p.add_argument("path"); p.add_argument("--webp", action="store_true"); p.add_argument("--max-width", type=int, default=0); p.set_defaults(fn=cmd_optimize)
    p = sub.add_parser("placeholder"); p.add_argument("--size", default="800x450"); p.add_argument("--text", default=""); p.add_argument("--color", default="#6366f1"); p.add_argument("--out", default="placeholder.svg"); p.set_defaults(fn=cmd_placeholder)
    p = sub.add_parser("analyze"); p.add_argument("image"); p.set_defaults(fn=cmd_analyze)
    p = sub.add_parser("favicon"); p.add_argument("image"); p.add_argument("--out", default="./favicons"); p.set_defaults(fn=cmd_favicon)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
