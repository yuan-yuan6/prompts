---
category: data-analytics
description: Clean, normalize, and transform raw text into structured features for NLP analysis including sentiment, topics, and entity recognition
title: Text Analytics - Preprocessing and Feature Engineering
tags:
- text-preprocessing
- feature-engineering
- nlp
- text-analytics
use_cases:
- Cleaning noisy text data from social media, web scraping, or user-generated content
- Normalizing text through tokenization, lemmatization, and stopword removal
- Engineering features using TF-IDF, word embeddings, and linguistic metrics
- Preparing text corpora for downstream sentiment, topic, or entity analysis
related_templates:
- data-analytics/Research-Analytics/text-analytics-sentiment-analysis.md
- data-analytics/Research-Analytics/text-analytics-topic-modeling.md
- data-analytics/Research-Analytics/text-analytics-entity-recognition.md
- data-analytics/Research-Analytics/text-analytics-overview.md
industries:
- technology
- retail
- healthcare
- finance
- media
type: framework
difficulty: intermediate
slug: text-analytics-preprocessing
---

# Text Analytics - Preprocessing and Feature Engineering

## Purpose
Provide comprehensive text preprocessing and feature engineering capabilities for NLP analysis. This template handles text cleaning, normalization, tokenization, and feature extraction to prepare raw text data for advanced analytics including sentiment analysis, topic modeling, and entity recognition.

## 🚀 Quick Start Prompt

> Preprocess **[TEXT DATA]** for **[ANALYSIS TYPE]**. Cover: (1) **Cleaning**—remove HTML, URLs, special characters, handle encoding issues; (2) **Normalization**—lowercase, expand contractions, normalize unicode; (3) **Tokenization**—word and sentence splitting with language-appropriate rules; (4) **Filtering**—remove stopwords (preserving negations if sentiment analysis), filter by word length; (5) **Lemmatization**—reduce words to base forms; (6) **Feature engineering**—create TF-IDF vectors, word embeddings, linguistic features. Output cleaned corpus with preprocessing statistics and quality metrics.

---

## Template

Preprocess and engineer features for {TEXT_DATA_DESCRIPTION}, preparing it for {ANALYSIS_OBJECTIVES} to support {DOWNSTREAM_APPLICATION}.

**1. Data Assessment and Cleaning Strategy**

Begin by assessing raw text characteristics to inform preprocessing decisions. Examine a sample of documents to identify noise types present—HTML tags, URLs, email addresses, social media handles, phone numbers, special characters, and encoding issues. Determine language composition and whether multilingual handling is needed. Note domain-specific elements requiring special treatment such as brand names, acronyms, technical terms, or industry jargon that should be preserved. Identify data quality issues including empty documents, duplicates, very short or very long outliers, and documents in wrong languages. Design the cleaning pipeline based on assessment findings, ordering operations to avoid artifacts (for example, expand contractions before removing punctuation).

**2. Text Cleaning and Noise Removal**

Apply systematic cleaning operations appropriate to your data source. Remove HTML tags using proper parsing rather than regex to handle nested and malformed markup. Extract or remove URLs, email addresses, and phone numbers based on whether they carry meaning for your analysis. Handle social media artifacts including @mentions, #hashtags, and RT markers—decide whether to remove entirely, extract as metadata, or normalize. Remove or normalize special characters and punctuation, being careful to preserve sentence boundaries if sentence-level analysis is needed. Normalize unicode characters to standard forms, handling accented characters, emojis, and special symbols according to analysis needs. Fix encoding issues and convert to consistent UTF-8. Remove extra whitespace, normalize line breaks, and handle tab characters.

**3. Text Normalization and Standardization**

Standardize text to reduce surface variation while preserving meaning. Convert to lowercase while optionally preserving case for named entities, acronyms, or brand names that carry semantic information. Expand contractions (don't → do not, I'm → I am) to normalize vocabulary, especially important for sentiment analysis where negations matter. Correct common misspellings if working with user-generated content, using dictionary lookup or edit distance matching. Normalize numbers to consistent format or replace with placeholder tokens depending on whether numeric values carry meaning. Handle date and time expressions consistently. Normalize repeated characters (sooooo → so) common in informal text. Apply domain-specific normalizations such as expanding abbreviations or standardizing terminology.

