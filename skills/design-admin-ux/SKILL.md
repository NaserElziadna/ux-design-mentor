---
name: design-admin-ux
description: This skill should be used when the user asks about "admin panel design", "back-office UX", "internal tool for non-technical staff", "CMS design", "dashboard for non-technical users", "admin UX", or wants guidance for an admin/back-office interface used by non-technical staff (store managers, office staff, content editors) — as opposed to `design-context`'s B2B SaaS guide, which assumes technical power users comfortable with density and keyboard shortcuts.
version: 0.1.0
---

# Admin UX for Non-Technical Users

Comprehensive guidance for admin panels, back-office tools, and internal dashboards used by staff who are not developers or technical power users — a store manager processing orders, an office worker running an HR tool, a content editor using a CMS. This is a distinct audience from `design-context`'s B2B SaaS guide: these users don't want keyboard shortcuts or dense data grids, they want to complete a specific task safely without training, and they're often anxious about "breaking something."

## Overview

The single biggest design mistake in admin UX is treating it as a stripped-down version of a developer tool. Non-technical admin users have different goals entirely: task completion without error, not efficiency through mastery. Every pattern below optimizes for **safety and confidence**, not speed.

**Contrast with B2B SaaS (`../design-context/references/b2b-saas.md`):** that guide is correct for tools used daily by people who *want* to become power users (analysts, ops specialists). This skill is for tools used occasionally or by staff whose actual job is something else — the admin panel is a means to their real work, not the work itself. If unsure which applies, ask: would this user want a keyboard-shortcuts cheat sheet, or would that terrify them? If the latter, use this skill.

**User preferences:** Check whether `.claude/ux-design-mentor.local.md` exists in the project. If it sets `preferred_domain` to something admin-adjacent, apply this skill's guidance directly rather than asking.

## Core Design Stance

- **Design for the least technical person who will use this**, not the most capable. Proficiency range should drive which controls are default-visible vs. tucked away — err toward hiding, not exposing.
- **Constraint is a kindness for this audience, not a limitation.** A curated set of options, sensible defaults, and a narrower path through a task reduces anxiety; an open-ended, maximally-flexible interface increases it.
- **Performance matters disproportionately.** A slow admin screen compounds the anxiety of someone who already feels unsure in the tool — treat load time and responsiveness as a UX requirement, not an engineering nice-to-have.
- **Plain language over system/database terminology.** Rename "Node" → "Article," "Taxonomy" → "Category," "View Mode" → "Layout." Technical vocabulary is a primary source of confusion for this audience — if a term wouldn't appear in the user's own job description, don't put it in the UI.

## Destructive Actions: Making Them Safe

Overused confirmation dialogs train users to click through them on autopilot — at that point they prevent nothing. Use this decision order instead of confirming everything by default:

