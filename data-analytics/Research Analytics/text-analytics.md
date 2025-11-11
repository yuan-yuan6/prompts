---
title: Text Analytics and NLP Template
category: data-analytics/Research Analytics
tags: [automation, data-analytics, data-science, design, machine-learning, research, template]
use_cases:
  - Creating conduct comprehensive text mining and natural language processing analysis to extract insights, patterns, sentiments, topics, and knowledge from unstructured text data using advanced nlp techniques and machine learning methods.

  - Project planning and execution
  - Strategy development
related_templates:
  - dashboard-design-patterns.md
  - data-governance-framework.md
  - predictive-modeling-framework.md
last_updated: 2025-11-09
---

# Text Analytics and NLP Template

## Purpose
Conduct comprehensive text mining and natural language processing analysis to extract insights, patterns, sentiments, topics, and knowledge from unstructured text data using advanced NLP techniques and machine learning methods.

## Quick Start

**Example: Customer Review Sentiment and Topic Analysis**

```
You are a text analytics expert. Analyze 50,000 customer product reviews from an e-commerce platform to understand sentiment drivers, identify key topics, and extract actionable insights for product improvement.

TEXT DATA OVERVIEW:
- Data source: E-commerce product reviews
- Volume: 50,000 reviews (2.5 million words)
- Product categories: Electronics, Home & Kitchen, Beauty, Sports
- Time period: Last 12 months
- Rating distribution: 1-5 stars with text comments
- Languages: English
- Average review length: 50 words
- Format: CSV with fields (review_id, product_id, rating, review_text, date, verified_purchase)

ANALYSIS OBJECTIVES:
1. Perform multi-method sentiment analysis (VADER, TextBlob, transformer models)
2. Conduct aspect-based sentiment analysis for product features (quality, price, shipping, customer service)
3. Extract main topics using LDA and BERTopic (target: 8-10 topics)
4. Identify key themes in negative reviews (1-2 star ratings)
5. Extract frequently mentioned product features and pain points
6. Compare sentiment trends across product categories and over time
7. Build classification model to predict review helpfulness

EXPECTED OUTPUTS:
- Overall sentiment distribution and trends
- Aspect-level sentiment scores with example quotes
- Topic model with top keywords and representative reviews
- Word clouds for positive vs. negative reviews
- Named entities (products, brands, features mentioned)
- Actionable insights ranked by impact and frequency

Use VADER for initial sentiment scoring, then apply transformer-based models for nuanced analysis. Extract topics with coherence scores > 0.4 for interpretability.
```

## Template

```
You are a text analytics expert. Perform comprehensive NLP analysis on [TEXT_DATA_SOURCE] to extract insights about [ANALYSIS_OBJECTIVE] using [NLP_TECHNIQUES] with focus on [SPECIFIC_TASKS].

TEXT DATA OVERVIEW:
Data Characteristics:
- Data source: [DATA_SOURCE_TYPE] (Social Media/Reviews/Documents/Surveys/News/Academic)
- Volume: [TEXT_VOLUME] ([NUMBER_DOCUMENTS] documents, [TOTAL_WORDS] words)
- Language(s): [LANGUAGES]
- Time period: [TIME_PERIOD]
- Geographic scope: [GEOGRAPHIC_SCOPE]
- Domain/Topic: [DOMAIN_AREA]
- Format: [TEXT_FORMAT] (Plain text/HTML/PDF/JSON/CSV)
- Encoding: [TEXT_ENCODING]

### Analysis Objectives
- Primary goal: [PRIMARY_ANALYSIS_GOAL]
- Secondary goals: [SECONDARY_GOALS]
- Research questions: [RESEARCH_QUESTIONS]
- Business questions: [BUSINESS_QUESTIONS]
- Expected insights: [EXPECTED_INSIGHTS]
- Success metrics: [SUCCESS_METRICS]
- Deliverable format: [DELIVERABLE_FORMAT]

### TEXT PREPROCESSING PIPELINE
### Data Cleaning and Preparation
```python
import pandas as pd
import numpy as np
import re
import string
import unicodedata
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tag import pos_tag
import spacy
from textblob import TextBlob
import contractions

class TextPreprocessor:
    def __init__(self, language='english', custom_config=None):
        self.language = language
        self.config = custom_config or self._default_config()
        self.setup_nlp_tools()

    def _default_config(self):
        return {
            'lowercase': True,
            'remove_html': True,
            'remove_urls': True,
            'remove_emails': True,
            'remove_phone_numbers': True,
            'remove_social_handles': True,
            'expand_contractions': True,
            'remove_punctuation': True,
            'remove_numbers': True,
            'remove_extra_whitespace': True,
            'remove_stopwords': True,
            'lemmatize': True,
            'stem': False,
            'min_word_length': 2,
            'max_word_length': 50,
            'custom_stopwords': [],
            'preserve_case_words': [],
            'custom_replacements': {}
        }

    def setup_nlp_tools(self):
        """Initialize NLP tools and resources"""
        # Download required NLTK data
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)

        # Initialize tools
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words(self.language))

        # Add custom stopwords
        self.stop_words.update(self.config['custom_stopwords'])

        # Load spaCy model
        try:
            self.nlp = spacy.load('en_core_web_sm')
        except OSError:
            print("spaCy model not found. Install with: python -m spacy download en_core_web_sm")
            self.nlp = None

    def clean_text(self, text):
        """Comprehensive text cleaning pipeline"""
        if pd.isna(text) or text == '':
            return ''

        # Ensure string type
        text = str(text)

        # Remove HTML tags
        if self.config['remove_html']:
            text = BeautifulSoup(text, 'html.parser').get_text()

        # Remove URLs
        if self.config['remove_urls']:
            text = re.sub(r'http\S+|www\.\S+|https\S+', '', text, flags=re.MULTILINE)

        # Remove email addresses
        if self.config['remove_emails']:
            text = re.sub(r'\S+@\S+', '', text)

        # Remove phone numbers
        if self.config['remove_phone_numbers']:
            phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
            text = re.sub(phone_pattern, '', text)

        # Remove social media handles
        if self.config['remove_social_handles']:
            text = re.sub(r'@\w+|#\w+', '', text)

        # Expand contractions
        if self.config['expand_contractions']:
            text = contractions.fix(text)

        # Apply custom replacements
        for old, new in self.config['custom_replacements'].items():
            text = text.replace(old, new)

        # Normalize unicode characters
        text = unicodedata.normalize('NFKD', text)

        # Convert to lowercase (preserve specified words)
        if self.config['lowercase']:
            preserve_words = self.config['preserve_case_words']
            if preserve_words:
                # Temporarily replace preserved words
                preserved = {}
                for i, word in enumerate(preserve_words):
                    placeholder = f"__PRESERVE_[I]__"
                    text = re.sub(rf'\b{re.escape(word)}\b', placeholder, text, flags=re.IGNORECASE)
                    preserved[placeholder] = word

                text = text.lower()

                # Restore preserved words
                for placeholder, word in preserved.items():
                    text = text.replace(placeholder, word)
            else:
                text = text.lower()

        # Remove punctuation
        if self.config['remove_punctuation']:
            text = text.translate(str.maketrans('', '', string.punctuation))

        # Remove numbers
        if self.config['remove_numbers']:
            text = re.sub(r'\d+', '', text)

        # Remove extra whitespace
        if self.config['remove_extra_whitespace']:
            text = ' '.join(text.split())

        return text

    def tokenize_and_process(self, text):
        """Tokenize and apply word-level processing"""
        if not text:
            return []

        # Tokenize
        tokens = word_tokenize(text)

        # Filter by word length
        tokens = [token for token in tokens
                 if self.config['min_word_length'] <= len(token) <= self.config['max_word_length']]

        # Remove stopwords
        if self.config['remove_stopwords']:
            tokens = [token for token in tokens if token not in self.stop_words]

        # Lemmatization
        if self.config['lemmatize']:
            tokens = [self.lemmatizer.lemmatize(token) for token in tokens]

        # Stemming
        if self.config['stem']:
            tokens = [self.stemmer.stem(token) for token in tokens]

        return tokens

    def advanced_preprocessing_spacy(self, text):
        """Advanced preprocessing using spaCy"""
        if not self.nlp or not text:
            return []

        doc = self.nlp(text)

        # Extract tokens with POS tags and named entities
        processed_tokens = []
        for token in doc:
            if not token.is_stop and not token.is_punct and not token.is_space:
                processed_tokens.append({
                    'text': token.text,
                    'lemma': token.lemma_,
                    'pos': token.pos_,
                    'tag': token.tag_,
                    'is_alpha': token.is_alpha,
                    'is_digit': token.is_digit,
                    'ent_type': token.ent_type_
                })

        # Extract named entities
        entities = [(ent.text, ent.label_, ent.start_char, ent.end_char)
                   for ent in doc.ents]

        # Extract noun phrases
        noun_phrases = [chunk.text for chunk in doc.noun_chunks]

        return {
            'tokens': processed_tokens,
            'entities': entities,
            'noun_phrases': noun_phrases,
            'sentences': [sent.text for sent in doc.sents]
        }

    def process_corpus(self, texts):
        """Process entire corpus of texts"""
        processed_corpus = []

        for i, text in enumerate(texts):
            if i % 1000 == 0:
                print(f"Processing document {i+1}/{len(texts)}")

            cleaned_text = self.clean_text(text)
            tokens = self.tokenize_and_process(cleaned_text)

            processed_corpus.append({
                'original_text': text,
                'cleaned_text': cleaned_text,
                'tokens': tokens,
                'token_count': len(tokens),
                'char_count': len(text),
                'word_count': len(text.split())
            })

        return processed_corpus

