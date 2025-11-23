---
category: data-analytics
last_updated: 2025-11-22
related_templates:
- data-analytics/Business-Intelligence/dashboard-strategy-requirements.md
- data-analytics/Business-Intelligence/dashboard-technical-implementation.md
- data-analytics/Business-Intelligence/dashboard-design-overview.md
tags:
- data-analytics
title: Dashboard UX/UI Design & User Experience
use_cases:
- Dashboard interface design
- Data visualization selection
- User experience optimization
industries:
- technology
type: template
difficulty: intermediate
slug: dashboard-ux-design
---

# Dashboard UX/UI Design & User Experience

## Overview
Design intuitive, visually compelling dashboards that enable effective decision-making. This prompt guides the creation of user-centered interfaces, appropriate visualizations, and engaging user experiences.

---

## Purpose
Use this prompt to:
- Design user-centered dashboard interfaces
- Select appropriate data visualizations
- Create effective visual hierarchy and navigation
- Optimize for usability and engagement

---

## Quick Start

**5-Minute Dashboard UX Design:**
1. **Define user personas and use cases** - Identify 2-3 primary users (e.g., Executive, Analyst) and their key questions
2. **Select visualization types** - Match data questions to chart types (trends → line charts, comparisons → bar charts, parts-of-whole → stacked bars)
3. **Create visual hierarchy** - Place KPIs at top, primary insights in upper left, supporting details below
4. **Design filter panel** - Add date range, 2-3 key filters visible, keep controls consistent across pages
5. **Test with real users** - Show mockups to 3 actual users, iterate based on feedback before development

**Key Decision:** Mobile vs. desktop-first? If executives use phones/tablets frequently, design for mobile screen sizes first (simplified charts, vertical layout).

---

## Prompt

I need to design a comprehensive UX/UI framework for a dashboard with the following requirements:

### User Context
- User personas: [USER_PERSONAS] (Executive/Manager/Analyst/Operational user)
- Primary use cases: [USE_CASES]
- Technical comfort level: [TECHNICAL_LEVEL] (Low/Medium/High)
- Device usage: [DEVICE_USAGE] (Desktop-only/Desktop-primary/Multi-device)
- Access frequency: [ACCESS_FREQUENCY] (Daily/Weekly/Ad-hoc)
- Session duration: [SESSION_DURATION] (Quick glance/Deep analysis)

### Visual Design Requirements
- Brand alignment: [BRAND_GUIDELINES] (Strict/Flexible/None)
- Color palette: [COLOR_PREFERENCES]
- Accessibility requirements: [ACCESSIBILITY] (WCAG 2.1 AA/AAA/None specified)
- Design style: [DESIGN_STYLE] (Minimal/Data-dense/Balanced)
- Screen sizes to support: [SCREEN_SIZES] (Desktop/Tablet/Mobile)

### Data Visualization Needs

**Comparison Analysis:**
- Compare values across categories: [COMPARISON_NEEDS]
- Preferred chart types: [COMPARISON_CHARTS] (Bar/Column/Bullet/Dot plot)

**Composition Analysis:**
- Show part-to-whole relationships: [COMPOSITION_NEEDS]
- Preferred chart types: [COMPOSITION_CHARTS] (Pie/Donut/Stacked bar/Treemap)

**Trend Analysis:**
- Track changes over time: [TEMPORAL_NEEDS]
- Preferred chart types: [TEMPORAL_CHARTS] (Line/Area/Sparkline/Timeline)

**Distribution Analysis:**
- Show data distribution: [DISTRIBUTION_NEEDS]
- Preferred chart types: [DISTRIBUTION_CHARTS] (Histogram/Box plot/Scatter/Heatmap)

**Geographic Analysis:**
- Location-based data: [GEOGRAPHIC_NEEDS]
- Preferred chart types: [GEOGRAPHIC_CHARTS] (Choropleth/Symbol map/Flow map)

