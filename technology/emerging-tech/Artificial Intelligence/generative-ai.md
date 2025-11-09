---
title: Generative AI Template
category: technology/emerging-tech/Artificial Intelligence
tags: [design, machine-learning, optimization, security, technology, template]
use_cases:
  - Implementing design comprehensive generative ai systems, large language model implementations...
  - Project planning and execution
  - Strategy development
related_templates:
  - generative-ai-implementation.md
last_updated: 2025-11-09
---

# Generative AI Template

## Purpose
Design comprehensive generative AI systems, large language model implementations, prompt engineering frameworks, and AI-powered applications that leverage cutting-edge AI capabilities while ensuring safety, ethics, and business value creation.

## Template

```
You are a generative AI architect. Develop [AI_SYSTEM] for [USE_CASE] using [AI_MODELS] targeting [BUSINESS_OBJECTIVES] with [PERFORMANCE_REQUIREMENTS] while ensuring [SAFETY_MEASURES] to achieve [SUCCESS_METRICS].

AI SYSTEM OVERVIEW:

Project Context:
- Use case: [USE_CASE]
- Business domain: [BUSINESS_DOMAIN]
- Target users: [TARGET_USERS]
- Scale requirements: [SCALE_REQUIREMENTS]
- Current capabilities: [CURRENT_CAPABILITIES]
- Success criteria: [SUCCESS_CRITERIA]

Technical Requirements:
- Model types: [MODEL_TYPES]
- Performance targets: [PERFORMANCE_TARGETS]
- Latency requirements: [LATENCY_REQUIREMENTS]
- Accuracy needs: [ACCURACY_NEEDS]
- Integration points: [INTEGRATION_POINTS]
- Compliance requirements: [COMPLIANCE_REQUIREMENTS]

AI ARCHITECTURE:

```
MODEL SELECTION:

Foundation Models:
Model            | Parameters      | Capabilities    | Cost/Token     | Use Cases
-----------------|-----------------|-----------------|----------------|----------
GPT-4            | [GPT4_PARAMS]   | [GPT4_CAP]      | [GPT4_COST]    | [GPT4_USE]
Claude           | [CLAUDE_PARAMS] | [CLAUDE_CAP]    | [CLAUDE_COST]  | [CLAUDE_USE]
PaLM             | [PALM_PARAMS]   | [PALM_CAP]      | [PALM_COST]    | [PALM_USE]
LLaMA            | [LLAMA_PARAMS]  | [LLAMA_CAP]     | [LLAMA_COST]   | [LLAMA_USE]
Custom/Fine-tuned| [CUSTOM_PARAMS] | [CUSTOM_CAP]    | [CUSTOM_COST]  | [CUSTOM_USE]
Multimodal       | [MULTI_PARAMS]  | [MULTI_CAP]     | [MULTI_COST]   | [MULTI_USE]

Model Evaluation:
Criteria         | Weight          | Model A Score   | Model B Score  | Model C Score
-----------------|-----------------|-----------------|----------------|---------------
Accuracy         | [ACC_WEIGHT]    | [ACC_A]         | [ACC_B]        | [ACC_C]
Speed            | [SPEED_WEIGHT]  | [SPEED_A]       | [SPEED_B]      | [SPEED_C]
Cost             | [COST_WEIGHT]   | [COST_A]        | [COST_B]       | [COST_C]
Scalability      | [SCALE_WEIGHT]  | [SCALE_A]       | [SCALE_B]      | [SCALE_C]
Safety           | [SAFE_WEIGHT]   | [SAFE_A]        | [SAFE_B]       | [SAFE_C]

Fine-tuning Strategy:
Dataset          | Size            | Quality Score   | Preparation    | Timeline
-----------------|-----------------|-----------------|----------------|----------
Training Data    | [TRAIN_SIZE]    | [TRAIN_QUAL]    | [TRAIN_PREP]   | [TRAIN_TIME]
Validation Data  | [VAL_SIZE]      | [VAL_QUAL]      | [VAL_PREP]     | [VAL_TIME]
Test Data        | [TEST_SIZE]     | [TEST_QUAL]     | [TEST_PREP]    | [TEST_TIME]
Augmented Data   | [AUG_SIZE]      | [AUG_QUAL]      | [AUG_PREP]     | [AUG_TIME]
```

PROMPT ENGINEERING:

Prompt Design Framework:
```
PROMPT OPTIMIZATION:

