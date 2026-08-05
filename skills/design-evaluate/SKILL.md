---
name: design-evaluate
description: This skill should be used when the user asks to "evaluate my design", "review this UI", "critique my wireframe", "analyze this interface", "check my design against principles", "is this design good", or provides code/images/descriptions for design analysis.
version: 0.1.0
---

# Smart Design Evaluation

Comprehensive design analysis using 10-book UX principles framework; provides structured feedback with improvement recommendations.

## Overview

This skill evaluates any design—wireframes, code, mockups, descriptions—against foundational UX principles from industry-leading books. Rather than generic advice, evaluation cites specific principles, books, and patterns.

**Evaluation approach:** Adaptive based on design type and evaluation depth needed
- **Quick scan** (~5 minutes) - Surface-level feedback
- **Systematic checklist** (~10 minutes) - Principle-by-principle review
- **Detailed analysis** (~20+ minutes) - Deep dive with patterns and recommendations
- **Interactive Q&A** (~15 minutes) - Questions to understand context, then personalized feedback

**User preferences:** Before choosing an output format, check whether `.claude/ux-design-mentor.local.md` exists in the project. If it sets `output_style`, default to that format (`checklist`, `narrative`, or `alternatives`) instead of asking or guessing.

## Design Evaluation Framework

### Core Principles Evaluated

**Fundamental Interaction Design (Don Norman)**
- Affordances: Clear what's interactive
- Feedback: System responds to actions
- Constraints: Errors are prevented
- Mapping: Controls match mental models

**Usability & Simplicity (Steve Krug)**
- Clarity: Purpose is obvious
- Consistency: Similar things work similarly
- Navigation: Users know where they are
- Error Prevention: Hard to do wrong

**User-Centered Foundation (All Books)**
- Problem Fit: Solves real user problems
- Research Base: Decisions based on evidence
- Inclusivity: Works for diverse users
- Accessibility: WCAG compliant

**Product & Strategy (Cagan, Hurff)**
- Business Alignment: Serves clear outcomes
- User Value: Solves meaningful problems
- Metrics: Success is measurable
- Team Clarity: Shared understanding

**Patterns & Interaction (Tidwell)**
- Pattern Use: Established vs custom
- Component Consistency: Reusable components
- Performance: Fast and responsive
- Accessibility: All patterns inclusive

**Standard Heuristic Pass (Nielsen Norman Group)**
- For a systematic, structured evaluation, run the design against `../ux-design-principles/references/nng-heuristics.md`'s 10 heuristics directly — it's the canonical industry checklist and complements rather than replaces the book-specific principles above.

**Visual Craft (if the request includes visual/aesthetic feedback)**
- Evaluation above covers UX process; it does not cover typography, color, spacing, or whether the design looks generic/templated. If the user wants feedback on the actual visual execution, hand off to or incorporate `../design-visual-craft/SKILL.md`.

## How Evaluation Works

### Step 1: Understand Context
First, understand what's being evaluated:
- **What is this?** (Wireframe, mockup, code, description?)
- **What does it do?** (Main user goal/purpose?)
- **Who are users?** (Target audience?)
- **What problem does it solve?** (Core value proposition?)

This context informs evaluation depth and focus.

### Step 2: Choose Evaluation Depth

**Option A: Quick Scan** (5 min)
- Initial impressions and obvious issues
- Most critical improvements
- High-level recommendation

**Option B: Systematic Checklist** (10 min)
- Principle-by-principle evaluation
- Ratings per principle
- Specific improvement areas
- Priority ordering

**Option C: Detailed Deep Dive** (20+ min)
- Comprehensive analysis of all areas
- Pattern recommendations
- Competitive analysis (where applicable)
- Detailed implementation guidance
- Accessibility audit

**Option D: Interactive Q&A** (15 min)
- Questions about goals and constraints
- Contextual analysis
- Personalized feedback
- Domain-specific guidance

**Default:** Intelligently choose depth based on design type and complexity

### Step 3: Evaluate Against Principles

#### Affordances Assessment
- [ ] Is every interactive element visually distinct?
- [ ] Do visual properties match actual function?
- [ ] Would first-time user understand without instructions?
- [ ] Are disabled states clearly indicated?

**Feedback:** [Specific observations with examples]

#### Feedback & Visibility
- [ ] Does system respond within 100ms?
- [ ] Is current state always visible?
- [ ] Are errors explained constructively?
- [ ] Is success state distinct from error?

