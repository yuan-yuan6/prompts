---
title: Named Entity Recognition Template
category: data-analytics/Research Analytics
tags: ['nlp', 'ner', 'entity-recognition', 'information-extraction']
use_cases:
  - Extract and classify named entities including persons, organizations, locations, dates, and custom entities using spaCy, transformers, and custom NER models.
related_templates:
  - See overview file for related templates
last_updated: 2025-11-11
---

# Named Entity Recognition Template

## Purpose
Extract and classify named entities including persons, organizations, locations, dates, and custom entities using spaCy, transformers, and custom NER models.

## Quick Start

### For Data Scientists

**Step 1: Define Your Requirements**
- Review the purpose and scope of this template
- Identify your specific extract needs
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
- Extract and classify named entities including persons, organizations, locations, dates, and custom entities using spaCy, transformers, and custom NER models.
- Project-specific implementations
- Research and analysis workflows



## Template

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
