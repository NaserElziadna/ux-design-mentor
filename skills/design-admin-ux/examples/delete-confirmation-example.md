# Example: Redesigning a Destructive Action for Non-Technical Users

**Scenario:** A store manager (non-technical) needs to remove a discontinued product from an inventory admin panel.

## Generic/Default Approach (what to avoid)

A trash-can icon on each row. Clicking it immediately shows a browser-style `confirm()` dialog: "Are you sure?" with OK/Cancel. Clicking OK deletes the product immediately and permanently, with no way to recover it.

**Why this fails this audience:** the confirmation is generic (doesn't name the product, so a distracted user can't verify they're deleting the right one), the buttons don't describe the action, there's no recovery path if they click OK on the wrong row, and "permanently" with zero safety net is exactly the kind of risk that makes non-technical users afraid to use the tool at all.

## Redesigned Approach (this skill's guidance applied)

1. **Row action:** the delete icon sits in an overflow "⋯" menu, not as a bare icon on every row — reducing visual clutter and reducing the chance of an accidental click on a densely packed row (`../references/data-tables-and-trust.md`).
2. **Confirmation, if used at all:** since this is a routine, moderate-frequency action (not rare/catastrophic), skip a blocking dialog entirely. Instead, removing the product immediately shows a toast: *"'Blue Ceramic Mug (Discontinued)' removed from inventory. [Undo]"* — visible for several seconds (Pattern 1, `../references/destructive-actions.md`).
3. **Underlying behavior:** the product isn't actually purged — it moves to a searchable **Inventory Trash** page with a 30-day recovery window, mirroring Google Drive's model (Pattern 2). If the manager realizes days later they removed the wrong item, they can search the Trash and restore it themselves without contacting support.
4. **Copy:** the toast names the specific item, not a generic "Item removed," so the manager can visually confirm it was the right one — directly reflecting the specificity principle in `../../ux-design-principles/references/ux-writing.md`.
5. **Trust signal:** the Inventory Trash page itself, and a visible Activity Log entry ("Removed 'Blue Ceramic Mug' — you, 2 minutes ago"), reduce the anxiety of "did I just break something" by making the action fully visible and reversible after the fact.

## Why This Is Better for This Audience

No step in the redesign asks the manager to make an irreversible decision under time pressure. The safety net (undo → soft delete → audit trail) does the work that a single blocking confirmation dialog was trying — and failing — to do, while keeping the actual task (removing a discontinued product) fast and frictionless for the common case.
