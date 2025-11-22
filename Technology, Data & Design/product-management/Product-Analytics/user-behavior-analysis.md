---
category: product-management/Product-Analytics
last_updated: 2025-11-12
title: User Behavior Analysis
tags:
- product-management
- analytics
- user-behavior
- data-analysis
use_cases:
- Analyzing user behavior patterns to inform product decisions
- Identifying friction points and drop-off in user journeys
- Segmenting users based on behavior for targeted improvements
- Understanding feature adoption and usage patterns
related_templates:
- product-management/Product-Analytics/product-metrics-kpis.md
- product-management/Product-Analytics/ab-testing-experimentation.md
- product-management/Product-Development/user-research-personas.md
- product-management/Product-Analytics/product-analytics-framework.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: template
difficulty: intermediate
slug: user-behavior-analysis
---

# User Behavior Analysis Template

## Purpose
Systematically analyze user behavior to uncover insights about how users interact with your product, identify opportunities for improvement, understand what drives engagement and retention, and make data-informed product decisions.

## Quick Start

**Need quick behavioral insights?** Use this streamlined approach:

### Minimal Example
```
Question: Why do users abandon checkout?
Analysis: Funnel analysis of checkout flow
Finding: 45% drop-off at shipping page (when costs revealed)
Segments: Price-sensitive users drop at 2x rate vs others
Action: Show shipping costs earlier + offer free shipping threshold
Impact: 15% improvement in checkout completion
```

### When to Use This
- Investigating product usage drop-offs or churn
- Understanding feature adoption patterns
- Identifying power user behaviors to replicate
- Optimizing conversion funnels
- Validating product hypotheses with data

### Basic 4-Step Workflow
1. **Define question** - What you want to understand about user behavior (1 day)
2. **Collect & analyze data** - Gather behavioral data and identify patterns (3-5 days)
3. **Segment analysis** - Break down by user types to find differences (2-3 days)
4. **Insights & actions** - Translate findings into product improvements (2 days)

---

## Template