# Initialize preprocessor with custom configuration
preprocessor = TextPreprocessor(
    language='[LANGUAGE]',
    custom_config={
        'remove_stopwords': [REMOVE_STOPWORDS],
        'lemmatize': [LEMMATIZE],
        'custom_stopwords': [CUSTOM_STOPWORDS],
        'min_word_length': [MIN_WORD_LENGTH]
    }
)

# Process the text data
processed_texts = preprocessor.process_corpus([TEXT_CORPUS])
```

Feature Engineering:
```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from gensim.models import Word2Vec, Doc2Vec, LdaModel, FastText
from gensim.corpora import Dictionary
import numpy as np

class TextFeatureEngineer:
    def __init__(self):
        self.vectorizers = {}
        self.models = {}

    def create_bow_features(self, texts, max_features=10000, ngram_range=(1, 2)):
        """Create Bag of Words features"""
        vectorizer = CountVectorizer(
            max_features=max_features,
            ngram_range=ngram_range,
            stop_words='english' if '[REMOVE_STOPWORDS]' else None
        )

        bow_matrix = vectorizer.fit_transform(texts)
        feature_names = vectorizer.get_feature_names_out()

        self.vectorizers['bow'] = vectorizer

        return {
            'matrix': bow_matrix,
            'feature_names': feature_names,
            'vocabulary': vectorizer.vocabulary_
        }

    def create_tfidf_features(self, texts, max_features=10000, ngram_range=(1, 3)):
        """Create TF-IDF features"""
        vectorizer = TfidfVectorizer(
            max_features=max_features,
            ngram_range=ngram_range,
            stop_words='english' if '[REMOVE_STOPWORDS]' else None,
            min_df=2,
            max_df=0.95,
            sublinear_tf=True
        )

        tfidf_matrix = vectorizer.fit_transform(texts)
        feature_names = vectorizer.get_feature_names_out()

        self.vectorizers['tfidf'] = vectorizer

        return {
            'matrix': tfidf_matrix,
            'feature_names': feature_names,
            'vocabulary': vectorizer.vocabulary_,
            'idf_scores': vectorizer.idf_
        }

    def train_word_embeddings(self, tokenized_texts, embedding_dim=300, window=5, min_count=5):
        """Train Word2Vec embeddings"""
        # Word2Vec
        w2v_model = Word2Vec(
            sentences=tokenized_texts,
            vector_size=embedding_dim,
            window=window,
            min_count=min_count,
            workers=4,
            epochs=100
        )

        self.models['word2vec'] = w2v_model

        # FastText (handles out-of-vocabulary words)
        ft_model = FastText(
            sentences=tokenized_texts,
            vector_size=embedding_dim,
            window=window,
            min_count=min_count,
            workers=4,
            epochs=100
        )

        self.models['fasttext'] = ft_model

        return {
            'word2vec': w2v_model,
            'fasttext': ft_model,
            'vocab_size': len(w2v_model.wv.key_to_index),
            'embedding_dim': embedding_dim
        }

    def train_doc_embeddings(self, texts, embedding_dim=300, window=5, min_count=5):
        """Train Doc2Vec embeddings"""
        from gensim.models.doc2vec import TaggedDocument

        # Create tagged documents
        tagged_docs = [TaggedDocument(words=text.split() if isinstance(text, str) else text,
                                     tags=[i]) for i, text in enumerate(texts)]

        # Train Doc2Vec model
        d2v_model = Doc2Vec(
            documents=tagged_docs,
            vector_size=embedding_dim,
            window=window,
            min_count=min_count,
            workers=4,
            epochs=100,
            dm=1  # PV-DM
        )

        self.models['doc2vec'] = d2v_model

        # Get document vectors
        doc_vectors = np.array([d2v_model.dv[i] for i in range(len(texts))])

        return {
            'model': d2v_model,
            'document_vectors': doc_vectors,
            'embedding_dim': embedding_dim
        }

    def extract_linguistic_features(self, texts):
        """Extract linguistic and stylistic features"""
        features = []

        for text in texts:
            if isinstance(text, list):
                text = ' '.join(text)

            # Basic counts
            char_count = len(text)
            word_count = len(text.split())
            sent_count = len(sent_tokenize(text))

            # Advanced features
            avg_word_length = np.mean([len(word) for word in text.split()])
            avg_sent_length = word_count / sent_count if sent_count > 0 else 0

            # Readability features
            syllable_count = self.count_syllables(text)
            flesch_reading_ease = self.flesch_reading_ease(text, word_count, sent_count, syllable_count)

            # Lexical diversity
            unique_words = len(set(text.lower().split()))
            lexical_diversity = unique_words / word_count if word_count > 0 else 0

            # POS distribution
            pos_counts = self.get_pos_distribution(text)

            # Punctuation features
            punct_features = self.get_punctuation_features(text)

            feature_vector = {
                'char_count': char_count,
                'word_count': word_count,
                'sent_count': sent_count,
                'avg_word_length': avg_word_length,
                'avg_sent_length': avg_sent_length,
                'syllable_count': syllable_count,
                'flesch_reading_ease': flesch_reading_ease,
                'lexical_diversity': lexical_diversity,
                **pos_counts,
                **punct_features
            }

            features.append(feature_vector)

        return pd.DataFrame(features)

    def count_syllables(self, text):
        """Count syllables in text (approximation)"""
        vowels = 'aeiouy'
        syllable_count = 0
        words = text.lower().split()

        for word in words:
            word = re.sub(r'[^a-z]', '', word)
            if word:
                syllables = 0
                prev_was_vowel = False
                for char in word:
                    is_vowel = char in vowels
                    if is_vowel and not prev_was_vowel:
                        syllables += 1
                    prev_was_vowel = is_vowel
                if word.endswith('e'):
                    syllables -= 1
                if syllables == 0:
                    syllables = 1
                syllable_count += syllables

        return syllable_count

    def flesch_reading_ease(self, text, word_count, sent_count, syllable_count):
        """Calculate Flesch Reading Ease score"""
        if sent_count == 0 or word_count == 0:
            return 0

        avg_sent_length = word_count / sent_count
        avg_syllables = syllable_count / word_count

        score = 206.835 - (1.015 * avg_sent_length) - (84.6 * avg_syllables)
        return max(0, min(100, score))

    def get_pos_distribution(self, text):
        """Get part-of-speech distribution"""
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)

        pos_counts = {}
        total_tags = len(pos_tags)

        for word, tag in pos_tags:
            pos_counts[f'pos_[TAG]'] = pos_counts.get(f'pos_[TAG]', 0) + 1

        # Normalize to proportions
        for tag in pos_counts:
            pos_counts[tag] /= total_tags

        return pos_counts

    def get_punctuation_features(self, text):
        """Extract punctuation-based features"""
        punct_counts = {}

        # Count specific punctuation marks
        punct_marks = ['.', ',', '!', '?', ';', ':', '"', "'", '-', '(', ')']
        for mark in punct_marks:
            punct_counts[f'punct_{mark.replace(".", "period").replace(",", "comma")}'] = text.count(mark)

        # Total punctuation
        total_punct = sum(punct_counts.values())
        punct_counts['total_punctuation'] = total_punct
        punct_counts['punct_ratio'] = total_punct / len(text) if len(text) > 0 else 0

        return punct_counts

