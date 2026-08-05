---
name: design-mobile
description: This skill should be used when the user asks about "mobile design", "responsive design", "touch targets", "mobile navigation", "bottom nav vs hamburger", "does this work on phones", "mobile version looks broken", or is building/reviewing any mobile or responsive interface.
version: 0.1.0
---

# Mobile & Touch Design

Read `../design-context/references/touch-and-mobile-standards.md` first (the researched standards: Apple/Material/WCAG target sizes, Hoober's thumb-zone research, mobile keyboards) and `../design-context/references/mobile.md` for broader mobile strategy. This skill is the decision procedure.

## The numbers that are not negotiable

- Touch targets: 44×44pt (Apple) / 48×48dp + 8dp gaps (Material); WCAG 2.5.8 AA floor is 24×24 CSS px. When in doubt: 48px.
- Body text ≥16px — also prevents iOS zoom-on-focus for inputs.
- Thumb zone (Hoober: 49% use one hand): primary actions in the bottom third; destructive actions OUT of the easy-reach zone.

## Decision procedure

1. **Navigation:** ≤5 top-level destinations → bottom nav bar (visible, thumb-reachable, Jakob's Law). More → bottom nav + "More" sheet before resorting to hamburger (hamburger halves discoverability of what's inside).
2. **Inputs:** right keyboard per field (`inputmode`, `type`, `autocomplete`); segmented controls or chips instead of dropdowns for ≤5 options (native pickers cost taps); date pickers only for nearby dates — typed input for birthdates.
3. **Gestures:** every gesture needs a visible alternative (WCAG 2.5.1) — swipe-to-delete duplicated by an edit-mode button; no gesture-only features; respect the OS back gesture.
4. **Layout:** design at 360–390px first; content in one column; sticky primary CTA at bottom when the page's job is one action (checkout, signup); safe-area insets (`env(safe-area-inset-*)`) for notch/home-indicator.
5. **States mobile makes worse:** slow network (skeletons, optimistic UI), offline (queue + sync, tell the user), interrupted sessions (persist form state aggressively).
6. **Test the review claims:** with browser tools available, resize to 390×844 and screenshot (the `visual-reviewer` agent does this) — don't reason about responsive behavior from desktop CSS alone.

## Review checklist

- [ ] All targets ≥44px with adequate spacing; measured, not guessed
- [ ] Primary actions in the bottom thumb zone; destructive out of it
- [ ] Body ≥16px; inputs ≥16px; correct keyboards + autocomplete
- [ ] Every gesture has a visible-button alternative
- [ ] No horizontal scroll at 360px; safe areas handled
- [ ] Orientation works or is justified (WCAG 1.3.4); offline/slow states designed
