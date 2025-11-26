---
category: ai-ml-applications
last_updated: 2025-11-22
title: AI Product Evaluation and Quality Measurement
tags:
- ai-ml
- evaluation
- metrics
- quality
- testing
use_cases:
- Evaluating AI model performance before deployment
- Establishing quality metrics for AI products
- Conducting A/B tests for AI features
- Measuring business impact of AI systems
related_templates:
- ai-ml-applications/AI-Product-Development/ai-product-strategy.md
- ai-ml-applications/MLOps-Deployment/ai-monitoring-observability.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: framework
difficulty: intermediate
slug: ai-product-evaluation
---

# AI Product Evaluation and Quality Measurement

## Purpose
Establish comprehensive evaluation frameworks for AI products that measure technical performance, user experience, and business impact. This template guides teams in setting quality thresholds, designing evaluation experiments, and making data-driven deployment decisions.

---

## 🚀 Quick Evaluation Prompt

**Copy and use this generic prompt to evaluate any AI product:**

> I need to evaluate **[AI PRODUCT/FEATURE]** before **[deployment/promotion to production/scaling]**. Help me systematically assess: (1) **Technical reliability**—does it meet accuracy, latency, and robustness requirements on production-representative data, including edge cases? (2) **User value**—will people actually use it, and does it measurably save time, reduce errors, or improve outcomes? (3) **Business impact**—what's the ROI, cost per prediction, and statistical significance of impact on key business metrics? (4) **Safety and responsibility**—are there harmful outputs, fairness issues across user groups, or regulatory compliance gaps? For each dimension, identify the 3 most critical metrics, test against clear pass/fail thresholds, and analyze results across user segments. Give me a final recommendation (**APPROVE**/**CONDITIONAL**/**REJECT**) with specific evidence, trade-off analysis, and actionable next steps.

**Usage:** Fill in the brackets with your product details and use this as a prompt to an AI assistant, or as a structured framework for your evaluation process.

## Quick Start

### Minimal Example
```
AI PRODUCT EVALUATION: Email Reply Suggestions

1. TECHNICAL METRICS
   - Suggestion relevance: 78% user acceptance rate
   - Response latency: P50=120ms, P99=450ms
   - Model accuracy: 85% match with user's final reply

2. USER EXPERIENCE METRICS
   - Time saved: 45 seconds average per email
   - Feature adoption: 62% of eligible users
   - User satisfaction: 4.2/5.0 rating

3. BUSINESS METRICS
   - Productivity gain: 12% more emails handled/day
   - Support cost: $0.02 per suggestion (within budget)
   - Retention impact: +3% for feature users

4. QUALITY GATES
   ✓ Latency P99 < 500ms: PASS
   ✓ Acceptance rate > 70%: PASS
   ✓ No harmful suggestions in 10K sample: PASS
   → APPROVED FOR PRODUCTION ROLLOUT
```

### When to Use This
- Before launching an AI feature to production
- Comparing multiple model versions for deployment decisions
- Setting up continuous evaluation for deployed AI systems
- Reporting AI product performance to stakeholders
- Investigating quality issues or regressions

### Basic 5-Step Workflow
1. **Define** - Establish metrics aligned with product goals
2. **Baseline** - Measure current performance or set thresholds
3. **Test** - Run evaluation experiments with representative data
4. **Analyze** - Interpret results and identify gaps
5. **Decide** - Make go/no-go decisions based on quality gates

---

## Template