**4. Tokenization and Sentence Segmentation**

Split text into appropriate units for analysis. Apply word tokenization using rules appropriate to your language—English tokenization differs from languages without spaces like Chinese or Japanese. Handle edge cases including contractions, hyphenated words, and punctuation attached to words. Perform sentence segmentation if sentence-level analysis is needed, handling abbreviations (Dr., Inc., etc.) that contain periods but don't end sentences. Consider subword tokenization (BPE, WordPiece) if using transformer models that expect this format. Preserve token positions and character offsets if you need to map results back to original text. Handle multi-word expressions that should be treated as single tokens based on domain knowledge.

**5. Stopword Removal and Filtering**

Filter tokens to reduce noise while preserving signal. Remove standard stopwords (the, a, is, are) that add little semantic content, using language-appropriate stopword lists. Critically evaluate whether to preserve negation words (not, no, never, neither) which are crucial for sentiment analysis. Add domain-specific stopwords that are frequent but uninformative in your context. Remove very short tokens (single characters, two-letter words) that are often noise, with exceptions for meaningful short words. Filter very long tokens that are often errors or artifacts. Consider removing very rare words (appearing in fewer than 2-3 documents) that add vocabulary size without predictive value. Remove very frequent words (appearing in over 90-95% of documents) that don't discriminate between documents.

**6. Lemmatization and Stemming**

Reduce words to base forms to normalize vocabulary. Apply lemmatization to convert inflected forms to dictionary base forms (running → run, better → good) while preserving valid words. Use part-of-speech tagging to improve lemmatization accuracy—"saw" lemmatizes differently as noun versus verb. Consider stemming as a faster but more aggressive alternative that produces non-word stems (running → run, connection → connect). Choose between lemmatization (more accurate, preserves interpretability) and stemming (faster, more aggressive normalization) based on your use case. For topic modeling, lemmatization typically works better; for information retrieval, stemming may suffice. Apply consistently across training and inference data.

**7. Feature Engineering and Vectorization**

Transform processed text into numerical features for analysis. Create bag-of-words features counting word occurrences per document. Generate TF-IDF features that weight terms by importance—high within document but not ubiquitous across corpus. Specify appropriate parameters including maximum features (typically 5,000-20,000), n-gram range (unigrams, bigrams, trigrams), minimum document frequency, and maximum document frequency. Train or load word embeddings (Word2Vec, FastText, GloVe) to capture semantic relationships. Generate document embeddings by averaging word vectors or using dedicated document embedding models (Doc2Vec). Extract linguistic features including average word length, sentence length, vocabulary diversity (type-token ratio), readability scores (Flesch-Kincaid), and part-of-speech distributions.

**8. Quality Validation and Output Preparation**

Validate preprocessing results and prepare outputs for downstream analysis. Compare statistics before and after preprocessing—vocabulary size, average document length, token distributions. Review sample processed documents to verify cleaning didn't introduce artifacts or remove important content. Check for empty documents created by aggressive filtering and decide on handling. Validate that preprocessing is consistent and reproducible by processing the same document multiple times. Save preprocessing configuration and parameters for documentation and reproducibility. Output cleaned text corpus alongside original text for reference. Save trained vectorizers and embedding models for applying consistent transformation to new data. Generate preprocessing report with statistics, configuration, and quality metrics.

Deliver your preprocessing pipeline as:

