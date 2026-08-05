# Onboarding & Empty States

Empty states and first-run experience decide whether a new user reaches value or bounces. The core research finding: upfront tutorials mostly get skipped and do not improve task success (NN/g), while empty states — the screens users actually land on — are the highest-leverage, most-neglected onboarding surface. Design onboarding as "learn by doing in context," not as a lecture before the product.

## The Four Types of Empty State

Each requires different treatment — never reuse one generic "nothing here" screen (Pencil & Paper, Toptal):

1. **First-use** — user has never added data. This is onboarding: explain what the feature does, why it's valuable, and give the primary action to create the first item. Sample data or templates belong here.
2. **User-cleared** — user emptied it themselves (inbox zero, completed tasks). Do NOT re-explain the feature; celebrate or acknowledge completion ("All done"). Re-education here reads as condescending.
3. **No-results** — search/filter returned nothing. Never a dead end: show the query, offer to clear filters, suggest spelling fixes or broader terms, and (in commerce) show alternatives. "No results found." alone is a failure.
4. **Error/permission** — data exists but can't be shown (network, access denied). Say what happened in plain language, whether user data is safe, and give a retry or escalation path. Never disguise an error as "nothing here yet."

- [ ] Every list/table/dashboard view has all four states designed, not just the happy path
- [ ] No-results states preserve the user's query and offer a recovery action
- [ ] Error states are visually distinct from first-use states

## Anatomy of a Good Empty State

Formula (Pencil & Paper, Mobbin): **what this is + why it's valuable + how to fill it.**

- **Headline**: name the value, not the absence ("Track every deploy in one place", not "No deploys").
- **1–2 sentences of explanation**: what will appear here and what it does for the user.
- **Primary CTA**: the single action that fills the state ("Connect repository"). One button, not three.
- **Optional**: illustration (keep it lightweight, don't let it push the CTA below the fold), secondary link to docs/import, or sample data preview.
- **Avoid dead ends**: if the user can't fill the state themselves (needs admin, needs data from elsewhere), say who can and offer "request access" or "notify me" — never leave zero actions.

- [ ] Empty state has exactly one primary action
- [ ] Copy explains value, not just absence
- [ ] User who lacks permission still gets a path forward

## Onboarding Patterns, Ranked

Rough effectiveness order, best first (NN/g, Appcues, Userpilot):

1. **Learn by doing** — the UI itself teaches via good defaults, clear labels, and empty states. Zero interruption cost.
2. **Interactive walkthrough** — user performs real actions in their real account with guidance ("now click Create"). Retains far better than passive tours because it produces real output.
3. **Product tour (coach marks / modal deck)** — passive pointing. NN/g's quantitative study (70 users, 4 apps with deck-of-cards tutorials) found tutorial readers were *no faster and no more successful*, and perceived tasks as **more difficult**; many users skip tours entirely (https://www.nngroup.com/articles/mobile-tutorials/). If you must use one: ≤3–5 steps, always skippable, re-launchable from help.
4. **Video** — worst for onboarding: passive, unsearchable, forces the user to hold instructions in memory. Acceptable only as optional supplementary help.

NN/g's blunt guidance: "skip onboarding when possible" — invest in an interface that doesn't need explaining (https://www.nngroup.com/videos/onboarding-skip-it-when-possible/).

- [ ] No forced, unskippable tour before first use
- [ ] Any walkthrough operates on the user's real data, not screenshots
- [ ] Tours are re-launchable from a help menu

## Progressive Onboarding vs Front-Loaded Tutorials

Front-loading instruction fails because users have no context to attach it to and forget it before it's needed (NN/g, Onboarding Tutorials vs. Contextual Help: https://www.nngroup.com/articles/onboarding-tutorials/). Instead:

- **Progressive onboarding**: teach each feature the first time the user encounters it, via contextual hints — one tip, dismissible, never shown again after interaction.
- Reserve day-one onboarding for the *single* action that delivers first value; defer everything else.
- Rule of thumb: if a tooltip explains a screen the user won't visit this week, cut it.

## Activation Metrics & the "Aha Moment"

- Define **activation**: the earliest measurable event correlated with retention (e.g., "created first project and invited 1 teammate within 7 days"). Design the entire first-run flow to shorten time-to-that-event, and measure time-to-value, not tour completion.
- Everything between signup and the aha moment is friction; count the clicks and cut ruthlessly.
- Instrument each onboarding step's drop-off; the biggest cliff is where to redesign first.

- [ ] Activation event is defined and instrumented
- [ ] First-run flow is measured as time-to-value, not tutorial completion rate

## Checklists & Setup Progress (Endowed Progress Effect)

Nunes & Drèze (2006): car-wash cards needing 8 stamps redeemed at 19%, but 10-stamp cards pre-filled with 2 stamps — same 8 purchases — redeemed at 34% (https://www.coglode.com/nuggets/endowed-progress-effect). Applied to onboarding:

- Show a setup checklist of 3–7 items with a progress bar.
- **Pre-check something real** ("Create account ✓") so the bar starts at ~20%, never 0%.
- Order items by value delivered, not by internal system logic.
- Make the checklist dismissible and auto-hide at 100%; a permanent nag destroys goodwill.

- [ ] Checklist starts with at least one item already complete
- [ ] ≤7 items, dismissible, disappears when done

## Personalization Questions

- Keep signup profiling to **≤3 questions**, and only ask what visibly changes the experience (role → templated workspace). Every extra question costs conversion.
- Show the payoff immediately after answering ("Marketing? Here's your campaign dashboard"). If an answer doesn't change what the user sees next, don't ask it.
- Always allow "skip" — segmenting a bounced user is worth nothing.

## Sample / Demo Data as Onboarding

- Pre-populate first-use views with clearly labeled sample data ("Example project — delete anytime") so users learn the populated UI, not a blank one. Charts, tables, and boards are meaningless empty.
- Make sample data one-click removable and visually tagged (badge/banner) so it's never mistaken for real records.
- Alternative: templates ("Start from: Sprint board / CRM / Blank") give structure without fake records.

## Contextual Help & Tooltips vs Upfront Instruction

- Prefer **contextual help** — tooltips, inline hints, "?" affordances that appear at the moment of need — over any upfront instruction (NN/g). Instructions delivered in context are used; instructions delivered up front are forgotten.
- One hint at a time; a screen sprouting five simultaneous tooltips is a tour in disguise.
- Persistent affordances (labeled buttons, placeholder examples, inline validation) beat ephemeral hints.

## Re-Onboarding & Feature Announcements

- **Returning after absence**: don't replay new-user onboarding; show "what changed since you left" and restore their last context.
- **New features**: announce contextually — a small badge/dot on the relevant menu item beats a launch modal. If you must modal, one feature per release, dismiss = never again.
- Keep tours and hints re-launchable from a help/"what's new" menu for users who skipped them the first time.
- Watch for "announcement fatigue": more than one interruption per session trains users to dismiss everything unread.

- [ ] Feature announcements are contextual badges, not blocking modals
- [ ] Skipped onboarding is recoverable from help

## Sources

- https://www.nngroup.com/articles/mobile-tutorials/
- https://www.nngroup.com/articles/onboarding-tutorials/
- https://www.nngroup.com/videos/onboarding-skip-it-when-possible/
- https://www.pencilandpaper.io/articles/empty-states
- https://www.toptal.com/designers/ux/empty-state-ux-design
- https://mobbin.com/glossary/empty-state
- https://www.eleken.co/blog-posts/empty-state-ux
- https://www.coglode.com/nuggets/endowed-progress-effect
- https://www.appcues.com/blog/product-tours-walkthroughs-ultimate-guide