```
You are an experienced product data analyst. Conduct comprehensive user behavior analysis for [PRODUCT_NAME] to answer [RESEARCH_QUESTION] using [DATA_SOURCES] to inform [PRODUCT_DECISIONS] and improve [TARGET_METRICS].

ANALYSIS CONTEXT:
Product Information:
- Product name: [PRODUCT_NAME]
- Analysis focus: [FEATURE/FLOW/OVERALL_PRODUCT]
- Time period: [DATE_RANGE]
- User base size: [TOTAL_USERS]

Research Objective:
- Primary question: [WHAT_YOU_WANT_TO_UNDERSTAND]
- Why it matters: [BUSINESS_IMPACT]
- Decision to inform: [WHAT_THIS_WILL_ENABLE]
- Success criteria: [WHAT_GOOD_ANALYSIS_LOOKS_LIKE]

### 1. ANALYSIS FRAMEWORK

Research Questions:
Primary Question: [MAIN_QUESTION]
- Why we're asking: [RATIONALE]
- Expected insights: [WHAT_WE_HOPE_TO_LEARN]

Supporting Questions:
1. [QUESTION_1]
2. [QUESTION_2]
3. [QUESTION_3]

Hypotheses:
- Hypothesis 1: [WHAT_YOU_BELIEVE]
  - Evidence for: [SUPPORTING_DATA]
  - How to validate: [ANALYSIS_METHOD]

- Hypothesis 2: [WHAT_YOU_BELIEVE]
  (Same structure)

Analysis Types:
- [ ] Funnel analysis
- [ ] Cohort analysis
- [ ] Path analysis
- [ ] Retention analysis
- [ ] Feature usage analysis
- [ ] Segmentation analysis
- [ ] Time-based patterns
- [ ] Correlation analysis

### 2. DATA SOURCES & COLLECTION

Data Sources:
Product Analytics:
- Platform: [MIXPANEL/AMPLITUDE/GOOGLE_ANALYTICS]
- Events tracked: [KEY_EVENTS]
- Properties captured: [USER_PROPERTIES]
- Completeness: [DATA_QUALITY_LEVEL]

Database Queries:
- Tables: [RELEVANT_TABLES]
- Metrics: [CALCULATED_METRICS]
- Joins required: [DATA_RELATIONSHIPS]

Third-Party Data:
- CRM data: [SALESFORCE/HUBSPOT]
- Support tickets: [ZENDESK/INTERCOM]
- Survey data: [USER_FEEDBACK]

Data Quality Check:
- Sample size: [N]
- Coverage: [% OF USERS WITH DATA]
- Accuracy: [VALIDATION_CHECKS]
- Completeness: [MISSING_DATA_ASSESSMENT]

### 3. FUNNEL ANALYSIS

Funnel Definition:
Funnel: [FUNNEL_NAME]
Purpose: [WHAT_THIS_FUNNEL_REPRESENTS]

Steps:
Step 1: [ACTION]
- Users: [COUNT]
- % of total: [100%]

Step 2: [ACTION]
- Users: [COUNT]
- % of previous: [CONVERSION_%]
- % of total: [OVERALL_%]
- Drop-off: [% WHO LEFT]

Step 3: [ACTION]
- Users: [COUNT]
- % of previous: [CONVERSION_%]
- % of total: [OVERALL_%]
- Drop-off: [% WHO LEFT]

Step 4: [ACTION]
- Users: [COUNT]
- % of previous: [CONVERSION_%]
- % of total: [OVERALL_%]

Step 5: [ACTION]
- Users: [COUNT]
- % of previous: [CONVERSION_%]
- Overall conversion: [END_TO_END_%]

Example:
"Signup Funnel"
- Step 1: Landing page view - 10,000 users (100%)
- Step 2: Click signup - 3,000 users (30%), drop: 70%
- Step 3: Enter email - 2,400 users (80% of prev), drop: 20%
- Step 4: Enter password - 2,100 users (88% of prev), drop: 12%
- Step 5: Complete signup - 1,800 users (86% of prev), overall: 18%

Drop-off Analysis:
Largest drop-off: [STEP]
- Drop-off rate: [%]
- Users affected: [COUNT]
- Why users drop: [HYPOTHESIS]
- Evidence: [QUALITATIVE/QUANTITATIVE]

Second largest drop-off: [STEP]
(Same structure)

Time Analysis:
- Median time to complete: [DURATION]
- Time by step:
  - Step 1→2: [DURATION]
  - Step 2→3: [DURATION]
  - Step 3→4: [DURATION]

Segment Comparison:
- [SEGMENT_A]: [OVERALL_CONVERSION_%]
- [SEGMENT_B]: [OVERALL_CONVERSION_%]
- Difference: [DELTA] - [INSIGHT]

### 4. COHORT ANALYSIS

Cohort Definition:
- Cohort basis: [SIGNUP_DATE/FIRST_PURCHASE/FEATURE_ADOPTION]
- Cohort period: [WEEKLY/MONTHLY]
- Time range: [DATE_RANGE]
- Number of cohorts: [COUNT]

Retention Cohorts:
Cohort: [MONTH/WEEK]
- Size: [USERS]
- Day 1: [RETENTION_%]
- Day 7: [RETENTION_%]
- Day 30: [RETENTION_%]
- Day 60: [RETENTION_%]
- Day 90: [RETENTION_%]

Cohort Comparison:
- Best performing cohort: [WHICH] - [WHY_BETTER]
- Worst performing cohort: [WHICH] - [WHY_WORSE]
- Trend over time: [IMPROVING/DECLINING/STABLE]
- External factors: [WHAT_INFLUENCED_COHORTS]

Revenue Cohorts:
Cohort: [MONTH]
- Month 1 revenue: [AMOUNT]
- Month 2 revenue: [AMOUNT]
- Month 3 revenue: [AMOUNT]
- LTV projection: [ESTIMATED_VALUE]

Insights:
- Retention pattern: [WHAT_CURVE_SHOWS]
- Inflection points: [WHEN_USERS_STICK_OR_LEAVE]
- Cohort differences: [VARIATIONS_EXPLAINED]

### 5. USER JOURNEY ANALYSIS

Path Analysis:
Most Common Paths:
Path 1: [SEQUENCE_OF_ACTIONS]
- Users: [COUNT]
- % of total: [%]
- Outcome: [WHERE_THEY_END_UP]

Path 2: [SEQUENCE]
(Same structure)

Path 3: [SEQUENCE]
(Same structure)

Unexpected Paths:
- Path: [SURPRISING_SEQUENCE]
- Why interesting: [INSIGHT]
- Frequency: [HOW_COMMON]

Dead Ends:
- Page/feature: [WHERE_USERS_GET_STUCK]
- % who exit: [%]
- Next steps taken: [WHAT_THEY_DO_INSTEAD]

Journey Maps:
Entry Points:
- [ENTRY_1]: [% OF USERS] - [TYPICAL_PATH_FROM_HERE]
- [ENTRY_2]: [% OF USERS] - [TYPICAL_PATH_FROM_HERE]

Critical Moments:
- Moment 1: [ACTION/PAGE]
  - Importance: [WHY_CRITICAL]
  - Success rate: [%]
  - Failure impact: [CONSEQUENCE]

Exit Points:
- [EXIT_1]: [% WHO LEAVE] - [WHY_THEY_LEAVE]
- [EXIT_2]: [% WHO LEAVE] - [WHY_THEY_LEAVE]

### 6. FEATURE USAGE ANALYSIS

Feature Adoption:
Feature: [FEATURE_NAME]
- Users exposed: [COUNT]
- Users who tried: [COUNT] ([ADOPTION_%])
- Active users: [COUNT] ([ACTIVE_%])
- Power users: [COUNT] ([HEAVY_USAGE_%])

Usage Patterns:
- Frequency: [DAILY/WEEKLY/MONTHLY]
- Sessions per user: [AVERAGE]
- Actions per session: [AVERAGE]
- Time spent: [AVERAGE_DURATION]

Adoption Curve:
- Week 1: [ADOPTION_%]
- Week 2: [ADOPTION_%]
- Week 4: [ADOPTION_%]
- Month 3: [ADOPTION_%]
- Plateau: [EVENTUAL_%]

Feature Correlation:
- Users of Feature A who also use Feature B: [%]
- Feature combos that predict retention: [COMBINATIONS]
- Feature usage vs churn: [CORRELATION]

Abandonment:
- Users who stopped using: [COUNT]
- When they stopped: [TIME_PERIOD]
- Why they stopped: [HYPOTHESIS_FROM_DATA]
- Reactivation rate: [%]

### 7. SEGMENTATION ANALYSIS

Behavioral Segments:
Segment 1: [SEGMENT_NAME]
- Definition: [BEHAVIORAL_CRITERIA]
- Size: [COUNT/_%]
- Characteristics:
  - Usage frequency: [PATTERN]
  - Features used: [PREFERENCES]
  - Engagement level: [SCORE]
  - Retention: [%]
  - Value: [LTV/REVENUE]

Example:
"Power Users"
- Definition: Use product 5+ days/week, use 3+ features, tenure >3 months
- Size: 15% of users (1,500 users)
- Characteristics:
  - Usage: Daily, avg 45 min/session
  - Features: Use advanced features + core
  - Engagement: 90% DAU/MAU
  - Retention: 95% month-over-month
  - Value: 3x ARPU, 5x LTV

Segment 2: [SEGMENT_NAME]
(Same structure)

Segment 3: [SEGMENT_NAME]
(Same structure)

Segment Comparison:
Metric: [METRIC_NAME]
- Segment A: [VALUE]
- Segment B: [VALUE]
- Segment C: [VALUE]
- Key differences: [INSIGHTS]

### 8. ENGAGEMENT PATTERNS

Activity Patterns:
Time-based Patterns:
- Peak usage hours: [TIME_OF_DAY]
- Peak usage days: [DAYS_OF_WEEK]
- Seasonal patterns: [MONTHLY/QUARTERLY]

Session Analysis:
- Average session length: [DURATION]
- Sessions per user: [FREQUENCY]
- Pages per session: [DEPTH]
- Bounce rate: [%]

Engagement Levels:
High Engagement:
- Definition: [CRITERIA]
- % of users: [%]
- Retention: [%]
- Value: [REVENUE_CONTRIBUTION]

Medium Engagement:
- Definition: [CRITERIA]
- % of users: [%]
- Retention: [%]

Low Engagement:
- Definition: [CRITERIA]
- % of users: [%]
- Retention: [%]
- At-risk: [% LIKELY TO CHURN]

Engagement Drivers:
- Action 1: [ACTION] - Increases engagement by [%]
- Action 2: [ACTION] - Increases engagement by [%]
- Action 3: [ACTION] - Increases engagement by [%]

### 9. CHURN & RETENTION ANALYSIS

Churn Analysis:
Overall Churn:
- Churn rate: [%_PER_MONTH]
- Churned users: [COUNT]
- Trend: [INCREASING/DECREASING/STABLE]

Churn Segments:
- [SEGMENT_1]: [CHURN_%]
- [SEGMENT_2]: [CHURN_%]
- [SEGMENT_3]: [CHURN_%]
- Highest risk: [WHICH_SEGMENT]

Early Warning Signals:
Signal 1: [BEHAVIOR]
- Churn probability: [%]
- Detection window: [HOW_EARLY]
- Prevalence: [% OF USERS SHOW THIS]

Signal 2: [BEHAVIOR]
(Same structure)

Signal 3: [BEHAVIOR]
(Same structure)

Retention Drivers:
Positive Drivers:
- [BEHAVIOR_1]: Associated with [%] higher retention
- [BEHAVIOR_2]: Associated with [%] higher retention

Negative Drivers:
- [BEHAVIOR_1]: Associated with [%] higher churn
- [BEHAVIOR_2]: Associated with [%] higher churn

Resurrection Analysis:
- Churned users who returned: [%]
- What brought them back: [TRIGGERS]
- Retention after return: [%]

### 10. POWER USER ANALYSIS

Power User Definition:
Criteria: [WHAT_MAKES_SOMEONE_A_POWER_USER]
- Size: [% OF USER BASE]
- Value: [REVENUE_CONTRIBUTION_%]

Power User Behaviors:
- Frequency: [USAGE_PATTERN]
- Features: [WHICH_FEATURES_THEY_USE]
- Depth: [HOW_DEEPLY_THEY_USE]
- Tenure: [HOW_LONG_THEY_STAY]

Path to Power User:
Activation Actions:
- Action 1: [ACTION]
  - % of power users who did this: [%]
  - Timing: [WHEN_IN_JOURNEY]
  - Impact: [CORRELATION_TO_RETENTION]

- Action 2: [ACTION]
  (Same structure)

Time to Power User:
- Median time: [DURATION]
- What happens in that time: [KEY_MILESTONES]

Replicating Power Users:
- Behaviors to encourage: [ACTIONS]
- Interventions to test: [PRODUCT_CHANGES]
- Expected impact: [PROJECTED_OUTCOME]

### 11. FRICTION POINTS

Friction Identification:
Friction Point 1: [LOCATION/FEATURE]
- Issue: [WHAT'S_WRONG]
- Evidence: [DATA_SHOWING_FRICTION]
  - Drop-off rate: [%]
  - Time spent: [LONGER_THAN_EXPECTED]
  - Error rate: [%]
  - User feedback: [QUOTES/COMPLAINTS]
- Impact: [USERS_AFFECTED/REVENUE_LOST]
- Severity: [HIGH/MEDIUM/LOW]

Friction Point 2: [LOCATION/FEATURE]
(Same structure)

Friction Point 3: [LOCATION/FEATURE]
(Same structure)

Root Cause Analysis:
- What: [OBSERVABLE_PROBLEM]
- Why 1: [SURFACE_REASON]
- Why 2: [DEEPER_REASON]
- Why 3: [ROOT_CAUSE]
- Solution: [HOW_TO_FIX]

### 12. INSIGHTS & RECOMMENDATIONS

Key Insights:
Insight 1: [FINDING]
- Evidence: [DATA_SUPPORTING]
- Impact: [WHO_AFFECTED/HOW_MUCH]
- Confidence: [HIGH/MEDIUM/LOW]
- Implications: [WHAT_THIS_MEANS]

Example:
"Users who complete onboarding in <5 minutes have 3x higher retention"
- Evidence: Cohort analysis shows 60% D30 retention vs 20% for slower onboarding
- Impact: 8,000 users/month, 40% take >5 minutes
- Confidence: High (n=50,000, p<0.001)
- Implications: Optimize onboarding for speed, target <5 minutes

Insight 2: [FINDING]
(Same structure)

Insight 3: [FINDING]
(Same structure)

Recommendations:
Priority 1 (High Impact, High Confidence):
- Recommendation: [WHAT_TO_DO]
- Rationale: [WHY]
- Expected impact: [QUANTIFIED_BENEFIT]
- Effort: [DEVELOPMENT_TIME]
- Owner: [TEAM_RESPONSIBLE]

Priority 2 (High Impact, Medium Confidence):
- Recommendation: [WHAT_TO_DO]
- Test first: [VALIDATION_NEEDED]
- Expected impact: [RANGE]

Priority 3 (Quick Wins):
- Recommendation: [WHAT_TO_DO]
- Low effort, moderate impact

Follow-up Analysis:
- [ ] [NEXT_QUESTION_TO_ANSWER]
- [ ] [ADDITIONAL_SEGMENTATION]
- [ ] [DEEPER_DIVE_NEEDED]

### 13. TRACKING & MEASUREMENT

Success Metrics:
If we implement recommendations:
- Metric 1: [METRIC] should move from [BASELINE] to [TARGET]
- Metric 2: [METRIC] should move from [BASELINE] to [TARGET]
- Timeline: [WHEN_TO_EXPECT_IMPACT]

Measurement Plan:
- Dashboard: [WHERE_TO_TRACK]
- Review cadence: [FREQUENCY]
- Owner: [WHO_MONITORS]
- Adjustments: [WHEN_TO_ITERATE]

A/B Tests to Run:
- Test 1: [HYPOTHESIS_TO_VALIDATE]
- Test 2: [HYPOTHESIS_TO_VALIDATE]
```

