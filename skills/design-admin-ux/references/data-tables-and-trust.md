# Data Tables & Lists for Non-Technical Admin Users

Admin tables generally fall into three types ([Pencil & Paper — UX Pattern Analysis: Enterprise Data Tables](https://www.pencilandpaper.io/articles/ux-pattern-analysis-enterprise-data-tables)):

- **Action-oriented** — the table exists so the user can act on rows (approve, fulfill, delete). Density should be low; row actions matter more than extra columns.
- **Info-oriented** — the table exists mainly so the user can read/reference data. Scannability and clear sort/filter matter more than inline actions.
- **Hybrid / "super-user"** — dense, highly configurable, built for people who live in the table all day.

**The core mistake in admin UX for non-technical staff is defaulting to the third type regardless of which one the task actually needs.** Identify which type this table actually is before designing it, and match density accordingly — a non-technical user managing occasional orders needs an action-oriented table with 4-5 columns, not a 20-column configurable grid.

## Column & Density Defaults

- Ship with **clean defaults**: fewer visible columns, a sensible pre-set sort applied automatically (e.g., newest first, or by urgency) rather than requiring the user to configure sorting themselves.
- Power-user customizations — freeze/reorder/hide columns, density toggle, saved custom views — should exist for the users who want them, but stay **off/hidden by default**, reachable through a clearly labeled "customize columns" affordance rather than cluttering the base view.
- Left-align text columns; right-align (and consider monospacing) numeric columns for easy scanning/comparison.
- Prefer minimal 1px row dividers over heavy gridlines — the goal is scannability, not a spreadsheet aesthetic.

## Bulk Actions

- Show bulk-select checkboxes **on hover**, not permanently on every row — a wall of checkboxes on first glance reads as more complex than the table actually is.
- The bulk-action toolbar should **only appear once at least one row is selected** — don't show ten row-level action icons on every single row by default; reveal actions contextually as the user selects rows, which keeps the resting state of the table calm and readable.

## Filtering

- Filters must be simple, named in plain language, and applied/removed dynamically (visible as removable "chips" once applied) — avoid exposing filter-builder logic (AND/OR combinators, regex, raw query syntax) that assumes technical fluency the audience doesn't have.
- Default to a small number of the most useful filters visible immediately, with a "more filters" expander for anything less common — this mirrors the Paradox of Choice guidance in `../../ux-design-principles/references/laws-of-ux.md`.

## Pagination vs. Infinite Scroll

Prefer **pagination** over infinite scroll for admin/back-office contexts. It's more predictable, supports "go back to where I was" reliably, and avoids the disorientation infinite scroll can cause when a user needs to cross-reference a specific row against something else on screen (a common admin task pattern — checking one row's data while looking something else up). This is a practical recommendation based on general admin-context usability reasoning rather than one single heavily-cited study, but it aligns with the broader "predictability over novelty" stance this whole skill takes for non-technical users.

## Row Actions

- Keep primary row actions (the ones the table exists for) visible and obvious; move secondary/rare actions into an overflow menu (e.g., a "⋯" kebab menu) rather than lining up six icons per row.
- Any destructive row action follows the decision order in `destructive-actions.md` — don't let a table's row-action pattern quietly reintroduce a bare "delete" icon with no confirmation tier behind it.

## Putting It Together: A Simplified Admin Table Checklist

- [ ] Table type identified (action/info/hybrid) and density matches it
- [ ] Default columns are the minimum needed for the primary task; extras are opt-in
- [ ] Sort has a sensible default; user isn't required to configure it themselves
- [ ] Bulk actions appear only when rows are selected
- [ ] Filters use plain language and visible removable chips, not query syntax
- [ ] Pagination used instead of infinite scroll
- [ ] Destructive row actions follow the full decision order from `destructive-actions.md`