# Initialize feature engineer
feature_engineer = TextFeatureEngineer()

# Create different types of features
bow_features = feature_engineer.create_bow_features([PROCESSED_TEXTS])
tfidf_features = feature_engineer.create_tfidf_features([PROCESSED_TEXTS])
word_embeddings = feature_engineer.train_word_embeddings([TOKENIZED_TEXTS])
doc_embeddings = feature_engineer.train_doc_embeddings([PROCESSED_TEXTS])
linguistic_features = feature_engineer.extract_linguistic_features([TEXTS])
```

SENTIMENT ANALYSIS:
Comprehensive Sentiment Analysis:
```python
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix

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
            print(f"Error loading transformer models: [E]")

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
            print(f"Emotion analysis not available: [E]")
            return [{'text': text, 'error': str(e)} for text in texts]

    def train_custom_sentiment_model(self, texts, labels, test_size=0.2):
        """Train custom sentiment classification model"""
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
```

TOPIC MODELING:
Advanced Topic Discovery:
```python
from gensim import corpora, models
from gensim.models import LdaModel, LdaMulticore, HdpModel
from sklearn.decomposition import LatentDirichletAllocation, NMF
from sklearn.feature_extraction.text import CountVectorizer
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
import matplotlib.pyplot as plt
import seaborn as sns

class TopicModeler:
    def __init__(self):
        self.models = {}
        self.dictionaries = {}
        self.corpora = {}

    def prepare_corpus(self, texts, min_df=2, max_df=0.95):
        """Prepare corpus for topic modeling"""
        # Create dictionary
        dictionary = Dictionary(texts)

        # Filter extremes
        dictionary.filter_extremes(no_below=min_df, no_above=max_df)

        # Create corpus
        corpus = [dictionary.doc2bow(text) for text in texts]

        self.dictionaries['main'] = dictionary
        self.corpora['main'] = corpus

        return corpus, dictionary

    def lda_topic_modeling(self, texts, num_topics=10, passes=20, alpha='auto', eta='auto'):
        """Perform LDA topic modeling with Gensim"""
        corpus, dictionary = self.prepare_corpus(texts)

        # Train LDA model
        lda_model = LdaMulticore(
            corpus=corpus,
            id2word=dictionary,
            num_topics=num_topics,
            random_state=42,
            chunksize=100,
            passes=passes,
            alpha=alpha,
            eta=eta,
            per_word_topics=True,
            workers=4
        )

        self.models['lda'] = lda_model

        # Get topics
        topics = []
        for i in range(num_topics):
            topic_words = lda_model.show_topic(i, topn=20)
            topics.append({
                'topic_id': i,
                'words': topic_words,
                'top_words': [word for word, prob in topic_words[:10]]
            })

        # Document topic distributions
        doc_topic_dists = []
        for i, doc in enumerate(corpus):
            topic_dist = lda_model.get_document_topics(doc, minimum_probability=0.01)
            doc_topic_dists.append(topic_dist)

        # Model evaluation
        coherence_model = models.CoherenceModel(
            model=lda_model, texts=texts, dictionary=dictionary, coherence='c_v'
        )
        coherence_score = coherence_model.get_coherence()

        perplexity = lda_model.log_perplexity(corpus)

        return {
            'model': lda_model,
            'topics': topics,
            'doc_topic_distributions': doc_topic_dists,
            'coherence_score': coherence_score,
            'perplexity': perplexity,
            'num_topics': num_topics
        }

    def bert_topic_modeling(self, texts, nr_topics='auto', min_topic_size=10):
        """Perform topic modeling using BERTopic"""
        # Initialize sentence transformer
        sentence_model = SentenceTransformer('[SENTENCE_MODEL]')

        # Initialize BERTopic
        topic_model = BERTopic(
            nr_topics=nr_topics,
            min_topic_size=min_topic_size,
            embedding_model=sentence_model,
            verbose=True
        )

        # Fit model
        topics, probabilities = topic_model.fit_transform(texts)

        self.models['bertopic'] = topic_model

        # Get topic information
        topic_info = topic_model.get_topic_info()

        # Get representative documents
        representative_docs = {}
        for topic_id in topic_info['Topic'].unique():
            if topic_id != -1:  # Exclude outlier topic
                docs = topic_model.get_representative_docs(topic_id)
                representative_docs[topic_id] = docs

        return {
            'model': topic_model,
            'topics': topics,
            'probabilities': probabilities,
            'topic_info': topic_info,
            'representative_docs': representative_docs,
            'num_topics': len(topic_info) - 1  # Exclude outlier topic
        }

    def hierarchical_topic_modeling(self, texts):
        """Perform hierarchical topic modeling"""
        corpus, dictionary = self.prepare_corpus(texts)

        # Hierarchical Dirichlet Process
        hdp_model = HdpModel(
            corpus=corpus,
            id2word=dictionary,
            random_state=42
        )

        self.models['hdp'] = hdp_model

        # Get topics (HDP automatically determines number of topics)
        topics = hdp_model.show_topics(num_topics=50, formatted=False)

        # Filter significant topics
        significant_topics = []
        for topic_id, topic_words in topics:
            # Calculate topic weight
            topic_weight = sum([prob for word, prob in topic_words])
            if topic_weight > 0.01:  # Threshold for significance
                significant_topics.append({
                    'topic_id': topic_id,
                    'words': topic_words,
                    'weight': topic_weight,
                    'top_words': [word for word, prob in topic_words[:10]]
                })

        return {
            'model': hdp_model,
            'all_topics': topics,
            'significant_topics': significant_topics,
            'num_significant_topics': len(significant_topics)
        }

    def nmf_topic_modeling(self, texts, num_topics=10):
        """Non-negative Matrix Factorization for topic modeling"""
        # Vectorize texts
        vectorizer = CountVectorizer(
            max_features=1000,
            ngram_range=(1, 2),
            stop_words='english',
            min_df=2,
            max_df=0.95
        )

        doc_term_matrix = vectorizer.fit_transform(texts)

        # Fit NMF model
        nmf_model = NMF(
            n_components=num_topics,
            random_state=42,
            max_iter=100,
            alpha=0.1,
            l1_ratio=0.5
        )

        doc_topic_matrix = nmf_model.fit_transform(doc_term_matrix)
        topic_word_matrix = nmf_model.components_

        # Get feature names
        feature_names = vectorizer.get_feature_names_out()

        # Extract topics
        topics = []
        for topic_idx in range(num_topics):
            top_word_indices = topic_word_matrix[topic_idx].argsort()[-20:][::-1]
            top_words = [feature_names[i] for i in top_word_indices]
            word_weights = [topic_word_matrix[topic_idx][i] for i in top_word_indices]

            topics.append({
                'topic_id': topic_idx,
                'top_words': top_words,
                'word_weights': word_weights
            })

        self.models['nmf'] = nmf_model

        return {
            'model': nmf_model,
            'vectorizer': vectorizer,
            'topics': topics,
            'doc_topic_matrix': doc_topic_matrix,
            'topic_word_matrix': topic_word_matrix,
            'num_topics': num_topics
        }

    def dynamic_topic_modeling(self, texts, timestamps, time_slices):
        """Dynamic topic modeling to track topic evolution over time"""
        corpus, dictionary = self.prepare_corpus(texts)

        # Group documents by time slices
        time_slice_counts = []
        sorted_indices = np.argsort(timestamps)

        current_slice = 0
        current_count = 0

        for i, idx in enumerate(sorted_indices):
            if timestamps[idx] <= time_slices[current_slice]:
                current_count += 1
            else:
                time_slice_counts.append(current_count)
                current_slice += 1
                current_count = 1

        time_slice_counts.append(current_count)

        # Dynamic Topic Model
        from gensim.models import LdaSeqModel

        try:
            dtm_model = LdaSeqModel(
                corpus=corpus,
                id2word=dictionary,
                time_slice=time_slice_counts,
                num_topics=[NUM_TOPICS],
                chunksize=1,
                passes=20,
                random_state=42
            )

            self.models['dtm'] = dtm_model

            # Extract topic evolution
            topic_evolution = []
            for time_point in range(len(time_slices)):
                time_topics = []
                for topic_id in range([NUM_TOPICS]):
                    topic_words = dtm_model.show_topic(
                        topicid=topic_id,
                        time=time_point,
                        topn=10
                    )
                    time_topics.append({
                        'topic_id': topic_id,
                        'time_slice': time_point,
                        'words': topic_words
                    })
                topic_evolution.append(time_topics)

            return {
                'model': dtm_model,
                'topic_evolution': topic_evolution,
                'time_slices': time_slices,
                'time_slice_counts': time_slice_counts
            }

        except Exception as e:
            print(f"Dynamic topic modeling failed: [E]")
            return None

    def evaluate_topic_models(self, texts, topic_ranges=range(2, 21)):
        """Evaluate topic models across different numbers of topics"""
        corpus, dictionary = self.prepare_corpus(texts)

        evaluation_results = []

        for num_topics in topic_ranges:
            print(f"Evaluating [NUM_TOPICS] topics...")

            # Train LDA model
            lda_model = LdaModel(
                corpus=corpus,
                id2word=dictionary,
                num_topics=num_topics,
                random_state=42,
                passes=10
            )

            # Calculate coherence
            coherence_model = models.CoherenceModel(
                model=lda_model, texts=texts, dictionary=dictionary, coherence='c_v'
            )
            coherence_score = coherence_model.get_coherence()

            # Calculate perplexity
            perplexity = lda_model.log_perplexity(corpus)

            evaluation_results.append({
                'num_topics': num_topics,
                'coherence': coherence_score,
                'perplexity': perplexity
            })

        return pd.DataFrame(evaluation_results)

    def visualize_topics(self, model_type='lda'):
        """Create interactive topic visualizations"""
        if model_type == 'lda' and 'lda' in self.models:
            # pyLDAvis for LDA
            vis = gensimvis.prepare(
                self.models['lda'],
                self.corpora['main'],
                self.dictionaries['main']
            )
            return vis

        elif model_type == 'bertopic' and 'bertopic' in self.models:
            # BERTopic visualizations
            model = self.models['bertopic']

            # Topic visualization
            fig1 = model.visualize_topics()

            # Topic hierarchy
            fig2 = model.visualize_hierarchy()

            # Topic heatmap
            fig3 = model.visualize_heatmap()

            return {
                'topics': fig1,
                'hierarchy': fig2,
                'heatmap': fig3
            }

        return None

