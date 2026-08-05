---
name: design-visual-craft
description: This skill should be used when the user asks to "make this look better", "improve the visual design", "this looks generic/templated/like every other AI site", "help with typography", "pick a color palette", "the spacing feels off", "make this look more polished/professional/distinctive", or needs concrete visual execution guidance (type, color, spacing, layout, depth) rather than UX process or psychology feedback.
version: 0.1.0
---

# Visual Design Craft

Concrete visual execution — typography, color, spacing, layout, depth — grounded in Refactoring UI's practical system and current research on why AI/template-generated interfaces look generic, so recommendations name specific values and choices instead of vague aesthetic opinions.

## Overview

The other skills in this plugin (`design-evaluate`, `design-generate`, `design-context`) cover UX *process* and *psychology* — affordances, feedback, user research, domain priorities. None of them tell you what pixel values to actually use. This skill fills that gap: it's about the craft decisions — type scale, color system, spacing, depth — that separate a design that merely follows good UX principles from one that also looks intentional, not templated.

**This skill is not about opinions ("make it cleaner").** Every recommendation should name a specific scale, ratio, or value, and explain what perceptual/cognitive effect it produces. "Increase the line-height" is not actionable; "line-height 1.5 for body text, 1.1 for the headline — line-height should scale inversely with font size" is.

**User preferences:** Check whether `.claude/ux-design-mentor.local.md` exists in the project. If it sets `output_style`, use that format by default.

## Why This Matters: The Generic-AI-Look Problem

Left to default choices, generated UI converges on the same look: a purple-to-blue gradient hero, Inter/Poppins everywhere, a bento grid of three feature cards, 1px grey borders on every card, floating 3D gradient blobs, and centered generic line icons. This isn't a coincidence — it's what "the statistical average of training data" looks like when no deliberate decision overrides it. See `references/avoiding-generic-ai-look.md` for the specific named anti-patterns and what to do instead.

**The fix is decision, not decoration.** Lock a small set of values upfront — a type scale, a color system, a spacing scale — before generating or reviewing UI, and every subsequent choice becomes "does this match the system" instead of "does this look okay." That discipline is what `references/typography-color-spacing.md` gives you.

## Core Framework

### Typography

- Hand-pick a **type scale**: e.g. 12/14/16/18/20/24/30/36/48/64px — not a rigid mathematical ratio, which produces awkward fractional values.
- Pick a typeface with **5+ weights available**; the personality of the font (serif = elegant, rounded sans = playful, neutral grotesque = plain/utilitarian) should match the product's actual tone, chosen deliberately, not defaulted to whatever the framework ships with.
- Line length: **45–75 characters per line** for body text. Line-height scales *inversely* with font size — tight (~1.1) for large headlines, loose (~1.5) for body copy.
- Build hierarchy with restraint: **two font weights** (regular + bold) and **three text colors** (primary/dark, secondary/grey, tertiary/light-grey) are usually enough — de-emphasize the less important elements rather than adding more emphasis to the important one.

### Color

- Build three palette categories: **8-10 grey shades**, **5-10 shades each of one or two primary/brand colors**, plus semantic accents (red = destructive, yellow = warning, green = positive).
- Generate shades in **HSL**, not hex — it maps to how humans actually perceive lightness/saturation. Going lighter or darker from a base color, **increase saturation** slightly or the midtones look washed out.
- Don't put grey text directly on a colored background — it looks muddy. Use a lighter/more-transparent tint of that background's own hue instead.
- Hand-pick every shade upfront; don't generate them on the fly with `lighten()`/`darken()` functions, which produce inconsistent steps.
- Cap the palette to roughly **60% dominant / 30% neutral / 10% accent** — this is also the single fastest fix for the "purple-gradient AI look," which comes from having no real palette discipline at all.

### Spacing & Layout

- Use a **non-linear spacing scale**: 4/8/12/16/24/32/48/64/96/128px. Don't invent ad-hoc pixel values per component.
- Start with more whitespace than feels necessary, then remove it — most first drafts are too cramped, not too loose.
- **Space around a group should exceed space within it** — that relationship is what visually signals grouping (this is also Gestalt's Law of Proximity, see `../ux-design-principles/references/laws-of-ux.md`).
- Break the "everything in a 3-column bento grid" default: vary section rhythm down the page, use one clear focal point per screen, and let asymmetry do work that a uniform grid can't.

### Depth

- Define ~5 shadow sizes (small → button, medium → dropdown, large → modal). A convincing shadow is two-part: a larger-blur "ambient" shadow plus a tighter, darker "direct" shadow — make the ambient one subtler at higher elevation.
- Flat-design alternative: communicate depth with color value alone (lighter = closer, darker = recedes), or a hard offset shadow with zero blur.
- Prefer whitespace and a subtle background-lightness shift over a 1px grey border as the default way to separate cards — borders-on-everything is a named anti-pattern (see reference file).

### Real Content

- Never design against lorem ipsum or vague placeholder blobs expecting real content to "just fit" later — real copy has different lengths and real photos have different crops, and this changes layout decisions that are expensive to unwind afterward.
- Design empty states deliberately; they're a real, frequent state, not an edge case to skip.

## Evaluating an Existing Design

When reviewing a design for visual craft (as opposed to UX process), check:
- [ ] Is there a consistent type scale, or do font sizes look ad-hoc?
- [ ] Is the color palette intentional (named roles: primary, neutral, accent, semantic) or default/arbitrary?
- [ ] Does spacing follow a scale, and does grouping spacing exceed internal spacing?
- [ ] Does this design have at least one deliberate, distinguishing visual choice, or could it be any product in this category?
- [ ] Cross-check against `references/avoiding-generic-ai-look.md` — does it hit any of the named generic-AI-look anti-patterns?

## Additional Resources

- **`references/typography-color-spacing.md`** — Full Refactoring UI-grounded rules with more detail and rationale
- **`references/avoiding-generic-ai-look.md`** — Named anti-patterns, concrete alternatives, and platform baseline conventions (Apple HIG vs. Material Design 3)
- **`examples/before-after.md`** — A worked example turning generic feedback into visual-craft-grounded feedback
- **`references/motion-and-microinteractions.md`** — Duration/easing standards, microinteraction anatomy, skeleton vs spinner, prefers-reduced-motion
- **`references/dark-mode.md`** — Surface elevation, desaturated accents, token-based theming, common dark-mode mistakes
- **`../ux-design-principles/references/laws-of-ux.md`** — The cognitive mechanisms (Fitts's, Hick's, proximity, etc.) behind several of the rules above
- **`../design-systems/SKILL.md`** — Once these decisions are made, formalize them as design tokens so they stay consistent at scale
