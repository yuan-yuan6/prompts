---
title: Text Classification Methods
category: data-analytics/Research Analytics
tags: [classification, data-analytics, machine-learning, nlp, template, text-analytics]
use_cases:
  - Categorizing documents into predefined classes
  - Spam detection and content filtering
  - Multi-label document classification
  - Intent classification for customer service
related_templates:
  - text-analytics-overview.md
  - text-preprocessing.md
  - sentiment-analysis.md
  - advanced-nlp-techniques.md
last_updated: 2025-11-09
---

# Text Classification Methods

## Purpose
Classify text documents into predefined categories using feature extraction, traditional machine learning, and deep learning methods with comprehensive model evaluation and performance optimization.

## Template

```
You are a text classification expert. Classify [TEXT_DATA_SOURCE] into [CLASSIFICATION_CATEGORIES] using [CLASSIFICATION_METHODS] with focus on [CLASSIFICATION_OBJECTIVE].

TEXT DATA OVERVIEW:
- Data source: [DATA_SOURCE_TYPE]
- Volume: [TEXT_VOLUME] ([NUMBER_DOCUMENTS] documents)
- Categories: [CLASSIFICATION_CATEGORIES]
- Category distribution: [CATEGORY_DISTRIBUTION]
- Domain: [DOMAIN_AREA]

CLASSIFICATION CONFIGURATION:
- Classification type: [CLASSIFICATION_TYPE] (binary/multi-class/multi-label)
- Features: [FEATURE_EXTRACTION_METHOD] (TF-IDF/embeddings/transformers)
- Models: [CLASSIFICATION_MODELS]
- Evaluation metrics: [EVALUATION_METRICS]
- Class imbalance handling: [IMBALANCE_STRATEGY]
- Cross-validation: [CV_FOLDS] folds

Perform comprehensive text classification:

### TEXT CLASSIFICATION PIPELINE

Feature Extraction and Model Training:
```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import precision_recall_fscore_support, roc_auc_score, roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
import matplotlib.pyplot as plt
import seaborn as sns