**Feedback:** [Specific observations with examples]

#### Simplicity & Clarity
- [ ] Is page/screen purpose obvious in 3 seconds?
- [ ] Is primary action clear?
- [ ] Have unnecessary elements been removed?
- [ ] Is copy scannable and concise?

**Feedback:** [Specific observations with examples]

#### Navigation & Consistency
- [ ] Is user location always clear?
- [ ] Are navigation patterns consistent?
- [ ] Is terminology consistent?
- [ ] Does layout match mental models?

**Feedback:** [Specific observations with examples]

#### Problem-Solution Fit
- [ ] Does this solve a real user problem?
- [ ] Have you validated the problem?
- [ ] Is the solution user-focused?
- [ ] Does it serve user goals first?

**Feedback:** [Specific observations with examples]

### Step 4: Generate Recommendations

Provide:
1. **Overall Assessment** - One sentence summary with 1-10 score
2. **Key Strengths** - What's working well (2-3 items)
3. **Priority Improvements** - Most impactful changes (ranked 1-5)
4. **Pattern Recommendations** - Specific patterns to use (from Tidwell)
5. **Book References** - Cite principles from source books
6. **Next Steps** - How to improve systematically

### Step 5: Book-Grounded Feedback

All feedback cites source books:

**Instead of:** "This button isn't clear"
**Say:** "This button lacks clear affordance (Don Norman). Make it look pressable with color, shadow, and 44px min height for touch targets"

**Instead of:** "The copy is too long"
**Say:** "Copy should be scannable (Steve Krug). Break into bullet points, highlight key benefits, reduce word count by 40%"

**Instead of:** "Add user research"
**Say:** "Validate assumptions with users (Rob Fitzpatrick). Run 5 user testing sessions focusing on [specific task]"

## Evaluation Output Format

### Quick Scan (5 min)
```
**Overall Assessment:** 6/10 - Functional but needs clarity improvements

**First Impressions:**
- Affordances are unclear (Don Norman principle)
- Missing feedback on actions (Steve Krug)
- Navigation path makes sense

**Top 3 Priority Fixes:**
1. Make buttons look pressable (color, shadow, size)
2. Add loading feedback for slow operations
3. Clarify primary action per screen

**Next Step:** Systematic deep-dive evaluation
```

### Systematic Checklist (10 min)
```
**Overall Assessment:** 6/10

**Principle Evaluation:**

| Principle | Rating | Status |
|-----------|--------|--------|
| Affordances | 4/10 | Buttons don't look interactive |
| Feedback | 6/10 | Some feedback missing on actions |
| Simplicity | 7/10 | Generally clear, some clutter |
| Consistency | 8/10 | Navigation is consistent |
| Problem Fit | 7/10 | Solves problem but needs validation |

**Priority Improvements:**
1. [Specific recommendation with why and how]
2. [Specific recommendation with why and how]
3. [Specific recommendation with why and how]

**Book References:**
- Don Norman on affordances
- Steve Krug on simplicity
- Rob Fitzpatrick on validation
```

### Detailed Analysis (20+ min)
```
**Overall Assessment:** 6/10 - Solid foundation, needs refinement

**Strengths:**
- Clear navigation structure
- Consistent interaction patterns
- Good information hierarchy

**Affordances (Don Norman):** 5/10
[Detailed analysis with examples]

**Feedback & Visibility (Steve Krug):** 6/10
[Detailed analysis with examples]

[... all principles ...]

**Pattern Recommendations (Tidwell):**
- Current: [Pattern used]
- Issue: [What's not working]
- Recommended: [Better pattern with rationale]

**Accessibility Audit:**
[WCAG compliance assessment]

**Competitive Analysis:** (if applicable)
[How does this compare to similar products?]

**Detailed Recommendations:** (Priority order)
1. [Specific change with rationale]
2. [Specific change with rationale]
[... more ...]

**Implementation Roadmap:**
- Phase 1 (Critical): [Changes]
- Phase 2 (Important): [Changes]
- Phase 3 (Nice-to-have): [Changes]

**Testing Plan:**
- Validate with 5 users on [specific tasks]
- Measure [specific metrics]
- Success criteria: [What counts as improvement?]
```

### Interactive Q&A (15 min)
```
**Understanding your design:**

Q1: Who are your primary users and what are they trying to accomplish?
[Answers inform evaluation focus]

Q2: What was your main design goal with this solution?
[Answers show problem-solution intent]

Q3: What constraints did you work within?
[Answers prevent unfair criticism]

**Personalized Feedback:**
[Based on context, provide targeted recommendations]

**Domain-Specific Guidance:**
[If e-commerce/B2B/mobile/accessibility, provide specialized advice]
```