**KPI Display:**
- Key metric cards: [KPI_DISPLAY_NEEDS]
- Trend indicators: [TREND_INDICATORS] (Arrows/Sparklines/Comparison values)

### Navigation & Interaction
- Navigation structure: [NAVIGATION_TYPE] (Top nav/Side nav/Tab-based/Mixed)
- Filter requirements: [FILTER_NEEDS] (Date range/Category/Geographic/Custom)
- Drill-down capabilities: [DRILLDOWN_NEEDS]
- Cross-filtering: [CROSS_FILTERING] (Yes/No)
- Export functionality: [EXPORT_NEEDS] (PDF/Excel/Image/None)
- Search functionality: [SEARCH_NEEDS]

### Layout & Information Hierarchy
- Dashboard size: [DASHBOARD_SIZE] (Single page/Multi-page/Scrollable)
- Widget count: [WIDGET_COUNT]
- Information density: [INFORMATION_DENSITY] (High/Medium/Low)
- Key focal point: [PRIMARY_FOCUS]
- Content priority: [CONTENT_PRIORITY] (Order by importance)

### Interactive Features
- Hover interactions: [HOVER_INTERACTIONS] (Tooltips/Highlights/Details)
- Click behaviors: [CLICK_BEHAVIORS] (Drill-down/Filter/Open detail/None)
- Real-time updates: [REALTIME_UPDATES] (Yes/No/Partial)
- Personalization: [PERSONALIZATION] (Custom layouts/Saved views/Themes)
- Annotations: [ANNOTATIONS] (User comments/System insights/None)

---

## Deliverables

Please provide:

1. **User Experience Design**
   - User journey maps for key personas
   - Information architecture
   - Wireframes for main dashboard views
   - Interaction patterns and behaviors

2. **Visual Design System**
   - Color palette (primary, secondary, accent, status colors)
   - Typography hierarchy
   - Icon library recommendations
   - Grid system and spacing rules
   - Component library specifications

3. **Data Visualization Guide**
   - Chart selection matrix for each data type
   - Visualization standards and best practices
   - Color coding system (status, categories, trends)
   - Label and annotation guidelines
   - Accessibility considerations

4. **Navigation & Layout Design**
   - Dashboard layout mockups
   - Navigation structure and menus
   - Filter panel design
   - Responsive design specifications
   - Mobile optimization approach

5. **Interactive Feature Specifications**
   - Drill-down navigation flows
   - Filter and cross-filtering behavior
   - Tooltip and hover state designs
   - Animation and transition guidelines
   - Loading and error states

---

## Example Usage

### Example: Executive Financial Dashboard

```
User personas: CFO, Finance Directors
Primary use cases: Monthly financial review, Quarterly board presentations
Technical comfort level: Medium
Device usage: Desktop-primary with mobile for key metrics
Access frequency: Daily for CFO, weekly for directors
Session duration: Quick glance (5 min) for daily, deep analysis (30 min) for monthly review

Brand alignment: Strict - must match corporate brand guidelines
Color palette: Corporate blue and gray with green/red for performance
Accessibility requirements: WCAG 2.1 AA compliance
Design style: Balanced - clean but data-rich
Screen sizes to support: Desktop (primary), tablet, mobile

Comparison needs: Revenue by region, product line comparison
Comparison charts: Horizontal bar charts for clear category comparison

Composition needs: Revenue breakdown by product, expense categories
Composition charts: Stacked bar for revenue mix, donut for expenses

Temporal needs: Revenue trend, Cash flow projection
Temporal charts: Line chart with forecast, dual-axis for multiple metrics

KPI display needs: 6 key metrics (Revenue, Profit, Cash, AR, AP, Runway)
Trend indicators: Month-over-month change with sparklines

Navigation structure: Top navigation with dropdowns (Overview/Revenue/Expenses/Cash)
Filter requirements: Date range, region, product line
Drill-down capabilities: Region → Country → Account
Cross-filtering: Yes - selections affect all charts
Export functionality: PDF for board presentations

Dashboard size: Single scrollable page
Widget count: 12-15 components
Information density: Medium-high
Primary focus: KPI cards at top, trend chart prominently displayed
Content priority: 1) KPIs, 2) Revenue trend, 3) Regional breakdown, 4) Details

Hover interactions: Detailed tooltips with variance explanations
Click behaviors: Drill-down on charts, filter on legend items
Real-time updates: No - data refreshes daily at 6 AM
Personalization: Saved filter presets, theme selection
Annotations: System-generated insights for anomalies
```

