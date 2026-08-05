# Motion and Microinteractions

Motion in UI exists to communicate, not to decorate. Every animation should answer a functional question — did my tap register, where did that panel come from, what changed — and get out of the way fast. This reference covers duration and easing standards, the anatomy of microinteractions, perceived-performance patterns, and accessibility requirements.

## Purpose-Driven Animation

Animation must serve at least one of these jobs; if it serves none, cut it:

- **Feedback** — confirm an input was received (button press state, ripple, checkmark on save).
- **Orientation** — show where something came from or went (drawer sliding in from its edge, item flying to the cart).
- **Continuity** — connect two states so the change reads as one event, not a jarring swap (shared-element transitions, expanding cards). Material calls this "informative, focused, and expressive" motion (m3.material.io/styles/motion/overview).
- **Status** — communicate that the system is working (loading indicators, progress).

Rule: decoration-only animation (bouncing icons, looping hero effects) adds cognitive load and battery cost with no informational payoff. NN/g: animation should be used "sparingly and purposefully"; gratuitous motion slows task completion (nngroup.com/articles/animation-purpose-ux/).

- [ ] Every animation maps to feedback, orientation, continuity, or status
- [ ] Nothing loops indefinitely except genuine loading states

## Duration Standards

Material Design 3 duration tokens (m3.material.io/styles/motion/easing-and-duration/tokens-specs):

| Scale | Duration | Examples |
|---|---|---|
| Small components | 100–200ms | switches, checkboxes, icon state changes, ripple |
| Medium components | 200–300ms | cards expanding, bottom sheets, menus, FAB morph |
| Large / full-screen | 300–400ms | page transitions, full-screen dialogs |

- Anything over **400ms feels slow** for a standard transition; reserve 400–500ms only for large emphasized full-screen moves (M3 `long` tokens run 450–600ms for emphasized transitions only).
- Exits should be **faster than entrances** (~20–30% shorter — Material 1 baseline: 225ms enter / 195ms exit on mobile), because outgoing content no longer needs attention.
- Hover/press feedback: near-instant, 50–100ms (M3 `short1` = 50ms ripple fade-in, `short2` = 100ms icon change).
- Desktop can run ~30% shorter than mobile (150–200ms typical); distances on screen are perceptually smaller.

- [ ] No standard transition exceeds 400ms
- [ ] Exit durations shorter than enter durations
- [ ] State feedback (hover, press) under 100ms

## Easing

Never use `linear` for UI movement — objects in the real world accelerate and decelerate; linear motion reads as mechanical and cheap (Apple HIG and Material both specify curved easing for interface motion). Reserve linear for opacity-only fades and continuous indicators.

- **Entering elements: ease-out** (decelerate). Start fast, settle gently. M3 `standard-decelerate`: `cubic-bezier(0, 0, 0, 1)`; emphasized-decelerate: `cubic-bezier(0.05, 0.7, 0.1, 1)`.
- **Exiting elements: ease-in** (accelerate). Leave quickly. M3 `standard-accelerate`: `cubic-bezier(0.3, 0, 1, 1)`; emphasized-accelerate: `cubic-bezier(0.3, 0, 0.8, 0.15)`.
- **On-screen moves (A to B): standard curve** — ease-in-out shape. M3 `standard`: `cubic-bezier(0.2, 0, 0, 1)`.
- CSS default `ease` is an acceptable general fallback; `ease-out` is the safest single choice for most UI.

- [ ] No `linear` timing on positional animation
- [ ] Enter = decelerate, exit = accelerate, move = standard

## Anatomy of a Microinteraction (Dan Saffer)

From Saffer's *Microinteractions* (O'Reilly, 2013; microinteractions.com):

1. **Trigger** — what starts it: user action (tap, swipe) or system event (message arrives).
2. **Rules** — what happens: the logic, constraints, and states.
3. **Feedback** — how the user knows what happened: visual, haptic, audio.
4. **Loops & modes** — what happens over time or on repeat: does it change on second use, expire, remember state?

Design each deliberately: e.g., a "like" button — trigger = tap; rules = toggle state, increment count once; feedback = fill + brief scale pop (~150ms); loop = stays filled across sessions.

## Microinteractions Worth Designing

