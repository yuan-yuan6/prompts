---
category: product-management
last_updated: 2025-11-12
title: Product Metrics & KPIs Framework
tags:
- product-management
- analytics
- metrics
- kpis
use_cases:
- Defining key product metrics and KPIs for measuring success
- Building metric frameworks aligned with business objectives
- Tracking product health and user engagement
- Creating data-driven product decision frameworks
related_templates:
- product-management/Product-Analytics/product-analytics-framework.md
- product-management/Product-Analytics/user-behavior-analysis.md
- product-management/Product-Analytics/ab-testing-experimentation.md
- product-management/Product-Strategy/product-strategy-vision.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: template
difficulty: intermediate
slug: product-metrics-kpis
---

# Product Metrics & KPIs Framework Template

## Purpose
Define comprehensive product metrics and KPIs that measure product success, guide decision-making, align teams on goals, and provide visibility into product health and business impact.

## Quick Metrics Prompt
Define metrics framework for [product] with [business model: SaaS/marketplace/e-commerce]. North Star metric: [primary value indicator]. Map AARRR metrics: Acquisition (source), Activation (aha moment), Retention (D1/D7/D30), Revenue (LTV, ARPU), Referral (viral coefficient). Set targets for each with rationale. Include: leading vs. lagging indicators, metric hierarchy, dashboard design, and weekly/monthly review cadence.

## Quick Start

**Need metrics quickly?** Use this streamlined approach:

### Minimal Example
```
Product: SaaS project management tool
North Star: Weekly Active Teams collaborating on projects
Key Metrics:
- Acquisition: New signups (target: 1,000/week)
- Activation: Teams that create first project (target: 60%)
- Engagement: DAU/MAU ratio (target: 40%)
- Retention: Week 4 retention (target: 50%)
- Revenue: MRR growth (target: 20% month-over-month)
- Referral: Viral coefficient (target: 0.4)
```

### When to Use This
- Launching new products or features
- Establishing measurement framework for existing products
- Aligning teams on success criteria
- Building analytics infrastructure
- Board/investor reporting requirements

### Basic 4-Step Workflow
1. **Define North Star metric** - Single metric capturing core value (1 day)
2. **Map key metrics** - AARRR framework or custom hierarchy (2-3 days)
3. **Set targets & instrumentation** - Goals and tracking setup (1 week)
4. **Dashboard & reviews** - Create dashboards, establish review cadence (1 week)

---

## Template