---

## Usage Examples

### Example 1: B2B SaaS Customer Success Dashboard

**Context:** Customer Success team needs visibility into account health and churn risk

**Copy-paste this prompt:**

```
I need to design a comprehensive UX/UI framework for a dashboard with the following requirements:

### User Context
- User personas: Customer Success Managers (8), VP Customer Success, Account Executives (for account handoff)
- Primary use cases: Daily account health monitoring, churn risk identification, QBR preparation
- Technical comfort level: Medium - comfortable with filters but not complex analytics
- Device usage: Desktop-primary with tablet for customer meetings
- Access frequency: CSMs check daily, VP checks weekly for team oversight
- Session duration: Quick glance (5 min) for daily checks, deep analysis (30 min) for QBR prep

### Visual Design Requirements
- Brand alignment: Flexible - follow general company colors (navy blue, teal accent)
- Color palette: Green/yellow/red for health scores, blue for neutral, gray for background
- Accessibility requirements: WCAG 2.1 AA compliance (team member with color vision deficiency)
- Design style: Balanced - show account health at a glance but allow drill-down
- Screen sizes to support: Desktop (primary), tablet (for customer meetings)

### Data Visualization Needs

**Comparison Analysis:**
- Compare values across categories: Account health scores by segment (Enterprise/Mid-Market/SMB), NRR by CSM
- Preferred chart types: Horizontal bar charts for CSM comparison, dot plot for benchmarking

**Composition Analysis:**
- Show part-to-whole relationships: Revenue by customer tier, support ticket categories
- Preferred chart types: Stacked bar for revenue mix, treemap for ticket breakdown

**Trend Analysis:**
- Track changes over time: Health score trends, usage patterns, NPS over time
- Preferred chart types: Line chart for health trends, area chart for usage patterns

**Distribution Analysis:**
- Show data distribution: Health score distribution across portfolio
- Preferred chart types: Histogram for health scores, scatter plot for health vs. revenue

**KPI Display:**
- Key metric cards: Total ARR at Risk, Accounts in Red, Renewal Rate, NPS, Expansion Pipeline
- Trend indicators: Month-over-month change with directional arrows, sparklines for 90-day trend

### Navigation & Interaction
- Navigation structure: Tab-based (Portfolio Overview | At-Risk Accounts | Renewals | My Accounts)
- Filter requirements: CSM, customer segment, renewal date range, health score threshold
- Drill-down capabilities: Portfolio → Segment → Account → Contact timeline
- Cross-filtering: Yes - clicking a segment filters all charts
- Export functionality: PDF for QBR decks, Excel for account lists
- Search functionality: Yes - search by account name or contact

### Layout & Information Hierarchy
- Dashboard size: Multi-page with 4 main tabs
- Widget count: 8-10 components per page
- Information density: Medium - clean but comprehensive
- Key focal point: Health score distribution and at-risk accounts
- Content priority: 1) At-risk alerts, 2) Portfolio health, 3) Renewals, 4) Individual metrics

### Interactive Features
- Hover interactions: Tooltips showing account details, last activity, key contacts
- Click behaviors: Drill-down to account detail, open Salesforce record
- Real-time updates: Partial - health scores update daily, alerts in real-time
- Personalization: Saved filters for "My Accounts", customizable alert thresholds
- Annotations: System insights for accounts with declining health

Please provide:
1. User journey map for CSM daily workflow
2. Visual design system with health score color coding
3. Chart selection for each data type (health, usage, sentiment)
4. Navigation structure with 4 main tabs
5. Mobile/tablet optimization for customer meeting use
```