Prompt Templates:
Template Type    | Structure       | Tokens          | Performance    | Use Case
-----------------|-----------------|-----------------|----------------|----------
Zero-shot        | [ZERO_STRUCT]   | [ZERO_TOKENS]   | [ZERO_PERF]    | [ZERO_USE]
Few-shot         | [FEW_STRUCT]    | [FEW_TOKENS]    | [FEW_PERF]     | [FEW_USE]
Chain-of-Thought | [COT_STRUCT]    | [COT_TOKENS]    | [COT_PERF]     | [COT_USE]
Tree-of-Thoughts | [TOT_STRUCT]    | [TOT_TOKENS]    | [TOT_PERF]     | [TOT_USE]
ReAct            | [REACT_STRUCT]  | [REACT_TOKENS]  | [REACT_PERF]   | [REACT_USE]
Constitutional   | [CONST_STRUCT]  | [CONST_TOKENS]  | [CONST_PERF]   | [CONST_USE]

Prompt Components:
Component        | Purpose         | Examples        | Best Practices | Pitfalls
-----------------|-----------------|-----------------|----------------|----------
System Message   | [SYS_PURPOSE]   | [SYS_EXAMPLE]   | [SYS_BEST]     | [SYS_PIT]
Context          | [CTX_PURPOSE]   | [CTX_EXAMPLE]   | [CTX_BEST]     | [CTX_PIT]
Instructions     | [INST_PURPOSE]  | [INST_EXAMPLE]  | [INST_BEST]    | [INST_PIT]
Examples         | [EX_PURPOSE]    | [EX_EXAMPLE]    | [EX_BEST]      | [EX_PIT]
Constraints      | [CON_PURPOSE]   | [CON_EXAMPLE]   | [CON_BEST]     | [CON_PIT]
Output Format    | [OUT_PURPOSE]   | [OUT_EXAMPLE]   | [OUT_BEST]     | [OUT_PIT]

Testing & Iteration:
Test Type        | Sample Size     | Success Rate    | Failure Modes  | Improvements
-----------------|-----------------|-----------------|----------------|-------------
Accuracy Test    | [ACC_SAMPLE]    | [ACC_SUCCESS]   | [ACC_FAIL]     | [ACC_IMPROVE]
Robustness Test  | [ROB_SAMPLE]    | [ROB_SUCCESS]   | [ROB_FAIL]     | [ROB_IMPROVE]
Edge Cases       | [EDGE_SAMPLE]   | [EDGE_SUCCESS]  | [EDGE_FAIL]    | [EDGE_IMPROVE]
Adversarial      | [ADV_SAMPLE]    | [ADV_SUCCESS]   | [ADV_FAIL]     | [ADV_IMPROVE]
```

RAG IMPLEMENTATION:

Retrieval-Augmented Generation:
```
KNOWLEDGE MANAGEMENT:

Vector Database:
Database         | Dimensions      | Index Type      | Query Speed    | Storage
-----------------|-----------------|-----------------|----------------|--------
Pinecone         | [PINE_DIM]      | [PINE_INDEX]    | [PINE_SPEED]   | [PINE_STORE]
Weaviate         | [WEAV_DIM]      | [WEAV_INDEX]    | [WEAV_SPEED]   | [WEAV_STORE]
ChromaDB         | [CHROMA_DIM]    | [CHROMA_INDEX]  | [CHROMA_SPEED] | [CHROMA_STORE]
Qdrant           | [QDRANT_DIM]    | [QDRANT_INDEX]  | [QDRANT_SPEED] | [QDRANT_STORE]
Custom           | [CUSTOM_DIM]    | [CUSTOM_INDEX]  | [CUSTOM_SPEED] | [CUSTOM_STORE]