```
You are an experienced product analytics leader. Define a comprehensive metrics framework for [PRODUCT_NAME] serving [TARGET_USERS] with [BUSINESS_MODEL] to measure [SUCCESS_CRITERIA] and drive [BUSINESS_OBJECTIVES].

METRICS CONTEXT:
Product Information:
- Product name: [PRODUCT_NAME]
- Product type: [B2B_SAAS/CONSUMER_APP/MARKETPLACE/PLATFORM]
- Business model: [SUBSCRIPTION/FREEMIUM/TRANSACTION/ADVERTISING]
- Stage: [EARLY/GROWTH/MATURE]
- Current scale: [USERS/CUSTOMERS/REVENUE]

Strategic Objectives:
- Primary objective: [MAIN_BUSINESS_GOAL]
- Success definition: [WHAT_SUCCESS_LOOKS_LIKE]
- Time horizon: [MEASUREMENT_PERIOD]
- Decision needs: [WHAT_METRICS_WILL_INFORM]

### 1. NORTH STAR METRIC

North Star Definition:
Metric: [PRIMARY_METRIC]
- Why this metric: [RATIONALE]
- What it measures: [WHAT_IT_REPRESENTS]
- Why it matters: [BUSINESS_IMPACT]
- Leading or lagging: [TYPE_AND_WHY]

Example:
"Weekly Active Teams creating projects"
- Why: Measures real value delivery, not just usage
- What: Teams actively collaborating on work
- Matters: Predicts retention and revenue
- Leading: Predicts long-term retention and expansion

North Star Components:
Value delivered: [WHAT_VALUE_USERS_GET]
Business outcome: [WHAT_BUSINESS_GETS]
Alignment: [HOW_USER_AND_BUSINESS_WIN_TOGETHER]

Current State:
- Current value: [BASELINE]
- Historical trend: [TREND_OVER_TIME]
- Segment breakdown: [HOW_IT_VARIES]
- Target: [GOAL_VALUE]
- Timeline: [WHEN_TO_ACHIEVE]

Inputs to North Star:
Input Metric 1: [METRIC_NAME]
- Contribution: [HOW_IT_AFFECTS_NORTH_STAR]
- Current value: [BASELINE]
- Improvement opportunity: [POTENTIAL]

Input Metric 2: [METRIC_NAME]
(Same structure)

Input Metric 3: [METRIC_NAME]
(Same structure)

### 2. PIRATE METRICS (AARRR) FRAMEWORK

Acquisition Metrics:
Definition: How users find and sign up for your product

Primary Metrics:
- New signups: [NUMBER_PER_PERIOD]
  - Target: [GOAL]
  - Trend: [DIRECTION]
  - Segment view: [BREAKDOWN]

- Traffic to signup conversion: [PERCENTAGE]
  - Target: [GOAL]
  - Current funnel: [STEPS_AND_CONVERSION]

- Customer Acquisition Cost (CAC): [COST]
  - Target: [GOAL]
  - By channel: [BREAKDOWN]

- Traffic sources: [CHANNELS]
  - Organic: [%]
  - Paid: [%]
  - Referral: [%]
  - Direct: [%]

Activation Metrics:
Definition: Users experiencing core value for first time

Primary Metrics:
- Activation rate: [PERCENTAGE]
  - Definition: [WHAT_COUNTS_AS_ACTIVATED]
  - Target: [GOAL]
  - Time to activation: [DURATION]

- "Aha moment" completion: [PERCENTAGE]
  - Aha moment defined: [KEY_VALUE_ACTION]
  - Target: [GOAL]

- Onboarding completion: [PERCENTAGE]
  - Steps: [ONBOARDING_FLOW]
  - Drop-off points: [WHERE_USERS_LEAVE]
  - Target: [GOAL]

- Time to first value: [DURATION]
  - Target: [GOAL]
  - Variance: [DISTRIBUTION]

Retention Metrics:
Definition: Users continuing to use product over time

Primary Metrics:
- Day 1 retention: [PERCENTAGE]
- Day 7 retention: [PERCENTAGE]
- Day 30 retention: [PERCENTAGE]
- Cohort retention curves: [VISUALIZATION]

- Monthly Active Users (MAU): [COUNT]
  - Target: [GOAL]
  - Growth rate: [PERCENTAGE]

- Daily Active Users (DAU): [COUNT]
  - Target: [GOAL]

- DAU/MAU ratio (stickiness): [RATIO]
  - Target: [GOAL]
  - Industry benchmark: [COMPARISON]

- Churn rate: [PERCENTAGE]
  - Voluntary: [%]
  - Involuntary: [%]
  - Target: [GOAL]

- Net Revenue Retention (NRR): [PERCENTAGE]
  - Target: [GOAL]
  - Components: [EXPANSION_MINUS_CHURN]

Engagement Metrics:
- Session frequency: [SESSIONS_PER_USER_PER_PERIOD]
  - Target: [GOAL]

- Session duration: [AVERAGE_TIME]
  - Target: [GOAL]

- Feature adoption: [PERCENTAGE_USING_KEY_FEATURES]
  - Feature 1: [%]
  - Feature 2: [%]
  - Feature 3: [%]

- Depth of usage: [ACTIONS_PER_SESSION]
  - Target: [GOAL]

Revenue Metrics:
Definition: Monetization and financial performance

Primary Metrics:
- Monthly Recurring Revenue (MRR): [AMOUNT]
  - Target: [GOAL]
  - Growth rate: [PERCENTAGE]
  - Composition: [NEW/EXPANSION/CHURN]

- Annual Recurring Revenue (ARR): [AMOUNT]
  - Target: [GOAL]

- Average Revenue Per User (ARPU): [AMOUNT]
  - Target: [GOAL]
  - By segment: [BREAKDOWN]

- Customer Lifetime Value (LTV): [AMOUNT]
  - Calculation: [METHOD]
  - Target: [GOAL]
  - LTV:CAC ratio: [RATIO]

- Gross Margin: [PERCENTAGE]
  - Target: [GOAL]
  - Unit economics: [PROFITABILITY]

- Conversion to paid: [PERCENTAGE]
  - Free to paid: [%]
  - Trial to paid: [%]
  - Target: [GOAL]

Referral Metrics:
Definition: Users bringing in new users

Primary Metrics:
- Net Promoter Score (NPS): [SCORE]
  - Target: [GOAL]
  - Trend: [DIRECTION]
  - Segment breakdown: [VARIATION]

- Viral coefficient: [K-FACTOR]
  - Target: [>1_FOR_VIRAL_GROWTH]
  - Calculation: [INVITES × CONVERSION]

- Referral rate: [PERCENTAGE]
  - Users who refer: [%]
  - Successful referrals: [%]

- Word of mouth attribution: [PERCENTAGE_OF_SIGNUPS]
  - Target: [GOAL]

### 3. PRODUCT HEALTH METRICS

Quality Metrics:
- Error rate: [PERCENTAGE]
  - Target: [<THRESHOLD]
  - Critical errors: [COUNT]

- Crash rate: [PERCENTAGE]
  - Target: [<THRESHOLD]
  - By platform: [BREAKDOWN]

- API uptime: [PERCENTAGE]
  - Target: [>99.9%]
  - Incidents: [COUNT]

- Performance (load time): [SECONDS]
  - Target: [<THRESHOLD]
  - P50/P95/P99: [DISTRIBUTION]

- Bug backlog: [COUNT]
  - By severity: [P0/P1/P2/P3]
  - Age: [TREND]

User Satisfaction Metrics:
- Customer Satisfaction (CSAT): [SCORE]
  - Target: [GOAL]
  - Survey method: [APPROACH]

- Net Promoter Score (NPS): [SCORE]
  - Promoters: [%]
  - Passives: [%]
  - Detractors: [%]

- Product-Market Fit Score: [PERCENTAGE]
  - "Very disappointed" if product went away
  - Target: [>40%]

- App store rating: [STARS]
  - Target: [GOAL]
  - Review sentiment: [POSITIVE/NEGATIVE_%]

Support Metrics:
- Support tickets: [VOLUME]
  - By type: [BREAKDOWN]
  - Trend: [DIRECTION]

- First response time: [HOURS]
  - Target: [SLA]

- Time to resolution: [HOURS]
  - Target: [SLA]

- Support satisfaction: [SCORE]
  - Target: [GOAL]

### 4. BUSINESS IMPACT METRICS

Growth Metrics:
- User growth rate: [PERCENTAGE]
  - Week-over-week: [%]
  - Month-over-month: [%]
  - Year-over-year: [%]

- Revenue growth rate: [PERCENTAGE]
  - Month-over-month: [%]
  - Year-over-year: [%]

- Market share: [PERCENTAGE]
  - Trend: [DIRECTION]
  - vs competitors: [COMPARISON]

Efficiency Metrics:
- Customer Acquisition Cost (CAC): [AMOUNT]
  - By channel: [BREAKDOWN]
  - Target: [GOAL]
  - Trend: [DIRECTION]

- CAC payback period: [MONTHS]
  - Target: [<12_MONTHS]
  - By segment: [BREAKDOWN]

- LTV:CAC ratio: [RATIO]
  - Target: [>3:1]
  - Healthy range: [3-5:1]

- Sales efficiency (Magic Number): [RATIO]
  - Calculation: [NET_NEW_ARR / SALES_MARKETING_SPEND]
  - Target: [>0.75]

Retention Economics:
- Gross Revenue Retention (GRR): [PERCENTAGE]
  - Target: [>90%]

- Net Revenue Retention (NRR): [PERCENTAGE]
  - Target: [>110%]

- Logo retention: [PERCENTAGE]
  - Target: [GOAL]

- Expansion revenue: [AMOUNT]
  - Upsell: [AMOUNT]
  - Cross-sell: [AMOUNT]

### 5. SEGMENTATION METRICS

User Segments:
Segment 1: [SEGMENT_NAME]
- Definition: [CRITERIA]
- Size: [USERS_OR_PERCENTAGE]
- Key metrics:
  - Activation: [%]
  - Retention: [%]
  - ARPU: [AMOUNT]
  - NPS: [SCORE]

Segment 2: [SEGMENT_NAME]
(Same structure)

Segment 3: [SEGMENT_NAME]
(Same structure)

Cohort Analysis:
Cohort: [COHORT_DEFINITION]
- Cohort date: [TIME_PERIOD]
- Size: [USERS]
- Retention curve: [VISUALIZATION]
- Revenue curve: [VISUALIZATION]
- Insights: [LEARNINGS]

Behavioral Segments:
- Power users: [DEFINITION]
  - Size: [%]
  - Characteristics: [BEHAVIORS]
  - Value: [LTV_OR_IMPACT]

- At-risk users: [DEFINITION]
  - Size: [%]
  - Warning signals: [INDICATORS]
  - Intervention: [STRATEGY]

- Dormant users: [DEFINITION]
  - Size: [%]
  - Reactivation opportunity: [POTENTIAL]

### 6. FEATURE-SPECIFIC METRICS

Feature: [FEATURE_NAME]
Adoption Metrics:
- Users exposed: [COUNT]
- Users activated: [COUNT]
- Adoption rate: [PERCENTAGE]
- Target: [GOAL]

Engagement Metrics:
- Usage frequency: [TIMES_PER_USER]
- Depth of use: [ACTIONS_PER_SESSION]
- Retention: [%_STILL_USING_AFTER_30_DAYS]

Impact Metrics:
- Impact on North Star: [CORRELATION]
- Impact on retention: [UPLIFT]
- Impact on revenue: [CONTRIBUTION]

Feature: [FEATURE_NAME]
(Same structure)

### 7. LEADING vs LAGGING INDICATORS

Leading Indicators:
Indicator 1: [METRIC]
- Why it's leading: [PREDICTS_WHAT]
- Current value: [BASELINE]
- Target: [GOAL]
- Response time: [HOW_QUICKLY_ACTIONABLE]

Example:
"Activation rate (Day 1)"
- Predicts: 30-day retention and LTV
- Current: 45%
- Target: 60%
- Response: Can intervene in onboarding immediately

Indicator 2: [METRIC]
(Same structure)

Indicator 3: [METRIC]
(Same structure)

Lagging Indicators:
Indicator 1: [METRIC]
- What it measures: [OUTCOME]
- Influenced by: [LEADING_METRICS]
- Current value: [BASELINE]
- Target: [GOAL]

Example:
"Monthly Recurring Revenue (MRR)"
- Measures: Revenue outcome
- Influenced by: Signups, activation, conversion, retention, expansion
- Current: $500K
- Target: $1M

### 8. METRIC TARGETS & GOALS

Goal-Setting Framework:
Metric: [METRIC_NAME]
- Current baseline: [VALUE]
- Historical growth rate: [TREND]
- Target: [GOAL_VALUE]
- Timeline: [TIMEFRAME]
- Rationale: [WHY_THIS_TARGET]
- Stretch goal: [AMBITIOUS_TARGET]

Realistic Range:
- Baseline scenario: [CONSERVATIVE_ESTIMATE]
- Target scenario: [EXPECTED_OUTCOME]
- Optimistic scenario: [BEST_CASE]

OKR Framework:
Objective: [GOAL_STATEMENT]

Key Result 1: [MEASURABLE_OUTCOME]
- Metric: [SPECIFIC_METRIC]
- Starting value: [BASELINE]
- Target value: [GOAL]
- Current progress: [STATUS]

Key Result 2: [MEASURABLE_OUTCOME]
(Same structure)

Key Result 3: [MEASURABLE_OUTCOME]
(Same structure)

### 9. DASHBOARDS & REPORTING

Executive Dashboard:
Purpose: High-level business health
Audience: Executives, board
Frequency: Weekly review, monthly deep dive

Key Metrics:
- North Star: [METRIC] - [TREND]
- Revenue: [MRR/ARR] - [GROWTH_%]
- Users: [MAU] - [GROWTH_%]
- Retention: [NRR] - [vs_TARGET]
- Unit economics: [LTV:CAC] - [RATIO]

Visualization: [DASHBOARD_STRUCTURE]

Product Team Dashboard:
Purpose: Product health and feature performance
Audience: Product, design, engineering
Frequency: Daily monitoring, weekly review

Key Metrics:
- Activation: [%]
- Engagement: [DAU/MAU]
- Feature adoption: [TOP_FEATURES_%]
- Quality: [ERROR_RATE/CRASH_RATE]
- User feedback: [NPS/CSAT]

Growth Dashboard:
Purpose: Acquisition and conversion optimization
Audience: Marketing, growth team
Frequency: Daily monitoring

Key Metrics:
- Traffic: [VISITORS]
- Signups: [NEW_USERS]
- Conversion rates: [FUNNEL_%]
- CAC: [BY_CHANNEL]
- Activation: [%]

Customer Success Dashboard:
Purpose: Retention and expansion
Audience: CS team, account managers
Frequency: Weekly monitoring

Key Metrics:
- Customer health scores: [DISTRIBUTION]
- Churn risk: [AT_RISK_COUNT]
- Usage trends: [ENGAGEMENT]
- NRR: [%]
- Expansion opportunities: [PIPELINE]

### 10. METRIC REVIEW CADENCE

Daily Reviews:
Focus: Operational metrics
- System health: [UPTIME/ERRORS]
- User activity: [DAU]
- Revenue: [DAILY_REVENUE]
- Anomalies: [ALERTS]

Actions: Quick response to issues

Weekly Reviews:
Focus: Tactical metrics
- Weekly actives: [WAU]
- Conversion funnels: [%]
- Feature launches: [ADOPTION]
- Support trends: [TICKET_VOLUME]

Actions: Tactical adjustments

Monthly Reviews:
Focus: Strategic metrics
- Monthly actives: [MAU]
- Revenue: [MRR]
- Retention cohorts: [ANALYSIS]
- OKR progress: [% TO GOAL]
- Competitive benchmarks: [COMPARISON]

Actions: Strategy refinement

Quarterly Reviews:
Focus: Business outcomes
- OKR achievement: [RESULTS]
- Strategy effectiveness: [ASSESSMENT]
- Metric framework review: [UPDATES_NEEDED]
- Target adjustments: [RECALIBRATION]

Actions: Strategic pivots if needed

### 11. INSTRUMENTATION PLAN

Event Tracking:
Event: [EVENT_NAME]
- Trigger: [WHEN_IT_FIRES]
- Properties: [DATA_CAPTURED]
  - Property 1: [NAME] - [TYPE] - [EXAMPLE]
  - Property 2: [NAME] - [TYPE] - [EXAMPLE]
- Purpose: [WHY_WE_TRACK_THIS]
- Used in metrics: [WHICH_METRICS]

Example:
"Project Created"
- Trigger: User creates new project
- Properties:
  - user_id: string - "user_12345"
  - project_type: string - "marketing_campaign"
  - team_size: integer - 5
  - template_used: boolean - true
- Purpose: Measure activation and feature adoption
- Metrics: Activation rate, North Star (active teams), feature adoption

Implementation:
- Analytics platform: [MIXPANEL/AMPLITUDE/SEGMENT]
- Tag management: [GTM/TEALIUM]
- Backend tracking: [APPROACH]
- Mobile tracking: [SDK]
- Data warehouse: [BIGQUERY/SNOWFLAKE]

Data Quality:
- Validation rules: [CHECKS]
- QA process: [HOW_VERIFY_ACCURACY]
- Ownership: [WHO_MAINTAINS]
- Documentation: [WHERE_SPEC_LIVES]

### 12. BENCHMARKS & TARGETS

Industry Benchmarks:
Metric: [METRIC_NAME]
- Our performance: [VALUE]
- Industry average: [VALUE]
- Top quartile: [VALUE]
- Source: [WHERE_BENCHMARK_FROM]

Internal Benchmarks:
Metric: [METRIC_NAME]
- Current performance: [VALUE]
- 3-month ago: [VALUE]
- 6-month ago: [VALUE]
- Year ago: [VALUE]
- Trend: [DIRECTION_AND_RATE]

Competitive Benchmarks:
- vs [COMPETITOR_1]: [COMPARISON]
- vs [COMPETITOR_2]: [COMPARISON]
- Our position: [RELATIVE_STANDING]
```

