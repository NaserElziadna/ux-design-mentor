# The UX Design Mentor Framework

A standalone, portable design-principle reference distilled from 10 foundational UX/UI books, plus industry-standard supplementary frameworks (Nielsen's heuristics, Laws of UX, Refactoring UI, Atomic Design, WCAG 2.2, UX writing research). Use this as a copy-paste reference, a grounding document for an AI assistant, or a personal checklist — it doesn't require the Claude Code plugin to be useful.

**Purpose:** turn any design conversation from generic ("make it cleaner") into specific, falsifiable, principle-backed feedback tied to the actual users and domain involved.

---

## How to Use This Document

1. **Evaluating a design?** Work through the Evaluation Checklist, citing which principle each finding violates.
2. **Generating a design?** Start with Problem-First Design below before touching a single pixel.
3. **Feeding this to another AI model?** Paste `system-prompt.txt` (in this same folder) directly as a system prompt, or point the model at `prompt-config.json` for a structured version.
4. **Unsure which domain applies?** Jump to Domain Priorities near the end.

---

## Problem-First Design

Before proposing any visual or interaction change, answer:
- Who is the user, specifically?
- What task are they trying to complete?
- What is actually blocking them today?

If you can't answer these, you're not ready to design — you're decorating. (Fitzpatrick, Cagan, Brown)

---

## The 10 Books at a Glance

| Book | Author | Core Contribution |
|------|--------|-----------|
| The Design of Everyday Things | Don Norman | Affordances, feedback, constraints, mapping |
| Don't Make Me Think | Steve Krug | Simplicity, self-evidence, usability testing |
| Designing Interfaces | Tidwell, Brewer, Valencia | Reusable interaction patterns |
| Change By Design | Tim Brown | Design thinking process, divergent ideation |
| Inspired | Marty Cagan | Product discovery, risk-based validation |
| Designing Products People Love | Scott Hurff | Emotional state design, habit loops |
| UX Research | Nunnally & Farkas | Matching research method to the question |
| The Mom Test | Rob Fitzpatrick | Validating problems without leading questions |
| Evil by Design | Chris Nodder | Persuasion psychology, used ethically |
| UX for Beginners | Joel Marsh | Invisible UX, compounding small fixes |

## Supplementary Frameworks at a Glance

| Framework | Source | Fills This Gap |
|---|---|---|
| 10 Usability Heuristics | Nielsen Norman Group | The canonical, structured evaluation checklist |
| Laws of UX | Jon Yablonski | The cognitive mechanism behind *why* a fix works |
| UX Writing & Microcopy | NN/g, Google Material, *Nicely Said* | Interface copy — none of the 10 books treat this as a first-class topic |
| Refactoring UI | Adam Wathan & Steve Schoger | Concrete visual execution: type, color, spacing, depth |
| Atomic Design & Design Tokens | Brad Frost; tokens practice | Consistency at scale as a product grows past one designer's memory |
| WCAG 2.2 | W3C | The current accessibility standard (supersedes 2.1) |

---

## Principle Deep-Dive

### 1. Affordances & Signifiers — Don Norman
Interactive elements must visually signal how they're used. A button looks pressable; a link looks clickable. The signifier (what's perceived) must be obvious, consistent, and never color-only.

**Check:** Would a first-time user know what's interactive without being told?

### 2. Feedback & Visibility — Don Norman
Every action needs an immediate (<100ms), visible response. Loading, success, and error states must be visually distinct and described in plain language, not error codes.

**Check:** Can users always see current system state? Do errors explain what to do, not just what went wrong?

### 3. Constraints & Error Prevention — Don Norman
Prevent errors by design — disable invalid options, require confirmation before destructive actions — rather than showing an error message after the mistake happens.

**Check:** Is it hard to do the wrong thing, or does the system just complain after you do it?

### 4. Mapping & Conceptual Models — Don Norman
Control layout and grouping should mirror the user's mental model of the task, not the underlying data schema or org chart. Where the real mechanism is invisible (an algorithm, a cache, an async job), the interface must communicate a good-enough approximation of it, or users will invent a wrong model on their own.

**Check:** Are related controls grouped the way users think about the task? Where the mechanism is invisible, does the design communicate a reasonable model of it?

### 4b. The Gulfs of Execution & Evaluation — Don Norman
Diagnose *where* an interaction breaks down: the Gulf of Execution is the gap between what a user intends and what the interface visibly lets them do; the Gulf of Evaluation is the gap between the system's actual state and how well the user can perceive it. Affordances/signifiers narrow the execution gulf; feedback narrows the evaluation gulf.

**Check:** At the point of confusion, is the problem that the user can't tell what to do (execution), or can't tell what happened after they did it (evaluation)?