# Initialize topic modeler
topic_modeler = TopicModeler()

# Perform different types of topic modeling
lda_results = topic_modeler.lda_topic_modeling([PROCESSED_TEXTS], num_topics=[NUM_TOPICS])
bert_results = topic_modeler.bert_topic_modeling([TEXT_DATA])
hdp_results = topic_modeler.hierarchical_topic_modeling([PROCESSED_TEXTS])
nmf_results = topic_modeler.nmf_topic_modeling([TEXT_DATA], num_topics=[NUM_TOPICS])

# Evaluate optimal number of topics
evaluation_results = topic_modeler.evaluate_topic_models([PROCESSED_TEXTS])
```

NAMED ENTITY RECOGNITION:
Comprehensive Entity Extraction:
```python
import spacy
from spacy import displacy
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification
import pandas as pd
from collections import defaultdict

class NamedEntityRecognizer:
    def __init__(self):
        self.models = {}
        self.setup_models()

    def setup_models(self):
        """Initialize NER models"""
        # spaCy models
        try:
            self.models['spacy_sm'] = spacy.load('en_core_web_sm')
            self.models['spacy_lg'] = spacy.load('en_core_web_lg')
        except OSError:
            print("spaCy models not found. Install with: python -m spacy download en_core_web_sm")

        # Transformer-based models
        try:
            self.models['bert_ner'] = pipeline(
                'ner',
                model='dbmdz/bert-large-cased-finetuned-conll03-english',
                aggregation_strategy='simple'
            )

            self.models['roberta_ner'] = pipeline(
                'ner',
                model='Jean-Baptiste/roberta-large-ner-english',
                aggregation_strategy='simple'
            )

            self.models['biobert'] = pipeline(
                'ner',
                model='dmis-lab/biobert-v1.1',
                aggregation_strategy='simple'
            )

        except Exception as e:
            print(f"Error loading transformer NER models: [E]")

    def extract_entities_spacy(self, texts, model_name='spacy_sm'):
        """Extract named entities using spaCy"""
        if model_name not in self.models:
            return None

        nlp = self.models[model_name]
        results = []

        for text in texts:
            doc = nlp(text)

            entities = []
            for ent in doc.ents:
                entities.append({
                    'text': ent.text,
                    'label': ent.label_,
                    'description': spacy.explain(ent.label_),
                    'start_char': ent.start_char,
                    'end_char': ent.end_char,
                    'confidence': ent._.get('confidence', 1.0)
                })

            # Additional linguistic features
            noun_phrases = [chunk.text for chunk in doc.noun_chunks]

            results.append({
                'text': text,
                'entities': entities,
                'noun_phrases': noun_phrases,
                'entity_count': len(entities),
                'unique_labels': list(set([e['label'] for e in entities]))
            })

        return results

    def extract_entities_transformer(self, texts, model_name='bert_ner'):
        """Extract named entities using transformer models"""
        if model_name not in self.models:
            return None

        ner_pipeline = self.models[model_name]
        results = []

        for text in texts:
            try:
                entities = ner_pipeline(text)

                # Process entities
                processed_entities = []
                for entity in entities:
                    processed_entities.append({
                        'text': entity['word'],
                        'label': entity['entity_group'],
                        'confidence': entity['score'],
                        'start_char': entity.get('start', 0),
                        'end_char': entity.get('end', 0)
                    })

                results.append({
                    'text': text,
                    'entities': processed_entities,
                    'entity_count': len(processed_entities),
                    'unique_labels': list(set([e['label'] for e in processed_entities]))
                })

            except Exception as e:
                results.append({
                    'text': text,
                    'entities': [],
                    'error': str(e)
                })

        return results

    def extract_custom_entities(self, texts, entity_patterns):
        """Extract custom entities using regex patterns"""
        results = []

        for text in texts:
            entities = []

            for pattern_name, pattern in entity_patterns.items():
                matches = re.finditer(pattern, text, re.IGNORECASE)

                for match in matches:
                    entities.append({
                        'text': match.group(),
                        'label': pattern_name,
                        'start_char': match.start(),
                        'end_char': match.end(),
                        'confidence': 1.0
                    })

            results.append({
                'text': text,
                'entities': entities,
                'entity_count': len(entities)
            })

        return results

    def entity_linking(self, entities, knowledge_base):
        """Link entities to knowledge base entries"""
        linked_entities = []

        for entity in entities:
            entity_text = entity['text'].lower()

            # Simple exact match linking (can be enhanced with fuzzy matching)
            if entity_text in knowledge_base:
                linked_entity = entity.copy()
                linked_entity['linked_id'] = knowledge_base[entity_text]['id']
                linked_entity['linked_description'] = knowledge_base[entity_text]['description']
                linked_entity['linked_category'] = knowledge_base[entity_text]['category']
                linked_entities.append(linked_entity)
            else:
                entity['linked_id'] = None
                linked_entities.append(entity)

        return linked_entities

    def entity_relationship_extraction(self, texts):
        """Extract relationships between entities"""
        if 'spacy_lg' not in self.models:
            return None

        nlp = self.models['spacy_lg']
        results = []

        for text in texts:
            doc = nlp(text)

            relationships = []
            entities = [(ent.text, ent.label_, ent.start, ent.end) for ent in doc.ents]

            # Simple relationship extraction based on dependency parsing
            for token in doc:
                if token.dep_ in ['nsubj', 'dobj', 'pobj']:
                    # Find related entities
                    subj_ents = [ent for ent in entities if ent[2] <= token.head.i <= ent[3]]
                    obj_ents = [ent for ent in entities if ent[2] <= token.i <= ent[3]]

                    if subj_ents and obj_ents:
                        relationships.append({
                            'subject': subj_ents[0][0],
                            'predicate': token.head.text,
                            'object': obj_ents[0][0],
                            'relation_type': token.dep_
                        })

            results.append({
                'text': text,
                'entities': entities,
                'relationships': relationships
            })

        return results

    def entity_cooccurrence_analysis(self, ner_results):
        """Analyze entity co-occurrence patterns"""
        cooccurrence_matrix = defaultdict(lambda: defaultdict(int))
        entity_counts = defaultdict(int)

        for result in ner_results:
            entities = [e['text'].lower() for e in result['entities']]

            # Count individual entities
            for entity in entities:
                entity_counts[entity] += 1

            # Count co-occurrences
            for i, entity1 in enumerate(entities):
                for j, entity2 in enumerate(entities):
                    if i != j:
                        cooccurrence_matrix[entity1][entity2] += 1

        # Convert to DataFrame for analysis
        entities_list = list(entity_counts.keys())
        matrix_data = []

        for entity1 in entities_list:
            row = []
            for entity2 in entities_list:
                row.append(cooccurrence_matrix[entity1][entity2])
            matrix_data.append(row)

        cooccurrence_df = pd.DataFrame(
            matrix_data,
            index=entities_list,
            columns=entities_list
        )

        return {
            'cooccurrence_matrix': cooccurrence_df,
            'entity_counts': dict(entity_counts),
            'top_entities': sorted(entity_counts.items(), key=lambda x: x[1], reverse=True)[:20]
        }

    def visualize_entities(self, text, model_name='spacy_sm'):
        """Visualize named entities in text"""
        if model_name not in self.models:
            return None

        nlp = self.models[model_name]
        doc = nlp(text)

        # Generate visualization
        html = displacy.render(doc, style='ent', jupyter=False)

        return html