## Variables

### PRODUCT_NAME
Your product.
**Examples:**
- "Enterprise CRM Platform"
- "Personal Finance Mobile App"
- "B2B SaaS Analytics Tool"

### TARGET_USERS
Who uses your product.
**Examples:**
- "Sales teams at mid-market companies"
- "Individual consumers managing personal finances"
- "Data analysts at enterprise companies"

### BUSINESS_MODEL
How you make money.
**Examples:**
- "Subscription SaaS ($99/user/month)"
- "Freemium with premium features ($9.99/month)"
- "Marketplace with transaction fees (15% take rate)"

### SUCCESS_CRITERIA
What success looks like.
**Examples:**
- "Grow MRR 20% month-over-month sustainably"
- "Achieve 40% DAU/MAU stickiness"
- "Reach $10M ARR with >100% NRR"

### BUSINESS_OBJECTIVES
What the business needs to achieve.
**Examples:**
- "Raise Series B funding with strong growth metrics"
- "Achieve profitability with positive unit economics"
- "Expand to enterprise segment with high retention"

## Usage Examples

### Example 1: B2B SaaS Metrics Framework
```
Product: Team collaboration platform
North Star: Weekly Active Teams running standups
AARRR:
- Acquisition: 2,000 signups/week, $50 CAC
- Activation: 65% create first standup within 48 hours
- Retention: 55% Week 4, 90% MRR retention
- Revenue: $800K MRR, 3.5:1 LTV:CAC, $45 ARPU
- Referral: NPS 45, 0.3 viral coefficient
Targets: $2M MRR by year end, 70% activation, 95% NRR
```

