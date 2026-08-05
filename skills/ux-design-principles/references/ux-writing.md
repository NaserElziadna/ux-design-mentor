# UX Writing & Microcopy

Interface copy is part of the design, not an afterthought filled in after layout is done. NN/g research found concise, scannable, neutral copy improved usability by 58%, and combined with removing promotional language, usability improved by 124%. Separately, unclear instructions caused roughly half of observed user errors, and a bad error message causes 79% of users to abandon the page and 27% to abandon the site entirely. ([NN/g — Errors](https://www.nngroup.com/topic/errors/))

## Buttons & CTAs

- Lead with a verb, followed by the specific object or outcome: "Save changes," "Download your template," "Start my free trial" — not "Submit," "Click here," or "Learn more."
- Keep to 1-3 words; the label should match the destination screen's heading so users feel oriented, not surprised, after clicking.

**Before → After:** "Submit" → "Save changes" · "Learn More" → "See pricing plans" · "Click Here" → "Download the report"

Source: [UX Writing Guide for Better Labels, CTAs, and Navigation](https://lettercrafted.com/ux-writing-guide-for-better-labels/)

## Error Messages

NN/g's guidelines: show the error near the field it concerns, in plain non-technical language; avoid blame words ("invalid," "illegal"); state the specific problem, not a generic failure; give a constructive, actionable next step; never delete what the user already typed; auto-suggest a fix when one is inferable. Reserve interrupting modals for severe errors — use inline banners for minor ones.

**Before → After:**
- "An error occurred" → "You must spend $35 to qualify for free shipping — add $12.50 more to your cart"
- "Invalid credentials" → "That's not the right password. Try again, or reset your password if you've forgotten it."

Google's Material writing guidance frames the same idea as: *"instead of telling the user what they did wrong, tell them how to get it right."*

Sources: [NN/g — Error-Message Guidelines](https://www.nngroup.com/articles/error-message-guidelines/) · [NN/g — Hostile Error Messages](https://www.nngroup.com/articles/hostile-error-messages/) · [Google — Material Communication Guidance](https://codelabs.developers.google.com/codelabs/material-communication-guidance)

## Confirmation & Destructive Actions

- The confirm button should name the actual action — "Delete," "Discard changes" — never a generic "OK" or "Confirm."
- Use text labels, not bare icons, for Cancel vs. Close; conflating them can silently lose user work.
- Reserve confirmation dialogs for genuinely severe or rare actions. Overuse causes click-through blindness, where users stop reading them at all — at that point the dialog no longer prevents anything.
- For the rarest, most irreversible operations, a non-standard confirmation (typing the item's name, as Mailchimp does before deleting a list) is justified. For everything else, undo is the better safety net — it doesn't interrupt the flow and doesn't require the user to predict their own intent correctly in advance.

Sources: [NN/g — Confirmation Dialogs Can Prevent User Errors](https://www.nngroup.com/articles/confirmation-dialog/) · [NN/g — Cancel vs. Close](https://www.nngroup.com/articles/cancel-vs-close/)

## Form Labels vs. Placeholder Text

Placeholder-as-label is a well-documented anti-pattern: the hint disappears the moment a user starts typing or the field is focused, forcing them to remember what was asked — a real problem in long forms and especially damaging for users with cognitive or visual impairments who rely on a persistent label.

**Rule:** always use a persistent, visible label positioned outside the field. If a placeholder is used at all, it should show a format example only ("MM/DD/YYYY"), never replace the label itself.

Source: [NN/g — Placeholders in Form Fields Are Harmful](https://www.nngroup.com/articles/form-design-placeholders/)

## Empty States

A bare "No results found" is technically correct and a dead end. An effective empty state restates what was searched, explains why it's empty, and offers a next action.

**Before → After:** "No results found" → "No results for 'kiwi.' Try adjusting your filters or checking your spelling." plus suggested alternatives.

For onboarding empty states specifically, don't leave a blank page — explain the value and give one obvious next action (Pinterest's pattern: "Create your first board to save ideas you love" + suggested topics + a clear CTA).

Sources: [Pencil & Paper — Empty State UX](https://www.pencilandpaper.io/articles/empty-states) · [UX Writing Hub — Empty State Examples](https://uxwritinghub.com/empty-state-examples/)

## Voice vs. Tone

From *Nicely Said* (Fenton & Kiefer Lee): **voice** is the product's consistent personality — it doesn't change day to day. **Tone** is how that voice adapts to the user's emotional state in the moment. An error during a bank transfer needs a calmer, more serious tone than a "board created" success toast, even though the underlying voice is the same product speaking both times. Consistency of voice with situational adaptation of tone is the core discipline — not picking one fixed tone for the whole product.

## The 3 C's Checklist

A widely-cited compact heuristic (aligned with Torrey Podmajersky's *Strategic Writing for UX*) for reviewing any piece of interface copy:

- **Clear** — unambiguous, plain language, no jargon the user wouldn't use themselves
- **Concise** — no filler words, scannable at a glance
- **Consistent** — the same action is described with the same wording everywhere in the product

Plus Google/Material's implicit conventions: sentence case (not Title Case) for labels and headings, second person ("you/your"), and no exclamation points except for genuine celebration — they otherwise read as shouting.

Source: [UX Writing Hub — 3 Microcopy Rules](https://uxwritinghub.com/3-microcopy-rules-every-ux-writer-must-know/)
