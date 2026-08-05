# Real-World Evaluation Example: Productivity Dashboard Redesign

## The Design Being Evaluated

A project management SaaS tool redesigned their main dashboard. Users see:
- Project list on left sidebar
- Task cards in main area (grouped by status: To Do, In Progress, Done)
- Quick action bar at top (Create Task, Filter, Sort, Settings)
- Team members sidebar on right showing who's assigned

**Designer's goal:** Help busy teams see what everyone is working on at a glance

---

## Step 1: Understand Context

**Questions to answer first:**
- **What is this?** Dashboard redesign for project management SaaS
- **What does it do?** Show tasks organized by status, team visibility
- **Who are users?** Product managers, developers, team leads (power users)
- **What problem does it solve?** Quick status overview without clicking multiple pages

**Context Impact:** B2B SaaS context means efficiency and power-user support matter more than simplicity for novices.

---

## Step 2: Evaluate Against Principles

### AFFORDANCES (Don Norman) - Rating: 7/10

**What works:**
- Task cards clearly look clickable (subtle shadow, pointer on hover)
- Status columns are visually grouped (different background colors)
- Settings icon looks like settings (gear icon, standard)
- "Create Task" button is obviously clickable (prominent, colored)

**What needs work:**
- Drag handle on cards is subtle (might miss that tasks are draggable)
- Assigned team member avatars could be clearer (just small circles)
- Status column headers lack affordance (don't look clickable for filtering)
- Sidebar project names lack visual indication of expansion (arrows very small)

**Assessment:** The primary interactions are clear, but advanced interactions (drag-drop, status filtering) could signal better.

**Recommendation (Don Norman):** "Make affordances obvious. Add stronger visual cues for drag handles (maybe ::drag-handle-icon). Make expandable projects more obviously expandable."

### FEEDBACK & VISIBILITY (Steve Krug) - Rating: 6/10

**What works:**
- Hover states show clearly which task you're about to click
- Assigned avatars show tooltip on hover (current assignee name)
- Status column highlights on hover
- Color change when dragging task (visual feedback)

**What needs work:**
- No loading state when page first loads (users don't know if it's loading)
- No visual feedback when task is created (silent success, refresh required)
- Team member's online status unclear (green dot exists but very subtle)
- Slow data sync doesn't show progress (takes 2-3 seconds, no indicator)

**Assessment:** Immediate interactions provide feedback, but system state (loading, syncing, creation) lacks visibility.

**Recommendation (Krug):** "Provide immediate feedback. Add loading skeleton while data fetches. Show success toast when task created. Make online status more obvious (larger indicator, color contrast)."

### CONSTRAINTS & PREVENTION - Rating: 8/10

**What works:**
- Can't create task without title (form validation)
- Can't drag task to invalid status (constraints based on workflow rules)
- Confirmation required before deleting task
- Disabled "Assign" button if no team members selected

**What needs work:**
- Can accidentally create duplicate task by clicking Create twice quickly (no debounce)
- No warning if trying to navigate away with unsaved task draft
- Can delete completed task immediately without protection (low consequence but still)

**Assessment:** Good constraint design for critical actions, minor gap on accidental duplicates.

**Recommendation:** "Add debounce/disable on Create button after first click to prevent duplicates. Add unsaved draft warning."

### CONSISTENCY & MAPPING (Don Norman) - Rating: 8/10

**What works:**
- All status columns use same layout (card style, spacing)
- Drag-drop works same way in all columns
- Sorting options consistent (name, date, priority)
- Filter icons consistent across page

**What needs work:**
- Team sidebar behaviors differ from project sidebar (expand/collapse different)
- Status colors inconsistent with company branding (blue not brand green)
- Action icons vary in style (some solid, some outline)

**Assessment:** Very consistent overall; a few inconsistencies in sidebars and styling.

**Recommendation:** "Unify sidebar behaviors (project and team should expand/collapse identically). Align status colors to brand palette. Standardize icon styles."

### CLARITY & SIMPLICITY (Steve Krug) - Rating: 7/10

**What works:**
- Task card title is immediately visible
- "To Do / In Progress / Done" statuses obvious
- Quick actions bar at top is recognizable
- Visual hierarchy: important info (title, assignee) are prominent

**What needs work:**
- Too many columns for small screens (not responsive)
- Settings panel overwhelming (20+ toggles visible at once)
- Task description hidden (requires click to see)
- Four different filter/sort options scattered across UI

**Assessment:** Good for power users with large monitors, but cluttered for mobile or casual users.

**Recommendation (Krug):** "Respect different screen sizes. Progressive disclosure in settings (show 5 most-used options, hide rest). Consolidate filters into one UI component. Consider mobile variant."

### NAVIGATION - Rating: 8/10

**What works:**
- Current project highlighted in left sidebar
- Breadcrumb at top (Home > Projects > [Project Name])
- Clear back button to project list
- Consistent top navigation bar

**What needs work:**
- Nested projects unclear (which project is parent of current?)
- Team sidebar position might confuse users (looks like it's another navigation option)
- No quick way to switch between projects in main area

**Assessment:** Clear navigation hierarchy, minor clarity issue with nested projects.

**Recommendation:** "Clarify nested project hierarchy with indentation. Label team sidebar differently (not as nav). Add quick-switch project dropdown in main content area."

### PROBLEM FIT (All books) - Rating: 6/10

**What works:**
- Does address stated problem (quick status overview)
- Shows who's assigned to what
- Supports common task workflows

**What needs work:**
- **Not validated with users:** Have you tested that users want THIS layout?
- **Alternative not explored:** Is task cards better than timeline or board view?
- **Problem not deeply understood:** Why do users need status overview? What's the actual pain point?
- **Success metrics not defined:** How will you measure if this improves team productivity?

**Assessment:** The design addresses a reasonable hypothesis, but that hypothesis isn't validated.

**Recommendation (Fitzpatrick):** "Before launching, test with 5 users. Ask: 'When was the last time you needed to see everyone's work? How did you find it? Would this design help?' Test against current solution. Measure: adoption rate, time-to-task-assignment, user satisfaction."

### ACCESSIBILITY - Rating: 5/10

**What works:**
- Good color contrast on text (white on dark background)
- Keyboard navigation works (tab through tasks)
- Task titles read clearly by screen readers

**What needs work:**
- Status columns not properly marked up (not semantic sections)
- Drag-drop not keyboard accessible (mouse-only interaction)
- Avatar tooltips don't work with keyboard navigation
- No ARIA labels on status columns or task importance indicators
- Color-only status indication (red = urgent) needs pattern/text backup

**Assessment:** Basic accessibility works, but advanced features (drag-drop) are blocked for non-mouse users.

**Recommendation:** "Add keyboard shortcuts for drag-drop (arrow keys to move). Mark columns semantically (`<section role="region">`). Add ARIA labels. Use pattern + color for urgency (not color alone). Test with keyboard and screen reader."

### BUSINESS ALIGNMENT & METRICS - Rating: 6/10

**What works:**
- Clear goal (quick status view)
- Supports team collaboration workflow
- Aligns with product direction

**What needs work:**
- **Success metrics not defined:** What counts as success?
- **Not measuring:** No baseline metrics before launch
- **Assumptions untested:** Assuming users want card view, but haven't tested
- **ROI unclear:** Will this increase productivity? Adoption? Reduce support tickets?

**Assessment:** Reasonable design for stated goal, but goal itself isn't validated.

**Recommendation (Cagan):** "Define success metrics: adoption rate (% of users opening dashboard daily), task completion time, user satisfaction. Measure baseline with old design. Launch to 50% of users, measure impact, then full rollout. Plan to iterate based on metrics."

---

## Step 3: Score Summary

| Principle | Rating | Status |
|-----------|--------|--------|
| Affordances | 7/10 | Good, minor clarity |
| Feedback | 6/10 | Missing system state feedback |
| Constraints | 8/10 | Strong |
| Consistency | 8/10 | Very consistent |
| Clarity | 7/10 | Good for power users, needs mobile |
| Navigation | 8/10 | Clear |
| Error Prevention | 8/10 | Good |
| Problem Fit | 6/10 | Unvalidated hypothesis |
| Accessibility | 5/10 | Basic OK, advanced not accessible |
| Business Metrics | 6/10 | Unmeasured |
| **OVERALL** | **6.9/10** | **Good but needs validation** |

---

## Step 4: Priority Improvements

### Priority 1: VALIDATE BEFORE FULL LAUNCH (Critical)
**Problem:** Unvalidated hypothesis that users want this layout
**Impact:** Could be building wrong thing
**How to fix:**
1. Run 5 user tests with current users
2. Ask them to find "what's Alice working on?" and "what's blocked?"
3. Observe if they find answers quickly
4. Ask which view they prefer: cards vs. list vs. timeline
5. Don't fully launch until validated

**Time:** 1 week
**Owner:** Product Manager + Designer

### Priority 2: ADD SYSTEM STATE FEEDBACK (Important)
**Problem:** Users don't see loading/syncing/creating feedback
**Impact:** Users think interface is broken when it's just slow
**How to fix:**
1. Add loading skeleton while fetching initial data
2. Show success toast when task created: "Task created ✓"
3. Show sync indicator: "Syncing..." with spinner
4. Make online status 2x larger and more obvious

**Time:** 2-3 days
**Owner:** Frontend Engineer

### Priority 3: IMPROVE ACCESSIBILITY (Important)
**Problem:** Drag-drop and advanced features not keyboard accessible
**Impact:** Excludes non-mouse users
**How to fix:**
1. Implement keyboard shortcuts: Up/Down arrow keys to move tasks between statuses
2. Add ARIA labels to all interactive elements
3. Make status colors not-only distinction (add icons or text labels)
4. Test with keyboard navigation and screen reader

**Time:** 3-4 days
**Owner:** Frontend Engineer + QA

### Priority 4: ADD MOBILE RESPONSIVENESS (Nice-to-have)
**Problem:** Cluttered on mobile; all three columns visible
**Impact:** Mobile users have poor experience
**How to fix:**
1. Show one column at a time on mobile
2. Add swipe to navigate between columns
3. Simplify actions for touch
4. Test on actual devices

**Time:** 1 week
**Owner:** Frontend Engineer

### Priority 5: REFINE DRAG AFFORDANCE (Nice-to-have)
**Problem:** Drag handle is subtle; users might not discover drag-drop
**Impact:** Users miss power feature; do more clicking than needed
**How to fix:**
1. Make drag handle more obvious (show on hover, larger)
2. Add tutorial tooltip first time: "Drag tasks to change status"
3. Consider drag icon (≡ or ⋮) before card

**Time:** 1-2 days
**Owner:** Designer + Frontend

---

## Step 5: Book Citations

**This evaluation used principles from:**

1. **Don Norman** - Affordances, feedback, constraints, mapping
   - "The Design of Everyday Things" Chapter 3
   - Applied to: drag handles, status filtering, sidebars

2. **Steve Krug** - Simplicity, clarity, feedback
   - "Don't Make Me Think" Chapter 2-3
   - Applied to: task visibility, system state feedback

3. **Jennifer Tidwell** - Patterns and consistency
   - "Designing Interfaces" Pattern: Card View
   - Applied to: task cards, column consistency

4. **Rob Fitzpatrick** - User validation
   - "The Mom Test"
   - Applied to: problem validation before launch

5. **Marty Cagan** - Product strategy and metrics
   - "Inspired" Chapter 5
   - Applied to: defining success metrics

---

## Conclusion

**Overall Assessment: 6.9/10 - Good design, needs validation**

**Recommendation:** Don't fully launch yet. Validate with 5 users first. The design is solid for power users (SaaS context), but you need evidence that this solves actual problems. After validation, the improvements are mostly polish (drag affordance, mobile) and accessibility fixes.

**Next Step:** Schedule 5 user tests for this week. Run them with instructions: "Show me how you'd find what Sarah is working on." Observe their behavior. That data will guide your next iteration.
