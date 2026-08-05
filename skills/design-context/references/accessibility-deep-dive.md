# Accessibility Deep Dive

A working reference for developers who already know the basics (alt text, contrast, labels — see accessibility.md). This file covers WCAG 2.2's new success criteria, focus management in SPAs, accessible-name computation, ARIA patterns and their expected keyboard behavior, and the hard limits of automated testing. WCAG 2.2 is a W3C Recommendation (Oct 2023); references below are to the spec at w3.org/TR/WCAG22.

## WCAG 2.2: the nine new success criteria

Six are Level A/AA (compliance-relevant); three are AAA. Each with a pass/fail example:

- **2.4.11 Focus Not Obscured (Minimum), AA** — a focused element must not be *entirely* hidden by author content. Fail: sticky cookie banner fully covers the focused "Submit" button when tabbing. Pass: banner overlaps at most part of it, or content scrolls focused elements into view (`scroll-padding-bottom` for sticky footers).
- **2.4.12 Focus Not Obscured (Enhanced), AAA** — no part of the focused element may be hidden.
- **2.4.13 Focus Appearance, AAA** — focus indicator area ≥ 2px perimeter equivalent with 3:1 contrast between focused/unfocused states.
- **2.5.7 Dragging Movements, AA** — any drag operation needs a single-pointer, non-drag alternative. Fail: reorderable list only via drag-and-drop. Pass: each item also has "Move up / Move down" buttons. (Kanban: add a "Move to column…" menu.)
- **2.5.8 Target Size (Minimum), AA** — pointer targets ≥ **24×24 CSS px**, or spaced so a 24px circle centered on each target doesn't intersect another target. Exceptions: inline links in text, equivalent larger control elsewhere, user-agent defaults. Fail: 16px icon buttons packed in a toolbar. Pass: 20px icons with padding making the hit area 24px+ (`min-width/min-height: 24px` on the button, not the icon).
- **3.2.6 Consistent Help, A** — if a help mechanism (contact link, chat, FAQ) appears on multiple pages, it appears in the **same relative order/location** on each. Fail: chat widget bottom-right on some pages, in the footer on others.
- **3.3.7 Redundant Entry, A** — don't make users re-enter information they already gave in the same process, unless essential (re-typing a password) or the info expired. Pass: "Billing same as shipping" checkbox; previously entered email pre-filled at later steps.
- **3.3.8 Accessible Authentication (Minimum), AA** — no cognitive function test (memorizing, transcribing, solving puzzles) to log in, unless there's an alternative or a mechanism to assist. Fail: blocking paste in the password field, or a CAPTCHA with no alternative. Pass: allow paste and password managers (`autocomplete="current-password"`), support WebAuthn/passkeys or emailed magic links. Object-recognition CAPTCHAs are exempt at AA but not at **3.3.9 (Enhanced, AAA)**.

- [ ] Sticky headers/footers never fully cover focused elements
- [ ] Every drag interaction has a click/tap alternative
- [ ] All controls ≥ 24×24px or adequately spaced
- [ ] Paste and password managers work on auth fields

## Focus management in SPAs

Client-side routing does not move focus or announce anything — a screen-reader user hears silence after clicking a nav link.

- **Route change**: after render, move focus to the new view's `<h1>` (give it `tabindex="-1"`) or a "skip target" container, and/or announce the new page title via a visually-hidden `aria-live="polite"` region. Also update `document.title`.
- **Modals/dialogs**: on open, move focus into the dialog (first field or the dialog itself); **trap** Tab/Shift+Tab inside; Esc closes; on close, **restore focus to the element that opened it**. Prefer native `<dialog>.showModal()`, which traps focus and handles Esc, or `inert` on background content instead of manual traps.
- **Deleted content**: when the focused element is removed (e.g., deleting a list row), move focus to the next row or the list heading — otherwise focus resets to `<body>`.
- **Async updates**: announce results ("14 results loaded", "Item added to cart") with a persistent `aria-live="polite"` region that exists at page load (dynamically injected live regions often miss the first announcement). Use `role="alert"` / `assertive` only for errors.

```html
<div aria-live="polite" class="visually-hidden" id="announcer"></div>
```

- [ ] Route changes move focus and update `document.title`
- [ ] Dialogs trap focus and restore it on close
- [ ] Async state changes announced via a pre-rendered live region

