---
name: design-audit
description: This skill should be used when the user asks to "audit my design", "research my users", "validate my assumptions", "should I build this", "how do I test my design", "what questions should I ask users", or wants to plan research and validation.
version: 0.1.0
---

# Research-Focused Design Audit

Comprehensive audit combining design evaluation with user research methodology; validates assumptions and creates evidence-based improvement plans.

## Overview

A design audit goes beyond feedback—it validates that you're solving real problems for real users and identifies what to test.

Combines:
- **Design evaluation** - How well does it work?
- **Problem validation** - Do users actually care?
- **Assumption auditing** - What are you assuming?
- **Research methodology** - How to test?

**User preferences:** Check whether `.claude/ux-design-mentor.local.md` exists in the project. If it sets `preferred_domain`, apply that domain's audit priorities from `design-context` without asking which domain applies (or from `../design-admin-ux/SKILL.md` if the value is `admin-non-technical`).

## Audit Framework

### Component 1: Design Evaluation
See `design-evaluate` skill for principle-based assessment.

**Quick assessment of:**
- Affordances and clarity
- Feedback and visibility
- Usability and simplicity
- Navigation and consistency

### Component 2: Problem Validation
Is this solving a real problem?

**Assessment questions:**
- [ ] Do users actually face this problem?
- [ ] How frequently does it occur?
- [ ] What's the cost of the problem?
- [ ] Have users tried solutions?
- [ ] Are they willing to pay?

**Research method:** User interviews focused on past behavior (The Mom Test)

### Component 3: Assumption Audit
What are you assuming?

**Common assumptions:**
- "Users want feature X"
- "This is the best approach"
- "Users will discover this"
- "Users prefer this over alternatives"
- "This will increase metric Y"

**For each assumption, ask:**
- [ ] Is this based on evidence?
- [ ] Have you tested with users?
- [ ] What would prove this wrong?
- [ ] What's your confidence level?

### Component 4: Research Plan
How to validate assumptions?

**Plan includes:**
- Research questions (what do you need to learn?)
- Method (interviews, testing, surveys?)
- Participants (who should you talk to?)
- Tasks/questions (what specifically to test?)
- Metrics (how to measure success?)
- Timeline (when to conduct?)

## Audit Output Format

```
## Design Audit Report: [Product/Feature]

### Executive Summary
- Overall assessment: X/10
- Key strength: [What works]
- Primary concern: [What needs validation]
- Highest-impact improvement: [Most critical finding]

### Design Evaluation
[Principle-by-principle assessment with ratings]

### Problem Validation
**Is this a real problem?**

From user interviews:
- [X] % of target users face this problem
- Frequency: [How often?]
- Impact: [What's the cost?]
- Current solutions: [What are they using?]

Assessment: [Problem is/isn't clearly validated]

### Assumption Audit

**Critical Assumptions:**
1. "[Assumption]"
   - Evidence level: [None/Weak/Strong]
   - Tested with users: [Yes/No/Partially]
   - Confidence: [Low/Medium/High]
   - Validation needed: [What would prove this?]

2. "[Assumption]"
   [Same structure]

### Research Validation Plan

**Phase 1: Problem Validation** (Week 1)
- Research: Structured interviews with 5 target users
- Question: "Tell me about the last time you faced [problem]"
- Success metric: 80%+ of users confirm problem relevance
- Timeline: 3-5 days

**Phase 2: Solution Validation** (Week 2)
- Research: User testing of current design
- Tasks: [Specific user tasks to test]
- Success metric: 80%+ task completion rate
- Timeline: 3-5 days

**Phase 3: Iterative Testing** (Week 3+)
- Method: [Iterate based on Phase 1-2 findings]
- Success metric: [Improvement toward goals]

### Recommendations

**Priority 1: Research (Do First)**
Before building/launching, conduct [specific research]
Estimated time: [X days]
Critical because: [Explanation]

**Priority 2: Design Changes** (Based on research findings)
[Specific recommendations]

**Priority 3: Validation Metrics**
Track: [Specific metrics]
Baseline: [Current]
Goal: [Target]

### Implementation Roadmap

**Phase 1 (Validation):**
- Conduct research [dates]
- Analyze findings
- Iterate design based on learning

**Phase 2 (Build/Launch):**
- Implement [core changes]
- Test with users
- Gather metrics

**Phase 3 (Iteration):**
- Analyze metrics
- Identify improvements
- Iterate continuously

### Key Questions to Answer

**Before investing more in this:**
1. [ ] Is the problem validated with real users?
2. [ ] Is your solution the best approach?
3. [ ] Can users discover/use it easily?
4. [ ] Will this move the metrics you care about?
5. [ ] What assumptions are you most uncertain about?

### Research Methodology

**Recommended approach:** The Mom Test (Fitzpatrick)

- Talk to people with the problem
- Ask about past behavior, not hypotheticals
- Avoid leading questions
- Look for commitment, not just agreement
- Document what you learn

### Success Criteria

Design/feature is ready to build when:
- [ ] Problem is validated (80%+ of users confirm it's real)
- [ ] Design tests well with users (80%+ success rate)
- [ ] Assumptions are tested or mitigated
- [ ] Team is aligned on problem and solution
- [ ] Success metrics are defined
- [ ] Implementation plan is clear
```

