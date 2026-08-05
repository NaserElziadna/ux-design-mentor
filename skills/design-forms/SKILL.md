---
name: design-forms
description: This skill should be used when the user asks about "form design", "form validation", "signup/login/checkout form", "edit form", "settings page", "form UX", "error messages in forms", "multi-step form", "should this be a modal or a page", or is building/reviewing ANY form — create forms, edit forms, filters, settings, admin CRUD screens.
version: 0.1.0
---

# Form Design — Create, Edit, and Validation UX

Read `../ux-design-principles/references/forms-and-input-ux.md` first (the researched reference: label placement, validation timing, mobile keyboards, Baymard checkout findings, WCAG 3.3.8). This skill adds the decision procedure plus **edit-form/CRUD patterns** the reference doesn't cover.

## Create-form rules (summary — details in the reference)

- Single column; top-aligned labels; never placeholder-as-label.
- Every field must justify its existence — each removed field measurably lifts completion (Baymard: average checkout shows ~11 fields, ~8 suffice).
- Validate on blur, not on keystroke; once a field is flagged, clear the error as the user types ("reward early, punish late").
- Error text: state the specific problem + how to fix it, next to the field, `aria-describedby` + `aria-invalid`.
- Mobile: correct `inputmode`/`type`/`autocomplete` per field; 16px+ input font (iOS zoom).
- Multi-step: show honest progress ("Step 2 of 4"), persist entered data across steps and back-navigation.

## Edit-form patterns (settings, admin CRUD, profile pages)

Edit forms differ from create forms — the user is changing existing data, and the cost of a mistake is corrupting something that already works:

- **Prefill everything.** Never make users re-enter existing values (WCAG 3.3.7 redundant entry). Show current values as editable, not as blank fields with the old value in helper text.
- **Dirty-state tracking.** Disable "Save" until something actually changed; enable it the moment a field diverges. This is feedback (Norman) — it tells users whether they've changed anything.
- **Unsaved-changes guard.** Navigating away with dirty fields → confirmation ("Discard unsaved changes?"). Discard must be the non-primary button.
- **Explicit save vs autosave — pick by risk.** Autosave for low-risk, frequently-edited, easily-reverted content (notes, drafts) with a visible "Saved" indicator + undo. Explicit Save/Cancel for consequential settings (billing, permissions, anything affecting other users). Never mix modes on one screen.
- **Save button placement:** bottom of the form (end of reading order); sticky if the form scrolls. Cancel beside it, visually secondary. Never two primary buttons.
- **Per-section save for long settings pages** (like GitHub settings): each card saves independently — a failure in one section doesn't hold the rest hostage.
- **Destructive actions live apart.** Delete/transfer-ownership go in a separated "danger zone" at the bottom, never adjacent to Save. Follow `../design-admin-ux/references/destructive-actions.md`.
- **After save:** confirm success visibly (toast + updated values), keep the user on the page unless the task is complete, and show *what* changed if the system transformed input (trimmed, reformatted).
- **Concurrent edits:** if two people can edit the same record, detect conflicts and say who changed what — never silently overwrite (last-write-wins loses real work).

## Modal vs page

Modal form: ≤ ~4 fields, single quick task, context of the underlying page matters (quick-add). Full page: anything longer, anything multi-step, any edit form users may leave mid-way. Never nest modals.

## Review checklist

- [ ] Single column, visible top labels, no placeholder-as-label
- [ ] Field count minimized; optional fields marked (mark optional, not required)
- [ ] Validation on blur; errors specific, adjacent, accessible
- [ ] Correct mobile input types and autocomplete tokens
- [ ] Edit forms: prefilled, dirty-tracked, unsaved-changes guarded
- [ ] One save model (explicit XOR autosave), destructive actions separated
- [ ] Success feedback after save; conflicts handled if multi-user
