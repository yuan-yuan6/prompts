---
category: product-management
last_updated: 2025-11-12
title: Product-Market Fit Assessment & Achievement
tags:
- product-management
- product-market-fit
- pmf
- validation
use_cases:
- Assessing current product-market fit levels
- Identifying gaps preventing PMF achievement
- Designing experiments to test and improve PMF
- Measuring PMF through quantitative and qualitative signals
related_templates:
- product-management/Product-Strategy/product-strategy-vision.md
- product-management/Product-Development/user-research-personas.md
- product-management/Product-Analytics/product-metrics-kpis.md
- product-management/Product-Strategy/market-competitive-analysis.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: template
difficulty: intermediate
slug: product-market-fit
---

# Product-Market Fit Assessment & Achievement Template

## Purpose
Systematically assess product-market fit, identify gaps preventing PMF achievement, design validation experiments, and create actionable plans to reach strong product-market fit.

## Quick PMF Prompt
Assess product-market fit for [product]. Measure: Sean Ellis survey (% "very disappointed"), retention curves (D1/D7/D30), NPS score, organic growth rate, engagement metrics. Benchmark against PMF thresholds (>40% Ellis, >20% M1 retention). Identify gaps preventing PMF. Recommend top 3 experiments to improve fit, with hypotheses and success criteria. Timeline to strong PMF: [target].

## Quick Start

**Need to assess PMF quickly?** Use this streamlined approach:

### Minimal Example
```
PMF Survey: "How disappointed would you be if you could no longer use this product?"
Result: 25% "very disappointed" (Target: >40% for strong PMF)
Key Metrics:
- Retention: 30% Month 1 (weak)
- NPS: 15 (poor)
- Organic growth: 10% (low)
Assessment: PRE-PMF
Gap: Product solves problem but UX too complex, onboarding poor
Action: Simplify core workflow, redesign onboarding, focus on power users
Target: 45% PMF score in 3 months
```

### When to Use This
- Early-stage product validating market need
- Product pivot or major repositioning
- Struggling with retention or growth
- Before scaling go-to-market efforts
- Investor/board requesting PMF evidence

### Basic 5-Step Workflow
1. **Measure current PMF** - Quantitative and qualitative assessment (1 week)
2. **Identify gaps** - What's preventing strong PMF (1 week)
3. **Prioritize actions** - Highest-impact improvements (2-3 days)
4. **Run experiments** - Test improvements (4-8 weeks)
5. **Iterate** - Continuous measurement and refinement (ongoing)

---

## Template

