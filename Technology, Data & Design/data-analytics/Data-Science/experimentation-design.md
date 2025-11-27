---
category: data-analytics
last_updated: 2025-11-09
related_templates:
- data-analytics/dashboard-design-patterns.md
- data-analytics/data-governance-framework.md
- data-analytics/predictive-modeling-framework.md
tags:
- data-science
- ab-testing
- experimentation
- statistical-analysis
title: A/B Testing & Experimentation Design Framework
use_cases:
- Creating comprehensive framework for designing and executing controlled experiments
  including a/b testing, multivariate testing, statistical analysis, power calculations,
  and decision-making based on experimental results.
- Project planning and execution
- Strategy development
industries:
- government
- healthcare
- technology
type: template
difficulty: intermediate
slug: experimentation-design
---

# A/B Testing & Experimentation Design Framework

## Purpose
Comprehensive framework for designing and executing controlled experiments including A/B testing, multivariate testing, statistical analysis, power calculations, and decision-making based on experimental results.

## Quick Experiment Prompt
Design an A/B test for [feature/change] targeting [primary metric]. Calculate sample size needed for [X]% minimum detectable effect at 95% confidence and 80% power. Define control vs. variant groups, randomization unit, test duration, primary and guardrail metrics, and decision criteria. Include risk mitigation for negative impact scenarios.

## Quick Start

**Need to design an A/B test quickly?** Use this minimal example:

### Minimal Example
```
Design A/B test for checkout page redesign to increase conversion rate from 3.5% to 4.0%. Need 100K users per variant for 95% confidence and 80% power. Test duration: 2 weeks. Primary metric: conversion rate. Guardrail metrics: average order value, page load time. Track by user, randomize at session level.
```

### When to Use This
- Testing product changes, features, or UX improvements
- Optimizing conversion rates, engagement, or revenue
- Making data-driven product decisions
- Validating hypotheses before full rollout

### Basic 3-Step Workflow
1. **Define hypothesis** - What you're testing, expected impact, success criteria
2. **Calculate sample size** - Users needed, test duration, significance level
3. **Analyze results** - Statistical significance, practical significance, decision

**Time to complete**: 2-4 hours for design, 1-4 weeks for execution, 1-2 days for analysis

---

## Template

Design experiment for [EXPERIMENT_NAME] testing [HYPOTHESIS] with [SAMPLE_SIZE] users, [VARIANT_COUNT] variants, [DURATION] test duration, targeting [SIGNIFICANCE_LEVEL] significance level, [POWER_TARGET]% statistical power, and [MDE] minimum detectable effect.

### 1. Experiment Strategy & Hypothesis

| **Experiment Component** | **Current State** | **Hypothesis** | **Expected Impact** | **Risk Assessment** | **Success Criteria** |
|------------------------|-----------------|--------------|-------------------|-------------------|-------------------|
| Primary Metric | [PRIMARY_CURRENT] | [PRIMARY_HYPOTHESIS] | [PRIMARY_IMPACT] | [PRIMARY_RISK] | [PRIMARY_SUCCESS] |
| Secondary Metrics | [SECONDARY_CURRENT] | [SECONDARY_HYPOTHESIS] | [SECONDARY_IMPACT] | [SECONDARY_RISK] | [SECONDARY_SUCCESS] |
| Guardrail Metrics | [GUARDRAIL_CURRENT] | [GUARDRAIL_HYPOTHESIS] | [GUARDRAIL_IMPACT] | [GUARDRAIL_RISK] | [GUARDRAIL_SUCCESS] |
| User Experience | [UX_CURRENT] | [UX_HYPOTHESIS] | [UX_IMPACT] | [UX_RISK] | [UX_SUCCESS] |
| Business Impact | [BUSINESS_CURRENT] | [BUSINESS_HYPOTHESIS] | [BUSINESS_IMPACT] | [BUSINESS_RISK] | [BUSINESS_SUCCESS] |
| Technical Feasibility | [TECH_CURRENT] | [TECH_HYPOTHESIS] | [TECH_IMPACT] | [TECH_RISK] | [TECH_SUCCESS] |

### 2. Statistical Design & Power Analysis