# Initialize NER system
ner_system = NamedEntityRecognizer()

# Extract entities using different models
spacy_entities = ner_system.extract_entities_spacy([TEXT_DATA])
transformer_entities = ner_system.extract_entities_transformer([TEXT_DATA])

# Custom entity extraction
custom_patterns = {
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'phone': r'\b\d{3}-\d{3}-\d{4}\b',
    'currency': r'\$\d+(?:,\d{3})*(?:\.\d{2})?',
    'date': r'\b\d{1,2}/\d{1,2}/\d{4}\b'
}
custom_entities = ner_system.extract_custom_entities([TEXT_DATA], custom_patterns)

# Entity relationship extraction
entity_relationships = ner_system.entity_relationship_extraction([TEXT_DATA])

# Co-occurrence analysis
cooccurrence_analysis = ner_system.entity_cooccurrence_analysis([ENTITY_RESULTS])
```

ADVANCED TEXT ANALYTICS:
Specialized Analysis Methods:
```python
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from umap import UMAP
import networkx as nx
from textstat import flesch_reading_ease, flesch_kincaid_grade, automated_readability_index
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class AdvancedTextAnalytics:
    def __init__(self):
        self.models = {}
        self.results = {}

    def document_clustering(self, texts, method='kmeans', n_clusters=5):
        """Cluster documents based on content similarity"""
        # Create document embeddings
        vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
        doc_vectors = vectorizer.fit_transform(texts)

        if method == 'kmeans':
            clusterer = KMeans(n_clusters=n_clusters, random_state=42)
        elif method == 'dbscan':
            clusterer = DBSCAN(eps=0.5, min_samples=5)
        elif method == 'hierarchical':
            clusterer = AgglomerativeClustering(n_clusters=n_clusters)

        cluster_labels = clusterer.fit_predict(doc_vectors.toarray())

        # Analyze clusters
        cluster_analysis = []
        for cluster_id in set(cluster_labels):
            if cluster_id != -1:  # Exclude noise cluster for DBSCAN
                cluster_docs = [texts[i] for i, label in enumerate(cluster_labels) if label == cluster_id]
                cluster_texts = ' '.join(cluster_docs)

                # Get top terms for cluster
                cluster_vectorizer = TfidfVectorizer(max_features=20, stop_words='english')
                cluster_tfidf = cluster_vectorizer.fit_transform([cluster_texts])
                feature_names = cluster_vectorizer.get_feature_names_out()
                top_terms = feature_names[cluster_tfidf.toarray()[0].argsort()[-10:][::-1]]

                cluster_analysis.append({
                    'cluster_id': cluster_id,
                    'size': len(cluster_docs),
                    'top_terms': top_terms.tolist(),
                    'sample_docs': cluster_docs[:3]
                })

        return {
            'cluster_labels': cluster_labels,
            'cluster_analysis': cluster_analysis,
            'n_clusters': len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)
        }

    def text_similarity_analysis(self, texts, method='cosine'):
        """Analyze similarity between texts"""
        from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

        # Create embeddings
        vectorizer = TfidfVectorizer(stop_words='english')
        text_vectors = vectorizer.fit_transform(texts)

        if method == 'cosine':
            similarity_matrix = cosine_similarity(text_vectors)
        elif method == 'euclidean':
            similarity_matrix = euclidean_distances(text_vectors)

        # Find most similar pairs
        similarity_pairs = []
        n_texts = len(texts)

        for i in range(n_texts):
            for j in range(i+1, n_texts):
                similarity_pairs.append({
                    'text1_index': i,
                    'text2_index': j,
                    'similarity': similarity_matrix[i][j],
                    'text1_preview': texts[i][:100] + '...' if len(texts[i]) > 100 else texts[i],
                    'text2_preview': texts[j][:100] + '...' if len(texts[j]) > 100 else texts[j]
                })

        # Sort by similarity
        similarity_pairs.sort(key=lambda x: x['similarity'], reverse=True)

        return {
            'similarity_matrix': similarity_matrix,
            'top_similar_pairs': similarity_pairs[:10],
            'least_similar_pairs': similarity_pairs[-10:]
        }

    def readability_analysis(self, texts):
        """Analyze text readability using multiple metrics"""
        readability_scores = []

        for text in texts:
            scores = {
                'flesch_reading_ease': flesch_reading_ease(text),
                'flesch_kincaid_grade': flesch_kincaid_grade(text),
                'automated_readability_index': automated_readability_index(text),
                'word_count': len(text.split()),
                'sentence_count': len(sent_tokenize(text)),
                'avg_sentence_length': len(text.split()) / len(sent_tokenize(text)) if len(sent_tokenize(text)) > 0 else 0,
                'syllable_count': self.count_syllables(text),
                'complex_words': self.count_complex_words(text)
            }

            # Readability interpretation
            fre_score = scores['flesch_reading_ease']
            if fre_score >= 90:
                scores['reading_level'] = 'Very Easy'
            elif fre_score >= 80:
                scores['reading_level'] = 'Easy'
            elif fre_score >= 70:
                scores['reading_level'] = 'Fairly Easy'
            elif fre_score >= 60:
                scores['reading_level'] = 'Standard'
            elif fre_score >= 50:
                scores['reading_level'] = 'Fairly Difficult'
            elif fre_score >= 30:
                scores['reading_level'] = 'Difficult'
            else:
                scores['reading_level'] = 'Very Difficult'

            readability_scores.append(scores)

        return pd.DataFrame(readability_scores)

    def count_syllables(self, text):
        """Count syllables in text"""
        vowels = 'aeiouy'
        syllable_count = 0
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

        for word in words:
            syllables = 0
            prev_was_vowel = False

            for char in word:
                is_vowel = char in vowels
                if is_vowel and not prev_was_vowel:
                    syllables += 1
                prev_was_vowel = is_vowel

            if word.endswith('e'):
                syllables = max(1, syllables - 1)
            if syllables == 0:
                syllables = 1

            syllable_count += syllables

        return syllable_count

    def count_complex_words(self, text):
        """Count complex words (3+ syllables)"""
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        complex_count = 0

        for word in words:
            if self.count_syllables(word) >= 3:
                complex_count += 1

        return complex_count

    def keyword_extraction(self, texts, method='tfidf', top_k=20):
        """Extract keywords using various methods"""
        if method == 'tfidf':
            vectorizer = TfidfVectorizer(
                max_features=1000,
                ngram_range=(1, 3),
                stop_words='english',
                min_df=2
            )

            tfidf_matrix = vectorizer.fit_transform(texts)
            feature_names = vectorizer.get_feature_names_out()

            # Get average TF-IDF scores
            mean_scores = tfidf_matrix.mean(axis=0).A1
            keyword_scores = list(zip(feature_names, mean_scores))
            keyword_scores.sort(key=lambda x: x[1], reverse=True)

            return {
                'method': 'tfidf',
                'keywords': keyword_scores[:top_k],
                'vectorizer': vectorizer
            }

        elif method == 'textrank':
            # TextRank implementation would go here
            # This is a simplified version
            from collections import Counter

            all_words = []
            for text in texts:
                words = word_tokenize(text.lower())
                words = [word for word in words if word.isalpha() and word not in stopwords.words('english')]
                all_words.extend(words)

            word_freq = Counter(all_words)
            top_words = word_freq.most_common(top_k)

            return {
                'method': 'frequency',
                'keywords': top_words
            }

    def text_summarization(self, texts, method='extractive', summary_ratio=0.3):
        """Generate text summaries"""
        if method == 'extractive':
            summaries = []

            for text in texts:
                sentences = sent_tokenize(text)
                if len(sentences) <= 3:
                    summaries.append(text)
                    continue

                # Simple extractive summarization using TF-IDF
                vectorizer = TfidfVectorizer(stop_words='english')
                sentence_vectors = vectorizer.fit_transform(sentences)

                # Calculate sentence scores (sum of TF-IDF values)
                sentence_scores = sentence_vectors.sum(axis=1).A1

                # Select top sentences
                num_sentences = max(1, int(len(sentences) * summary_ratio))
                top_indices = sentence_scores.argsort()[-num_sentences:][::-1]
                top_indices.sort()  # Maintain original order

                summary_sentences = [sentences[i] for i in top_indices]
                summary = ' '.join(summary_sentences)

                summaries.append(summary)

            return summaries

        elif method == 'abstractive':
            # This would use transformer models for abstractive summarization
            try:
                summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
                summaries = []

                for text in texts:
                    if len(text) > 1024:  # Model input limit
                        text = text[:1024]

                    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
                    summaries.append(summary[0]['summary_text'])

                return summaries

            except Exception as e:
                print(f"Abstractive summarization failed: [E]")
                return self.text_summarization(texts, method='extractive', summary_ratio=summary_ratio)

    def dimensionality_reduction_visualization(self, texts, method='tsne'):
        """Create 2D visualization of document embeddings"""
        # Create embeddings
        vectorizer = TfidfVectorizer(max_features=500, stop_words='english')
        embeddings = vectorizer.fit_transform(texts).toarray()

        if method == 'tsne':
            reducer = TSNE(n_components=2, random_state=42, perplexity=min(30, len(texts)-1))
        elif method == 'pca':
            reducer = PCA(n_components=2, random_state=42)
        elif method == 'umap':
            reducer = UMAP(n_components=2, random_state=42)

        reduced_embeddings = reducer.fit_transform(embeddings)

        # Create visualization
        plt.figure(figsize=(12, 8))
        scatter = plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1],
                            c=range(len(texts)), cmap='viridis', alpha=0.6)
        plt.colorbar(scatter)
        plt.title(f'Document Embeddings Visualization ({method.upper()})')
        plt.xlabel('Dimension 1')
        plt.ylabel('Dimension 2')

        # Add text previews on hover (conceptual)
        for i, (x, y) in enumerate(reduced_embeddings):
            if i % 10 == 0:  # Annotate every 10th point to avoid clutter
                preview = texts[i][:50] + '...' if len(texts[i]) > 50 else texts[i]
                plt.annotate(f'Doc [I]', (x, y), xytext=(5, 5),
                           textcoords='offset points', fontsize=8, alpha=0.7)

        plt.tight_layout()
        return plt.gcf()

    def create_word_cloud(self, texts, max_words=100):
        """Create word cloud visualization"""
        # Combine all texts
        combined_text = ' '.join(texts)

        # Create word cloud
        wordcloud = WordCloud(
            width=800,
            height=400,
            max_words=max_words,
            background_color='white',
            colormap='viridis',
            stopwords=set(stopwords.words('english'))
        ).generate(combined_text)

        # Plot
        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud')
        plt.tight_layout()

        return plt.gcf()