```
You are an experienced product strategist and PMF expert. Assess product-market fit for [PRODUCT_NAME] serving [TARGET_MARKET] with [CURRENT_STATE] to identify [PMF_GAPS] and create plan to achieve [PMF_TARGET] within [TIMEFRAME].

PMF ASSESSMENT CONTEXT:
Product Information:
- Product name: [PRODUCT_NAME]
- Product category: [CATEGORY]
- Target market: [MARKET_DESCRIPTION]
- Stage: [EARLY_MVP/GROWTH/SCALING]
- Time in market: [DURATION]

Current Metrics:
- Users: [COUNT]
- Customers: [COUNT_IF_B2B]
- Revenue: [MRR/ARR]
- Growth rate: [%_MONTHLY]
- Retention: [COHORT_RETENTION]

### 1. PMF MEASUREMENT FRAMEWORK

Sean Ellis PMF Test:
Survey Question:
"How would you feel if you could no longer use [PRODUCT_NAME]?"
- [ ] Very disappointed
- [ ] Somewhat disappointed
- [ ] Not disappointed (it isn't really that useful)
- [ ] N/A - I no longer use [PRODUCT_NAME]

Results:
- Very disappointed: [%]
- Somewhat disappointed: [%]
- Not disappointed: [%]
- No longer use: [%]

PMF Score: [% WHO ANSWERED "VERY DISAPPOINTED"]

Benchmark:
- <40%: Pre-PMF (not enough love)
- 40-50%: Medium PMF (good, keep improving)
- >50%: Strong PMF (ready to scale)

Your Score: [%] - [ASSESSMENT]

Qualitative Follow-up:
For "Very Disappointed" Users:
- What is the main benefit you receive from [PRODUCT]?
- What type of person do you think would most benefit?
- How can we improve [PRODUCT] for you?

For "Not Disappointed" Users:
- What would make [PRODUCT] more useful to you?
- What alternatives have you tried or would you use?

Insights: [KEY_THEMES_FROM_RESPONSES]

### 2. QUANTITATIVE PMF SIGNALS

Retention Metrics:
Cohort Retention:
- Week 1: [%]
- Month 1: [%]
- Month 3: [%]
- Month 6: [%]

Assessment:
- Retention curve: [FLATTENING/DECLINING]
- Benchmark vs industry: [ABOVE/BELOW_AVERAGE]
- PMF Signal: [STRONG/WEAK]

Strong PMF indicators:
- Retention curve flattens (not declining to zero)
- >40% retention at Month 3
- Cohorts improving over time

Growth Metrics:
Organic Growth:
- Organic signups: [% OF TOTAL]
- Word-of-mouth: [% ATTRIBUTE TO WOM]
- Viral coefficient: [K-FACTOR]

Paid vs Organic:
- If >80% paid growth: [WEAK_PMF_SIGNAL]
- If >40% organic: [STRONG_PMF_SIGNAL]

Net Promoter Score (NPS):
- Score: [VALUE]
- Promoters: [%]
- Passives: [%]
- Detractors: [%]

PMF Benchmark:
- <0: Pre-PMF
- 0-30: Emerging PMF
- 30-50: Good PMF
- >50: Excellent PMF

Usage Intensity:
- Daily Active Users / Monthly Active Users: [RATIO]
- Sessions per user per week: [COUNT]
- Time spent per session: [MINUTES]

Benchmark:
- DAU/MAU >40%: Strong engagement
- DAU/MAU 20-40%: Medium engagement
- DAU/MAU <20%: Weak engagement

Revenue Metrics (if applicable):
- LTV:CAC ratio: [RATIO]
  - <1: Not viable
  - 1-3: Weak economics
  - >3: Good economics
- Payback period: [MONTHS]
  - <12 months: Good
  - >18 months: Problematic
- Net Revenue Retention: [%]
  - >100%: Strong PMF
  - 90-100%: Acceptable
  - <90%: PMF issues

Expansion Revenue:
- Upsell rate: [%]
- Cross-sell rate: [%]
- Expansion MRR: [% OF TOTAL]

Strong Signal: Customers naturally want more

### 3. QUALITATIVE PMF SIGNALS

Customer Voice:
Customer Testimonials:
- Number of unsolicited testimonials: [COUNT]
- Themes: [WHAT_CUSTOMERS_SAY]
- Passion level: [LOW/MEDIUM/HIGH]

Reference Customers:
- Willing to be references: [COUNT]
- Actively referring others: [COUNT]
- Case study participants: [COUNT]

Social Proof:
- Online reviews: [AVG_RATING]
- Social media mentions: [VOLUME/SENTIMENT]
- Community engagement: [ACTIVITY_LEVEL]

Sales Signals:
Sales Cycle:
- Average time to close: [DAYS]
- Trend: [SHORTENING/LENGTHENING]

If shortening: [PRODUCT_SELLING_ITSELF]
If lengthening: [PMF_ISSUES]

Win Rate:
- Competitive win rate: [%]
- Overall win rate: [%]
- Trend: [IMPROVING/DECLINING]

Deal Size:
- Average deal size: [AMOUNT]
- Trend: [INCREASING/FLAT/DECREASING]

Increasing deal size = customers see value

Objections:
- Common objections: [LIST]
- Frequency of "too expensive": [HIGH/LOW]
- Product gaps mentioned: [THEMES]

Churn Analysis:
Churn Reasons:
- Top reason 1: [REASON] - [%]
- Top reason 2: [REASON] - [%]
- Top reason 3: [REASON] - [%]

Interpretation:
- Product fit issues: [WHAT_THIS_INDICATES]
- Target market issues: [INSIGHTS]
- Competition: [PATTERNS]

Reactivation:
- % of churned users who return: [%]
- What brings them back: [TRIGGERS]

Market Pull:
Inbound Demand:
- Inbound leads: [% OF PIPELINE]
- Unsolicited demo requests: [VOLUME]
- Waitlist growth: [TREND]

Strong PMF: Market pulling vs you pushing

Media & PR:
- Unsolicited press coverage: [INSTANCES]
- Industry recognition: [AWARDS/MENTIONS]
- Thought leadership requests: [SPEAKING/WRITING]

### 4. PMF ASSESSMENT BY SEGMENT

Segment Analysis:
Segment 1: [SEGMENT_NAME]
- PMF Score: [%]
- Retention: [MONTH_3_%]
- NPS: [SCORE]
- Growth: [ORGANIC_%]
- Assessment: [STRONG/WEAK_PMF]

Evidence:
- [SUPPORTING_DATA_1]
- [SUPPORTING_DATA_2]

Segment 2: [SEGMENT_NAME]
(Same structure)

Segment 3: [SEGMENT_NAME]
(Same structure)

Findings:
- Strongest PMF: [WHICH_SEGMENT]
- Why: [EXPLANATION]
- Weakest PMF: [WHICH_SEGMENT]
- Why: [EXPLANATION]

Strategic Implication:
- Double down on: [STRONG_PMF_SEGMENT]
- Deprioritize: [WEAK_PMF_SEGMENT]
- Iterate for: [MEDIUM_PMF_SEGMENT]

### 5. PMF GAP ANALYSIS

PMF Components Framework:
Component 1: Target Market
- Clarity: [CLEAR/VAGUE]
- Evidence: [DO_WE_KNOW_WHO_WE_SERVE]
- Gap: [WHAT'S_MISSING]
- Score: [1-10]

Component 2: Underserved Need
- Validated: [YES/NO]
- Pain level: [CRITICAL/MODERATE/NICE_TO_HAVE]
- Current alternatives: [WHAT_THEY_USE_TODAY]
- Gap: [WHAT'S_MISSING]
- Score: [1-10]

Component 3: Value Proposition
- Clarity: [CLEAR/MUDDY]
- Differentiation: [UNIQUE/SIMILAR_TO_OTHERS]
- Proof: [EVIDENCE_OF_VALUE]
- Gap: [WHAT'S_MISSING]
- Score: [1-10]

Component 4: Product Experience
- Solves problem: [WELL/PARTIALLY/POORLY]
- Ease of use: [EASY/MODERATE/HARD]
- Quality: [HIGH/MEDIUM/LOW]
- Gap: [WHAT'S_MISSING]
- Score: [1-10]

Component 5: Pricing & Business Model
- Alignment: [VALUE_MATCHES_PRICE]
- Affordability: [FOR_TARGET_MARKET]
- Model fit: [BUSINESS_MODEL_WORKS]
- Gap: [WHAT'S_MISSING]
- Score: [1-10]

Gap Summary:
- Overall PMF Score: [AVERAGE_OF_COMPONENTS]
- Biggest gap: [LOWEST_SCORING_COMPONENT]
- Critical fixes: [TOP_3_PRIORITIES]

### 6. WHY PMF IS LACKING

Problem Hypotheses:
Hypothesis 1: Wrong Target Market
Evidence:
- [DATA_POINT_1]
- [DATA_POINT_2]
Validation: [HOW_TO_TEST]

Hypothesis 2: Product Doesn't Solve Problem Well Enough
Evidence:
- [DATA_POINT_1]
- [DATA_POINT_2]
Validation: [HOW_TO_TEST]

Hypothesis 3: Problem Not Painful Enough
Evidence:
- [DATA_POINT_1]
- [DATA_POINT_2]
Validation: [HOW_TO_TEST]

Hypothesis 4: Go-to-Market Issues
Evidence:
- [DATA_POINT_1]
- [DATA_POINT_2]
Validation: [HOW_TO_TEST]

Hypothesis 5: Positioning/Messaging Unclear
Evidence:
- [DATA_POINT_1]
- [DATA_POINT_2]
Validation: [HOW_TO_TEST]

Most Likely Root Cause:
- Primary issue: [HYPOTHESIS]
- Why we believe this: [RATIONALE]
- How to validate: [APPROACH]

### 7. PATH TO PMF

PMF Roadmap:
Phase 1: Validate (Weeks 1-4)
Goals:
- Identify true ICP
- Validate problem/solution fit
- Find early adopters

Actions:
- [ ] Interview 20+ target customers
- [ ] Analyze power user behavior
- [ ] Run PMF survey
- [ ] Identify common patterns

Success Criteria:
- [METRIC_1]: [TARGET]
- [METRIC_2]: [TARGET]

Phase 2: Iterate (Weeks 5-12)
Goals:
- Improve core value prop
- Optimize for power users
- Remove friction

Actions:
- [ ] Implement top 3 user requests
- [ ] Simplify onboarding
- [ ] Improve core workflow
- [ ] A/B test key improvements

Success Criteria:
- [METRIC_1]: [TARGET]
- [METRIC_2]: [TARGET]

Phase 3: Double Down (Weeks 13-24)
Goals:
- Achieve PMF with ICP
- Prove repeatability
- Build growth engine

Actions:
- [ ] Focus 100% on ICP
- [ ] Scale what's working
- [ ] Build viral loops
- [ ] Optimize conversion

Success Criteria:
- PMF Score: [>40%]
- Retention: [FLATTENING_CURVE]
- Organic growth: [>30%_OF_SIGNUPS]

### 8. SPECIFIC PMF EXPERIMENTS

Experiment 1: [EXPERIMENT_NAME]
Hypothesis: [WHAT_WE_BELIEVE]
Metric: [HOW_WE_MEASURE]
Method: [WHAT_WE'LL_DO]
Duration: [TIMELINE]
Success criteria: [THRESHOLD]

Example:
"Simplified Onboarding Test"
Hypothesis: Complex onboarding prevents activation
Metric: % users who complete first key action
Method: A/B test 3-step vs 7-step onboarding
Duration: 2 weeks
Success: >60% activation (vs 40% baseline)

Experiment 2: [EXPERIMENT_NAME]
(Same structure)

Experiment 3: [EXPERIMENT_NAME]
(Same structure)

### 9. ICP REFINEMENT

Current ICP:
- Definition: [WHO_WE_THINK_WE_SERVE]
- Evidence: [WHAT_SUPPORTS_THIS]

PMF by ICP Characteristic:
By Company Size (B2B):
- 1-10 employees: [PMF_SCORE]
- 11-50 employees: [PMF_SCORE]
- 51-200 employees: [PMF_SCORE]
- 200+ employees: [PMF_SCORE]

Strongest: [SEGMENT]

By Industry:
- [INDUSTRY_1]: [PMF_SCORE]
- [INDUSTRY_2]: [PMF_SCORE]
- [INDUSTRY_3]: [PMF_SCORE]

Strongest: [SEGMENT]

By Use Case:
- [USE_CASE_1]: [PMF_SCORE]
- [USE_CASE_2]: [PMF_SCORE]
- [USE_CASE_3]: [PMF_SCORE]

Strongest: [SEGMENT]

Refined ICP:
- Who: [SPECIFIC_PROFILE]
- Why them: [EVIDENCE_OF_STRONGEST_PMF]
- Market size: [ADDRESSABLE_MARKET]
- Strategy: [FOCUS_HERE_FIRST]

### 10. PMF TRACKING & GOALS

Current State:
- PMF Score: [%]
- Status: [PRE_PMF/EMERGING/STRONG]
- Key weakness: [MAIN_GAP]

30-Day Goals:
- PMF Score: [TARGET_%]
- Retention (M1): [TARGET_%]
- NPS: [TARGET_SCORE]
- Actions: [TOP_3_PRIORITIES]

90-Day Goals:
- PMF Score: [TARGET_%]
- Retention (M3): [TARGET_%]
- Organic growth: [TARGET_%]
- Actions: [MAJOR_INITIATIVES]

6-Month Goals:
- PMF Score: [TARGET_%]
- Status: [TARGET_STATE]
- Business metrics: [REVENUE/GROWTH_TARGETS]

Review Cadence:
- Weekly: [LEADING_INDICATORS]
- Monthly: [PMF_SURVEY/COHORTS]
- Quarterly: [COMPREHENSIVE_ASSESSMENT]

### 11. RED FLAGS & GREEN FLAGS

Red Flags (Pre-PMF):
- [ ] PMF score <40%
- [ ] Retention declining over time
- [ ] >80% paid acquisition
- [ ] High churn (>5% monthly)
- [ ] Long sales cycles getting longer
- [ ] Customers need heavy convincing
- [ ] Low NPS (<20)
- [ ] Few organic signups
- [ ] No one "loves" the product
- [ ] Can't articulate clear value prop

Count: [NUMBER_OF_RED_FLAGS]

Green Flags (Strong PMF):
- [ ] PMF score >40%
- [ ] Retention curve flattening
- [ ] Organic growth >30%
- [ ] Customers referring others
- [ ] NPS >30
- [ ] Growing without paid marketing
- [ ] Customers resist losing product
- [ ] Sales cycles shortening
- [ ] Natural upsells happening
- [ ] Clear, passionate user testimonials

Count: [NUMBER_OF_GREEN_FLAGS]

Assessment:
- If >5 red flags: [SIGNIFICANT_PMF_ISSUES]
- If >5 green flags: [STRONG_PMF]
- Mixed signals: [EMERGING_PMF_IN_SOME_SEGMENTS]

### 12. DECISION FRAMEWORK

If Strong PMF (>50% score):
Actions:
- [ ] Scale go-to-market
- [ ] Invest in growth
- [ ] Expand team
- [ ] Optimize for scale
- [ ] Consider raising capital

If Emerging PMF (40-50% score):
Actions:
- [ ] Continue iterating product
- [ ] Focus on power users
- [ ] Improve retention
- [ ] Limited marketing spend
- [ ] Don't scale prematurely

If Pre-PMF (<40% score):
Actions:
- [ ] Pause scaling efforts
- [ ] Deep customer research
- [ ] Rapid iteration
- [ ] Consider pivot
- [ ] Burn rate awareness
- [ ] Do not scale marketing

Pivot Consideration:
When to consider pivot:
- No improvement after 3+ months of focused iteration
- <20% PMF score with no upward trend
- Can't find segment with strong PMF
- Market shrinking or disappearing
- Fundamental product/market mismatch

Pivot Options:
- Target market pivot: [NEW_CUSTOMER]
- Problem pivot: [NEW_PROBLEM_TO_SOLVE]
- Solution pivot: [NEW_APPROACH]
- Business model pivot: [NEW_MONETIZATION]
```

