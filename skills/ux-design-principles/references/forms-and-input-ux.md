# Forms and Input UX

Forms are where users do work and where products lose them: Baymard's checkout research attributes a large share of abandonments to form friction, and their benchmark shows the average checkout can be cut from roughly 16 form fields to 8 with no loss of data (Baymard). Every field, label, and error message is a chance to either reduce or add cognitive load. These rules are grounded in NN/g, Baymard Institute, WCAG 2.2, and GOV.UK Design System guidance.

## Layout and Labels

- Use a single-column layout. Multi-column forms break the vertical scanning path and cause fields to be skipped or misinterpreted (Baymard; GOV.UK Design System).
- Place labels above their fields (top-aligned). Top-aligned labels keep label and input in one fixation, work at any label length, translate well, and suit narrow mobile viewports (NN/g "Form Design: Labels"; Material Design 3 text fields use floating top labels).
- Left-align labels and fields to a single vertical axis so the eye travels straight down.
- Never use placeholder text as the only label. Placeholders disappear on input, so users lose context mid-entry, can't review before submitting, and low-contrast placeholder text fails many users; screen readers may skip it entirely (NN/g "Placeholders in Form Fields Are Harmful"). Use placeholders only for optional hints, and prefer persistent helper text below the field.
- Group related fields with visible section headings; one topic per section.

Checklist:
- [ ] Single column, labels above fields
- [ ] No placeholder-as-label anywhere
- [ ] Helper text persists below the field, not inside it

## Field Count and Defaults

- Remove every field you can. Ask only for what you need now; each extra field adds friction and abandonment risk (Baymard "From 16 Form Fields to 8"; GOV.UK: "ask users for information only once").
- Combine fields where natural (single "Full name" instead of first/middle/last unless the backend truly requires the split — GOV.UK recommends a single name field where possible).
- Pre-fill sensible defaults: country from locale, "shipping address = billing address" checked by default (Baymard), remembered values for returning users.
- Never default-select anything consequential (marketing opt-ins, paid add-ons).
- Derive instead of asking: city/state from postal code, card type from card number (Baymard).

Checklist:
- [ ] Every field justified; optional "nice to have" fields removed
- [ ] Sensible, non-manipulative defaults set
- [ ] Derivable data (card type, city from ZIP) not asked for

## Input Types, Keyboards, and Autofill

- Use the right HTML type/inputmode so mobile users get the right keyboard: `type="email"`, `type="tel"`, `inputmode="numeric"` for card numbers, one-time codes, and ZIPs (avoid `type="number"` for card numbers — it allows spinners and drops leading zeros).
- Add `autocomplete` tokens (`name`, `email`, `postal-code`, `cc-number`, `cc-exp`, `one-time-code`, `new-password`/`current-password`). Autofill support is a WCAG 1.3.5 Identify Input Purpose requirement at AA (W3C WCAG 2.2) and dramatically speeds completion (Baymard).
- Auto-format as the user types (card number spacing, phone grouping) rather than rejecting "wrong" formats; accept input with or without spaces/dashes (Baymard; GOV.UK).
- Never block paste — it breaks password managers and violates WCAG 3.3.8 expectations (W3C).

Checklist:
- [ ] Correct type/inputmode per field; numeric keyboard for numeric entry
- [ ] autocomplete attributes on all standard fields
- [ ] Input auto-formatted; lenient parsing; paste allowed

## Validation Timing and Error Messages

- Validate on blur (when the user leaves the field), never on every keystroke while they are still typing a not-yet-complete value (NN/g "Errors in Forms"; Smashing Magazine "Live Validation UX").
- Follow "reward early, punish late": once a field has been flagged invalid, re-validate on each keystroke so the error clears the instant it's fixed; but never show a first-time error before the user has finished the field (Smashing Magazine; Konjević's inline-validation research).
- Debounce server-side checks (e.g., username availability) by ~500 ms–1 s (Smashing Magazine).
- Place the error message directly adjacent to the field (below or beside it), in text — not only color — with an icon; keep the user's input so they can correct rather than retype (NN/g "10 Design Guidelines for Reporting Errors in Forms").
- Write errors in plain, polite, specific language that says what happened and how to fix it: "Enter an email address in the format name@example.com", not "Invalid input" (NN/g "Hostile Patterns in Error Messages"; GOV.UK error message guidance).
- On submit failure, show an error summary at the top that links to each offending field and move focus to it (GOV.UK error summary component; WCAG 3.3.1 Error Identification).