### Example 2: Consumer Mobile App Metrics
```
Product: Fitness tracking app
North Star: Weekly workout sessions logged
AARRR:
- Acquisition: 50K downloads/week, 40% organic
- Activation: 50% log first workout within 24 hours
- Retention: Day 7: 35%, Day 30: 18%, DAU/MAU: 25%
- Revenue: 8% free→paid conversion, $4.99/month, $15 LTV
- Referral: NPS 55, 12% share workouts socially
Targets: 1M active users, 25% retention, 12% conversion
```

### Example 3: Marketplace Metrics
```
Product: Freelance services marketplace
North Star: Successful project completions per week
Supply: 10K active freelancers, 60% fill rate
Demand: 5K active clients, 3 projects posted/week average
Liquidity: 48-hour average match time
Economics: 20% take rate, $250 average project value
Retention: 40% client repeat rate, 70% freelancer retention
Targets: 2,000 completions/week, <24hr match time
```

### Example 4: Freemium SaaS Metrics
```
Product: Email marketing platform
North Star: Emails sent by paying customers
Funnel:
- Free signups: 10K/month
- Activated (sent campaign): 40%
- Convert to paid: 10%
- Retained (Month 3): 85%
Economics: $49/month, $588 LTV, $150 CAC, 3.9:1 ratio
Targets: 15% conversion, $1M MRR, 90% retention
```

