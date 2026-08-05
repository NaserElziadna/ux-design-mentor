---
name: design-dark-mode
description: This skill should be used when the user asks about "dark mode", "dark theme", "light/dark toggle", "the dark version looks wrong", "colors look weird on dark background", or is adding/reviewing a dark color scheme for any UI.
version: 0.1.0
---

# Dark Mode Design

Read `../design-visual-craft/references/dark-mode.md` first (the researched reference: Material dark-theme spec, elevation overlays, desaturation rules). This skill is the decision procedure.

## The six rules that prevent 90% of dark-mode failures

1. **Never pure black.** Base surface ~`#121212` (Material) or a very dark tint of the brand hue. Pure #000 + pure #fff causes halation for astigmatic users.
2. **Elevation = lighter, not shadow.** Raised surfaces get progressively lighter overlays (Material: +5% white at 1dp → +16% at 24dp). Shadows are nearly invisible on dark.
3. **Desaturate accents.** The light theme's 500–700 tones vibrate on dark; switch to the 200–400 tones of the same scale (`design_tokens.py` generates the full scale — remap, don't invent).
4. **Soften text.** Not pure white: high-emphasis ~87% white (`#E0E0E0`-ish), secondary ~60%, disabled ~38%. Still verify 4.5:1 with `image_tools.py contrast`.
5. **Theme = token remap.** Dark mode is only feasible cleanly when colors are semantic tokens (`--surface`, `--text-primary`) — if hexes are hardcoded per component, fix that first (see `../design-systems/SKILL.md`).
6. **Respect the OS, allow override:** default from `prefers-color-scheme`, persist a manual toggle, no flash-of-wrong-theme (set class before first paint).

## Commonly forgotten surfaces

Form controls and their focus rings, scrollbars, dividers (12% white, not gray hexes), images in white content boxes (add dark-tolerant padding/background), charts (recheck every series color), code blocks, email templates, favicons/logos with dark strokes.

## Review procedure

If reviewing an existing dark theme: extract actual fg/bg pairs and run `python "${CLAUDE_PLUGIN_ROOT}/skills/design-image-tools/scripts/image_tools.py" contrast` on each; check accents against the desaturation rule; check elevation is expressed by surface lightness; check the forgotten-surfaces list above.

- [ ] No #000 surfaces, no #fff text
- [ ] Elevation via lighter surfaces
- [ ] Accents from 200–400 range, measured ≥4.5:1
- [ ] All colors flow through semantic tokens
- [ ] prefers-color-scheme + persisted manual override
- [ ] Forms/scrollbars/dividers/images/charts all themed
