# Destructive Actions: Full Pattern Catalog

NN/g's core guidance on confirmation dialogs: reserve them *only* for actions with serious, hard-to-reverse consequences. Overuse trains users to click through them on autopilot, which defeats the purpose entirely. ([NN/g — Confirmation Dialogs Can Prevent User Errors](https://www.nngroup.com/articles/confirmation-dialog/))

## Pattern 1: Undo Over Confirm (default choice for routine actions)

A toast notification with an inline "Undo" action, shown for a few seconds after the action completes, rather than a dialog shown *before* the action. This is superior for most routine actions because:
- It doesn't interrupt the user's flow with an interstitial decision
- It doesn't require the user to correctly predict, in advance, whether they'll regret the action
- It still provides full recovery for the (usually rare) case where they do

Use for: archiving an item, removing a tag, deselecting/removing a row from a list, marking something inactive.

## Pattern 2: Soft Delete / Trash (default for most "delete" actions)

Mirror Google Drive or Outlook: the deleted item disappears from the main view but sits in a dedicated, searchable Trash for a disclosed recovery window (commonly 30 days) before permanent purge.

Why this is the right default for admin contexts: it lets a non-technical user self-recover from their own mistake without knowing anything technical and without filing a support ticket — which matters enormously for someone who is already anxious about "breaking something." A visible Trash screen (with a clear "restore" action per item) turns "I think I deleted the wrong thing" from a crisis into a two-click fix.

Use for: deleting orders, articles, user accounts, records — any admin object where "gone forever, immediately" isn't actually required by the business.

## Pattern 3: Specific Confirmation Dialogs

For actions more consequential than Pattern 1 but not catastrophic enough to need Pattern 4. Two specificity rules:

- **Name the exact item**, not a generic question: "Delete 'Q3 Sales Order #4471'?" — not "Are you sure?" Generic confirmations are what train users to click through without reading.
- **Label the buttons with the actual action**, not Yes/No or OK/Cancel: "Delete order" / "Keep order." A descriptive verb forces the user to register what they're choosing, rather than pattern-matching a button position.

Use for: canceling an order, removing a user's access, bulk-deleting multiple selected rows.

## Pattern 4: Non-Standard Confirmation (rare, last-resort)

Require the user to type the item's name or a specific word (Mailchimp's "type DELETE to confirm" before deleting an entire list) before the action proceeds. This pattern only works *because* it's rare — if applied broadly it becomes just another dialog to click through without reading.

Use for: permanently purging data with no recovery window, deleting an entire account/organization, any action that is both immediate and truly irreversible.

## Pattern 5: Spatial/Stylistic Separation

Never place a destructive action directly adjacent to a benign one with similar visual weight and size — a misclick between "Archive" and "Delete Forever" sitting next to each other is a design failure, not a user error. Separate them with spacing, and style destructive actions distinctly (e.g., red text/icon, secondary/ghost button style rather than a filled primary button) so the visual weight itself signals caution. This is directly Fitts's-Law-adjacent: proximity between dissimilar-consequence targets increases misclick risk regardless of color coding, so don't rely on color alone.

## Decision Order

When designing any action that removes, disables, or overwrites something, work through these in order and stop at the first one that's adequate:

1. Can this be undo-able via a toast? → Use Pattern 1, no dialog needed.
2. Is it a "delete" where a recovery window is acceptable to the business? → Use Pattern 2 (soft delete/Trash).
3. Is it consequential enough to warrant a pause, but not catastrophic? → Use Pattern 3 (specific confirmation).
4. Is it immediate, irreversible, and rare? → Use Pattern 4 (non-standard confirmation) — and only this case.
5. Regardless of which pattern applies, apply Pattern 5 (spatial/stylistic separation) if this action sits near a safer one.

Defaulting to Pattern 3 or 4 for everything is the most common mistake — it produces confirmation fatigue, which is worse than having no confirmations at all, because it trains the exact autopilot clicking the dialog was meant to prevent.
