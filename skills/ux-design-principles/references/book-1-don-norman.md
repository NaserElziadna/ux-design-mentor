# The Design of Everyday Things - Don Norman

Core principles for intuitive, discoverable design through affordances, signifiers, feedback, constraints, mapping, and conceptual models — diagnosed through the Seven Stages of Action and the Gulfs of Execution/Evaluation.

## Key Concepts

### Affordances

**Definition:** Properties that suggest how something should be used.

Visual affordances show what's interactive:
- Buttons look pressable (raised, colored, shadowed)
- Links look clickable (underlined, blue, distinctive)
- Sliders look draggable (handles, track)
- Text fields look editable (borders, cursor)

Functional affordances determine actual capabilities:
- A door pushes or pulls based on design
- A knob rotates
- A touchscreen responds to touch

**Evaluation questions:**
- Does each interactive element clearly signal its purpose?
- Do visual properties match actual functionality?
- Would a first-time user understand without instructions?

**Common mistakes:**
- Buttons that don't look clickable
- Links that don't look like links
- Interactive elements hidden or unclear
- Mismatched visual properties (looks like a button, but isn't)

### Feedback

**Definition:** System response that informs users of state and action outcomes.

Essential feedback types:
- **Immediate feedback** - Response within 0.1 seconds (typing, clicks)
- **Progress feedback** - Long operations show status (loading bars, percentage)
- **Completion feedback** - Clear confirmation of success (checkmarks, messages)
- **Error feedback** - Explains what went wrong constructively

**Feedback principles:**
- Feedback must be immediate and obvious
- Use multiple sensory channels (visual + audio + haptic when possible)
- Error messages should be in plain language
- Success should be as obvious as errors

**Evaluation checklist:**
- [ ] Does the system respond within 100ms of user input?
- [ ] Can users see current system state at all times?
- [ ] Are errors described in user-friendly language?
- [ ] Do success and error states look visually distinct?
- [ ] Is progress shown for operations >1 second?

**Implementation patterns:**
- Form validation: Show errors inline, not on submit
- Loading states: Use progress bars, spinners, time estimates
- Deletion: Require confirmation, show what will be deleted
- Errors: Explain problem + solution, not just "Error 404"

### Constraints

**Definition:** Design limitations that prevent errors and guide behavior.

Types of constraints:

**Physical constraints** - Prevent wrong actions physically:
- Power outlet shape prevents wrong insertion
- Camera lenses have limited rotation
- USB ports only fit one way

**Logical constraints** - Mental models guide behavior:
- Filing system organization matches user thinking
- Control position matches result position
- Related items grouped together

**Cultural constraints** - Standards and conventions:
- Red = danger/stop
- Green = go/safe
- Save icons look like floppy disks

**Practical constraints** - Business rules:
- Disable checkout before shipping address entered
- Hide premium features until account verified
- Require password for account deletion

**Evaluation questions:**
- [ ] Does design prevent common errors before they happen?
- [ ] Could users accidentally do something destructive?
- [ ] Are disabled options still visible with explanation?
- [ ] Do constraints help or frustrate users?

**Application examples:**
- Disable "Next" button until required fields filled
- Gray out unavailable options with tooltip explaining why
- Require password confirmation for sensitive changes
- Use logical field order matching user mental model

### Mapping

**Definition:** Clear relationship between control location, control function, and effect.

Good mapping:
- Stove burner controls are arranged like the burners
- Light switches align with room lights
- Menu items are grouped logically
- Navigation hierarchy matches information architecture

Poor mapping:
- Random light switch order
- Hidden settings scattered throughout
- Unintuitive menu organization
- Navigation that doesn't match user thinking

**Evaluation questions:**
- [ ] Does the interface match user mental models?
- [ ] Is the relationship between controls and effects clear?
- [ ] Are related functions grouped together logically?
- [ ] Is terminology consistent with user language?

**Implementation patterns:**
- Organize menus by user tasks, not technical categories
- Use familiar metaphors (save = diskette, trash = bin)
- Keep controls near their effects
- Support multiple mental models when possible

### Conceptual Models

**Definition:** The mental model a user forms of how a system works, built from what the design shows them — not from the system's actual internal logic. Norman treats this as arguably the most load-bearing concept in the book: mapping and feedback matter *because* they're what a conceptual model is built out of. A design succeeds when the user's mental model matches how the system actually behaves; it fails when the two diverge (e.g., a thermostat that users believe works like a valve — "turn it up further to heat the room faster" — when it's actually a simple on/off switch with a target temperature).

