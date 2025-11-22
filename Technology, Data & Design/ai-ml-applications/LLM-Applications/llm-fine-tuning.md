---
category: ai-ml-applications/LLM-Applications
last_updated: 2025-11-12
title: LLM Fine-Tuning & Customization
tags:
- ai-ml
- llm
- fine-tuning
- model-training
- customization
use_cases:
- Fine-tuning LLMs for domain-specific tasks and terminology
- Customizing models for consistent brand voice and style
- Adapting models for specialized use cases (legal, medical, technical)
- Improving task performance beyond what prompting achieves
related_templates:
- ai-ml-applications/LLM-Applications/llm-application-development.md
- ai-ml-applications/LLM-Applications/prompt-engineering-workflows.md
- ai-ml-applications/AI-Product-Development/ai-product-evaluation.md
- ai-ml-applications/MLOps-Deployment/mlops-model-deployment.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: template
difficulty: intermediate
slug: llm-fine-tuning
---

# LLM Fine-Tuning & Customization Template

## Purpose
Systematically fine-tune and customize Large Language Models to achieve better performance on specific tasks, domains, or style requirements beyond what prompt engineering alone can accomplish.

## Quick Start

**Need to evaluate if fine-tuning is right for you?** Use this decision framework:

### Minimal Example
```python
# Simple fine-tuning workflow with OpenAI

# 1. Prepare training data
training_data = []
for example in your_examples:
    training_data.append({
        "messages": [
            {"role": "system", "content": "You are a legal document analyzer"},
            {"role": "user", "content": example["input"]},
            {"role": "assistant", "content": example["expected_output"]}
        ]
    })

# Save to JSONL
with open("training_data.jsonl", "w") as f:
    for item in training_data:
        f.write(json.dumps(item) + "\n")

# 2. Upload training file
client = OpenAI()
file = client.files.create(
    file=open("training_data.jsonl", "rb"),
    purpose="fine-tune"
)

# 3. Create fine-tuning job
job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo",
    hyperparameters={
        "n_epochs": 3
    }
)

# 4. Use fine-tuned model
response = client.chat.completions.create(
    model=job.fine_tuned_model,
    messages=[{"role": "user", "content": "Analyze this contract..."}]
)
```

### When to Use Fine-Tuning
✅ **Use fine-tuning when:**
- Consistent format/style required that prompting doesn't achieve
- Domain-specific terminology not well-handled by base models
- Performance improvement worth the cost and effort
- Need latency reduction (smaller fine-tuned model vs large prompted model)
- Have 100+ high-quality training examples

❌ **Don't fine-tune when:**
- Prompting achieves acceptable results
- Insufficient training data (<100 examples)
- Task is too general or frequently changing
- Cost/complexity not justified by improvement

### Basic 5-Step Workflow
1. **Evaluate Need** - Establish baseline with prompting, identify gaps
2. **Prepare Data** - Collect, clean, and format training examples
3. **Train Model** - Fine-tune with appropriate hyperparameters
4. **Evaluate Performance** - Compare against baseline on held-out test set
5. **Deploy & Monitor** - Launch fine-tuned model, track performance

---

## Template

```
You are an expert in LLM fine-tuning and model customization. Help me fine-tune [BASE_MODEL] for [TASK_DESCRIPTION] using [TRAINING_DATA] to achieve [PERFORMANCE_GOALS] for [USE_CASE].

FINE-TUNING CONTEXT:
Project Overview:
- Task: [SPECIFIC_TASK]
- Current approach: [CURRENT_SOLUTION]
- Current performance: [BASELINE_METRICS]
- Target performance: [TARGET_METRICS]
- Improvement needed: [SPECIFIC_GAPS]

Model Selection:
- Base model: [GPT3.5/GPT4/CLAUDE/LLAMA/OTHER]
- Model size: [SMALL/MEDIUM/LARGE]
- Fine-tuning method: [FULL_FINE_TUNE/LORA/QLORA/PROMPT_TUNING]
- Infrastructure: [CLOUD_PROVIDER/ON_PREM]

Data Context:
- Training examples available: [NUMBER]
- Data quality: [HIGH/MEDIUM/LOW]
- Domain: [DOMAIN_DESCRIPTION]
- Example format: [INPUT_OUTPUT_FORMAT]
- Label quality: [HOW_LABELED]

### 1. DECISION FRAMEWORK

When to Fine-Tune vs. Other Approaches:

Decision Tree:
```
Do you need consistent output format?
├─ No → Try structured prompting first
└─ Yes → Can prompting + few-shot achieve it?
    ├─ Yes → Use prompting (cheaper, simpler)
    └─ No → Continue evaluation

