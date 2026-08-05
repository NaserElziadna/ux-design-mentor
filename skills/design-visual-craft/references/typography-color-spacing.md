# Typography, Color, Spacing & Depth (Refactoring UI)

Detailed practical rules from *Refactoring UI* (Adam Wathan & Steve Schoger) — written for people executing visual design without formal design training. Source: [refactoringui.com](https://refactoringui.com/), corroborated by multiple independent chapter summaries.

## Typography

- **Type scale:** hand-pick values instead of using a strict mathematical/modular ratio — a computed scale produces awkward fractional pixel sizes. A workable scale: 12/14/16/18/20/24/30/36/48/64px. Define in px or rem, not em, so the system stays predictable as it composes.
- **Typeface choice:** pick a family with 5+ weights available so you have real range for hierarchy. Match personality to product tone — serif reads elegant/editorial, rounded sans reads friendly/playful, neutral grotesque sans reads plain/utilitarian. This is a deliberate choice, not whatever the framework defaults to.
- **Line length:** 45-75 characters per line for body text — shorter than that feels choppy, longer strains tracking from line to line.
- **Line-height:** scales *inversely* with font size. Large headlines want tight line-height (~1.0-1.1); body text wants loose line-height (~1.5) for readability.
- **Letter-spacing:** increase slightly on all-caps text — caps lose the ascender/descender cues that normally help letter recognition, so more room between characters compensates.
- **Alignment of mixed sizes:** align by baseline, not by vertical center — centering mismatched type sizes looks visually "off" even when the math is centered correctly.
- **Hierarchy with restraint:** use only two font weights (regular + bold) and three text colors (dark/primary, grey/secondary, light-grey/tertiary). To make something more prominent, de-emphasize what's around it rather than adding more emphasis to the target — competing emphasis cancels out.

## Color

- **Palette structure:** build ~8-10 grey shades, 5-10 shades each of one or two primary/brand hues, plus semantic accents (red = destructive/error, yellow = warning, green = positive/success).
- **Use HSL, not hex, to generate shades** — HSL's lightness/saturation axes map to human perception directly, so stepping through them produces perceptually even shades. Hex requires you to eyeball it.
- **Saturation compensation:** as a color gets lighter or darker from its base, bump saturation up slightly, or the mid-tones will look washed out and flat.
- **Grey isn't always grey:** tint your greys slightly warm (toward yellow/orange) or cool (toward blue) rather than using pure desaturated grey — this is a cheap way to give a palette a distinct personality.
- **Never put grey text on a colored background** — it reads muddy. Instead use a lighter, more transparent tint of that background's own hue for de-emphasized text on a colored surface.
- **Hand-pick every shade upfront.** Don't generate palette steps at runtime with `lighten()`/`darken()` CSS functions — the resulting steps are inconsistent and don't compose into a real system.
- **Contrast:** 4.5:1 minimum for normal text, 3:1 for large text (WCAG AA). Prefer dark text on a light background over the reverse when you have the choice — it's generally easier to hit good contrast that way.

## Spacing

- **Use a non-linear spacing scale**, not arbitrary per-component values: 4/8/12/16/24/32/48/64/96/128/192/256px is a workable default.
- **Start with too much space, then remove it.** Most first-draft layouts are too cramped; the fix is almost always to add space, not subtract it.
- **Grouping rule:** the space *around* a group of related elements should be greater than the space *within* that group — this relationship is what visually communicates "these things belong together" (this is the same mechanism as the Law of Common Region / Law of Proximity — see `../../ux-design-principles/references/laws-of-ux.md`).
- **Avoid percentage-based sizing** unless you actually want fluid scaling behavior; prefer `max-width` constraints, and let larger elements shrink proportionally faster than small ones at narrow viewport widths.

## Depth

- **Define ~5 shadow sizes** tied to elevation level: small (buttons, chips), medium (dropdowns, popovers), large (modals, dialogs).
- **A convincing shadow is two-part:** a larger-blur, larger-offset shadow simulating ambient light, plus a tighter, darker shadow simulating a more direct light source. At higher elevations, make the ambient component *more* subtle, not less — real shadows get softer as objects rise further from their surface.
- **Flat-design alternative:** communicate depth via color value instead of shadow — lighter surfaces read as closer, darker surfaces recede. A hard-edged offset shadow with zero blur radius is a valid alternative aesthetic to soft shadows.
- **Overlap across a boundary:** letting an element overlap a background-color/section boundary implies depth without needing a shadow at all.

## Real Content

- Never design final layouts against lorem ipsum or placeholder-blob images assuming real content will "just fit" later — real copy has different lengths and real photography has different crops/aspect ratios than filler, and discovering the mismatch after the layout is built is expensive to fix.
- For user-generated content (avatars, uploaded images), crop into fixed-aspect containers, and use a subtle inner shadow rather than a hard border — unpredictable user image colors clash less against an inner shadow than against a flat border.
- Design empty states deliberately as a first-class state, not an afterthought — they occur constantly (new accounts, cleared filters, zero search results) and are usually the first thing a new user sees.
