---
category: data-analytics
last_updated: 2025-11-10
related_templates:
- data-analytics/Research-Analytics/text-analytics-sentiment-analysis.md
- data-analytics/Research-Analytics/text-analytics-topic-modeling.md
- data-analytics/Research-Analytics/text-analytics-overview.md
tags:
- research-analytics
- text-analytics
- text-preprocessing
- feature-engineering
title: Text Analytics - Preprocessing and Feature Engineering
use_cases:
- Clean and preprocess raw text data for NLP analysis, including tokenization, normalization,
  and text cleaning operations.
- Engineer text features using TF-IDF, word embeddings, and linguistic features for
  machine learning models.
industries:
- education
- manufacturing
- technology
type: template
difficulty: intermediate
slug: text-analytics-preprocessing
---

# Text Analytics - Preprocessing and Feature Engineering

## Purpose
Provide comprehensive text preprocessing and feature engineering capabilities for NLP analysis. This template handles text cleaning, normalization, tokenization, and feature extraction to prepare raw text data for advanced analytics including sentiment analysis, topic modeling, and entity recognition.

## Quick Preprocessing Prompt
Preprocess [X] text documents from [source]. Clean (remove HTML, URLs, special characters), normalize (lowercase, expand contractions), tokenize, remove stopwords (keep negations), lemmatize, and engineer features: TF-IDF vectors (max 5000 features, include bigrams), word embeddings (300d), and linguistic features. Output cleaned corpus ready for [sentiment/topic/entity] analysis.

## Quick Start

**Example: Clean and Prepare Customer Reviews for Analysis**

```
You are a text preprocessing expert. Clean and prepare 10,000 customer product reviews for sentiment and topic analysis.

TEXT DATA:
- Source: E-commerce review database (CSV format)
- Volume: 10,000 reviews with HTML markup and social media handles
- Average length: 50-200 words per review
- Contains: URLs, emojis, hashtags, misspellings
- Language: English

PREPROCESSING REQUIREMENTS:
1. Remove HTML tags, URLs, email addresses
2. Expand contractions (don't → do not)
3. Remove special characters and punctuation
4. Convert to lowercase (preserve brand names: iPhone, Amazon)
5. Remove stopwords but keep negations (not, no, never)
6. Apply lemmatization for consistency

FEATURE ENGINEERING:
1. Create TF-IDF features (max 5000 features, bigrams and trigrams)
2. Train Word2Vec embeddings (300 dimensions)
3. Extract linguistic features (reading level, sentiment indicators)
4. Generate document-level feature vectors

EXPECTED OUTPUT:
- Cleaned text corpus ready for analysis
- TF-IDF feature matrix
- Word embeddings model
- Linguistic feature dataframe
- Preprocessing statistics and quality metrics
```

## Template

```
You are a text preprocessing expert. Process [TEXT_DATA_SOURCE] containing [TEXT_VOLUME] to prepare for [ANALYSIS_OBJECTIVE] using [PREPROCESSING_METHODS].

TEXT DATA OVERVIEW:
- Data source: [DATA_SOURCE_TYPE]
- Volume: [NUMBER_DOCUMENTS] documents
- Format: [TEXT_FORMAT]
- Language: [LANGUAGE]
- Encoding: [TEXT_ENCODING]
- Special characteristics: [DATA_CHARACTERISTICS]

### TEXT PREPROCESSING PIPELINE

#### Data Cleaning and Preparation
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

### Feature Engineering
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
            pos_counts[f'pos_{tag}'] = pos_counts.get(f'pos_{tag}', 0) + 1

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
```

## Variables

### Preprocessing Configuration Variables
- [LANGUAGE] - Primary language for processing (default: 'english')
- [REMOVE_STOPWORDS] - Whether to remove stop words (True/False)
- [LEMMATIZE] - Whether to apply lemmatization (True/False)
- [STEM] - Whether to apply stemming (True/False)
- [CUSTOM_STOPWORDS] - List of custom stop words to remove
- [MIN_WORD_LENGTH] - Minimum word length to keep (default: 2)
- [MAX_WORD_LENGTH] - Maximum word length to keep (default: 50)
- [PRESERVE_CASE_WORDS] - Words to preserve original case (e.g., brand names)
- [CUSTOM_REPLACEMENTS] - Dictionary of custom text replacements
- [NORMALIZATION_METHOD] - Text normalization method to use