Checklist:
- [ ] Validation fires on blur, not on first keystroke
- [ ] Errors clear immediately once fixed (reward early)
- [ ] Error text is specific, adjacent to the field, and not color-only
- [ ] Submit failures produce a linked error summary

## Optional vs. Required

- Mark the minority case. If most fields are required, mark only the optional ones with "(optional)" in the label — GOV.UK's approach — or, if only a few are required, mark those. Never rely on an unexplained asterisk alone (Baymard finds users often miss or misread bare asterisks; NN/g recommends explicit "Required"/"Optional" text).
- Better: make everything required by removing optional fields.

Checklist:
- [ ] "(optional)" written out on optional fields
- [ ] No unexplained asterisks

## Long Forms: Progressive Disclosure and Multi-Step Patterns

- Hide rarely used fields behind a link/toggle rather than showing them by default (progressive disclosure): "Add a company name", "Add Address Line 2" (Baymard; NN/g "Progressive Disclosure").
- For long flows, split into steps of related fields ("one thing per page" — GOV.UK). Each step should have one clear topic.
- Show a progress indicator with step labels ("Step 2 of 4: Delivery"); users tolerate long flows when they can see position and remaining effort (NN/g wizard/progress guidance; Baymard recommends linear checkout with a visible steps indicator).
- Preserve entered data across steps and on back-navigation; let users review before final submit (GOV.UK "Check your answers" pattern).

Checklist:
- [ ] Rare fields collapsed behind a link
- [ ] Multi-step forms show "Step X of Y" with labels
- [ ] Data survives back/forward; review step before submit

## Payment and Checkout Specifics (Baymard)

- Format the expiration date exactly like the physical card: MM/YY, two fields or a masked single field, in that order — 72% of sites get this wrong (Baymard "Format the Expiration Date Fields").
- Auto-space the card number to match the card's embossing (4-4-4-4 for Visa/Mastercard, 4-6-5 for Amex) using IIN range detection; auto-detect and highlight the card type instead of asking (Baymard "Credit Card IIN Ranges and Spacing Patterns").
- Collapse "Address Line 2" (and "Company name") behind a link by default — visible optional fields cause hesitation and mis-entry (Baymard checkout usability).
- Offer guest checkout; never force account creation before payment (Baymard consistently ranks forced account creation among top abandonment causes).
- Explain why you ask for sensitive data (phone number) inline, or drop the field.

Checklist:
- [ ] Expiration date is MM/YY matching the card
- [ ] Card number auto-formats with correct spacing; card type auto-detected
- [ ] Address Line 2 collapsed behind a link
- [ ] Guest checkout available

## Password Fields

- Provide a show/hide password toggle; masking without a reveal causes typos and abandoned logins (NN/g "Stop Password Masking" lineage; GOV.UK password input component ships with a toggle).
- Never disable paste into password fields — it defeats password managers (NCSC and GOV.UK guidance).
- State password rules up front, before the first error, and validate them as a live checklist.
- Meet WCAG 3.3.8 Accessible Authentication (Minimum), new at AA in WCAG 2.2: no cognitive function test (memorizing/transcribing) without an alternative — so allow paste, support password managers and autofill (`autocomplete="current-password"`), and offer copy-paste-able one-time codes (`autocomplete="one-time-code"`) (W3C WCAG 2.2).
- Prefer length over composition rules; don't force periodic resets (NIST SP 800-63B, echoed by GOV.UK).

Checklist:
- [ ] Show/hide toggle present
- [ ] Paste and password managers work
- [ ] Rules shown before errors; WCAG 3.3.8 satisfied

## Sources

- https://baymard.com/blog/how-to-format-expiration-date-fields
- https://baymard.com/checkout-usability/credit-card-patterns
- https://baymard.com/blog/checkout-optimization-from-16-fields-to-8
- https://www.nngroup.com/articles/errors-forms-design-guidelines/
- https://www.nngroup.com/articles/hostile-error-messages/
- https://www.nngroup.com/articles/form-design-placeholders/
- https://www.smashingmagazine.com/2022/09/inline-validation-web-forms-ux/
- https://www.w3.org/TR/WCAG22/ (1.3.5, 3.3.1, 3.3.8)
- https://design-system.service.gov.uk/patterns/ (question pages, error messages, check your answers, passwords)
- https://m3.material.io/components/text-fields/guidelines