# Initialize advanced analytics
advanced_analytics = AdvancedTextAnalytics()

# Perform various analyses
clustering_results = advanced_analytics.document_clustering([TEXT_DATA])
similarity_analysis = advanced_analytics.text_similarity_analysis([TEXT_DATA])
readability_scores = advanced_analytics.readability_analysis([TEXT_DATA])
keywords = advanced_analytics.keyword_extraction([TEXT_DATA])
summaries = advanced_analytics.text_summarization([TEXT_DATA])
```

REPORTING AND VISUALIZATION:
Comprehensive Text Analytics Reporting:
```python
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_comprehensive_text_report(analysis_results):
    """Create comprehensive text analytics report"""

    # Set up the report structure
    report = {
        'executive_summary': create_executive_summary(analysis_results),
        'data_overview': create_data_overview_section(analysis_results),
        'preprocessing_report': create_preprocessing_report(analysis_results),
        'sentiment_analysis': create_sentiment_report(analysis_results),
        'topic_analysis': create_topic_report(analysis_results),
        'entity_analysis': create_entity_report(analysis_results),
        'advanced_analytics': create_advanced_analytics_report(analysis_results),
        'visualizations': create_visualization_suite(analysis_results),
        'insights_recommendations': create_insights_section(analysis_results)
    }

    return report

def create_visualization_suite(results):
    """Create comprehensive visualization suite"""

    fig = make_subplots(
        rows=3, cols=3,
        subplot_titles=[
            'Sentiment Distribution', 'Topic Coherence Scores', 'Entity Frequency',
            'Document Length Distribution', 'Reading Level Distribution', 'Keyword Frequency',
            'Temporal Sentiment Trends', 'Topic Evolution', 'Entity Co-occurrence Network'
        ],
        specs=[
            [{"type": "bar"}, {"type": "scatter"}, {"type": "bar"}],
            [{"type": "histogram"}, {"type": "pie"}, {"type": "bar"}],
            [{"type": "scatter"}, {"type": "heatmap"}, {"type": "scatter"}]
        ]
    )

    # Add visualizations to subplots
    # This would include all the specific plotting code for each analysis type

    fig.update_layout(height=1200, showlegend=False, title_text="Text Analytics Dashboard")

    return fig

