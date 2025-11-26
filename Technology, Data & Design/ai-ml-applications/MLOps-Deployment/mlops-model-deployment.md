---
category: ai-ml-applications
last_updated: 2025-11-22
title: MLOps Model Deployment
tags:
- ai-ml
- mlops
- deployment
- ci-cd
- model-serving
use_cases:
- Deploying ML models to production environments
- Setting up CI/CD pipelines for model updates
- Managing model versioning and rollbacks
- Implementing canary and blue-green deployments
related_templates:
- ai-ml-applications/MLOps-Deployment/mlops.md
- ai-ml-applications/MLOps-Deployment/ai-monitoring-observability.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: framework
difficulty: intermediate
slug: mlops-model-deployment
---

# MLOps Model Deployment

## Purpose
Deploy ML models to production reliably and safely. This framework covers deployment strategies, CI/CD pipelines, model serving infrastructure, and rollback procedures for production ML systems.

## 🚀 Quick Deployment Prompt

> Plan a **model deployment** for **[MODEL_NAME v.X.X]** to **[ENVIRONMENT]** with **[TRAFFIC VOLUME]** requests/day. Guide me through: (1) **Pre-deployment validation**—what quality gates (accuracy, latency, A/B results) must pass? What's the checklist? (2) **Deployment strategy**—should I use canary, blue-green, or rolling? What's the rollout percentage and timeline? (3) **Monitoring setup**—what metrics to watch during deployment? What are the automatic rollback triggers? (4) **Rollback procedure**—what's the instant rollback command and verification checklist? Provide deployment configuration, traffic routing rules, monitoring dashboard requirements, and a step-by-step runbook.

**Usage:** Replace bracketed placeholders with your specifics. Use as a prompt to an AI assistant for rapid deployment planning.

---

## Quick Start

### Minimal Example
```
MODEL DEPLOYMENT: Fraud Detection v2.1

1. PRE-DEPLOYMENT CHECKLIST
   ✓ Model validation: AUC 0.92 (>0.90 threshold)
   ✓ Latency test: P99 45ms (<50ms requirement)
   ✓ A/B test: +5% fraud catch rate, neutral FP rate
   ✓ Security scan: No vulnerabilities found

2. DEPLOYMENT STRATEGY
   Type: Canary deployment
   Rollout: 1% → 10% → 50% → 100%
   Duration: 4 hours total
   Rollback trigger: Error rate >1% or latency P99 >100ms

3. DEPLOYMENT EXECUTION
   10:00 - Deploy to 1% traffic
   10:30 - Metrics stable, proceed to 10%
   11:30 - Metrics stable, proceed to 50%
   13:00 - Metrics stable, proceed to 100%
   14:00 - Deployment complete, v2.0 decommissioned

4. POST-DEPLOYMENT
   ✓ Monitoring dashboards updated
   ✓ Runbooks updated for v2.1
   ✓ Stakeholders notified
```

### When to Use This
- Deploying a new ML model version to production
- Setting up deployment infrastructure for ML systems
- Planning rollout strategy for high-risk model changes
- Recovering from a failed model deployment
- Establishing MLOps best practices for your team

### Basic 5-Step Workflow
1. **Validate** - Ensure model meets quality and performance gates
2. **Package** - Containerize model with dependencies
3. **Stage** - Deploy to staging environment for final testing
4. **Release** - Gradually roll out to production traffic
5. **Monitor** - Verify deployment success and watch for issues

---

## Template

