---
name: design-context
description: This skill should be used when the user asks about "design for e-commerce", "B2B SaaS design", "mobile design", "accessibility guidance for my product", "design for [specific domain]", "domain-specific principles", or wants guidance tailored to a specific product domain rather than a general design evaluation.
version: 0.1.0
---

# Domain-Specific Design Guidance

Contextualized design principles for e-commerce, B2B SaaS, mobile, and accessibility; adapts universal UX principles to domain-specific constraints and goals.

## Overview

Universal UX principles apply everywhere, but different domains have different priorities, constraints, and user behaviors.

**Domain guides:**
- **E-commerce** - Conversion focus, trust, discovery
- **B2B SaaS** - Efficiency, power users, data-dense
- **Mobile** - Touch, performance, small screens
- **Accessibility** - Inclusive design for all users

**User preferences:** Check whether `.claude/ux-design-mentor.local.md` exists in the project. If it sets `preferred_domain`, use that domain guide by default instead of asking which domain applies — unless the user's message clearly indicates a different domain. If the value is `admin-non-technical`, defer to `../design-admin-ux/SKILL.md` instead of the B2B SaaS guide here.

## How Context Guidance Works

### Step 1: Understand Your Domain

This skill starts by understanding:
- What domain are you in?
- What are your primary goals?
- Who are your users?
- What are the key constraints?
- What does success look like?

### Step 2: Offer Domain Options

**Option A: E-Commerce Design**
Optimized for conversion, trust, and discovery
- Reduce friction to purchase
- Build trust signals
- Enable product discovery
- Optimize pricing display
- Streamline checkout

**Option B: B2B SaaS Design**
Optimized for efficiency and power users
- Reduce clicks/actions
- Support advanced workflows
- Enable data analysis
- Provide customization
- Support teams/sharing

**Option C: Mobile-First Design**
Optimized for touch, performance, and small screens
- Touch-friendly targets
- Offline functionality
- Performance critical
- Progressive disclosure
- Simplified flows

**Option D: Accessible Design**
Inclusive design for all users
- WCAG AA/AAA compliance
- Keyboard navigation
- Screen reader support
- Color contrast
- Semantic HTML

**Step 3: Contextualize Principles**

Apply universal principles with domain lens:

"Feedback is important everywhere, but in SaaS it's critical for long operations. In e-commerce, feedback builds trust."

### Step 4: Provide Specific Guidance

Domain-specific recommendations for:
- Key metrics (what matters in your domain)
- Common patterns (what works well)
- Critical mistakes (what to avoid)
- Testing approach (how to validate)

## Domain Guides

Each domain guide covers primary goals, adapted core principles (with book citations), critical metrics, common patterns, critical mistakes to avoid, and a testing approach. Load only the guide relevant to the detected domain:

- **`references/ecommerce.md`** — Conversion, trust, discovery, checkout friction
- **`references/b2b-saas.md`** — Efficiency, power users, data density, team workflows
- **`references/mobile.md`** — Touch targets, performance, offline capability, responsive design
- **`references/accessibility.md`** — WCAG compliance, keyboard/screen-reader support, inclusive design
- **`references/accessibility-deep-dive.md`** — WCAG 2.2's new criteria, SPA focus management, ARIA patterns per APG, screen-reader testing (beyond the basics file above)
- **`references/touch-and-mobile-standards.md`** — Authoritative touch-target sizes (Apple/Material/WCAG), thumb zones, mobile keyboards, gesture discoverability
- **`references/conversion-and-checkout.md`** — Baymard-grounded checkout & product-page conversion patterns, cart abandonment causes, dark-pattern lines
- **`references/dashboards-and-dataviz.md`** — Dashboard types, chart selection rules, axis integrity, data-ink, per-widget states

**Not sure if this is B2B SaaS or something else?** The B2B SaaS guide assumes technical power users who want density, keyboard shortcuts, and customization. If the actual users are non-technical staff (a store manager, an office worker, a content editor) using an admin panel or back-office tool as a means to their real job — not people trying to master the tool itself — use `../design-admin-ux/SKILL.md` instead. It optimizes for safety and confidence rather than efficiency.

## Cross-Domain Application

**Overlapping Principles:**

Some principles matter across domains:
- Performance (e-commerce & mobile)
- Trust (e-commerce & SaaS)
- Efficiency (SaaS & mobile)
- Accessibility (all domains)

**When priorities conflict:**
Rank by business goals
- E-commerce: Conversion first
- SaaS: Efficiency first
- Mobile: Performance first
- Accessibility: Inclusive always

## Domain Context Framework

**For any domain:**

1. **Identify primary goal** (What matters most?)
2. **Identify users** (Who are they?)
3. **Identify constraints** (What's hard?)
4. **Identify key metrics** (How to measure?)
5. **Adapt principles** (How to apply universally?)
6. **Test in context** (Real users, real scenarios)

## Additional Resources

- **`../ux-design-principles/SKILL.md`** - Universal principles
- **`../design-evaluate/SKILL.md`** - Evaluation in your domain
- **`../design-generate/SKILL.md`** - Generate domain-specific solutions
- **`../design-admin-ux/SKILL.md`** - Non-technical admin/back-office users specifically (distinct from B2B SaaS power users)
- **`../design-visual-craft/SKILL.md`** - Concrete typography/color/spacing execution once domain priorities are set
- **`../design-systems/SKILL.md`** - Keeping domain-specific patterns consistent as the product scales

## Summary

This skill:
✅ Understands your domain
✅ Adapts universal principles
✅ Provides specific patterns
✅ Defines critical metrics
✅ Avoids domain-specific mistakes
✅ Plans domain-focused testing
✅ Prioritizes appropriately
✅ Stays accessible always

Design for your domain, without losing universally good design.