```markdown
# AI Product Evaluation: [PRODUCT_NAME]

## 1. Evaluation Objectives

### Product Context
- **AI feature:** [FEATURE_DESCRIPTION]
- **User benefit:** [VALUE_PROPOSITION]
- **Evaluation purpose:** [Pre-launch | Version comparison | Ongoing monitoring]
- **Decision to be made:** [DEPLOYMENT_DECISION]

### Success Criteria
| Criterion | Metric | Target | Priority |
|-----------|--------|--------|----------|
| [CRITERION_1] | [METRIC] | [TARGET] | Must-have |
| [CRITERION_2] | [METRIC] | [TARGET] | Must-have |
| [CRITERION_3] | [METRIC] | [TARGET] | Nice-to-have |

---

## 2. Technical Performance Metrics

### Model Quality Metrics
| Metric | Definition | Current | Target | Status |
|--------|------------|---------|--------|--------|
| Accuracy | [DEFINITION] | [VALUE] | >[TARGET] | [PASS/FAIL] |
| Precision | [DEFINITION] | [VALUE] | >[TARGET] | [PASS/FAIL] |
| Recall | [DEFINITION] | [VALUE] | >[TARGET] | [PASS/FAIL] |
| F1 Score | [DEFINITION] | [VALUE] | >[TARGET] | [PASS/FAIL] |
| AUC-ROC | [DEFINITION] | [VALUE] | >[TARGET] | [PASS/FAIL] |

### Task-Specific Metrics
For [TASK_TYPE], measure:
- **Classification:** Accuracy, Precision, Recall, F1, Confusion Matrix
- **Regression:** MAE, RMSE, R², MAPE
- **Ranking:** NDCG, MAP, MRR
- **Generation:** BLEU, ROUGE, Perplexity, Human eval scores
- **Retrieval:** Precision@K, Recall@K, Hit Rate
- **LLM/Generative AI:** Hallucination rate, Faithfulness, Instruction following, Toxicity score
- **RAG Systems:** Answer relevance, Context precision, Context recall, Faithfulness to sources

### LLM-Specific Quality Metrics
| Metric | Definition | Current | Target | Status |
|--------|------------|---------|--------|--------|
| Hallucination rate | % of factually incorrect outputs | [VALUE]% | <[TARGET]% | [PASS/FAIL] |
| Faithfulness score | Alignment with source material | [VALUE] | >[TARGET] | [PASS/FAIL] |
| Instruction following | % of prompts correctly followed | [VALUE]% | >[TARGET]% | [PASS/FAIL] |
| Toxicity score | Harmful content rate | [VALUE]% | <[TARGET]% | [PASS/FAIL] |
| Context retention | Accuracy over conversation turns | [VALUE]% | >[TARGET]% | [PASS/FAIL] |
| Prompt injection resistance | % of injection attempts blocked | [VALUE]% | >[TARGET]% | [PASS/FAIL] |

### Latency and Throughput
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| P50 latency | [VALUE]ms | <[TARGET]ms | [PASS/FAIL] |
| P95 latency | [VALUE]ms | <[TARGET]ms | [PASS/FAIL] |
| P99 latency | [VALUE]ms | <[TARGET]ms | [PASS/FAIL] |
| Throughput | [VALUE] req/s | >[TARGET] req/s | [PASS/FAIL] |
| Error rate | [VALUE]% | <[TARGET]% | [PASS/FAIL] |

### Robustness Testing
| Test Type | Method | Result | Status |
|-----------|--------|--------|--------|
| Edge cases | [TEST_SET] | [SCORE] | [PASS/FAIL] |
| Adversarial inputs | [METHOD] | [SCORE] | [PASS/FAIL] |
| Distribution shift | [DRIFT_TEST] | [SCORE] | [PASS/FAIL] |
| Stress testing | [LOAD_TEST] | [SCORE] | [PASS/FAIL] |

---

## 3. User Experience Metrics

### Adoption Metrics
| Metric | Definition | Value | Benchmark |
|--------|------------|-------|-----------|
| Feature awareness | % users who see the feature | [VALUE]% | [BENCHMARK]% |
| Trial rate | % aware users who try it | [VALUE]% | [BENCHMARK]% |
| Adoption rate | % users who use regularly | [VALUE]% | [BENCHMARK]% |
| Retention | % still using after 30 days | [VALUE]% | [BENCHMARK]% |

### User Satisfaction
| Metric | Method | Score | Target |
|--------|--------|-------|--------|
| CSAT | Post-interaction survey | [SCORE]/5 | >[TARGET] |
| NPS | Periodic survey | [SCORE] | >[TARGET] |
| Thumbs up/down | In-product feedback | [RATIO] | >[TARGET] |
| Qualitative feedback | User interviews | [SUMMARY] | [THEMES] |

### Human Evaluation Protocol
**Evaluation Setup:**
- Sample size: [N] examples
- Evaluators: [N] raters ([EXPERTISE_LEVEL])
- Evaluation rubric: [LINK_OR_DESCRIPTION]

**Rating Dimensions:**
| Dimension | Scale | Weight | Inter-rater Agreement |
|-----------|-------|--------|-----------------------|
| [DIMENSION_1] | 1-5 | [%] | Kappa=[VALUE] |
| [DIMENSION_2] | 1-5 | [%] | Kappa=[VALUE] |
| [DIMENSION_3] | 1-5 | [%] | Kappa=[VALUE] |

**Human Eval Results:**
| Metric | Score | Target | Status |
|--------|-------|--------|--------|
| Overall quality | [VALUE]/5 | >[TARGET] | [PASS/FAIL] |
| Agreement with automated metrics | [CORRELATION] | >[TARGET] | [PASS/FAIL] |
| Evaluator consensus (avg Kappa) | [VALUE] | >[TARGET] | [PASS/FAIL] |

### Behavioral Signals
| Signal | Interpretation | Value | Trend |
|--------|---------------|-------|-------|
| Accept rate | User finds suggestions useful | [VALUE]% | [TREND] |
| Edit rate | Suggestions need modification | [VALUE]% | [TREND] |
| Dismiss rate | Suggestions not relevant | [VALUE]% | [TREND] |
| Time to action | Cognitive load indicator | [VALUE]s | [TREND] |

### User Segmentation Analysis
| Segment | Metric | Performance | vs. Average | Notes |
|---------|--------|-------------|----------------|-------|
| New users (<7 days) | [METRIC] | [VALUE] | [+/-X%] | [INSIGHTS] |
| Power users (top 10%) | [METRIC] | [VALUE] | [+/-X%] | [INSIGHTS] |
| Geographic: [REGION] | [METRIC] | [VALUE] | [+/-X%] | [INSIGHTS] |
| Device: [PLATFORM] | [METRIC] | [VALUE] | [+/-X%] | [INSIGHTS] |
| Language: [LANGUAGE] | [METRIC] | [VALUE] | [+/-X%] | [INSIGHTS] |

---

## 4. Business Impact Metrics

### Direct Impact
| Metric | Baseline | With AI | Lift | Significance |
|--------|----------|---------|------|--------------|
| [REVENUE_METRIC] | [VALUE] | [VALUE] | [%] | p=[VALUE] |
| [COST_METRIC] | [VALUE] | [VALUE] | [%] | p=[VALUE] |
| [EFFICIENCY_METRIC] | [VALUE] | [VALUE] | [%] | p=[VALUE] |

### Unit Economics
| Component | Value | Acceptable Range |
|-----------|-------|------------------|
| Cost per prediction | $[VALUE] | <$[MAX] |
| Revenue per user | $[VALUE] | >$[MIN] |
| ROI | [VALUE]% | >[TARGET]% |
| Payback period | [VALUE] months | <[MAX] months |

### Cost Breakdown (for LLMs/API-based models)
| Cost Component | Monthly | Per 1K requests | % of Total |
|----------------|---------|-----------------|------------|
| Input tokens | $[VALUE] | $[VALUE] | [%] |
| Output tokens | $[VALUE] | $[VALUE] | [%] |
| Compute/inference | $[VALUE] | $[VALUE] | [%] |
| Storage | $[VALUE] | $[VALUE] | [%] |
| API calls (external) | $[VALUE] | $[VALUE] | [%] |
| **Total** | **$[VALUE]** | **$[VALUE]** | **100%** |

### Sustainability Metrics
| Metric | Value | Benchmark | Notes |
|--------|-------|-----------|-------|
| Carbon footprint | [VALUE] kg CO2/month | [BENCHMARK] | [CALCULATION_METHOD] |
| Energy consumption | [VALUE] kWh/1K requests | [BENCHMARK] | [INFRASTRUCTURE] |
| Model size efficiency | [PARAMS]/[PERFORMANCE] | [BENCHMARK] | Params vs. quality trade-off |

### Strategic Value
- [ ] Competitive differentiation achieved
- [ ] Platform capability expanded
- [ ] Data flywheel strengthened
- [ ] User engagement increased

---

## 5. Safety and Fairness Evaluation

### Harm Assessment
| Harm Category | Test Method | Result | Status |
|---------------|-------------|--------|--------|
| Offensive content | [TEST_SET] | [RATE] | [PASS/FAIL] |
| Misinformation | [VALIDATION] | [RATE] | [PASS/FAIL] |
| Privacy leakage | [AUDIT] | [FINDINGS] | [PASS/FAIL] |
| Security vulnerabilities | [PENTEST] | [FINDINGS] | [PASS/FAIL] |

### Fairness Metrics
| Protected Group | Metric | Value | Threshold | Status |
|-----------------|--------|-------|-----------|--------|
| [GROUP_A] vs [GROUP_B] | [METRIC] | [DIFF] | <[MAX] | [PASS/FAIL] |

### Responsible AI Checklist
- [ ] **Explainability:** Model decisions can be explained to users
  - Method: [SHAP/LIME/Attention/Other]
  - Explanation quality score: [VALUE]
- [ ] **Model documentation:** Model card completed
  - Link: [URL_TO_MODEL_CARD]
- [ ] **Regulatory compliance:** Meets all applicable requirements
  - GDPR: [COMPLIANT/NOT_APPLICABLE]
  - EU AI Act: [RISK_LEVEL]
  - Industry-specific: [REQUIREMENTS]
- [ ] **Audit trail:** All decisions logged for review
  - Retention period: [DAYS]
  - Audit access: [ROLES]
- [ ] **Human oversight:** Human-in-the-loop for high-stakes decisions
  - Override mechanism: [IMPLEMENTED/NOT_NEEDED]
  - Escalation path: [DEFINED]

### Failure Mode Analysis
| Failure Mode | Frequency | Severity | Mitigation |
|--------------|-----------|----------|------------|
| [FAILURE_1] | [RATE] | [HIGH/MED/LOW] | [MITIGATION] |
| [FAILURE_2] | [RATE] | [HIGH/MED/LOW] | [MITIGATION] |

---

## 6. Experiment Design (A/B Testing)

### Experiment Setup
- **Hypothesis:** [HYPOTHESIS]
- **Primary metric:** [METRIC]
- **Secondary metrics:** [METRICS]
- **Guardrail metrics:** [METRICS]

### Sample Size and Duration
```
Baseline conversion: [X]%
Minimum detectable effect: [Y]%
Statistical power: 80%
Significance level: 5%
Required sample size: [N] per variant
Estimated duration: [DAYS] days
```

### Variant Allocation
| Variant | Description | Traffic % |
|---------|-------------|-----------|
| Control | [DESCRIPTION] | [%] |
| Treatment | [DESCRIPTION] | [%] |

### Shadow Mode Evaluation (if applicable)
**Shadow Mode Setup:**
- Duration: [DAYS] days
- Traffic: [%]% of production
- Comparison: Shadow model runs alongside production, no user impact

**Shadow Mode Results:**
| Metric | Production Model | Shadow Model | Difference |
|--------|-----------------|--------------|------------|
| [METRIC_1] | [VALUE] | [VALUE] | [DIFF] |
| [METRIC_2] | [VALUE] | [VALUE] | [DIFF] |
| Agreement rate | N/A | [VALUE]% | N/A |

**Canary Deployment Plan:**
- [ ] Phase 1: 5% traffic for [DURATION]
- [ ] Phase 2: 25% traffic for [DURATION]
- [ ] Phase 3: 50% traffic for [DURATION]
- [ ] Phase 4: 100% traffic (full rollout)
- Rollback criteria: [CRITERIA]

### Results
| Metric | Control | Treatment | Lift | p-value | CI |
|--------|---------|-----------|------|---------|-----|
| [PRIMARY] | [VALUE] | [VALUE] | [%] | [P] | [CI] |
| [SECONDARY] | [VALUE] | [VALUE] | [%] | [P] | [CI] |
| [GUARDRAIL] | [VALUE] | [VALUE] | [%] | [P] | [CI] |

---

## 7. Quality Gates and Decision

### Quality Gate Checklist
| Gate | Criterion | Result | Priority | Required |
|------|-----------|--------|----------|----------|
| Technical | Accuracy > [X]% | [PASS/FAIL] | Must-have | Yes |
| Technical | Latency P99 < [X]ms | [PASS/FAIL] | Must-have | Yes |
| Technical | Hallucination rate < [X]% | [PASS/FAIL] | Must-have | Yes |
| UX | Acceptance rate > [X]% | [PASS/FAIL] | Must-have | Yes |
| UX | Human eval score > [X] | [PASS/FAIL] | Should-have | No |
| Safety | Zero critical harms | [PASS/FAIL] | Must-have | Yes |
| Fairness | Disparity < [X]% | [PASS/FAIL] | Must-have | Yes |
| Responsible AI | Model card completed | [PASS/FAIL] | Should-have | No |
| Business | Positive ROI | [PASS/FAIL] | Could-have | No |
| Business | Cost per prediction < $[X] | [PASS/FAIL] | Should-have | No |

### Trade-off Analysis
**Competing Metrics:**
- Latency vs. Accuracy: [ANALYSIS]
- Cost vs. Quality: [ANALYSIS]
- Recall vs. Precision: [ANALYSIS]

**Chosen Trade-offs:**
| Decision | Rationale |
|----------|----------|
| [TRADE_OFF_1] | [REASON] |
| [TRADE_OFF_2] | [REASON] |

### Decision
**Recommendation:** [APPROVE | CONDITIONAL | REJECT]

**Rationale:**
[SUMMARY_OF_FINDINGS]

**Conditions (if applicable):**
- [CONDITION_1]
- [CONDITION_2]

**Next Steps:**
- [ ] [ACTION_1]
- [ ] [ACTION_2]

---

## 8. Ongoing Evaluation Plan

### Monitoring Cadence
| Metric Type | Frequency | Owner | Alert Threshold |
|-------------|-----------|-------|-----------------|-------|
| Technical | Real-time | [TEAM] | [THRESHOLD] |
| UX | Daily | [TEAM] | [THRESHOLD] |
| Business | Weekly | [TEAM] | [THRESHOLD] |
| Safety | Continuous | [TEAM] | Any incident |

### Data Drift Monitoring
| Drift Type | Detection Method | Check Frequency | Action Threshold |
|------------|------------------|-----------------|------------------|
| Input distribution drift | KS test / PSI | Daily | p<0.05 or PSI>0.2 |
| Prediction drift | Chi-square test | Daily | p<0.05 |
| Concept drift | Performance degradation | Real-time | >10% drop in accuracy |
| Label drift | Ground truth comparison | Weekly | >5% shift |

**Drift Alert Response:**
- [ ] Investigate data quality issues
- [ ] Review recent changes (features, infrastructure)
- [ ] Evaluate need for model retraining
- [ ] Consider rollback if drift is severe

### Model Refresh Strategy
**Automatic Retraining Triggers:**
- [ ] Performance drops below [THRESHOLD]
- [ ] Data drift exceeds [THRESHOLD] for [N] consecutive days
- [ ] [N] days since last training
- [ ] New labeled data reaches [N] examples

**Champion/Challenger Framework:**
- Current production model: Champion
- New model candidate: Challenger
- Challenger evaluation: [SHADOW_MODE/A_B_TEST/OFFLINE]
- Promotion criteria: [CRITERIA]
- Rollback plan: [PLAN]

### Re-evaluation Triggers
- [ ] Model retrained or updated
- [ ] Significant traffic increase (>50%)
- [ ] User behavior shift detected
- [ ] New failure mode discovered
- [ ] Data drift alert triggered
- [ ] Regulatory requirements change
- [ ] Quarterly scheduled review

---

## 9. Evaluation Resources and Timeline

### Team Composition
| Role | Responsibilities | Time Commitment |
|------|------------------|----------------|
| ML Engineer | Technical evaluation, metrics implementation | [N] hours |
| Data Scientist | Statistical analysis, A/B test design | [N] hours |
| Product Manager | Success criteria, business metrics | [N] hours |
| Domain Expert | Human evaluation, use case validation | [N] hours |
| UX Researcher | User testing, qualitative feedback | [N] hours |
| Legal/Compliance | Regulatory review, risk assessment | [N] hours |

### Evaluation Timeline
| Project Size | Offline Eval | Human Eval | A/B Test | Total Duration |
|--------------|--------------|------------|----------|----------------|
| Small (MVP) | 3-5 days | 2-3 days | 1 week | 2-3 weeks |
| Medium (Feature) | 1-2 weeks | 1 week | 2-3 weeks | 4-6 weeks |
| Large (Platform) | 2-4 weeks | 2 weeks | 4-6 weeks | 8-12 weeks |

### Budget Considerations
| Cost Item | Estimate | Notes |
|-----------|----------|-------|
| Compute for evaluation | $[VALUE] | Test set inference, ablations |
| Human evaluation | $[VALUE] | [N] raters × [N] hours |
| A/B test opportunity cost | $[VALUE] | Potential revenue impact |
| Tools/infrastructure | $[VALUE] | Monitoring, experimentation platform |
| **Total** | **$[VALUE]** | |
```

