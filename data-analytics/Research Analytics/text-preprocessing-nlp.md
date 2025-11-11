---
title: Text Preprocessing & NLP Pipeline Template
category: data-analytics/Research Analytics
tags: ['nlp', 'text-analytics', 'preprocessing', 'tokenization']
use_cases:
  - Design comprehensive text preprocessing pipelines including cleaning, tokenization, normalization, and feature engineering for NLP analysis.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Text Preprocessing & NLP Pipeline Template

## Purpose
Design comprehensive text preprocessing pipelines including cleaning, tokenization, normalization, and feature engineering for NLP analysis.

## Quick Start

### For Data Scientists

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific design needs
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
- Design comprehensive text preprocessing pipelines including cleaning, tokenization, normalization, and feature engineering for NLP analysis.
- Project-specific implementations
- Research and analysis workflows



## Template

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


   - Text preprocessing pipeline and steps

   - Data cleaning and quality assessment

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



## Variables

[The template continues with 400+ comprehensive variables covering all aspects of text analytics and NLP, organized by category...]

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