```markdown
# Model Deployment Plan: [MODEL_NAME] v[VERSION]

## 1. Deployment Overview

### Model Information
- **Model name:** [MODEL_NAME]
- **Version:** [VERSION]
- **Previous version:** [PREV_VERSION]
- **Change summary:** [DESCRIPTION]
- **Risk level:** [Low | Medium | High | Critical]

### Deployment Window
- **Planned start:** [DATE_TIME]
- **Expected duration:** [DURATION]
- **Rollback deadline:** [DEADLINE]
- **Change ticket:** [TICKET_ID]

### Stakeholders
| Role | Name | Responsibility |
|------|------|----------------|
| Model Owner | [NAME] | Approve deployment |
| ML Engineer | [NAME] | Execute deployment |
| On-call | [NAME] | Monitor and respond |
| Business Owner | [NAME] | Validate business metrics |

---

## 2. Pre-Deployment Validation

### Model Quality Gates
| Gate | Metric | Required | Actual | Status |
|------|--------|----------|--------|--------|
| Accuracy | [METRIC] | >[THRESHOLD] | [VALUE] | [PASS/FAIL] |
| Latency | P99 | <[THRESHOLD]ms | [VALUE]ms | [PASS/FAIL] |
| Throughput | RPS | >[THRESHOLD] | [VALUE] | [PASS/FAIL] |
| Error rate | % | <[THRESHOLD]% | [VALUE]% | [PASS/FAIL] |

### Comparison with Previous Version
| Metric | v[PREV] | v[NEW] | Change | Acceptable |
|--------|---------|--------|--------|------------|
| [METRIC_1] | [VALUE] | [VALUE] | [DELTA] | [Yes/No] |
| [METRIC_2] | [VALUE] | [VALUE] | [DELTA] | [Yes/No] |
| [METRIC_3] | [VALUE] | [VALUE] | [DELTA] | [Yes/No] |

### Pre-Deployment Checklist
- [ ] Model trained on approved dataset
- [ ] Offline evaluation completed
- [ ] Shadow mode testing passed
- [ ] Performance benchmarks met
- [ ] Security scan completed
- [ ] Documentation updated
- [ ] Rollback procedure tested
- [ ] Stakeholder approval obtained

---

## 3. Deployment Strategy

### Strategy Selection
| Strategy | Use When | Our Choice |
|----------|----------|------------|
| Blue-Green | Zero downtime, instant rollback | [ ] |
| Canary | Gradual validation, risk mitigation | [ ] |
| Rolling | Resource efficient, gradual | [ ] |
| Shadow | Pre-production validation | [ ] |
| A/B Test | Business metric validation | [ ] |

### Canary Deployment Plan
```
Stage 1: Canary (1% traffic)
├── Duration: [TIME]
├── Success criteria: [CRITERIA]
└── Proceed if: [CONDITIONS]

Stage 2: Limited (10% traffic)
├── Duration: [TIME]
├── Success criteria: [CRITERIA]
└── Proceed if: [CONDITIONS]

Stage 3: Broad (50% traffic)
├── Duration: [TIME]
├── Success criteria: [CRITERIA]
└── Proceed if: [CONDITIONS]

Stage 4: Full (100% traffic)
├── Duration: [TIME]
├── Success criteria: [CRITERIA]
└── Complete when: [CONDITIONS]
```

### Traffic Routing Configuration
```yaml
deployment:
  strategy: canary
  stages:
    - name: canary
      weight: 1
      duration: 30m
      promotion:
        analysis:
          metrics:
            - name: error-rate
              threshold: 1
            - name: latency-p99
              threshold: [THRESHOLD]

    - name: limited
      weight: 10
      duration: 1h
      promotion:
        analysis:
          metrics:
            - name: error-rate
              threshold: 1
            - name: accuracy
              threshold: [THRESHOLD]
```

---

## 4. Infrastructure Configuration

### Model Serving Setup
```yaml
serving:
  framework: [TensorFlow Serving | TorchServe | Triton | Custom]
  replicas:
    min: [MIN]
    max: [MAX]
  resources:
    cpu: [CPU_LIMIT]
    memory: [MEMORY_LIMIT]
    gpu: [GPU_COUNT]

  autoscaling:
    metric: [cpu | gpu | custom]
    target: [VALUE]

  health_check:
    path: /health
    interval: 10s
    timeout: 5s
