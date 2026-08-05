---
name: ux-design-principles
description: This skill should be used when the user asks to "what are the design principles", "show me the principles checklist", "what does Don Norman say about", "explain the principle of affordance", "how should I think about feedback", or otherwise wants to look up, cite, or learn a specific design principle or book by name — as opposed to evaluating, generating, auditing, or getting domain guidance for an actual design (use design-evaluate, design-generate, design-audit, or design-context for those).
version: 0.1.0
---

# UX Design Principles: Core Knowledge Base

A comprehensive reference distilling 10 essential design books into actionable principles, checklists, and frameworks for evaluating and creating user-centered designs.

## Overview

This skill provides the foundational knowledge that powers all design mentor capabilities. Rather than offering generic design tips, these principles are grounded in specific insights from the 10 most influential UX/design books, plus three supplementary industry-standard frameworks (Nielsen's usability heuristics, the Laws of UX, and UX writing principles) that fill gaps the books alone don't cover.

**Key principle categories:**
- **Fundamental concepts** (affordances, feedback, constraints, mapping)
- **User-centered thinking** (research, validation, problem-first design)
- **Product thinking** (strategy, teamwork, validation)
- **Interaction patterns** (interfaces, persuasion, psychology)
- **Design methodology** (design thinking, systematic approaches)

## The 10 Books: Quick Reference

| Book | Author | Core Focus |
|------|--------|-----------|
| **The Design of Everyday Things** | Don Norman | Affordances, feedback, constraints, discoverability |
| **UX for Beginners** | Joel Marsh | Fundamentals, bite-sized actionable lessons |
| **Designing Products People Love** | Scott Hurff | Product leadership, designing desirable solutions |
| **Inspired** | Marty Cagan | Team dynamics, discovery, strategy |
| **Don't Make Me Think** | Steve Krug | Simplicity, common sense, usability |
| **Designing Interfaces** | Tidwell et al. | Patterns, components, interaction design |
| **Change By Design** | Tim Brown | Design thinking methodology, innovation |
| **Evil by Design** | Chris Nodder | Persuasion psychology, ethical manipulation |
| **UX Research** | Nunnally & Farkas | Research methodology, user testing |
| **The Mom Test** | Rob Fitzpatrick | User validation, asking good questions |

## Supplementary Frameworks

Three industry-standard resources beyond the 10 books, added because they cover real gaps: a canonical evaluation checklist, the cognitive mechanisms behind why principles work, and interface copy (which none of the 10 books treat as a first-class topic).

| Resource | Source | Use it for |
|---|---|---|
| **Nielsen's 10 Usability Heuristics** | Nielsen Norman Group | The default structure for a systematic heuristic evaluation — `references/nng-heuristics.md` |
| **Laws of UX** | Jon Yablonski | The cognitive/psychological mechanism behind a recommendation (Fitts's, Hick's, Miller's Law, etc.) — `references/laws-of-ux.md` |
| **UX Writing & Microcopy** | NN/g, Material Design, *Nicely Said* | Button labels, error messages, empty states, confirmation copy — `references/ux-writing.md` |

## Core Design Principles Framework

### 1. Affordances (Don Norman)

**Definition:** Visual and functional cues that suggest how an object should be used.

**In practice:**
- A button should look pressable
- A handle should look graspable
- An underlined link should look clickable

**Checklist:**
- [ ] Can users instantly understand what's interactive?
- [ ] Do affordances match user expectations?
- [ ] Are visual cues consistent throughout the interface?

**See:** `references/book-1-don-norman.md` for detailed affordance patterns

### 2. Feedback & Visibility (Don Norman, Steve Krug)

**Definition:** Clear communication of system state and response to user actions.

**In practice:**
- Form validation messages tell users what went wrong
- Loading states show progress
- Error messages explain how to fix problems
- Confirmation messages validate successful actions

**Checklist:**
- [ ] Does the system respond immediately to user actions?
- [ ] Are errors described clearly and constructively?
- [ ] Can users always see what state the system is in?
- [ ] Are success and failure states visually distinct?

**See:** `references/book-5-steve-krug.md` for usability-focused feedback

### 3. Constraints & Prevention (Don Norman)

**Definition:** Design limitations that prevent errors and guide users toward correct actions.

**In practice:**
- Disable unavailable options instead of showing errors
- Require confirmation before destructive actions
- Restrict input to valid formats
- Hide irrelevant options

**Checklist:**
- [ ] Do constraints prevent common errors?
- [ ] Is it hard to do the wrong thing?
- [ ] Do constraints feel helpful, not restrictive?

### 4. Consistency & Mapping (Don Norman)

**Definition:** Consistent patterns and logical relationships between controls and their effects.

**In practice:**
- Similar actions are triggered the same way
- Related items are grouped together
- Navigation structure mirrors mental models
- Control position matches result position

**Checklist:**
- [ ] Are similar functions performed similarly?
- [ ] Do controls match user mental models?
- [ ] Is the relationship between cause and effect clear?

### 5. Simplicity & Clarity (Steve Krug)

**Definition:** Remove unnecessary elements; make critical information and actions obvious.

**Principle quote:** "Don't Make Me Think"

**In practice:**
- One clear primary action per screen
- Minimize cognitive load
- Remove decorative elements
- Make instructions unnecessary through obvious design

**Checklist:**
- [ ] Can a first-time user understand this instantly?
- [ ] Have unnecessary elements been removed?
- [ ] Is the primary action obvious?
- [ ] Is copy scannable and concise?

**See:** `references/book-5-steve-krug.md` for detailed usability heuristics

### 6. User Research & Validation (Rob Fitzpatrick, Brad Nunnally)

**Definition:** Assumptions must be tested with actual users; design decisions should be evidence-based.

**The Mom Test principle:** People lie in interviews, but their actions don't. Ask about behavior, not opinions.

**In practice:**
- Watch users interact with designs, don't ask how they would use it
- Ask about past behavior, not future intentions
- Seek evidence of the problem you're solving
- Avoid leading questions

**Checklist:**
- [ ] Have you validated the problem with real users?
- [ ] Have users been observed using the design?
- [ ] Do users have a compelling need for this solution?
- [ ] Have you tested assumptions before building?

**See:** 
- `references/book-10-rob-fitzpatrick.md` - The Mom Test methodology
- `references/book-9-brad-nunnally.md` - Research techniques

### 7. Design Thinking Process (Tim Brown)

**Definition:** A human-centered approach: empathize, define, ideate, prototype, test.

**In practice:**
- Start with empathy for actual users
- Define the real problem, not symptoms
- Generate diverse solutions before evaluating
- Test assumptions with prototypes early and often
- Iterate based on feedback

**Checklist:**
- [ ] Have you deeply understood user needs (not requests)?
- [ ] Have you defined the core problem statement?
- [ ] Have multiple solutions been explored?
- [ ] Has the concept been tested with users?
- [ ] Is iteration built into the process?

**See:** `references/book-7-tim-brown.md` for the full design thinking framework

### 8. Product Strategy & Discovery (Marty Cagan)

**Definition:** Design decisions should align with business goals and be validated through discovery.

**In practice:**
- Understand the problem before building the solution
- Involve product managers, designers, developers in discovery
- Test hypotheses, not final solutions
- Measure against key metrics
- Continuous discovery during development

**Checklist:**
- [ ] Is the business outcome clear and measurable?
- [ ] Have discovery conversations happened?
- [ ] Are success metrics defined?
- [ ] Is the team aligned on the problem?
- [ ] Are you testing hypotheses or final solutions?

**See:** `references/book-4-marty-cagan.md` for product team dynamics

### 9. Interaction Patterns & Components (Jennifer Tidwell)

**Definition:** Proven patterns for common interaction problems; consistency across interfaces.

**In practice:**
- Reuse established patterns for standard problems
- Adapt patterns for domain-specific needs
- Document custom patterns for consistency
- Provide component libraries for teams

**Checklist:**
- [ ] Are you using established patterns for common problems?
- [ ] Are patterns consistent across the product?
- [ ] Do custom patterns have clear documentation?
- [ ] Is a component library maintained and used?

**See:** `references/book-6-jennifer-tidwell.md` for pattern catalog

### 10. Persuasion & Psychology (Chris Nodder, Joel Marsh)

**Definition:** Understand how users make decisions; design experiences that support positive actions.

**In practice:**
- Default options guide behavior
- Social proof influences decisions
- Scarcity creates urgency
- Reciprocity encourages sharing
- Progress visualization motivates completion

**Checklist:**
- [ ] Are defaults set to the most helpful option?
- [ ] Does design acknowledge user psychology?
- [ ] Are persuasion techniques ethical and transparent?
- [ ] Does design support user goals, not just business goals?

**See:** `references/book-8-chris-nodder.md` for ethical persuasion patterns

## Evaluation Checklist

Use this framework to evaluate any design systematically:

### Fundamentals (Don Norman)
- [ ] **Affordances**: User expectations match visual cues
- [ ] **Feedback**: System responds clearly to actions
- [ ] **Constraints**: Design prevents errors
- [ ] **Mapping**: Controls match mental models

### Usability (Steve Krug)
- [ ] **Clarity**: Purpose and actions are obvious
- [ ] **Consistency**: Similar things work similarly
- [ ] **Error Prevention**: Hard to do wrong things
- [ ] **Recovery**: Easy to undo/fix mistakes

### User-Centered (All Books)
- [ ] **User Research**: Based on validated needs
- [ ] **Problem Definition**: Solves real problems
- [ ] **Inclusive**: Works for diverse users
- [ ] **Accessible**: WCAG compliant

### Strategy (Cagan, Hurff)
- [ ] **Business Alignment**: Serves clear outcomes
- [ ] **Metrics**: Success is measurable
- [ ] **Team Alignment**: Shared understanding
- [ ] **Iteration Plan**: Learning built in

### Patterns & Interactions (Tidwell)
- [ ] **Consistency**: Uses established patterns
- [ ] **Components**: Reusable and documented
- [ ] **Performance**: Responsive and fast
- [ ] **Accessibility**: Works for all users

## Using These Principles

### For Design Evaluation
1. Use the evaluation checklist above
2. Reference specific books for deeper understanding
3. Cite which principles need improvement
4. Provide examples of better patterns

### For Design Generation
1. Start with the problem (what is the user trying to do?)
2. Reference relevant patterns from Tidwell
3. Ensure feedback and affordances are clear
4. Test assumptions with users (Fitzpatrick)

### For Design Teaching
1. Explain why a principle matters (the research)
2. Show concrete examples
3. Demonstrate the principle in action
4. Reference the foundational book

## Additional Resources

### Reference Files

Detailed guidance for each book:
- **`references/book-1-don-norman.md`** - Affordances, feedback, constraints, mapping
- **`references/book-2-joel-marsh.md`** - Fundamental lessons and frameworks
- **`references/book-3-scott-hurff.md`** - Designing products people love
- **`references/book-4-marty-cagan.md`** - Inspired: product thinking
- **`references/book-5-steve-krug.md`** - Don't Make Me Think: usability
- **`references/book-6-jennifer-tidwell.md`** - Design patterns and components
- **`references/book-7-tim-brown.md`** - Change by Design: design thinking
- **`references/book-8-chris-nodder.md`** - Evil by Design: persuasion
- **`references/book-9-brad-nunnally.md`** - UX Research: methodology
- **`references/book-10-rob-fitzpatrick.md`** - The Mom Test: validation

Supplementary frameworks:
- **`references/nng-heuristics.md`** - Nielsen's 10 Usability Heuristics, the canonical evaluation checklist
- **`references/laws-of-ux.md`** - 21 cognitive/psychological laws (Fitts's, Hick's, Miller's, Jakob's, etc.)
- **`references/ux-writing.md`** - Button labels, error messages, empty states, confirmation copy
- **`references/forms-and-input-ux.md`** - Form design: labels, validation timing, mobile keyboards, checkout fields, password UX
- **`references/onboarding-and-empty-states.md`** - First-run experience, the four empty-state types, activation, progressive onboarding

### Examples

Real-world application examples:
- **`examples/evaluation-checklist.md`** - How to systematically evaluate a design
- **`examples/evaluation-example.md`** - A worked evaluation of a real design

## Quick Principle Lookup

**Need to understand affordances?** → See book-1-don-norman.md

**How do I handle errors?** → See book-5-steve-krug.md (usability)

**What questions should I ask users?** → See book-10-rob-fitzpatrick.md (The Mom Test)

**How do I structure discovery?** → See book-4-marty-cagan.md (Inspired)

**What patterns exist for this problem?** → See book-6-jennifer-tidwell.md (Designing Interfaces)

**How do I test my assumptions?** → See book-9-brad-nunnally.md (UX Research)

**How do I think like a designer?** → See book-7-tim-brown.md (Change by Design)

**What makes users tick?** → See book-8-chris-nodder.md (Evil by Design)

**What's the core problem?** → See book-3-scott-hurff.md (Designing Products People Love)

**What's the standard heuristic checklist?** → See nng-heuristics.md (Nielsen's 10 Usability Heuristics)

**Why does this specific fix work, mechanically?** → See laws-of-ux.md (Fitts's, Hick's, Miller's Law, etc.)

**How should this button/error/empty-state copy read?** → See ux-writing.md

**How should this form behave (labels, validation, keyboards)?** → See forms-and-input-ux.md

**What goes in an empty state / first-run screen?** → See onboarding-and-empty-states.md

---

**This skill forms the knowledge foundation for all design mentor capabilities.** All other skills reference these principles and books when providing guidance: `design-evaluate`, `design-generate`, `design-audit`, and `design-context` for UX process and domain guidance; `design-visual-craft` for typography/color/spacing execution; `design-systems` for component/token consistency at scale; `design-admin-ux` for non-technical back-office interfaces.