1. **Data assessment** summarizing noise types, quality issues, and special handling requirements
2. **Cleaning configuration** specifying operations applied and their order
3. **Normalization rules** documenting case handling, contraction expansion, and standardizations
4. **Tokenization approach** with language settings and edge case handling
5. **Filtering parameters** including stopword lists and frequency thresholds
6. **Lemmatization choice** with rationale and POS tagging approach
7. **Feature matrices** including TF-IDF, embeddings, and linguistic features
8. **Quality report** with before/after statistics and sample validations

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{TEXT_DATA_DESCRIPTION}` | Source, volume, and characteristics of text | "50,000 customer reviews with HTML markup and emoji from e-commerce platform" |
| `{ANALYSIS_OBJECTIVES}` | What the preprocessing should optimize for | "sentiment classification and aspect extraction" |
| `{DOWNSTREAM_APPLICATION}` | How preprocessed data will be used | "training supervised sentiment classifier and topic model" |

---

## Usage Examples

### Example 1: E-commerce Review Preprocessing
**Prompt:** "Preprocess and engineer features for {TEXT_DATA_DESCRIPTION: 25,000 product reviews containing HTML, star ratings, and user-generated content with frequent misspellings}, preparing it for {ANALYSIS_OBJECTIVES: aspect-based sentiment analysis identifying product quality, shipping, and customer service opinions}, to support {DOWNSTREAM_APPLICATION: automated review categorization and satisfaction scoring dashboard}."

**Expected Output:** Cleaning pipeline removing HTML while preserving paragraph structure, expanding contractions with negation preservation, normalizing repeated punctuation (!!!! → !), correcting common misspellings using domain dictionary. Stopword removal keeping negations and sentiment-bearing words. TF-IDF features with bigrams capturing "not good" and "very happy" patterns. Linguistic features including exclamation density and caps usage as sentiment indicators. Quality report showing vocabulary reduced from 45,000 to 12,000 terms, average document length from 89 to 52 tokens.

### Example 2: Social Media Text Preprocessing
**Prompt:** "Preprocess and engineer features for {TEXT_DATA_DESCRIPTION: 100,000 tweets and posts containing @mentions, #hashtags, URLs, emojis, and informal language}, preparing it for {ANALYSIS_OBJECTIVES: brand sentiment tracking and trend detection}, to support {DOWNSTREAM_APPLICATION: real-time social listening dashboard with alerting}."

**Expected Output:** Cleaning pipeline extracting @mentions and #hashtags as metadata before removal from text, URL removal, emoji conversion to text descriptions or sentiment indicators. Normalization handling repeated characters (sooooo → so), all-caps words, and common abbreviations (ur → your, pls → please). Lightweight lemmatization preserving informal expressions. Word embeddings trained on social corpus to capture slang semantics. Fast processing pipeline optimized for streaming with sub-second per-document latency. Quality validation on sample showing informal language preserved appropriately.

### Example 3: Academic Literature Preprocessing
**Prompt:** "Preprocess and engineer features for {TEXT_DATA_DESCRIPTION: 5,000 research paper abstracts with technical terminology, citations, and author names}, preparing it for {ANALYSIS_OBJECTIVES: research theme discovery and citation network analysis}, to support {DOWNSTREAM_APPLICATION: systematic literature review and research gap identification}."

**Expected Output:** Cleaning preserving technical terms, acronyms, and hyphenated compound words while removing citation markers and author affiliations. Custom stopword list adding domain-frequent but uninformative terms (study, research, results, analysis). Careful lemmatization preserving technical vocabulary. TF-IDF with trigrams capturing multi-word technical concepts. Domain-specific embeddings fine-tuned on scientific text. Extraction of author names and citations as structured metadata. Quality validation ensuring technical terms not over-normalized (machine-learning kept distinct from machine and learning).

---

## Cross-References

- [text-analytics-sentiment-analysis.md](text-analytics-sentiment-analysis.md) - Sentiment and emotion analysis on preprocessed text
- [text-analytics-topic-modeling.md](text-analytics-topic-modeling.md) - Topic discovery using preprocessed corpora
- [text-analytics-entity-recognition.md](text-analytics-entity-recognition.md) - Named entity extraction from cleaned text
- [text-analytics-overview.md](text-analytics-overview.md) - Guide to selecting text analytics approaches