class TextClassifier:
    def __init__(self, classification_type='multi-class'):
        self.classification_type = classification_type
        self.vectorizers = {}
        self.models = {}
        self.results = {}

    def extract_features(self, texts, method='tfidf', max_features=10000, ngram_range=(1, 2)):
        """Extract features from text"""
        if method == 'tfidf':
            vectorizer = TfidfVectorizer(
                max_features=max_features,
                ngram_range=ngram_range,
                stop_words='english',
                min_df=2,
                max_df=0.95,
                sublinear_tf=True
            )
        elif method == 'bow':
            vectorizer = CountVectorizer(
                max_features=max_features,
                ngram_range=ngram_range,
                stop_words='english',
                min_df=2,
                max_df=0.95
            )

        features = vectorizer.fit_transform(texts)
        self.vectorizers[method] = vectorizer

        return features, vectorizer

    def handle_class_imbalance(self, X, y, strategy='smote'):
        """Handle class imbalance in training data"""
        if strategy == 'smote':
            # Synthetic Minority Over-sampling Technique
            smote = SMOTE(random_state=42)
            X_resampled, y_resampled = smote.fit_resample(X, y)

        elif strategy == 'undersample':
            # Random under-sampling
            rus = RandomUnderSampler(random_state=42)
            X_resampled, y_resampled = rus.fit_resample(X, y)

        elif strategy == 'class_weight':
            # Use class weights in model (no resampling)
            X_resampled, y_resampled = X, y

        else:
            # No resampling
            X_resampled, y_resampled = X, y

        return X_resampled, y_resampled

    def train_traditional_models(self, X_train, y_train, X_test, y_test):
        """Train multiple traditional ML models"""
        models = {
            'logistic_regression': LogisticRegression(
                random_state=42,
                max_iter=1000,
                class_weight='balanced'
            ),
            'naive_bayes': MultinomialNB(alpha=0.1),
            'linear_svc': LinearSVC(
                random_state=42,
                max_iter=1000,
                class_weight='balanced'
            ),
            'random_forest': RandomForestClassifier(
                n_estimators=100,
                random_state=42,
                class_weight='balanced'
            ),
            'gradient_boosting': GradientBoostingClassifier(
                n_estimators=100,
                random_state=42
            )
        }

        results = {}

        for name, model in models.items():
            print(f"Training {name}...")

            # Train model
            model.fit(X_train, y_train)

            # Predictions
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Evaluate
            train_accuracy = accuracy_score(y_train, y_train_pred)
            test_accuracy = accuracy_score(y_test, y_test_pred)

            # Cross-validation
            cv_scores = cross_val_score(model, X_train, y_train, cv=5)

            # Classification report
            report = classification_report(y_test, y_test_pred, output_dict=True)

            # Confusion matrix
            cm = confusion_matrix(y_test, y_test_pred)

            results[name] = {
                'model': model,
                'train_accuracy': train_accuracy,
                'test_accuracy': test_accuracy,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'classification_report': report,
                'confusion_matrix': cm,
                'y_test_pred': y_test_pred
            }

            self.models[name] = model

        self.results['traditional'] = results
        return results

    def train_neural_network(self, X_train, y_train, X_test, y_test):
        """Train neural network classifier"""
        mlp = MLPClassifier(
            hidden_layer_sizes=(100, 50),
            activation='relu',
            solver='adam',
            max_iter=500,
            random_state=42,
            early_stopping=True,
            validation_fraction=0.1
        )

        # Train
        mlp.fit(X_train, y_train)

        # Predictions
        y_train_pred = mlp.predict(X_train)
        y_test_pred = mlp.predict(X_test)

        # Evaluate
        train_accuracy = accuracy_score(y_train, y_train_pred)
        test_accuracy = accuracy_score(y_test, y_test_pred)

        # Classification report
        report = classification_report(y_test, y_test_pred, output_dict=True)

        # Confusion matrix
        cm = confusion_matrix(y_test, y_test_pred)

        result = {
            'model': mlp,
            'train_accuracy': train_accuracy,
            'test_accuracy': test_accuracy,
            'classification_report': report,
            'confusion_matrix': cm,
            'y_test_pred': y_test_pred,
            'loss_curve': mlp.loss_curve_
        }

        self.models['neural_network'] = mlp
        self.results['neural_network'] = result

        return result

    def train_transformer_classifier(self, texts_train, y_train, texts_test, y_test):
        """Train transformer-based classifier"""
        from transformers import AutoTokenizer, AutoModelForSequenceClassification
        from transformers import Trainer, TrainingArguments
        from datasets import Dataset

        try:
            # Load pretrained model and tokenizer
            model_name = "distilbert-base-uncased"
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            num_labels = len(np.unique(y_train))

            model = AutoModelForSequenceClassification.from_pretrained(
                model_name,
                num_labels=num_labels
            )

            # Tokenize data
            train_encodings = tokenizer(
                list(texts_train),
                truncation=True,
                padding=True,
                max_length=512
            )
            test_encodings = tokenizer(
                list(texts_test),
                truncation=True,
                padding=True,
                max_length=512
            )

            # Create datasets
            train_dataset = Dataset.from_dict({
                **train_encodings,
                'labels': y_train
            })
            test_dataset = Dataset.from_dict({
                **test_encodings,
                'labels': y_test
            })

            # Training arguments
            training_args = TrainingArguments(
                output_dir='./results',
                num_train_epochs=3,
                per_device_train_batch_size=8,
                per_device_eval_batch_size=8,
                warmup_steps=500,
                weight_decay=0.01,
                logging_dir='./logs',
                evaluation_strategy="epoch"
            )

            # Trainer
            trainer = Trainer(
                model=model,
                args=training_args,
                train_dataset=train_dataset,
                eval_dataset=test_dataset
            )

            # Train
            trainer.train()

            # Evaluate
            eval_results = trainer.evaluate()

            self.models['transformer'] = {
                'model': model,
                'tokenizer': tokenizer,
                'trainer': trainer
            }

            return {
                'model': model,
                'tokenizer': tokenizer,
                'eval_results': eval_results
            }

        except Exception as e:
            print(f"Transformer training failed: {e}")
            return None

    def hyperparameter_tuning(self, X_train, y_train, model_type='logistic_regression'):
        """Perform hyperparameter tuning"""
        if model_type == 'logistic_regression':
            model = LogisticRegression(random_state=42, max_iter=1000)
            param_grid = {
                'C': [0.1, 1, 10, 100],
                'penalty': ['l1', 'l2'],
                'solver': ['liblinear', 'saga']
            }

        elif model_type == 'random_forest':
            model = RandomForestClassifier(random_state=42)
            param_grid = {
                'n_estimators': [50, 100, 200],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10]
            }

        elif model_type == 'svc':
            model = SVC(random_state=42)
            param_grid = {
                'C': [0.1, 1, 10],
                'kernel': ['linear', 'rbf'],
                'gamma': ['scale', 'auto']
            }

        # Grid search
        grid_search = GridSearchCV(
            model,
            param_grid,
            cv=5,
            scoring='f1_weighted',
            n_jobs=-1,
            verbose=1
        )

        grid_search.fit(X_train, y_train)

        return {
            'best_params': grid_search.best_params_,
            'best_score': grid_search.best_score_,
            'best_model': grid_search.best_estimator_,
            'cv_results': grid_search.cv_results_
        }

    def multi_label_classification(self, X_train, y_train, X_test, y_test):
        """Perform multi-label classification"""
        from sklearn.multioutput import MultiOutputClassifier
        from sklearn.metrics import hamming_loss, jaccard_score

        # Base classifier
        base_classifier = LogisticRegression(random_state=42, max_iter=1000)

        # Multi-output classifier
        multi_label_classifier = MultiOutputClassifier(base_classifier)

        # Train
        multi_label_classifier.fit(X_train, y_train)

        # Predictions
        y_pred = multi_label_classifier.predict(X_test)

        # Evaluate
        hamming = hamming_loss(y_test, y_pred)
        jaccard = jaccard_score(y_test, y_pred, average='samples')

        return {
            'model': multi_label_classifier,
            'hamming_loss': hamming,
            'jaccard_score': jaccard,
            'y_pred': y_pred
        }

    def evaluate_model_performance(self, model_name):
        """Generate comprehensive evaluation report"""
        if model_name not in self.results.get('traditional', {}):
            return None

        results = self.results['traditional'][model_name]

        evaluation = {
            'accuracy': results['test_accuracy'],
            'precision': results['classification_report']['weighted avg']['precision'],
            'recall': results['classification_report']['weighted avg']['recall'],
            'f1_score': results['classification_report']['weighted avg']['f1-score'],
            'cv_mean': results['cv_mean'],
            'cv_std': results['cv_std'],
            'confusion_matrix': results['confusion_matrix']
        }

        return evaluation