Document Processing:
Process Step     | Method          | Quality Metrics | Performance    | Cost
-----------------|-----------------|-----------------|----------------|------
Ingestion        | [ING_METHOD]    | [ING_QUALITY]   | [ING_PERF]     | [ING_COST]
Chunking         | [CHUNK_METHOD]  | [CHUNK_QUALITY] | [CHUNK_PERF]   | [CHUNK_COST]
Embedding        | [EMB_METHOD]    | [EMB_QUALITY]   | [EMB_PERF]     | [EMB_COST]
Indexing         | [INDEX_METHOD]  | [INDEX_QUALITY] | [INDEX_PERF]   | [INDEX_COST]
Retrieval        | [RET_METHOD]    | [RET_QUALITY]   | [RET_PERF]     | [RET_COST]

Context Management:
Strategy         | Context Window  | Relevance Score | Reranking      | Fusion Method
-----------------|-----------------|-----------------|----------------|---------------
Top-K            | [TOPK_WINDOW]   | [TOPK_SCORE]    | [TOPK_RERANK]  | [TOPK_FUSION]
Semantic Search  | [SEM_WINDOW]    | [SEM_SCORE]     | [SEM_RERANK]   | [SEM_FUSION]
Hybrid           | [HYB_WINDOW]    | [HYB_SCORE]     | [HYB_RERANK]   | [HYB_FUSION]
Contextual       | [CTX_WINDOW]    | [CTX_SCORE]     | [CTX_RERANK]   | [CTX_FUSION]
```

AGENT FRAMEWORKS:

AI Agent Architecture:
```
AUTONOMOUS AGENTS:

Agent Types:
Agent Type       | Capabilities    | Tools Access    | Autonomy Level | Use Cases
-----------------|-----------------|-----------------|----------------|----------
Task Agent       | [TASK_CAP]      | [TASK_TOOLS]    | [TASK_AUTO]    | [TASK_CASES]
Conversational   | [CONV_CAP]      | [CONV_TOOLS]    | [CONV_AUTO]    | [CONV_CASES]
Research Agent   | [RES_CAP]       | [RES_TOOLS]     | [RES_AUTO]     | [RES_CASES]
Code Agent       | [CODE_CAP]      | [CODE_TOOLS]    | [CODE_AUTO]    | [CODE_CASES]
Multi-Agent      | [MULTI_CAP]     | [MULTI_TOOLS]   | [MULTI_AUTO]   | [MULTI_CASES]

Tool Integration:
Tool Category    | APIs/Services   | Authentication  | Rate Limits    | Cost
-----------------|-----------------|-----------------|----------------|------
Search           | [SEARCH_API]    | [SEARCH_AUTH]   | [SEARCH_RATE]  | [SEARCH_COST]
Code Execution   | [CODE_API]      | [CODE_AUTH]     | [CODE_RATE]    | [CODE_COST]
Database         | [DB_API]        | [DB_AUTH]       | [DB_RATE]      | [DB_COST]
External Systems | [EXT_API]       | [EXT_AUTH]      | [EXT_RATE]     | [EXT_COST]
Memory Systems   | [MEM_API]       | [MEM_AUTH]      | [MEM_RATE]     | [MEM_COST]

Orchestration:
Component        | Function        | Scalability     | Fault Tolerance| Monitoring
-----------------|-----------------|-----------------|----------------|------------
Task Queue       | [QUEUE_FUNC]    | [QUEUE_SCALE]   | [QUEUE_FAULT]  | [QUEUE_MON]
State Management | [STATE_FUNC]    | [STATE_SCALE]   | [STATE_FAULT]  | [STATE_MON]
Error Handling   | [ERROR_FUNC]    | [ERROR_SCALE]   | [ERROR_FAULT]  | [ERROR_MON]
Workflow Engine  | [WORK_FUNC]     | [WORK_SCALE]    | [WORK_FAULT]   | [WORK_MON]
```

SAFETY & ETHICS:

AI Safety Framework:
```
RESPONSIBLE AI:

Safety Measures:
Risk Type        | Detection Method| Mitigation      | Monitoring     | Response Plan
-----------------|-----------------|-----------------|----------------|---------------
Hallucination    | [HALL_DETECT]   | [HALL_MITIG]    | [HALL_MON]     | [HALL_RESP]
Bias             | [BIAS_DETECT]   | [BIAS_MITIG]    | [BIAS_MON]     | [BIAS_RESP]
Toxic Output     | [TOX_DETECT]    | [TOX_MITIG]     | [TOX_MON]      | [TOX_RESP]
Data Leakage     | [LEAK_DETECT]   | [LEAK_MITIG]    | [LEAK_MON]     | [LEAK_RESP]
Adversarial      | [ADV_DETECT]    | [ADV_MITIG]     | [ADV_MON]      | [ADV_RESP]
Misuse           | [MIS_DETECT]    | [MIS_MITIG]     | [MIS_MON]      | [MIS_RESP]

Content Filtering:
Filter Type      | Sensitivity     | False Positive  | False Negative | Override Process
-----------------|-----------------|-----------------|----------------|------------------
Profanity        | [PROF_SENS]     | [PROF_FP]       | [PROF_FN]      | [PROF_OVER]
Violence         | [VIO_SENS]      | [VIO_FP]        | [VIO_FN]       | [VIO_OVER]
Adult Content    | [ADULT_SENS]    | [ADULT_FP]      | [ADULT_FN]     | [ADULT_OVER]
PII/Sensitive    | [PII_SENS]      | [PII_FP]        | [PII_FN]       | [PII_OVER]
Misinformation   | [MIS_SENS]      | [MIS_FP]        | [MIS_FN]       | [MIS_OVER]

Alignment Techniques:
Technique        | Implementation  | Effectiveness   | Overhead       | Trade-offs
-----------------|-----------------|-----------------|----------------|------------
RLHF             | [RLHF_IMPL]     | [RLHF_EFF]      | [RLHF_OVER]    | [RLHF_TRADE]
Constitutional AI| [CONST_IMPL]    | [CONST_EFF]     | [CONST_OVER]   | [CONST_TRADE]
Red Teaming      | [RED_IMPL]      | [RED_EFF]       | [RED_OVER]     | [RED_TRADE]
Adversarial Training| [ADV_IMPL]   | [ADV_EFF]       | [ADV_OVER]     | [ADV_TRADE]
```

DEPLOYMENT & SCALING:

Infrastructure Design:
```
PRODUCTION DEPLOYMENT:

Deployment Architecture:
Component        | Technology      | Scaling Strategy| HA/DR Plan     | Cost
-----------------|-----------------|-----------------|----------------|------
API Gateway      | [API_TECH]      | [API_SCALE]     | [API_HA]       | [API_COST]
Model Serving    | [MODEL_TECH]    | [MODEL_SCALE]   | [MODEL_HA]     | [MODEL_COST]
Load Balancer    | [LB_TECH]       | [LB_SCALE]      | [LB_HA]        | [LB_COST]
Cache Layer      | [CACHE_TECH]    | [CACHE_SCALE]   | [CACHE_HA]     | [CACHE_COST]
Monitoring       | [MON_TECH]      | [MON_SCALE]     | [MON_HA]       | [MON_COST]

Performance Optimization:
Optimization     | Current         | Target          | Method         | Impact
-----------------|-----------------|-----------------|----------------|--------
Latency          | [LAT_CURR]      | [LAT_TARG]      | [LAT_METHOD]   | [LAT_IMPACT]
Throughput       | [THRU_CURR]     | [THRU_TARG]     | [THRU_METHOD]  | [THRU_IMPACT]
Cost per Request | [COST_CURR]     | [COST_TARG]     | [COST_METHOD]  | [COST_IMPACT]
Model Size       | [SIZE_CURR]     | [SIZE_TARG]     | [SIZE_METHOD]  | [SIZE_IMPACT]
Memory Usage     | [MEM_CURR]      | [MEM_TARG]      | [MEM_METHOD]   | [MEM_IMPACT]