Is domain knowledge missing from base model?
├─ No → Fine-tuning may not help much
└─ Yes → Do you have 100+ quality examples?
    ├─ No → RAG (retrieval) may be better
    └─ Yes → Fine-tuning is promising

Is cost/latency critical?
├─ No → Prompting large model may be sufficient
└─ Yes → Fine-tuned smaller model worth exploring

Can you maintain the model?
├─ No → Stick with prompted APIs
└─ Yes → Fine-tuning is feasible
```

Comparison of Approaches:
```
Approach: Prompting
Pros: Fast to iterate, no training needed, works immediately
Cons: Higher latency, higher cost per call, less consistent
Best for: Prototyping, general tasks, frequently changing requirements

Approach: RAG (Retrieval)
Pros: Easy to update knowledge, good for factual tasks
Cons: Retrieval quality limits, added complexity
Best for: Q&A over documents, knowledge-intensive tasks

Approach: Fine-tuning
Pros: Best task performance, consistent outputs, can use smaller models
Cons: Needs training data, slower to iterate, maintenance overhead
Best for: Specific formats, domain adaptation, production optimization

Approach: Hybrid (RAG + Fine-tuning)
Pros: Best of both worlds
Cons: Most complex
Best for: Domain-specific Q&A systems, specialized applications
```

### 2. DATA PREPARATION

Data Collection:
```python
class TrainingDataCollector:
    """Collect and organize training examples"""

    def __init__(self, task_type: str):
        self.task_type = task_type
        self.examples = []

    def add_example(self, input_text: str, output_text: str, metadata: dict = None):
        """Add training example"""
        example = {
            "input": input_text,
            "output": output_text,
            "metadata": metadata or {},
            "added_at": datetime.now()
        }

        # Validate example
        if self.validate_example(example):
            self.examples.append(example)

    def collect_from_production(self, limit: int = 1000):
        """Collect examples from production logs"""
        # Find high-quality interactions
        # - High user satisfaction ratings
        # - Verified correct outputs
        # - Diverse inputs
        pass

    def collect_from_human_labeling(self, inputs: list[str]):
        """Get human-labeled examples"""
        # Send to labeling platform
        # Quality control with multiple annotators
        # Resolve disagreements
        pass

    def validate_example(self, example: dict) -> bool:
        """Ensure example is valid"""
        # Check format
        if not example["input"] or not example["output"]:
            return False

        # Check length
        if len(example["input"]) > MAX_INPUT_LENGTH:
            return False

        # Check quality
        if self.is_low_quality(example):
            return False

        return True

    def is_low_quality(self, example: dict) -> bool:
        """Detect low-quality examples"""
        output = example["output"]

        # Too short
        if len(output) < 10:
            return True

        # Repetitive
        if is_repetitive(output):
            return True

        # Contains errors
        if contains_obvious_errors(output):
            return True

        return False
```

Data Formatting:
```python
def format_for_openai(examples: list[dict]) -> list[dict]:
    """Format examples for OpenAI fine-tuning"""

    formatted = []
    for ex in examples:
        formatted.append({
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": ex["input"]},
                {"role": "assistant", "content": ex["output"]}
            ]
        })

    return formatted

def format_for_anthropic(examples: list[dict]) -> list[dict]:
    """Format examples for Anthropic fine-tuning"""

    # Anthropic format (as of 2025)
    formatted = []
    for ex in examples:
        formatted.append({
            "prompt": f"{SYSTEM_PROMPT}\n\nHuman: {ex['input']}\n\nAssistant:",
            "completion": ex["output"]
        })

    return formatted

def format_for_huggingface(examples: list[dict]) -> Dataset:
    """Format examples for Hugging Face fine-tuning"""

    from datasets import Dataset

    data = {
        "text": [
            f"{PROMPT_TEMPLATE.format(input=ex['input'])}\n{ex['output']}"
            for ex in examples
        ]
    }

    return Dataset.from_dict(data)
