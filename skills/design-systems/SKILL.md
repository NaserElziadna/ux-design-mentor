---
name: design-systems
description: This skill should be used when the user asks about "design systems", "component libraries", "design tokens", "atomic design", "how do I keep this consistent across screens", "when should we build a component library", or wants guidance on structuring reusable UI components at scale — as opposed to a single screen's evaluation or visual polish.
version: 0.1.0
---

# Design Systems

Structuring UI as a system of reusable components and named design tokens, so consistency holds as a product grows past what any one person can track by memory alone. Grounded in Brad Frost's Atomic Design methodology and current design-tokens practice.

## Overview

Individual screens can be evaluated (`design-evaluate`) and individually polished (`design-visual-craft`), but neither prevents *drift* — the slow divergence where five teams each build a slightly different button because nothing forced them to reuse the same one. This skill is about the structure that prevents that: component hierarchy and design tokens.

**User preferences:** Check whether `.claude/ux-design-mentor.local.md` exists in the project. If it sets `preferred_domain`, note that B2B SaaS and admin-heavy products (`design-context`, `design-admin-ux`) benefit disproportionately from an early design system, since they accumulate the most screens fastest.

## Atomic Design (Brad Frost)

The core thesis: **"We're not designing pages, we're designing systems of components."** Five levels, from abstract to concrete:

1. **Atoms** — the smallest indivisible pieces: a label, a text input, a button, a color palette, a font, an animation timing value. Mostly useful as an inventory, not functional alone.
2. **Molecules** — small, simple combinations of atoms serving one purpose. Example: a label + search input + button combine into a *search-form* molecule — together they satisfy a single responsibility, which makes the piece easy to test and reuse identically everywhere a search box is needed.
3. **Organisms** — complex, distinct sections built from molecules and/or atoms, forming a recognizable standalone part of an interface. Example: a *header* organism = logo atom + primary-nav molecule + search-form molecule. Organisms show how pieces behave together in context, not in isolation.
4. **Templates** — page-level layouts that place organisms into structure, focused on content *structure* rather than final content — effectively a wireframe made of real components, setting guardrails for dynamic content (expected image sizes, text lengths).
5. **Pages** — specific instances of a template with real, representative content substituted in. This is where the system gets stress-tested against actual data: a long headline, a missing avatar, a truncation edge case.

**Why this helps at scale:** every organism/template/page is *composed of* the same finite atom/molecule set rather than bespoke markup, so a fix at the atom or molecule level propagates everywhere automatically — teams stop reinventing buttons and forms per screen. It also gives designers and engineers a shared vocabulary to talk about UI at the right altitude ("this needs a new molecule" vs. "redesign the whole page").

Source: [Atomic Design, Brad Frost — Chapter 2](https://atomicdesign.bradfrost.com/chapter-2/)

## Design Tokens

Design tokens are the atomic *decisions* of a system stored as named variables instead of hardcoded values — a single source of truth shared between design and code.

**Common categories:** color (`color-primary`, `color-text-default`), spacing (`space-xs`/`space-md`/`space-lg`), typography (family/size/weight/line-height), radius (`radius-sm` → `radius-full`), shadow/elevation (`shadow-sm` → `shadow-xl`).

**Why teams use them:** they decouple *what a value means* from *what it currently is* — a rebrand or dark-mode theme becomes a token-file edit instead of a find-and-replace across thousands of components, and tokens give designers and engineers a shared vocabulary ("bump this to `space-lg`") instead of raw pixel arguments.

**A concrete starting token set** (pairs directly with `design-visual-craft`'s spacing scale):
```
space-1 = 4px      radius-sm = 4px       shadow-sm  (buttons, chips)
space-2 = 8px      radius-md = 8px       shadow-md  (dropdowns, popovers)
space-3 = 16px     radius-lg = 16px      shadow-lg  (modals, dialogs)
space-4 = 24px     radius-full = 9999px
space-5 = 32px
space-6 = 48px
space-7 = 64px
```
See `references/design-tokens-example.md` for a fuller worked example including color and type tokens.

Source: [Penpot — What Are Design Tokens?](https://penpot.app/blog/what-are-design-tokens-a-complete-guide/)

## When to Formalize a Design System

Brad Frost's take: it's "never too early" to *think* in component-driven terms — that discipline costs nothing extra and prevents debt later. A heavyweight, fully-governed system is a separate, bigger investment decision. Warning signs it's time to formalize:

- **Team/product growth outpacing shared components** — new people join without a mapped component library in design or code, and divergence starts immediately.
- **Duplicated "snowflake" solutions** — multiple teams independently build near-identical components with mismatched variants (a UI audit turning up "a dozen blue hues or button permutations" is the classic tell).
- **Design/dev drift** — designers work far ahead of what's actually implemented, producing inconsistent, messy engineering.
- **Redesign/build friction** — every new screen starts from scratch instead of assembling existing parts, so velocity keeps dropping as the product grows.
- **"Shadow components"** — teams quietly rebuild system pieces because they don't trust, can't find, or don't think the official component covers their case — a sign the system exists but isn't actually adopted.

Conversely: a very early-stage product still searching for product-market fit risks a system being *premature* — a restrictive structure locked in before the product's actual shape is known. The commonly recommended middle path is a **lightweight system** (a handful of core components plus a few stated principles) that grows only as real duplication or inconsistency pain shows up.

Sources: [Brad Frost — Design Systems Q&A](https://bradfrost.com/blog/post/design-systems-qa/) · [NN/g — Design-System Maturity: A 6-Dimension Framework](https://www.nngroup.com/articles/design-system-maturity/)

## Well-Known Reference Systems

- **Material Design (Google)** — the most widely referenced system; documents not just components but explicit *when-to-use* guidance and a full motion/elevation model.
- **IBM Carbon** — enterprise-grade, fully token-driven, open source, framework-agnostic (React, Angular, Vue, web components); a strong reference for accessibility rigor.
- **Shopify Polaris** — commerce-focused; notable less for visual flair and more for exceptional content/UX-writing guidelines tuned to merchant workflows (pairs well with `../ux-design-principles/references/ux-writing.md`).
- **Atlassian Design System** — battle-tested across many distinct products (Jira, Confluence, Trello); strong on cross-product *patterns* and governance, not just a component kit.

## Additional Resources

- **`references/design-tokens-example.md`** — Fuller worked token set (color, type, spacing, radius, shadow)
- **`../design-visual-craft/SKILL.md`** — The visual-craft rules that these tokens should encode
- **`../design-context/references/b2b-saas.md`** and **`../design-admin-ux/SKILL.md`** — Domains that accumulate screens fastest and benefit most from early tokenization

## Token Generator Script

To bootstrap a concrete, WCAG-validated token system from a single brand color (instead of hand-writing one):

```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/design-systems/scripts/design_tokens.py" "#4f46e5" --format css   # :root variables
python "${CLAUDE_PLUGIN_ROOT}/skills/design-systems/scripts/design_tokens.py" "#4f46e5"                # full JSON
```

Generates: brand scale 50–950, hue-tinted neutral scale, harmonized semantic colors (success/warning/danger/info), a modular type scale (`--type-ratio`, default 1.25), 4px spacing scale, radius and shadow tokens — plus an `accessibility` report saying which steps pass AA on white/dark and what to use for button backgrounds. Present the accessibility pairings to the user alongside the tokens; they encode the contrast decisions so the user doesn't reinvent them per screen.
