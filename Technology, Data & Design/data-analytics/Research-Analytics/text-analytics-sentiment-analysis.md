---
title: Text Analytics - Sentiment Analysis
category: data-analytics
tags:
- automation
- data-analytics
- ai-ml
use_cases:
- Analyze sentiment in customer reviews, social media posts, and feedback using multiple
  models including VADER, TextBlob, and transformer-based approaches.
- Perform aspect-based sentiment analysis to understand opinions about specific product
  features or service attributes.
- Track sentiment trends over time and detect emotion patterns in text data.
related_templates:
- data-analytics/Research-Analytics/text-analytics-preprocessing.md
- data-analytics/Research-Analytics/text-analytics-topic-modeling.md
- data-analytics/Research-Analytics/text-analytics-overview.md
last_updated: 2025-11-10
industries:
- healthcare
- manufacturing
- technology
type: template
difficulty: intermediate
slug: text-analytics-sentiment-analysis
---

# Text Analytics - Sentiment Analysis

## Purpose
Conduct comprehensive sentiment analysis using multiple methods including rule-based (VADER, TextBlob), machine learning, and transformer-based deep learning models. Analyze overall sentiment, aspect-level opinions, emotions, and sentiment trends over time to extract actionable insights from text data.

## Quick Sentiment Prompt
Analyze sentiment in [X] documents from [source]. Classify overall sentiment (positive/neutral/negative) using VADER and transformer models, perform aspect-based analysis for [aspects: quality/price/service], detect emotions (joy/anger/frustration), and track sentiment trends over [time period]. Provide sentiment distribution, aspect scores, and key driver quotes.

## Quick Start

**Example: Multi-Method Sentiment Analysis of Product Reviews**

```
You are a sentiment analysis expert. Analyze 5,000 product reviews to understand customer satisfaction and identify areas for improvement.

TEXT DATA:
- Source: E-commerce product reviews (electronics category)
- Volume: 5,000 reviews with star ratings (1-5 stars)
- Average length: 80 words per review
- Contains: Product feedback, shipping comments, customer service mentions

SENTIMENT ANALYSIS REQUIREMENTS:
1. Overall sentiment using VADER and transformer models (RoBERTa)
2. Aspect-based sentiment for: product quality, price, shipping, customer service
3. Emotion analysis (joy, anger, sadness, surprise)
4. Sentiment trends over last 6 months
5. Compare sentiment across 1-star vs 5-star reviews

ASPECTS TO ANALYZE:
- Product quality: durability, performance, design
- Price: value for money, competitiveness
- Shipping: speed, packaging, condition on arrival
- Customer service: responsiveness, helpfulness, resolution

EXPECTED OUTPUT:
- Overall sentiment distribution (positive/neutral/negative percentages)
- Aspect-level sentiment scores with example quotes
- Top positive and negative themes
- Emotion distribution across reviews
- Sentiment trend visualization over time
- Actionable recommendations for improvement
```

## Template

```
You are a sentiment analysis expert. Analyze sentiment in [TEXT_DATA_SOURCE] containing [TEXT_VOLUME] to understand [ANALYSIS_OBJECTIVE] using [SENTIMENT_METHODS].

TEXT DATA:
- Data source: [DATA_SOURCE_TYPE]
- Volume: [NUMBER_DOCUMENTS] documents
- Domain: [DOMAIN_AREA]
- Language: [LANGUAGE]

SENTIMENT ANALYSIS:

### Comprehensive Sentiment Analysis
```python
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from nltk.tokenize import sent_tokenize

class SentimentAnalyzer:
    def __init__(self):
        self.models = {}
        self.setup_models()

    def setup_models(self):
        """Initialize various sentiment analysis models"""
        # VADER
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
        """Analyze emotions using NRC Emotion Lexicon approach"""
        # This would require emotion lexicons or pre-trained models
        # Conceptual implementation

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