## Variables

### PRODUCT_NAME
Your product.
**Examples:**
- "Enterprise HR platform"
- "Personal finance app"
- "B2B sales automation tool"

### TARGET_MARKET
Who you serve.
**Examples:**
- "Mid-market SaaS companies (50-500 employees)"
- "Millennials managing student debt"
- "Inside sales teams at tech companies"

### CURRENT_STATE
Where you are now.
**Examples:**
- "6 months post-launch, 1,000 users, struggling with retention"
- "2 years in market, $500K ARR, seeking PMF before scaling"
- "Early MVP, 100 users, validating problem/solution fit"

### PMF_GAPS
What's preventing PMF.
**Examples:**
- "Unclear ICP, product too complex, poor onboarding"
- "Right problem, wrong solution approach"
- "Strong product but wrong target market"

### PMF_TARGET
Goal state.
**Examples:**
- "45% PMF score, 50% Month 3 retention, 30% organic growth"
- "Clear ICP with >50% PMF, ready to scale GTM"
- "Product-market fit with SMB segment proven"

### TIMEFRAME
Timeline to achieve.
**Examples:**
- "3 months to prove PMF"
- "6 months to strong PMF"
- "90 days to validate or pivot"

## Usage Examples

### Example 1: B2B SaaS Pre-PMF
```
Product: Project management for agencies
PMF Score: 28% (Pre-PMF)
Metrics: 35% M1 retention, NPS 12, 15% organic
Gap: Too complex, unclear differentiation vs competitors
Action: Focus on creative agencies specifically, simplify for their workflow
Experiments: Simplified onboarding, agency-specific templates
Target: 45% PMF score in 3 months
```