```

### Container Configuration
```dockerfile
FROM [BASE_IMAGE]

# Model artifacts
COPY model/ /models/[MODEL_NAME]/[VERSION]/

# Dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Serving configuration
ENV MODEL_NAME=[MODEL_NAME]
ENV MODEL_VERSION=[VERSION]

EXPOSE 8501
CMD ["serve"]
```

### Environment Variables
| Variable | Staging | Production |
|----------|---------|------------|
| MODEL_PATH | [PATH] | [PATH] |
| LOG_LEVEL | DEBUG | INFO |
| BATCH_SIZE | [SIZE] | [SIZE] |
| FEATURE_STORE_URL | [URL] | [URL] |

---

## 5. Deployment Execution

### Step-by-Step Procedure
```markdown
## Deployment Steps

### 1. Preparation ([TIME])
- [ ] Notify stakeholders of deployment start
- [ ] Verify staging environment healthy
- [ ] Confirm rollback procedure ready
- [ ] Start deployment monitoring dashboard

### 2. Stage 1 - Canary ([TIME])
- [ ] Deploy new version to canary
- [ ] Verify canary pods healthy
- [ ] Route 1% traffic to canary
- [ ] Monitor for [DURATION]
- [ ] Verify metrics within thresholds
- [ ] Decision: Proceed / Rollback

### 3. Stage 2 - Limited ([TIME])
- [ ] Scale up new version replicas
- [ ] Route 10% traffic to new version
- [ ] Monitor for [DURATION]
- [ ] Verify metrics within thresholds
- [ ] Decision: Proceed / Rollback

### 4. Stage 3 - Broad ([TIME])
- [ ] Route 50% traffic to new version
- [ ] Monitor for [DURATION]
- [ ] Verify business metrics stable
- [ ] Decision: Proceed / Rollback

### 5. Stage 4 - Full ([TIME])
- [ ] Route 100% traffic to new version
- [ ] Scale down old version
- [ ] Verify all metrics stable
- [ ] Keep old version for [DURATION] (quick rollback)

### 6. Cleanup ([TIME])
- [ ] Decommission old version
- [ ] Update documentation
- [ ] Notify stakeholders of completion
- [ ] Close change ticket
```

### Commands Reference
```bash
# Deploy new version
kubectl apply -f deployment-v[VERSION].yaml

# Check rollout status
kubectl rollout status deployment/[MODEL_NAME]

# Route traffic (Istio example)
kubectl apply -f virtual-service-canary.yaml

# Rollback if needed
kubectl rollout undo deployment/[MODEL_NAME]

# Scale down old version
kubectl scale deployment/[MODEL_NAME]-v[PREV] --replicas=0
```

---

## 6. Monitoring During Deployment

### Key Metrics to Watch
| Metric | Threshold | Dashboard Link |
|--------|-----------|----------------|
| Error rate | <[THRESHOLD]% | [LINK] |
| Latency P99 | <[THRESHOLD]ms | [LINK] |
| Throughput | >[THRESHOLD] RPS | [LINK] |
| [BUSINESS_METRIC] | [THRESHOLD] | [LINK] |

### Comparison View
```
Side-by-side comparison:
┌─────────────────┬─────────────┬─────────────┐
│ Metric          │ v[PREV]     │ v[NEW]      │
├─────────────────┼─────────────┼─────────────┤
│ Error rate      │ [VALUE]%    │ [VALUE]%    │
│ P99 latency     │ [VALUE]ms   │ [VALUE]ms   │
│ Throughput      │ [VALUE] RPS │ [VALUE] RPS │
│ [Custom metric] │ [VALUE]     │ [VALUE]     │
└─────────────────┴─────────────┴─────────────┘
```

### Alert Escalation
| Condition | Action | Contact |
|-----------|--------|---------|
| Error rate >1% | Pause rollout | [ON_CALL] |
| Error rate >5% | Automatic rollback | [ON_CALL] |
| Latency >2x baseline | Investigate | [ML_ENGINEER] |
| Business metric degradation | Escalate | [BUSINESS_OWNER] |

---

## 7. Rollback Procedure

### Rollback Triggers
| Trigger | Threshold | Auto/Manual |
|---------|-----------|-------------|
| Error rate spike | >[X]% | Automatic |
| Latency degradation | >[X]x baseline | Manual |
| Business metric drop | >[X]% | Manual |
| Customer complaints | >[X] reports | Manual |

### Rollback Steps
```markdown
## Emergency Rollback Procedure

