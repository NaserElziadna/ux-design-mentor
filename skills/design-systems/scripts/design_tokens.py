#!/usr/bin/env python3
"""
design_tokens.py — generate a complete, WCAG-validated design-token system
from a single brand color. Pure stdlib.

What you get:
  - brand scale 50..950 (11 steps, perceptually spaced lightness)
  - neutral (gray) scale subtly tinted toward the brand hue
  - semantic colors (success / warning / danger / info) harmonized to brand saturation
  - accessible pairings report (which steps pass AA on white / on darkest)
  - modular type scale (default ratio 1.25 "major third")
  - 4px-based spacing scale
  - radius + shadow tokens

Usage:
  python design_tokens.py "#4f46e5"                      # JSON to stdout
  python design_tokens.py "#0e7c66" --format css         # :root CSS variables
  python design_tokens.py "#4f46e5" --type-ratio 1.333 --base-size 16
"""

import argparse
import colorsys
import json
import sys


def hex_to_rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(*(max(0, min(255, round(c))) for c in rgb))


def rel_lum(rgb):
    def ch(c):
        c /= 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(c1, c2):
    l1, l2 = sorted((rel_lum(c1), rel_lum(c2)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


STEPS = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
# target HSL lightness per step (roughly Tailwind-like, perceptually even)
LIGHTNESS = {50: .97, 100: .93, 200: .85, 300: .75, 400: .62, 500: .52,
             600: .44, 700: .36, 800: .28, 900: .20, 950: .13}


def make_scale(h, s, sat_curve=1.0):
    scale = {}
    for step in STEPS:
        light = LIGHTNESS[step]
        # desaturate at the extremes so tints/shades don't look neon
        sat = s * sat_curve * (1 - 0.55 * abs(light - 0.55))
        r, g, b = colorsys.hls_to_rgb(h, light, min(1.0, sat))
        scale[str(step)] = rgb_to_hex((r * 255, g * 255, b * 255))
    return scale


def build(brand_hex, type_ratio, base_size):
    r, g, b = hex_to_rgb(brand_hex)
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)

    brand = make_scale(h, max(s, 0.25))
    neutral = make_scale(h, min(s * 0.12, 0.06))
    semantic = {
        "success": make_scale(145 / 360, max(s * 0.9, 0.35)),
        "warning": make_scale(38 / 360, max(s * 0.95, 0.5)),
        "danger": make_scale(2 / 360, max(s * 0.9, 0.45)),
        "info": make_scale(210 / 360, max(s * 0.9, 0.35)),
    }

    # accessibility report: first step of each scale that passes AA on white/darkest
    white, darkest = (255, 255, 255), hex_to_rgb(neutral["950"])
    pairs = {}
    for name, scale in {"brand": brand, **semantic}.items():
        on_white = next((st for st in map(str, STEPS)
                         if contrast(hex_to_rgb(scale[st]), white) >= 4.5), None)
        on_dark = next((st for st in map(str, reversed(STEPS))
                        if contrast(hex_to_rgb(scale[st]), darkest) >= 4.5), None)
        pairs[name] = {
            "text_on_white_use_step": on_white,
            "text_on_dark_use_step": on_dark,
            "white_text_on_500": round(contrast(hex_to_rgb(scale["500"]), white), 2),
            "white_text_on_600": round(contrast(hex_to_rgb(scale["600"]), white), 2),
            "button_recommendation": ("600+ background with white text"
                                      if contrast(hex_to_rgb(scale["600"]), white) >= 4.5
                                      else "700+ background with white text"),
        }

    names = ["xs", "sm", "base", "lg", "xl", "2xl", "3xl", "4xl", "5xl"]
    type_scale = {n: round(base_size * type_ratio ** (i - 2), 2)
                  for i, n in enumerate(names)}

    spacing = {str(i): i * 4 for i in [0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32]}

    return {
        "meta": {"brand": brand_hex, "type_ratio": type_ratio, "base_size": base_size},
        "color": {"brand": brand, "neutral": neutral, **semantic},
        "accessibility": pairs,
        "typography": {"scale_px": type_scale,
                       "line_height": {"tight": 1.2, "normal": 1.5, "relaxed": 1.7},
                       "weights": {"regular": 400, "medium": 500, "bold": 700}},
        "spacing_px": spacing,
        "radius_px": {"sm": 4, "md": 8, "lg": 12, "xl": 16, "full": 9999},
        "shadow": {
            "sm": "0 1px 2px rgb(0 0 0 / .06)",
            "md": "0 2px 8px rgb(0 0 0 / .08)",
            "lg": "0 8px 24px rgb(0 0 0 / .12)",
        },
    }


def to_css(t):
    lines = [":root {"]
    for group, scale in t["color"].items():
        for step, hexv in scale.items():
            lines.append(f"  --color-{group}-{step}: {hexv};")
    for n, v in t["typography"]["scale_px"].items():
        lines.append(f"  --text-{n}: {v / 16:.4g}rem;")
    for n, v in t["spacing_px"].items():
        lines.append(f"  --space-{n}: {v}px;")
    for n, v in t["radius_px"].items():
        lines.append(f"  --radius-{n}: {v}px;")
    for n, v in t["shadow"].items():
        lines.append(f"  --shadow-{n}: {v};")
    lines.append("}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Design tokens from one brand color")
    ap.add_argument("brand", help="brand hex color, e.g. '#4f46e5'")
    ap.add_argument("--format", choices=["json", "css"], default="json")
    ap.add_argument("--type-ratio", type=float, default=1.25)
    ap.add_argument("--base-size", type=float, default=16)
    ap.add_argument("--out", help="write to file instead of stdout")
    args = ap.parse_args()

    tokens = build(args.brand, args.type_ratio, args.base_size)
    text = to_css(tokens) if args.format == "css" else json.dumps(tokens, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(json.dumps({"written": args.out}))
    else:
        print(text)


if __name__ == "__main__":
    main()