# Initialize sentiment analyzer
sentiment_analyzer = SentimentAnalyzer()

# Perform comprehensive sentiment analysis
sentiment_results = sentiment_analyzer.analyze_sentiment_comprehensive([TEXT_DATA])
aspect_sentiment = sentiment_analyzer.aspect_based_sentiment([TEXT_DATA], [ASPECTS])
emotion_results = sentiment_analyzer.emotion_analysis([TEXT_DATA])
trend_analysis = sentiment_analyzer.sentiment_trend_analysis([TEXT_DATA], [TIMESTAMPS])
```
```

## Variables

### Sentiment Analysis Configuration
- [SENTIMENT_MODEL] - Sentiment analysis model to use (vader/textblob/roberta/bert/custom)
- [SENTIMENT_METHODS] - List of sentiment methods to apply
- [SENTIMENT_THRESHOLD] - Threshold for sentiment classification (default: ±0.05)
- [MULTI_MODEL_ENSEMBLE] - Use ensemble of multiple models (True/False)
- [DOMAIN_SPECIFIC_SENTIMENT] - Use domain-specific sentiment model (True/False)
- [SENTIMENT_CONFIDENCE] - Minimum confidence threshold for classification
- [POLARITY_CALCULATION] - Method for polarity calculation (average/weighted/max)
- [SUBJECTIVITY_ANALYSIS] - Include subjectivity analysis (True/False)

### Aspect-Based Sentiment Variables
- [ASPECTS] - List of aspects to analyze (e.g., quality, price, service)
- [ASPECT_CATEGORIES] - Categories for aspect-based sentiment
- [ASPECT_KEYWORDS] - Keywords associated with each aspect
- [ASPECT_EXTRACTION_METHOD] - Method for extracting aspects (keyword/ml/hybrid)
- [CONTEXT_WINDOW] - Sentence window for aspect context (default: 1)
- [ASPECT_SENTIMENT_AGGREGATION] - How to aggregate aspect sentiment (mean/weighted)

### Emotion Analysis Variables
- [EMOTION_MODEL] - Model for emotion detection (nrc/distilroberta/custom)
- [EMOTION_CATEGORIES] - Emotions to detect (joy, anger, sadness, fear, surprise, disgust)
- [EMOTION_THRESHOLD] - Minimum threshold for emotion classification
- [MULTI_LABEL_EMOTION] - Allow multiple emotions per text (True/False)
- [EMOTION_INTENSITY] - Measure emotion intensity (True/False)

### Temporal Analysis Variables
- [TIMESTAMPS] - Timestamp data for temporal analysis
- [TIME_AGGREGATION] - Aggregation level (hourly/daily/weekly/monthly)
- [TREND_DETECTION] - Enable sentiment trend detection (True/False)
- [SEASONALITY_ANALYSIS] - Analyze seasonal sentiment patterns (True/False)
- [MOVING_AVERAGE_WINDOW] - Window size for smoothing trends (default: 7)

### Model Training Variables
- [TRAINING_DATA] - Labeled data for training custom model
- [TRAINING_LABELS] - Sentiment labels for training data
- [TEST_SIZE] - Proportion of data for testing (default: 0.2)
- [CROSS_VALIDATION_FOLDS] - Number of CV folds (default: 5)
- [MODEL_HYPERPARAMETERS] - Hyperparameters for custom model
- [FEATURE_ENGINEERING] - Feature engineering method for custom model

### Input Data Variables
- [TEXT_DATA] - Text data for sentiment analysis
- [TEXT_DATA_SOURCE] - Source of text data
- [DATA_SOURCE_TYPE] - Type of data source (reviews/social/surveys)
- [NUMBER_DOCUMENTS] - Number of documents to analyze
- [DOMAIN_AREA] - Domain or industry area
- [LANGUAGE] - Language of text data

