# Avoiding the Generic AI/Template Look

Named anti-patterns from current (2025-2026) design criticism of AI-generated and template-generated interfaces, with concrete alternatives. Root cause across every source: generative models predict the *statistical average* of training data, and the average web page is a generic SaaS template — a vague prompt or vague brief makes any generator (human or AI) default to the most common pattern rather than a designed one. The fix is making explicit decisions, not applying decoration.

Sources: [vibecodekit.dev — AI Slop Design](https://vibecodekit.dev/ai-slop-design) · [925studios — AI Slop Design Tells](https://www.925studios.co/blog/ai-slop-design-tells) · [Shuffle — Why AI-Generated Websites Look the Same](https://shuffle.dev/blog/2026/01/why-do-most-ai-generated-websites-look-the-same/) · [prg.sh](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website)

## Named Anti-Patterns → Alternatives

| Anti-pattern | Why it happens | Alternative |
|---|---|---|
| Purple→blue gradient hero | Traced to Tailwind's default `indigo-500`; the single most-flagged "AI tell" in 2025-2026 critiques | Cap the palette to 3 hues at roughly 60% dominant / 30% neutral / 10% accent, each chosen for a reason (brand, not defaults) |
| Inter/Roboto/Poppins/Space Grotesk used reflexively | Framework/generator default font, never overridden | Deliberately pair a display font with a body font suited to the product's actual tone; vary weight for hierarchy instead of stacking multiple font families |
| Bento grid of 3 feature cards; hero → cards → logos → pricing → FAQ → footer, every time | The most common page skeleton in training data | Vary section rhythm down the page; use one clear focal point per screen; asymmetric layout where it serves the content |
| Flat 1px grey border on every card ("cardocalypse") | Cheapest, safest-looking way to separate content | Default to whitespace first; if separation is still needed, a subtle 3-5% background-lightness shift; add soft elevation only if that's still not enough |
| Floating 3D gradient blobs / abstract orbs behind hero; glassmorphism panels; generic stock photography; centered oversized line icons | Decorative filler that requires no product-specific decision | Real photography or context-specific illustration; motifs that reference something concrete (an era, a material, a cultural aesthetic) instead of generic abstract shapes |
| Dark mode applied automatically as the default | Assumed to look more "modern"/technical | Light mode by default; dark mode offered as a deliberate, considered choice with its own contrast/elevation pass, not a CSS filter over the light theme |
| Identical fade-in-on-scroll animation applied to every element | Cheap way to seem "interactive" | One orchestrated, staggered reveal on load if motion is used at all; spend the effort instead on designing real interaction states — hover, focus, active, disabled, loading |
| Weightless copy ("Build faster. Ship smarter.") paired with interchangeable line icons | Generic copy that could apply to any product in any category | Product-specific copy naming the actual thing the product does; icon/illustration choices tied to the specific feature, not a generic "lightning bolt = fast" stock icon |

## The Operational Fix

Lock a small design-token set — palette, type scale, spacing scale, radius, shadow levels — into a short spec *before* generating or reviewing UI (see `../../design-systems/SKILL.md` for how to structure this). Verify contrast numerically (APCA or WCAG contrast ratio) rather than eyeballing it. This is the direct connection between "define the system upfront" (Refactoring UI's core discipline) and avoiding generic output: a generator or reviewer with no constraints defaults to the average; one working against a locked, specific system can't.

## Platform Baseline Conventions

Knowing the platform's own design philosophy helps distinguish "generic" from "appropriately conventional" — following a platform's real conventions is not the same failure as defaulting to a generic web template.

**Apple Human Interface Guidelines** — philosophy: *Clarity, Deference, Depth*; content takes priority over chrome; "coherency over consistency" (do what's right for the specific platform/context rather than forcing rigid uniformity everywhere).
- Tab bars for top-level navigation (max ~5 items on iPhone); navigation bars for hierarchical drill-down; modals reserved for focused, decision-requiring tasks — not general content display.
- SF Symbols (6,000+ system icons with weight/scale/multicolor variants, Dynamic-Type-aware, dark-mode-aware) are preferred over custom icon sets for system-level consistency.
- Restrained, realistic motion and subtle gradients that direct focus, not decorate for its own sake.

**Material Design 3** — philosophy: cross-platform consistency; a "material" metaphor with physical properties; personalization via "Material You."
- **Dynamic color:** extracts tonal palettes from a seed color (e.g., the user's wallpaper) to theme the whole app — a deliberate personalization mechanism, not arbitrary color choice.
- **Tonal elevation:** surfaces communicate elevation primarily through a primary-color tint overlay rather than drop shadows, so hierarchy still reads correctly in dark mode.
- **Spring-based motion:** physics parameters (stiffness/damping/velocity) instead of fixed easing curves, so animations can interrupt and retarget naturally mid-motion.

Sources: [Medium — Apple HIG vs. Material Design](https://medium.com/@shivaniy0211/apples-human-interface-guidelines-vs-google-s-material-design-guidelines-e28db15028c0) · [Android Developers — Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3) · [m3.material.io — Elevation](https://m3.material.io/styles/elevation/applying-elevation)