### 5. Self-Evidence & Simplicity — Steve Krug
Every screen should answer "what is this, where am I, what can I do here" without requiring thought. If a tooltip is needed to explain a control, the control needs redesigning — not documentation.

**Check:** Could a new user state this page's purpose in one glance? Is there exactly one obvious primary action?

### 6. Scannability — Steve Krug
Users scan, they don't read line by line. Front-load key words, use real headings, keep copy short and concrete.

**Check:** Can the key information be gotten from headings and bold terms alone?

### 7. Test Early, Test Cheap — Steve Krug
One user testing a rough prototype beats an internal debate among ten stakeholders. Usability problems are usually obvious within the first few minutes of watching a real user.

**Check:** Has this been shown to an actual user, or only discussed in a meeting?

### 7b. The Trunk Test — Steve Krug
Imagine a user dropped onto any single page as if let out of a car trunk. They should instantly answer: what site/product is this, what page, what section, and how do I get home.

**Check:** Looking only at this one page, can identity/location/section/way-home all be answered within a few seconds?

### 7c. Reservoir of Goodwill — Steve Krug
Users have a finite tolerance for friction that depletes with every confusing label or broken step, and refills when the product respects their time or delights them. No single screen usually causes abandonment — the accumulation does.

**Check:** Across the full flow, how many small frictions accumulate before the goal is reached, and does anything refill goodwill to offset them?

### 8. Pattern Reuse — Jennifer Tidwell
Don't invent a new interaction pattern for a problem that's already solved (wizards, autocomplete, card sorting, etc.), unless the domain gives a specific reason the standard pattern fails.

**Check:** Is there a well-known pattern for this exact problem, and if we're deviating from it, why?

### 9. Product-Wide Consistency — Jennifer Tidwell
Consistency across the whole product usually matters more than locally optimizing one screen. Custom patterns should be documented so they don't drift as the product grows.

**Check:** Does this screen behave the way the same kind of interaction behaves elsewhere in the product?

### 10. Design Thinking Order — Tim Brown
Empathize with real users → define the actual underlying problem (not the requested feature) → ideate broadly → prototype cheaply → test and iterate. Skipping straight to "ideate" or "prototype" without defining the real problem is the most common failure mode.

**Check:** Has the real problem been defined, or did this start from a pre-chosen solution?

### 11. Diverge Before You Converge — Tim Brown
Generate multiple meaningfully different approaches before narrowing to one. The first idea is rarely the best one — it's just the first one anyone said out loud.

**Check:** Were 2–3 genuinely different directions considered, or just one direction refined?

### 12. Outcome Alignment — Marty Cagan
Design decisions should serve a measurable business or user outcome — not just "look better." If a change can't be tied to an outcome, question why it's being made.

**Check:** What metric or user outcome does this specific change move?

### 13. Discovery Before Delivery — Marty Cagan
Test the riskiest assumptions cheaply (prototypes, concierge tests, fake-door tests) before committing engineering effort to build the real thing.

**Check:** Has the riskiest assumption been tested cheaply, or are we building straight to production and hoping?

### 14. The Four Risks — Marty Cagan
Before committing to a design, check: value risk (will they want it), usability risk (can they use it), feasibility risk (can we build it), business viability risk (does it work for the business).

**Check:** Which of the four risks is least validated right now?

### 15. Emotional State Design — Scott Hurff
Users arrive in different mental/emotional states (bored, anxious, task-focused, manic-multitasking). Design the response to match that state, not a generic "calm, happy user" default.

**Check:** What's the user's likely emotional state right before this screen, and does the design account for it?

### 16. Habit Loops — Scott Hurff
Sustainable engagement forms around a trigger, a low-friction action, and a fast reward. Evaluate whether a flow supports or breaks that loop.

**Check:** Is there a clear trigger and a fast, low-friction path to the reward?

### 17. Assumption-to-Method Mapping — Nunnally & Farkas
Every major design assumption should map to a specific research method capable of proving it wrong — usability test, survey, analytics, or field study, chosen for the type of question being asked.

**Check:** What method would disprove this assumption, and has it been run?

### 18. Method Matches Question Type — Nunnally & Farkas
Behavioral questions ("will they actually use this") need behavioral observation. Opinion questions can use surveys. Using the wrong method type produces confident, wrong answers.

**Check:** Is a behavioral question being answered with a stated-opinion survey?

### 19. No Leading Questions — Rob Fitzpatrick (The Mom Test)
Never ask hypothetical or leading questions ("would you use a feature that...?"). Ask about specific past behavior and existing workarounds instead — people are polite liars about future intent.

**Check:** Does the validation question ask about intent ("would you") instead of past behavior ("what have you already tried")?

