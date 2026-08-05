# UX Design Mentor Plugin

**by [Naser Elziadna](https://github.com/NaserElziadna)**

[![CI](https://github.com/NaserElziadna/ux-design-mentor/actions/workflows/ci.yml/badge.svg)](https://github.com/NaserElziadna/ux-design-mentor/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.5.0-blue.svg)](CHANGELOG.md)

A comprehensive Claude Code plugin that helps you design better UIs/UX by leveraging insights from 10 essential design books plus industry-standard supplementary frameworks. It evaluates, generates, and teaches design principles — covering UX process, visual execution, design-system consistency, and non-technical admin UX — in a non-generic, context-aware way.

## Features

- **Design Evaluation**: Analyze designs (text, code, images) against established principles
- **Design Generation**: Get design recommendations with context-specific guidance
- **Design Audit**: Comprehensive research-focused audit with validation methodology
- **Context-Aware Guidance**: Domain-specific advice for e-commerce, B2B, mobile, accessibility
- **Visual Design Craft**: Concrete typography/color/spacing/layout guidance, and how to avoid the generic "AI-template" look
- **Design Systems**: Component hierarchy and design tokens for consistency at scale
- **Admin UX for Non-Technical Users**: Safety- and confidence-first patterns for back-office tools, distinct from power-user B2B SaaS
- **Principle Checklists**: Systematic evaluation with ratings per principle
- **Book- and Research-Grounded**: All recommendations cite a specific book, framework, or study — never unattributed opinion
- **Design Review Agent**: A self-contained `design-analyst` subagent that reviews UI code/screenshots and returns a prioritized, principle-cited report
- **Image Search & Inspiration** (`design-inspiration`): Python script that searches/downloads images from the web, Pinterest, Dribbble, Behance (via search index) plus license-safe sources (Openverse, Wikimedia, Pexels, Unsplash) — for moodboards and realistic mockup content
- **Image Toolbox** (`design-image-tools`): Python script with palette extraction, WCAG 2.2 contrast checking, image analysis (luminance/busyness/text-overlay advice), resize/crop, web optimization, branded placeholders, and favicon generation

## Books & Frameworks Included

**The 10 books:**

1. **The Design of Everyday Things** - Don Norman (Affordances, signifiers, feedback, constraints, mapping, conceptual models, the Gulfs of Execution/Evaluation)
2. **UX for Beginners** - Joel Marsh (Fundamentals, bite-sized lessons)
3. **Designing Products People Love** - Scott Hurff (Product leadership insights)
4. **Inspired** - Marty Cagan (Team dynamics, product strategy)
5. **Don't Make Me Think** - Steve Krug (Simplicity, common sense, the Trunk Test, Reservoir of Goodwill)
6. **Designing Interfaces** - Jennifer Tidwell et al. (Patterns, components)
7. **Change By Design** - Tim Brown (Design thinking methodology)
8. **Evil by Design** - Chris Nodder (Persuasion and psychology)
9. **UX Research** - Brad Nunnally & David Farkas (Research methodology)
10. **The Mom Test** - Rob Fitzpatrick (User validation, asking good questions)

**Supplementary industry-standard frameworks** (added to cover real gaps the books don't address):

- **Nielsen's 10 Usability Heuristics** (Nielsen Norman Group) — the canonical evaluation checklist
- **Laws of UX** (Jon Yablonski) — 21 cognitive/psychological mechanisms (Fitts's, Hick's, Miller's Law, etc.)
- **UX Writing & Microcopy** (NN/g, Material Design, *Nicely Said*) — button labels, error messages, empty states
- **Refactoring UI** (Adam Wathan & Steve Schoger) — concrete typography, color, spacing, and depth execution
- **Atomic Design** (Brad Frost) & **design tokens** — component hierarchy and consistency at scale
- **WCAG 2.2** (current W3C standard) — accessibility criteria, including the additions past WCAG 2.1

**Topic deep-dives (v0.5.0, internet-researched from NN/g, Baymard, Material 3, Apple HIG, W3C):**

- **Forms & Input UX** — label placement, validation timing ("reward early, punish late"), mobile keyboards, checkout field findings (Baymard), accessible authentication
- **Touch & Mobile Standards** — target sizes (Apple 44pt / Material 48dp / WCAG 24px), Hoober's thumb-zone research, 16px iOS zoom threshold
- **Onboarding & Empty States** — the four empty-state types, NN/g's tour-skipping findings, endowed-progress effect (19%→34% completion)
- **Dashboards & Data Viz** — chart selection rules, axis integrity, data-ink ratio, per-widget states, alert fatigue
- **Motion & Microinteractions** — M3 duration/easing tokens, NN/g response-time limits, skeleton vs spinner, prefers-reduced-motion
- **Dark Mode** — #121212 surfaces, elevation-as-overlay, desaturated accents, token-based theming
- **Conversion & Checkout** — Baymard cart-abandonment causes, guest checkout, trust signal placement, dark-pattern lines
- **Accessibility Deep-Dive** — WCAG 2.2's nine new criteria with pass/fail examples, SPA focus management, ARIA APG keyboard patterns

## Installation

Works with every major AI coding agent. The plugin format (skills + agents + AGENTS.md) is supported natively by most clients; for the rest, use the manual setup at the bottom.

### Claude Code

```
/plugin marketplace add NaserElziadna/ux-design-mentor
/plugin install ux-design-mentor@ux-design-mentor
```

### Codex CLI

Run `/plugins`, then:

```
/plugins install https://github.com/NaserElziadna/ux-design-mentor
```

Or clone the repo and add a pointer to `ux-design-mentor/AGENTS.md` in your `~/.codex/AGENTS.md`.

### Codex App

Plugins → paste `https://github.com/NaserElziadna/ux-design-mentor` → **+**

### Cursor

```
/add-plugin https://github.com/NaserElziadna/ux-design-mentor
```

Or manually: clone the repo, then create `.cursor/rules/ux-design-mentor.mdc` containing the contents of `exports/system-prompt.txt` (or a rule that says "consult ux-design-mentor/AGENTS.md for all UI/UX work").

### Gemini CLI

```
gemini extensions install https://github.com/NaserElziadna/ux-design-mentor
```

### GitHub Copilot / Copilot CLI

```
copilot plugin install https://github.com/NaserElziadna/ux-design-mentor
```

Or manually: clone the repo and append to `.github/copilot-instructions.md`: "For any UI/UX design work, consult ux-design-mentor/AGENTS.md and its skill files."

### OpenCode

Clone into your project (or a shared tools folder) — OpenCode reads `AGENTS.md` automatically:

```bash
git clone https://github.com/NaserElziadna/ux-design-mentor.git
```

Then add to your `opencode.json`: `"instructions": ["ux-design-mentor/AGENTS.md"]`

### Windsurf

Clone the repo, then add to `.windsurfrules`: "For all UI/UX design work, consult ux-design-mentor/AGENTS.md and follow its skill files."

### aider

```bash
git clone https://github.com/NaserElziadna/ux-design-mentor.git
aider --read ux-design-mentor/AGENTS.md
```

### Any other agent (manual setup)

Everything here is plain Markdown + standalone Python — nothing requires a specific client:

1. `git clone https://github.com/NaserElziadna/ux-design-mentor.git`
2. Point your agent at **[AGENTS.md](AGENTS.md)** (task → skill-file map + tool commands), or embed `exports/system-prompt.txt` into your agent's system prompt / rules file.
3. For the Python tools: `pip install pillow ddgs` (optional: `PEXELS_API_KEY` / `UNSPLASH_ACCESS_KEY` env vars for stock photo APIs).

## Quick Start

### User-Invoked Skills

Skills auto-activate when your message matches their trigger phrases — you don't need to remember exact syntax, just describe your design problem naturally:

- "Evaluate this checkout flow: product page → cart → shipping → payment" → **design-evaluate**
- "Help me design navigation for a productivity app with 8 features" → **design-generate**
- "Audit our new dashboard design and tell me what to validate with users" → **design-audit**
- "What should I prioritize designing a B2B admin dashboard?" → **design-context**
- "What does Don Norman say about affordances?" → **ux-design-principles**
- "This looks like every other AI-generated SaaS site" → **design-visual-craft**
- "Should we build a component library for this?" → **design-systems**
- "Our store managers need a safe way to manage orders in the admin panel" → **design-admin-ux**

If your Claude Code setup supports explicit skill invocation, you can also call any of them directly, e.g. `/ux-design-mentor:design-evaluate`, `/ux-design-mentor:design-visual-craft`, `/ux-design-mentor:design-admin-ux`.

Newer skills (0.3.0–0.5.0):

- "Find Pinterest inspiration for a coffee shop landing page" → **design-inspiration** (searches & downloads images)
- "Extract a palette from this hero image" / "check this contrast" → **design-image-tools**
- "How long should this animation be?" / "add hover transitions" → **design-motion**
- "Design this settings/edit form" / "when should validation fire?" → **design-forms**
- "Make a dark mode for this" → **design-dark-mode**
- "Which chart should I use?" / "design this admin dashboard" → **design-dashboards**
- "Design the first-run experience / empty states" → **design-onboarding**
- "Does this work on phones?" / "bottom nav or hamburger?" → **design-mobile**

## Slash Commands (Claude Code)

- `/ux-design-mentor:audit [path]` — measured UX/a11y audit + principle review
- `/ux-design-mentor:tokens #4f46e5` — WCAG-validated design-token system
- `/ux-design-mentor:inspire coffee shop landing` — inspiration hunt + moodboard

## Python Toolbelt (5 scripts)

| Script | Skill | Does |
|---|---|---|
| `fetch_images.py` | design-inspiration | Search/download images: web, Pinterest, Dribbble, Behance, Openverse, Wikimedia, Pexels, Unsplash |
| `moodboard.py` | design-inspiration | HTML moodboard from an image folder with per-image palettes + aggregated direction palette |
| `image_tools.py` | design-image-tools | palette / contrast (WCAG 2.2) / analyze / resize / optimize / placeholder / favicon |
| `audit_page.py` | design-evaluate | Static UX & a11y audit of HTML/CSS: alt text, labels, headings, focus styles, measured contrast failures, vague links, keyboard traps |
| `design_tokens.py` | design-systems | Full WCAG-validated token system (color scales, type scale, spacing, radius, shadows) from one brand hex |

## Agents (3)

- **design-analyst** — multi-pass review of UI code/screenshots: Nielsen heuristics, visual craft, domain patterns, WCAG — with measured contrast, returns a prioritized principle-cited report
- **visual-reviewer** — opens a RUNNING page in a browser, screenshots desktop + mobile, critiques what users actually see (hierarchy, spacing, responsive breakage, generic-AI-look symptoms)
- **inspiration-researcher** — hunts references on Pinterest/Dribbble/Behance/web, builds a moodboard, and synthesizes a concrete visual direction (palette, type mood, layout, one distinctive move)

### The design-analyst Agent

Ask Claude to "review my design" (or point it at UI files/screenshots) and the **design-analyst** subagent runs a full multi-pass review — Nielsen heuristics, visual craft, domain patterns, WCAG 2.2 — with objectively measured contrast ratios, and returns a prioritized report where every finding cites a principle and every fix is concrete.

### Image scripts — requirements

- Python 3.9+; `pip install pillow` for most `image_tools.py` commands
- `pip install ddgs` for reliable web/Pinterest/Dribbble/Behance image search
- Optional: `PEXELS_API_KEY` / `UNSPLASH_ACCESS_KEY` env vars for stock photo APIs
- Licensing: search-engine results are for inspiration/mockups only; use Openverse/Wikimedia/Pexels/Unsplash for anything that ships

## Configuration

Set your default preferences by creating `.claude/ux-design-mentor.local.md` in your project root:

```markdown
---
preferred_domain: e-commerce
output_style: checklist
---
```

- `preferred_domain`: `e-commerce` | `b2b` | `mobile` | `accessibility` | `admin-non-technical` (skips the domain-detection question in `design-context`/`design-audit`; `admin-non-technical` routes to `design-admin-ux` instead of the B2B SaaS guide)
- `output_style`: `checklist` | `narrative` | `alternatives` (sets the default format for `design-evaluate`/`design-generate` output)

Skills check for this file and honor it when present; if it's missing, they ask or infer from context. Add `.claude/*.local.md` to your project's `.gitignore` — this file is per-user, not shared config.

## Plugin Skills

### `design-evaluate` - Smart Design Evaluation
Analyzes designs with adaptive workflow:
- Checklist mode for systematic review
- Narrative mode for story-based feedback
- Interactive Q&A for personalized insights
- Intelligently chooses approach based on input

### `design-generate` - Smart Design Generation
Generates recommendations with user input:
- Asks what you need
- Suggests scope options
- Provides tailored solutions

### `design-audit` - Holistic Design Audit
Comprehensive audit covering:
- Research methodology and validation
- Design assumptions audit
- Research roadmap planning
- Competitive analysis

### `design-context` - Domain-Specific Guidance
Tailored advice for:
- E-commerce (conversion, discovery, trust)
- B2B SaaS (efficiency, power users, dashboards)
- Mobile-first (touch, performance, responsiveness)
- Accessibility (WCAG, inclusivity, screen readers)

### `ux-design-principles` - Core Knowledge Base
Central reference for all design principles with:
- Quick principle summaries
- Detailed examples from each book
- Application patterns
- Interactive Q&A format
- Supplementary frameworks: Nielsen's 10 heuristics, Laws of UX, UX writing

### `design-visual-craft` - Visual Design Craft
Concrete visual execution grounded in Refactoring UI and current design criticism:
- Typography, color, spacing, and depth systems with specific values
- Named anti-patterns for the generic "AI-template" look (gradient heroes, bento grids, cardocalypse) and their alternatives
- Platform baseline conventions (Apple HIG vs. Material Design 3)

### `design-systems` - Design Systems
Component hierarchy and design tokens for consistency at scale:
- Atomic Design methodology (atoms → molecules → organisms → templates → pages)
- A concrete starter design-token set (color, type, spacing, radius, shadow)
- When to formalize a system vs. stay ad-hoc, with warning signs

### `design-admin-ux` - Admin UX for Non-Technical Users
Comprehensive, safety-first guidance for back-office tools, distinct from power-user B2B SaaS:
- Destructive-action patterns (undo, soft delete, confirmation tiers) to prevent "are you sure" fatigue
- Anxiety-reduction patterns (wizards, plain language, guardrails, audit trails, permission clarity)
- Data-table simplification for non-technical users

## Agents

### `design-analyst` - Proactive Design Analysis
Automatically triggers when you discuss:
- Design decisions or challenges
- Product feedback
- Usability concerns

Intelligently routes to appropriate analysis (evaluate, generate, teach).

## Standalone Exports

The plugin generates three export formats for use outside Claude Code:

### System Prompt (system-prompt.txt)
Copy-paste instructions for:
- ChatGPT
- Claude API
- Other AI models

### Markdown Guide (DESIGN-PRINCIPLES.md)
Comprehensive reference guide for design principles

### JSON Config (prompt-config.json)
Structured format for programmatic AI integration

## Examples

### Example 1: Evaluate an E-commerce Checkout Flow
```
Input: "Evaluate our checkout flow: product page → cart → shipping form → payment"
Output: Principle checklist, 7/10 score, top 3 improvements based on Don Norman + Steve Krug
```

### Example 2: Generate Mobile App Navigation
```
Input: "We need navigation for a productivity app with 8 main features"
Output: Three approaches (tab bar vs drawer vs combo), pros/cons, which principle supports each
```

### Example 3: Audit Research Approach
```
Input: "We designed a new dashboard for power users, what should we validate?"
Output: Research methodology (The Mom Test), assumptions to validate, suggested study plan
```

### Example 4: Fix a Generic-Looking Landing Page
```
Input: "This SaaS landing page looks like every other AI-generated site"
Output: Named anti-patterns present (gradient hero, cardocalypse, bento grid), specific
palette/type/spacing fixes, and why each default choice is the "AI tell"
```

### Example 5: Safe Deletion Flow for a Non-Technical Admin
```
Input: "Store managers keep worrying they'll break something when deleting a product"
Output: Decision-order pattern (undo → soft delete → confirmation → non-standard
confirmation), reasoning for why "Are you sure?" dialogs fail this audience
```

## Future Enhancements

- **Figma Integration**: Pull and analyze actual design files
- **GitHub Integration**: Analyze deployed UI code
- **Image Processing**: Vision-based design analysis
- **Design Critique Community**: Compare against peer designs

## Support

For issues or feature requests, see the plugin documentation or contact the author.

## License

MIT - Feel free to use, modify, and distribute.

---

## Author

Built and maintained by **Naser Elziadna** — [github.com/NaserElziadna](https://github.com/NaserElziadna)

If this plugin helps you design better products, star the repo and share it.
