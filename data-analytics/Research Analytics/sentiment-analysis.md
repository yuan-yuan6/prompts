---
title: Sentiment Analysis Methods
category: data-analytics/Research Analytics
tags: [data-analytics, machine-learning, nlp, sentiment-analysis, template, text-analytics]
use_cases:
  - Analyzing sentiment in customer reviews and feedback
  - Monitoring brand sentiment on social media
  - Detecting emotions in text communications
  - Tracking sentiment trends over time
related_templates:
  - text-analytics-overview.md
  - text-preprocessing.md
  - text-classification.md
  - advanced-nlp-techniques.md
last_updated: 2025-11-09
---

# Sentiment Analysis Methods

## Purpose
Perform comprehensive sentiment analysis to classify sentiment polarity, detect emotions, analyze aspect-based sentiment, and track sentiment trends using multiple methods from rule-based to transformer models.

## Template

```
You are a sentiment analysis expert. Analyze sentiment in [TEXT_DATA_SOURCE] to understand [SENTIMENT_OBJECTIVE] using [SENTIMENT_METHODS] with focus on [ANALYSIS_DEPTH].

TEXT DATA OVERVIEW:
- Data source: [DATA_SOURCE_TYPE]
- Volume: [TEXT_VOLUME]
- Domain: [DOMAIN_AREA]
- Analysis goal: [SENTIMENT_GOAL]

SENTIMENT ANALYSIS REQUIREMENTS:
- Sentiment classification: [SENTIMENT_CATEGORIES] (positive/negative/neutral or custom)
- Granularity: [SENTIMENT_GRANULARITY] (document/sentence/aspect level)
- Aspects to analyze: [ASPECT_CATEGORIES]
- Emotion detection: [EMOTION_TYPES]
- Time-based analysis: [TEMPORAL_ANALYSIS]
- Confidence thresholds: [CONFIDENCE_THRESHOLD]

Perform comprehensive sentiment analysis:

### COMPREHENSIVE SENTIMENT ANALYSIS

Multi-Method Sentiment Analysis:
```python
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import numpy as np
from nltk.tokenize import sent_tokenize

