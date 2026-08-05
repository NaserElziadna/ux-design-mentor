# Dark Mode Design

Dark mode is not inverted light mode — it is a separate theme with its own rules for surfaces, elevation, color saturation, and contrast. Done well it reduces eye strain in dim environments and saves power on OLED; done as a naive inversion it produces vibrating colors, invisible dividers, and glowing text. This reference gives the concrete values.

## Never Pure Black Backgrounds

- Use dark gray, not `#000000`. Material Design's recommended baseline dark surface is **#121212** (material.io/design/color/dark-theme.html).
- Why: pure white text on pure black hits ~21:1 contrast, which causes **halation** — text appears to glow and bleed, especially for users with astigmatism (roughly a third to half of adults have some). Dark gray softens the edge.
- Dark gray also leaves headroom to express elevation with even-lighter surfaces (see next section); from #000 there is nowhere obvious to go.
- Exception: true-black OLED themes are a legitimate user *option* (battery savings), but default to near-black gray.

- [ ] Base background is #0D0D0D–#1A1A1A range, not #000
- [ ] Text is not pure white on the darkest surface

## Elevation via Lighter Surfaces, Not Shadows

Shadows are nearly invisible on dark backgrounds, so Material expresses elevation by lightening the surface — compositing a semi-transparent white overlay whose opacity scales with elevation (material.io/design/color/dark-theme.html, "Elevation overlays"):

| Elevation | White overlay |
|---|---|
| 0dp | 0% |
| 1dp | 5% |
| 2dp | 7% |
| 3dp | 8% |
| 4dp | 9% |
| 6dp | 11% |
| 8dp | 12% |
| 12dp | 14% |
| 16dp | 15% |
| 24dp | 16% |

- Practical translation: on #121212, a card at 1dp ≈ #1E1E1E, a dialog at 24dp ≈ #383838.
- The rule: **higher = lighter**. A modal must be visibly lighter than the page behind it.
- M3 replaces literal overlays with `surface-container` token tiers (lowest→highest) plus surface tint — same principle, tokenized (m3.material.io/styles/color/the-color-system/color-roles).

- [ ] Elevation ladder defined as 4–6 surface tones, each lighter than the last
- [ ] Overlays/tokens used consistently — no ad-hoc grays per component

## Desaturate Accent Colors

Saturated colors (Material 500–700 tones) optically **vibrate** against dark surfaces and fail contrast as text. Material's guidance: use the lighter, less saturated **200–400 tones** in dark themes (material.io/design/color/dark-theme.html).

- Example: primary `#6200EE` (purple 500) in light mode becomes `#BB86FC` (purple 200) in dark mode — Material's own baseline pair.
- Fully saturated red error text on #121212 is unreadable; Material's dark error color is `#CF6679` (a desaturated tone), not `#B00020`.
- Large filled areas of bright saturated color are even worse than text — mute fills, or use the color as a tinted-surface/outline treatment instead.

- [ ] Every accent has a dark-mode variant 2–3 tone steps lighter/less saturated
- [ ] Error/success/warning colors have desaturated dark variants

## Contrast: Enough, But Not Too Much

- WCAG still applies: body text needs **4.5:1** minimum, large text 3:1, UI components 3:1 (WCAG 2.2 SC 1.4.3 / 1.4.11, w3.org/TR/WCAG22/). Dark mode is not an exemption, and remember the elevated (lighter) surfaces are the ones most likely to fail.
- But avoid *maximum* contrast: pure `#FFFFFF` on #121212 causes halation and fatigue. Material specifies high-emphasis text at **87% opacity white** (≈ `#E0E0E0`–`#DEDEDE` on #121212), medium-emphasis at 60%, disabled at 38% (material.io/design/color/text-legibility.html).
- Check contrast against the lightest surface in your elevation ladder, not just the base background.

- [ ] Body text ≥ 4.5:1 against its actual surface
- [ ] Primary text ~87% white, secondary ~60%, never 100%

## Semantic Tokens Are the Prerequisite

Dark mode is only cheap if color is referenced through **semantic tokens** (`surface`, `surface-container`, `on-surface`, `primary`, `outline`), never hardcoded hexes. Theming then becomes a token remap — one file, not a codebase audit.

