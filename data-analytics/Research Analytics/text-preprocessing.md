---
title: Text Preprocessing and Cleaning
category: data-analytics/Research Analytics
tags: [data-analytics, machine-learning, nlp, preprocessing, template, text-analytics]
use_cases:
  - Cleaning and normalizing text data for NLP analysis
  - Tokenizing and preparing text for machine learning
  - Creating text features for classification and modeling
related_templates:
  - text-analytics-overview.md
  - sentiment-analysis.md
  - text-classification.md
  - topic-modeling.md
last_updated: 2025-11-09
---

# Text Preprocessing and Cleaning

## Purpose
Clean, normalize, and prepare text data for NLP analysis through comprehensive preprocessing pipelines including tokenization, normalization, feature engineering, and quality assessment.

## Template

```
You are a text preprocessing expert. Clean and prepare [TEXT_DATA_SOURCE] for [ANALYSIS_TYPE] by applying [PREPROCESSING_STEPS] with focus on [QUALITY_OBJECTIVES].

TEXT DATA CHARACTERISTICS:
- Data source: [DATA_SOURCE_TYPE]
- Volume: [TEXT_VOLUME] ([NUMBER_DOCUMENTS] documents)
- Language(s): [LANGUAGES]
- Format: [TEXT_FORMAT]
- Encoding: [TEXT_ENCODING]
- Domain: [DOMAIN_AREA]

PREPROCESSING OBJECTIVES:
- Primary goal: [PREPROCESSING_GOAL]
- Quality requirements: [QUALITY_REQUIREMENTS]
- Output format: [OUTPUT_FORMAT]
- Performance constraints: [PERFORMANCE_CONSTRAINTS]

Apply comprehensive text preprocessing pipeline:

### TEXT PREPROCESSING PIPELINE

Comprehensive Data Cleaning:
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
                    placeholder = f"__PRESERVE_{i}__"
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

    def get_corpus_statistics(self, processed_corpus):
        """Calculate corpus-level statistics"""
        stats = {
            'total_documents': len(processed_corpus),
            'total_tokens': sum(doc['token_count'] for doc in processed_corpus),
            'total_chars': sum(doc['char_count'] for doc in processed_corpus),
            'total_words': sum(doc['word_count'] for doc in processed_corpus),
            'avg_tokens_per_doc': np.mean([doc['token_count'] for doc in processed_corpus]),
            'avg_words_per_doc': np.mean([doc['word_count'] for doc in processed_corpus]),
            'avg_chars_per_doc': np.mean([doc['char_count'] for doc in processed_corpus]),
            'median_tokens_per_doc': np.median([doc['token_count'] for doc in processed_corpus]),
            'std_tokens_per_doc': np.std([doc['token_count'] for doc in processed_corpus])
        }

        # Vocabulary statistics
        all_tokens = []
        for doc in processed_corpus:
            all_tokens.extend(doc['tokens'])

        stats['vocabulary_size'] = len(set(all_tokens))
        stats['token_frequency'] = pd.Series(all_tokens).value_counts()

        return stats

# Initialize preprocessor with custom configuration
preprocessor = TextPreprocessor(
    language='[LANGUAGE]',
    custom_config={
        'remove_stopwords': [REMOVE_STOPWORDS],
        'lemmatize': [LEMMATIZE],
        'custom_stopwords': [CUSTOM_STOPWORDS],
        'min_word_length': [MIN_WORD_LENGTH],
        'remove_html': [REMOVE_HTML],
        'expand_contractions': [EXPAND_CONTRACTIONS]
    }
)

# Process the text data
processed_texts = preprocessor.process_corpus([TEXT_CORPUS])

# Get corpus statistics
corpus_stats = preprocessor.get_corpus_statistics(processed_texts)
```

Feature Engineering:
```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from gensim.models import Word2Vec, Doc2Vec, FastText
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
            avg_word_length = np.mean([len(word) for word in text.split()]) if text.split() else 0
            avg_sent_length = word_count / sent_count if sent_count > 0 else 0

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
                'lexical_diversity': lexical_diversity,
                **pos_counts,
                **punct_features
            }

            features.append(feature_vector)

        return pd.DataFrame(features)

    def get_pos_distribution(self, text):
        """Get part-of-speech distribution"""
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)

        pos_counts = {}
        total_tags = len(pos_tags)

        for word, tag in pos_tags:
            pos_counts[f'pos_{tag}'] = pos_counts.get(f'pos_{tag}', 0) + 1

        # Normalize to proportions
        for tag in pos_counts:
            pos_counts[tag] /= total_tags if total_tags > 0 else 1

        return pos_counts

    def get_punctuation_features(self, text):
        """Extract punctuation-based features"""
        punct_counts = {}

        # Count specific punctuation marks
        punct_marks = {
            'period': '.', 'comma': ',', 'exclamation': '!',
            'question': '?', 'semicolon': ';', 'colon': ':',
            'quote': '"', 'apostrophe': "'", 'dash': '-'
        }

        for name, mark in punct_marks.items():
            punct_counts[f'punct_{name}'] = text.count(mark)

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
linguistic_features = feature_engineer.extract_linguistic_features([TEXTS])
```