## Best Practices

### Metric Selection
1. **Start with North Star** - One metric that captures core value
2. **Limit to essentials** - 5-7 key metrics per team, not 50
3. **Leading indicators** - Metrics you can influence, not just outcomes
4. **Aligned to strategy** - Metrics drive behavior toward goals
5. **User and business** - Balance what's good for users and business

### Target Setting
1. **Baseline first** - Know where you are before setting targets
2. **Realistic but ambitious** - Stretch goals that are achievable
3. **Time-bound** - Specific timeline for achievement
4. **Segment-specific** - Different targets for different cohorts
5. **Revisit quarterly** - Adjust based on learnings

### Instrumentation
1. **Track early** - Instrument before you need the data
2. **Consistent naming** - Standard event and property names
3. **Rich context** - Capture properties that enable segmentation
4. **QA tracking** - Verify accuracy before relying on data
5. **Document everything** - Tracking plan that everyone references

### Dashboards
1. **Audience-specific** - Different dashboards for different teams
2. **Hierarchy** - Summary to detail, easy to drill down
3. **Real-time where needed** - Daily for operational, weekly for strategic
4. **Accessible** - Everyone can see relevant metrics
5. **Actionable** - Metrics lead to decisions and actions

### Analysis
1. **Segmentation** - Always look at segments, not just aggregates
2. **Trends over snapshots** - Direction matters more than point-in-time
3. **Correlation and causation** - Test hypotheses with experiments
4. **Context** - External factors affecting metrics
5. **Story behind numbers** - Metrics tell a story, understand it