### Output Variables
- [SENTIMENT_DISTRIBUTION] - Distribution of sentiment labels
- [OVERALL_SENTIMENT] - Overall sentiment score/label
- [ASPECT_SENTIMENT_SCORES] - Sentiment scores per aspect
- [EMOTION_DISTRIBUTION] - Distribution of emotions
- [SENTIMENT_TRENDS] - Temporal sentiment trends
- [CONFIDENCE_SCORES] - Model confidence scores
- [POSITIVE_EXAMPLES] - Example positive texts
- [NEGATIVE_EXAMPLES] - Example negative texts

## Usage Examples

### Example 1: Customer Review Sentiment Analysis
```
TEXT_DATA_SOURCE: "Amazon product reviews"
SENTIMENT_MODEL: "vader"
ASPECTS: ["quality", "price", "shipping", "customer service"]
DOMAIN_AREA: "E-commerce electronics"
SENTIMENT_THRESHOLD: 0.1
SUBJECTIVITY_ANALYSIS: True
```

### Example 2: Social Media Brand Monitoring
```
TEXT_DATA_SOURCE: "Twitter mentions of brand"
SENTIMENT_METHODS: ["vader", "roberta"]
MULTI_MODEL_ENSEMBLE: True
EMOTION_CATEGORIES: ["joy", "anger", "surprise"]
TIME_AGGREGATION: "hourly"
TREND_DETECTION: True
```

### Example 3: Financial News Sentiment
```
TEXT_DATA_SOURCE: "Financial news articles"
SENTIMENT_MODEL: "finbert"
DOMAIN_SPECIFIC_SENTIMENT: True
SENTIMENT_CONFIDENCE: 0.7
ASPECT_CATEGORIES: ["market_outlook", "company_performance", "economic_indicators"]
```

### Example 4: Employee Feedback Analysis
```
TEXT_DATA_SOURCE: "Employee satisfaction surveys"
ASPECT_CATEGORIES: ["work_environment", "compensation", "management", "work_life_balance"]
SENTIMENT_MODEL: "textblob"
EMOTION_MODEL: "distilroberta"
MULTI_LABEL_EMOTION: True
```

### Example 5: Healthcare Patient Feedback
```
TEXT_DATA_SOURCE: "Patient feedback forms"
DOMAIN_SPECIFIC_SENTIMENT: True
ASPECTS: ["treatment_quality", "wait_time", "staff_courtesy", "facility_cleanliness"]
EMOTION_CATEGORIES: ["satisfaction", "frustration", "anxiety"]
SENTIMENT_THRESHOLD: 0.05
```

## Best Practices

1. **Use multiple sentiment methods** - Combine rule-based and ML approaches for robust analysis
2. **Consider domain context** - Use domain-specific models for specialized text (finance, healthcare)
3. **Validate with human judgment** - Sample results and compare with human annotations
4. **Handle negation carefully** - Ensure models properly handle negation (not good, not bad)
5. **Account for sarcasm** - Be aware of model limitations with irony and sarcasm
6. **Set appropriate thresholds** - Adjust sentiment thresholds based on your data distribution
7. **Analyze aspect-level sentiment** - Go beyond overall sentiment to understand specific attributes
8. **Track sentiment over time** - Monitor trends to identify changes and patterns
9. **Include confidence scores** - Report model confidence to assess reliability
10. **Provide context with examples** - Include representative text examples for each sentiment category

## Tips for Success

- Preprocess text appropriately for each sentiment model (some work better with raw text)
- VADER works well for social media text with emoticons and slang
- Transformer models provide better nuanced sentiment but are slower
- For aspect-based sentiment, ensure aspect keywords are comprehensive
- Consider sentence-level sentiment for longer documents
- Aggregate multiple reviews to identify overall trends
- Use emotion analysis to add depth beyond positive/negative/neutral
- Cross-validate sentiment models on a labeled subset of your data
- Monitor model performance over time as language evolves
- Combine sentiment with other analytics (topics, entities) for richer insights