```

Data Quality Checks:
```python
def analyze_dataset_quality(examples: list[dict]) -> dict:
    """Analyze training data quality"""

    analysis = {
        "total_examples": len(examples),
        "avg_input_length": np.mean([len(ex["input"]) for ex in examples]),
        "avg_output_length": np.mean([len(ex["output"]) for ex in examples]),
        "unique_inputs": len(set(ex["input"] for ex in examples)),
        "diversity_score": calculate_diversity(examples),
        "format_consistency": check_format_consistency(examples),
        "quality_issues": find_quality_issues(examples)
    }

    # Recommendations
    recommendations = []

    if analysis["total_examples"] < 100:
        recommendations.append("⚠️ Need more examples (minimum 100, ideal 1000+)")

    if analysis["diversity_score"] < 0.5:
        recommendations.append("⚠️ Low diversity - collect more varied examples")

    if analysis["format_consistency"] < 0.9:
        recommendations.append("⚠️ Inconsistent output format - review examples")

    if analysis["quality_issues"]:
        recommendations.append(f"⚠️ Found {len(analysis['quality_issues'])} quality issues")

    analysis["recommendations"] = recommendations

    return analysis
```

Train/Validation/Test Split:
```python
def split_dataset(examples: list[dict], train_size: float = 0.8, val_size: float = 0.1):
    """Split data into train/val/test sets"""

    # Shuffle
    random.shuffle(examples)

    # Split
    n = len(examples)
    train_end = int(n * train_size)
    val_end = train_end + int(n * val_size)

    train_set = examples[:train_end]
    val_set = examples[train_end:val_end]
    test_set = examples[val_end:]

    # Ensure test set is representative
    if not is_representative(test_set, examples):
        # Stratified split instead
        train_set, val_set, test_set = stratified_split(examples)

    return {
        "train": train_set,
        "validation": val_set,
        "test": test_set,
        "stats": {
            "train_count": len(train_set),
            "val_count": len(val_set),
            "test_count": len(test_set)
        }
    }
```

### 3. FINE-TUNING EXECUTION

OpenAI Fine-Tuning:
```python
def finetune_openai(training_file: str, model: str = "gpt-3.5-turbo") -> dict:
    """Fine-tune OpenAI model"""

    client = OpenAI()

    # Upload training file
    train_file = client.files.create(
        file=open(training_file, "rb"),
        purpose="fine-tune"
    )

    # Optional: Upload validation file
    val_file = client.files.create(
        file=open(validation_file, "rb"),
        purpose="fine-tune"
    ) if validation_file else None

    # Create fine-tuning job
    job = client.fine_tuning.jobs.create(
        training_file=train_file.id,
        validation_file=val_file.id if val_file else None,
        model=model,
        hyperparameters={
            "n_epochs": 3,  # 3-4 epochs typical
            "batch_size": "auto",  # Let OpenAI optimize
            "learning_rate_multiplier": "auto"
        },
        suffix="my-task-v1"  # Name for fine-tuned model
    )

    print(f"Fine-tuning job created: {job.id}")

    # Monitor progress
    while True:
        job_status = client.fine_tuning.jobs.retrieve(job.id)
        print(f"Status: {job_status.status}")

        if job_status.status == "succeeded":
            return {
                "model_id": job_status.fine_tuned_model,
                "job_id": job.id,
                "metrics": job_status.result_files
            }
        elif job_status.status == "failed":
            raise Exception(f"Fine-tuning failed: {job_status.error}")

        time.sleep(60)  # Check every minute
```

Hugging Face Fine-Tuning (LoRA):
```python
def finetune_with_lora(model_name: str, dataset: Dataset) -> str:
    """Fine-tune using LoRA (parameter-efficient)"""

    from transformers import (
        AutoModelForCausalLM,
        AutoTokenizer,
        TrainingArguments,
        Trainer
    )
    from peft import LoraConfig, get_peft_model

    # Load base model
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        load_in_8bit=True,  # Memory efficiency
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # LoRA configuration
    lora_config = LoraConfig(
        r=8,  # LoRA rank
        lora_alpha=32,
        target_modules=["q_proj", "v_proj"],  # Which layers to adapt
        lora_dropout=0.1,
        bias="none",
        task_type="CAUSAL_LM"
    )

    # Apply LoRA
    model = get_peft_model(model, lora_config)

    # Training arguments
    training_args = TrainingArguments(
        output_dir="./results",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        warmup_steps=100,
        learning_rate=2e-4,
        logging_steps=10,
        save_strategy="epoch",
        evaluation_strategy="epoch"
    )

    # Train
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"]
    )

    trainer.train()

    # Save
    model.save_pretrained("./finetuned_model")
    tokenizer.save_pretrained("./finetuned_model")

    return "./finetuned_model"