## Audit Scenarios

### Scenario 1: New Feature - Full Validation Before Building

**Situation:** Your team wants to add a new feature (e.g., "export to PDF")

**Audit Process:**
1. **Validate the problem** - Do users actually need this?
   - Interview 5 target users: "When did you last need to export data?"
   - Ask about current workaround: "How do you share reports now?"
   - Assess frequency and cost: "How often? What's the impact?"
   - Red flag: If users haven't spontaneously mentioned it, they might not actually need it

2. **Validate the solution** - Will this solve it?
   - Show quick mockup: "If PDF export existed, would you use it?"
   - Observe: Do they get excited or polite agreement? (Mom Test principle)
   - Ask commitment: "When could you use this?" "Want to beta test?"
   - Weak signal: Polite "sounds great" but no specific use case

3. **Evaluate the design** - Is the solution usable?
   - Quick usability test: Can 3 users find and use export without help?
   - Measure: Task completion rate, time to export, satisfaction
   - Success criteria: 100% task completion, <30 seconds, "easy to use"

4. **Plan metrics** - How will you measure success?
   - Define: What indicates this feature is valuable?
   - Measure baseline: How many users request PDF export today?
   - Post-launch: Track adoption % among eligible users
   - Success: >30% of target users export within first month

### Scenario 2: Redesign - Understanding What's Broken

**Situation:** Current dashboard has poor engagement; redesign planned

**Audit Process:**
1. **Understand current pain** - What's not working?
   - Analyze usage data: Where do users drop off?
   - Watch users with current design: Where do they struggle?
   - Interview: "What frustrates you about the dashboard?"
   - Root cause analysis: Slow? Confusing? Missing info? Poor layout?

2. **Validate improved approach** - Do users prefer it?
   - Create 2 alternative designs (high-level prototypes)
   - Test with 5-8 power users: "Which helps you find what you need faster?"
   - Measure task completion rate on each design
   - Video record to observe where they struggle
   - Pick design with >80% preference and faster completion

3. **Evaluate new design** - Is it usable?
   - Systematic evaluation against principles (use design-evaluate skill)
   - Test on target users: critical paths only
   - Accessibility audit: WCAG AA compliance
   - Performance check: Load time <2 seconds

4. **Plan rollout** - How to transition?
   - Canary deployment to 10% of users
   - Measure: Adoption, task completion rate, user satisfaction
   - Gradual rollout: 25% → 50% → 100%
   - Option to revert if metrics decline

### Scenario 3: Iteration - Optimize Based on Data

**Situation:** Feature is live but adoption is below target; need to iterate