## Common Pitfalls

❌ **Vanity metrics** - Tracking impressive but meaningless numbers
✅ Instead: Focus on metrics that predict business outcomes

❌ **Too many metrics** - Tracking everything, optimizing nothing
✅ Instead: 5-7 key metrics that drive decisions

❌ **Lagging indicators only** - Waiting until it's too late to act
✅ Instead: Balance leading (predictive) and lagging (outcome) metrics

❌ **Aggregate metrics** - Overall averages hide important segments
✅ Instead: Always segment by user type, cohort, behavior

❌ **Metric without context** - Numbers without targets or trends
✅ Instead: Show baseline, target, trend, and comparison

❌ **Set and forget** - Tracking metrics but not reviewing regularly
✅ Instead: Established review cadence with clear ownership

❌ **Instrumentation debt** - Inconsistent or inaccurate tracking
✅ Instead: Treat tracking like code - reviewed, documented, maintained

❌ **No action from insights** - Dashboards that inform but don't drive decisions
✅ Instead: Every metric review should lead to actions or experiments

## Metrics Framework Checklist

Initial Setup:
- [ ] North Star metric defined and measured
- [ ] AARRR framework populated with current values
- [ ] Targets set for each key metric
- [ ] Instrumentation plan documented
- [ ] Analytics tools selected and implemented
- [ ] Dashboards created for each audience
- [ ] Baseline metrics captured

Ongoing Management:
- [ ] Daily monitoring of operational metrics
- [ ] Weekly review of tactical metrics
- [ ] Monthly deep dive on strategic metrics
- [ ] Quarterly OKR review and target adjustment
- [ ] Regular data quality audits
- [ ] Metric framework evolves with product
- [ ] Team trained on metric definitions

---

**Last Updated:** 2025-11-12
**Category:** Product Management > Product Analytics
**Difficulty:** Intermediate to Advanced
**Estimated Time:** 2-3 weeks for initial framework; ongoing refinement