### Example 2: Consumer App Emerging PMF
```
Product: Habit tracking app
PMF Score: 42% (Emerging PMF)
Metrics: 45% M1 retention, NPS 38, 35% organic
Strong with: Young professionals seeking productivity
Weak with: Older demographics, casual users
Action: Double down on professional productivity use case
Target: 55% PMF score in 6 months
```

### Example 3: Marketplace Finding PMF
```
Product: Freelance marketplace for designers
PMF Score: 35% overall (Pre-PMF)
Segmented: Enterprise buyers 55%, SMB buyers 22%
Gap: Trying to serve everyone, weak for SMB
Action: Pivot to enterprise-only, build for their needs
Target: 50% PMF with enterprise in 4 months
```

### Example 4: B2B Product Pivoting
```
Product: General business analytics
PMF Score: 22% after 12 months
Problem: Too generic, competitors have stronger offerings
Decision: Pivot to retail-specific analytics
Rationale: 10 of 50 customers are retail with 60% PMF score
Action: Rebuild for retail use case exclusively
Target: 45% PMF in retail segment in 6 months
```

## Best Practices

### Measurement
1. **Quantitative + qualitative** - Don't rely on single metric
2. **Segment analysis** - PMF varies by customer type
3. **Regular cadence** - Monthly PMF surveys minimum
4. **Honest assessment** - Don't fool yourself
5. **Trend over time** - Direction matters as much as absolute score