**Audit Process:**
1. **Identify hypothesis** - What should improve?
   - Analyze data: Users abandon at [specific point]
   - User interviews: "Why didn't you complete [task]?"
   - Generate hypotheses: "Discovery is hard" or "Unclear value" or "Too slow"
   - Prioritize: Which hypothesis is most likely correct?

2. **Test with users** - Do they agree?
   - Show problem area to users: "Do you see this challenge?"
   - Get commitment: "Would [proposed fix] help?"
   - Test fix with prototype: "Is this better?"
   - Look for honest feedback, not polite agreement (Mom Test)

3. **Evaluate impact** - What changed?
   - A/B test the fix with 50% of users
   - Measure: Adoption, task completion, satisfaction
   - Compare baseline vs. with fix
   - Statistical significance: Is improvement real or just noise?

4. **Iterate** - What's next?
   - If fix worked: Roll to 100%, plan next improvement
   - If fix didn't work: Revert, test different hypothesis
   - Continue: Monthly optimization cycle based on data

## Key Research Methods

### The Mom Test (Fitzpatrick)
Best practices for user conversations:
- Talk to people with the problem
- Ask about past behavior
- Avoid leading questions
- Look for commitment/action
- Document everything

### User Testing (Nunnally, Krug)
Validate that your design works:
- 5-8 participants
- Specific tasks
- Think-aloud protocol
- Observe behavior
- Measure task completion

### Interviews (Brown, Nunnally)
Understand problems and needs:
- Open-ended questions
- Dig into specific details
- Understand emotions
- Find patterns
- Learn context

## What to Test

### Must-Test (Before building)
- Does the problem exist? (Do users care?)
- Is this the best solution? (Did you explore alternatives?)
- Can users use it? (Can they complete key tasks?)

### Should-Test (Before launching)
- Will users discover it?
- Is it better than current solution?
- Is it worth the effort?

### Nice-to-Test (After launch)
- Optimization questions
- Feature prioritization
- Engagement patterns

## Common Audit Findings

**Finding: Design is solid, problem isn't validated**
→ Invest in problem research before building

**Finding: Problem is real, design needs work**
→ Iterate design based on user feedback

**Finding: Design and problem are good, assumptions are risky**
→ Plan specific validation for risky assumptions

**Finding: Everything seems good**
→ Still validate with users; assumptions often wrong

## Audit Checklist

```
[ ] Design evaluated against principles
[ ] Problem validated with real users
[ ] Problem frequency/impact understood
[ ] Current solutions explored
[ ] Solution alternatives considered
[ ] Key assumptions identified
[ ] Assumptions tested or risk mitigated
[ ] Success metrics defined and measurable
[ ] User testing completed (or planned)
[ ] Team aligned on problem/solution
[ ] Implementation plan is clear
[ ] Validation metrics are tracked
```

## When to Use This Skill

- **Early stage** - Validate before designing
- **Before launch** - Final validation check
- **Struggling** - Understand what's not working
- **Iteration** - What to improve next
- **Learning** - How to think about validation

## Key Principle: Validate, Don't Assume

The Mom Test (Fitzpatrick):
> "Ideas are worthless. Execution is everything. But what do you execute on?"

Answer: What you can validate with real users.

## Additional Resources

- **`../ux-design-principles/references/book-10-rob-fitzpatrick.md`** - The Mom Test
- **`../ux-design-principles/references/book-9-brad-nunnally.md`** - UX Research
- **`../ux-design-principles/references/nng-heuristics.md`** - Standard heuristic checklist for the evaluation component
- **`../design-evaluate/SKILL.md`** - Design evaluation
- **`../design-admin-ux/SKILL.md`** - If auditing an admin/back-office tool for non-technical users, its safety/anxiety patterns should shape what "success criteria" means

## Summary

This skill:
✅ Evaluates design systematically
✅ Validates problems with users
✅ Audits assumptions
✅ Plans research methodology
✅ Creates evidence-based roadmap
✅ Prioritizes validation needs
✅ Defines success metrics
✅ Guides iteration

Build with confidence, validated by research.