```

Hyperparameter Tuning:
```python
def tune_hyperparameters(train_data: Dataset, val_data: Dataset):
    """Find optimal hyperparameters"""

    import optuna

    def objective(trial):
        # Suggest hyperparameters
        learning_rate = trial.suggest_float("learning_rate", 1e-5, 1e-3, log=True)
        batch_size = trial.suggest_categorical("batch_size", [4, 8, 16])
        epochs = trial.suggest_int("epochs", 2, 5)

        # Train with these hyperparameters
        metrics = train_model(
            train_data,
            val_data,
            learning_rate=learning_rate,
            batch_size=batch_size,
            epochs=epochs
        )

        # Return validation metric to optimize
        return metrics["val_loss"]

    # Run optimization
    study = optuna.create_study(direction="minimize")
    study.optimize(objective, n_trials=20)

    print("Best hyperparameters:", study.best_params)
    return study.best_params
```

### 4. EVALUATION

Comprehensive Evaluation:
```python
def evaluate_finetuned_model(
    model_id: str,
    test_set: list[dict],
    baseline_model_id: str = None
) -> dict:
    """Evaluate fine-tuned model against test set"""

    results = {
        "accuracy": [],
        "bleu_score": [],
        "rouge_score": [],
        "latency": [],
        "cost": [],
        "human_eval": []
    }

    for example in test_set:
        start = time.time()

        # Get fine-tuned model response
        ft_response = generate(model_id, example["input"])

        latency = time.time() - start

        # Compare to expected output
        accuracy = evaluate_accuracy(ft_response, example["output"])
        bleu = calculate_bleu(ft_response, example["output"])
        rouge = calculate_rouge(ft_response, example["output"])

        results["accuracy"].append(accuracy)
        results["bleu_score"].append(bleu)
        results["rouge_score"].append(rouge)
        results["latency"].append(latency)
        results["cost"].append(estimate_cost(ft_response))

        # Optional: Compare to baseline
        if baseline_model_id:
            baseline_response = generate(baseline_model_id, example["input"])
            improvement = compare_responses(
                ft_response,
                baseline_response,
                example["output"]
            )
            results["improvement"] = results.get("improvement", [])
            results["improvement"].append(improvement)

    # Aggregate metrics
    summary = {
        "avg_accuracy": np.mean(results["accuracy"]),
        "avg_bleu": np.mean(results["bleu_score"]),
        "avg_rouge": np.mean(results["rouge_score"]),
        "avg_latency_ms": np.mean(results["latency"]) * 1000,
        "avg_cost": np.mean(results["cost"])
    }

    if baseline_model_id:
        summary["avg_improvement"] = np.mean(results["improvement"])

    return summary

def human_evaluation(model_id: str, test_examples: list[dict], n: int = 50):
    """Human evaluation of outputs"""

    # Sample examples
    sample = random.sample(test_examples, min(n, len(test_examples)))

    ratings = []
    for ex in sample:
        response = generate(model_id, ex["input"])

        # Present to human evaluator
        rating = show_to_evaluator(
            input=ex["input"],
            expected=ex["output"],
            actual=response,
            criteria=[
                "Accuracy",
                "Completeness",
                "Clarity",
                "Tone appropriateness"
            ]
        )

        ratings.append(rating)

    return {
        "overall_quality": np.mean([r["overall"] for r in ratings]),
        "accuracy": np.mean([r["accuracy"] for r in ratings]),
        "completeness": np.mean([r["completeness"] for r in ratings]),
        "clarity": np.mean([r["clarity"] for r in ratings]),
        "tone": np.mean([r["tone"] for r in ratings])
    }
```

A/B Testing:
```python
def ab_test_models(
    model_a_id: str,
    model_b_id: str,
    traffic_split: float = 0.5,
    duration_days: int = 7
):
    """A/B test fine-tuned vs baseline model"""

    test_results = {
        "model_a": {"responses": [], "metrics": []},
        "model_b": {"responses": [], "metrics": []}
    }

    # Run for duration
    start_time = datetime.now()
    while (datetime.now() - start_time).days < duration_days:

        # Route traffic
        if random.random() < traffic_split:
            model_id = model_a_id
            variant = "model_a"
        else:
            model_id = model_b_id
            variant = "model_b"

        # Handle request
        response, metrics = handle_request(model_id)

        # Record results
        test_results[variant]["responses"].append(response)
        test_results[variant]["metrics"].append(metrics)

    # Analyze results
    return analyze_ab_test(test_results)