OUTPUT REQUIREMENTS:
1. Cleaned and normalized text corpus
2. Tokenized documents with metadata
3. Feature matrices (BoW, TF-IDF, embeddings)
4. Linguistic feature dataframe
5. Corpus statistics and quality metrics
6. Vocabulary and frequency distributions
7. Processing pipeline documentation
```

## Variables

### Data Source Variables
- [TEXT_DATA_SOURCE] - Source of text data for preprocessing
- [DATA_SOURCE_TYPE] - Type of data source (social media, documents, etc.)
- [TEXT_VOLUME] - Volume of text data to process
- [NUMBER_DOCUMENTS] - Total number of documents
- [LANGUAGES] - Languages in the text data
- [TEXT_FORMAT] - Format of input text (plain text, HTML, JSON, etc.)
- [TEXT_ENCODING] - Character encoding (UTF-8, ASCII, etc.)
- [DOMAIN_AREA] - Subject domain of the text

### Preprocessing Configuration
- [ANALYSIS_TYPE] - Type of analysis to prepare for
- [PREPROCESSING_STEPS] - Specific preprocessing steps to apply
- [QUALITY_OBJECTIVES] - Quality goals for preprocessing
- [PREPROCESSING_GOAL] - Primary preprocessing objective
- [QUALITY_REQUIREMENTS] - Quality standards to meet
- [OUTPUT_FORMAT] - Desired output format
- [PERFORMANCE_CONSTRAINTS] - Performance requirements

### Cleaning Options
- [LANGUAGE] - Primary language for processing
- [REMOVE_STOPWORDS] - Remove stop words (true/false)
- [LEMMATIZE] - Apply lemmatization (true/false)
- [STEM] - Apply stemming (true/false)
- [REMOVE_HTML] - Remove HTML tags (true/false)
- [REMOVE_URLS] - Remove URLs (true/false)
- [REMOVE_EMAILS] - Remove email addresses (true/false)
- [EXPAND_CONTRACTIONS] - Expand contractions (true/false)
- [REMOVE_PUNCTUATION] - Remove punctuation (true/false)
- [LOWERCASE] - Convert to lowercase (true/false)

### Advanced Options
- [CUSTOM_STOPWORDS] - Additional stop words to remove
- [MIN_WORD_LENGTH] - Minimum word length to keep
- [MAX_WORD_LENGTH] - Maximum word length to keep
- [PRESERVE_CASE_WORDS] - Words to preserve original case
- [CUSTOM_REPLACEMENTS] - Custom text replacements

### Feature Engineering
- [MAX_FEATURES] - Maximum number of features to extract
- [NGRAM_RANGE] - N-gram range for features (e.g., (1, 2))
- [EMBEDDING_DIM] - Dimension of word embeddings
- [WINDOW_SIZE] - Context window size for embeddings
- [MIN_COUNT] - Minimum word frequency for embeddings

## Usage Examples

### Example 1: Social Media Text Preprocessing
```
TEXT_DATA_SOURCE: "Twitter posts about product reviews"
PREPROCESSING_STEPS: "Remove URLs, hashtags, mentions, expand contractions"
REMOVE_STOPWORDS: true
LEMMATIZE: true
CUSTOM_STOPWORDS: ["rt", "via"]
PRESERVE_CASE_WORDS: ["iPhone", "MacBook"]
```

### Example 2: Academic Paper Preprocessing
```
TEXT_DATA_SOURCE: "Research paper abstracts"
PREPROCESSING_STEPS: "Clean, tokenize, preserve technical terms"
REMOVE_STOPWORDS: false
LEMMATIZE: true
STEM: false
PRESERVE_CASE_WORDS: ["DNA", "RNA", "COVID-19"]
```

## Best Practices

1. **Understand your data**: Inspect samples before applying preprocessing
2. **Domain-specific considerations**: Preserve domain-specific terminology
3. **Balance cleaning and information loss**: Don't over-clean
4. **Test preprocessing impact**: Evaluate how it affects downstream tasks
5. **Document decisions**: Keep track of preprocessing choices
6. **Handle edge cases**: Plan for special characters, encodings, formats
7. **Validate output**: Check quality of preprocessed text
8. **Consider language-specific rules**: Different languages need different handling
9. **Preserve important patterns**: Keep emoticons, capitalization if relevant
10. **Version your preprocessing pipeline**: Track changes over time
