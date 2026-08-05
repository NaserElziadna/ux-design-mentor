# Don't Make Me Think - Steve Krug

Practical, common-sense approach to web usability and user testing through simplicity and clarity.

## Core Principle: Don't Make Me Think

Users should be able to understand and use your design without having to think about it.

When users have to think about how to use something:
- They slow down
- They make mistakes
- They abandon the experience
- Friction increases

Every element should communicate its purpose instantly.

## Key Concepts

### Obviousness

Every page should be self-evident.

Users should not need to ask:
- "What is this website about?" (should be immediately obvious)
- "Where am I?" (clear page title, positioning)
- "What can I do here?" (clear primary action)
- "How do I do it?" (instructions should be unnecessary)

**Page anatomy checklist:**
- [ ] Site identity/logo is clear and prominent
- [ ] Current location is obvious (page title, breadcrumbs, visual highlighting)
- [ ] Main content is immediately visible
- [ ] Primary action is obvious
- [ ] Secondary options don't clutter the main message

**Anti-patterns:**
- Clever navigation that requires thought to understand
- Ambiguous terminology that needs explanation
- Hidden functionality requiring discovery
- Multiple conflicting primary actions
- Inconsistent location indication

### Clarity Over Cleverness

Clever design often creates confusion.

**Bad:** Novel interaction patterns that are original but unclear
**Good:** Familiar patterns that work intuitively

Users prefer:
- Standard patterns they recognize
- Clear, direct language
- Straightforward navigation
- Obvious affordances
- No surprises