## Variables

### PRODUCT_NAME
Your product.
**Examples:**
- "Mobile fitness app"
- "B2B SaaS platform"
- "E-commerce website"

### RESEARCH_QUESTION
What you want to understand.
**Examples:**
- "Why do users abandon onboarding?"
- "What behaviors predict long-term retention?"
- "Why isn't Feature X being adopted?"

### DATA_SOURCES
Where your data comes from.
**Examples:**
- "Mixpanel events + Postgres database + support tickets"
- "Google Analytics + Stripe + user surveys"
- "Amplitude + Salesforce + NPS surveys"

### PRODUCT_DECISIONS
What this analysis will inform.
**Examples:**
- "Whether to redesign onboarding flow"
- "Which segments to target with new feature"
- "Where to focus product improvements"

### TARGET_METRICS
What you're trying to improve.
**Examples:**
- "7-day retention rate"
- "Feature adoption rate"
- "Conversion to paid"

## Usage Examples

### Example 1: Onboarding Drop-off Analysis
```
Question: Why do 60% of users abandon onboarding?
Funnel Analysis:
- Step 1 (Welcome): 10,000 users
- Step 2 (Profile): 7,000 (-30%)
- Step 3 (Connect accounts): 4,500 (-36%) ← Largest drop
- Step 4 (First action): 4,000 (-11%)
Finding: OAuth connection step is major friction
Segment: Mobile users drop at 2x rate (45% vs 20%)
Action: Simplify connection flow, make skippable
```