**Experiment Design Framework:**
```
Sample Size Calculation:
- Baseline Conversion: [BASELINE_RATE]%
- Minimum Detectable Effect: [MDE]%
- Statistical Power: [POWER]%
- Significance Level (α): [ALPHA]
- Test Type: [TEST_TYPE]
- Required Sample Size: [SAMPLE_SIZE]

Randomization Strategy:
- Randomization Unit: [RANDOM_UNIT]
- Assignment Method: [ASSIGN_METHOD]
- Stratification Variables: [STRATIFY_VARS]
- Block Randomization: [BLOCK_RANDOM]
- Balance Checks: [BALANCE_CHECKS]
- Spillover Control: [SPILLOVER_CONTROL]

### Duration Planning
- Minimum Duration: [MIN_DURATION]
- Maximum Duration: [MAX_DURATION]
- Weekly Sample: [WEEKLY_SAMPLE]
- Seasonality Factors: [SEASONALITY]
- Early Stopping Rules: [EARLY_STOP]
- Extension Criteria: [EXTENSION_CRITERIA]

### Multiple Testing Correction
- Number of Comparisons: [NUM_COMPARISONS]
- Correction Method: [CORRECTION_METHOD]
- Adjusted α: [ADJUSTED_ALPHA]
- Family-wise Error Rate: [FWER]
- False Discovery Rate: [FDR]
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[EXPERIMENT_NAME]` | Name of the experiment | "Checkout Flow Optimization", "Homepage Redesign Test", "Pricing Model A/B Test", "Onboarding Flow Experiment" |
| `[HYPOTHESIS]` | Hypothesis being tested | "Simplified checkout will increase conversion by 5%", "New CTA button color will improve CTR", "Dynamic pricing will increase revenue without hurting satisfaction" |
| `[SAMPLE_SIZE]` | Required sample size per variant | "50,000 users", "100K per variant", "25,000 sessions", "10K new users per arm" |
| `[VARIANT_COUNT]` | Number of experiment variants | "2 (A/B)", "3 (A/B/C)", "4 (multivariate)", "5 (factorial design)" |
| `[DURATION]` | Experiment duration | "2 weeks", "30 days", "6 weeks", "14 days minimum" |
| `[SIGNIFICANCE_LEVEL]` | Statistical significance level (alpha) | "0.05", "0.01", "0.10", "0.05 (two-tailed)" |
| `[POWER_TARGET]` | Target statistical power | "80%", "90%", "85%", "80% minimum" |
| `[MDE]` | Minimum detectable effect | "2% relative lift", "5% absolute change", "0.5pp conversion increase", "10% improvement" |
| `[PRIMARY_CURRENT]` | Current primary metric value | "3.5% conversion rate", "12% CTR", "$45 AOV", "68% D7 retention" |
| `[PRIMARY_HYPOTHESIS]` | Primary metric hypothesis | "Treatment will increase conversion from 3.5% to 4.0%", "CTR will improve by 15%", "AOV will increase by $5" |
| `[PRIMARY_IMPACT]` | Expected primary metric impact | "+0.5pp conversion (+$2M/year)", "+15% CTR", "+$5 AOV (+$10M annual)", "+5% retention" |
| `[PRIMARY_RISK]` | Primary metric risk assessment | "Low - reversible change", "Medium - user habit disruption", "High - revenue sensitive", "Low - isolated feature" |
| `[PRIMARY_SUCCESS]` | Primary metric success criteria | "Statistically significant lift >2%", "p<0.05 with >3% lift", "95% CI excludes zero", "MDE achieved at 80% power" |
| `[SECONDARY_CURRENT]` | Current secondary metrics | "Bounce rate: 45%, Time on page: 2.5min", "Add-to-cart: 8%, Wishlist: 3%", "Sessions/user: 4.2, Pages/session: 5.8" |
| `[SECONDARY_HYPOTHESIS]` | Secondary metrics hypothesis | "Engagement metrics will remain stable or improve", "Secondary KPIs neutral or positive", "No degradation in related metrics" |
| `[SECONDARY_IMPACT]` | Expected secondary impact | "Neutral to +5% engagement", "Slight improvement in time-on-site", "Maintain or improve NPS" |
| `[SECONDARY_RISK]` | Secondary metrics risk | "Low - independent of primary", "Medium - correlated with primary", "Low - informational only" |
| `[SECONDARY_SUCCESS]` | Secondary success criteria | "No significant degradation (>5% drop)", "Within historical variance", "Directionally positive" |
| `[GUARDRAIL_CURRENT]` | Current guardrail metric values | "Page load: 2.1s, Error rate: 0.1%, Revenue/user: $12", "NPS: 45, Support tickets: 100/day" |
| `[GUARDRAIL_HYPOTHESIS]` | Guardrail hypothesis | "No negative impact on performance or errors", "User experience maintained", "Revenue protected" |
| `[GUARDRAIL_IMPACT]` | Expected guardrail impact | "Neutral (within 5% threshold)", "No degradation expected", "Maintain current levels" |
| `[GUARDRAIL_RISK]` | Guardrail risk assessment | "Low - architectural change minimal", "Medium - new code paths", "High - payment flow change" |
| `[GUARDRAIL_SUCCESS]` | Guardrail success criteria | "No statistically significant degradation", "Within +/-5% of baseline", "Error rate <0.5%" |
| `[UX_CURRENT]` | Current UX metrics | "Task completion: 78%, Satisfaction: 4.2/5, Usability score: 72", "SUS score: 68, CSAT: 85%" |
| `[UX_HYPOTHESIS]` | UX improvement hypothesis | "New design improves task completion by 10%", "Reduced friction increases satisfaction", "Simpler flow improves usability" |
| `[UX_IMPACT]` | Expected UX impact | "+10% task completion", "+0.3 satisfaction score", "+8 SUS points", "Reduced support inquiries" |
| `[UX_RISK]` | UX change risk | "Low - incremental change", "Medium - navigation change", "High - major redesign", "Low - A/B testable" |
| `[UX_SUCCESS]` | UX success criteria | "Usability score improvement", "Positive qualitative feedback", "Reduced user complaints", "Task time reduction" |
| `[BUSINESS_CURRENT]` | Current business metrics | "Revenue: $10M/month, Profit margin: 25%, CAC: $45", "LTV: $150, Churn: 5%/month" |
| `[BUSINESS_HYPOTHESIS]` | Business impact hypothesis | "Treatment will increase revenue without hurting margins", "LTV improvement through better engagement" |
| `[BUSINESS_IMPACT]` | Expected business impact | "+$2M annual revenue", "+5% margin improvement", "-10% CAC", "+15% LTV" |
| `[BUSINESS_RISK]` | Business risk assessment | "Medium - revenue at risk during test", "Low - isolated segment", "High - core funnel change" |
| `[BUSINESS_SUCCESS]` | Business success criteria | "Positive ROI within 6 months", "Revenue lift covers implementation cost", "Margin maintained or improved" |
| `[TECH_CURRENT]` | Current technical state | "Page load: 2.1s, API latency: 150ms, Uptime: 99.9%", "Error rate: 0.1%, Mobile performance: 75/100" |
| `[TECH_HYPOTHESIS]` | Technical hypothesis | "New implementation maintains performance SLAs", "No degradation in system reliability" |
| `[TECH_IMPACT]` | Expected technical impact | "Neutral performance", "Slight latency increase <50ms", "Memory usage +10%", "No infrastructure changes" |
| `[TECH_RISK]` | Technical risk assessment | "Low - feature flag isolated", "Medium - database changes", "High - third-party dependency", "Low - client-side only" |
| `[TECH_SUCCESS]` | Technical success criteria | "Performance within SLA", "Error rate <0.5%", "No P1 incidents", "Deployment success rate 100%" |
| `[BASELINE_RATE]` | Baseline metric rate before experiment | "3.5%", "12%", "0.08", "25% conversion", "4.2 sessions/user" |
| `[POWER]` | Statistical power for detection | "80%", "90%", "85%", "0.80" |
| `[ALPHA]` | Type I error rate (significance level) | "0.05", "0.01", "0.10", "5%", "0.05 two-sided" |
| `[TEST_TYPE]` | Type of statistical test | "Two-sample t-test", "Chi-square", "Mann-Whitney U", "Z-test for proportions", "Bayesian A/B" |
| `[RANDOM_UNIT]` | Unit of randomization | "User ID", "Session ID", "Device ID", "Cookie", "Household", "Geographic cluster" |
| `[ASSIGN_METHOD]` | Assignment methodology | "Simple random", "Stratified random", "Deterministic hash", "Weighted assignment", "Multi-arm bandit" |
| `[STRATIFY_VARS]` | Stratification variables | "Country, Platform, User tenure", "New vs returning, Device type", "Subscription tier, Region" |
| `[BLOCK_RANDOM]` | Block randomization approach | "By week cohort", "By geography", "By user segment", "Time-based blocks", "None (simple random)" |
| `[BALANCE_CHECKS]` | Pre-experiment balance checks | "Chi-square for categoricals, t-test for continuous", "Covariate balance tests", "SRM check within 24hrs" |
| `[SPILLOVER_CONTROL]` | Spillover/interference control | "User-level isolation", "Geographic clustering", "Network randomization", "Time-based separation", "None expected" |
| `[MIN_DURATION]` | Minimum experiment duration | "7 days", "14 days (2 full weeks)", "21 days", "1 business cycle" |
| `[MAX_DURATION]` | Maximum experiment duration | "30 days", "6 weeks", "8 weeks", "90 days hard cap" |
| `[WEEKLY_SAMPLE]` | Weekly sample accumulation | "50K users/week", "10K conversions/week", "100K sessions/week", "Based on traffic forecast" |
| `[SEASONALITY]` | Seasonality considerations | "Avoid holiday periods", "Account for day-of-week effects", "Include full month cycle", "Control for promotions" |
| `[EARLY_STOP]` | Early stopping rules | "O'Brien-Fleming boundaries", "Harm threshold at p<0.01 for degradation", "Sequential testing with alpha-spending", "No early stopping" |
| `[EXTENSION_CRITERIA]` | Experiment extension criteria | "If power <80% at planned end", "Inconclusive results at primary endpoint", "Seasonal impact detected", "Technical issues resolved" |
| `[NUM_COMPARISONS]` | Number of statistical comparisons | "1 (primary only)", "5 (primary + 4 secondary)", "10 (including segments)", "3 variants = 3 comparisons" |
| `[CORRECTION_METHOD]` | Multiple comparison correction | "Bonferroni", "Benjamini-Hochberg", "Holm-Bonferroni", "Hierarchical testing", "No correction (primary pre-specified)" |
| `[ADJUSTED_ALPHA]` | Adjusted significance level | "0.025 (Bonferroni for 2)", "0.01", "0.017 (3 comparisons)", "Sequential alpha-spending" |
| `[FWER]` | Family-wise error rate | "0.05", "0.10", "Controlled at 5%", "Per-comparison 0.05" |
| `[FDR]` | False discovery rate control | "0.05", "0.10", "Benjamini-Hochberg at 5%", "Not applicable (single primary)" |
| `[CONTROL_DESC]` | Control group description | "Current production experience", "Existing checkout flow", "Original homepage design", "Baseline without feature" |
| `[CONTROL_CHANGES]` | Control group changes | "None - unchanged from current", "No modifications", "Status quo maintained", "Existing implementation" |
| `[CONTROL_IMPL]` | Control implementation details | "Feature flag OFF", "Default code path", "No new code deployed", "Existing production version" |
| `[CONTROL_TRACK]` | Control tracking requirements | "Standard analytics events", "Existing tracking maintained", "Control exposure logged", "Attribution to control arm" |
| `[CONTROL_QA]` | Control QA verification | "Verify baseline behavior", "No regression from prod", "Tracking validation", "Cross-browser testing" |
| `[VARIANT_A_DESC]` | Variant A description | "Simplified 1-step checkout", "Green CTA button", "New onboarding flow", "Personalized recommendations" |
| `[VARIANT_A_CHANGES]` | Variant A changes from control | "Collapsed address form", "Button color #00AA00", "3-step wizard removed", "ML model integration" |
| `[VARIANT_A_IMPL]` | Variant A implementation | "Feature flag variant_a=true", "CSS override + React component", "New page route /checkout-v2", "API endpoint switch" |
| `[VARIANT_A_TRACK]` | Variant A tracking | "New events: step_completion, form_interaction", "Button click tracking", "Funnel events added", "Exposure logging" |
| `[VARIANT_A_QA]` | Variant A QA requirements | "Full regression suite", "Mobile/desktop testing", "Edge case validation", "Performance benchmark" |
| `[VARIANT_B_DESC]` | Variant B description | "Progressive checkout with save", "Blue CTA with animation", "Video onboarding", "Category-based recommendations" |
| `[VARIANT_B_CHANGES]` | Variant B changes from control | "Auto-save form state", "Animated button + #0066CC", "Video tutorial added", "Category affinity model" |
| `[VARIANT_B_IMPL]` | Variant B implementation | "Feature flag variant_b=true", "Animation library added", "Video player component", "Alternate ML endpoint" |
| `[VARIANT_B_TRACK]` | Variant B tracking | "Save state events", "Animation interaction", "Video engagement metrics", "Recommendation clicks" |
| `[VARIANT_B_QA]` | Variant B QA requirements | "State persistence testing", "Animation performance", "Video playback validation", "Model output verification" |
| `[VARIANT_C_DESC]` | Variant C description | "Guest checkout option", "Orange high-contrast CTA", "Interactive onboarding quiz", "Trending items recommendations" |
| `[VARIANT_C_CHANGES]` | Variant C changes | "Skip registration option", "High contrast design", "Quiz-based personalization", "Popularity-based model" |
| `[VARIANT_C_IMPL]` | Variant C implementation | "Feature flag variant_c=true", "Accessibility update", "Quiz component", "Trending API integration" |
| `[VARIANT_C_TRACK]` | Variant C tracking | "Guest vs registered path", "Accessibility interactions", "Quiz completion rate", "Trending engagement" |
| `[VARIANT_C_QA]` | Variant C QA requirements | "Guest flow E2E testing", "WCAG compliance check", "Quiz logic validation", "API response validation" |
| `[VARIANT_D_DESC]` | Variant D description | "Express checkout (1-click)", "Minimalist CTA design", "AI-guided onboarding", "Hybrid recommendation model" |
| `[VARIANT_D_CHANGES]` | Variant D changes | "Saved payment 1-click", "Reduced visual elements", "Conversational AI guide", "Ensemble model approach" |
| `[VARIANT_D_IMPL]` | Variant D implementation | "Feature flag variant_d=true", "Payment tokenization", "Chatbot integration", "Multi-model orchestration" |
| `[VARIANT_D_TRACK]` | Variant D tracking | "1-click conversion events", "Minimal UI interactions", "AI conversation logs", "Model blend attribution" |
| `[VARIANT_D_QA]` | Variant D QA requirements | "Payment security testing", "Visual regression", "AI response validation", "Model performance testing" |
| `[HOLDOUT_DESC]` | Holdout group description | "Long-term baseline population", "Feature-excluded control", "Clean measurement group", "Cumulative effect measurement" |
| `[HOLDOUT_CHANGES]` | Holdout changes | "Excluded from all related experiments", "No new features", "Permanent control state", "Isolated from treatments" |
| `[HOLDOUT_IMPL]` | Holdout implementation | "Separate holdout flag", "Excluded from feature rollouts", "Sticky assignment", "Cross-experiment exclusion" |
| `[HOLDOUT_TRACK]` | Holdout tracking | "Full funnel metrics", "Long-term engagement", "Cumulative exposure logging", "Clean baseline metrics" |
| `[HOLDOUT_QA]` | Holdout QA requirements | "Verify no treatment leakage", "Assignment persistence check", "Exclusion validation", "Baseline stability testing" |
| `[PRIMARY_DEFINITION]` | Primary metric definition | "Conversion rate = Orders / Unique visitors", "CTR = Clicks / Impressions", "D7 Retention = Users active day 7 / Day 0 users" |
| `[PRIMARY_CALC]` | Primary metric calculation method | "COUNT(orders) / COUNT(DISTINCT user_id)", "SUM(clicks) / SUM(impressions)", "Rolling 7-day average" |
| `[PRIMARY_SOURCE]` | Primary metric data source | "Snowflake analytics.conversions table", "Google Analytics", "Amplitude events", "Internal data warehouse" |
| `[PRIMARY_WINDOW]` | Primary metric measurement window | "Per-session", "7-day attribution window", "28-day conversion window", "Same-day only" |
| `[PRIMARY_THRESHOLD]` | Primary metric success threshold | ">2% relative lift", "p<0.05 with positive effect", "+0.5pp absolute improvement", "95% CI excludes zero" |
| `[PRIMARY_TEST]` | Primary metric statistical test | "Two-proportion z-test", "Welch's t-test", "Mann-Whitney U", "Bayesian posterior probability" |
| `[ENGAGE_METRICS]` | Engagement secondary metrics | "Time on site, Pages per session, Scroll depth, Feature usage", "DAU, WAU, MAU, Sessions per user" |
| `[REVENUE_METRICS]` | Revenue secondary metrics | "AOV, Revenue per user, Basket size, Upsell rate", "GMV, Take rate, Commission revenue" |
| `[RETENTION_METRICS]` | Retention secondary metrics | "D1, D7, D30 retention, Churn rate, Reactivation rate", "Subscription renewal, LTV projection" |
| `[QUALITY_METRICS]` | Quality secondary metrics | "Task completion rate, Error rate, Support tickets, Returns rate", "Refund rate, NPS, CSAT" |
| `[OPERATIONAL_METRICS]` | Operational secondary metrics | "Page load time, API latency, Server errors, Availability", "Processing time, Queue length" |
| `[SATISFACTION_METRICS]` | User satisfaction metrics | "NPS score, CSAT rating, CES score, App store rating", "Survey responses, Feedback sentiment" |
| `[PERF_GUARDRAIL]` | Performance guardrail metrics | "Page load <3s, LCP <2.5s, FID <100ms, CLS <0.1", "API p99 latency <500ms" |
| `[ERROR_GUARDRAIL]` | Error rate guardrail metrics | "Error rate <0.5%, Crash rate <0.1%, API 5xx <0.1%", "Client-side errors <1%" |
| `[UX_GUARDRAIL]` | UX guardrail metrics | "Bounce rate increase <5%, Task abandonment <10%, Rage clicks <baseline", "Accessibility violations = 0" |
| `[REVENUE_GUARDRAIL]` | Revenue guardrail metrics | "Revenue per user decrease <2%, AOV decrease <5%, Refund rate increase <1pp", "No negative revenue impact" |
| `[COMPLIANCE_GUARDRAIL]` | Compliance guardrail metrics | "GDPR consent rate maintained, Cookie compliance 100%", "Accessibility WCAG AA compliance" |
| `[GUARDRAIL_LIMITS]` | Guardrail threshold limits | "Max degradation 5%, Minimum sample for alert 1000", "Auto-stop at 10% degradation" |
| `[VALIDATION_RULES]` | Data validation rules | "Non-null user_id, Valid timestamp, Known event types", "Referential integrity checks" |
| `[MISSING_DATA]` | Missing data handling strategy | "Exclude from analysis", "Multiple imputation", "Last observation carried forward", "Intent-to-treat analysis" |
| `[OUTLIER_TREATMENT]` | Outlier treatment approach | "Winsorize at 99th percentile", "Log transformation", "Exclude >3 standard deviations", "Robust statistics" |
| `[DATA_FRESHNESS]` | Data freshness requirements | "Real-time for guardrails", "T+1 for daily metrics", "Hourly refresh", "Near real-time (<5min lag)" |
| `[LOGGING_ACCURACY]` | Logging accuracy validation | ">99.5% event capture rate", "Cross-validation with server logs", "Sampling validation checks" |
| `[NEW_CRITERIA]` | New users selection criteria | "First visit within experiment window", "Account created <7 days", "No prior purchases", "First-time app install" |
| `[NEW_SAMPLE]` | New users sample size | "20K new users/week", "5K per variant", "10% of new user traffic", "Sufficient for 80% power" |
| `[NEW_RANDOM]` | New users randomization | "Hash on user_id at first exposure", "Stratified by acquisition channel", "Bucketed by signup date" |
| `[NEW_BEHAVIOR]` | New users expected behavior | "Higher sensitivity to UX changes", "Lower baseline metrics", "More variance in behavior", "Unbiased by prior experience" |
| `[NEW_ANALYSIS]` | New users analysis plan | "Separate cohort analysis", "Learning curve effects", "Compare to mature user response", "Day-over-day trends" |
| `[ACTIVE_CRITERIA]` | Active users selection criteria | "Logged in within 30 days", "2+ sessions in past week", "Made purchase in past 90 days", "DAU/MAU >0.2" |
| `[ACTIVE_SAMPLE]` | Active users sample size | "50K active users", "Largest segment", "15K per variant needed", "80% of experiment traffic" |
| `[ACTIVE_RANDOM]` | Active users randomization | "Consistent hash on user_id", "Pre-stratified by engagement tier", "Activity-balanced assignment" |
| `[ACTIVE_BEHAVIOR]` | Active users expected behavior | "Established habits", "More consistent behavior", "Sensitive to workflow changes", "Higher baseline metrics" |
| `[ACTIVE_ANALYSIS]` | Active users analysis plan | "Primary analysis population", "Habit disruption monitoring", "Long-term engagement tracking", "Revenue impact focus" |
| `[POWER_CRITERIA]` | Power users selection criteria | "Top 10% by engagement", "5+ purchases/month", "Daily active for 30+ days", "Premium tier subscribers" |
| `[POWER_SAMPLE]` | Power users sample size | "10K power users", "Smaller but high-value", "May require longer duration", "5K minimum per arm" |
| `[POWER_RANDOM]` | Power users randomization | "Stratified by value tier", "Balanced by tenure", "Revenue-weighted assignment consideration" |
| `[POWER_BEHAVIOR]` | Power users expected behavior | "Highest baseline metrics", "Most resistant to change", "Greatest revenue impact", "Vocal feedback" |
| `[POWER_ANALYSIS]` | Power users analysis plan | "Revenue impact analysis", "Qualitative feedback collection", "Churn risk monitoring", "Feature adoption depth" |
| `[MOBILE_CRITERIA]` | Mobile users selection criteria | "Mobile app users", "Mobile web sessions", "Primary device = mobile", "iOS or Android platform" |
| `[MOBILE_SAMPLE]` | Mobile users sample size | "40K mobile users", "60% of total traffic", "Platform-balanced", "Sufficient per platform" |
| `[MOBILE_RANDOM]` | Mobile users randomization | "Device ID based", "Platform-stratified", "Consistent across sessions", "Cross-device consideration" |
| `[MOBILE_BEHAVIOR]` | Mobile users expected behavior | "Shorter sessions", "Touch interactions", "Performance sensitive", "Notification responsive" |
| `[MOBILE_ANALYSIS]` | Mobile users analysis plan | "Platform-specific analysis", "Performance metrics priority", "App store rating monitoring", "Mobile-specific UX metrics" |
| `[GEO_CRITERIA]` | Geographic segment criteria | "Country/region based", "Timezone clustering", "Market maturity", "Regulatory zones (EU/US/APAC)" |
| `[GEO_SAMPLE]` | Geographic segment sample size | "US: 30K, EU: 15K, APAC: 10K", "Proportional to traffic", "Minimum 5K per major region" |
| `[GEO_RANDOM]` | Geographic segment randomization | "Within-region randomization", "Market-level clustering", "Time zone balanced exposure" |
| `[GEO_BEHAVIOR]` | Geographic segment expected behavior | "Cultural/UX preferences vary", "Payment method differences", "Language/localization effects", "Regulatory constraints" |
| `[GEO_ANALYSIS]` | Geographic segment analysis plan | "Region-specific lift estimation", "Heterogeneous treatment effects", "Market-level decisions", "Localization insights" |
| `[CUSTOM_CRITERIA]` | Custom segment criteria | "Business-defined cohort", "Propensity score matched", "Behavioral clustering", "Customer lifecycle stage" |
| `[CUSTOM_SAMPLE]` | Custom segment sample size | "Based on segment definition", "Ensure sufficient power", "May require extended duration", "Quota-based sampling" |
| `[CUSTOM_RANDOM]` | Custom segment randomization | "Stratified within segment", "Propensity score blocking", "Matched pair design", "Segment-specific hash" |
| `[CUSTOM_BEHAVIOR]` | Custom segment expected behavior | "Defined by segment hypothesis", "Expected differential response", "Targeted use case behavior", "Hypothesis-specific metrics" |
| `[CUSTOM_ANALYSIS]` | Custom segment analysis plan | "Pre-registered subgroup analysis", "Interaction effect testing", "Segment-specific success criteria", "Targeting validation" |
| `[PRE_TIMELINE]` | Pre-launch phase timeline | "Day -7 to Day -1", "1 week before launch", "T-5 days", "Pre-experiment week" |
| `[PRE_ACTIVITIES]` | Pre-launch activities | "Feature flag setup, QA testing, Tracking validation, Stakeholder alignment", "Documentation, Code review, Load testing" |
| `[PRE_CHECKS]` | Pre-launch checkpoints | "Tracking accuracy verified, Feature parity confirmed, Rollback tested, Stakeholder sign-off" |
| `[PRE_CRITERIA]` | Pre-launch go/no-go criteria | "All QA tests pass, Tracking validated, No blocking bugs, Stakeholder approval received" |
| `[PRE_ROLLBACK]` | Pre-launch rollback plan | "Delay launch if issues found", "Fix and retest", "Escalate blockers immediately", "Update timeline if needed" |
| `[SOFT_TIMELINE]` | Soft launch phase timeline | "Day 1-2", "48 hours", "First 2 days", "Initial exposure period" |
| `[SOFT_ACTIVITIES]` | Soft launch activities | "1% traffic exposure, Real-time monitoring, Bug triage, Stakeholder updates", "Guardrail metric validation" |
| `[SOFT_CHECKS]` | Soft launch checkpoints | "No critical bugs, Guardrails green, Data flowing correctly, User feedback review" |
| `[SOFT_CRITERIA]` | Soft launch go/no-go criteria | "Error rate <0.5%, No P1 issues, Data quality confirmed, Metrics logging correctly" |
| `[SOFT_ROLLBACK]` | Soft launch rollback plan | "Immediate 0% traffic if P1 issue", "Feature flag kill switch", "Automatic rollback triggers configured" |
| `[RAMP_TIMELINE]` | Ramp-up phase timeline | "Day 3-7", "Week 1", "5 days ramp", "Gradual increase period" |
| `[RAMP_ACTIVITIES]` | Ramp-up activities | "Increase to 10%, 25%, 50% traffic, Daily monitoring, Bug fixes, Performance checks", "Sample size accumulation" |
| `[RAMP_CHECKS]` | Ramp-up checkpoints | "Metrics stable at each stage", "Performance within SLA", "No regression detected", "Sufficient sample accumulating" |
| `[RAMP_CRITERIA]` | Ramp-up go/no-go criteria | "Guardrails stable, No degradation trends, Technical metrics green, On track for target sample" |
| `[RAMP_ROLLBACK]` | Ramp-up rollback plan | "Roll back to previous ramp level", "Pause at current level to investigate", "Full rollback if >5% degradation" |
| `[FULL_TIMELINE]` | Full launch phase timeline | "Day 8-21", "2 weeks at full traffic", "Days 8-14", "Full exposure period" |
| `[FULL_ACTIVITIES]` | Full launch activities | "50/50 traffic split, Statistical monitoring, Interim analysis, Stakeholder reporting", "Sample size completion" |
| `[FULL_CHECKS]` | Full launch checkpoints | "Sample size on track, No early stopping triggered, Metrics within expected range", "Weekly status updates" |
| `[FULL_CRITERIA]` | Full launch go/no-go criteria | "Continue if no harm detected", "Stop early if significant harm", "Extend if underpowered" |
| `[FULL_ROLLBACK]` | Full launch rollback plan | "Immediate rollback if harm detected", "Preserve data for analysis", "Post-incident review" |
| `[MONITOR_TIMELINE]` | Monitoring phase timeline | "Continuous during experiment", "Daily checks", "Real-time dashboards", "Throughout experiment duration" |
| `[MONITOR_ACTIVITIES]` | Monitoring activities | "Dashboard review, Alert triage, Data quality checks, Stakeholder updates", "Guardrail metric tracking" |
| `[MONITOR_CHECKS]` | Monitoring checkpoints | "Daily metric review, Weekly stakeholder update, SRM checks, Balance validation" |
| `[MONITOR_CRITERIA]` | Monitoring success criteria | "All guardrails green", "No data quality issues", "Sample accumulation on track", "No anomalies detected" |
| `[MONITOR_ROLLBACK]` | Monitoring rollback triggers | "Automatic alert on guardrail breach", "SRM >0.01 triggers investigation", "Manual escalation path defined" |
| `[CONCLUDE_TIMELINE]` | Conclusion phase timeline | "Day 22-25", "Final week", "Post-experiment period", "3-5 days for analysis" |
| `[CONCLUDE_ACTIVITIES]` | Conclusion activities | "Final analysis, Statistical tests, Report generation, Decision meeting, Documentation" |
| `[CONCLUDE_CHECKS]` | Conclusion checkpoints | "Data completeness verified, All analyses run, Results validated, Peer review completed" |
| `[CONCLUDE_CRITERIA]` | Conclusion success criteria | "Sufficient power achieved", "Primary endpoint analyzed", "Decision documented", "Learnings captured" |
| `[CONCLUDE_ROLLBACK]` | Conclusion rollback options | "Extend experiment if underpowered", "Follow-up experiment if inconclusive", "Ship winning variant or rollback to control" |
| `[PRIMARY_STAT_TEST]` | Primary statistical test | "Two-sample z-test for proportions", "Welch's t-test", "Chi-square test", "Mann-Whitney U for non-normal data" |
| `[EFFECT_SIZE]` | Effect size calculation | "Cohen's d", "Relative lift = (Treatment - Control) / Control", "Absolute difference", "Risk ratio" |
| `[CONFIDENCE_INT]` | Confidence interval calculation | "95% CI using bootstrap", "Agresti-Coull interval for proportions", "Percentile bootstrap CI", "Wilson score interval" |
| `[P_VALUE_THRESH]` | P-value threshold for significance | "p < 0.05", "p < 0.01 for high stakes", "p < 0.10 for exploratory", "One-sided p < 0.025" |
| `[PRACTICAL_SIG]` | Practical significance threshold | "Minimum 2% lift for business impact", "$100K annual revenue threshold", "1pp absolute improvement", "ROI positive within 6 months" |
| `[PRIMARY_INTERPRET]` | Primary result interpretation | "Statistically significant + practically meaningful = Ship", "Significant but small = Consider costs", "Not significant = Do not ship" |
| `[SUBGROUP_ANALYSIS]` | Subgroup analysis approach | "Pre-registered segments only", "New vs existing users, Mobile vs desktop, Geography", "Exploratory with adjusted alpha" |
| `[INTERACTION_EFFECTS]` | Interaction effects analysis | "Treatment x segment interaction testing", "Heterogeneous treatment effects", "Factorial ANOVA for multivariate" |
| `[TIME_SERIES]` | Time series analysis approach | "Day-over-day effect stability", "Novelty/primacy effect detection", "Cumulative metric tracking", "Time trend regression" |
| `[COHORT_ANALYSIS]` | Cohort analysis plan | "Weekly cohort comparison", "Entry cohort retention curves", "First exposure cohort tracking", "Maturation effects" |
| `[FUNNEL_ANALYSIS]` | Funnel analysis approach | "Step-by-step conversion analysis", "Drop-off point identification", "Funnel velocity metrics", "Bottleneck detection" |
| `[LONGTERM_EFFECTS]` | Long-term effect analysis | "28-day, 60-day, 90-day holdout comparison", "LTV projection", "Retention curve extrapolation", "Cumulative effect estimation" |
| `[BAYESIAN_ANALYSIS]` | Bayesian analysis approach | "Beta-binomial for proportions", "Posterior probability of being best", "Expected loss calculation", "Credible intervals" |
| `[SEQUENTIAL_TEST]` | Sequential testing methodology | "O'Brien-Fleming boundaries", "Alpha spending function", "Group sequential design", "Continuous monitoring bounds" |
| `[VARIANCE_REDUCE]` | Variance reduction techniques | "CUPED (pre-experiment covariate adjustment)", "Stratified sampling", "Control variates", "Difference-in-differences" |
| `[CAUSAL_INFERENCE]` | Causal inference methods | "Intent-to-treat analysis", "Instrumental variables", "Regression discontinuity", "Propensity score matching" |
| `[ML_METHODS]` | Machine learning analysis methods | "Causal forests for heterogeneous effects", "CATE estimation", "Uplift modeling", "Feature importance for segmentation" |
| `[NETWORK_EFFECTS]` | Network effects handling | "Cluster randomization", "Ego-network analysis", "Interference modeling", "Spatial regression models" |
| `[SENSITIVITY]` | Sensitivity analysis plan | "Varying thresholds", "Exclude outliers analysis", "Intent-to-treat vs per-protocol", "Multiple imputation sensitivity" |
| `[BALANCE_TESTS]` | Balance/covariate checks | "Chi-square for categoricals", "t-test for continuous", "Standardized mean differences", "Pre-experiment metric comparison" |
| `[MANIPULATION]` | Manipulation check approach | "Verify treatment delivery", "Exposure logging validation", "Feature visibility confirmation", "User awareness survey" |
| `[SRM_CHECK]` | Sample ratio mismatch check | "Chi-square test on sample sizes", "Expected vs actual ratio comparison", "Daily SRM monitoring", "Alert if p < 0.01" |
| `[NOVELTY_CHECK]` | Novelty effect detection | "Time-windowed analysis", "New vs returning user split", "Effect decay over time", "Learning curve adjustment" |
| `[SELECTION_CHECK]` | Selection bias validation | "Pre-treatment covariate balance", "Attrition analysis", "Survivor bias check", "Non-compliance analysis" |
| `[SYSTEM_METRICS]` | System health monitoring metrics | "API latency p99, Error rate, CPU/Memory utilization, Request throughput", "Page load time, Server availability" |
| `[SYSTEM_THRESH]` | System health thresholds | "Latency <500ms, Error rate <0.5%, CPU <80%", "Page load <3s, Availability >99.9%" |
| `[SYSTEM_ALERTS]` | System health alert conditions | "Alert if latency >1s for 5min", "Page if error rate >2%", "Warning at 80% threshold" |
| `[SYSTEM_RESPONSE]` | System health response actions | "Automated scaling trigger", "On-call notification", "Traffic reduction to variant", "Incident ticket creation" |
| `[SYSTEM_ESCALATE]` | System health escalation path | "L1 On-call > L2 Engineering > Engineering Manager > VP Engineering", "SLA: 15min response" |
| `[DATA_METRICS]` | Data quality monitoring metrics | "Event logging rate, Missing data percentage, Duplicate events, Schema violations", "Data freshness" |
| `[DATA_THRESH]` | Data quality thresholds | "Logging rate >99%, Missing <1%, Duplicates <0.1%", "Freshness <1hr, Schema compliance 100%" |
| `[DATA_ALERTS]` | Data quality alert conditions | "Alert if logging drops >5%", "Alert on schema violations", "Warning if freshness >2hr" |
| `[DATA_RESPONSE]` | Data quality response actions | "Investigate data pipeline", "Check tracking implementation", "Validate data source", "Pause experiment if severe" |
| `[DATA_ESCALATE]` | Data quality escalation path | "Data Engineer > Analytics Manager > Data Science Lead", "SLA: 1hr investigation start" |
| `[UX_METRICS]` | UX monitoring metrics | "Bounce rate, Task completion, Rage clicks, Time to interact, Accessibility errors", "User complaints" |
| `[UX_THRESH]` | UX metric thresholds | "Bounce rate increase <10%, Task completion decrease <5%", "Rage clicks <baseline, Accessibility 100%" |
| `[UX_ALERTS]` | UX alert conditions | "Alert if bounce rate +15%", "Alert on accessibility violations", "Warning on high rage click areas" |
| `[UX_RESPONSE]` | UX response actions | "UX review triggered", "Qualitative user feedback collection", "Hotjar/FullStory session review", "Accessibility audit" |
| `[UX_ESCALATE]` | UX escalation path | "UX Designer > UX Manager > Product Manager", "SLA: 24hr review" |
| `[STAT_METRICS]` | Statistical validity metrics | "Sample ratio (SRM), Effect size trend, Variance stability, P-value trajectory", "Power accumulation" |
| `[STAT_THRESH]` | Statistical validity thresholds | "SRM p>0.01, Variance within 2x historical", "Effect size stable within CI", "On track for target power" |
| `[STAT_ALERTS]` | Statistical validity alerts | "Alert if SRM p<0.01", "Warning if underpowered at midpoint", "Alert on unexpected variance spike" |
| `[STAT_RESPONSE]` | Statistical validity response | "Investigate randomization", "Check for bot traffic", "Review data pipeline", "Consider experiment extension" |
| `[STAT_ESCALATE]` | Statistical validity escalation | "Data Scientist > Analytics Manager > Experimentation Lead", "SLA: Same day investigation" |
| `[BUS_METRICS]` | Business impact metrics | "Revenue per user, Conversion rate, AOV, Customer acquisition cost", "LTV indicators, Margin impact" |
| `[BUS_THRESH]` | Business impact thresholds | "Revenue decline <5%, Conversion decline <3%", "AOV within 10% of baseline", "CAC increase <10%" |
| `[BUS_ALERTS]` | Business impact alerts | "Alert if revenue -10% significant", "Warning at -5% trend", "Daily revenue variance report" |
| `[BUS_RESPONSE]` | Business impact response | "Stakeholder notification", "Impact assessment meeting", "Consider early stopping", "Mitigation plan development" |
| `[BUS_ESCALATE]` | Business impact escalation | "Product Manager > Director > VP Product > C-Suite", "SLA: 4hr for significant impact" |
| `[ETHICAL_METRICS]` | Ethical monitoring metrics | "User complaints, Support ticket themes, Bias indicators, Vulnerable population impact", "Consent compliance" |
| `[ETHICAL_THRESH]` | Ethical concern thresholds | "No harm to vulnerable groups", "Complaint rate increase <50%", "Bias metrics within fairness bounds" |
| `[ETHICAL_ALERTS]` | Ethical concern alerts | "Alert on user harm reports", "Alert on bias detection", "Warning on consent issues" |
| `[ETHICAL_RESPONSE]` | Ethical concern response | "Immediate ethics review", "User outreach if needed", "Treatment modification or stop", "Documentation for review board" |
| `[ETHICAL_ESCALATE]` | Ethical concern escalation | "Ethics Committee > Legal > Executive Team", "SLA: Immediate for harm concerns" |
| `[LAUNCH_CRITERIA]` | Launch decision criteria | "Statistically significant positive result", "p<0.05 with practical significance", "No guardrail violations", "Stakeholder alignment" |
| `[LAUNCH_STAKE]` | Launch decision stakeholders | "Product Manager, Engineering Lead, Data Science Lead, Business Owner", "Executive sponsor for high-impact" |
| `[LAUNCH_DATA]` | Launch decision data requirements | "Final statistical analysis", "Confidence intervals", "Segment breakdowns", "Long-term projections" |
| `[LAUNCH_TIME]` | Launch decision timeline | "Within 3 days of experiment end", "Decision meeting scheduled", "Same-week for time-sensitive" |
| `[LAUNCH_DOC]` | Launch decision documentation | "Decision memo with rationale", "Analysis report link", "Stakeholder sign-off record", "JIRA ticket updated" |
| `[EARLY_CRITERIA]` | Early stopping criteria | "Significant harm detected (p<0.01)", "Guardrail breach >10%", "Critical bug discovered", "External events impact" |
| `[EARLY_STAKE]` | Early stopping stakeholders | "Experiment owner, Product Manager, On-call engineer", "Executive for revenue impact" |
| `[EARLY_DATA]` | Early stopping data requirements | "Real-time guardrail metrics", "Statistical significance at current sample", "Impact magnitude estimate" |
| `[EARLY_TIME]` | Early stopping timeline | "Immediate for critical issues", "24hr review for harm signals", "Same-day decision for guardrails" |
| `[EARLY_DOC]` | Early stopping documentation | "Incident report", "Data snapshot preservation", "Decision rationale", "Post-mortem scheduled" |
| `[ROLLOUT_CRITERIA]` | Rollout decision criteria | "Positive experiment result", "No ramp-up issues at 50%", "Engineering capacity confirmed", "Monitoring in place" |
| `[ROLLOUT_STAKE]` | Rollout decision stakeholders | "Product Manager, Engineering Lead, Release Manager", "QA Lead for quality sign-off" |
| `[ROLLOUT_DATA]` | Rollout decision data requirements | "Experiment results summary", "Ramp metrics stability", "Performance benchmarks", "Risk assessment" |
| `[ROLLOUT_TIME]` | Rollout decision timeline | "1 week after experiment conclusion", "Sprint planning alignment", "Release calendar consideration" |
| `[ROLLOUT_DOC]` | Rollout decision documentation | "Release notes", "Feature documentation", "Rollback plan", "Monitoring dashboard" |
| `[ITERATE_CRITERIA]` | Iteration decision criteria | "Inconclusive results", "Positive signal but not significant", "Segment-specific success", "New hypothesis generated" |
| `[ITERATE_STAKE]` | Iteration decision stakeholders | "Product Manager, Data Scientist, UX Researcher", "Engineering for feasibility" |
| `[ITERATE_DATA]` | Iteration decision data requirements | "Exploratory analysis", "Segment deep-dives", "User feedback", "Competitive analysis" |
| `[ITERATE_TIME]` | Iteration decision timeline | "Within 2 weeks of experiment end", "Roadmap prioritization cycle", "Next sprint planning" |
| `[ITERATE_DOC]` | Iteration decision documentation | "Learnings summary", "Next experiment hypothesis", "Design iteration plan", "Backlog item created" |
| `[SCALE_CRITERIA]` | Scale decision criteria | "Proven impact at current scale", "Infrastructure readiness", "Cost/benefit positive", "Market expansion opportunity" |
| `[SCALE_STAKE]` | Scale decision stakeholders | "VP Product, Engineering Director, Finance", "Operations for capacity" |
| `[SCALE_DATA]` | Scale decision data requirements | "Impact extrapolation", "Infrastructure capacity plan", "Cost projections", "Market analysis" |
| `[SCALE_TIME]` | Scale decision timeline | "Quarterly planning cycle", "Budget approval timeline", "Resource allocation review" |
| `[SCALE_DOC]` | Scale decision documentation | "Business case document", "Scaling plan", "Resource request", "Success metrics definition" |
| `[SUNSET_CRITERIA]` | Sunset decision criteria | "Negative experiment result", "No path to improvement", "Opportunity cost too high", "Strategic pivot" |
| `[SUNSET_STAKE]` | Sunset decision stakeholders | "Product Manager, Engineering Lead, Business Owner", "Executive for significant investments" |
| `[SUNSET_DATA]` | Sunset decision data requirements | "Final experiment analysis", "Investment-to-date summary", "Alternative options assessment" |
| `[SUNSET_TIME]` | Sunset decision timeline | "Within 1 week of negative result", "Quarterly review for ongoing features", "Budget cycle alignment" |
| `[SUNSET_DOC]` | Sunset decision documentation | "Sunset decision memo", "Learnings document", "Code cleanup plan", "Stakeholder communication" |
| `[HYPOTHESIS_REG]` | Pre-registration documentation | "OSF pre-registration", "Internal experiment registry", "Confluence hypothesis doc", "GitHub experiment spec" |
| `[DESIGN_DOCS]` | Experiment design documentation | "Confluence design doc", "Technical spec in Google Docs", "JIRA epic with acceptance criteria", "Notion experiment brief" |
| `[ANALYSIS_CODE]` | Analysis code repository | "GitHub: experiments/[experiment-name]", "Jupyter notebooks in data-science repo", "dbt models in analytics repo" |
| `[RESULTS_REPO]` | Results repository location | "Experiment results database", "Confluence results wiki", "Amplitude experiment archive", "Internal knowledge base" |
| `[DECISION_LOG]` | Decision log documentation | "Decision memo in Confluence", "JIRA decision record", "Slack thread summary", "Meeting notes with rationale" |
| `[LESSONS]` | Lessons learned documentation | "Post-experiment retrospective doc", "Learnings database entry", "Team retro action items", "Knowledge base update" |
| `[WIKI_UPDATES]` | Wiki and documentation updates | "Confluence page updated", "README refreshed", "Process documentation revised", "FAQ section added" |
| `[PRESENTATIONS]` | Presentation materials | "Executive summary deck", "Technical deep-dive slides", "All-hands presentation", "Cross-team sharing session" |
| `[BEST_PRACTICES]` | Best practices documentation | "Experimentation playbook update", "Do's and don'ts list", "Template improvements", "Process refinements" |
| `[FAILURE_ANALYSIS]` | Failure analysis approach | "5-whys root cause analysis", "Failure mode documentation", "Process gap identification", "Prevention recommendations" |
| `[SUCCESS_PATTERNS]` | Success pattern recognition | "Winning experiment characteristics", "Replicable patterns identified", "Success factor documentation", "Playbook for similar experiments" |
| `[TRAINING_MAT]` | Training materials updates | "Onboarding deck updated", "Case study added", "Training module created", "Workshop materials refreshed" |
| `[CROSS_LEARNING]` | Cross-team learning approach | "Monthly experiment review meeting", "Slack channel updates", "Cross-functional presentations", "Experimentation newsletter" |
| `[PATTERN_RECOG]` | Pattern recognition insights | "Effect size database query", "Historical experiment comparison", "Trend analysis across experiments", "Meta-analysis insights" |
| `[EFFECT_DATABASE]` | Effect size database | "Historical effects repository", "Baseline effect sizes by metric", "Variance estimates archive", "Power analysis reference data" |
| `[VELOCITY_METRICS]` | Experimentation velocity metrics | "Experiments launched/month", "Time from idea to launch", "Analysis turnaround time", "Decision cycle time" |
| `[WIN_RATE]` | Win rate tracking | "30% historical win rate", "Win rate by domain", "Win rate trends over time", "Benchmark comparison" |
| `[ROI_ANALYSIS]` | ROI analysis approach | "Value delivered vs. investment", "Cumulative experiment ROI", "Cost per experiment", "Value per successful experiment" |
| `[EXP_VELOCITY]` | Experiment velocity targets | "10 experiments/quarter", "2x velocity improvement goal", "Time-to-insight <3 weeks", "Decision latency <5 days" |
| `[TOOL_OPTIMIZE]` | Tool optimization opportunities | "Automation opportunities identified", "Platform upgrades planned", "Integration improvements", "Self-service enablement" |
| `[TEAM_EFFICIENCY]` | Team efficiency metrics | "Experiments per data scientist", "Analysis time reduction", "Stakeholder self-service rate", "Repeat experiment rate reduction" |
| `[STAKE_SATISFY]` | Stakeholder satisfaction tracking | "CSAT survey results", "NPS for experimentation team", "Feedback collection process", "Improvement action items" |
| `[INNOVATION_INDEX]` | Innovation index measurement | "Novel experiment rate", "New method adoption", "Cross-domain experiments", "Strategic experiment alignment" |