- **Button press** — visible pressed state within 100ms (darken/scale 0.97); never let a tap feel dead.
- **Toggle/switch** — thumb slides with track color crossfade, 150–200ms; state must be readable without color alone.
- **Form validation** — validate on blur, not on every keystroke; error appears with a short fade/slide (150ms) next to the field; success can use a subtle check. Shake animations for hard errors: once, ~300ms, and skip under reduced motion.
- **Pull-to-refresh** — indicator tracks finger 1:1 (direct manipulation), commits past threshold, spinner while loading, content settles with ease-out.
- **Skeleton screens vs spinners** — skeletons for *content-shaped* loads (feeds, cards, lists) where layout is predictable: they set expectations and reduce perceived wait versus spinners. Spinners for short, unshaped, or action-triggered waits (submitting a form). Don't skeleton for <300ms loads — flashing placeholders feel slower than nothing.

- [ ] Every tappable element has a pressed state
- [ ] Validation errors appear near the field, on blur
- [ ] Skeletons match the real content's layout

## Perceived Performance

NN/g response-time limits (nngroup.com/articles/response-times-3-important-limits/, Nielsen 1993):

- **< 0.1s** — feels instantaneous; no feedback needed beyond the state change itself.
- **0.1–1s** — user notices but flow of thought is uninterrupted; no spinner needed (a spinner that flashes for 200ms reads as jank).
- **1–10s** — show an indeterminate indicator (spinner/skeleton) so the user knows the system is working.
- **> 10s** — show a determinate progress bar with percent-done and, ideally, time estimate; provide a way to cancel. Attention is lost beyond 10s.

Tricks:
- **Optimistic UI** — apply the change immediately (like, rename, toggle), sync in background, roll back with an error message on failure. Works when failure is rare and reversible.
- **Delay the spinner** — only show loading UI if the wait exceeds ~300ms–1s; instant spinners make fast responses feel slow.
- **Progress bars should never stall or move backwards**; front-load perceived speed (faster at the start).

- [ ] No spinner for operations that usually finish under ~1s
- [ ] Determinate progress for anything over 10s
- [ ] Optimistic updates for reversible, high-success actions

## Performance: Animate Transform and Opacity Only

Only `transform` and `opacity` can be animated by the browser compositor without triggering layout or paint, which is what keeps animation at 60fps (web.dev/articles/animations-guide). Animating `width`, `height`, `top/left`, `margin`, or `box-shadow` forces layout/paint every frame and causes jank on mid-range devices.

- Move with `transform: translate()`, size with `transform: scale()`, fade with `opacity`.
- Fake expensive effects: crossfade two shadow layers via opacity instead of animating `box-shadow`.
- Use `will-change: transform` sparingly and only just before animating; remove after.

- [ ] Animations touch only transform and opacity
- [ ] Verified no layout thrash in DevTools performance panel

## Reduced Motion (WCAG 2.3.3)

WCAG 2.2 SC 2.3.3 "Animation from Interactions" (AAA): motion animation triggered by interaction can be disabled unless essential (w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html). Vestibular disorders make large parallax, zoom, and multi-directional motion physically nauseating. Respect the OS setting:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Better than nuking everything: replace movement with opacity crossfades — reduced motion means reduced *movement*, not zero feedback. Keep essential status indicators (progress bars) functional.

- [ ] Site honors `prefers-reduced-motion`
- [ ] Parallax, auto-playing motion, and large zooms disabled under reduced motion
- [ ] Feedback preserved as fades, not removed entirely

## Entrance Choreography and Stagger

When multiple elements enter (list items, dashboard cards), stagger them so the eye follows one wave instead of a simultaneous pop:

- Stagger interval: **20–50ms** between siblings (Material recommends short offsets; total sequence should still finish within ~400–500ms).
- Cap the stagger: after ~6 items, load the rest together — a 20-item cascade wastes seconds.
- Direction should follow reading order or the spatial origin of the trigger (top-down for lists, outward from a tapped card).
- Choreograph one container, not the whole page; competing simultaneous animations read as chaos.

- [ ] Stagger 20–50ms, capped at ~6 items
- [ ] Total entrance sequence under ~500ms

## Sources

- https://m3.material.io/styles/motion/easing-and-duration/tokens-specs
- https://m3.material.io/styles/motion/overview
- https://www.nngroup.com/articles/response-times-3-important-limits/
- https://www.nngroup.com/articles/animation-purpose-ux/
- https://developer.apple.com/design/human-interface-guidelines/motion
- https://web.dev/articles/animations-guide
- https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
- Dan Saffer, *Microinteractions* (O'Reilly, 2013) — https://microinteractions.com