## Evaluation Checklist Template

Use this for systematic evaluation:

```
AFFORDANCES & DISCOVERABILITY
- [ ] All interactive elements visually distinct
- [ ] Visual properties match functionality
- [ ] Disabled states clearly indicated
- [ ] No hidden functionality

FEEDBACK & SYSTEM VISIBILITY
- [ ] Response within 100ms for actions
- [ ] Current system state always visible
- [ ] Error messages constructive & clear
- [ ] Success states visually distinct

SIMPLICITY & CLARITY
- [ ] Purpose obvious without instructions
- [ ] Primary action clear & prominent
- [ ] Unnecessary elements removed
- [ ] Copy scannable & concise

CONSISTENCY & NAVIGATION
- [ ] User location always indicated
- [ ] Navigation consistent across product
- [ ] Terminology consistent
- [ ] Layout matches mental models

ERROR PREVENTION & RECOVERY
- [ ] Common errors prevented
- [ ] Confirmation for destructive actions
- [ ] Easy undo when possible
- [ ] Helpful error recovery

USER-CENTERED
- [ ] Solves real problem (validated)
- [ ] Inclusive & accessible (WCAG)
- [ ] Tested with real users
- [ ] Metrics defined

PATTERN & COMPONENT USE
- [ ] Uses established patterns appropriately
- [ ] Components consistent & reusable
- [ ] Performance acceptable
- [ ] Accessibility built in
```

## What Triggers This Skill

This skill activates when users ask to:
- "Evaluate my design"
- "Review this interface"
- "Critique my wireframe"
- "Analyze this UI"
- "Check if this is good design"
- "Provide design feedback"
- "Rate my design"
- "What's wrong with this design?"
- Provide screenshots, code, or descriptions for analysis

## When to Use This Skill

- **During design process** - Get feedback before building
- **Before launch** - Final quality check
- **Iterating on designs** - Understand what to improve
- **Learning UX principles** - See them applied to real designs
- **Competitive analysis** - Evaluate other products
- **Teaching** - Show why certain designs work better

## Additional Resources

### Reference
- **`../ux-design-principles/SKILL.md`** - Full principles framework
- **`../ux-design-principles/references/`** - Detailed book guidance
- **`../ux-design-principles/references/nng-heuristics.md`** - Standard 10-heuristic evaluation checklist
- **`../design-visual-craft/SKILL.md`** - For typography/color/spacing/layout feedback specifically
- **`../design-admin-ux/SKILL.md`** - If the design under evaluation is an admin panel for non-technical users

### Examples
- **`../ux-design-principles/examples/evaluation-example.md`** - Sample evaluation of real design

## Key Principle: Actionable Feedback

Every recommendation should be:
- **Specific:** "Make buttons 44px tall" not "Make buttons bigger"
- **Grounded:** "Don Norman's affordance principle" not "Just a feeling"
- **Actionable:** "Change button color to red with shadow" not "Improve button"
- **Prioritized:** "Most critical:" vs "Nice to have:"
- **Book-Cited:** Reference which book/principle supports the recommendation

## Summary

This skill provides:
✅ Principle-based evaluation (not generic tips)
✅ Adaptive depth (quick scan to deep dive)
✅ Actionable recommendations
✅ Book citations for each principle
✅ Domain-specific guidance
✅ Pattern recommendations
✅ Clear prioritization
✅ Testing/validation suggestions

All grounded in the 10 most influential UX/design books.

## Objective Audit Script

Before (or alongside) the principle-based review, run the static auditor on any HTML/CSS artifact the user provides — it produces measured findings the qualitative review should incorporate and cite:

```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/design-evaluate/scripts/audit_page.py" <file-or-folder>
```

It checks (pure stdlib, JSON output, severity-ranked): document structure (title/lang/viewport/h1/heading skips), image alt text, unlabeled form fields, vague/empty links and buttons, keyboard traps (positive tabindex, div-onclick), autoplay media, and CSS issues — WCAG contrast failures on real color pairs, sub-12px text, missing `:focus` styles, font-family overload. Verify individual color pairs with `../design-image-tools/scripts/image_tools.py contrast`. Merge script findings into the evaluation report with their measured evidence (ratios, line numbers) — never contradict a measured result with an eyeballed judgment.