### 3. Variant Design & Implementation

| **Variant** | **Description** | **Changes** | **Implementation** | **Tracking** | **Quality Assurance** |
|-----------|---------------|-----------|------------------|------------|---------------------|
| Control | [CONTROL_DESC] | [CONTROL_CHANGES] | [CONTROL_IMPL] | [CONTROL_TRACK] | [CONTROL_QA] |
| Variant A | [VARIANT_A_DESC] | [VARIANT_A_CHANGES] | [VARIANT_A_IMPL] | [VARIANT_A_TRACK] | [VARIANT_A_QA] |
| Variant B | [VARIANT_B_DESC] | [VARIANT_B_CHANGES] | [VARIANT_B_IMPL] | [VARIANT_B_TRACK] | [VARIANT_B_QA] |
| Variant C | [VARIANT_C_DESC] | [VARIANT_C_CHANGES] | [VARIANT_C_IMPL] | [VARIANT_C_TRACK] | [VARIANT_C_QA] |
| Variant D | [VARIANT_D_DESC] | [VARIANT_D_CHANGES] | [VARIANT_D_IMPL] | [VARIANT_D_TRACK] | [VARIANT_D_QA] |
| Holdout | [HOLDOUT_DESC] | [HOLDOUT_CHANGES] | [HOLDOUT_IMPL] | [HOLDOUT_TRACK] | [HOLDOUT_QA] |