### 20. Evidence of Investment — Rob Fitzpatrick (The Mom Test)
"That sounds cool" is not validation. Real signal looks like money, time, or effort a user has already spent trying to solve the problem.

**Check:** Has the user spent real money, time, or workaround effort on this problem, unprompted?

### 21. Deliberate Defaults — Chris Nodder (Evil by Design, used ethically)
Defaults are extremely powerful — most users end up with whatever the default is. Choose defaults deliberately, in the user's interest, and disclose them transparently.

**Check:** Was this default chosen to serve the user, or is it just whatever was easiest to implement?

### 22. Flag Dark Patterns — Chris Nodder
Explicitly name and avoid manipulative patterns: confirmshaming ("No thanks, I don't want to save money"), hidden costs revealed at the last step, forced continuity, and roach-motel flows (easy to get into, hard to get out of).

**Check:** Would this flow embarrass the team if it were made public?

### 23. Invisible UX — Joel Marsh
Good UX is often unnoticed — if a user comments on the interface rather than their task, something is usually broken.

**Check:** Did the user's feedback mention the interface, or only whether they completed their goal?

### 24. Compounding Small Fixes — Joel Marsh
Fix specific, concrete frictions one at a time rather than chasing a vague "make it better" goal. Small fixes compound; abstract redesigns often don't ship.

**Check:** Is this feedback a concrete, fixable friction point, or a vague aesthetic preference with no clear fix?

---

## Supplementary Frameworks — Deep Dive

### 25. Nielsen's 10 Usability Heuristics
The canonical, most-cited UX evaluation checklist: visibility of system status, match with the real world, user control and freedom (undo), consistency and standards, error prevention, recognition over recall, flexibility and efficiency for both novices and experts, aesthetic and minimalist design, help users recognize/diagnose/recover from errors, and help/documentation that's ideally unnecessary. Use this as the default structure for a systematic heuristic pass — it deliberately overlaps with Norman and Krug above, describing the same reality from a different, more exhaustive angle.

**Check:** Score the design against each of the 10 heuristics with specific evidence; prioritize fixes that resolve multiple heuristics at once.

### 26. Laws of UX — the Mechanism Behind the Fix
Twenty-one cognitive/psychological principles (Fitts's, Hick's, Miller's, Jakob's, Postel's, Peak-End Rule, Aesthetic-Usability Effect, Von Restorff, Zeigarnik, Serial Position, Doherty Threshold, Goal-Gradient, Common Region, Proximity, Prägnanz, Occam's Razor, Tesler's Law, Parkinson's Law, Paradox of Choice, Cognitive Load, Flow, Chunking) explaining *why* a recommendation works, not just that it should. Naming the specific law makes feedback falsifiable and teachable instead of a stylistic opinion.

**Check:** Does the recommendation cite the specific law whose mechanism actually explains the failure, not just the most famous one?

### 27. UX Writing & Microcopy
Interface copy is part of the design: verb-first specific button labels ("Save changes," not "Submit"), plain-language error messages naming the actual problem near the field, confirm-buttons that name the real action rather than generic OK/Confirm, persistent visible form labels (never placeholder-as-label), and empty states that explain why and offer one next action.

**Check:** Does every piece of interface copy pass the "Clear, Concise, Consistent" test?

### 28. Visual Design Craft (Refactoring UI)
A deliberate type scale, an intentional color system (hand-picked HSL shades, not a decorative gradient), a non-linear spacing scale where grouping spacing exceeds internal spacing, and two-part shadows for depth. This is the layer of craft most AI-generated UI skips, converging instead on named anti-patterns: the purple-to-blue gradient hero, reflexive default fonts, the 3-card bento grid, "cardocalypse" (1px grey borders on everything), and floating 3D gradient blobs.

**Check:** Is every visual choice traceable to a deliberate system, or is it a framework default?

### 29. Design Systems & Atomic Design
Structure UI as atoms → molecules → organisms → templates → pages so a fix at the component level propagates everywhere, and encode the resulting decisions as named design tokens (color, spacing, type, radius, shadow) rather than hardcoded values. Formalize a system when duplicated "snowflake" components, design/dev drift, or rebuild-from-scratch friction actually appear — not before, since a heavyweight system built too early can be as costly as none at all.

**Check:** Would a rebrand or theme change require a token edit, or a find-and-replace across components?

### 30. Admin UX for Non-Technical Users
A distinct audience from B2B SaaS power users: design for the least technical person who will use this, optimizing for safety and confidence over efficiency. For destructive actions, prefer undo (toast) → soft-delete with a recovery window → specific named confirmation → rare type-to-confirm, in that order — defaulting to confirmation dialogs for everything causes click-through fatigue that defeats their purpose. Use the user's own job vocabulary, wizards for infrequent tasks, and a visible audit trail as a trust mechanism.