### Immediate Actions (< 5 minutes)
1. [ ] Acknowledge alert
2. [ ] Execute rollback command:
   ```
   kubectl rollout undo deployment/[MODEL_NAME]
   # OR
   kubectl apply -f deployment-v[PREV].yaml
   ```
3. [ ] Verify old version serving traffic
4. [ ] Confirm metrics stabilizing

### Follow-up Actions (< 30 minutes)
5. [ ] Notify stakeholders of rollback
6. [ ] Capture logs and metrics for analysis
7. [ ] Scale down failed version
8. [ ] Update incident ticket

### Post-Rollback (< 24 hours)
9. [ ] Conduct root cause analysis
10. [ ] Document lessons learned
11. [ ] Plan remediation
12. [ ] Schedule re-deployment attempt
```

### Rollback Verification
| Check | Expected | Actual |
|-------|----------|--------|
| Old version serving | Yes | [ ] |
| Error rate | <[BASELINE] | [ ] |
| Latency | <[BASELINE] | [ ] |
| Business metrics | Normal | [ ] |

---

## 8. Post-Deployment

### Success Criteria
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Deployment time | <[TARGET] | [ACTUAL] | [MET/MISSED] |
| Rollback count | 0 | [COUNT] | [MET/MISSED] |
| Error rate | <[TARGET]% | [ACTUAL]% | [MET/MISSED] |
| User impact | None | [DESCRIPTION] | [MET/MISSED] |

### Documentation Updates
- [ ] Model registry updated with new version
- [ ] Runbooks updated for new version
- [ ] Architecture diagrams updated
- [ ] API documentation updated
- [ ] Changelog updated

### Stakeholder Communication
```markdown
Subject: [MODEL_NAME] v[VERSION] Deployment Complete

Deployment Summary:
- Model: [MODEL_NAME]
- Version: [VERSION] (from [PREV_VERSION])
- Status: Successful
- Duration: [DURATION]

Key Changes:
- [CHANGE_1]
- [CHANGE_2]

Metrics:
- Accuracy: [VALUE] ([DELTA] from previous)
- Latency: [VALUE]ms ([DELTA] from previous)

Next Steps:
- Monitor for 48 hours
- Review business metrics after 1 week
```
```

---

## Variables

### MODEL_NAME
Identifier for the ML model being deployed.
- Examples: "fraud-detector", "recommendation-engine", "churn-predictor"

### VERSION
Version identifier for the model.
- Examples: "v2.1.0", "20231115", "experiment-42"

### DEPLOYMENT_STRATEGY
Method for releasing the new model version.
- Examples: "Canary", "Blue-green", "Rolling", "Shadow"

### ROLLBACK_TRIGGER
Condition that initiates a rollback.
- Examples: "Error rate >5%", "P99 latency >200ms", "Conversion rate drop >10%"

---

## Usage Examples

### Example 1: High-Risk Financial Model
```
MODEL: Credit Scoring Model v3.0

PRE-DEPLOYMENT:
- Offline validation: 6 months backtesting
- Shadow mode: 2 weeks parallel scoring
- A/B test: 1% traffic for 1 week
- Regulatory review: Compliance approved

DEPLOYMENT STRATEGY:
- Type: Canary with extended observation
- Stages: 0.1% → 1% → 5% → 25% → 100%
- Stage duration: 24 hours each
- Total duration: 5 days

MONITORING:
- Primary: Default rate prediction accuracy
- Secondary: Score distribution stability
- Guardrail: Fair lending metrics

ROLLBACK PLAN:
- Automatic: Score distribution shift >10%
- Manual: Approval rate change >5%
- Instant rollback capability maintained for 30 days
```