### 4. Metrics & Measurement

```
Metrics Framework:
Primary Metrics:
- Metric Definition: [PRIMARY_DEFINITION]
- Calculation Method: [PRIMARY_CALC]
- Data Source: [PRIMARY_SOURCE]
- Measurement Window: [PRIMARY_WINDOW]
- Success Threshold: [PRIMARY_THRESHOLD]
- Statistical Test: [PRIMARY_TEST]

Secondary Metrics:
- Engagement Metrics: [ENGAGE_METRICS]
- Revenue Metrics: [REVENUE_METRICS]
- Retention Metrics: [RETENTION_METRICS]
- Quality Metrics: [QUALITY_METRICS]
- Operational Metrics: [OPERATIONAL_METRICS]
- User Satisfaction: [SATISFACTION_METRICS]

### Guardrail Metrics
- Performance: [PERF_GUARDRAIL]
- Error Rates: [ERROR_GUARDRAIL]
- User Experience: [UX_GUARDRAIL]
- Revenue Protection: [REVENUE_GUARDRAIL]
- Compliance: [COMPLIANCE_GUARDRAIL]
- Threshold Limits: [GUARDRAIL_LIMITS]

### Data Quality
- Validation Rules: [VALIDATION_RULES]
- Missing Data Handling: [MISSING_DATA]
- Outlier Treatment: [OUTLIER_TREATMENT]
- Data Freshness: [DATA_FRESHNESS]
- Logging Accuracy: [LOGGING_ACCURACY]
```