class SentimentAnalyzer:
    def __init__(self):
        self.models = {}
        self.setup_models()

    def setup_models(self):
        """Initialize various sentiment analysis models"""
        # VADER (rule-based, optimized for social media)
        self.models['vader'] = SentimentIntensityAnalyzer()

        # TextBlob (rule-based)
        self.models['textblob'] = TextBlob

        # Transformer-based models
        try:
            self.models['roberta'] = pipeline(
                'sentiment-analysis',
                model='cardiffnlp/twitter-roberta-base-sentiment-latest',
                return_all_scores=True
            )

            self.models['bert'] = pipeline(
                'sentiment-analysis',
                model='nlptown/bert-base-multilingual-uncased-sentiment',
                return_all_scores=True
            )

            self.models['finbert'] = pipeline(
                'sentiment-analysis',
                model='ProsusAI/finbert',
                return_all_scores=True
            )

        except Exception as e:
            print(f"Error loading transformer models: {e}")

    def analyze_sentiment_comprehensive(self, texts):
        """Comprehensive sentiment analysis using multiple methods"""
        results = []

        for text in texts:
            text_results = {'text': text}

            # VADER Sentiment
            vader_scores = self.models['vader'].polarity_scores(text)
            text_results['vader'] = {
                'compound': vader_scores['compound'],
                'positive': vader_scores['pos'],
                'neutral': vader_scores['neu'],
                'negative': vader_scores['neg'],
                'label': self.classify_vader_sentiment(vader_scores['compound'])
            }

            # TextBlob Sentiment
            blob = TextBlob(text)
            text_results['textblob'] = {
                'polarity': blob.sentiment.polarity,
                'subjectivity': blob.sentiment.subjectivity,
                'label': self.classify_textblob_sentiment(blob.sentiment.polarity)
            }

            # Transformer models (if available)
            for model_name in ['roberta', 'bert', 'finbert']:
                if model_name in self.models:
                    try:
                        scores = self.models[model_name](text)[0]
                        text_results[model_name] = {
                            'scores': scores,
                            'label': max(scores, key=lambda x: x['score'])['label'],
                            'confidence': max(scores, key=lambda x: x['score'])['score']
                        }
                    except Exception as e:
                        text_results[model_name] = {'error': str(e)}

            results.append(text_results)

        return results

    def classify_vader_sentiment(self, compound_score):
        """Classify VADER sentiment based on compound score"""
        if compound_score >= 0.05:
            return 'positive'
        elif compound_score <= -0.05:
            return 'negative'
        else:
            return 'neutral'

    def classify_textblob_sentiment(self, polarity):
        """Classify TextBlob sentiment based on polarity"""
        if polarity > 0:
            return 'positive'
        elif polarity < 0:
            return 'negative'
        else:
            return 'neutral'

    def aspect_based_sentiment(self, texts, aspects):
        """Perform aspect-based sentiment analysis"""
        results = []

        for text in texts:
            text_results = {'text': text, 'aspects': {}}

            for aspect in aspects:
                # Find sentences mentioning the aspect
                sentences = sent_tokenize(text)
                aspect_sentences = [sent for sent in sentences
                                 if aspect.lower() in sent.lower()]

                if aspect_sentences:
                    # Analyze sentiment of aspect-related sentences
                    aspect_text = ' '.join(aspect_sentences)
                    vader_score = self.models['vader'].polarity_scores(aspect_text)

                    text_results['aspects'][aspect] = {
                        'sentences': aspect_sentences,
                        'sentiment_score': vader_score['compound'],
                        'sentiment_label': self.classify_vader_sentiment(vader_score['compound']),
                        'context_count': len(aspect_sentences)
                    }
                else:
                    text_results['aspects'][aspect] = {
                        'sentences': [],
                        'sentiment_score': 0,
                        'sentiment_label': 'not_mentioned',
                        'context_count': 0
                    }

            results.append(text_results)

        return results

    def emotion_analysis(self, texts):
        """Analyze emotions using emotion classification models"""
        try:
            emotion_pipeline = pipeline(
                "text-classification",
                model="j-hartmann/emotion-english-distilroberta-base",
                return_all_scores=True
            )

            results = []
            for text in texts:
                emotions = emotion_pipeline(text)[0]
                emotion_dict = {emotion['label']: emotion['score'] for emotion in emotions}
                dominant_emotion = max(emotions, key=lambda x: x['score'])

                results.append({
                    'text': text,
                    'emotions': emotion_dict,
                    'dominant_emotion': dominant_emotion['label'],
                    'confidence': dominant_emotion['score']
                })

            return results

        except Exception as e:
            print(f"Emotion analysis not available: {e}")
            return [{'text': text, 'error': str(e)} for text in texts]

    def train_custom_sentiment_model(self, texts, labels, test_size=0.2):
        """Train custom sentiment classification model"""
        from sklearn.feature_extraction.text import TfidfVectorizer

        # Create features using TF-IDF
        vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1, 2))
        X = vectorizer.fit_transform(texts)

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, labels, test_size=test_size, random_state=42, stratify=labels
        )

        # Train model
        model = LogisticRegression(random_state=42, max_iter=1000)
        model.fit(X_train, y_train)

        # Evaluate
        train_score = model.score(X_train, y_train)
        test_score = model.score(X_test, y_test)

        # Cross-validation
        cv_scores = cross_val_score(model, X_train, y_train, cv=5)

        # Predictions
        y_pred = model.predict(X_test)

        # Store model
        self.models['custom'] = {
            'model': model,
            'vectorizer': vectorizer,
            'performance': {
                'train_accuracy': train_score,
                'test_accuracy': test_score,
                'cv_mean': cv_scores.mean(),
                'cv_std': cv_scores.std(),
                'classification_report': classification_report(y_test, y_pred),
                'confusion_matrix': confusion_matrix(y_test, y_pred)
            }
        }

        return self.models['custom']

    def sentiment_trend_analysis(self, texts, timestamps):
        """Analyze sentiment trends over time"""
        # Combine texts with timestamps
        text_time_data = list(zip(texts, timestamps))
        text_time_data.sort(key=lambda x: x[1])  # Sort by timestamp

        # Analyze sentiment for each time period
        sentiment_scores = []
        for text, timestamp in text_time_data:
            vader_score = self.models['vader'].polarity_scores(text)
            sentiment_scores.append({
                'timestamp': timestamp,
                'text': text,
                'compound_score': vader_score['compound'],
                'positive': vader_score['pos'],
                'negative': vader_score['neg'],
                'neutral': vader_score['neu']
            })

        # Create time-based aggregations
        df = pd.DataFrame(sentiment_scores)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['date'] = df['timestamp'].dt.date

        # Daily sentiment trends
        daily_sentiment = df.groupby('date').agg({
            'compound_score': ['mean', 'std', 'count'],
            'positive': 'mean',
            'negative': 'mean',
            'neutral': 'mean'
        }).round(4)

        return {
            'individual_scores': sentiment_scores,
            'daily_trends': daily_sentiment,
            'overall_trend': df['compound_score'].corr(df['timestamp'].astype('int64'))
        }

    def comparative_sentiment_analysis(self, groups_dict):
        """Compare sentiment across different groups or categories"""
        comparative_results = {}

        for group_name, texts in groups_dict.items():
            sentiments = []
            for text in texts:
                vader_score = self.models['vader'].polarity_scores(text)
                sentiments.append(vader_score['compound'])

            comparative_results[group_name] = {
                'mean_sentiment': np.mean(sentiments),
                'median_sentiment': np.median(sentiments),
                'std_sentiment': np.std(sentiments),
                'positive_count': sum(1 for s in sentiments if s >= 0.05),
                'negative_count': sum(1 for s in sentiments if s <= -0.05),
                'neutral_count': sum(1 for s in sentiments if -0.05 < s < 0.05),
                'total_count': len(sentiments)
            }

        return comparative_results

    def sentence_level_sentiment(self, texts):
        """Analyze sentiment at sentence level within documents"""
        results = []

        for text in texts:
            sentences = sent_tokenize(text)
            sentence_sentiments = []

            for sent in sentences:
                vader_score = self.models['vader'].polarity_scores(sent)
                sentence_sentiments.append({
                    'sentence': sent,
                    'compound_score': vader_score['compound'],
                    'label': self.classify_vader_sentiment(vader_score['compound'])
                })

            # Aggregate document sentiment
            avg_compound = np.mean([s['compound_score'] for s in sentence_sentiments])

            results.append({
                'text': text,
                'sentences': sentence_sentiments,
                'sentence_count': len(sentences),
                'avg_sentiment': avg_compound,
                'overall_label': self.classify_vader_sentiment(avg_compound)
            })

        return results

