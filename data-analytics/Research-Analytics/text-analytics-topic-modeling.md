---
category: data-analytics/Research-Analytics
last_updated: 2025-11-10
related_templates:
- data-analytics/Research-Analytics/text-analytics-preprocessing.md
- data-analytics/Research-Analytics/text-analytics-sentiment-analysis.md
- data-analytics/Research-Analytics/text-analytics-overview.md
tags:
- automation
- data-analytics
- data-science
- machine-learning
- nlp
- topic-modeling
- lda
- bertopic
- template
title: Text Analytics - Topic Modeling
use_cases:
- Discover latent topics in large document collections using LDA, NMF, HDP, and BERTopic
  algorithms.
- Track topic evolution over time to understand how themes change in dynamic datasets.
- Evaluate and compare topic models to select the optimal number of topics for interpretability.
---

# Text Analytics - Topic Modeling

## Purpose
Discover and analyze latent topics in document collections using state-of-the-art topic modeling algorithms including LDA, BERTopic, NMF, and Hierarchical Dirichlet Process. Extract interpretable topics, track topic evolution over time, evaluate model quality, and generate interactive visualizations for topic exploration.

## Quick Start

**Example: Discover Research Themes in Academic Papers**

```
You are a topic modeling expert. Analyze 2,000 research paper abstracts to identify main research themes and their evolution over 5 years.

TEXT DATA:
- Source: PubMed abstracts (biomedical research)
- Volume: 2,000 abstracts (2019-2024)
- Average length: 250 words per abstract
- Domain: Cancer immunotherapy research
- Format: CSV with fields (pmid, title, abstract, year, journal)

TOPIC MODELING REQUIREMENTS:
1. Use LDA to extract 10-12 interpretable topics
2. Apply BERTopic for comparison and validation
3. Evaluate topic coherence (target: >0.4)
4. Track topic evolution across the 5-year period
5. Identify emerging vs declining research themes
6. Extract representative papers for each topic

EVALUATION CRITERIA:
- Topic coherence score > 0.4
- Distinct and interpretable topic labels
- Minimal topic overlap
- Good coverage of document collection

EXPECTED OUTPUT:
- 10-12 topics with top 20 keywords each
- Topic coherence scores and perplexity metrics
- Representative abstracts for each topic (5 examples)
- Topic evolution heatmap showing trends
- Interactive pyLDAvis visualization
- Topic labels based on content analysis
- Research recommendations for emerging themes
```

## Template