### 5. User Segmentation & Targeting

| **Segment** | **Selection Criteria** | **Sample Size** | **Randomization** | **Expected Behavior** | **Analysis Plan** |
|-----------|---------------------|---------------|-----------------|---------------------|------------------|
| New Users | [NEW_CRITERIA] | [NEW_SAMPLE] | [NEW_RANDOM] | [NEW_BEHAVIOR] | [NEW_ANALYSIS] |
| Active Users | [ACTIVE_CRITERIA] | [ACTIVE_SAMPLE] | [ACTIVE_RANDOM] | [ACTIVE_BEHAVIOR] | [ACTIVE_ANALYSIS] |
| Power Users | [POWER_CRITERIA] | [POWER_SAMPLE] | [POWER_RANDOM] | [POWER_BEHAVIOR] | [POWER_ANALYSIS] |
| Mobile Users | [MOBILE_CRITERIA] | [MOBILE_SAMPLE] | [MOBILE_RANDOM] | [MOBILE_BEHAVIOR] | [MOBILE_ANALYSIS] |
| Geographic Segments | [GEO_CRITERIA] | [GEO_SAMPLE] | [GEO_RANDOM] | [GEO_BEHAVIOR] | [GEO_ANALYSIS] |
| Custom Segments | [CUSTOM_CRITERIA] | [CUSTOM_SAMPLE] | [CUSTOM_RANDOM] | [CUSTOM_BEHAVIOR] | [CUSTOM_ANALYSIS] |