### Example 2: Real-time Recommendation System
```
MODEL: Product Recommendations v4.2

PRE-DEPLOYMENT:
- A/B test results: +8% CTR, +3% conversion
- Latency benchmark: P99 85ms (<100ms target)
- Load test: 5000 RPS sustained

DEPLOYMENT STRATEGY:
- Type: Blue-green with canary validation
- Canary: 5% traffic for 2 hours
- Flip: 100% traffic switch
- Rollback: Instant (keep blue environment warm)

DEPLOYMENT EXECUTION:
09:00 - Deploy green environment
09:30 - Health checks pass
09:35 - Route 5% canary traffic
11:30 - Metrics validated, execute full switch
11:32 - 100% traffic on green
12:00 - Blue environment scaled to minimum (warm standby)
Next day - Blue environment decommissioned
```

### Example 3: Batch Model Update
```
MODEL: Customer Segmentation v2.0

PRE-DEPLOYMENT:
- Segment stability analysis: 85% consistency
- Business review: Marketing approved new segments
- Integration test: Downstream systems compatible

DEPLOYMENT STRATEGY:
- Type: Side-by-side comparison
- Run both versions for one batch cycle
- Compare outputs before switching

DEPLOYMENT EXECUTION:
Day 1 - Deploy v2.0 to parallel pipeline
Day 2 - Run batch job with both versions
Day 3 - Analyze segment differences with business
Day 4 - Business approves, switch primary pipeline
Day 5 - Archive v1.0 pipeline

POST-DEPLOYMENT:
- Monitor segment-based campaign performance
- Weekly segment stability check
- Monthly model refresh evaluation
```

---

## Best Practices

1. **Automate Everything** - Manual deployments introduce human error. Automate validation, deployment, and rollback.

2. **Deploy Small, Deploy Often** - Smaller changes are easier to validate and debug. Avoid big-bang deployments.

3. **Test Rollback Before You Need It** - Practice rollbacks regularly. The time to learn is not during an incident.

4. **Keep Old Version Warm** - Maintain quick rollback capability by keeping the previous version ready to serve.

5. **Monitor Business Metrics** - Technical metrics aren't enough. Track business KPIs that indicate real-world impact.

6. **Document Everything** - Future you will thank present you. Record decisions, configurations, and lessons learned.

---

## Common Pitfalls

❌ **Deploying on Fridays** - Reduced staffing for incident response
✅ Instead: Deploy early in the week with full team coverage

❌ **Skipping Staging** - Going directly to production
✅ Instead: Always validate in staging environment first

❌ **No Rollback Plan** - Assuming deployment will succeed
✅ Instead: Test rollback procedure before every deployment

❌ **Insufficient Monitoring** - Not watching during deployment
✅ Instead: Dedicated monitoring during entire rollout window

❌ **Big Bang Releases** - Deploying to 100% immediately
✅ Instead: Gradual rollout with validation at each stage

---

## Related Resources

**Tools:**
- [Argo Rollouts](https://argoproj.github.io/rollouts/) - Kubernetes progressive delivery
- [Flagger](https://flagger.app/) - Canary deployments for Kubernetes
- [MLflow](https://mlflow.org/) - Model registry and deployment
- [Seldon Core](https://www.seldon.io/) - ML model deployment platform

**Further Reading:**
- [Continuous Delivery for ML (Google)](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
- [ML Model Deployment Patterns (AWS)](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-patterns.html)

---

**Last Updated:** 2025-11-22
**Category:** AI/ML Applications > MLOps-Deployment
**Difficulty:** Intermediate
**Estimated Time:** 1-2 days for standard deployment