---

## Variables

### PRODUCT_NAME
Name of the AI product or feature being evaluated.
- Examples: "Smart Reply", "Fraud Detection System", "Product Recommendations", "Document Classifier"

### METRIC
Quantitative measure of performance or quality.
- Examples: "Accuracy", "F1 Score", "User acceptance rate", "Revenue per user", "P99 latency"

### TARGET
Threshold that defines success for a metric.
- Examples: ">90%", "<200ms", ">4.0/5.0", "±10% of baseline"

### TASK_TYPE
Category of ML task the product performs.
- Examples: "Binary classification", "Multi-class classification", "Regression", "Ranking", "Text generation", "Image recognition"

---

## Usage Examples

### Example 1: Search Ranking Evaluation
```
PRODUCT: AI-Powered Search Results

TECHNICAL METRICS:
- NDCG@10: 0.72 (target: >0.70) ✓
- MRR: 0.65 (target: >0.60) ✓
- P95 latency: 180ms (target: <250ms) ✓

USER EXPERIENCE:
- Click-through rate: +15% vs. baseline
- Zero-result rate: -40% vs. baseline
- Search refinement rate: -25% (users find results faster)

A/B TEST RESULTS (2 weeks, 500K users):
- Sessions with search: +8.2% (p<0.001)
- Items added to cart from search: +12.1% (p<0.001)
- Search abandonment: -18.5% (p<0.001)

DECISION: APPROVE - Ship to 100%
```