### Example 2: Feature Adoption Analysis
```
Feature: Advanced reporting dashboard
Adoption: Only 12% of eligible users
Analysis:
- Discovery: 80% of users don't know it exists
- Activation: Of those aware, 60% try it
- Retention: Of those who try, 50% use regularly
Issue: Discovery problem, not value problem
Action: Add in-product prompts, highlight in emails
Expected: 30% adoption (2.5x improvement)
```

### Example 3: Churn Prediction
```
Question: Can we predict churn before it happens?
Analysis: Logistic regression on 6 months of data
Warning Signals:
- No login in 7 days: 3x churn risk
- <50% feature usage vs first month: 4x risk
- Support ticket in last 30 days: 2x risk
Predictive: Model accuracy 78%, 14-day lead time
Action: Automated health scores, proactive outreach
```

### Example 4: Power User Analysis
```
Power Users: Top 10% by engagement
Behaviors:
- Invite 3+ team members (vs 0 for others)
- Use mobile + desktop (vs desktop only)
- Complete profile within 24 hours
- Use 4+ features (vs 2 average)
Value: 5x LTV, 95% retention vs 60%
Action: Optimize for these behaviors in onboarding
Expected: 25% more users reach power user status
```

## Best Practices

### Analysis Approach
1. **Start with questions** - Not "let's look at the data" but "what do we need to know?"
2. **Hypothesize first** - Form beliefs to test, not just explore
3. **Multiple methods** - Combine funnel, cohort, segment analysis
4. **Quantitative + qualitative** - Numbers + user feedback
5. **Action-oriented** - Every insight should inform a decision

