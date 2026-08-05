# Worked Example: A Starter Design Token Set

A small, concrete token set covering the categories most products need first. Names use a generic convention (`category-variant-property`); adapt the naming convention to whatever the team's tooling expects (CSS custom properties, a JS theme object, Style Dictionary, etc.) — the values and structure matter more than the exact naming scheme.

## Color

```
color-grey-50   = hsl(220, 15%, 98%)   /* lightest background */
color-grey-100  = hsl(220, 15%, 95%)
color-grey-300  = hsl(220, 12%, 85%)   /* borders, dividers */
color-grey-500  = hsl(220, 10%, 60%)   /* secondary text */
color-grey-700  = hsl(220, 12%, 35%)   /* primary text on light bg */
color-grey-900  = hsl(220, 15%, 12%)   /* near-black, headings */

color-primary-100 = hsl(230, 85%, 95%)
color-primary-300 = hsl(230, 80%, 80%)
color-primary-500 = hsl(230, 75%, 55%)  /* base brand color */
color-primary-700 = hsl(230, 75%, 40%)
color-primary-900 = hsl(230, 70%, 25%)

color-success = hsl(150, 60%, 40%)
color-warning = hsl(45, 90%, 50%)
color-danger  = hsl(0, 70%, 50%)
```
Note the saturation bump at the extremes (`color-primary-500` at 75% vs. `color-primary-900` still at 70%, not dropping to 40%) — this is the "increase saturation as you go lighter/darker" rule from `../../design-visual-craft/SKILL.md` that keeps mid-tones from looking washed out.

## Typography

```
font-family-display = "Your Display Font", serif
font-family-body     = "Your Body Font", sans-serif

font-size-xs   = 12px    line-height-xs   = 1.5
font-size-sm   = 14px    line-height-sm   = 1.5
font-size-base = 16px    line-height-base = 1.5
font-size-lg   = 18px    line-height-lg   = 1.4
font-size-xl   = 20px    line-height-xl   = 1.3
font-size-2xl  = 24px    line-height-2xl  = 1.25
font-size-3xl  = 30px    line-height-3xl  = 1.15
font-size-4xl  = 36px    line-height-4xl  = 1.1
font-size-5xl  = 48px    line-height-5xl  = 1.05

font-weight-regular = 400
font-weight-bold    = 700
```

## Spacing

```
space-1 = 4px
space-2 = 8px
space-3 = 16px
space-4 = 24px
space-5 = 32px
space-6 = 48px
space-7 = 64px
space-8 = 96px
```

## Radius

```
radius-sm   = 4px    /* inputs, small buttons */
radius-md   = 8px    /* cards, standard buttons */
radius-lg   = 16px   /* modals, large containers */
radius-full = 9999px /* pills, avatars */
```

## Shadow / Elevation

```
shadow-sm = 0 1px 2px hsl(220 15% 12% / 0.06), 0 1px 1px hsl(220 15% 12% / 0.08)
shadow-md = 0 4px 8px hsl(220 15% 12% / 0.08), 0 2px 4px hsl(220 15% 12% / 0.10)
shadow-lg = 0 12px 24px hsl(220 15% 12% / 0.10), 0 4px 8px hsl(220 15% 12% / 0.08)
```
Each shadow is two-part (a soft, larger ambient shadow plus a tighter, darker one) per the depth rules in `../../design-visual-craft/references/typography-color-spacing.md`.

## How to Use This

This is a starting point, not a prescription — the actual hue, type family, and exact scale values should come from the product's real brand and content needs (see `../../design-visual-craft/SKILL.md` for how to make those choices deliberately). What matters structurally is: every value used anywhere in the UI traces back to one of these named tokens, so a change to `color-primary-500` or `space-4` propagates everywhere at once instead of requiring a search-and-replace across components.
