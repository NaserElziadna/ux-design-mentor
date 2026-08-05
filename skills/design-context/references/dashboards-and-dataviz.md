# Dashboards & Data Visualization

Stephen Few defines a dashboard as "a visual display of the most important information needed to achieve one or more objectives, consolidated on a single screen so it can be monitored at a glance" (Information Dashboard Design). Most dashboard failures are not chart bugs — they are hierarchy failures: nobody decided what the one most important thing is. Design for the question the viewer brings, not for the data you happen to have.

## Dashboard Types

Match refresh rate and detail level to purpose (Few; Perceptual Edge):

- **Operational** — monitoring right now (server health, live orders). Refresh: seconds–minutes. Single screen, no scrolling, large status indicators, alert-driven.
- **Analytical** — exploring why (cohorts, funnels). Refresh: hourly–daily. Rich interaction: filters, comparisons, drill-down; scrolling acceptable.
- **Strategic** — executive KPIs vs targets. Refresh: weekly–monthly. Few numbers, trend + target context, minimal interaction, presentation-quality.

Mixing types is the classic failure: a live-refreshing executive dashboard, or an operational board buried under filters.

- [ ] Dashboard has a declared type and audience
- [ ] Refresh cadence matches decisions made from it

## The 5-Second Rule & Information Hierarchy

- A viewer should grasp overall status ("is anything wrong?") within ~5 seconds. If they must read to know, the hierarchy failed.
- **Top-left gets the most important KPI** in LTR locales — top-left and center carry the greatest visual emphasis (Few); mirror for RTL.
- Operational and strategic dashboards: one screen, no scrolling (Few). Scrolled-away information is unmonitored information.
- Group related metrics spatially; separate groups with whitespace, not boxes and rules.
- Show comparison context on every number: vs target, vs prior period, or trend sparkline. A lone "42,318" answers nothing.
- Limit to roughly 5–9 widgets per screen; beyond that, split into multiple purpose-specific dashboards.

- [ ] Most important KPI is top-left (LTR)
- [ ] Status readable in 5 seconds without interaction
- [ ] Every KPI has a comparison (target, delta, or trend)

## Chart Type Selection

Rules of thumb (Few, Show Me the Numbers; Datawrapper Academy):

- **Change over time** → line chart (or area for one cumulative series).
- **Comparison across categories** → horizontal bar chart (horizontal leaves room for labels); sort by value, not alphabetically, unless order is inherent.
- **Part-of-whole** → stacked bar or 100% stacked bar; prefer over pie because length is judged more accurately than angle.
- **Pie acceptable only when**: ≤3 slices, one clearly dominant, and the message is "roughly half/quarter." Never 3-D, never exploded, never two pies for comparison.
- **Distribution** → histogram or box plot.
- **Correlation** → scatter plot.
- **Single value + trend** → big number with sparkline, not a gauge (gauges waste space for one value — Few calls most gauges chartjunk).

- [ ] Chart type chosen by the question, not by novelty
- [ ] No pie charts with >3 slices; bars sorted meaningfully

## Axis Integrity

