---
name: design-inspiration
description: This skill should be used when the user asks to "find design inspiration", "scrape images", "search Google/Pinterest/Dribbble for images", "get images for my mockup", "find reference designs", "I need photos for this landing page", "download stock images", or whenever building/designing a UI that needs real images (hero photos, avatars, product shots, moodboards) instead of gray placeholder boxes.
version: 0.1.0
---

# Design Inspiration & Image Sourcing

Search and download images from the internet for two distinct jobs:

1. **Inspiration / reference** — collect real-world examples (Pinterest pins, Dribbble shots, Behance projects, general web images) before designing, to ground visual direction in what actually exists.
2. **Mockup assets** — fill designs with real photos instead of gray boxes, because a design can only be evaluated honestly with realistic content (see `design-visual-craft`).

## The Script

`scripts/fetch_images.py` — stdlib-only Python, prints JSON, optional download.

```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/design-inspiration/scripts/fetch_images.py" \
  "modern fintech dashboard dark mode" --source pinterest --count 10 --download --out ./inspiration
```

**Sources:**

Best results require the `ddgs` package (`pip install ddgs`) — the script falls back to a flakier Bing scrape without it, so install it on first use if missing.

| `--source` | What it searches | Key needed | Use for |
|---|---|---|---|
| `web` (default) | Whole web (DuckDuckGo/Bing image index) | no | broad reference search |
| `pinterest` | pinterest.com only | no | moodboards, style inspiration |
| `dribbble` | dribbble.com only | no | UI shots, component ideas |
| `behance` | behance.net only | no | full case studies, branding |
| `openverse` | Openly-licensed images | no | images you can ship |
| `wikimedia` | Wikimedia Commons | no | free-license photos/illustrations |
| `pexels` | Pexels stock | `PEXELS_API_KEY` | production-quality photos |
| `unsplash` | Unsplash stock | `UNSPLASH_ACCESS_KEY` | production-quality photos |

Output is JSON: `title`, `image_url`, `thumbnail`, `source_page`, `width`, `height`, `license` (+ `local_path` when `--download`).

## Workflow

**Building a moodboard / gathering references:**
1. Run 2–3 searches with different phrasings (`pinterest` + `dribbble` give different flavors).
2. Download to a project `inspiration/` folder, then Read the images to analyze them — extract common patterns (layout, palette, type treatment) and report them to the user, citing 2–3 specific reference images.
3. Feed conclusions into `design-generate` or `design-visual-craft`.

**Filling a mockup with images:**
1. Prefer `pexels`/`unsplash` (if keys set), else `openverse`/`wikimedia` — these are license-safe.
2. Match photo mood to the design's intended feel (see `design-visual-craft` on realistic content).
3. After download, use `design-image-tools`' `image_tools.py` to resize/crop/optimize and to extract a palette from the hero image so UI colors harmonize with it.

## Licensing rules (always follow)

- `web` / `pinterest` / `dribbble` / `behance` results are **third-party copyrighted work**: use only for local inspiration, moodboards, and throwaway mockups. Never commit them to a shipping product, and tell the user so when relevant.
- For anything that ships: `openverse`, `wikimedia`, `pexels`, `unsplash` — and surface the `license` field to the user.
- Pinterest/Dribbble/Behance are searched via DuckDuckGo's index (no ToS-violating site scraping, no login).

## Failure modes

- `web`/`pinterest`/`dribbble`/`behance` failing or returning irrelevant results → ensure `pip install ddgs` (the Bing fallback gets bot-detected under repeated use), else fall back to `openverse`.
- If a download 403s (hotlink protection), use the `thumbnail` URL or another result.
- No network / blocked environment → generate placeholders with `design-image-tools` instead.

## Moodboard Builder

After downloading references, assemble them into a shareable HTML moodboard (thumbnail grid + per-image palette strips + an aggregated "direction palette" across all references):

```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/design-inspiration/scripts/moodboard.py" ./inspiration --title "Coffee shop landing" --out moodboard.html
```

Requires Pillow. The `direction_palette` in its JSON output is the cross-reference color consensus — feed it into `design-systems`' `design_tokens.py` or `design-visual-craft` decisions.
