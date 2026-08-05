---
name: design-generate
description: This skill should be used when the user asks to "generate design recommendations", "suggest a design solution", "what should I design", "help me design", "design this feature", "create design options", or describes a problem needing a design solution.
version: 0.1.0
---

# Smart Design Generation

Generate design recommendations grounded in UX principles; asks clarifying questions to scope solution appropriately.

## Overview

Rather than prescribing one solution, this skill helps you explore design options aligned with user needs and constraints.

**Generation approach:** Smart scoping based on context
- **Design direction** - Approach and key principles to follow
- **Specific patterns** - Which established patterns apply
- **Multiple alternatives** - 2-3 different approaches with trade-offs
- **Complete solution** - Full wireframes, flows, and components

**User preferences:** Before presenting recommendations, check whether `.claude/ux-design-mentor.local.md` exists in the project. If it sets `output_style`, default to that format instead of asking. If it sets `preferred_domain`, apply that domain's guidance from `design-context` without asking which domain applies (or from `../design-admin-ux/SKILL.md` if the value is `admin-non-technical`).

## How Design Generation Works

### Step 1: Understand the Problem

Before designing, understand what you're solving:

**Critical questions:**
- What problem are users facing?
- Who are the users?
- What outcome do you want?
- What constraints exist?
- What have you already tried?

**Scope questions:**
- Is this a new feature or redesign?
- How complex is the problem?
- What's your timeline?
- What's your technical capability?

### Step 2: Offer Scope Options

Based on answers, offer generation depth:

**Option A: Design Direction**
- Overall approach
- Key principles to follow
- Recommended patterns
- What to focus on first

**Option B: Pattern Selection**
- Which patterns fit this problem
- How to adapt them for context
- Component recommendations
- Implementation guidance

**Option C: Multiple Alternatives**
- 2-3 different approaches
- Trade-offs of each
- When to use each
- Hybrid approach

**Option D: Complete Solution**
- Full wireframes/flows
- Component specifications
- Interaction patterns
- Accessibility considerations
- Implementation steps

**Default:** Ask user which depth fits their needs

### Step 3: Generate Options

Generate designs grounded in:
- **User research** (The Mom Test, UX Research)
- **Design thinking** (Tim Brown)
- **Established patterns** (Tidwell)
- **Principles** (Don Norman, Steve Krug)
- **Product strategy** (Cagan, Hurff)

### Step 4: Explain Reasoning

For every recommendation, explain:
- **Why this approach** - Problem it solves
- **What principle** - Which book/concept supports it
- **When to use** - Context and constraints
- **How to implement** - Specific steps
- **What to test** - How to validate

## Generation Output Format

### Design Direction (Quick)
```
**Problem:** [What you're solving]
**Solution Direction:** [Overall approach]

**Key Principles to Follow:**
1. [Principle from book] - [How to apply]
2. [Principle from book] - [How to apply]
3. [Principle from book] - [How to apply]

**Recommended Patterns:** (Tidwell)
- [Pattern name] - [Why it fits]
- [Pattern name] - [Why it fits]

**What to Focus On First:**
1. [Critical element]
2. [Important element]
3. [Nice-to-have element]

**Testing Approach:**
Test with [X] users on [specific tasks]
```

### Pattern Selection (Moderate)
```
**Problem:** [What you're solving]

**Best-Fit Patterns:**

**Pattern 1: [Name]** (Tidwell)
- Problem it solves: [Details]
- How to adapt for your context: [Guidance]
- Components needed: [List]
- When to use: [Context]

**Pattern 2: [Name]** (Tidwell)
[Similar structure]

**Recommended Approach:**
Start with Pattern 1 because [rationale]

**Implementation Steps:**
1. [Step]
2. [Step]
3. [Step]

**What to Test:**
[Specific validation approach]
```

### Multiple Alternatives (Exploratory)
```
**Problem:** [What you're solving]

**Approach A: [Name]**
- Concept: [Description]
- Principles used: [Which books]
- Pros: [Advantages]
- Cons: [Trade-offs]
- Best when: [Context]

**Approach B: [Name]**
[Similar structure]

**Approach C: [Name]** (Hybrid)
[Similar structure]

**Recommendation:**
[Your assessment of which fits best and why]

**How to Choose:**
Ask users which resonates: [Specific scenarios to test]

**Implementation Path:**
Start with [Approach]: [Reasoning]
```