### 6. Implementation & Rollout

**Experiment Execution Plan:**
| **Phase** | **Timeline** | **Activities** | **Checkpoints** | **Go/No-Go Criteria** | **Rollback Plan** |
|---------|------------|-------------|---------------|---------------------|------------------|
| Pre-Launch | [PRE_TIMELINE] | [PRE_ACTIVITIES] | [PRE_CHECKS] | [PRE_CRITERIA] | [PRE_ROLLBACK] |
| Soft Launch | [SOFT_TIMELINE] | [SOFT_ACTIVITIES] | [SOFT_CHECKS] | [SOFT_CRITERIA] | [SOFT_ROLLBACK] |
| Ramp-Up | [RAMP_TIMELINE] | [RAMP_ACTIVITIES] | [RAMP_CHECKS] | [RAMP_CRITERIA] | [RAMP_ROLLBACK] |
| Full Launch | [FULL_TIMELINE] | [FULL_ACTIVITIES] | [FULL_CHECKS] | [FULL_CRITERIA] | [FULL_ROLLBACK] |
| Monitoring | [MONITOR_TIMELINE] | [MONITOR_ACTIVITIES] | [MONITOR_CHECKS] | [MONITOR_CRITERIA] | [MONITOR_ROLLBACK] |
| Conclusion | [CONCLUDE_TIMELINE] | [CONCLUDE_ACTIVITIES] | [CONCLUDE_CHECKS] | [CONCLUDE_CRITERIA] | [CONCLUDE_ROLLBACK] |

