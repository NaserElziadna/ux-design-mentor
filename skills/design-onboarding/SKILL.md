---
name: design-onboarding
description: This skill should be used when the user asks about "onboarding", "first-run experience", "empty states", "welcome screen", "product tour", "getting users activated", "users sign up but don't come back", "what to show when there's no data yet", or is designing the first-use experience of any product or feature.
version: 0.1.0
---

# Onboarding & Empty States

Read `../ux-design-principles/references/onboarding-and-empty-states.md` first (the researched reference: NN/g tour findings, endowed progress, the four empty-state types). This skill is the decision procedure.

## Decision procedure

1. **Identify which empty state you're designing** — they need different treatments:
   - **First-use** (new user, nothing created) → onboarding moment: what belongs here, why it's valuable, one primary action to create the first thing. Consider sample/demo data.
   - **Cleared** (user emptied it — inbox zero) → celebrate or stay quiet; don't nag.
   - **No-results** (search/filter) → restate the query, offer corrections and looser filters; never a dead end.
   - **Error** (couldn't load) → say so honestly + retry; never disguise an error as "nothing here".
2. **Default to learn-by-doing over tours.** NN/g's study: tutorial viewers were no faster and rated tasks *harder*. Prefer contextual help at the moment of need over front-loaded walkthroughs. If a tour is demanded, make it ≤3 steps and skippable.
3. **Setup checklist for multi-step activation** (connect data → invite team → first result): visible progress, pre-check what's already done (endowed progress: pre-filled progress lifted completion 19%→34%), each item deep-links to the action.
4. **Personalization questions:** ≤3, only ones that visibly change what happens next; every additional signup step costs activation.
5. **Get to the "aha" fast.** Identify the moment the product proves its value and count the steps from signup to it; cut every step that isn't strictly needed. Demo data is legitimate if real value needs setup time.
6. **Returning users are onboarded too:** feature announcements via small contextual badges/spotlights, not modal takeovers; re-orient after long absence rather than assuming memory.

## Review checklist

- [ ] All four empty-state types designed (first-use / cleared / no-results / error)
- [ ] Each empty state: what this is + why valuable + one action; no dead ends
- [ ] No front-loaded tour where contextual help would do
- [ ] Checklist has endowed progress + deep links
- [ ] ≤3 personalization questions, each visibly consequential
- [ ] Steps from signup to first value counted and minimized
