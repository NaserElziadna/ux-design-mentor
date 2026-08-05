---
name: design-dashboards
description: This skill should be used when the user asks about "dashboard design", "data visualization", "which chart should I use", "KPI cards", "analytics page", "admin dashboard layout", "charts look confusing", or is building/reviewing any dashboard, report, or data-heavy screen.
version: 0.1.0
---

# Dashboard & Data Visualization Design

Read `../design-context/references/dashboards-and-dataviz.md` first (the researched reference: dashboard types, chart selection, axis integrity, Tufte's data-ink). This skill is the decision procedure.

## Decision procedure

1. **Classify the dashboard first** — operational (live monitoring, glanceable, auto-refresh), analytical (exploration, drill-down, comparisons), or strategic (KPIs vs targets, periodic). Different types need different density, refresh, and interactivity; most bad dashboards are three types mashed together.
2. **One question per widget.** Every chart must answer a question the viewer actually asks. Name it ("Is lag rising?") — if you can't, cut the widget.
3. **Hierarchy:** the single most important status goes top-left (LTR reading order, Few). Operational dashboards fit one screen without scrolling.
4. **Chart selection rules:** change over time → line; comparison across categories → bar (sorted, zero-baseline — mandatory for bars); part-of-whole → stacked bar (pie only if ≤3 slices); distribution → histogram; correlation → scatter. Single number + trend → stat tile with sparkline.
5. **Axis integrity:** bar charts start at zero, always. Line charts may truncate but label it. Same metric across widgets = same scale and color everywhere.
6. **Color:** max ~6 categorical series; sequential palettes for magnitude, diverging for above/below-target; never encode meaning in color alone (WCAG 1.4.1) — pair with labels/patterns.
7. **Numbers:** thousands separators, consistent decimals, tabular figures (`font-variant-numeric: tabular-nums`), explicit units and time ranges ("last 30 days", not ambiguous).
8. **Every widget needs 4 states:** loading (skeleton), empty ("no data yet" + why + action), error (retry, not blank), and data. Design them all.

## Anti-patterns to flag in review

Vanity metrics without a decision attached; everything-red alert fatigue (if half the dashboard is red, nothing is); pies with 7 slices; dual y-axes implying false correlation; truncated bar axes exaggerating differences; unlabeled time ranges; decorative gauges that waste space over a plain number.

- [ ] Dashboard type declared; density/refresh matches it
- [ ] Top-left = most important; one screen for operational
- [ ] Chart types follow the selection rules; bars zero-based
- [ ] ≤6 categorical colors; color never the sole encoding
- [ ] Loading/empty/error state per widget
- [ ] Every number has units and a time range