# Initialize classifier
text_classifier = TextClassifier(classification_type='[CLASSIFICATION_TYPE]')

# Load and prepare data
texts = [TEXT_DATA]
labels = [LABELS]

# Split data
texts_train, texts_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, random_state=42, stratify=labels
)

# Extract features
X_train, vectorizer = text_classifier.extract_features(
    texts_train,
    method='[FEATURE_EXTRACTION_METHOD]',
    max_features=[MAX_FEATURES],
    ngram_range=[NGRAM_RANGE]
)

X_test = vectorizer.transform(texts_test)

# Handle class imbalance (if needed)
if [HANDLE_IMBALANCE]:
    X_train, y_train = text_classifier.handle_class_imbalance(
        X_train, y_train, strategy='[IMBALANCE_STRATEGY]'
    )

# Train traditional models
traditional_results = text_classifier.train_traditional_models(
    X_train, y_train, X_test, y_test
)

# Train neural network
nn_results = text_classifier.train_neural_network(
    X_train, y_train, X_test, y_test
)

# Hyperparameter tuning (optional)
if [TUNE_HYPERPARAMETERS]:
    tuning_results = text_classifier.hyperparameter_tuning(
        X_train, y_train, model_type='[MODEL_TO_TUNE]'
    )

# Train transformer model (optional)
if [USE_TRANSFORMER]:
    transformer_results = text_classifier.train_transformer_classifier(
        texts_train, y_train, texts_test, y_test
    )
```

Visualization and Analysis:
```python
def visualize_model_comparison(results):
    """Compare performance of different models"""
    models = list(results.keys())
    accuracies = [results[m]['test_accuracy'] for m in models]
    cv_means = [results[m]['cv_mean'] for m in models]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Test accuracy comparison
    axes[0].bar(models, accuracies)
    axes[0].set_title('Test Accuracy Comparison')
    axes[0].set_ylabel('Accuracy')
    axes[0].tick_params(axis='x', rotation=45)

    # CV scores comparison
    axes[1].bar(models, cv_means)
    axes[1].set_title('Cross-Validation Mean Accuracy')
    axes[1].set_ylabel('CV Mean Accuracy')
    axes[1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    return fig

def plot_confusion_matrix(cm, class_names):
    """Plot confusion matrix heatmap"""
    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=class_names, yticklabels=class_names, ax=ax)

    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.set_title('Confusion Matrix')

    plt.tight_layout()
    return fig

