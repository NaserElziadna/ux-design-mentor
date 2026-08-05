# Touch and Mobile Standards

Mobile interfaces fail for physical reasons before visual ones: fingers are imprecise (~7–10 mm contact patch), thumbs have limited reach, and networks drop. Apple, Google, and the W3C publish hard numbers for target sizes, and Steven Hoober's field research shows how people actually hold phones. Design to these standards rather than to how the layout looks in a desktop browser.

## Touch Target Sizes

- Apple HIG: minimum 44×44 pt for any tappable element (Apple HIG "Layout" / "Buttons").
- Material Design 3: minimum 48×48 dp touch target, with at least 8 dp between targets; the visual element may be smaller (e.g., a 24 dp icon) as long as the touch area is 48 dp (Material Design 3 accessibility guidance).
- WCAG 2.2 SC 2.5.8 Target Size (Minimum), Level AA: targets at least 24×24 CSS px, or spaced so a 24 px circle centered on each target doesn't intersect another; exceptions for inline links and equivalent alternatives (W3C WCAG 2.2).
- WCAG 2.5.5 Target Size (Enhanced), Level AAA: 44×44 CSS px (W3C).
- Practical rule: build to 48 dp / 44 pt; treat WCAG's 24 px as an absolute floor, not a goal.
- Increase padding, not just icon size; keep destructive actions physically separated from frequent ones.

Checklist:
- [ ] All tappable elements ≥ 44 pt / 48 dp
- [ ] ≥ 8 dp spacing between adjacent targets
- [ ] Nothing interactive smaller than 24×24 CSS px (WCAG 2.5.8)

## Thumb Zones and One-Handed Use

