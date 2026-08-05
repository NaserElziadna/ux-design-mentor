---
name: design-motion
description: This skill should be used when the user asks about "animation", "transitions", "motion design", "microinteractions", "hover effects", "loading animation", "skeleton screens", "how long should this animation be", "easing", "the animation feels slow/janky", or is adding/reviewing any UI motion — durations, easing curves, feedback animations, loaders, reduced-motion accessibility.
version: 0.1.0
---

# Motion & Animation Design

Read `references/../../design-visual-craft/references/motion-and-microinteractions.md` (the full researched reference: Material 3 duration/easing tokens, NN/g response-time limits, microinteraction anatomy) before giving motion advice. This skill is the decision procedure on top of it.

## Decision procedure

1. **Justify first.** Every animation must serve feedback, orientation, continuity, or status. If it serves none — recommend cutting it, not tuning it.
2. **Pick duration by size** (Material 3): small components 100–200ms, medium (cards, panels) 200–300ms, large/full-screen 300–400ms. Over 400ms feels slow (Doherty threshold); under ~80ms is invisible.
3. **Pick easing by direction:** entering → ease-out (decelerate, `cubic-bezier(0.05,0.7,0.1,1)`), exiting → ease-in (accelerate), moving on screen → standard `cubic-bezier(0.2,0,0,1)`. Never `linear` for UI, never default `ease` for large moves.
4. **Loading:** <1s show nothing; 1–10s spinner or skeleton (skeleton when layout is known — perceived as faster); >10s progress bar + time estimate + cancel (NN/g limits).
5. **Performance:** animate only `transform` and `opacity`; never `width/height/top/left` (layout thrash). Add `will-change` only during the animation.
6. **Accessibility (non-negotiable):** ship the `prefers-reduced-motion` block — replace movement with opacity fades, kill parallax/autoplay. WCAG 2.3.3.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

## When reviewing existing motion

Grep the CSS for `transition`, `animation`, `@keyframes` and check each against: justified purpose? duration in band? correct easing direction? transform/opacity only? reduced-motion fallback present? Report violations with measured values ("transition: all 800ms ease — 2× over the 400ms ceiling, animates `all` including layout properties").

## Checklist

- [ ] Every animation maps to feedback / orientation / continuity / status
- [ ] Durations: 100–400ms band, sized to element scale
- [ ] Ease-out in, ease-in out, no linear
- [ ] transform/opacity only
- [ ] prefers-reduced-motion handled
- [ ] Loading states follow the 1s/10s thresholds
