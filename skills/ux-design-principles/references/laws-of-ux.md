# Laws of UX (Jon Yablonski)

A collection of psychology and cognitive-science principles applied to interface design, compiled by Jon Yablonski. Where Norman and Krug explain *why* good design works, these laws give the underlying cognitive mechanism — useful for explaining *why* a specific fix will work, not just that it should.

Source: [lawsofux.com](https://lawsofux.com/)

## Jakob's Law
Users spend most of their time on *other* products, so they prefer yours to work the way those already do.
**Apply:** Put navigation where users expect it (top or left), keep the cart icon top-right — don't invent a novel interaction for a solved, conventional problem.

## Fitts's Law
The time to acquire a target is a function of its size and the distance to it.
**Apply:** Make the primary mobile CTA a full-width, 44px+ button placed in the thumb zone at the bottom of the screen — not a small link near the top.

## Hick's Law
Decision time increases with the number and complexity of choices.
**Apply:** Cut a 12-item nav down to 5 top-level categories with progressive disclosure, and highlight one recommended pricing tier instead of presenting all options as equally weighted.

## Miller's Law
The average person can hold only about 7 (±2) items in working memory at once.
**Apply:** Auto-format a long account or card number into chunks of 4 digits instead of one unbroken string.

## Postel's Law
Be liberal in what you accept, conservative in what you send — systems should tolerate messy input but produce clean, predictable output.
**Apply:** Accept a phone number typed with dashes, spaces, or parentheses and normalize it automatically instead of rejecting the whole submission over formatting.

## Peak-End Rule
People judge an experience mainly by its most intense moment and its ending, not the average of every moment in between.
**Apply:** Invest specifically in the final confirmation screen of a flow (checkout, signup) — a well-designed ending disproportionately shapes how the whole experience is remembered.

## Aesthetic-Usability Effect
Users perceive visually pleasing designs as more usable, and are more forgiving of minor usability flaws when the design is attractive.
**Apply:** Polish core flows visually — but never let this substitute for actual usability testing, since attractiveness can mask real friction rather than fix it.

## Von Restorff Effect
When several similar items are present, the one that visually differs stands out and is remembered best.
**Apply:** Give the single primary action a distinct filled color while secondary actions stay outlined — but don't overuse this, and never rely on color alone (pair with shape/icon for accessibility).

## Zeigarnik Effect
People remember and feel driven to finish uncompleted or interrupted tasks better than completed ones.
**Apply:** Show a "Profile 70% complete" progress bar with a visible next-step checklist to pull users back to finish remaining setup steps.

## Serial Position Effects
Users best recall the first (primacy) and last (recency) items in a series; middle items are the most easily forgotten.
**Apply:** Place the most important nav items at the far left and far right of a horizontal bar; bury lower-priority links in the middle.

## Doherty Threshold
Productivity and engagement rise sharply when system response time stays under roughly 400ms.
**Apply:** For any action likely to exceed 400ms (search-as-you-type, file upload), show an immediate skeleton loader or spinner within that window so the interface feels responsive even while real work continues.

## Goal-Gradient Effect
Motivation to reach a goal increases the closer someone gets to it.
**Apply:** Start a checkout progress bar partially filled ("Step 2 of 4" shown as already 25% done) rather than at zero, and let visual progress accelerate near the end to encourage completion.

## Law of Common Region
Elements sharing a clearly bounded area (border, background, shadow) are perceived as a group.
**Apply:** Wrap each pricing plan in its own card with a background fill so its features read as belonging to that plan, not the one beside it.

## Law of Proximity
Objects placed near each other are perceived as related, regardless of similarity in shape or color.
**Apply:** Tighten the space between a form label and its input, and widen the space between unrelated field groups, so users instinctively see which label belongs to which field.

## Law of Prägnanz / Law of Similarity
People perceive ambiguous or complex shapes in the simplest form possible; elements that look alike are perceived as one group or pattern.
**Apply:** Use one consistent icon style and color for every destructive action (delete, remove, archive) across the product so users recognize the category by pattern, not by reading each label.

## Occam's Razor
Among equally effective solutions, choose the one with the fewest assumptions and elements.
**Apply:** Auto-detect city/state from a ZIP code instead of asking for four separate address fields when three can be inferred.

## Tesler's Law (Law of Conservation of Complexity)
Every system has an irreducible core of complexity — it can be moved between the system and the user, but never eliminated entirely.
**Apply:** When you remove a field from the user (per Occam's Razor above), that complexity has to go *somewhere* — build the ZIP-to-address lookup into the backend rather than pretending the complexity vanished.

## Parkinson's Law
A task expands to fill the time allotted for its completion.
**Apply:** Give a low-priority onboarding step a visible, tight time estimate ("2 minutes") so users don't let it drag out indefinitely.

## Paradox of Choice (Choice Overload)
Presenting too many options overwhelms users and degrades both their decision-making and their satisfaction with whatever they pick.
**Apply:** Reduce a 20-item filter list to 4-5 curated top filters plus a "more filters" expander, and default to a "recommended" sort instead of surfacing every sort option at once.

## Cognitive Load / Working Memory
Working memory holds roughly 4-7 chunks for 20-30 seconds; cognitive load is the total mental effort — intrinsic plus extraneous — required to use an interface.
**Apply:** Persist previously entered data across a multi-page form so users never have to re-type or remember it, and strip decorative or non-essential UI from task-critical screens.

## Flow (Csikszentmihalyi)
Full immersion and enjoyment occur when a task's challenge is well-matched to the user's skill, with clear goals and immediate feedback.
**Apply:** Offer adjustable complexity (a simple mode and an advanced panel) and give instant visual feedback on every action, so users across the skill range stay in a matched-challenge state instead of getting bored or frustrated.

## Chunking
Breaking information into smaller, meaningful groups improves comprehension and recall.
**Apply:** Split a long settings page into labeled sections ("Account," "Notifications," "Privacy") with clear visual separation instead of one continuous list of 30 toggles.

## How to Use These Laws in Feedback

Naming the specific law behind a recommendation makes it falsifiable and teachable, not just a stylistic preference: "reduce this to 5 options" is an opinion; "reduce this to 5 options because Hick's Law predicts decision time will drop as choice count drops" is a claim someone could test. Prefer citing the law whose mechanism most directly explains the failure, not the most famous one — e.g. a cluttered settings page is usually a Chunking/Cognitive-Load problem, not a Hick's Law problem (Hick's Law is about choosing among options, not about parsing a dense list).