**Implementation patterns:**
- Use familiar metaphors deliberately (desktop, shopping cart, trash bin) — they import a conceptual model the user already has
- Make the system's actual behavior visible enough that the user's mental model can self-correct through use
- When the underlying mechanism is invisible (e.g., an algorithm, a cache, an async job), the interface must communicate an approximate, useful model of it — don't leave users to invent one that's wrong
- Consistency across a product reinforces one coherent model instead of forcing users to hold several

**Evaluation questions:**
- [ ] What model would a user reasonably infer about how this works from what's visible?
- [ ] Does that inferred model match what the system actually does?
- [ ] Where the real mechanism is invisible, does the design communicate a good-enough approximation of it?

### Seven Stages of Action & The Two Gulfs

**Definition:** Norman's structural model of how people act on the world, used to diagnose *where* an interaction breaks down rather than just noting that it did. The cycle: **goal** → plan → specify → **perform** the action, then **perceive** → interpret → **compare** the result against the goal.

That cycle collapses into two practically useful gaps:
- **Gulf of Execution** — the distance between what a user intends to do and what the interface lets them actually do. It's wide when the available actions don't obviously map to the user's goal (e.g., no visible way to "cancel this subscription," only a maze of account settings).
- **Gulf of Evaluation** — the distance between the system's actual state and how well the interface lets the user perceive and understand that state. It's wide when it's unclear whether an action worked, is still processing, or failed (e.g., clicking "Submit" with no confirmation, so the user can't tell if it registered).

**Why this matters for evaluation:** most of the principles above are really tools for narrowing one of these two gulfs — affordances and signifiers narrow the gulf of execution (they make it clear what you *can* do), feedback narrows the gulf of evaluation (it makes it clear what *did* happen). Naming which gulf a problem falls into makes feedback sharper than a generic "this is confusing."

**Evaluation questions:**
- [ ] At the point of failure, is the problem that the user couldn't figure out what action to take (execution), or couldn't tell what happened after they took it (evaluation)?
- [ ] Does every stage of the action cycle (plan → act → perceive → interpret) have a visible support in the interface, or does the design go silent at one stage?

### A Note on Affordance vs. Signifier

Norman himself later flagged that "affordance" is the single most misused term from his own book: most people who say "this button has good affordance" actually mean it has a good **signifier** (a perceivable cue), not that it has a good affordance (the underlying possibility for action, which may exist without being perceivable at all, or be perceived without existing). Precision matters when citing this principle: a flat, borderless button *can* still be clickable (the affordance exists) — the actual defect is that it lacks a signifier telling the user so.

### Signifiers

**Definition:** Observable signals that communicate function and affordances.

Signifiers are what users perceive; affordances are the actual capability.

Types:
- Visual signifiers: Color, shape, text labels, icons
- Spatial signifiers: Proximity, alignment, grouping
- Temporal signifiers: Animation, transitions, timing

**Effective signifiers:**
- Obvious and unambiguous
- Consistent with user expectations
- Discoverable without instructions
- Accessible to diverse users (not color-only)

**Common failures:**
- No signifier (hidden affordance)
- Weak signifier (unclear if interactive)
- False signifier (looks interactive but isn't)
- Contradictory signifiers (looks like button, acts like link)

## Case Studies

### Example 1: Smart Door Design
**Problem:** Users push/pull wrong side of door, break glass

**Don Norman solution:**
- Clear signifier: Metal handle on pull side, flat plate on push side
- Affordance: Handle suggests pulling, plate suggests pushing
- Constraint: Door physically easier to pull/push correct direction

**Result:** Eliminated confusion without instructions

### Example 2: Stove Controls
**Problem:** Users select wrong burner because controls don't match layout

**Solution:** Control arrangement matches physical burner arrangement

**Lesson:** Mapping reduces cognitive load and errors

## Applying Don Norman to Design Evaluation

**Checklist for any interface:**
- [ ] Are all interactive elements clearly afforded?
- [ ] Does the system provide immediate feedback?
- [ ] Does design prevent common errors?
- [ ] Does layout match user mental models?
- [ ] Are signifiers clear and consistent?
- [ ] Is terminology user-friendly?
- [ ] Are instructions unnecessary?
- [ ] Could this work without instructions?
- [ ] For any point of confusion: is it a Gulf of Execution problem (unclear what to do) or a Gulf of Evaluation problem (unclear what happened)?
- [ ] Does the design communicate a conceptual model of the system that matches how it actually behaves?

## Key Takeaways

1. **Design is about communicating intent** - Make function obvious
2. **Prevent errors, don't just recover from them** - Constraints prevent problems
3. **Feedback is essential** - Users must know what happened
4. **Support mental models** - Design with user thinking in mind
5. **Simple is hard** - Simplicity requires deep understanding of user needs

> "The best way to make people happy is to give them a device they can use successfully. A device that has good discoverability." - Don Norman