Scaling Strategy:
Metric           | Threshold       | Scaling Action  | Cool-down      | Max Instances
-----------------|-----------------|-----------------|----------------|---------------
Request Rate     | [REQ_THRESH]    | [REQ_ACTION]    | [REQ_COOL]     | [REQ_MAX]
CPU Usage        | [CPU_THRESH]    | [CPU_ACTION]    | [CPU_COOL]     | [CPU_MAX]
Memory Usage     | [MEM_THRESH]    | [MEM_ACTION]    | [MEM_COOL]     | [MEM_MAX]
Queue Length     | [QUEUE_THRESH]  | [QUEUE_ACTION]  | [QUEUE_COOL]   | [QUEUE_MAX]
```

MONITORING & EVALUATION:

Performance Metrics:
```
AI SYSTEM MONITORING:

Quality Metrics:
Metric           | Target          | Current         | Trend          | Alert Threshold
-----------------|-----------------|-----------------|----------------|----------------
Accuracy         | [ACC_TARGET]    | [ACC_CURRENT]   | [ACC_TREND]    | [ACC_ALERT]
F1 Score         | [F1_TARGET]     | [F1_CURRENT]    | [F1_TREND]     | [F1_ALERT]
Perplexity       | [PERP_TARGET]   | [PERP_CURRENT]  | [PERP_TREND]   | [PERP_ALERT]
BLEU Score       | [BLEU_TARGET]   | [BLEU_CURRENT]  | [BLEU_TREND]   | [BLEU_ALERT]
Human Evaluation | [HUMAN_TARGET]  | [HUMAN_CURRENT] | [HUMAN_TREND]  | [HUMAN_ALERT]

Operational Metrics:
Metric           | SLA             | Current         | Availability   | MTTR
-----------------|-----------------|-----------------|----------------|------
Uptime           | [UP_SLA]        | [UP_CURRENT]    | [UP_AVAIL]     | [UP_MTTR]
Response Time    | [RESP_SLA]      | [RESP_CURRENT]  | [RESP_AVAIL]   | [RESP_MTTR]
Error Rate       | [ERR_SLA]       | [ERR_CURRENT]   | [ERR_AVAIL]    | [ERR_MTTR]
Token Usage      | [TOK_SLA]       | [TOK_CURRENT]   | [TOK_AVAIL]    | [TOK_MTTR]

Business Metrics:
Metric           | Target          | Actual          | Impact         | ROI
-----------------|-----------------|-----------------|----------------|-----
User Adoption    | [ADOPT_TARGET]  | [ADOPT_ACTUAL]  | [ADOPT_IMPACT] | [ADOPT_ROI]
Cost Savings     | [SAVE_TARGET]   | [SAVE_ACTUAL]   | [SAVE_IMPACT]  | [SAVE_ROI]
Revenue Impact   | [REV_TARGET]    | [REV_ACTUAL]    | [REV_IMPACT]   | [REV_ROI]
Efficiency Gain  | [EFF_TARGET]    | [EFF_ACTUAL]    | [EFF_IMPACT]   | [EFF_ROI]
```

CONTINUOUS IMPROVEMENT:

Evolution Strategy:
```
MODEL LIFECYCLE:

Update Cycle:
Phase            | Frequency       | Activities      | Resources      | Validation
-----------------|-----------------|-----------------|----------------|------------
Data Collection  | [DATA_FREQ]     | [DATA_ACT]      | [DATA_RES]     | [DATA_VAL]
Model Retraining | [TRAIN_FREQ]    | [TRAIN_ACT]     | [TRAIN_RES]    | [TRAIN_VAL]
A/B Testing      | [AB_FREQ]       | [AB_ACT]        | [AB_RES]       | [AB_VAL]
Deployment       | [DEPLOY_FREQ]   | [DEPLOY_ACT]    | [DEPLOY_RES]   | [DEPLOY_VAL]
Evaluation       | [EVAL_FREQ]     | [EVAL_ACT]      | [EVAL_RES]     | [EVAL_VAL]