### Finding PMF
1. **Narrow focus** - Easier to achieve PMF with specific ICP
2. **Talk to users** - Constant customer conversations
3. **Rapid iteration** - Weekly product improvements
4. **Follow the love** - Double down on who loves you
5. **Patience** - PMF can take 12-24 months

### Avoiding Pitfalls
1. **Don't scale prematurely** - PMF before growth
2. **Don't ignore signals** - Low retention means no PMF
3. **Don't over-pivot** - Give iterations time to work
4. **Don't optimize locally** - Solve real problem, not symptoms
5. **Don't confuse revenue with PMF** - Can sell without PMF

### Iteration
1. **Focus on retention** - Acquisition without retention is futile
2. **Power user analysis** - Understand who loves you and why
3. **Remove friction** - Every obstacle delays PMF
4. **Validate assumptions** - Test, don't assume
5. **Kill bad segments** - Stop serving those without PMF

## Common Pitfalls

❌ **Scaling before PMF** - Spending on growth without retention
✅ Instead: Achieve PMF first, then scale

❌ **Ignoring retention** - Focusing on signups while users churn
✅ Instead: Retention > acquisition until PMF

❌ **Serving everyone** - Trying to achieve PMF with broad market
✅ Instead: Nail PMF with narrow ICP first

❌ **Confusing revenue with PMF** - Selling but users aren't engaged
✅ Instead: Look at retention, NPS, organic growth