# Initialize sentiment analyzer
sentiment_analyzer = SentimentAnalyzer()

# Perform comprehensive sentiment analysis
sentiment_results = sentiment_analyzer.analyze_sentiment_comprehensive([TEXT_DATA])

# Aspect-based sentiment analysis
aspect_sentiment = sentiment_analyzer.aspect_based_sentiment(
    [TEXT_DATA],
    [ASPECT_CATEGORIES]
)

# Emotion analysis
emotion_results = sentiment_analyzer.emotion_analysis([TEXT_DATA])

# Trend analysis (if timestamps available)
if [HAS_TIMESTAMPS]:
    trend_results = sentiment_analyzer.sentiment_trend_analysis([TEXT_DATA], [TIMESTAMPS])

# Sentence-level analysis
sentence_results = sentiment_analyzer.sentence_level_sentiment([TEXT_DATA])
```

Sentiment Visualization:
```python
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_sentiment_results(sentiment_results):
    """Create comprehensive sentiment visualizations"""

    # Extract sentiment labels
    vader_labels = [r['vader']['label'] for r in sentiment_results]

    # Sentiment distribution
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1. Sentiment distribution pie chart
    sentiment_counts = pd.Series(vader_labels).value_counts()
    axes[0, 0].pie(sentiment_counts.values, labels=sentiment_counts.index,
                   autopct='%1.1f%%', startangle=90)
    axes[0, 0].set_title('Sentiment Distribution')

    # 2. Sentiment scores histogram
    compound_scores = [r['vader']['compound'] for r in sentiment_results]
    axes[0, 1].hist(compound_scores, bins=30, edgecolor='black')
    axes[0, 1].set_xlabel('Compound Sentiment Score')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].set_title('Distribution of Sentiment Scores')
    axes[0, 1].axvline(x=0, color='r', linestyle='--', label='Neutral')
    axes[0, 1].legend()

    # 3. Positive/Negative/Neutral proportions
    pos_scores = [r['vader']['positive'] for r in sentiment_results]
    neg_scores = [r['vader']['negative'] for r in sentiment_results]
    neu_scores = [r['vader']['neutral'] for r in sentiment_results]

    avg_scores = [np.mean(pos_scores), np.mean(neg_scores), np.mean(neu_scores)]
    categories = ['Positive', 'Negative', 'Neutral']

    axes[1, 0].bar(categories, avg_scores, color=['green', 'red', 'gray'])
    axes[1, 0].set_ylabel('Average Proportion')
    axes[1, 0].set_title('Average Sentiment Component Proportions')

    # 4. Subjectivity vs Polarity (TextBlob)
    if 'textblob' in sentiment_results[0]:
        polarity = [r['textblob']['polarity'] for r in sentiment_results]
        subjectivity = [r['textblob']['subjectivity'] for r in sentiment_results]

        axes[1, 1].scatter(polarity, subjectivity, alpha=0.5)
        axes[1, 1].set_xlabel('Polarity')
        axes[1, 1].set_ylabel('Subjectivity')
        axes[1, 1].set_title('Sentiment Polarity vs Subjectivity')
        axes[1, 1].axvline(x=0, color='r', linestyle='--', alpha=0.5)

    plt.tight_layout()
    return fig