### Example 2: Content Moderation Evaluation
```
PRODUCT: Automated Content Moderation

TECHNICAL METRICS:
- Precision (harmful content): 94% (target: >90%) ✓
- Recall (harmful content): 89% (target: >85%) ✓
- False positive rate: 2.1% (target: <5%) ✓

SAFETY EVALUATION:
- Missed harmful content (sample audit): 0.8%
- Wrongful removal appeals upheld: 1.2%
- Bias audit: No significant disparities by language

OPERATIONAL METRICS:
- Human review queue reduced by 65%
- Average review time: 2.3s vs 45s manual
- Cost per moderation: $0.003 vs $0.15 manual

QUALITY GATES:
✓ Recall > 85%: PASS
✓ False positive < 5%: PASS
✓ Bias audit passed: PASS
✗ Appeal rate < 1%: FAIL (1.2%)

DECISION: CONDITIONAL APPROVE
- Condition: Improve precision for borderline cases
- Action: Add human review for confidence 0.7-0.9
```

### Example 3: Predictive Model Comparison
```
EVALUATION: Churn Prediction Model v2 vs v1

MODEL COMPARISON:
| Metric | v1 (Current) | v2 (Candidate) | Improvement |
|--------|--------------|----------------|-------------|
| AUC-ROC | 0.78 | 0.84 | +7.7% |
| Precision@10% | 0.45 | 0.58 | +28.9% |
| Recall@10% | 0.32 | 0.41 | +28.1% |
| Inference time | 45ms | 52ms | -15.6% |

BUSINESS SIMULATION:
- Interventions saved (projected): +2,400 customers/quarter
- Revenue retained (projected): +$1.2M/quarter
- Additional compute cost: +$8K/quarter

LATENCY TRADE-OFF ANALYSIS:
- 7ms increase acceptable for batch scoring use case
- Real-time scoring not required

DECISION: APPROVE v2
- Deploy to batch scoring pipeline
- Monitor intervention effectiveness for 1 quarter
```

