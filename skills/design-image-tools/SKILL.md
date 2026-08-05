---
name: design-image-tools
description: This skill should be used when the user asks to "extract a color palette from an image", "check color contrast", "is this WCAG compliant" (for colors), "resize/crop/optimize images for web", "generate a placeholder image", "make favicons", "can I put text over this image", or when a design task needs image processing — palette harmonization, contrast validation, web optimization, placeholders, favicon sets.
version: 0.1.0
---

# Design Image Tools

One Python script, `scripts/image_tools.py`, with seven design-focused commands. All output is JSON. Requires Pillow (`pip install pillow`) except `contrast` and SVG placeholders, which are stdlib-only.

```bash
TOOLS="${CLAUDE_PLUGIN_ROOT}/skills/design-image-tools/scripts/image_tools.py"
```

| Command | What it does | Example |
|---|---|---|
| `palette` | Dominant colors + luminance + contrast vs black/white for each | `python "$TOOLS" palette hero.jpg --colors 6` |
| `contrast` | WCAG 2.2 contrast ratio + AA/AAA pass/fail verdict | `python "$TOOLS" contrast "#1a1a2e" "#e0e0f0"` |
| `analyze` | Size, aspect ratio, luminance, busyness, palette, text-overlay advice | `python "$TOOLS" analyze hero.jpg` |
| `resize` | Smart center-crop to exact dimensions | `python "$TOOLS" resize hero.jpg --size 1600x900 --out hero-web.jpg` |
| `optimize` | Compress file or whole folder for web (`--webp`, `--max-width`) | `python "$TOOLS" optimize ./assets --webp --max-width 1920` |
| `placeholder` | Branded gradient placeholder, SVG or PNG, auto-picks legible text color | `python "$TOOLS" placeholder --size 800x450 --text "Hero" --color "#4f46e5" --out ph.svg` |
| `favicon` | 16/32/48/180/512 PNGs + multi-size .ico from a logo | `python "$TOOLS" favicon logo.png --out ./favicons` |

## When to reach for each

- **Starting a design around a hero image** → `analyze` it first: it tells you the aspect ratio, whether text can sit on it safely, and gives a palette to harmonize UI colors with (feeds `design-visual-craft`).
- **Choosing text/background colors** → always verify with `contrast` before recommending a pair. Quote the ratio and the AA/AAA verdict, never eyeball it. (WCAG: 4.5:1 normal text, 3:1 large text and UI components.)
- **User's page has downloaded/stock images** → `resize` to the exact slot size, then `optimize --webp`; report the KB savings.
- **No real image available and network is blocked** → `placeholder` with the project's brand color, so mockups still look intentional rather than gray-box generic.
- **Shipping a site** → `favicon` from the logo; wire the sizes into `<link rel="icon">` / `apple-touch-icon`.

## Workflow with other skills

1. `design-inspiration` downloads reference/stock images →
2. `analyze` + `palette` extract facts and colors →
3. `design-visual-craft` turns them into type/color/spacing decisions →
4. `contrast` validates every text/background pair →
5. `resize` + `optimize` prepare final assets.