1. **Undo over confirm, as the default.** A toast with an "Undo" affordance doesn't interrupt flow and doesn't require the user to correctly predict their own intent in advance — it's the strongest pattern for routine actions.
2. **Soft delete with a recovery window, for most "delete" actions.** Mirror Google Drive/Outlook: the item disappears from the main view but sits in a searchable Trash for a disclosed window (commonly 30 days) before permanent purge. A dedicated Trash screen lets non-technical users self-recover without filing a support ticket — this should be the default mental model for deleting orders, articles, users, and similar records.
3. **Specific confirmation dialogs, for less-frequent, harder-to-undo actions.** Name the exact item ("Delete 'Q3 Sales Order #4471'?"), not a generic "Are you sure?" Replace Yes/No with descriptive action verbs ("Delete order" / "Keep order") so a user can't blindly click through without registering what they chose.
4. **Non-standard confirmation (type the item's name to confirm), reserved for the rarest, truly catastrophic, immediate, and irreversible actions only** — e.g. permanently purging data with no recovery window. Overusing this pattern turns it into noise; it only works because it's rare.
5. **Spatial separation from safe actions.** Never place a destructive action directly next to a benign one with similar visual weight — separate them spatially and/or stylistically (e.g. red vs. neutral) so a misclick is structurally harder, not just discouraged by color alone.

See `references/destructive-actions.md` for the full pattern catalog with more examples.

## Reducing Anxiety, Building Confidence

- **Wizards for unfamiliar or infrequent tasks; forms for routine ones.** Novices and infrequent users prefer step-by-step wizards; frequent power users prefer dense forms. An admin user issuing a refund or onboarding a new employee once a month is exactly the infrequent-user profile — default to a stepped flow with visible progress, not a dense settings page.
- **Guardrails, not open canvases.** Curated component/option sets, intelligent defaults, predefined (accessible) color choices, and options limited by context — this constraint reduces decisions the user has to get right on their own.
- **Inline help beats separate documentation.** A contextual tooltip next to the control beats sending the user to a help center they have to leave the task to consult.
- **Empty states as onboarding, not blank screens.** Explain *why* it's empty and give exactly one obvious next action — don't show every possible feature to a first-timer; reveal complexity gradually as they need it.
- **Audit trails as a trust mechanism.** A searchable, filterable "who did what, when" log gives non-technical users (and their managers) confidence that mistakes are traceable and reversible — it directly reduces the fear of silently breaking something they won't be able to explain later.
- **Explicit permission clarity.** State plainly, next to the action itself, who can do this and why it's greyed out for them if it is — don't bury role logic in a settings page the user never visits. Users should only *see* controls their role can act on, not see-but-be-blocked, wherever feasible.

See `references/reducing-anxiety.md` for the fuller pattern catalog.

## Data Tables & Lists for Non-Technical Users

Admin tables fall into three types — action-oriented, info-oriented, and hybrid/"super-user" — and the design should match density and controls to which type this actually is, not default to a maximalist power-user grid.

- Clean defaults: fewer visible columns, a sensible pre-set sort. Power-user customizations (freeze/reorder/hide columns, density toggle) should exist but stay off by default.
- Bulk-select checkboxes appear on hover; the bulk-action bar only appears once rows are selected — don't show a row of action icons on every row by default, reveal actions contextually.
- Filters must be simple and named in plain language, applied/removed dynamically — avoid filter-builder logic (AND/OR, regex) that assumes technical fluency.
- Prefer pagination over infinite scroll for admin contexts — it's more predictable and supports "go back to where I was" when cross-referencing rows.

See `references/data-tables-and-trust.md` for the fuller catalog, including the audit-trail and permission-clarity patterns in more depth.

## Evaluation Checklist

- [ ] Could someone with zero training complete the primary task without asking for help?
- [ ] Is every destructive action handled by undo or soft-delete, with hard confirmation reserved only for the rare, truly irreversible cases?
- [ ] Is there a visible, searchable audit trail for actions that matter?
- [ ] Does the language match the user's own job vocabulary, not the underlying data model?
- [ ] Is an infrequent, unfamiliar task presented as a guided wizard rather than a dense form?
- [ ] Are advanced/power-user options present but hidden by default rather than cluttering the primary view?
- [ ] Would this design still make sense to someone who is anxious about making a mistake?

## Notable Reference Points

- **Google Drive Trash / Outlook Deleted Items** — the reference implementation for soft-delete-with-recovery-window; treat this as the default mental model for admin deletes.
- **Mailchimp's "type DELETE to confirm"** — the canonical example of non-standard confirmation; useful as a named pattern, but explicitly a last resort, not a default.
- **Squarespace** is repeatedly cited as more intuitive for non-technical users (real-time visual editing) compared to more structured, merchant-first admin tools like **Shopify's admin**, which optimizes well for inventory/orders but can feel awkward for adjacent non-technical tasks like content editing — a useful illustration that an admin optimized for one persona doesn't automatically serve an adjacent one.

## Additional Resources

- **`references/destructive-actions.md`** — Full confirmation/undo/soft-delete pattern catalog
- **`references/reducing-anxiety.md`** — Wizards, plain language, guardrails, empty states, audit trails, permission clarity
- **`references/data-tables-and-trust.md`** — Table simplification patterns for non-technical users
- **`examples/delete-confirmation-example.md`** — Worked before/after example of a destructive-action flow
- **`../design-context/references/b2b-saas.md`** — The contrasting guide for technical power users
- **`../ux-design-principles/references/ux-writing.md`** — Error/confirmation copy principles referenced throughout this skill