❌ **Not talking to users** - Relying only on analytics
✅ Instead: Constant customer conversations

❌ **Pivot too quickly** - Changing direction every month
✅ Instead: Give iterations 3 months to show results

❌ **Optimize features vs problem** - Adding features without validating problem
✅ Instead: Ensure you're solving right problem first

❌ **Vanity metrics** - Celebrating signups while ignoring churn
✅ Instead: Focus on retention and engagement

## PMF Assessment Checklist

Monthly PMF Check:
- [ ] Run PMF survey (Sean Ellis test)
- [ ] Calculate retention cohorts
- [ ] Measure NPS
- [ ] Track organic vs paid growth
- [ ] Analyze churn reasons
- [ ] Review customer testimonials
- [ ] Assess segment performance
- [ ] Update PMF score

Quarterly Deep Dive:
- [ ] Comprehensive PMF assessment
- [ ] Segment analysis
- [ ] Gap analysis
- [ ] ICP refinement
- [ ] Experiment results review
- [ ] Roadmap adjustment
- [ ] Team alignment on priorities

Signs You Have PMF:
- [ ] >40% would be "very disappointed" without product
- [ ] Retention curve flattening (not declining)
- [ ] >30% organic growth
- [ ] NPS >30
- [ ] Customers actively referring others
- [ ] Natural expansion revenue
- [ ] Clear, passionate testimonials
- [ ] Product selling itself

---

**Last Updated:** 2025-11-12
**Category:** Product Management > Product Strategy
**Difficulty:** Advanced
**Estimated Time:** Ongoing assessment; 3-12 months to achieve strong PMF
