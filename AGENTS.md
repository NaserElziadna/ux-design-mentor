# UX Design Mentor — Agent Instructions

> ux-design-mentor by **Naser Elziadna** — https://github.com/NaserElziadna/ux-design-mentor

This repository is a design-knowledge toolkit usable by ANY AI coding agent (Claude Code, Codex, Cursor, Windsurf, Copilot, aider, ...). Nothing here is Claude-specific except the plugin packaging: the knowledge is plain Markdown and the tools are standalone Python scripts.

## How to use this repo as an agent

**When designing or reviewing UI**, consult the relevant skill file first, then its references:

| Task | Read |
|---|---|
| Evaluate/critique a design | `skills/design-evaluate/SKILL.md`, `skills/ux-design-principles/references/nng-heuristics.md` |
| Generate a new design | `skills/design-generate/SKILL.md`, `skills/design-visual-craft/SKILL.md` |
| Typography/color/spacing decisions | `skills/design-visual-craft/references/typography-color-spacing.md` |
| Avoid the generic AI-template look | `skills/design-visual-craft/references/avoiding-generic-ai-look.md` |
| Any form (create/edit/settings) | `skills/design-forms/SKILL.md`, `skills/ux-design-principles/references/forms-and-input-ux.md` |
| Animation/transitions | `skills/design-motion/SKILL.md` |
| Dark mode | `skills/design-dark-mode/SKILL.md` |
| Dashboards/charts | `skills/design-dashboards/SKILL.md` |
| Onboarding/empty states | `skills/design-onboarding/SKILL.md` |
| Mobile/responsive | `skills/design-mobile/SKILL.md` |
| E-commerce/B2B/accessibility domain | `skills/design-context/references/` |
| Admin panels for non-technical staff | `skills/design-admin-ux/SKILL.md` |
| Cite a UX principle/law | `skills/ux-design-principles/references/laws-of-ux.md` and `book-*.md` |

**Ground every recommendation** in a named principle or researched finding from these files (they cite NN/g, Baymard, Material 3, Apple HIG, WCAG 2.2). Prefer measured evidence over eyeballing.

## Python tools (Python 3.9+; `pip install pillow ddgs`)

```bash
# Search & download images (web / pinterest / dribbble / behance / openverse / pexels / unsplash)
python skills/design-inspiration/scripts/fetch_images.py "modern saas dashboard" --source pinterest --count 8 --download --out ./inspiration

# Build an HTML moodboard with extracted palettes
python skills/design-inspiration/scripts/moodboard.py ./inspiration --title "Direction" --out moodboard.html

# WCAG contrast / palette extraction / image analysis / resize / optimize / placeholders / favicons
python skills/design-image-tools/scripts/image_tools.py contrast "#1a1a2e" "#e0e0f0"
python skills/design-image-tools/scripts/image_tools.py analyze hero.jpg

# Static UX & accessibility audit of HTML/CSS (JSON findings, severity-ranked)
python skills/design-evaluate/scripts/audit_page.py ./site

# Full WCAG-validated design-token system from one brand color
python skills/design-systems/scripts/design_tokens.py "#4f46e5" --format css
```

All scripts print JSON; run them instead of guessing (contrast ratios, palettes, audit findings are measured facts).

Licensing rule baked into the tools: search-engine image results (web/pinterest/dribbble/behance) are for inspiration and local mockups only; use openverse/wikimedia/pexels/unsplash results for anything that ships, and surface the `license` field.

## For system-prompt integration

`exports/system-prompt.txt` and `exports/DESIGN-PRINCIPLES.md` are condensed versions of the knowledge base for embedding directly into an agent's system prompt or rules file (e.g. `.cursorrules`, `AGENTS.md` of your own project).