**Apply this principle:**
- Use standard conventions (most users won't learn your unique system)
- Write in plain language
- Put important information above the fold
- Use clear, action-oriented button labels
- Make navigation consistent

### Scanning Over Reading

Users don't read web content; they scan it.

Users scan for:
- Keywords and headings
- Formatting and emphasis
- Action buttons and links
- Relevant information

**Writing for scanning:**
- Use short paragraphs
- Front-load important info
- Highlight keywords
- Use bulleted lists
- Break up text with headings
- Use visuals and icons
- Keep line length short

**Bad:**
```
Our innovative platform leverages cutting-edge technology to synergize 
your workflow optimization, enabling unprecedented paradigm shifts in 
operational efficiency.
```

**Good:**
```
Save 5 hours per week
Get started in 10 minutes
No setup required
```

### Visual Hierarchy

Page design should guide users' attention to important information.

**Visual weight signals importance:**
- Size: Larger = more important
- Color: Bright/contrasting = more important
- Position: Top/left = more important (in LTR languages)
- Density: Less crowded = more important
- Whitespace: More breathing room = more important

**Implementation:**
- Make primary action largest, most prominent
- Use color strategically (not to decorate)
- Put most important content top-left
- Leave generous whitespace around key elements
- Highlight key information subtly

### Navigation Design

Users need to:
1. Find what they're looking for
2. Understand where they are
3. Know how to go back

**Navigation principles:**
- Consistent location and behavior across site
- Clear current location indication
- Obvious path to home
- Logical grouping of options
- Clear labeling (no jargon)

**Anti-patterns:**
- "Mystery meat" navigation (unclear what links are)
- Unclear navigation labels
- Hidden navigation (no site map, no home link)
- Navigation in unexpected locations
- Inconsistent behavior across pages

### Error Prevention & Recovery

Users will make mistakes. Design should prevent them and help recovery.

**Prevention:**
- Disable options that don't apply
- Confirm destructive actions
- Validate forms in real-time
- Suggest corrections proactively
- Use constraints to guide correct behavior

**Recovery:**
- Plain language error messages
- Explain exactly what went wrong
- Suggest how to fix it
- Don't delete user input on error
- Provide undo when possible

**Error message checklist:**
- [ ] Is it polite? (no blame or negativity)
- [ ] Does it use plain language?
- [ ] Does it explain what went wrong?
- [ ] Does it suggest how to fix it?
- [ ] Is it visible and obvious?

### The Trunk Test

**Definition:** Imagine a user dropped onto any single page of your site, as if they'd been riding in a car trunk and were let out at a random point. Within a few seconds they should be able to answer, without hunting: *What site is this? What page am I on? What are the major sections of this site? Where can I search? How do I get back to the home page?*

**Why it's useful:** it's a concrete, testable version of "is this self-evident" that works on any single page in isolation — you don't need the whole site to run it, just one screen and a stopwatch.

**Evaluation questions:**
- [ ] Looking only at this page, can I identify the site/product identity within a few seconds?
- [ ] Is it obvious which section/area of the product this page belongs to?
- [ ] Is there always a visible way back to a known "home" state?

### Reservoir of Goodwill

**Definition:** Users arrive with a finite tolerance for friction — a "reservoir" that depletes with every confusing label, broken link, or unnecessary step, and refills when the product delights them or clearly respects their time. It's Krug's model for *why* usability problems compound: no single confusing screen causes abandonment, but enough small ones drain the reservoir until the next minor annoyance is the one that makes the user leave.

**Why it matters for evaluation:** it reframes "is this good enough" — a flow doesn't need to be perfect, it needs to not deplete goodwill faster than the product earns it back. It also means minor annoyances are worth fixing even when no single one seems severe enough to justify the work in isolation.

**Evaluation questions:**
- [ ] Across this entire flow (not just one screen), how many small frictions accumulate before the user reaches their goal?
- [ ] Does anything in the experience actively refill goodwill (delight, clear time savings, a job done well) to offset the friction elsewhere?
- [ ] Is there a point in the flow where an accumulation of small annoyances is likely to tip a user into abandoning, even though no single step is a hard blocker?

### Usability Testing

"Get a sense of what it's like to see the site for the first time." - Steve Krug

**Why test:**
- Designers are not users
- You'll be surprised by what confuses people
- Small design changes have big impact
- Testing reveals wrong assumptions

**Test method (simplified):**
1. Give test participant a scenario/task
2. Ask them to think aloud while attempting it
3. Observe where they struggle
4. Note where they get confused
5. Make one specific change
6. Test again

**What to test:**
- Can users find what they're looking for?
- Do they understand what they're looking at?
- Can they use the navigation?
- Do they notice important information?
- Are they confused by anything?

**Testing myth:** "I need 10+ users"
**Reality:** 3-5 users reveal 85% of usability issues

## Common Usability Failures

### Failure 1: Unclear Purpose
Users land on page but don't understand what it's about.

**Fix:**
- Clear, benefit-focused headline
- Obvious explanation of value proposition
- Visual indication of purpose

### Failure 2: Unclear Navigation
Users can't find what they're looking for.

**Fix:**
- Clear, consistent navigation
- Obvious site structure
- Search functionality
- Breadcrumbs for location

### Failure 3: Poor Information Hierarchy
Important information is hidden or unclear.

**Fix:**
- Prominent placement of key info
- Clear visual hierarchy
- Scannable content
- Progressive disclosure of details

### Failure 4: Unexplained Jargon
Users don't understand technical terminology.

**Fix:**
- Use user language, not insider jargon
- Define technical terms
- Provide contextual help
- Test language with actual users

## Steve Krug's Usability Testing Process

### The Three-Question Test

"If someone asks you for your address, and you immediately say it aloud as you're typing it, that's wrong. If you have to pause and think about it, that's wrong." - Steve Krug

Users should:
1. Know what you do without hesitation
2. Know where to start without hesitation
3. Know how to get help without hesitation

### The 5-Second Test

Show a page for 5 seconds, then ask:
- What was the main purpose of the page?
- What did you see?
- Would you stay or leave?

If users can't answer, page messaging needs work.

### Guerrilla Testing

Quick, informal tests with regular people:
- Coffee shop users
- Friends and family
- Coworkers
- 5-10 minutes per test
- One task to complete

Results are often more valuable than formal lab testing.

## Applying Krug to Design Evaluation

**Quick usability audit:**
- [ ] Is page purpose immediately obvious?
- [ ] Can I find main content in 3 seconds?
- [ ] Is navigation clear and consistent?
- [ ] Do buttons clearly show what they do?
- [ ] Is form validation helpful?
- [ ] Would a first-time user succeed?
- [ ] Is copy scannable?
- [ ] Are errors prevented or recovered easily?
- [ ] Is the interface self-explanatory?
- [ ] Does this page pass the Trunk Test (identity, location, section, way home all clear in a few seconds)?
- [ ] Across the full flow, is the reservoir of goodwill being depleted faster than it's refilled?

## Key Principles Summary

1. **Eliminate unnecessary complexity** - Every element must earn its place
2. **Make important information prominent** - Visual hierarchy matters
3. **Create clear navigation** - Users need to know where they are
4. **Use plain language** - No jargon or clever phrasing
5. **Prevent errors** - Better than recovering from them
6. **Test with real users** - You're not the user
7. **Focus on the user's task** - Not the design system
8. **Simplicity requires hard work** - It takes more effort than complexity

## Memorable Quotes

> "Your job is to get out of the way." - Steve Krug

> "If something requires a large instruction manual, it's probably not well designed." - Steve Krug

> "Designing is not just what it looks like and feels like. Designing is how it works." - Steve Jobs (referenced by Krug)

## Testing Checklist

Before launching, test with 3-5 real users:
- [ ] Can they accomplish the main task?
- [ ] Do they understand the page purpose?
- [ ] Can they find what they're looking for?
- [ ] Where did they get stuck?
- [ ] What surprised them?
- [ ] What confused them?
- [ ] Would they recommend it?

Make changes based on feedback, then test again.