### Example 4: LLM-Powered Customer Support Chatbot
```
PRODUCT: AI Support Assistant (GPT-4 based)

LLM-SPECIFIC METRICS:
- Hallucination rate: 2.3% (target: <5%) ✓
- Instruction following: 94% (target: >90%) ✓
- Toxicity score: 0.1% (target: <1%) ✓
- Context retention (5 turns): 89% (target: >85%) ✓

HUMAN EVALUATION (200 conversations, 3 raters):
- Helpfulness: 4.3/5 (Kappa: 0.72)
- Accuracy: 4.1/5 (Kappa: 0.68)
- Tone appropriateness: 4.5/5 (Kappa: 0.81)
- Overall quality: 4.2/5

BUSINESS IMPACT (4-week A/B test):
- Resolution rate: +18% (p<0.001)
- Time to resolution: -35% (p<0.001)
- Customer satisfaction: +0.4 points (p=0.002)
- Support ticket volume: -22% (deflection to AI)

COST ANALYSIS:
- Input tokens: $0.08 per conversation
- Output tokens: $0.12 per conversation
- Total: $0.20 per conversation vs. $8.50 human agent
- ROI: 4,150%

DECISION: APPROVE - Full rollout
- Start with 50% of simple queries (canary)
- Scale to 100% over 2 weeks
- Maintain human escalation for complex issues
```