def plot_feature_importance(model, vectorizer, top_n=20):
    """Plot feature importance for linear models"""
    if hasattr(model, 'coef_'):
        feature_names = vectorizer.get_feature_names_out()
        coefficients = model.coef_[0]

        # Get top positive and negative features
        top_positive_idx = coefficients.argsort()[-top_n:][::-1]
        top_negative_idx = coefficients.argsort()[:top_n]

        top_features = np.concatenate([top_positive_idx, top_negative_idx])
        top_feature_names = feature_names[top_features]
        top_coefficients = coefficients[top_features]

        # Plot
        fig, ax = plt.subplots(figsize=(10, 8))
        colors = ['green' if c > 0 else 'red' for c in top_coefficients]
        ax.barh(range(len(top_coefficients)), top_coefficients, color=colors)
        ax.set_yticks(range(len(top_feature_names)))
        ax.set_yticklabels(top_feature_names)
        ax.set_xlabel('Coefficient Value')
        ax.set_title('Top Features by Importance')

        plt.tight_layout()
        return fig

    return None
```

OUTPUT REQUIREMENTS:
1. Trained classification models with performance metrics
2. Test accuracy, precision, recall, F1-scores
3. Cross-validation results
4. Confusion matrices for all models
5. Feature importance analysis
6. Model comparison visualizations
7. Hyperparameter tuning results (if applicable)
8. Classification reports for each class
9. ROC curves and AUC scores (for binary classification)
10. Recommendations for best model
```

## Variables

### Data Configuration
- [TEXT_DATA_SOURCE] - Source of text for classification
- [DATA_SOURCE_TYPE] - Type of data source
- [TEXT_VOLUME] - Volume of text to classify
- [NUMBER_DOCUMENTS] - Total number of documents
- [DOMAIN_AREA] - Domain/industry area

### Classification Configuration
- [CLASSIFICATION_CATEGORIES] - Categories to classify into
- [CATEGORY_DISTRIBUTION] - Distribution of categories
- [CLASSIFICATION_TYPE] - Type (binary/multi-class/multi-label)
- [CLASSIFICATION_OBJECTIVE] - Primary objective
- [CLASSIFICATION_METHODS] - Methods to use

### Feature Extraction
- [FEATURE_EXTRACTION_METHOD] - Method (tfidf/bow/embeddings)
- [MAX_FEATURES] - Maximum number of features
- [NGRAM_RANGE] - N-gram range (e.g., (1, 2))

### Model Configuration
- [CLASSIFICATION_MODELS] - Models to train
- [HANDLE_IMBALANCE] - Handle class imbalance
- [IMBALANCE_STRATEGY] - Strategy (smote/undersample/class_weight)
- [CV_FOLDS] - Number of cross-validation folds
- [TUNE_HYPERPARAMETERS] - Perform hyperparameter tuning
- [MODEL_TO_TUNE] - Model for tuning
- [USE_TRANSFORMER] - Use transformer models

### Evaluation
- [EVALUATION_METRICS] - Metrics to use
- [TEXT_DATA] - Text data to classify
- [LABELS] - Category labels

## Usage Examples

### Example 1: News Article Classification
```
CLASSIFICATION_CATEGORIES: ["sports", "politics", "technology", "entertainment"]
CLASSIFICATION_TYPE: "multi-class"
FEATURE_EXTRACTION_METHOD: "tfidf"
CLASSIFICATION_MODELS: ["logistic_regression", "random_forest", "svc"]
HANDLE_IMBALANCE: false
```

### Example 2: Spam Detection
```
CLASSIFICATION_CATEGORIES: ["spam", "not_spam"]
CLASSIFICATION_TYPE: "binary"
FEATURE_EXTRACTION_METHOD: "tfidf"
IMBALANCE_STRATEGY: "smote"
TUNE_HYPERPARAMETERS: true
```

### Example 3: Multi-Label Document Tagging
```
CLASSIFICATION_TYPE: "multi-label"
CLASSIFICATION_CATEGORIES: ["urgent", "technical", "customer_facing", "internal"]
FEATURE_EXTRACTION_METHOD: "tfidf"
CLASSIFICATION_MODELS: ["logistic_regression"]
```

## Best Practices

1. **Balance your dataset**: Address class imbalance before training
2. **Use appropriate features**: TF-IDF works well for most tasks
3. **Cross-validate**: Always use cross-validation for robust evaluation
4. **Try multiple models**: Different models work better for different data
5. **Tune hyperparameters**: Grid search can significantly improve performance
6. **Analyze errors**: Study misclassifications to improve model
7. **Use ensemble methods**: Combine multiple models for better results
8. **Monitor overfitting**: Check train vs test performance
9. **Validate with domain experts**: Ensure categories make sense
10. **Document feature engineering**: Track what works and what doesn't