**Expected Output:**
- CSM daily workflow: Alert review → At-risk triage → Account deep-dive → Action planning
- Health score visualization: Traffic light system (0-40 red, 41-70 yellow, 71-100 green)
- Tab structure with clear information architecture
- Responsive tablet layout for customer-facing presentations

---

### Example 2: E-commerce Operations Dashboard

**Context:** Operations team needs real-time visibility into order fulfillment and inventory

**Copy-paste this prompt:**

```
I need to design a comprehensive UX/UI framework for a dashboard with the following requirements:

### User Context
- User personas: Warehouse Manager, Fulfillment Leads (3), VP Operations
- Primary use cases: Real-time order monitoring, inventory alerts, shift performance tracking
- Technical comfort level: Low to Medium - need simple, actionable interface
- Device usage: Large wall-mounted displays in warehouse, desktop for managers, mobile for floor walks
- Access frequency: Continuous during operations (displayed on TVs), hourly checks by leads
- Session duration: Quick glance for real-time status, periodic deep dives for planning

### Visual Design Requirements
- Brand alignment: None - prioritize readability and quick scanning
- Color palette: High contrast for warehouse displays, green/yellow/red status indicators
- Accessibility requirements: Large fonts for wall displays, high contrast for bright warehouse
- Design style: Data-dense but scannable - critical for time-sensitive operations
- Screen sizes to support: Large display (4K TV), desktop, mobile

### Data Visualization Needs

**Comparison Analysis:**
- Compare values across categories: Orders by fulfillment status, inventory by warehouse zone
- Preferred chart types: Horizontal stacked bar for order status, column chart for zone comparison

**Trend Analysis:**
- Track changes over time: Orders per hour today vs. yesterday, SLA compliance trend
- Preferred chart types: Line chart with hour-by-hour comparison, area chart for cumulative orders

**KPI Display:**
- Key metric cards: Orders Pending, Orders Shipped, SLA %, Pick Rate, Inventory Alerts
- Trend indicators: Real-time count-up animation, red flash for SLA violations

### Navigation & Interaction
- Navigation structure: Single scrollable page for TV display, tabbed for desktop
- Filter requirements: Warehouse location, carrier, order type (standard/express/same-day)
- Drill-down capabilities: Status → Orders → Order detail
- Cross-filtering: Yes - click on status bar to filter order list
- Export functionality: PDF shift report, Excel order list

### Layout & Information Hierarchy
- Dashboard size: Single page for TV, multi-page for desktop
- Widget count: 6 large components for TV visibility
- Information density: Low for TV (large numbers), medium for desktop
- Key focal point: Orders pending + SLA status
- Content priority: 1) Real-time status, 2) SLA tracking, 3) Inventory alerts, 4) Shift metrics

### Interactive Features
- Hover interactions: None for TV, tooltips for desktop
- Click behaviors: TV = auto-cycle views, Desktop = drill-down
- Real-time updates: Yes - every 30 seconds for critical metrics
- Personalization: Different views by role (floor vs. manager)
- Annotations: Automatic alerts for inventory stockouts, SLA at risk

Please provide:
1. TV display layout optimized for 20-foot viewing distance
2. Color system for status indicators (green/yellow/red thresholds)
3. Real-time update strategy (which metrics update in real-time)
4. Alert design for critical situations (flashing, sound, etc.)
5. Desktop vs. TV layout differences
```

**Expected Output:**
- TV layout: 4-6 large KPI cards, minimal text, huge numbers
- Status thresholds: Green (>95% SLA), Yellow (90-95%), Red (<90%)
- Update frequency by metric type
- Alert escalation design (visual → audio → notification)

---

### Example 3: Healthcare Clinical Dashboard

**Context:** Hospital needs clinical quality dashboard for department heads and CMO

**Copy-paste this prompt:**