### 7. Analysis & Statistical Methods

```
Analysis Framework:
Primary Analysis:
- Statistical Test: [PRIMARY_STAT_TEST]
- Effect Size: [EFFECT_SIZE]
- Confidence Intervals: [CONFIDENCE_INT]
- P-value Threshold: [P_VALUE_THRESH]
- Practical Significance: [PRACTICAL_SIG]
- Interpretation: [PRIMARY_INTERPRET]

Secondary Analysis:
- Subgroup Analysis: [SUBGROUP_ANALYSIS]
- Interaction Effects: [INTERACTION_EFFECTS]
- Time-Series Analysis: [TIME_SERIES]
- Cohort Analysis: [COHORT_ANALYSIS]
- Funnel Analysis: [FUNNEL_ANALYSIS]
- Long-term Effects: [LONGTERM_EFFECTS]

### Advanced Methods
- Bayesian Analysis: [BAYESIAN_ANALYSIS]
- Sequential Testing: [SEQUENTIAL_TEST]
- Variance Reduction: [VARIANCE_REDUCE]
- Causal Inference: [CAUSAL_INFERENCE]
- Machine Learning: [ML_METHODS]
- Network Effects: [NETWORK_EFFECTS]

### Robustness Checks
- Sensitivity Analysis: [SENSITIVITY]
- Balance Tests: [BALANCE_TESTS]
- Manipulation Checks: [MANIPULATION]
- Sample Ratio Mismatch: [SRM_CHECK]
- Novelty Effects: [NOVELTY_CHECK]
- Selection Bias: [SELECTION_CHECK]
```