def visualize_aspect_sentiment(aspect_results):
    """Visualize aspect-based sentiment"""
    # Extract aspects and their sentiments
    all_aspects = {}

    for result in aspect_results:
        for aspect, data in result['aspects'].items():
            if aspect not in all_aspects:
                all_aspects[aspect] = []
            if data['sentiment_label'] != 'not_mentioned':
                all_aspects[aspect].append(data['sentiment_score'])

    # Calculate average sentiment per aspect
    aspect_avg = {aspect: np.mean(scores) for aspect, scores in all_aspects.items()}

    # Create bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    aspects = list(aspect_avg.keys())
    scores = list(aspect_avg.values())
    colors = ['green' if s > 0 else 'red' if s < 0 else 'gray' for s in scores]

    ax.barh(aspects, scores, color=colors)
    ax.axvline(x=0, color='black', linestyle='-', linewidth=0.8)
    ax.set_xlabel('Average Sentiment Score')
    ax.set_title('Aspect-Based Sentiment Analysis')
    ax.set_xlim(-1, 1)

    plt.tight_layout()
    return fig
```

OUTPUT REQUIREMENTS:
1. Overall sentiment classification (positive/negative/neutral)
2. Sentiment confidence scores from multiple models
3. Aspect-based sentiment breakdown
4. Emotion detection results
5. Sentiment trends over time (if applicable)
6. Sentence-level sentiment analysis
7. Comparative sentiment analysis (if multiple groups)
8. Visualizations (pie charts, histograms, trend charts)
9. Statistical summaries and metrics
10. Model performance evaluation (if custom model trained)
```

## Variables

