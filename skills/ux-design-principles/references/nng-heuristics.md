# Nielsen's 10 Usability Heuristics (Nielsen Norman Group)

The most-cited UX evaluation checklist in the industry — developed by Jakob Nielsen and Rolf Molich (1990), refined in 1994 through factor analysis of 249 real usability problems. Use this as the default structure for a systematic heuristic evaluation, complementing (not replacing) the book-specific principles elsewhere in this skill — there's deliberate overlap with Norman and Krug by design, since all three describe the same underlying reality from different angles.

Source: [nngroup.com/articles/ten-usability-heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)

## 1. Visibility of System Status

Keep users informed about what's happening through timely, appropriate feedback.

- Does the UI show loading/progress states for anything that takes >1 second?
- Does every user action produce a visible response quickly?
- Can users always tell the current state (e.g., cart contents, save status, connection status)?

## 2. Match Between the System and the Real World

Speak the user's language; use familiar words and concepts; follow real-world conventions.

- Does copy avoid internal jargon or technical terms the user wouldn't use themselves?
- Do icons and metaphors map to real-world equivalents users already know?
- Is information ordered the way the user would naturally think about the task?

## 3. User Control and Freedom

Provide a clearly marked "emergency exit" to leave an unwanted state or action.

- Is there an obvious way to undo or cancel most actions?
- Can users exit a multi-step flow without penalty?
- Are "back" and "cancel" always present and behaving as expected?

## 4. Consistency and Standards

Don't make users wonder whether different words, situations, or actions mean the same thing; follow platform and industry conventions.

- Are the same terms/icons used for the same concept everywhere in the product?
- Does the UI follow platform conventions (iOS/Android/web patterns) rather than inventing new ones unnecessarily?
- Is button/link styling consistent across all screens?

## 5. Error Prevention

Prevention beats good error messages — eliminate error-prone conditions or catch them before submission.

- Are destructive actions confirmed, reversible, or both?
- Does the UI disable or hide invalid options instead of letting users pick them and fail later?
- Is input validated inline, before submission, rather than only after?

## 6. Recognition Rather Than Recall

Minimize memory load by making options and actions visible instead of requiring users to remember them.

- Are choices shown rather than requiring the user to recall them from elsewhere in the product?
- Does the interface surface recently used items or relevant context automatically?
- Are labels self-explanatory without requiring memorized codes or IDs?

## 7. Flexibility and Efficiency of Use

Offer accelerators — invisible to novices, useful to experts — so the design serves both.

- Are there keyboard shortcuts or batch/bulk actions for frequent tasks?
- Can repeat users customize or automate common workflows?
- Does the design avoid forcing experienced users through a novice-length flow every time?

## 8. Aesthetic and Minimalist Design

Every extra, irrelevant, or rarely-needed unit of information competes with the relevant units and diminishes their visibility.

- Does every visible element serve a purpose?
- Could any clutter, redundant labeling, or decoration be removed without losing function?
- Does visual hierarchy draw attention to what actually matters most on this screen?

## 9. Help Users Recognize, Diagnose, and Recover From Errors

Error messages in plain language that precisely state the problem and suggest a constructive solution.

- Do error messages avoid error codes and jargon?
- Do they state specifically what went wrong and how to fix it?
- Is the error shown near the point of failure, not in a disconnected location?

## 10. Help and Documentation

Ideally the product needs no documentation; if it does, help should be easy to search and focused on the user's actual task.

- Can most tasks be completed without consulting help at all?
- If help exists, is it contextual and searchable rather than one monolithic manual?
- Is documentation task-oriented ("how to export a report") rather than feature-oriented ("the Export module")?

## Extension for Complex/Enterprise Applications

NN/g's later research ([Usability Heuristics Applied to Complex Applications](https://www.nngroup.com/articles/usability-heuristics-complex-applications/)) refines these heuristics for domain-specific and enterprise software — directly relevant to `design-context`'s B2B SaaS guide and `design-admin-ux`:

- **Richer feedback for long waits.** A spinner is enough for a 2-second wait; anything approaching or exceeding 10 seconds needs a progress indicator with detail (percentage, current step, estimated time), not just an indication that something is happening.
- **Domain metaphors still matter for experts.** Even power users benefit from icon/metaphor conventions that map to real-world equivalents — expertise in the domain doesn't remove the cost of an unfamiliar icon system.
- **Undo supports learning by doing** (the "paradox of the active user" — people prefer to explore and learn a tool by using it rather than reading about it first). Reversibility isn't just error recovery, it's what makes exploration safe.
- **Experts hit an efficiency plateau.** Beyond a point, more practice doesn't make a power user faster — only shortcuts, customization, and automation do. If a workflow has flat-lined on speed for experienced users, that's a heuristic-7 (flexibility/efficiency) gap, not a training gap.
- **Errors double as teaching moments in complex domains** — a good error message in a complex tool should help the user build a more accurate mental model of the system, not just unblock the immediate task.

## Quick Evaluation Pass

When using this checklist to evaluate a design, score each heuristic (e.g., 1-5 or pass/fail), cite the specific evidence for the score, and prioritize fixes by how many heuristics a single change would improve — a fix that resolves both error prevention (5) and recognition-over-recall (6) is higher leverage than one that only touches aesthetics (8).