### Text Cleaning Variables
- [REMOVE_HTML] - Remove HTML tags (True/False)
- [REMOVE_URLS] - Remove URLs and web links (True/False)
- [REMOVE_EMAILS] - Remove email addresses (True/False)
- [REMOVE_PHONE_NUMBERS] - Remove phone numbers (True/False)
- [REMOVE_SOCIAL_HANDLES] - Remove @mentions and #hashtags (True/False)
- [EXPAND_CONTRACTIONS] - Expand contractions (don't → do not) (True/False)
- [REMOVE_PUNCTUATION] - Remove punctuation marks (True/False)
- [REMOVE_NUMBERS] - Remove numeric characters (True/False)
- [REMOVE_EXTRA_WHITESPACE] - Normalize whitespace (True/False)
- [LOWERCASE] - Convert text to lowercase (True/False)

### Feature Engineering Variables
- [VECTORIZATION_METHOD] - Method for text vectorization (bow/tfidf/embeddings)
- [MAX_FEATURES] - Maximum number of features to extract (default: 10000)
- [NGRAM_RANGE] - N-gram range for feature extraction (e.g., (1, 2) for unigrams and bigrams)
- [MIN_DOCUMENT_FREQUENCY] - Minimum document frequency (default: 2)
- [MAX_DOCUMENT_FREQUENCY] - Maximum document frequency (default: 0.95)
- [EMBEDDING_DIMENSION] - Dimension of word embeddings (default: 300)
- [EMBEDDING_MODEL] - Pre-trained embedding model to use
- [WINDOW_SIZE] - Window size for word embeddings (default: 5)
- [MIN_COUNT] - Minimum word count for vocabulary inclusion (default: 5)
- [VOCABULARY_SIZE] - Size of vocabulary to maintain

### Input Data Variables
- [TEXT_DATA_SOURCE] - Source of text data for analysis
- [TEXT_CORPUS] - Raw text data to process
- [TEXT_FORMAT] - Format of the text data (CSV/JSON/TXT)
- [TEXT_ENCODING] - Character encoding of the text (UTF-8/ASCII)
- [NUMBER_DOCUMENTS] - Total number of documents in dataset
- [DATA_SOURCE_TYPE] - Type of data source (social media, documents, etc.)
- [TEXT_VOLUME] - Volume of text data to process
- [DATA_CHARACTERISTICS] - Special characteristics of the data

### Output Variables
- [PROCESSED_TEXTS] - Cleaned and processed text data
- [TOKENIZED_TEXTS] - Tokenized text data
- [BOW_MATRIX] - Bag of Words feature matrix
- [TFIDF_MATRIX] - TF-IDF feature matrix
- [WORD_EMBEDDINGS] - Trained word embedding model
- [DOC_EMBEDDINGS] - Document embedding vectors
- [LINGUISTIC_FEATURES] - Extracted linguistic feature dataframe

## Usage Examples

### Example 1: Basic Text Cleaning
```
TEXT_DATA_SOURCE: "Customer feedback forms with HTML content"
LANGUAGE: "english"
REMOVE_HTML: True
REMOVE_URLS: True
EXPAND_CONTRACTIONS: True
REMOVE_STOPWORDS: True
LEMMATIZE: True
MIN_WORD_LENGTH: 3
```

### Example 2: Social Media Text Processing
```
TEXT_DATA_SOURCE: "Twitter posts about product launches"
REMOVE_SOCIAL_HANDLES: True
REMOVE_URLS: True
PRESERVE_CASE_WORDS: ["iPhone", "MacBook", "iOS"]
CUSTOM_STOPWORDS: ["rt", "via"]
LEMMATIZE: True
REMOVE_STOPWORDS: False  # Keep all words for social media context
```

### Example 3: Academic Text Processing
```
TEXT_DATA_SOURCE: "Research paper abstracts from PubMed"
REMOVE_STOPWORDS: True
LEMMATIZE: True
CUSTOM_STOPWORDS: ["et al", "fig", "table"]
PRESERVE_CASE_WORDS: ["DNA", "RNA", "COVID-19"]
MIN_WORD_LENGTH: 3
VECTORIZATION_METHOD: "tfidf"
MAX_FEATURES: 5000
```

### Example 4: Feature Engineering for ML
```
VECTORIZATION_METHOD: "tfidf"
MAX_FEATURES: 10000
NGRAM_RANGE: (1, 3)
MIN_DOCUMENT_FREQUENCY: 5
MAX_DOCUMENT_FREQUENCY: 0.9
EMBEDDING_DIMENSION: 300
WINDOW_SIZE: 5
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Text Analytics Sentiment Analysis](text-analytics-sentiment-analysis.md)** - Leverage data analysis to drive informed decisions
- **[Text Analytics Topic Modeling](text-analytics-topic-modeling.md)** - Leverage data analysis to drive informed decisions
- **[Text Analytics Overview](text-analytics-overview.md)** - Leverage data analysis to drive informed decisions

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Text Analytics - Preprocessing and Feature Engineering)
2. Use [Text Analytics Sentiment Analysis](text-analytics-sentiment-analysis.md) for deeper analysis
3. Apply [Text Analytics Topic Modeling](text-analytics-topic-modeling.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Research Analytics](../../data-analytics/Research Analytics/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Clean and preprocess raw text data for NLP analysis, including tokenization, normalization, and text cleaning operations.**: Combine this template with related analytics and strategy frameworks
- **Engineer text features using TF-IDF, word embeddings, and linguistic features for machine learning models.**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Start with minimal preprocessing** - Apply only necessary cleaning operations to preserve important information
2. **Preserve domain-specific terms** - Use PRESERVE_CASE_WORDS for brand names, acronyms, and technical terms
3. **Choose appropriate tokenization** - Select word-level, sentence-level, or subword tokenization based on task
4. **Balance vocabulary size** - Use min_df and max_df to filter very rare and very common terms
5. **Test different feature representations** - Compare BOW, TF-IDF, and embeddings for your specific task
6. **Document preprocessing decisions** - Keep track of all preprocessing steps for reproducibility
7. **Handle missing values** - Check for and handle null or empty text entries
8. **Consider language-specific needs** - Adjust preprocessing for different languages and scripts
9. **Validate cleaning results** - Sample and review processed text to ensure quality
10. **Optimize for performance** - Batch process large corpora and use appropriate data structures

## Tips for Success

- Create a preprocessing pipeline that can be easily modified and reused
- Save intermediate results (cleaned text, tokens) for iterative development
- Use spaCy for advanced linguistic features and entity recognition
- Monitor memory usage when processing large text corpora
- Consider using HashingVectorizer for very large vocabularies
- Test preprocessing on a sample before processing entire dataset
- Keep original text alongside processed versions for reference
- Use consistent preprocessing across training and test data
- Profile your preprocessing code to identify bottlenecks
- Consider parallel processing for very large datasets