### Complete Solution (Comprehensive)
```
**Problem:** [What you're solving]

**Solution Overview:**
[Overall concept]

**User Flow:**
[Step-by-step flow from start to finish]

**Wireframes/Mockups:**
[Visual representations]

**Key Design Decisions:**
1. [Decision] - Reasoning from [Book]
2. [Decision] - Reasoning from [Book]

**Component Specifications:**
- [Component A]: [Details]
- [Component B]: [Details]

**Interaction Patterns:** (Tidwell)
[How things work, what patterns apply]

**Accessibility Considerations:**
- WCAG Level AA compliance
- [Specific considerations]

**Implementation Roadmap:**
Phase 1: [What to build first]
Phase 2: [Next priority]
Phase 3: [Nice-to-haves]

**Validation Plan:**
1. User testing with [X] users
2. Measure [Specific metrics]
3. Success criteria: [What counts as success]
4. Iterate based on: [What you'll change]
```

## Generation Framework

All generation follows this structure:

### 1. Problem Validation
- Have you confirmed this is a real problem?
- Have you talked to users about it?
- Do multiple users face this?
- What are they doing currently?

**Principle:** The Mom Test (Fitzpatrick) & UX Research (Nunnally)

### 2. Scope Definition
- What exactly needs designing?
- What's outside scope?
- What constraints exist?
- What's the timeline?

**Principle:** Design Thinking (Brown) - Define phase

### 3. Option Generation
- What existing patterns apply?
- What novel approaches could work?
- What are the trade-offs?
- What fits your context?

**Principle:** Ideate (Brown) & Patterns (Tidwell)

### 4. Principle Application
- Which Don Norman principles apply?
- Which Steve Krug usability rules?
- Which Marty Cagan product insights?
- Which Tidwell patterns?

**Principle:** All books

### 5. Validation Plan
- How will you test this works?
- What would make you change it?
- What metrics indicate success?
- How will you iterate?

**Principle:** Design Thinking (Brown) - Test phase

## Common Generation Scenarios

### Scenario 1: New Feature Development

**Situation:** You need to add a new capability (e.g., notifications feature to a SaaS product)

**Generation Process:**
1. **Understand user need** - "Why do users need notifications? What problem does this solve?"
   - Interview users about their current workflow without notifications
   - Observe where they currently miss important information
   - Confirm notifications are actually the best solution (vs. email summaries or in-app feed)

2. **Explore pattern options** - "What established patterns exist for notifications?"
   - Refer to Tidwell patterns: toast notifications, notification center, badge counts
   - For SaaS context, consider notification preferences (critical vs. optional)
   - Consider notification channels: in-app, email, mobile, Slack

3. **Generate 2-3 approaches**
   - **Approach A:** Simple toast notifications (minimal, non-intrusive)
   - **Approach B:** Notification center with history (comprehensive, needs navigation)
   - **Approach C:** Hybrid - toast for urgent, center for archive

4. **Recommend best fit** - For SaaS power users, Approach C likely wins
   - Toast for what needs immediate attention
   - Center for review/archive of notifications they dismissed

5. **Define validation approach**
   - Test with 5 power users who complained about missing info
   - Measure: time to discover important changes, satisfaction with notification frequency
   - Success: 80% say "this helps me stay informed"

### Scenario 2: Redesign Project

**Situation:** Current checkout flow has high cart abandonment; you need a better design

**Generation Process:**
1. **Understand what's failing**
   - Analyze where users abandon (80% abandon at shipping, 15% at payment)
   - Interview recent abandoners: "Why didn't you complete your purchase?"
   - Identify specific pain points (unexpected shipping cost, unclear return policy)

2. **Understand user frustration**
   - Users feel "surprised" by costs (The Mom Test - validate what they say)
   - Users distrust security at payment (lack of clear trust signals)
   - Users want confirmation checkout will succeed before entering payment

3. **Define success metrics**
   - Reduce cart abandonment from 65% to <40%
   - Increase average order value (reduce free shipping abandonment)
   - Decrease checkout time <90 seconds for returning customers