- Name tokens by role, not appearance: `text-secondary`, not `gray-600` (a "gray-600" that turns light in dark mode is a lie).
- Two layers: primitive palette (gray-100…900) → semantic aliases that flip per theme. Components consume only the aliases.
- Audit trick: grep the codebase for `#` hex literals and raw `rgb(` in component code; each hit is a dark-mode bug waiting.

- [ ] Zero hardcoded color values in components
- [ ] Every semantic token has a defined value in both themes

## Images, Illustrations, and Media

- Photos at full light-mode brightness glare against dark surfaces. Common fix: `filter: brightness(0.85)` (or ~0.8–0.9) on images in dark mode, removed on hover if fidelity matters.
- Illustrations with **pure white backgrounds become glowing boxes**. Use transparent-background assets, or supply dark-mode variants via `<picture>` + `source media="(prefers-color-scheme: dark)"`.
- Logos: provide a dark-mode variant (dark wordmarks vanish on dark surfaces).
- White content areas that must stay white (document previews, embedded checkout) should get a subtle border so they read as intentional cards, not errors.

- [ ] Images dimmed ~10–20% in dark mode
- [ ] No opaque white asset backgrounds; dark logo variant exists

## Shadows Become Borders and Tints

Since shadows barely register on dark surfaces, replace or supplement depth cues:

- Swap `box-shadow` separation for a **1px border** in a low-contrast outline color (e.g., `rgba(255,255,255,0.12)` — Material's divider opacity) plus the lighter-surface step.
- M3's approach: **surface tint** — elevated surfaces take a faint wash of the primary color instead of a shadow.
- Keep a faint shadow only where a surface overlaps a *lighter* one (menus over cards).

- [ ] Cards/menus separated by surface step + subtle border, not shadow alone
- [ ] Dividers at ~12% white opacity, verified visible (3:1 for meaningful boundaries)

## System Preference + Manual Override

Respect the OS, but let users override per-site (web.dev/articles/prefers-color-scheme):

```css
:root { color-scheme: light dark; /* light tokens */ }
@media (prefers-color-scheme: dark) { :root { /* dark tokens */ } }
/* Manual override wins: */
:root[data-theme="light"] { /* light tokens */ }
:root[data-theme="dark"]  { /* dark tokens */ }
```

- Offer three states: Light / Dark / System. Persist the choice (localStorage) and apply it in a blocking inline script before first paint to avoid the wrong-theme flash (FART).
- Declare `color-scheme: light dark` (CSS or meta) so the browser themes form controls, scrollbars, and default UI to match.

- [ ] Three-way toggle (light/dark/system), persisted
- [ ] No flash of wrong theme on load; `color-scheme` declared

## Testing Checklist

- [ ] Contrast-check every text/surface pair in the dark palette (both base and elevated surfaces)
- [ ] Form controls, selects, checkboxes, and scrollbars themed (not white islands)
- [ ] Focus rings visible on dark surfaces (3:1 against adjacent colors)
- [ ] Charts/data-viz palettes have dark variants (see saturation rules)
- [ ] Test on OLED at low screen brightness in a dim room — smearing and halation show up here
- [ ] Test with browser/OS toggled both ways plus manual override in each

## Common Mistakes

- **Inverted grayscale**: mechanically flipping gray-100↔gray-900 breaks elevation logic (in light mode elevation is shadow on same-color surfaces; in dark mode elevation is lighter surfaces) and produces harsh 21:1 text.
- **Forgetting native UI**: unthemed form controls, autofill styles, scrollbars, and `<select>` dropdowns render blinding white — set `color-scheme` and style them.
- **Low-contrast dividers**: light-mode `#E0E0E0` borders hardcoded on dark surfaces are invisible; divider tokens must flip to white-at-low-opacity.
- **Reusing light-mode shadows**: black shadows on near-black backgrounds communicate nothing.
- **Saturated brand color kept as-is**: vibrates and fails contrast — desaturate/lighten it (see above).
- **Only testing the base surface**: contrast failures usually hide on elevated surfaces and hover states.

## Sources

- https://material.io/design/color/dark-theme.html
- https://m3.material.io/styles/color/the-color-system/color-roles
- https://material.io/design/color/text-legibility.html
- https://codelabs.developers.google.com/codelabs/design-material-darktheme
- https://web.dev/articles/prefers-color-scheme
- https://www.w3.org/TR/WCAG22/ (SC 1.4.3, 1.4.11)
- https://www.nngroup.com/articles/dark-mode/
- https://design.google/library/material-design-dark-theme