def generate_insights_and_recommendations(analysis_results):
    """Generate actionable insights and recommendations"""

    insights = {
        'key_findings': [],
        'sentiment_insights': [],
        'topic_insights': [],
        'entity_insights': [],
        'content_quality_insights': [],
        'recommendations': []
    }

    # Extract key findings from each analysis component
    if 'sentiment' in analysis_results:
        sentiment_data = analysis_results['sentiment']

        # Sentiment insights
        positive_ratio = len([s for s in sentiment_data if s['vader']['label'] == 'positive']) / len(sentiment_data)
        insights['sentiment_insights'].append(f"Overall sentiment is {positive_ratio:.1%} positive")

        if positive_ratio < 0.3:
            insights['recommendations'].append("Consider addressing negative sentiment drivers")
        elif positive_ratio > 0.7:
            insights['recommendations'].append("Leverage positive sentiment for marketing/promotion")

    # Topic insights
    if 'topics' in analysis_results:
        topic_data = analysis_results['topics']
        insights['topic_insights'].append(f"Identified {len(topic_data['topics'])} main topics")

        # Most coherent topics
        coherent_topics = [t for t in topic_data['topics'] if t.get('coherence', 0) > 0.5]
        if coherent_topics:
            insights['topic_insights'].append(f"{len(coherent_topics)} topics show high coherence")

    return insights

# Create final report
def generate_final_report():
    """Generate final comprehensive report"""

    final_report = f"""
    # TEXT ANALYTICS COMPREHENSIVE REPORT

    ## Executive Summary
    Analysis of {[TEXT_VOLUME]} documents revealed {[KEY_FINDINGS]}.

    ## Key Metrics
    - Overall Sentiment: {[OVERALL_SENTIMENT]} ({[SENTIMENT_CONFIDENCE]}% confidence)
    - Primary Topics: {[TOP_TOPICS]}
    - Key Entities: {[TOP_ENTITIES]}
    - Average Reading Level: {[READING_LEVEL]}
    - Content Quality Score: {[QUALITY_SCORE]}/10

    ## Detailed Findings

    ### Sentiment Analysis
    {[SENTIMENT_DETAILED_FINDINGS]}

    ### Topic Analysis
    {[TOPIC_DETAILED_FINDINGS]}

    ### Entity Analysis
    {[ENTITY_DETAILED_FINDINGS]}

    ### Content Quality Assessment
    {[QUALITY_DETAILED_FINDINGS]}

    ## Recommendations
    {[STRATEGIC_RECOMMENDATIONS]}

    ## Technical Appendix
    - Processing Time: {[PROCESSING_TIME]}
    - Models Used: {[MODELS_USED]}
    - Data Quality Score: {[DATA_QUALITY_SCORE]}
    - Confidence Intervals: {[CONFIDENCE_INTERVALS]}
    """

    return final_report
```

OUTPUT REQUIREMENTS:
Deliver comprehensive text analytics analysis including:

1. **Data Processing Summary**
   - Text preprocessing pipeline and steps
   - Data cleaning and quality assessment
   - Feature engineering methods applied
   - Corpus statistics and characteristics

2. **Sentiment Analysis Results**
   - Multi-method sentiment scoring
   - Aspect-based sentiment analysis
   - Emotion detection and classification
   - Sentiment trends and patterns
   - Comparative sentiment analysis

3. **Topic Discovery**
   - Topic modeling with multiple algorithms
   - Topic coherence and quality metrics
   - Topic evolution over time
   - Topic relationships and hierarchy
   - Representative documents per topic

4. **Named Entity Recognition**
   - Multi-model entity extraction
   - Entity classification and linking
   - Entity relationship mapping
   - Co-occurrence analysis
   - Custom entity detection

5. **Advanced Text Analytics**
   - Document clustering and similarity
   - Keyword and keyphrase extraction
   - Text summarization
   - Readability and complexity analysis
   - Linguistic feature analysis

6. **Visualization Suite**
   - Interactive dashboards and plots
   - Word clouds and frequency distributions
   - Network visualizations
   - Temporal analysis charts
   - Dimensionality reduction plots

7. **Statistical Analysis**
   - Significance testing for patterns
   - Correlation analysis
   - Comparative analysis across groups
   - Time series analysis
   - Confidence intervals and error bars

8. **Model Performance**
   - Model accuracy and validation metrics
   - Cross-validation results
   - Feature importance analysis
   - Model comparison and selection
   - Confidence scores and uncertainty

9. **Business Intelligence**
   - Actionable insights and recommendations
   - Key performance indicators
   - Trend analysis and forecasting
   - Competitive analysis (if applicable)
   - ROI and impact assessment

10. **Technical Documentation**
    - Methodology documentation
    - Code and reproducibility information
    - Data sources and limitations
    - Model specifications and parameters
    - Quality assurance procedures
```

## Variables

[The template continues with 400+ comprehensive variables covering all aspects of text analytics and NLP, organized by category...]

### Data Source Variables
- [TEXT_DATA_SOURCE] - Source of text data for analysis
- [DATA_SOURCE_TYPE] - Type of data source (social media, documents, etc.)
- [TEXT_VOLUME] - Volume of text data (number of documents/words)
- [NUMBER_DOCUMENTS] - Total number of documents in dataset
- [TOTAL_WORDS] - Total word count across all documents
- [LANGUAGES] - Languages present in the text data
- [TIME_PERIOD] - Time period covered by the data
- [GEOGRAPHIC_SCOPE] - Geographic coverage of the data
- [DOMAIN_AREA] - Subject domain or topic area
- [TEXT_FORMAT] - Format of the text data
- [TEXT_ENCODING] - Character encoding of the text

### Analysis Objective Variables
- [ANALYSIS_OBJECTIVE] - Primary objective of text analysis
- [NLP_TECHNIQUES] - NLP techniques to be applied
- [SPECIFIC_TASKS] - Specific analysis tasks to perform
- [PRIMARY_ANALYSIS_GOAL] - Main goal of the analysis
- [SECONDARY_GOALS] - Additional analysis objectives
- [RESEARCH_QUESTIONS] - Research questions to address
- [BUSINESS_QUESTIONS] - Business questions to answer
- [EXPECTED_INSIGHTS] - Expected insights from analysis
- [SUCCESS_METRICS] - Metrics to measure success
- [DELIVERABLE_FORMAT] - Format of final deliverables

### Preprocessing Variables
- [LANGUAGE] - Primary language for processing
- [REMOVE_STOPWORDS] - Whether to remove stop words
- [LEMMATIZE] - Whether to apply lemmatization
- [CUSTOM_STOPWORDS] - Custom stop words to remove
- [MIN_WORD_LENGTH] - Minimum word length to keep
- [MAX_WORD_LENGTH] - Maximum word length to keep
- [NGRAM_RANGE] - N-gram range for feature extraction
- [CUSTOM_REPLACEMENTS] - Custom text replacements
- [PRESERVE_CASE_WORDS] - Words to preserve original case
- [NORMALIZATION_METHOD] - Text normalization method

### Feature Engineering Variables
- [VECTORIZATION_METHOD] - Method for text vectorization
- [MAX_FEATURES] - Maximum number of features to extract
- [MIN_DOCUMENT_FREQUENCY] - Minimum document frequency
- [MAX_DOCUMENT_FREQUENCY] - Maximum document frequency
- [EMBEDDING_DIMENSION] - Dimension of word embeddings
- [EMBEDDING_MODEL] - Pre-trained embedding model to use
- [WINDOW_SIZE] - Window size for word embeddings
- [VOCABULARY_SIZE] - Size of vocabulary
- [FEATURE_SELECTION_METHOD] - Method for feature selection
- [DIMENSIONALITY_REDUCTION] - Dimensionality reduction technique