```
You are a topic modeling expert. Discover topics in [TEXT_DATA_SOURCE] containing [TEXT_VOLUME] to understand [ANALYSIS_OBJECTIVE] using [TOPIC_MODELING_METHODS].

TEXT DATA:
- Data source: [DATA_SOURCE_TYPE]
- Volume: [NUMBER_DOCUMENTS] documents
- Domain: [DOMAIN_AREA]
- Time period: [TIME_PERIOD]

TOPIC MODELING:

### Advanced Topic Discovery
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
import pandas as pd
import numpy as np

class TopicModeler:
    def __init__(self):
        self.models = {}
        self.dictionaries = {}
        self.corpora = {}

    def prepare_corpus(self, texts, min_df=2, max_df=0.95):
        """Prepare corpus for topic modeling"""
        from gensim.corpora import Dictionary

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
            print(f"Dynamic topic modeling failed: {e}")
            return None

    def evaluate_topic_models(self, texts, topic_ranges=range(2, 21)):
        """Evaluate topic models across different numbers of topics"""
        corpus, dictionary = self.prepare_corpus(texts)

        evaluation_results = []

        for num_topics in topic_ranges:
            print(f"Evaluating {num_topics} topics...")

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

# Create visualizations
lda_visualization = topic_modeler.visualize_topics('lda')
```
```

## Variables

### Topic Modeling Configuration
- [NUM_TOPICS] - Number of topics to extract (default: 10)
- [TOPIC_MODEL_TYPE] - Type of topic model (lda/bertopic/nmf/hdp)
- [TOPIC_MODELING_METHODS] - List of methods to apply
- [MIN_TOPIC_SIZE] - Minimum documents per topic for BERTopic (default: 10)
- [AUTO_TOPIC_SELECTION] - Automatically determine optimal number of topics (True/False)
- [HIERARCHICAL_TOPICS] - Enable hierarchical topic modeling (True/False)

### LDA Parameters
- [ALPHA_PARAMETER] - Alpha parameter for LDA (document-topic density, default: 'auto')
- [BETA_PARAMETER] - Beta/eta parameter for LDA (topic-word density, default: 'auto')
- [PASSES] - Number of passes through corpus (default: 20)
- [ITERATIONS] - Number of iterations for training (default: 400)
- [CHUNKSIZE] - Number of documents in each batch (default: 100)
- [UPDATE_EVERY] - Update model every N chunks (default: 1)

### Evaluation Metrics
- [COHERENCE_MEASURE] - Coherence measure type (c_v/u_mass/c_uci/c_npmi)
- [TOPIC_COHERENCE_THRESHOLD] - Minimum acceptable coherence (default: 0.4)
- [PERPLEXITY_CALCULATION] - Calculate perplexity score (True/False)
- [TOPIC_DIVERSITY] - Measure topic diversity (True/False)
- [TOPIC_OVERLAP_THRESHOLD] - Maximum acceptable topic overlap (default: 0.3)

### BERTopic Configuration
- [SENTENCE_MODEL] - Sentence transformer model (default: 'all-MiniLM-L6-v2')
- [UMAP_NEIGHBORS] - Number of neighbors for UMAP (default: 15)
- [UMAP_COMPONENTS] - Number of UMAP components (default: 5)
- [HDBSCAN_MIN_CLUSTER_SIZE] - Minimum cluster size for HDBSCAN (default: 10)
- [VECTORIZER_MODEL] - Vectorizer for BERTopic (CountVectorizer/TfidfVectorizer)

### Corpus Preparation
- [MIN_DOCUMENT_FREQUENCY] - Minimum documents containing term (default: 2)
- [MAX_DOCUMENT_FREQUENCY] - Maximum proportion of documents (default: 0.95)
- [MAX_VOCABULARY_SIZE] - Maximum vocabulary size (default: no limit)
- [NGRAM_RANGE] - N-gram range for topic words (default: (1, 2))
- [FILTER_EXTREMES] - Filter very common/rare words (True/False)

### Temporal Analysis
- [TIMESTAMPS] - Document timestamps for temporal analysis
- [TIME_SLICES] - Time periods for dynamic topic modeling
- [TEMPORAL_ANALYSIS] - Enable temporal topic tracking (True/False)
- [TOPIC_EVOLUTION_TRACKING] - Track how topics evolve (True/False)
- [TREND_DETECTION] - Detect emerging and declining topics (True/False)

### Input Data Variables
- [TEXT_DATA] - Raw text data for topic modeling
- [PROCESSED_TEXTS] - Preprocessed and tokenized texts
- [TEXT_DATA_SOURCE] - Source of text documents
- [NUMBER_DOCUMENTS] - Total number of documents
- [DOMAIN_AREA] - Subject domain of documents
- [TIME_PERIOD] - Time period covered by documents

### Output Variables
- [TOPICS] - Discovered topics with keywords
- [TOPIC_LABELS] - Human-readable topic labels
- [DOCUMENT_TOPICS] - Topic assignments for documents
- [TOPIC_COHERENCE] - Coherence scores for topics
- [TOPIC_PERPLEXITY] - Model perplexity score
- [REPRESENTATIVE_DOCUMENTS] - Example documents per topic
- [TOPIC_DISTRIBUTION] - Distribution of topics in corpus
- [TOPIC_KEYWORDS] - Top keywords for each topic

## Usage Examples

### Example 1: Academic Literature Analysis
```
TEXT_DATA_SOURCE: "Research paper abstracts from PubMed"
TOPIC_MODEL_TYPE: "lda"
NUM_TOPICS: 15
COHERENCE_MEASURE: "c_v"
TOPIC_COHERENCE_THRESHOLD: 0.45
PASSES: 30
ALPHA_PARAMETER: "auto"
MIN_DOCUMENT_FREQUENCY: 5
```

### Example 2: Customer Feedback Topic Discovery
```
TEXT_DATA_SOURCE: "Customer support tickets"
TOPIC_MODEL_TYPE: "bertopic"
MIN_TOPIC_SIZE: 15
AUTO_TOPIC_SELECTION: True
SENTENCE_MODEL: "all-MiniLM-L6-v2"
HDBSCAN_MIN_CLUSTER_SIZE: 20
```

### Example 3: News Article Clustering
```
TEXT_DATA_SOURCE: "News articles"
TOPIC_MODEL_TYPE: "lda"
NUM_TOPICS: 20
TEMPORAL_ANALYSIS: True
TIME_SLICES: ["2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06"]
TOPIC_EVOLUTION_TRACKING: True
```

### Example 4: Social Media Theme Analysis
```
TEXT_DATA_SOURCE: "Twitter posts about brand"
TOPIC_MODEL_TYPE: "nmf"
NUM_TOPICS: 12
NGRAM_RANGE: (1, 2)
MIN_DOCUMENT_FREQUENCY: 10
MAX_DOCUMENT_FREQUENCY: 0.8
```

### Example 5: Legal Document Classification
```
TEXT_DATA_SOURCE: "Legal case documents"
TOPIC_MODEL_TYPE: "hdp"
HIERARCHICAL_TOPICS: True
MIN_DOCUMENT_FREQUENCY: 3
COHERENCE_MEASURE: "c_v"
AUTO_TOPIC_SELECTION: True
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Text Analytics Preprocessing](text-analytics-preprocessing.md)** - Leverage data analysis to drive informed decisions
- **[Text Analytics Sentiment Analysis](text-analytics-sentiment-analysis.md)** - Leverage data analysis to drive informed decisions
- **[Text Analytics Overview](text-analytics-overview.md)** - Leverage data analysis to drive informed decisions

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Text Analytics - Topic Modeling)
2. Use [Text Analytics Preprocessing](text-analytics-preprocessing.md) for deeper analysis
3. Apply [Text Analytics Sentiment Analysis](text-analytics-sentiment-analysis.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Research Analytics](../../data-analytics/Research Analytics/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Discover latent topics in large document collections using LDA, NMF, HDP, and BERTopic algorithms.**: Combine this template with related analytics and strategy frameworks
- **Track topic evolution over time to understand how themes change in dynamic datasets.**: Combine this template with related analytics and strategy frameworks
- **Evaluate and compare topic models to select the optimal number of topics for interpretability.**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Preprocess text appropriately** - Remove noise but keep domain-relevant terms
2. **Start with model evaluation** - Test different numbers of topics before committing
3. **Use coherence scores** - Aim for coherence > 0.4 for interpretable topics
4. **Examine representative documents** - Validate topics with actual document examples
5. **Compare multiple algorithms** - LDA, NMF, and BERTopic have different strengths
6. **Filter extreme terms** - Remove very common and very rare words
7. **Tune hyperparameters** - Adjust alpha, beta, and passes for optimal results
8. **Label topics meaningfully** - Create human-readable labels based on top words
9. **Consider topic hierarchy** - Use HDP for unknown number of topics
10. **Visualize results** - Use pyLDAvis and interactive plots for exploration

## Tips for Success

- Start with 5-15 topics for initial exploration
- Use BERTopic for short texts and diverse domains
- Use LDA for longer documents and established domains
- Increase passes and iterations for more stable topics
- Filter stopwords and domain-specific common terms
- Use bigrams and trigrams to capture multi-word concepts
- Validate topics with domain experts
- Monitor coherence and perplexity during training
- Save models for reproducibility and future use
- Create topic labels by examining top words and documents
- Track topic distribution across document subsets
- Use dynamic topic modeling for temporal datasets
- Consider computational resources (BERTopic is slower but more accurate)
- Iterate and refine based on interpretability
