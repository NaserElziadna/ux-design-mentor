# Accessible Design

**Primary Goals:**
- Inclusive design for all users
- WCAG AA compliance minimum
- Screen reader support
- Keyboard navigation

**Core Principles (Adapted):**
1. **Perceivable** (Don Norman - affordances)
   - Color isn't only indicator
   - Sufficient contrast (WCAG AA)
   - Text alternatives for images
   - Captions for video
   - Clear language

2. **Operable** (Krug - simplicity)
   - Keyboard navigable
   - No keyboard traps
   - Skip links
   - Sufficient time
   - No seizure-inducing animation

3. **Understandable** (Krug - clarity)
   - Clear language
   - Consistent navigation
   - Error messages helpful
   - Labels and instructions
   - Predictable interaction

4. **Robust** (Technical foundation)
   - Valid HTML
   - ARIA used correctly
   - Works with assistive tech
   - Cross-browser compatible
   - Standards compliant

5. **Inclusive** (Brown - design thinking)
   - Diverse user testing
   - Consider limitations
   - Provide alternatives
   - Don't exclude
   - Continuous improvement

**Critical Standards:**
- WCAG 2.2 Level AA minimum (current W3C recommendation, published Oct 2023 — supersedes 2.1; 2.1's criteria all carry forward plus the additions below)
- Section 508 compliance (US gov)
- ADA compliance
- EN 301 549 (EU)

**New in WCAG 2.2 (vs. 2.1) — check these specifically, they're the most commonly missed:**

| Criterion | Level | What it requires |
|---|---|---|
| 2.4.11 Focus Not Obscured (Minimum) | AA | A keyboard-focused element must not be entirely hidden by other content (sticky headers/footers, cookie banners) — at least part must stay visible |
| 2.5.7 Dragging Movements | AA | Any drag-operated function (sliders, reorder lists) needs a single-pointer alternative (tap + move, or up/down buttons) |
| 2.5.8 Target Size (Minimum) | AA | Interactive targets ≥24×24 CSS px, unless spacing gives an equivalent offset, an equivalent control exists elsewhere, it's inline text, or size is essential to the function |
| 3.2.6 Consistent Help | A | If a help mechanism (contact, chat, help link) appears on multiple pages, it must be in the same relative location on each |
| 3.3.7 Redundant Entry | A | Information already entered earlier in a process must be auto-populated or reusable, not re-typed from scratch |
| 3.3.8 Accessible Authentication (Minimum) | AA | Login can't rely purely on a cognitive test (remembering a password/puzzle) without an alternative, autofill/paste support, or object-recognition fallback |

Source: [W3C WAI — What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/)

**Touch target size — the numbers, and why there are three of them:**
- WCAG 2.2 SC 2.5.8 (AA, mandatory floor): **24×24 CSS px**
- WCAG SC 2.5.5 (AAA, best practice): **44×44 CSS px**
- Apple HIG minimum tap target: **44×44 pt**
- Material Design 3 minimum: **48×48 dp** (achieved by padding a smaller visual icon out to the full touch area, not by enlarging the icon itself)

Treat 24px as the absolute legal floor and 44–48px as the actual target for primary or mobile controls.

**Focus indicators:** the focused element's changed pixels need ≥3:1 contrast against their unfocused state (not just against the page background). A resilient technique: a double outline (a light ring plus a dark ring, ≥9:1 contrast between the two) so at least one ring is visible against any background color. Missing or low-contrast focus indicators remain one of the most commonly failed checks in real-world audits.

**Common Accessibility Patterns:**
- Semantic HTML (`<button>` not `<div>`)
- ARIA labels and roles
- Keyboard shortcuts
- Focus indicators
- Skip to content
- Form labels and validation
- Color + pattern (not color alone)

**Critical Mistakes to Avoid:**
- ❌ Image with no alt text
- ❌ Color-only distinction
- ❌ No focus indicators
- ❌ Keyboard traps
- ❌ Auto-playing video/sound
- ❌ Unclear form labels
- ❌ Moving/flashing content
- ❌ PDFs without tagging

**Testing Approach:**
- Keyboard-only testing
- Screen reader testing (NVDA, JAWS, VoiceOver, TalkBack)
- Color contrast checking (normal text 4.5:1, large text 3:1 for AA; non-text UI components like icons/borders/focus rings need 3:1 against adjacent colors — SC 1.4.11, frequently overlooked)
- `prefers-reduced-motion` support: strip nonessential motion (parallax, autoplay, scroll-triggered movement) or substitute a static/cross-fade alternative for users who enable it
- Accessibility audit tools
- User testing with disabled users

**Platform-specific accessibility conventions:**
- **Apple HIG:** every interactive element needs a concise VoiceOver label; reading order should mirror the visual layout; Dynamic Type support is required — test at the largest accessibility text size, not just the default, since layouts must not truncate or clip.
- **Material Design 3:** dynamic content changes (toasts, live updates) need live-region semantics so TalkBack announces them; standard M3 components carry accessible defaults built in, so prefer them over custom-built equivalents when possible.