### 8. Monitoring & Quality Control

| **Monitoring Area** | **Metrics** | **Thresholds** | **Alert Conditions** | **Response Actions** | **Escalation** |
|-------------------|-----------|--------------|-------------------|--------------------|--------------|
| System Health | [SYSTEM_METRICS] | [SYSTEM_THRESH] | [SYSTEM_ALERTS] | [SYSTEM_RESPONSE] | [SYSTEM_ESCALATE] |
| Data Quality | [DATA_METRICS] | [DATA_THRESH] | [DATA_ALERTS] | [DATA_RESPONSE] | [DATA_ESCALATE] |
| User Experience | [UX_METRICS] | [UX_THRESH] | [UX_ALERTS] | [UX_RESPONSE] | [UX_ESCALATE] |
| Statistical Validity | [STAT_METRICS] | [STAT_THRESH] | [STAT_ALERTS] | [STAT_RESPONSE] | [STAT_ESCALATE] |
| Business Metrics | [BUS_METRICS] | [BUS_THRESH] | [BUS_ALERTS] | [BUS_RESPONSE] | [BUS_ESCALATE] |
| Ethical Concerns | [ETHICAL_METRICS] | [ETHICAL_THRESH] | [ETHICAL_ALERTS] | [ETHICAL_RESPONSE] | [ETHICAL_ESCALATE] |

### 9. Decision Framework

**Decision Making Process:**
| **Decision Point** | **Criteria** | **Stakeholders** | **Data Required** | **Timeline** | **Documentation** |
|------------------|-----------|----------------|----------------|------------|------------------|
| Launch Decision | [LAUNCH_CRITERIA] | [LAUNCH_STAKE] | [LAUNCH_DATA] | [LAUNCH_TIME] | [LAUNCH_DOC] |
| Early Stopping | [EARLY_CRITERIA] | [EARLY_STAKE] | [EARLY_DATA] | [EARLY_TIME] | [EARLY_DOC] |
| Rollout Decision | [ROLLOUT_CRITERIA] | [ROLLOUT_STAKE] | [ROLLOUT_DATA] | [ROLLOUT_TIME] | [ROLLOUT_DOC] |
| Iteration Decision | [ITERATE_CRITERIA] | [ITERATE_STAKE] | [ITERATE_DATA] | [ITERATE_TIME] | [ITERATE_DOC] |
| Scale Decision | [SCALE_CRITERIA] | [SCALE_STAKE] | [SCALE_DATA] | [SCALE_TIME] | [SCALE_DOC] |
| Sunset Decision | [SUNSET_CRITERIA] | [SUNSET_STAKE] | [SUNSET_DATA] | [SUNSET_TIME] | [SUNSET_DOC] |

### 10. Learning & Documentation

```
Knowledge Management:
Experiment Documentation:
- Hypothesis Registry: [HYPOTHESIS_REG]
- Design Documents: [DESIGN_DOCS]
- Analysis Code: [ANALYSIS_CODE]
- Results Repository: [RESULTS_REPO]
- Decision Log: [DECISION_LOG]
- Lessons Learned: [LESSONS]

Knowledge Sharing:
- Internal Wiki: [WIKI_UPDATES]
- Team Presentations: [PRESENTATIONS]
- Best Practices: [BEST_PRACTICES]
- Failure Analysis: [FAILURE_ANALYSIS]
- Success Patterns: [SUCCESS_PATTERNS]
- Training Materials: [TRAINING_MAT]

Meta-Analysis:
- Cross-Experiment Learning: [CROSS_LEARNING]
- Pattern Recognition: [PATTERN_RECOG]
- Effect Size Database: [EFFECT_DATABASE]
- Velocity Metrics: [VELOCITY_METRICS]
- Win Rate Tracking: [WIN_RATE]
- ROI Analysis: [ROI_ANALYSIS]

### Process Improvement
- Experiment Velocity: [EXP_VELOCITY]
- Quality Metrics: [QUALITY_METRICS]
- Tool Optimization: [TOOL_OPTIMIZE]
- Team Efficiency: [TEAM_EFFICIENCY]
- Stakeholder Satisfaction: [STAKE_SATISFY]
- Innovation Index: [INNOVATION_INDEX]
```

## Usage Examples

## Best Practices

1. **Start with clear objectives** - Define what success looks like before beginning
2. **Use data to inform decisions** - Base choices on evidence and measurable outcomes
3. **Iterate and improve continuously** - Treat implementation as an ongoing process
4. **Engage stakeholders early** - Include key participants in planning and execution
5. **Document thoroughly** - Maintain clear records for reference and knowledge transfer
6. **Communicate regularly** - Keep all parties informed of progress and changes
7. **Address challenges proactively** - Identify potential issues before they become problems
8. **Celebrate milestones** - Recognize achievements to maintain motivation
9. **Learn from experience** - Reflect on what works and adjust accordingly
10. **Stay flexible** - Be ready to adapt based on feedback and changing circumstances

## Tips for Success

- Break complex tasks into manageable steps with clear milestones
- Set realistic timelines that account for dependencies and constraints
- Allocate sufficient resources including time, budget, and personnel
- Use templates and frameworks to ensure consistency and quality
- Seek feedback from users and stakeholders throughout the process
- Build in checkpoints to assess progress and make adjustments
- Maintain quality standards while remaining practical and efficient
- Document lessons learned for future reference and improvement
- Foster collaboration across teams and departments
- Stay current with industry best practices and emerging trends
### Example 1: E-commerce Checkout
```
Hypothesis: Simplified checkout increases conversion
Test: 3-step vs 1-step checkout
Sample: 100,000 users over 2 weeks
MDE: 2% conversion increase
Results: 3.5% lift, p < 0.001
Decision: Full rollout
Revenue Impact: +$2M annually
Learning: Reduced friction critical
```

### Example 2: Mobile App Feature
```
Experiment: New onboarding flow
Variants: 4 different flows
Metrics: D7 retention primary
Duration: 30 days
Segments: New users only
Power: 80% to detect 5% lift
Result: Variant C +8% retention
Implementation: Gradual rollout
```

### Example 3: Pricing Strategy
```
Test: Dynamic pricing algorithm
Control: Fixed pricing
Treatment: ML-based pricing
Guardrails: Revenue protection
Sample: 10% traffic holdout
Duration: 3 months
Analysis: DiD with matching
Impact: +12% revenue, maintained satisfaction
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Dashboard Design Patterns](dashboard-design-patterns.md)** - Complementary approaches and methodologies
- **[Data Governance Framework](data-governance-framework.md)** - Leverage data analysis to drive informed decisions
- **[Predictive Modeling Framework](predictive-modeling-framework.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (A/B Testing & Experimentation Design Framework)
2. Use [Dashboard Design Patterns](dashboard-design-patterns.md) for deeper analysis
3. Apply [Data Governance Framework](data-governance-framework.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Data Science](../../data-analytics/Data Science/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating comprehensive framework for designing and executing controlled experiments including a/b testing, multivariate testing, statistical analysis, power calculations, and decision-making based on experimental results.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Customization Options

### 1. Experiment Type
- A/B Test
- Multivariate Test
- Multi-Armed Bandit
- Sequential Testing
- Factorial Design

### 2. Analysis Method
- Frequentist
- Bayesian
- Causal Inference
- Machine Learning
- Mixed Methods

### 3. Scale
- Small (<1K users)
- Medium (1K-100K)
- Large (100K-1M)
- Very Large (1M+)
- Network Effects

### 4. Risk Level
- Low Risk
- Medium Risk
- High Risk
- Critical Systems
- Regulatory Constrained

### 5. Industry
- E-commerce
- SaaS
- Media/Content
- Financial Services
- Healthcare