```

### 5. PRODUCTION DEPLOYMENT

Deployment Strategy:
```python
class FineTunedModelDeployment:
    """Deploy and manage fine-tuned models"""

    def __init__(self, model_id: str, config: dict):
        self.model_id = model_id
        self.config = config
        self.baseline_model = config.get("baseline_model")

    def gradual_rollout(self, stages: list[dict]):
        """Gradually increase traffic to fine-tuned model"""

        for stage in stages:
            percentage = stage["percentage"]
            duration = stage["duration_hours"]

            print(f"Rolling out to {percentage}% of traffic for {duration}h")

            # Route percentage of traffic to fine-tuned model
            self.set_traffic_split(self.model_id, percentage)

            # Monitor for duration
            time.sleep(duration * 3600)

            # Check metrics
            metrics = self.get_metrics(duration)

            if not self.meets_criteria(metrics, stage["criteria"]):
                # Rollback
                print("Metrics below threshold, rolling back")
                self.set_traffic_split(self.model_id, 0)
                return False

        # Full rollout
        self.set_traffic_split(self.model_id, 100)
        return True

    def canary_deployment(self, canary_duration_hours: int = 24):
        """Canary deployment with automatic rollback"""

        # Deploy to 5% of traffic
        self.set_traffic_split(self.model_id, 5)

        # Monitor closely
        start = datetime.now()
        while (datetime.now() - start).hours < canary_duration_hours:
            metrics = self.get_recent_metrics(minutes=10)

            # Check for issues
            if self.has_critical_issues(metrics):
                print("Critical issues detected, rolling back")
                self.rollback()
                return False

            time.sleep(600)  # Check every 10 minutes

        # Canary successful, full rollout
        return self.gradual_rollout([
            {"percentage": 25, "duration_hours": 12, "criteria": {...}},
            {"percentage": 50, "duration_hours": 12, "criteria": {...}},
            {"percentage": 100, "duration_hours": 0, "criteria": {...}}
        ])

    def rollback(self):
        """Rollback to baseline model"""
        print("Rolling back to baseline model")
        self.set_traffic_split(self.baseline_model, 100)
```

Monitoring:
```python
def monitor_finetuned_model(model_id: str):
    """Monitor fine-tuned model in production"""

    metrics_to_track = {
        # Quality
        "task_success_rate": lambda: measure_success_rate(),
        "user_satisfaction": lambda: get_user_ratings(),
        "error_rate": lambda: count_errors(),

        # Performance
        "latency_p50": lambda: get_latency_percentile(50),
        "latency_p95": lambda: get_latency_percentile(95),
        "throughput": lambda: count_requests_per_minute(),

        # Cost
        "cost_per_request": lambda: calculate_avg_cost(),
        "daily_cost": lambda: get_daily_cost(),

        # Model health
        "distribution_shift": lambda: detect_drift(),
        "output_quality": lambda: sample_quality_check()
    }

    # Check metrics regularly
    while True:
        current_metrics = {
            name: fn() for name, fn in metrics_to_track.items()
        }

        # Log
        logger.info("model_metrics", extra=current_metrics)

        # Alert on anomalies
        check_alerts(current_metrics, model_id)

        time.sleep(300)  # Every 5 minutes
```

### 6. MAINTENANCE & ITERATION

Continuous Improvement:
```python
class ModelMaintenance:
    """Maintain and improve fine-tuned models"""

    def __init__(self, model_id: str):
        self.model_id = model_id
        self.performance_history = []

    def collect_production_data(self, days: int = 30):
        """Collect new training data from production"""

        # Get production interactions
        interactions = get_production_logs(days=days)

        # Filter for high-quality examples
        good_examples = []
        for interaction in interactions:
            # Include if:
            # - User provided positive feedback
            # - Output was verified correct
            # - Diverse (not duplicate of existing training data)
            if self.is_good_training_example(interaction):
                good_examples.append(interaction)

        return good_examples

    def retrain_schedule(self, frequency: str = "monthly"):
        """Periodic retraining with new data"""

        if frequency == "weekly":
            schedule = 7
        elif frequency == "monthly":
            schedule = 30
        elif frequency == "quarterly":
            schedule = 90

        last_training = datetime.now()

        while True:
            if (datetime.now() - last_training).days >= schedule:
                # Collect new data
                new_data = self.collect_production_data()

                if len(new_data) >= MIN_NEW_EXAMPLES:
                    # Retrain model
                    new_model_id = self.retrain_model(new_data)

                    # Evaluate
                    if self.new_model_better(new_model_id, self.model_id):
                        # Deploy new version
                        self.deploy_new_version(new_model_id)
                        self.model_id = new_model_id

                last_training = datetime.now()

            time.sleep(86400)  # Check daily

    def detect_degradation(self):
        """Detect if model performance is degrading"""

        # Get recent metrics
        recent = self.get_metrics(days=7)
        baseline = self.get_metrics(days=30)

        # Statistical comparison
        if recent["accuracy"] < baseline["accuracy"] * 0.95:
            alert("Model accuracy degraded", {
                "recent": recent["accuracy"],
                "baseline": baseline["accuracy"]
            })
            return True

        if recent["user_satisfaction"] < baseline["user_satisfaction"] * 0.9:
            alert("User satisfaction dropped", {
                "recent": recent["user_satisfaction"],
                "baseline": baseline["user_satisfaction"]
            })
            return True

        return False
