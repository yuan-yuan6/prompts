---
category: data-analytics
title: A/B Testing & Experimentation Design Framework
tags:
- data-science
- ab-testing
- experimentation
- statistical-analysis
use_cases:
- Designing controlled experiments and A/B tests
- Calculating sample sizes and statistical power
- Analyzing experiment results and making decisions
- Building experimentation culture and platforms
related_templates:
- data-analytics/Advanced-Analytics/statistical-experimentation.md
- data-analytics/dashboard-design-patterns.md
- data-analytics/predictive-modeling-framework.md
industries:
- technology
- e-commerce
- finance
- healthcare
type: framework
difficulty: intermediate
slug: experimentation-design
---

# A/B Testing & Experimentation Design Framework

## Purpose
Design and execute rigorous controlled experiments to make data-driven decisions. This framework covers hypothesis formulation, statistical design, sample size calculation, experiment execution, analysis, and decision-making for A/B tests, multivariate tests, and other controlled experiments.

## Template

Design an A/B test for {CHANGE_DESCRIPTION} measuring impact on {PRIMARY_METRIC} with {MINIMUM_DETECTABLE_EFFECT} sensitivity.

**1. HYPOTHESIS AND BUSINESS CASE**

Frame the experiment clearly:

Business context: What problem are you solving? What's the potential impact? Experiments should tie to business objectives—revenue, engagement, retention, efficiency. Quantify the opportunity: "If this increases conversion by 2%, that's $500K annual revenue."

Hypothesis statement: State the hypothesis in testable form. "Changing X will cause Y to change by Z because of mechanism M." Be specific about direction and magnitude. A vague hypothesis leads to ambiguous results.

Success criteria: Define what "winning" looks like before you start. What's the minimum lift that justifies implementation? Consider implementation cost, ongoing maintenance, and opportunity cost. A statistically significant 0.1% lift may not be worth shipping.

Risk assessment: What could go wrong? Identify potential negative impacts on other metrics. Define guardrails—metrics that must not degrade. Plan for early stopping if harm is detected.

**2. STATISTICAL DESIGN**

Set up the experiment for valid inference:

Sample size calculation: Determine users needed per variant. Inputs: baseline conversion rate, minimum detectable effect (MDE), significance level (typically 0.05), and statistical power (typically 80%). Use two-sample proportion test for conversion metrics, t-test for continuous metrics. Online calculators or statsmodels power analysis work well.

Test duration: Calculate how long to reach target sample size based on traffic. Include at least one full week to capture day-of-week effects. Consider business cycles—don't run only during a sale period. Set maximum duration to avoid indefinite tests.

Randomization unit: Choose what gets randomly assigned—usually user ID for consistent experience. Session-level randomization risks inconsistent experience. Device or cookie has cross-device issues. Geographic clustering for network effects or when user-level isn't possible.

Allocation ratio: Default to 50/50 for maximum power. Use smaller treatment allocation (10-20%) for risky changes or limited inventory. Consider holdout groups for long-term measurement—permanently exclude small percentage from all experiments.

**3. VARIANT DESIGN**

Define control and treatment clearly:

Control group: The existing experience—"what we have today." Document the current state precisely. Control should receive no changes during the experiment. Verify control matches production exactly.

Treatment group: The change you're testing. Minimize differences from control to isolate the variable being tested. Document exactly what's different. If testing multiple changes, consider factorial design or prioritize which to test first.

Implementation requirements: How will variants be delivered? Feature flags, configuration, or code deployment? Ensure consistent experience within a user's session. Test thoroughly in staging—bugs invalidate experiments. Plan rollback mechanism.

**4. METRICS FRAMEWORK**

Measure what matters:

Primary metric: The single metric that determines success. Must be directly influenced by the change. Must be measurable within the test duration. Conversion rate, revenue per user, task completion rate are common choices. Pre-register the primary metric—no changing after seeing results.

Secondary metrics: Supporting metrics that provide context. Help understand why the primary metric moved. Examples: funnel steps, engagement metrics, segment-specific performance. Don't optimize for secondary metrics—they inform interpretation.

Guardrail metrics: Metrics that must not degrade significantly. Performance metrics: page load time, error rates, latency. Business metrics: revenue, customer satisfaction, support tickets. Set thresholds for acceptable degradation. Trigger investigation or early stopping if guardrails breach.

Metric definitions: Document exactly how each metric is calculated. Specify numerator, denominator, time window, and data source. "Conversion rate = unique purchasers / unique visitors within 7 days of first exposure." Ambiguous definitions cause disputes later.

**5. EXECUTION AND MONITORING**

Run the experiment properly:

Pre-launch checklist: Verify tracking is working—log exposures and outcomes. Confirm variants render correctly across devices and browsers. Validate randomization is balanced—check for sample ratio mismatch (SRM). Get stakeholder alignment on design and success criteria. Document the experiment in your tracking system.

Ramp-up plan: Start with small traffic percentage (1-5%) to catch bugs. Monitor guardrails closely in first 24-48 hours. Increase to full allocation once confident. Never peek at primary metric during ramp—it biases decisions.

Monitoring during experiment: Check for technical issues daily—error rates, performance, logging gaps. Verify sample sizes accumulating as expected. Watch guardrail metrics but not primary metric. Address SRM immediately if detected—indicates randomization problem.

Early stopping rules: Define conditions for stopping early. Stop for harm: significant degradation in guardrails or primary metric. Stop for implementation bugs that affect user experience. Generally, don't stop early for positive results—sequential testing requires special methods.

**6. ANALYSIS AND INTERPRETATION**

Draw valid conclusions:

Statistical testing: Apply the pre-specified statistical test. Calculate p-value and confidence interval for the treatment effect. Report effect size (absolute and relative lift), not just significance. A 95% confidence interval is more informative than p < 0.05.

Practical significance: Statistical significance doesn't equal business significance. Is the measured lift large enough to matter? Consider confidence interval bounds—would you ship if the true effect is at the lower bound? Factor in implementation and maintenance costs.

Segment analysis: Examine effects across pre-defined segments—new vs returning users, mobile vs desktop, geography. Pre-register segments to avoid p-hacking. Expect variation across segments—don't over-interpret without sufficient power. Segment results inform targeting, not primary decision.

Validity checks: Verify no sample ratio mismatch. Check for novelty effects—did the effect decay over time? Look for interaction with other concurrent experiments. Assess external validity—would results generalize to full rollout?

**7. DECISION AND DOCUMENTATION**

Make the call and record learnings:

Decision framework: Ship if statistically significant, practically significant, and guardrails intact. Don't ship if not significant after adequate sample—the change doesn't work. Iterate if results suggest a modified approach could work. Consider partial rollout if effect varies by segment.

Documentation: Record hypothesis, design, results, and decision. Include what you learned, even from failed experiments. Document any deviations from the plan. Make results discoverable for future reference.

Post-launch monitoring: Track metrics after full rollout to confirm experiment results hold. Watch for long-term effects not captured in test duration. Be prepared to rollback if issues emerge.

**8. EXPERIMENTATION MATURITY**

Build organizational capability:

Platform capabilities: Invest in experimentation platform—randomization, exposure logging, analysis tools. Enable self-service experiment creation for product teams. Automate sample size calculation, monitoring, and analysis. Build guardrail monitoring with automatic alerts.

Process and governance: Establish experiment review process for high-risk changes. Create templates and documentation standards. Define ownership and decision rights. Build experiment backlog and prioritization.

Culture: Celebrate learning, not just wins—failed experiments provide valuable information. Require experiments for significant changes. Share results broadly to prevent redundant tests. Train teams on statistical literacy and best practices.

Deliver your experiment design as:

1. **EXPERIMENT BRIEF** - Hypothesis, business case, success criteria, risk assessment

2. **STATISTICAL DESIGN** - Sample size calculation, test duration, randomization approach

3. **METRICS SPECIFICATION** - Primary, secondary, and guardrail metrics with definitions

4. **EXECUTION PLAN** - Launch checklist, ramp schedule, monitoring plan, stopping rules

5. **ANALYSIS PLAN** - Statistical tests, segment analyses, decision criteria

6. **DOCUMENTATION TEMPLATE** - Results summary, learnings, recommendations

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{CHANGE_DESCRIPTION}` | Feature or change being tested | "Simplified checkout flow", "New recommendation algorithm", "Pricing page redesign" |
| `{PRIMARY_METRIC}` | Main success metric | "Purchase conversion rate", "Revenue per visitor", "7-day retention" |
| `{MINIMUM_DETECTABLE_EFFECT}` | Smallest meaningful lift | "2% relative lift", "0.5pp absolute increase", "5% improvement" |

## Usage Examples

### Example 1: E-commerce Checkout Optimization

```
Design an A/B test for Simplified One-Page Checkout measuring impact 
on purchase conversion rate with 5% relative lift sensitivity.
```

**Expected Output:**
- Hypothesis: One-page checkout reduces abandonment, increasing conversion from 3.2% to 3.36%
- Sample size: 47K users per variant for 80% power at α=0.05
- Duration: 14 days based on 6,700 daily visitors
- Primary: Purchase conversion rate (purchases / visitors within session)
- Guardrails: Average order value (>-2%), page load time (<3s), error rate (<0.5%)
- Segments: New vs returning, mobile vs desktop, cart value tiers
- Decision: Ship if significant positive lift with guardrails intact

### Example 2: Content Recommendation Algorithm

```
Design an A/B test for New Collaborative Filtering Recommendations 
measuring impact on content engagement with 3% relative lift sensitivity.
```

**Expected Output:**
- Hypothesis: Collaborative filtering improves relevance, increasing engagement from 45% to 46.35%
- Sample size: 85K users per variant for 80% power
- Duration: 21 days to capture weekly patterns
- Primary: Content click-through rate (clicks / impressions)
- Secondary: Time on site, content diversity, return visits
- Guardrails: Page load time, recommendation latency, content coverage
- Segments: User tenure, content preferences, device type
- Decision: Ship if CTR lifts without reducing content diversity

### Example 3: Subscription Pricing Test

```
Design an A/B test for Annual Discount Pricing ($99/year vs $9.99/month) 
measuring impact on subscription revenue with 10% sensitivity.
```

**Expected Output:**
- Hypothesis: Annual discount increases revenue by shifting mix and reducing churn
- Sample size: 12K new visitors per variant (pricing tests need careful power analysis)
- Duration: 30 days minimum to capture subscription decisions
- Primary: Revenue per visitor (total subscription revenue / visitors)
- Secondary: Subscription rate, plan mix (annual vs monthly), 30-day churn
- Guardrails: Overall conversion (>-5%), customer satisfaction
- Segments: Price-sensitive vs premium segments, geography
- Decision: Complex—consider LTV implications beyond test window

## Cross-References

- **Statistical Methods:** statistical-experimentation.md - Deep dive on statistical testing
- **Dashboards:** dashboard-design-patterns.md - Visualizing experiment results
- **Predictive Modeling:** predictive-modeling-framework.md - When prediction beats experimentation
- **Data Governance:** data-governance-framework.md - Data quality for reliable experiments