```
I need to design a comprehensive UX/UI framework for a dashboard with the following requirements:

### User Context
- User personas: CMO, Department Chiefs (6), Quality Officers (2), Nurse Managers
- Primary use cases: Clinical quality monitoring, regulatory compliance, patient safety metrics
- Technical comfort level: Low - physicians prefer simple, clean interfaces
- Device usage: Desktop in offices, tablet during rounds
- Access frequency: Daily for quality officers, weekly for leadership
- Session duration: 10-15 minutes for quality review, 5 minutes for quick status check

### Visual Design Requirements
- Brand alignment: Strict - hospital brand (blue, white, professional)
- Color palette: Muted professional colors, red only for critical safety alerts
- Accessibility requirements: WCAG 2.1 AA, high contrast for aging user base
- Design style: Minimal and clean - physicians won't use cluttered interfaces
- Screen sizes to support: Desktop (primary), tablet (iPad Pro for rounds)

### Data Visualization Needs

**Comparison Analysis:**
- Compare values across categories: Quality metrics by department, benchmark vs. actual
- Preferred chart types: Bullet charts for vs. benchmark, horizontal bar for department comparison

**Composition Analysis:**
- Show part-to-whole relationships: Patient mix by acuity, infection types
- Preferred chart types: Stacked bar (not pie) for clear comparison

**Trend Analysis:**
- Track changes over time: Infection rates, readmission trends, length of stay
- Preferred chart types: Line chart with control limits (SPC), sparklines for quick trends

**Distribution Analysis:**
- Show data distribution: Length of stay distribution, wait time histogram
- Preferred chart types: Box plot for LOS, histogram for wait times

**Geographic Analysis:**
- Location-based data: Floor-by-floor patient census, infection hotspots
- Preferred chart types: Floor plan heatmap, simple location markers

**KPI Display:**
- Key metric cards: HAI Rate, Readmission Rate, Mortality Index, Patient Satisfaction, ED Wait Time
- Trend indicators: Statistical control indicators (within control/above UCL/below LCL)

### Navigation & Interaction
- Navigation structure: Top navigation (Quality | Safety | Experience | Operations)
- Filter requirements: Department, date range, patient population, unit
- Drill-down capabilities: Hospital → Department → Unit → Metric detail
- Cross-filtering: Limited - filter by department only (HIPAA concerns)
- Export functionality: PDF for board reports, limited Excel (de-identified)
- Search functionality: Metric search only (no patient search on dashboard)

### Layout & Information Hierarchy
- Dashboard size: Single scrollable page per domain (Quality, Safety, etc.)
- Widget count: 8-10 components, well-spaced
- Information density: Low - white space is critical for busy clinicians
- Key focal point: Safety alerts and quality exceptions
- Content priority: 1) Safety alerts, 2) Regulatory metrics, 3) Trends, 4) Benchmarks

### Interactive Features
- Hover interactions: Metric definitions (clinicians need to verify methodology)
- Click behaviors: Drill to department detail, open methodology documentation
- Real-time updates: Daily refresh at 6 AM (near-real-time not needed for quality metrics)
- Personalization: Department-specific default views by user role
- Annotations: CMS star ratings, national benchmarks, control limits

Please provide:
1. Clinical dashboard design principles (minimal, trustworthy, actionable)
2. Statistical process control (SPC) chart design for quality metrics
3. Alert design for safety events (without alarm fatigue)
4. HIPAA-compliant drill-down strategy
5. Tablet layout for physician rounding
```

**Expected Output:**
- Clean, minimal design with ample white space
- SPC charts with UCL/LCL control limits
- Alert prioritization (critical/warning/informational)
- De-identified drill-down paths
- Touch-friendly tablet interface for rounds

---

## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Dashboard Strategy Requirements](dashboard-strategy-requirements.md)** - Strategic planning and execution frameworks
- **[Dashboard Technical Implementation](dashboard-technical-implementation.md)** - Complementary approaches and methodologies
- **[Dashboard Design Overview](dashboard-design-overview.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Dashboard UX/UI Design & User Experience)
2. Use [Dashboard Strategy Requirements](dashboard-strategy-requirements.md) for deeper analysis
3. Apply [Dashboard Technical Implementation](dashboard-technical-implementation.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Business Intelligence](../../data-analytics/Business Intelligence/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Dashboard interface design**: Combine this template with related analytics and strategy frameworks
- **Data visualization selection**: Combine this template with related analytics and strategy frameworks
- **User experience optimization**: Combine this template with related analytics and strategy frameworks

## Best Practices

### Visual Design
1. **Use color purposefully** - Limit palette to 3-5 colors plus neutral tones
2. **Maintain consistency** - Reuse colors, fonts, and patterns throughout
3. **Design for accessibility** - Ensure 4.5:1 contrast ratio minimum
4. **Respect white space** - Don't overcrowd the interface
5. **Establish clear hierarchy** - Guide user attention to key insights

### Data Visualization
6. **Choose the right chart** - Match visualization to data type and question
7. **Avoid pie charts for >5 categories** - Use bar charts instead
8. **Start axes at zero** - Avoid misleading visualizations
9. **Label directly** - Place labels near data instead of legends when possible
10. **Highlight insights** - Use annotations to point out key findings

### User Experience
11. **Design for scanning** - Users should grasp key insights in 5 seconds
12. **Minimize clicks** - Show important information immediately
13. **Provide context** - Include comparisons, targets, and trends
14. **Guide the narrative** - Arrange content to tell a story
15. **Test with real users** - Validate designs before full development

### Navigation & Interaction
16. **Keep filters visible** - Don't hide critical controls
17. **Indicate filter state** - Show what filters are active
18. **Provide breadcrumbs** - Help users navigate hierarchies
19. **Enable quick reset** - Allow users to clear all filters easily
20. **Show loading states** - Indicate when data is refreshing

---

## Chart Selection Guide

| Data Question | Best Chart Type | Avoid |
|---------------|----------------|--------|
| Compare categories | Bar chart | Pie chart (>5 items) |
| Show trends over time | Line chart | Bar chart |
| Part-to-whole | Stacked bar, Treemap | Multiple pie charts |
| Distribution | Histogram, Box plot | Bar chart |
| Correlation | Scatter plot | Line chart |
| Ranking | Horizontal bar | Column chart |
| Geographic | Choropleth map | Table |
| Single KPI | Big number + sparkline | Gauge chart |

---

## Common Mistakes to Avoid

- Using 3D charts (they distort data perception)
- Too many colors (stick to 5-7 max including neutrals)
- Unclear axis labels or missing units
- Legends far from data (use direct labels)
- Starting axes at non-zero values (except for variance)
- Unnecessary decoration or chart junk
- Poor color choices for colorblind users
- Overwhelming users with too many widgets
- Hidden or unclear navigation
- Inconsistent interaction patterns

---

## Variables Quick Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `[USER_PERSONAS]` | Primary users | "CFO, Finance managers" |
| `[USE_CASES]` | Main usage scenarios | "Monthly performance review" |
| `[TECHNICAL_LEVEL]` | User tech savviness | "Medium" |
| `[DEVICE_USAGE]` | Primary devices | "Desktop-primary" |
| `[COMPARISON_NEEDS]` | What to compare | "Revenue by region" |
| `[COMPARISON_CHARTS]` | Preferred charts | "Horizontal bar charts" |
| `[TEMPORAL_NEEDS]` | Time-based analysis | "12-month revenue trend" |
| `[TEMPORAL_CHARTS]` | Trend charts | "Line chart with forecast" |
| `[NAVIGATION_TYPE]` | Navigation style | "Top nav with dropdowns" |
| `[FILTER_NEEDS]` | Required filters | "Date range, region, product" |
| `[DRILLDOWN_NEEDS]` | Drill-down paths | "Region → Country → Account" |
| `[DASHBOARD_SIZE]` | Layout approach | "Single scrollable page" |