### Data Quality
1. **Validate data** - Check sample sizes, completeness, accuracy
2. **Understand bias** - What's missing or skewed in your data?
3. **Segment appropriately** - Aggregates hide important variation
4. **Time windows** - Choose analysis periods carefully
5. **Statistical significance** - Know when sample sizes matter

### Insights
1. **So what?** - Every finding should have a clear implication
2. **Prioritize** - Not all insights are equally actionable
3. **Confidence levels** - Be honest about certainty
4. **Context** - External factors, seasonality, experiments running
5. **Tell a story** - Connect findings into coherent narrative

### Communication
1. **Visual** - Charts and graphs over tables
2. **Simple** - Accessible to non-technical stakeholders
3. **Action-focused** - Recommendations, not just observations
4. **Transparent** - Show methodology and limitations
5. **Iterative** - Share early, incorporate feedback

## Common Pitfalls

❌ **Analysis paralysis** - Endless analysis without action
✅ Instead: Time-box analysis, make decision with available data

❌ **Confirmation bias** - Only looking for data that supports your hypothesis
✅ Instead: Actively seek disconfirming evidence

❌ **Spurious correlations** - Confusing correlation with causation
✅ Instead: Test causal hypotheses with experiments

❌ **Ignoring segments** - Looking only at aggregate metrics
✅ Instead: Always segment by user type, cohort, behavior