### Example 5: Code Generation Assistant
```
PRODUCT: AI Code Completion (Codex-based)

TECHNICAL METRICS:
- Acceptance rate: 26% (industry benchmark: 20-30%) ✓
- Latency P99: 380ms (target: <500ms) ✓
- Suggestion correctness: 82% compile without errors

HUMAN EVALUATION (500 completions):
- Code quality: 3.9/5
- Helpfulness: 4.1/5
- Security concerns: 3 instances flagged (0.6%)

USER SEGMENTATION:
- Junior devs: 32% acceptance (+23% vs. average)
- Senior devs: 21% acceptance (-19% vs. average)
- Python: 29% acceptance
- JavaScript: 24% acceptance

PRODUCTIVITY IMPACT:
- Time saved: 11 minutes per hour of coding
- Tasks completed: +9% (p=0.012)
- Developer satisfaction: 4.0/5

SAFETY CHECKS:
- Prompt injection resistance: 97% blocked
- Secrets detection: 100% blocked from suggestions
- License compliance: OSS license checker integrated

DECISION: CONDITIONAL APPROVE
- Add security review layer for suggestions
- Provide opt-out for senior developers
- Monitor acceptance rate by language/framework
```

---

## Best Practices

1. **Align Metrics with Goals** - Choose metrics that directly reflect what users and the business care about. Technical metrics alone don't guarantee product success.