- **Bar/column charts must start at zero** — bars encode value as length; a truncated baseline makes a 3% difference look like 300% (Datawrapper: https://www.datawrapper.de/academy/why-our-column-and-bar-charts-start-at-zero).
- **Line charts need not start at zero** — lines encode by position/slope; zoom the range to show meaningful variation, but don't over-zoom noise into drama (Datawrapper line-chart guide).
- Never use dual y-axes with different scales to imply correlation; use two small charts instead.
- Keep identical y-scales across small multiples meant to be compared.
- Label axes with units; don't rely on the title.

## Data-Ink Ratio & Chartjunk (Tufte)

Tufte's principle: maximize the share of ink that encodes data; erase the rest (The Visual Display of Quantitative Information).

- Remove: backgrounds, heavy gridlines (use light gray, few), borders around charts, legends when direct labeling fits, redundant axis labels, all 3-D effects, gradients, drop shadows.
- Gridlines: 3–5 light ones beat 10 dark ones; often data labels replace them entirely.
- Sparklines (Tufte's invention) are ideal in KPI tiles and table rows — but only for series with enough points to show a shape (≥ ~10); a 3-point sparkline is noise ("sparkline abuse").

- [ ] No 3-D, gradients, or decorative imagery on charts
- [ ] Legends replaced with direct labels where possible

## Color in Data Visualization

- **Max ~6 categorical colors** per chart; beyond that, humans can't track the mapping — group the tail into "Other."
- **Sequential palette** (light→dark, one hue) for ordered magnitude; **diverging palette** (two hues through neutral midpoint) only when there's a meaningful midpoint (zero, target, average).
- **Never rely on color alone** — WCAG 1.4.1 Use of Color (https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html): pair color with labels, shapes, patterns, or position. Test palettes for deuteranopia (~8% of men have some color-vision deficiency); avoid red/green as the only status distinction.
- Use gray for context series and one saturated accent for the series that matters — color is emphasis, not decoration.
- Keep a color's meaning consistent across every widget on the dashboard (revenue is always the same blue).

- [ ] ≤6 categorical colors; consistent meaning across widgets
- [ ] Status conveyed by icon/label as well as color (WCAG 1.4.1)

## Number Formatting

- Thousands separators always: 1,234,567 — and abbreviate on dashboards: 1.2M, 45.3K.
- Consistent decimal places within a column/widget (98.5%, 7.0% — not 98.5% next to 7%).
- Precision matched to the decision: 2 decimals on conversion rates, 0 on user counts. False precision (12.847%) signals unreliability.
- Use **tabular (monospaced) figures** in tables and KPI tiles so digits align and don't jitter on live refresh (`font-variant-numeric: tabular-nums`).
- Right-align numbers in tables; show negative values with a minus sign or color+sign, never color alone.
- Show units once (in the header), not on every value.

## Widget States: Empty, Loading, Error

Every widget needs all three, independently:

- **Loading**: skeleton in the widget's final shape (prevents layout shift); never spin the whole dashboard for one slow query.
- **Empty**: "No data for this filter/date range" plus the fix (widen range, clear filter) — distinct from zero, which is real data and must render as a chart showing zero.
- **Error**: per-widget error with retry; one failed widget must not blank the page. Show data timestamp so users know staleness.

- [ ] One widget's failure never breaks the dashboard
- [ ] "No data," "zero," and "error" render distinctly

## Drill-Down & Real-Time Labeling

- Pattern: overview → filter/highlight → detail on demand (Shneiderman's mantra). Clicking a KPI tile or chart segment should open the underlying detail (filtered table or dedicated view).
- Preserve breadcrumbs/back state so users can return to the overview without losing filters; encode dashboard state in the URL for sharing.
- **Label data recency explicitly**: "Live," "Updated 3 min ago," or "As of Aug 4" on every dashboard — mixing real-time and nightly-batch widgets without labels causes users to reconcile numbers that can never match.

## Dashboard Anti-Patterns

- **Vanity metrics**: cumulative "total signups ever" always goes up and informs nothing; show actionable rates and deltas instead.
- **Everything-is-red alert fatigue**: if a third of the dashboard is red, nothing is urgent. Reserve alert color for states requiring action now; use calibrated thresholds, and prefer "top N problems" over coloring every metric.
- **Sparkline abuse**: sparklines on data with too few points, or where the trend doesn't matter, add ink without information.
- **The wall of gauges**: gauges/donuts repeating one number each — replace with a compact bullet-graph or table (Few).
- **Filter overload on operational boards**: monitoring dashboards should need zero configuration to answer their core question.
- **Data dump**: showing every available metric because it exists. Start from the 3 decisions the viewer makes, work backward.

- [ ] Alert color appears only on actionable exceptions
- [ ] Every widget traces to a decision someone actually makes

## Sources

- https://www.perceptualedge.com/files/Dashboard_Design_Course.pdf
- https://www.amazon.com/Information-Dashboard-Design-At-Glance/dp/1938377001
- https://www.datawrapper.de/academy/why-our-column-and-bar-charts-start-at-zero
- https://www.datawrapper.de/academy/what-to-consider-when-creating-line-charts
- https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html
- https://www.biztory.com/blog/2016/04/06/information-dashboard-design-lessons-learned
- https://blogs.sap.com/2011/04/14/a-few-dashboard-design-principles/
- Edward Tufte, The Visual Display of Quantitative Information (data-ink ratio, sparklines)
- Stephen Few, Show Me the Numbers / Information Dashboard Design