```
```

## Variables

### BASE_MODEL
The foundation model you'll fine-tune.
**Examples:**
- "gpt-3.5-turbo (OpenAI API)"
- "Claude 3 Haiku (Anthropic)"
- "Llama 3 8B (self-hosted)"
- "Mistral 7B (Hugging Face)"

### TASK_DESCRIPTION
The specific task for fine-tuning.
**Examples:**
- "Legal contract analysis and extraction"
- "Medical record summarization with standardized format"
- "Customer support response generation in brand voice"
- "SQL query generation from natural language"

### PERFORMANCE_GOALS
Target improvements from fine-tuning.
**Examples:**
- "95% output format compliance (currently 70% with prompting)"
- "30% reduction in latency by using smaller fine-tuned model"
- "90% accuracy on domain-specific terminology (currently 60%)"
- "Consistent brand voice across all responses"

## Best Practices

### Data Quality
1. **Quality over quantity** - 100 great examples beat 1000 poor ones
2. **Diverse examples** - Cover full range of inputs and outputs
3. **Consistent format** - Train on format you want in production
4. **Human-verified** - Ensure outputs are actually correct
5. **Representative test set** - Hold out truly unseen examples

### Training
1. **Start small** - Few epochs initially, iterate based on results
2. **Monitor overfitting** - Watch validation loss
3. **Compare to baseline** - Always measure vs prompted model
4. **Document everything** - Track data versions, hyperparameters, results
5. **Cost-benefit analysis** - Ensure improvement justifies cost

### Deployment
1. **Gradual rollout** - Start with small traffic percentage
2. **Monitor closely** - Watch for unexpected behavior
3. **Easy rollback** - Keep baseline model ready
4. **A/B testing** - Measure real-world impact
5. **User feedback** - Collect feedback on fine-tuned outputs

### Maintenance
1. **Regular retraining** - Update with new production data
2. **Performance monitoring** - Track degradation over time
3. **Data drift detection** - Watch for distribution changes
4. **Version control** - Track model versions and training data
5. **Cost tracking** - Monitor total cost of ownership

## Common Pitfalls

❌ **Fine-tuning too early** - Before trying prompt optimization
✅ Instead: Exhaust prompting techniques first

❌ **Insufficient training data** - <100 examples
✅ Instead: Collect more data or use RAG/prompting

❌ **Low-quality training data** - Noisy, inconsistent labels
✅ Instead: Manual review, quality filtering, multiple annotators

❌ **Overfitting** - Too many epochs, model memorizes training set
✅ Instead: Monitor validation loss, use early stopping

❌ **No baseline comparison** - Don't know if fine-tuning helped
✅ Instead: Evaluate against prompted baseline on same test set

❌ **Testing on training data** - Inflated performance metrics
✅ Instead: Strict train/test split, never leak test data

❌ **One-time fine-tuning** - Model gets stale over time
✅ Instead: Regular retraining with new production data

❌ **Ignoring cost** - Fine-tuning and hosting costs add up
✅ Instead: Calculate ROI, compare to prompting costs

## Related Resources

**Platforms:**
- OpenAI Fine-tuning API
- Anthropic (custom training for enterprise)
- Hugging Face PEFT
- AWS SageMaker
- Google Vertex AI

**Methods:**
- LoRA (Low-Rank Adaptation)
- QLoRA (Quantized LoRA)
- Prompt Tuning
- Instruction Tuning

**Tools:**
- Weights & Biases (experiment tracking)
- Label Studio (data labeling)
- Snorkel (weak supervision)
- Evidently AI (monitoring)

---

**Last Updated:** 2025-11-12
**Category:** AI/ML Applications > LLM Applications
**Difficulty:** Advanced
**Estimated Time:** 3-6 weeks for complete fine-tuning pipeline
