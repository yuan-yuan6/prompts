---
title: Sentiment Analysis Template
category: data-analytics/Research Analytics
tags: ['nlp', 'sentiment-analysis', 'text-analytics', 'machine-learning']
use_cases:
  - Conduct comprehensive sentiment analysis using lexicon-based, machine learning, and transformer approaches including aspect-based sentiment and emotion detection.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Sentiment Analysis Template

## Purpose
Conduct comprehensive sentiment analysis using lexicon-based, machine learning, and transformer approaches including aspect-based sentiment and emotion detection.

## Quick Start

### For Data Scientists

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific conduct needs
- Gather necessary input data and parameters

**Step 2: Customize the Template**
- Fill in the required variables in the template section
- Adjust parameters to match your specific context
- Review examples to understand usage patterns

**Step 3: Generate and Refine**
- Run the template with your specifications
- Review the generated output
- Iterate and refine as needed

**Common Use Cases:**
- Conduct comprehensive sentiment analysis using lexicon-based, machine learning, and transformer approaches including aspect-based sentiment and emotion detection.
- Project-specific implementations
- Research and analysis workflows



## Template

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


## Purpose
Conduct comprehensive text mining and natural language processing analysis to extract insights, patterns, sentiments, topics, and knowledge from unstructured text data using advanced NLP techniques and machine learning methods.


## Quick Start

**Example: Customer Review Sentiment and Topic Analysis**


You are a text analytics expert. Analyze 50,000 customer product reviews from an e-commerce platform to understand sentiment drivers, identify key topics, and extract actionable insights for product improvement.

1. Perform multi-method sentiment analysis (VADER, TextBlob, transformer models)

2. Conduct aspect-based sentiment analysis for product features (quality, price, shipping, customer service)

4. Identify key themes in negative reviews (1-2 star ratings)

6. Compare sentiment trends across product categories and over time

- Overall sentiment distribution and trends

- Aspect-level sentiment scores with example quotes

- Word clouds for positive vs. negative reviews

Use VADER for initial sentiment scoring, then apply transformer-based models for nuanced analysis. Extract topics with coherence scores > 0.4 for interpretability.
```


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

[Content truncated for length - see original for full details]


## Variables

[The template continues with 400+ comprehensive variables covering all aspects of text analytics and NLP, organized by category...]

## Usage Examples

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


### Example 5: Legal Document Analysis
```
TEXT_DATA_SOURCE: "Legal contracts and court documents"
ANALYSIS_OBJECTIVE: "Extract key clauses and identify risk factors"
CUSTOM_ENTITY_PATTERNS: "Legal entities, dates, monetary amounts"
DOMAIN_SPECIFIC_SENTIMENT: "Legal language sentiment model"
TOPIC_MODELING: "Legal topic classification and clustering"
```


## Best Practices

1. **Focus**: Concentrate on the specific aspect covered by this template
2. **Integration**: Combine with related templates for comprehensive solutions
3. **Iteration**: Start simple and refine based on results
4. **Documentation**: Track your parameters and customizations

## Tips for Success

- Begin with the Quick Start section
- Customize variables to your specific context
- Validate outputs against your requirements
- Iterate and refine based on results

## Related Resources

See the overview file for the complete collection of related templates.

---

**Note:** This focused template is part of a comprehensive collection designed for improved usability.