- Steven Hoober observed 1,300+ phone users (2013): 49% used one hand, 36% cradled (hold with one hand, tap with the other), 15% used two hands/two thumbs (Hoober, "How Do Users Really Hold Mobile Devices?", UXmatters; summarized in Smashing Magazine "The Thumb Zone").
- Grips shift constantly during a session; design for the one-handed case because it is both common and most constrained (Hoober).
- The comfortable thumb arc covers roughly the bottom third and center of the screen; top corners (especially the corner opposite the thumb) are hardest to reach (Smashing Magazine; Hoober's later research notes people focus and tap most accurately at the center of the screen).
- Put primary actions and navigation in the bottom half; put destructive or rarely used actions in hard-to-reach zones deliberately.

Checklist:
- [ ] Primary actions reachable by a right or left thumb in one-handed grip
- [ ] Nothing critical pinned to the top corners on tall phones
- [ ] Destructive actions outside the easy-reach zone

## Navigation: Bottom Bar vs. Hamburger

- Prefer visible bottom navigation (3–5 top-level destinations) over a hamburger menu: hidden navigation measurably reduces discoverability, usage, and task success (NN/g "Hamburger Menus and Hidden Navigation"; Material 3 navigation bar; Apple HIG tab bars).
- Bottom placement matches the thumb zone; both Apple (tab bar) and Material (navigation bar) make it the default pattern.
- Use a hamburger/overflow only for genuinely secondary destinations, never as the sole navigation.
- Label icons with text — icon-only navigation is ambiguous (NN/g).

Checklist:
- [ ] 3–5 primary destinations in a bottom bar with text labels
- [ ] Hamburger reserved for secondary items

## Safe Areas, Notches, and System Gestures

- Respect safe area insets (`env(safe-area-inset-*)` on the web; safe area layout guides on iOS): content and controls must not sit under the notch/Dynamic Island, rounded corners, or the home indicator (Apple HIG "Layout").
- Keep interactive elements out of system gesture zones (bottom edge home-indicator swipe, left/right back-swipe edges) or they will conflict with OS gestures (Apple HIG; Android gesture navigation guidance).
- Extend backgrounds edge-to-edge, but inset content.

Checklist:
- [ ] Layout uses safe-area insets on notched devices
- [ ] No custom controls in the home-indicator or edge-swipe zones

## Gestures: Affordance and Discoverability

- Gestures are invisible; never make a swipe/long-press the only way to reach a function — provide a visible alternative (NN/g on gesture discoverability; Apple HIG "Gestures").
- WCAG 2.2 SC 2.5.1 Pointer Gestures (A): any multipoint or path-based gesture (pinch, swipe-to-delete) must have a single-pointer alternative (W3C).
- WCAG 2.5.4 Motion Actuation (A): functions triggered by shaking/tilting need a UI alternative and a way to disable motion triggers (W3C).
- Teach gestures with partial reveals (a list item peeking), brief hints on first use, and consistent platform conventions — don't invent novel gestures for core tasks.

Checklist:
- [ ] Every gesture has a visible button/menu equivalent (WCAG 2.5.1)
- [ ] Motion-based triggers optional and disable-able (WCAG 2.5.4)

## Mobile Typography and Feedback Timing

- Body text minimum 16 px. iOS Safari auto-zooms any focused input with font-size under 16 px, breaking the layout — set inputs to ≥ 16 px rather than disabling zoom (never use `user-scalable=no`; WCAG 1.4.4 requires 200% zoom).
- Apple's default body style is 17 pt (Apple HIG Typography); Material 3 body-large is 16 sp. Treat 12 px as the floor for captions only.
- Tap feedback must appear within ~100 ms to feel instantaneous (NN/g / Nielsen's response-time limits: 0.1 s = instantaneous, 1 s = flow limit, 10 s = attention limit). Show pressed states immediately even if the resulting action takes longer.
- Ensure `touch-action: manipulation` or equivalent so taps aren't delayed waiting for double-tap detection.

Checklist:
- [ ] Body text and all inputs ≥ 16 px; pinch-zoom never disabled
- [ ] Visible pressed state within 100 ms of touch

## Mobile Form Specifics

- Trigger the right keyboard: `type="email"`, `type="tel"`, `inputmode="numeric"` for PINs/codes/card numbers; add `autocomplete` tokens so autofill works (WCAG 1.3.5; Baymard).
- Avoid dropdowns for few options: for 2–5 mutually exclusive choices use radio buttons or a segmented control instead — dropdowns cost two taps, hide options, and require scrolling in a picker (Baymard "Drop-Down Usability"; Apple HIG segmented controls; GOV.UK avoids select where possible).
- Use native pickers for dates/times; use steppers for small quantity ranges.
- Pull-to-refresh: use only for user-updated, reverse-chronological content feeds (its original context — Loren Brichter's Tweetie pattern, standardized in Material's swipe-to-refresh); always pair with an automatic refresh and a visible loading indicator; don't hijack scroll on web.

Checklist:
- [ ] Correct keyboard per input; autofill supported
- [ ] ≤ 5 options rendered as segmented control/radios, not a dropdown
- [ ] Pull-to-refresh only on feed-type content

## Orientation, Offline, and Slow Networks

- WCAG 1.3.4 Orientation (AA): don't lock content to portrait or landscape unless the orientation is essential (piano app, bank check capture) (W3C).
- Preserve state and scroll position on rotation.
- Design explicit offline/slow-network states: show cached content with a "you're offline" banner rather than a dead error screen; queue user actions for retry; use skeleton screens for loads over ~1 s and never spinners alone for long waits (NN/g progress-indicator guidance).
- Set timeouts and offer retry buttons; distinguish "no connection" from "server error" in the message.

Checklist:
- [ ] Both orientations supported (WCAG 1.3.4); state survives rotation
- [ ] Offline state shows cached data + banner, not a blank error
- [ ] Skeletons/progress for waits > 1 s, with retry on failure

## Sources

- https://developer.apple.com/design/human-interface-guidelines/layout
- https://developer.apple.com/design/human-interface-guidelines/gestures
- https://m3.material.io/foundations/designing/structure
- https://m3.material.io/foundations/accessible-design/accessibility-basics
- https://www.w3.org/TR/WCAG22/ (2.5.8, 2.5.5, 2.5.1, 2.5.4, 1.3.4, 1.4.4)
- https://www.smashingmagazine.com/2016/09/the-thumb-zone-designing-for-mobile-users/
- https://alistapart.com/article/how-we-hold-our-gadgets/ (Hoober's grip data)
- https://www.nngroup.com/articles/hamburger-menus/
- https://www.nngroup.com/articles/response-times-3-important-limits/
- https://baymard.com/blog/drop-down-usability