## Accessible name computation

Order of precedence (per W3C accname spec): `aria-labelledby` → `aria-label` → native labeling (`<label>`, `alt`, `<legend>`) → `title` (last resort) → content text (for roles that allow it).

- Prefer **visible text** as the name — it serves voice-control users ("click Submit" fails if the accessible name differs from the label). WCAG 2.5.3 Label in Name: the accessible name must contain the visible label text.
- `aria-labelledby` when the name already exists in the DOM (e.g., a card's heading names its "Read more" link): `aria-labelledby="link-id heading-id"` concatenates.
- `aria-label` only when no visible text exists (icon-only buttons). Remember it **replaces** inner text entirely.
- `aria-label` on non-interactive, non-landmark elements (`<div>`, `<span>`, `<p>`) is ignored or harmful.
- Placeholder is not a label. `title` alone is unreliable.

- [ ] Icon-only controls have `aria-label`; everything else named by visible text
- [ ] No `aria-label` that contradicts visible text

## Landmarks & heading outline as navigation

Screen-reader users navigate by headings (most common strategy per WebAIM's screen reader surveys) and by landmarks — treat both as your page's API.

- One `<main>`, one `<header>` (banner), one `<footer>` (contentinfo). Multiple `<nav>`/`<aside>` need distinguishing names: `<nav aria-label="Breadcrumb">`.
- All content should live inside a landmark; stray content between landmarks is easy to miss.
- Exactly one `<h1>`; never skip levels downward (h2 → h4 fails outline logic); choose heading level by structure, style by CSS. Don't use headings for styling non-heading text.
- Sections that users would want to jump to (filters, results, cart summary) deserve a heading even if visually hidden.

- [ ] Every page region inside a labeled landmark
- [ ] Heading levels form a strict outline under one h1

## Forms deep dive

- **Errors**: link message to field with `aria-describedby`, set `aria-invalid="true"`; the message element should exist adjacent to the field. On submit failure, move focus to the first invalid field or an error summary that links to each field.

```html
<input id="email" aria-invalid="true" aria-describedby="email-err">
<p id="email-err">Enter an email like name@example.com</p>
```

- **Hints**: also via `aria-describedby` (it accepts multiple IDs: `aria-describedby="hint err"`).
- **Groups**: radio groups and related checkboxes need `<fieldset><legend>` (or `role="group"` + `aria-labelledby`) — otherwise the group question ("Shipping speed?") is never read with the options.
- **WCAG 1.3.5 Identify Input Purpose (AA)**: personal-data fields need `autocomplete` tokens (`name`, `email`, `tel`, `street-address`, `postal-code`, `cc-number`…). This is a real SC, not just convenience — it enables user agents to augment fields with icons/autofill.
- Don't disable the submit button as validation UX — users get no feedback on *why*; validate on submit and explain.

- [ ] Errors: `aria-describedby` + `aria-invalid`, focus moved to first error
- [ ] Radio/checkbox groups wrapped in fieldset/legend
- [ ] Autocomplete tokens on all personal-data fields (1.3.5)

## Keyboard patterns per ARIA APG

If you use an ARIA role, you owe its full keyboard contract (w3.org/WAI/ARIA/apg/patterns). Expected bindings:

- **Dialog**: Tab cycles inside; Esc closes; focus enters on open, restores on close.
- **Tabs**: Tab lands on the active tab only; **Arrow Left/Right** move between tabs (roving tabindex); Tab from a tab goes into the panel. Home/End to first/last tab.
- **Menu / menubar** (real menus, not nav links): Enter/Space/Down opens; arrows navigate items; Esc closes and returns focus to the trigger; type-ahead by first letter. If it's site navigation, don't use `role="menu"` — use a list of links with a disclosure button.
- **Combobox** (per APG combobox pattern): Down opens/moves through options with `aria-activedescendant` or roving focus; Enter selects; Esc closes without selecting; `aria-expanded` reflects state.
- **Listbox/grid**: arrow-key navigation, single tab stop for the whole widget.

Rule of thumb: one Tab stop per composite widget; arrows move *within* it. If you can't implement the keyboard contract, use simpler native elements instead of the role.

- [ ] Every ARIA widget implements its APG keyboard map
- [ ] Composite widgets use roving tabindex (one tab stop)

## Common ARIA mistakes

- **Redundant roles**: `<button role="button">`, `<nav role="navigation">` — noise; native semantics already provide the role.
- **`aria-hidden="true"` on focusable content** — element disappears from the accessibility tree but stays tabbable: "ghost" focus stops. Also never `aria-hidden` on an ancestor of the focused element.
- **`role="button"` on a div without keyboard support** — role alone adds nothing; you must add `tabindex="0"` plus Enter and Space handlers. (Just use `<button>`.)
- **`role="menu"` for navigation** — imposes menu keyboard expectations users can't meet.
- **State attributes never updated** — `aria-expanded`, `aria-selected`, `aria-checked` set once at render and never toggled.
- **`aria-live` regions injected on demand** — often not announced; render them empty at load.
- Children violations: e.g., `role="tab"` not inside `tablist`, `option` not inside `listbox` — breaks screen-reader interaction modes.
- WebAIM's Million report (webaim.org/projects/million) consistently finds pages *with* ARIA average **more** detectable errors than pages without — ARIA is a scalpel, not seasoning. First rule of ARIA: don't use ARIA when HTML suffices.

- [ ] No aria-hidden on focusable elements or their ancestors
- [ ] All ARIA state attributes updated on interaction

## Screen-reader testing quick-start

Test the top pairings (per WebAIM screen reader user surveys, NVDA and JAWS with Chrome/Edge dominate on Windows; VoiceOver on macOS/iOS):

- **NVDA (Windows, free — nvaccess.org)**: NVDA key = Insert (or Caps Lock). Start/stop: Ctrl+Alt+N / NVDA+Q. Browse mode: `H` next heading, `K` link, `F` form field, `D` landmark, `B` button; NVDA+Space toggles browse/focus mode; NVDA+F7 elements list. Test: can you complete the core flow with the screen off?
- **VoiceOver (macOS, built-in)**: Cmd+F5 toggles. VO keys = Ctrl+Option. VO+A read page; VO+U rotor (headings/links/landmarks); VO+Right Arrow next item; VO+Space activate. On iOS: triple-click side button, swipe right = next item, double-tap = activate.
- Minimum manual pass: unplug the mouse — Tab through the whole flow (visible focus everywhere, no traps, logical order), then repeat with the screen reader: are names, roles, states, and live updates announced?

- [ ] Core flows completable with keyboard only
- [ ] Core flows completable with NVDA or VoiceOver, screen off

## Limits of automated tools

- Automated scanners (axe-core, Lighthouse, WAVE) catch only a fraction of real issues. Deque's own audit study puts axe automated coverage at ~57% of issues by volume (deque.com/automated-accessibility-coverage-report); independent estimates commonly land at ~30-40% of WCAG failures. Either way: **passing axe is not conformance.**
- What automation cannot judge: whether alt text is *meaningful*, focus order sensibility, keyboard operability of custom widgets, whether announcements happen at the right moment, cognitive load, correctness of accessible names ("Read more" ×12 passes axe).
- Recommended pipeline: axe in CI (zero-violation gate, catches regressions cheaply) → manual keyboard pass per feature → screen-reader pass on core flows per release → periodic testing with real assistive-technology users.
- Overlay widgets ("accessibility toolbars") do not fix underlying code and are not a compliance path.

- [ ] Automated scan in CI, treated as a floor not a certificate
- [ ] Manual keyboard + screen-reader checks in definition of done

## Sources

- https://www.w3.org/TR/WCAG22/ — WCAG 2.2 Recommendation (all nine new SC)
- https://www.w3.org/WAI/WCAG22/Understanding/ — Understanding docs per criterion
- https://www.w3.org/WAI/ARIA/apg/patterns/ — ARIA Authoring Practices keyboard patterns
- https://www.w3.org/TR/accname/ — accessible name computation
- https://webaim.org/projects/million/ — WebAIM Million (ARIA error findings)
- https://webaim.org/projects/screenreadersurvey10/ — screen reader usage/navigation habits
- https://webaim.org/articles/nvda/ and https://webaim.org/articles/voiceover/ — testing quick-starts
- https://www.deque.com/automated-accessibility-coverage-report/ — automated coverage (~57% by issue volume)