### Data Configuration
- [TEXT_DATA_SOURCE] - Source of text for sentiment analysis
- [DATA_SOURCE_TYPE] - Type of data source
- [TEXT_VOLUME] - Volume of text to analyze
- [DOMAIN_AREA] - Domain/industry area
- [SENTIMENT_OBJECTIVE] - Primary objective of sentiment analysis
- [SENTIMENT_GOAL] - Specific sentiment analysis goal

### Analysis Configuration
- [SENTIMENT_METHODS] - Methods to use (VADER, BERT, etc.)
- [ANALYSIS_DEPTH] - Depth of analysis (document, sentence, aspect)
- [SENTIMENT_CATEGORIES] - Categories (positive/negative/neutral or custom)
- [SENTIMENT_GRANULARITY] - Level of granularity
- [ASPECT_CATEGORIES] - Aspects to analyze (e.g., price, quality, service)
- [EMOTION_TYPES] - Emotions to detect (joy, anger, sadness, etc.)
- [TEMPORAL_ANALYSIS] - Include time-based analysis
- [CONFIDENCE_THRESHOLD] - Minimum confidence threshold

### Model Configuration
- [SENTIMENT_MODEL] - Primary sentiment model to use
- [DOMAIN_SPECIFIC_MODEL] - Domain-specific model (if applicable)
- [MULTI_MODEL_ENSEMBLE] - Use ensemble of models
- [CUSTOM_MODEL_TRAINING] - Train custom model

### Aspect Analysis
- [ASPECTS] - List of aspects to analyze
- [ASPECT_DETECTION_METHOD] - How to detect aspects
- [ASPECT_SENTIMENT_AGGREGATION] - How to aggregate aspect sentiments

### Time Series Analysis
- [HAS_TIMESTAMPS] - Whether data has timestamps
- [TIMESTAMPS] - Timestamp data
- [TIME_AGGREGATION] - Time period for aggregation (daily, weekly, monthly)
- [TREND_ANALYSIS] - Include trend analysis

## Usage Examples

### Example 1: Product Review Sentiment
```
TEXT_DATA_SOURCE: "E-commerce product reviews"
SENTIMENT_OBJECTIVE: "Understand customer satisfaction"
ASPECT_CATEGORIES: ["quality", "price", "shipping", "customer_service"]
SENTIMENT_METHODS: "VADER + BERT ensemble"
SENTIMENT_GRANULARITY: "aspect-level"
```

### Example 2: Social Media Brand Monitoring
```
TEXT_DATA_SOURCE: "Twitter mentions of brand"
SENTIMENT_OBJECTIVE: "Monitor brand reputation"
TEMPORAL_ANALYSIS: true
TIME_AGGREGATION: "daily"
SENTIMENT_METHODS: "Twitter-RoBERTa"
EMOTION_TYPES: ["joy", "anger", "sadness", "fear"]
```

### Example 3: Financial Sentiment Analysis
```
TEXT_DATA_SOURCE: "Financial news articles"
SENTIMENT_OBJECTIVE: "Assess market sentiment"
DOMAIN_SPECIFIC_MODEL: "FinBERT"
SENTIMENT_CATEGORIES: ["bullish", "bearish", "neutral"]
CONFIDENCE_THRESHOLD: 0.7
```

## Best Practices

1. **Use domain-appropriate models**: Financial text needs FinBERT, social media needs VADER
2. **Validate with human judgment**: Check model outputs against expert labeling
3. **Consider context**: Sentiment can be domain and context-specific
4. **Handle negation**: Ensure models properly handle "not good" vs "good"
5. **Account for sarcasm**: Transformer models handle this better than rule-based
6. **Aggregate carefully**: Document-level sentiment may not equal sentence averages
7. **Set appropriate thresholds**: Confidence thresholds affect precision/recall
8. **Track temporal changes**: Sentiment can shift over time
9. **Analyze aspects separately**: Overall sentiment may mask aspect-specific issues
10. **Ensemble when possible**: Multiple models provide more robust results
