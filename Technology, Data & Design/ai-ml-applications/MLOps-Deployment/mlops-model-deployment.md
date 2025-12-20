---
category: ai-ml-applications
title: MLOps Model Deployment
tags:
- model-deployment
- ml-cicd
- model-serving
- canary-deployment
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

## Template

Create a deployment plan for {MODEL_NAME} version {VERSION} targeting {DEPLOYMENT_ENVIRONMENT}.

**1. DEPLOYMENT OVERVIEW**

Understand what you're deploying and why:

Model context: What model is being deployed? What version? What's changing from the previous version? Summarize the key improvements or fixes. Assess the risk level—changes to model architecture or training data are higher risk than hyperparameter tuning.

Deployment window: When will deployment start? How long should it take? What's the deadline for rollback decision? Having clear timelines creates accountability and ensures adequate monitoring coverage.

Stakeholder roles: Who owns the model and approves deployment? Who executes the deployment? Who monitors during rollout? Who validates business metrics? Clear ownership prevents confusion during incidents.

**2. PRE-DEPLOYMENT VALIDATION**

Ensure the model is ready for production:

Quality gates: Define the metrics that must pass before deployment proceeds. Accuracy or performance metrics must exceed thresholds. Latency must meet SLA requirements. Throughput must handle expected load. Error rates must be below acceptable limits. Document required thresholds and actual values for each gate.

Version comparison: Compare the new version against the current production version. For each key metric, show the previous value, new value, and whether the change is acceptable. Regressions in any metric need explicit justification.

Pre-deployment checklist: Verify model was trained on approved dataset. Confirm offline evaluation completed successfully. Ensure shadow mode or A/B testing passed. Validate performance benchmarks met. Complete security scan with no vulnerabilities. Update documentation. Test rollback procedure. Obtain stakeholder approval. No deployment should proceed with unchecked items.

**3. DEPLOYMENT STRATEGY SELECTION**

Choose the right approach for your risk profile:

Blue-green deployment: Maintain two identical environments—blue (current) and green (new). Deploy to green, validate, then switch all traffic instantly. Provides zero downtime and instant rollback by switching back to blue. Best for high-availability requirements and when you need immediate rollback capability. Requires double the infrastructure.

Canary deployment: Route a small percentage of traffic to the new version while most traffic goes to the current version. Gradually increase the new version's traffic as metrics validate. Allows validation with real traffic at minimal risk. Best for catching issues that only appear at scale or with real user behavior. Takes longer but provides highest safety.

Rolling deployment: Gradually replace instances of the old version with the new version. More resource-efficient than blue-green but slower rollback. Good for resource-constrained environments with lower risk tolerance.

Shadow deployment: Route production traffic to both versions but only return responses from the current version. Compare outputs without user impact. Best for validating model behavior before any production exposure.

**4. CANARY ROLLOUT PLAN**

Execute gradual deployment with validation gates:

Stage 1 - Canary (1% traffic): Deploy new version to minimal traffic. Duration depends on your traffic volume—need enough requests for statistical significance. Success criteria include error rate within threshold, latency within threshold, and no anomalies in prediction distribution. Proceed only if all criteria pass.

Stage 2 - Limited (10% traffic): Increase traffic to validate at larger scale. Monitor for issues that only appear with more diverse traffic. Verify business metrics remain stable. Duration should allow capturing edge cases and variations.

Stage 3 - Broad (50% traffic): Half of production traffic tests the new version thoroughly. Any remaining issues should surface at this scale. Business stakeholders should validate business impact metrics.

Stage 4 - Full (100% traffic): Complete the rollout. Keep old version ready for quick rollback for an additional period. After the stability window passes, decommission the old version.

Traffic routing: Configure your service mesh or load balancer to split traffic by percentage. Use consistent routing (same user always hits same version) for A/B testing validity. Define routing rules declaratively so they can be version controlled and audited.

**5. INFRASTRUCTURE CONFIGURATION**

Set up the serving environment:

Model serving: Choose a serving framework appropriate to your model (TensorFlow Serving, TorchServe, Triton, or custom). Configure replica counts with minimum for baseline and maximum for scaling. Allocate appropriate CPU, memory, and GPU resources. Set autoscaling based on the right metric—CPU utilization, GPU utilization, or custom metrics like requests per replica.

Health checks: Configure liveness and readiness probes. The model should respond to health check endpoints within timeout. Failed health checks should trigger automatic restart or traffic removal. Health check intervals should balance responsiveness with overhead.

Environment configuration: Define environment-specific settings for staging vs production. Include model path, logging level, batch size, and feature store connections. Use configuration management to ensure consistency and auditability.

**6. DEPLOYMENT EXECUTION**

Follow a systematic procedure:

Preparation: Notify stakeholders of deployment start. Verify staging environment is healthy. Confirm rollback procedure is ready and tested. Open deployment monitoring dashboard with side-by-side version comparison.

Stage execution: For each deployment stage, deploy or scale the new version, verify pods or instances are healthy, route the specified traffic percentage, monitor for the stage duration, verify all metrics within thresholds, then make an explicit proceed or rollback decision. Document the decision and reasoning.

Completion: After successful full rollout, scale down the old version but keep it available for quick rollback. Maintain this warm standby for a defined period (typically 24-72 hours). After the stability period, decommission the old version completely. Update documentation. Notify stakeholders of successful completion.

**7. MONITORING DURING DEPLOYMENT**

Watch closely for problems:

Key metrics: Monitor error rate, latency percentiles (P50, P95, P99), throughput, and business metrics. Define thresholds for each metric that would indicate a problem. Display new version and old version metrics side-by-side for easy comparison.

Automated alerts: Configure alerts that fire during deployment if metrics breach thresholds. Distinguish between pause triggers (investigate before proceeding) and rollback triggers (automatic revert). Error rate spikes typically warrant automatic rollback. Latency degradation may warrant pause and investigation.

Escalation paths: Define who gets notified for different issue severities. On-call engineer handles technical issues. ML engineer investigates model-specific problems. Business owner gets involved for business metric concerns.

**8. ROLLBACK PROCEDURE**

Be ready to revert quickly:

Rollback triggers: Define conditions that require rollback—automatic (error rate exceeds threshold) and manual (business metric degradation, customer complaints). Automatic triggers execute without human decision for clear-cut failures. Manual triggers require human judgment for ambiguous situations.

Immediate rollback steps: Acknowledge the issue triggering rollback. Execute the rollback command (traffic routing change or version revert). Verify old version is serving traffic. Confirm metrics are stabilizing. This should complete within 5 minutes.

Follow-up actions: Notify stakeholders of rollback and reason. Capture logs and metrics for root cause analysis. Scale down the failed version. Document the incident. Conduct post-mortem within 24 hours. Plan remediation before re-attempting deployment.

Rollback verification: After rollback, verify old version is serving all traffic, error rate returned to baseline, latency returned to baseline, and business metrics normalized. Don't consider rollback complete until verification passes.

**9. POST-DEPLOYMENT**

Complete the deployment lifecycle:

Success criteria: Evaluate deployment against targets. Was deployment completed within the planned window? Were there any rollbacks? Did error rates stay within acceptable limits? Was there any user impact? Document actual vs target for each criterion.

Documentation updates: Update model registry with new version as production. Update runbooks with any new operational procedures. Update architecture diagrams if infrastructure changed. Update API documentation if interfaces changed. Update changelog with deployment details.

Stakeholder communication: Send deployment summary to stakeholders. Include model name, version deployed, deployment status, key changes, and metric comparisons. Describe next steps including monitoring period and planned reviews.

Deliver your deployment plan as:

1. **DEPLOYMENT OVERVIEW** - Model, version, changes, risk level, timeline, stakeholders

2. **PRE-DEPLOYMENT CHECKLIST** - Quality gates with thresholds, version comparison, approval status

3. **DEPLOYMENT STRATEGY** - Selected strategy with rationale, stage-by-stage plan

4. **INFRASTRUCTURE CONFIG** - Serving setup, scaling, health checks

5. **EXECUTION RUNBOOK** - Step-by-step procedure with commands and decision points

6. **MONITORING PLAN** - Metrics, thresholds, dashboards, alert configuration

7. **ROLLBACK PROCEDURE** - Triggers, immediate steps, verification, follow-up

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{MODEL_NAME}` | Model being deployed | "Fraud Detection", "Recommendation Engine", "Churn Predictor" |
| `{VERSION}` | Version identifier | "v2.1.0", "2024-01-15", "experiment-42" |
| `{DEPLOYMENT_ENVIRONMENT}` | Target environment and traffic | "Production (10K RPS)", "Staging", "US-East production" |

## Usage Examples

### Example 1: High-Risk Financial Model

```
Create a deployment plan for Credit Scoring Model version v3.0 targeting 
Production serving 50K decisions/day.
```

**Expected Output:**
- Overview: Major model architecture change, HIGH risk, requires extended validation
- Pre-deployment: 6-month backtesting, 2-week shadow mode, compliance approval required
- Strategy: Extended canary (0.1% → 1% → 5% → 25% → 100%), 24 hours per stage
- Monitoring: Score distribution stability, approval rate changes, fair lending metrics
- Rollback: Automatic on score distribution shift >10%, manual on approval rate change >5%
- Timeline: 5-day deployment with 30-day warm standby

### Example 2: Real-time Recommendation System

```
Create a deployment plan for Product Recommendations version v4.2 targeting 
Production serving 5000 RPS peak.
```

**Expected Output:**
- Overview: Performance optimization + new features, MEDIUM risk
- Pre-deployment: A/B test showed +8% CTR, latency P99 85ms (<100ms target)
- Strategy: Blue-green with canary validation (5% for 2 hours, then full switch)
- Monitoring: CTR, conversion rate, latency P99, error rate
- Rollback: Instant switch back to blue environment
- Timeline: 3-hour deployment, 24-hour warm standby

### Example 3: Batch Processing Model

```
Create a deployment plan for Customer Segmentation version v2.0 targeting 
Nightly batch pipeline processing 10M customers.
```

**Expected Output:**
- Overview: New segmentation approach, MEDIUM risk, requires business validation
- Pre-deployment: Segment stability analysis, marketing team approval
- Strategy: Side-by-side comparison run before switching primary pipeline
- Execution: Deploy parallel pipeline, run both versions, compare outputs, switch after approval
- Monitoring: Segment distribution, downstream campaign performance
- Rollback: Revert pipeline configuration to v1.0
- Timeline: 5-day deployment with output comparison

## Cross-References

- **MLOps:** mlops.md - End-to-end ML pipeline including deployment
- **Monitoring:** ai-monitoring-observability.md - Post-deployment monitoring setup
- **Performance:** ai-performance-optimization.md - Optimize before deploying
- **Cost:** ai-cost-optimization.md - Right-size deployment infrastructure