4. **Generate alternative approaches**
   - **Approach A:** Show all costs upfront, before adding to cart (prevents surprises)
   - **Approach B:** Guest checkout option, fewer form fields (reduce friction)
   - **Approach C:** Multi-step wizard with clear progress (psychological commitment)
   - **Approach D:** One-page checkout with inline expandable sections (progressive disclosure)

5. **Plan iterative rollout**
   - Launch to 20% of users first
   - Measure abandonment rate
   - If >10% improvement, roll to 100%
   - If <10%, test different approach with next 20%

### Scenario 3: Problem-Solving for Stuck Work

**Situation:** New users struggle to discover features; you need onboarding design

**Generation Process:**
1. **Deep understanding of problem**
   - Watch new users explore for 10 minutes without guidance
   - Note: where do they get lost? What do they miss?
   - Interview: "What were you trying to do?" vs "What did you think this was?"

2. **Brainstorm solutions**
   - Guided tutorial (interactive walkthrough)
   - Contextual help (inline tips at first-use moment)
   - Help center (searchable documentation)
   - Onboarding checklist (shows first steps)
   - Email onboarding sequence (guides over time)

3. **Evaluate against principles**
   - **Clarity (Krug):** Does user understand what to do? Contextual help wins.
   - **Constraints (Norman):** Can they do wrong things? Guided tutorial prevents mistakes.
   - **Affordance (Norman):** Is it obvious something needs learning? Checklist is obvious.
   - **Progressive disclosure (Brown):** Don't overwhelm. Gradual reveal better than info dump.

4. **Recommend approach**
   - Hybrid: Contextual tips for critical moments + optional tutorial + help center
   - Why: Respects user agency, provides help when needed, doesn't force learning

5. **Define testing**
   - New user testing: measure time to first successful action
   - Success metric: 90% complete first task without help request
   - Iterate based on where users still struggle

### Scenario 4: Exploration Mode

**Situation:** You have a general problem (increase user retention) but multiple possible solutions

**Generation Process:**
1. **Generate multiple directions**
   - **Direction A:** Engagement features (daily challenges, streaks, social)
   - **Direction B:** Utility features (advanced reporting, integrations, customization)
   - **Direction C:** Community features (sharing, collaboration, forums)

2. **Test with users**
   - Show quick sketches of each direction to 3-5 users
   - Ask: "Which would make you use this more frequently?"
   - Which direction do power users suggest?

3. **Learn and refine**
   - Users gravitate toward Direction B (advanced features for their workflow)
   - They want customization and integrations, not gamification

4. **Pick direction** - Advanced features / customization

5. **Iterate to solution**
   - Generate detailed designs for API access and custom fields
   - Test with beta users
   - Iterate based on feedback before full launch

## When to Use This Skill

- **Early design** - Exploring possibilities
- **Feature planning** - What should we build?
- **Problem solving** - How do we solve this?
- **Iteration** - How can we improve?
- **Learning** - Show me options
- **Team alignment** - Explore together

## Key Principle: User-Centered Generation

All generation starts with:
1. **Real problem validation** (Mom Test)
2. **User understanding** (UX Research)
3. **Principle-based approach** (Don Norman, Krug)
4. **Established patterns** (Tidwell)
5. **Clear success metrics** (Cagan)

## Additional Resources

- **`../ux-design-principles/SKILL.md`** - Full principles
- **`../ux-design-principles/references/book-6-jennifer-tidwell.md`** - Patterns catalog
- **`../ux-design-principles/references/laws-of-ux.md`** - Cognitive mechanism behind a recommendation
- **`../ux-design-principles/references/ux-writing.md`** - Button/error/empty-state copy for the generated design
- **`../design-audit/SKILL.md`** - Research your users first
- **`../design-visual-craft/SKILL.md`** - Turn a design direction into concrete type/color/spacing choices
- **`../design-systems/SKILL.md`** - Structure the generated components for reuse if this will scale to more screens
- **`../design-admin-ux/SKILL.md`** - If generating for a non-technical admin/back-office audience specifically

## Summary

This skill:
✅ Asks clarifying questions
✅ Offers appropriate scope options
✅ Generates principle-based solutions
✅ Provides multiple alternatives
✅ Explains reasoning thoroughly
✅ Includes implementation guidance
✅ Plans validation approach
✅ Cites source books

Design with confidence, grounded in research and proven principles.