Innovation Pipeline:
Innovation       | Maturity        | Potential Impact| Investment     | Timeline
-----------------|-----------------|-----------------|----------------|----------
[INNOVATION_1]   | [MAT_1]         | [IMPACT_1]      | [INVEST_1]     | [TIME_1]
[INNOVATION_2]   | [MAT_2]         | [IMPACT_2]      | [INVEST_2]     | [TIME_2]
[INNOVATION_3]   | [MAT_3]         | [IMPACT_3]      | [INVEST_3]     | [TIME_3]
[INNOVATION_4]   | [MAT_4]         | [IMPACT_4]      | [INVEST_4]     | [TIME_4]
```

GENERATIVE AI OUTPUT:
[Generate comprehensive AI system design]

System Type: [FINAL_SYSTEM_TYPE]
Model Architecture: [FINAL_ARCHITECTURE]
Expected Performance: [FINAL_PERFORMANCE]
Implementation Timeline: [FINAL_TIMELINE]

[COMPLETE_AI_SYSTEM]

---

AI System Summary:
- Use case impact: [USE_CASE_SUMMARY]
- Technical approach: [TECHNICAL_SUMMARY]
- Safety measures: [SAFETY_SUMMARY]
- Deployment strategy: [DEPLOYMENT_SUMMARY]
- Success metrics: [SUCCESS_SUMMARY]

OUTPUT: Deliver comprehensive generative AI system with:
1. Model selection and architecture
2. Prompt engineering framework
3. RAG implementation
4. Agent frameworks
5. Safety and ethics protocols
6. Deployment infrastructure
7. Monitoring systems
8. Continuous improvement plan
```

## Variables
[All 450+ variables for comprehensive generative AI systems]

## Usage Examples

### Example 1: Enterprise Chatbot
```
AI_SYSTEM: "Customer service AI assistant"
USE_CASE: "24/7 customer support automation"
AI_MODELS: "GPT-4, custom fine-tuned model, RAG system"
BUSINESS_OBJECTIVES: "Reduce support costs 50%, improve satisfaction"
PERFORMANCE_REQUIREMENTS: "<2 second response, 95% accuracy"
SAFETY_MEASURES: "PII protection, content filtering, human escalation"
SUCCESS_METRICS: "CSAT >4.5, 70% query resolution, 50% cost reduction"
```

### Example 2: Code Generation Platform
```
AI_SYSTEM: "AI-powered development assistant"
USE_CASE: "Accelerate software development"
AI_MODELS: "Codex, CodeLLaMA, custom models"
BUSINESS_OBJECTIVES: "2x developer productivity"
PERFORMANCE_REQUIREMENTS: "Real-time suggestions, secure code generation"
SAFETY_MEASURES: "Code security scanning, license compliance"
SUCCESS_METRICS: "50% reduction in development time, code quality metrics"
```

### Example 3: Content Creation Suite
```
AI_SYSTEM: "Multi-modal content generation platform"
USE_CASE: "Marketing content automation"
AI_MODELS: "GPT-4, DALL-E, Stable Diffusion, custom models"
BUSINESS_OBJECTIVES: "Scale content production 10x"
PERFORMANCE_REQUIREMENTS: "High quality, brand-aligned, multi-format"
SAFETY_MEASURES: "Brand safety, copyright protection, quality control"
SUCCESS_METRICS: "Content engagement rates, production efficiency"
```

## Customization Options

1. **AI Applications**
   - Chatbots & assistants
   - Content generation
   - Code generation
   - Data analysis
   - Translation
   - Summarization
   - Question answering
   - Creative tools

2. **Model Types**
   - Large language models
   - Multi-modal models
   - Specialized models
   - Fine-tuned models
   - Ensemble models
   - Edge models
   - Domain-specific
   - Custom architectures

3. **Deployment Modes**
   - Cloud-based
   - On-premises
   - Edge deployment
   - Hybrid cloud
   - Serverless
   - Containerized
   - API-based
   - Embedded

4. **Safety Levels**
   - Consumer applications
   - Enterprise use
   - Healthcare/Medical
   - Financial services
   - Legal applications
   - Education
   - Government
   - Critical infrastructure

5. **Scale Requirements**
   - Prototype/POC
   - Small scale
   - Department level
   - Enterprise wide
   - Consumer scale
   - Global deployment
   - Real-time systems
   - Batch processing