### Sentiment Analysis Variables
- [SENTIMENT_MODEL] - Sentiment analysis model to use
- [SENTIMENT_THRESHOLD] - Threshold for sentiment classification
- [ASPECT_CATEGORIES] - Categories for aspect-based sentiment
- [EMOTION_MODEL] - Model for emotion detection
- [SENTIMENT_LEXICON] - Sentiment lexicon to use
- [POLARITY_CALCULATION] - Method for polarity calculation
- [SUBJECTIVITY_ANALYSIS] - Include subjectivity analysis
- [SENTIMENT_CONFIDENCE] - Confidence threshold for sentiment
- [MULTI_LABEL_SENTIMENT] - Multi-label sentiment classification
- [DOMAIN_SPECIFIC_SENTIMENT] - Domain-specific sentiment model

### Topic Modeling Variables
- [NUM_TOPICS] - Number of topics for modeling
- [TOPIC_MODEL_TYPE] - Type of topic model to use
- [COHERENCE_MEASURE] - Coherence measure for evaluation
- [TOPIC_COHERENCE_THRESHOLD] - Minimum coherence threshold
- [ALPHA_PARAMETER] - Alpha parameter for LDA
- [BETA_PARAMETER] - Beta parameter for LDA
- [PASSES] - Number of passes for topic modeling
- [ITERATIONS] - Number of iterations for training
- [TOPIC_WORD_THRESHOLD] - Minimum probability for topic words
- [HIERARCHICAL_TOPICS] - Enable hierarchical topic modeling

### Named Entity Recognition Variables
- [NER_MODEL] - Named entity recognition model
- [ENTITY_TYPES] - Types of entities to extract
- [CUSTOM_ENTITY_PATTERNS] - Custom regex patterns for entities
- [ENTITY_CONFIDENCE_THRESHOLD] - Confidence threshold for entities
- [ENTITY_LINKING] - Enable entity linking
- [KNOWLEDGE_BASE] - Knowledge base for entity linking
- [COREFERENCE_RESOLUTION] - Enable coreference resolution
- [RELATION_EXTRACTION] - Extract entity relationships
- [ENTITY_NORMALIZATION] - Normalize entity mentions
- [BIOMEDICAL_ENTITIES] - Include biomedical entity types

### Advanced Analytics Variables
- [CLUSTERING_METHOD] - Document clustering method
- [NUM_CLUSTERS] - Number of clusters for document clustering
- [SIMILARITY_METRIC] - Metric for similarity calculation
- [DIMENSIONALITY_REDUCTION_METHOD] - Method for dimension reduction
- [KEYWORD_EXTRACTION_METHOD] - Keyword extraction algorithm
- [NUM_KEYWORDS] - Number of keywords to extract
- [SUMMARIZATION_METHOD] - Text summarization approach
- [SUMMARY_LENGTH] - Length of generated summaries
- [READABILITY_METRICS] - Readability metrics to calculate
- [LINGUISTIC_FEATURES] - Linguistic features to extract

### Model Configuration Variables
- [TRAINING_DATA_SIZE] - Size of training dataset
- [VALIDATION_SPLIT] - Proportion for validation set
- [CROSS_VALIDATION_FOLDS] - Number of CV folds
- [RANDOM_STATE] - Random seed for reproducibility
- [BATCH_SIZE] - Batch size for processing
- [LEARNING_RATE] - Learning rate for training
- [REGULARIZATION_PARAMETER] - Regularization strength
- [EARLY_STOPPING] - Enable early stopping
- [MODEL_PERSISTENCE] - Save trained models
- [HYPERPARAMETER_TUNING] - Enable hyperparameter optimization

### Performance Metrics Variables
- [ACCURACY_SCORE] - Model accuracy score
- [PRECISION_SCORE] - Precision metric
- [RECALL_SCORE] - Recall metric
- [F1_SCORE] - F1 score
- [COHERENCE_SCORE] - Topic coherence score
- [PERPLEXITY_SCORE] - Model perplexity
- [SILHOUETTE_SCORE] - Clustering silhouette score
- [ARI_SCORE] - Adjusted Rand Index
- [MODULARITY_SCORE] - Network modularity
- [BLEU_SCORE] - BLEU score for summarization

### Output Variables
- [KEY_FINDINGS] - Summary of key findings
- [TOP_TOPICS] - Most prominent topics discovered
- [TOP_ENTITIES] - Most frequent entities
- [OVERALL_SENTIMENT] - Overall sentiment classification
- [READING_LEVEL] - Average reading level
- [QUALITY_SCORE] - Content quality assessment
- [PROCESSING_TIME] - Total processing time
- [MODELS_USED] - List of models employed
- [DATA_QUALITY_SCORE] - Data quality assessment
- [CONFIDENCE_INTERVALS] - Statistical confidence intervals

### Visualization Variables
- [PLOT_TYPE] - Type of visualization to create
- [COLOR_SCHEME] - Color scheme for visualizations
- [FIGURE_SIZE] - Dimensions of figures
- [INTERACTIVE_PLOTS] - Enable interactive visualizations
- [WORD_CLOUD_SETTINGS] - Word cloud configuration
- [NETWORK_LAYOUT] - Network visualization layout
- [HEATMAP_SETTINGS] - Heatmap visualization settings
- [TIME_SERIES_PLOT] - Temporal visualization settings
- [DASHBOARD_LAYOUT] - Dashboard arrangement
- [EXPORT_FORMAT] - Format for exporting visualizations

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
### Example 1: Social Media Sentiment Analysis
```
TEXT_DATA_SOURCE: "Twitter API posts about brand mentions"
ANALYSIS_OBJECTIVE: "Monitor brand sentiment and identify key issues"
NLP_TECHNIQUES: "Sentiment analysis, entity extraction, topic modeling"
SENTIMENT_MODEL: "VADER and transformer-based models"
NUM_TOPICS: "8 topics for thematic analysis"
```

### Example 2: Customer Review Analysis
```
TEXT_DATA_SOURCE: "E-commerce product reviews and ratings"
ANALYSIS_OBJECTIVE: "Understand customer satisfaction drivers"
ASPECT_CATEGORIES: "Quality, price, shipping, customer service"
SENTIMENT_MODEL: "Domain-specific retail sentiment model"
KEYWORD_EXTRACTION_METHOD: "TF-IDF with aspect focus"
```

### Example 3: Academic Literature Mining
```
TEXT_DATA_SOURCE: "PubMed abstracts and full-text articles"
ANALYSIS_OBJECTIVE: "Identify research trends and collaboration patterns"
NER_MODEL: "BioBERT for biomedical entity extraction"
TOPIC_MODEL_TYPE: "Hierarchical Dirichlet Process"
ENTITY_LINKING: "Link to medical ontologies (MeSH, UMLS)"
```

### Example 4: News Analysis
```
TEXT_DATA_SOURCE: "News articles from multiple sources"
ANALYSIS_OBJECTIVE: "Track story evolution and bias detection"
ENTITY_TYPES: "Person, organization, location, event"
TEMPORAL_ANALYSIS: "Track entity mentions over time"
SUMMARIZATION_METHOD: "Extractive and abstractive summarization"
```

### Example 5: Legal Document Analysis
```
TEXT_DATA_SOURCE: "Legal contracts and court documents"
ANALYSIS_OBJECTIVE: "Extract key clauses and identify risk factors"
CUSTOM_ENTITY_PATTERNS: "Legal entities, dates, monetary amounts"
DOMAIN_SPECIFIC_SENTIMENT: "Legal language sentiment model"
TOPIC_MODELING: "Legal topic classification and clustering"
```

## Customization Options

1. **Analysis Scope**
   - Single document analysis
   - Comparative analysis
   - Longitudinal studies
   - Cross-lingual analysis
   - Domain-specific analysis

2. **Model Complexity**
   - Rule-based approaches
   - Traditional ML methods
   - Deep learning models
   - Transformer architectures
   - Hybrid approaches

3. **Application Domain**
   - Social media analysis
   - Academic research
   - Business intelligence
   - Healthcare/biomedical
   - Legal and compliance

4. **Output Format**
   - Interactive dashboards
   - Static reports
   - API endpoints
   - Real-time monitoring
   - Batch processing results

5. **Integration Level**
   - Standalone analysis
   - Pipeline integration
   - Real-time processing
   - Cloud deployment
   - Edge computing