**Check:** Is a routine action handled with undo/soft-delete, with hard confirmation reserved only for the rare, truly irreversible cases?

---

## Master Evaluation Checklist

**Fundamentals (Norman)**
- [ ] Affordances match user expectations
- [ ] Feedback is immediate and unambiguous
- [ ] Errors are prevented by constraint, not just caught after
- [ ] Layout maps to the user's mental model

**Usability (Krug)**
- [ ] Purpose and primary action are instantly obvious
- [ ] Copy is scannable, not a wall of text
- [ ] This has been tested with at least one real user

**Patterns (Tidwell)**
- [ ] Uses an established pattern where one exists
- [ ] Consistent with the rest of the product
- [ ] Any custom pattern is documented

**Process (Brown, Cagan)**
- [ ] The real underlying problem is defined, not just the requested feature
- [ ] Multiple approaches were considered before converging
- [ ] Tied to a measurable outcome
- [ ] Riskiest assumption identified and validated (or flagged as untested)

**Research & Validation (Nunnally/Farkas, Fitzpatrick)**
- [ ] Key assumptions are validated with evidence of real behavior, not stated intent
- [ ] The research method used matches the question type

**Ethics & Psychology (Nodder)**
- [ ] Defaults were chosen deliberately, in the user's interest
- [ ] No dark patterns (confirmshaming, hidden costs, forced continuity, roach motel)

**Standard Heuristics (NN/g)**
- [ ] Scored against all 10 heuristics, with specific evidence per score

**Visual Craft (Refactoring UI)**
- [ ] Type/color/spacing follow a deliberate system, not framework defaults
- [ ] No named generic-AI-look anti-pattern present (gradient hero, cardocalypse, bento-grid-only, 3D blobs)

**Copy (UX Writing)**
- [ ] Buttons are verb-first and specific; errors are plain-language and near the field
- [ ] Destructive-action buttons name the actual action, not generic OK/Confirm

**Accessibility (cross-cutting)**
- [ ] WCAG 2.2 AA minimum: contrast, keyboard nav, screen-reader labels, plus the 2.2 additions (Focus Not Obscured, Target Size Minimum ≥24px, Dragging Movements alternative, Consistent Help, Redundant Entry, Accessible Authentication)
- [ ] No signifier relies on color alone
- [ ] `prefers-reduced-motion` respected

**If This Is an Admin/Back-Office Tool for Non-Technical Users**
- [ ] Destructive actions use undo/soft-delete by default, not confirmation dialogs for everything
- [ ] Language matches the user's job vocabulary, not the data model
- [ ] Infrequent tasks are wizards, not dense forms

---

## Domain Priorities

Different domains weight these principles differently. Establish the domain before prescribing solutions — and note that "admin panel" is not automatically "B2B SaaS": check whether the actual users are technical power users or non-technical staff.

**E-commerce** — trust signals, checkout friction reduction, product discoverability, social proof, price/shipping transparency, mobile checkout performance.

**B2B SaaS (technical power users)** — efficiency for repeat power users over first-time discoverability, information density, keyboard shortcuts, role/permission complexity, error prevention (real data at stake), onboarding across varied roles.

**Admin/back-office (non-technical users)** — safety and confidence over efficiency; undo and soft-delete over confirmation dialogs; plain job vocabulary; guided wizards for infrequent tasks; a visible audit trail as a trust mechanism. Do not default to B2B SaaS patterns here.

**Mobile-first** — touch targets ≥24px (WCAG 2.2 AA floor), 44-48px recommended for primary/mobile controls, thumb-reach zones, tolerance for offline/latency, recovery from interruption, low cognitive load per screen, performance as a UX feature in itself.

**Accessibility-critical** — WCAG 2.2 AA minimum (supersedes 2.1; adds Focus Not Obscured, Dragging Movements, Target Size Minimum, Consistent Help, Redundant Entry, Accessible Authentication), no color-only signifiers, full keyboard navigation with visible high-contrast focus indicators, correct screen-reader labels, `prefers-reduced-motion` support, sufficient contrast ratios (4.5:1 text, 3:1 large text and non-text UI components).

---

## Output Format for Feedback

1. Restate the problem/goal in one sentence to confirm understanding.
2. Identify the domain context (or ask, if unclear).
3. List specific findings — each one naming the principle and book behind it.
4. Give a concrete, actionable fix per finding — not "improve X," but what to change and why.
5. Flag which parts are principle-backed fact vs. untested assumption, and suggest a cheap way to validate the risky ones.

---

*Generated as part of the `ux-design-mentor` Claude Code plugin. See `system-prompt.txt` for a condensed version suited to system-prompt use, and `prompt-config.json` for a structured/programmatic version.*