2. **Use Holdout Sets Properly** - Never evaluate on data used for training. Maintain clean test sets that reflect production distribution.

3. **Statistical Rigor in Experiments** - Pre-register hypotheses, calculate sample sizes, and don't peek at results early. Accept negative results.

4. **Evaluate on Slices** - Overall metrics can hide problems. Evaluate performance across user segments, content types, and edge cases.

5. **Include Human Evaluation** - For generative AI, automated metrics correlate imperfectly with quality. Invest in human evaluation protocols with proper inter-rater reliability.

6. **Set Quality Gates Before Testing** - Define pass/fail criteria upfront to avoid post-hoc rationalization of results. Use MoSCoW prioritization (Must/Should/Could/Won't).

7. **Shadow Mode First** - Run new models in shadow mode before A/B testing to catch issues without user impact.

8. **Monitor for Drift** - Set up automated monitoring for data drift and concept drift. Don't assume model performance stays constant.

9. **Document Everything** - Create model cards, document assumptions, and maintain audit trails for regulatory compliance.

10. **Plan for Iteration** - Build evaluation into your continuous deployment pipeline. Evaluation is ongoing, not one-time.

---

## Common Pitfalls

❌ **Goodhart's Law** - Optimizing for metrics that stop measuring what matters
✅ Instead: Use diverse metrics and validate that improvements reflect real quality

❌ **Ignoring Tail Cases** - Focusing only on average performance
✅ Instead: Evaluate P95/P99 and explicitly test edge cases

❌ **Over-indexing on Accuracy** - High accuracy with wrong errors can be worse than lower accuracy
✅ Instead: Understand the cost of different error types (false positives vs. false negatives)

❌ **Short Evaluation Windows** - Not accounting for novelty effects or long-term behavior
✅ Instead: Run experiments long enough to see stable behavior (usually 2+ weeks)

❌ **Skipping Offline Evaluation** - Going straight to A/B tests without offline validation
✅ Instead: Use offline evaluation to filter candidates before expensive online tests

❌ **Ignoring LLM-Specific Risks** - Treating LLMs like traditional ML models
✅ Instead: Test for hallucinations, prompt injections, and context retention

❌ **No Drift Monitoring** - Assuming model performance is static
✅ Instead: Implement automated drift detection and retraining triggers

❌ **Insufficient Human Evaluation** - Relying only on automated metrics for generative AI
✅ Instead: Invest in structured human eval with proper rubrics and inter-rater agreement

❌ **Missing Cost Tracking** - Not monitoring token usage and inference costs
✅ Instead: Track detailed cost breakdown, especially for API-based models

---

## Related Resources

**Evaluation Frameworks & Tools:**
- [MLflow](https://mlflow.org/) - Experiment tracking and model registry
- [Weights & Biases](https://wandb.ai/) - ML experiment tracking and collaboration
- [Evidently AI](https://evidentlyai.com/) - ML monitoring and drift detection
- [Statsig](https://statsig.com/) - Feature flags and experimentation platform
- [RAGAS](https://github.com/explodinggradients/ragas) - RAG evaluation framework
- [LangSmith](https://www.langchain.com/langsmith) - LLM application evaluation
- [Phoenix](https://phoenix.arize.com/) - LLM observability and evaluation
- [Giskard](https://www.giskard.ai/) - AI quality and testing

**LLM Evaluation:**
- [OpenAI Evals](https://github.com/openai/evals) - Framework for LLM evaluation
- [EleutherAI LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness)
- [HELM (Stanford)](https://crfm.stanford.edu/helm/) - Holistic evaluation of language models

**Responsible AI:**
- [AI Fairness 360 (IBM)](https://aif360.res.ibm.com/) - Fairness metrics and mitigation
- [Model Cards Toolkit](https://github.com/tensorflow/model-card-toolkit) - Model documentation
- [EU AI Act Compliance Checker](https://artificialintelligenceact.eu/)

**Further Reading:**
- [Rules of ML (Google)](https://developers.google.com/machine-learning/guides/rules-of-ml)
- [Trustworthy Online Controlled Experiments](https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/)
- [Patterns for LLM Evaluation (Microsoft)](https://microsoft.github.io/promptbase/)
- [A Guide to Model Evaluation (Anthropic)](https://www.anthropic.com/research)

---

**Last Updated:** 2025-11-23
**Category:** AI/ML Applications > AI-Product-Development
**Difficulty:** Intermediate
**Estimated Time:** 2-12 weeks for comprehensive evaluation (varies by project size)
**Version:** 2.0 (Enhanced for LLMs and Generative AI)