❌ **Cherry-picking** - Selecting favorable time periods or metrics
✅ Instead: Consistent methodology across analyses

❌ **Missing the forest** - Getting lost in details, missing big picture
✅ Instead: Start with high-level patterns, drill into details

❌ **Not validating findings** - Acting on analysis without testing
✅ Instead: Use A/B tests to validate insights before major changes

❌ **Stale analysis** - Using outdated data or not refreshing
✅ Instead: Regular updates, especially for key metrics

## Analysis Checklist

Planning:
- [ ] Research questions clearly defined
- [ ] Hypotheses documented
- [ ] Success criteria established
- [ ] Data sources identified
- [ ] Analysis timeline set

Execution:
- [ ] Data quality validated
- [ ] Sample sizes sufficient
- [ ] Multiple analysis methods used
- [ ] Segmentation applied
- [ ] Statistical significance checked

Insights:
- [ ] Key findings documented
- [ ] Confidence levels assigned
- [ ] Implications explained
- [ ] Recommendations prioritized
- [ ] Follow-up questions identified

Communication:
- [ ] Results visualized clearly
- [ ] Stakeholders briefed
- [ ] Decisions made
- [ ] Actions assigned
- [ ] Tracking plan established

---

**Last Updated:** 2025-11-12
**Category:** Product Management > Product Analytics
**Difficulty:** Intermediate to Advanced
**Estimated Time:** 1-2 weeks per major analysis
