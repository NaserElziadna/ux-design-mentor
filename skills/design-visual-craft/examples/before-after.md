# Example: Generic Feedback vs. Visual-Craft-Grounded Feedback

**Scenario:** A user shares a SaaS landing page — purple-to-blue gradient hero, three feature cards in a bento grid with 1px grey borders, Inter font throughout, centered line icons, a floating 3D gradient blob behind the headline.

## Generic Feedback (what to avoid producing)

> This looks pretty good! Maybe make the hero a bit more eye-catching, and the cards could use a bit more visual interest. Consider a more modern font. Overall solid design.

This is unusable — no specific value, no reason, nothing to act on.

## Visual-Craft-Grounded Feedback (what this skill should produce)

> **Palette:** The purple→blue gradient hero is the single most-flagged "AI-generic" tell right now — it's Tailwind's default `indigo-500`, not a brand decision. Replace it with a palette built around one deliberate hue at 60% dominant / 30% neutral / 10% accent, with 5-10 hand-picked HSL shades of that hue rather than a gradient standing in for a real color system.
>
> **Typography:** Inter is the reflexive default and reads as unconsidered here. Pick a display font with real personality for the headline (paired with a plain, highly-legible body font) — the choice should say something about the product's tone, not just "modern SaaS."
>
> **Cards:** The 1px grey border on each feature card ("cardocalypse") is doing the cheapest possible version of separation. Try removing the border entirely and relying on whitespace plus a 3-5% background-lightness shift between the card and the page background — add a soft shadow only if that's still not enough contrast.
>
> **Layout:** Three cards in a row is the most common feature-section skeleton in existence — it's not wrong, but it reads as default. Consider breaking symmetry: one larger featured card plus two smaller ones, or a staggered vertical rhythm instead of a uniform grid.
>
> **Icons/decoration:** The centered line icons and the floating 3D gradient blob are decorative filler that requires no product-specific decision — replace the blob with something that references the product concretely (a real screenshot, a specific illustration style tied to what the product actually does), and swap generic stock icons for ones that map to the specific feature, not a generic "lightning bolt = fast."
>
> **Net effect:** none of this changes the page's information architecture or UX — it's purely visual craft. But right now every choice is a framework default, which is exactly what makes it look interchangeable with any other generated SaaS page. Locking a small palette/type/spacing system before revising would prevent this from happening again on the next page.

## Why the Second Version Works

Every claim names a specific anti-pattern (with its common name, so it's recognizable and searchable), states *why* it happens (default value, not a decision), and gives a concrete alternative — not "make it better" but "do this instead, because of this mechanism." This is the same discipline the rest of the plugin applies to UX principles, applied to visual execution.
