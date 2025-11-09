---
title: Topic Modeling Techniques
category: data-analytics/Research Analytics
tags: [data-analytics, machine-learning, nlp, template, text-analytics, topic-modeling]
use_cases:
  - Discovering themes and topics in document collections
  - Organizing large text corpora by topic
  - Tracking topic evolution over time
  - Understanding document similarity and clustering
related_templates:
  - text-analytics-overview.md
  - text-preprocessing.md
  - text-classification.md
  - advanced-nlp-techniques.md
last_updated: 2025-11-09
---

# Topic Modeling Techniques

## Purpose
Discover latent topics in text collections using advanced topic modeling techniques including LDA, NMF, BERTopic, and hierarchical methods to extract themes, interpret topics, and track evolution over time.

## Template

```
You are a topic modeling expert. Discover topics in [TEXT_DATA_SOURCE] to identify [TOPIC_OBJECTIVES] using [TOPIC_MODELING_METHODS] with [NUM_TOPICS] topics and focus on [TOPIC_QUALITY_METRICS].

TEXT DATA OVERVIEW:
- Data source: [DATA_SOURCE_TYPE]
- Volume: [TEXT_VOLUME] ([NUMBER_DOCUMENTS] documents)
- Domain: [DOMAIN_AREA]
- Time period: [TIME_PERIOD]

TOPIC MODELING CONFIGURATION:
- Number of topics: [NUM_TOPICS] (or auto-detect)
- Modeling method: [TOPIC_MODEL_TYPE] (LDA/NMF/BERTopic/HDP)
- Coherence threshold: [COHERENCE_THRESHOLD]
- Topic granularity: [TOPIC_GRANULARITY]
- Temporal analysis: [DYNAMIC_TOPICS]
- Hierarchical structure: [HIERARCHICAL_TOPICS]

Perform comprehensive topic discovery:

### ADVANCED TOPIC MODELING

Topic Modeling with Multiple Methods:
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
        # Create dictionary
        dictionary = corpora.Dictionary(texts)

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
        sentence_model = SentenceTransformer('all-MiniLM-L6-v2')

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

    def dynamic_topic_modeling(self, texts, timestamps, num_time_slices=5, num_topics=10):
        """Dynamic topic modeling to track topic evolution over time"""
        corpus, dictionary = self.prepare_corpus(texts)

        # Sort by timestamp
        sorted_indices = np.argsort(timestamps)
        sorted_corpus = [corpus[i] for i in sorted_indices]

        # Group documents by time slices
        docs_per_slice = len(texts) // num_time_slices
        time_slice_counts = [docs_per_slice] * num_time_slices

        # Adjust last slice to include remaining documents
        time_slice_counts[-1] += len(texts) % num_time_slices

        try:
            from gensim.models import LdaSeqModel

            dtm_model = LdaSeqModel(
                corpus=sorted_corpus,
                id2word=dictionary,
                time_slice=time_slice_counts,
                num_topics=num_topics,
                chunksize=1,
                passes=10,
                random_state=42
            )

            self.models['dtm'] = dtm_model

            # Extract topic evolution
            topic_evolution = []
            for time_point in range(num_time_slices):
                time_topics = []
                for topic_id in range(num_topics):
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
                'num_time_slices': num_time_slices,
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

    def interpret_topics(self, topic_model_results, label_method='keywords'):
        """Generate interpretable topic labels"""
        topics = topic_model_results['topics']
        labeled_topics = []

        for topic in topics:
            if label_method == 'keywords':
                # Use top 3 keywords as label
                top_words = topic['top_words'][:3]
                label = ', '.join(top_words)

            labeled_topics.append({
                **topic,
                'label': label
            })

        return labeled_topics

    def get_dominant_topics(self, doc_topic_distributions, num_docs=10):
        """Get dominant topic for each document"""
        dominant_topics = []

        for i, dist in enumerate(doc_topic_distributions):
            if dist:
                # Get topic with highest probability
                dominant_topic = max(dist, key=lambda x: x[1])
                dominant_topics.append({
                    'doc_index': i,
                    'topic_id': dominant_topic[0],
                    'probability': dominant_topic[1]
                })

        return dominant_topics

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

# Perform LDA topic modeling
lda_results = topic_modeler.lda_topic_modeling(
    [PROCESSED_TEXTS],
    num_topics=[NUM_TOPICS],
    passes=[PASSES],
    alpha=[ALPHA_PARAMETER]
)

# Perform BERTopic modeling
bert_results = topic_modeler.bert_topic_modeling(
    [TEXT_DATA],
    nr_topics=[NUM_TOPICS] if [NUM_TOPICS] != 'auto' else 'auto',
    min_topic_size=[MIN_TOPIC_SIZE]
)

# Hierarchical topic modeling
hdp_results = topic_modeler.hierarchical_topic_modeling([PROCESSED_TEXTS])

# NMF topic modeling
nmf_results = topic_modeler.nmf_topic_modeling([TEXT_DATA], num_topics=[NUM_TOPICS])

# Evaluate optimal number of topics
if [EVALUATE_NUM_TOPICS]:
    evaluation_results = topic_modeler.evaluate_topic_models([PROCESSED_TEXTS])

# Dynamic topic modeling (if timestamps available)
if [HAS_TIMESTAMPS]:
    dtm_results = topic_modeler.dynamic_topic_modeling(
        [PROCESSED_TEXTS],
        [TIMESTAMPS],
        num_time_slices=[NUM_TIME_SLICES],
        num_topics=[NUM_TOPICS]
    )
```

Topic Analysis and Visualization:
```python
def analyze_topic_quality(topic_results):
    """Analyze quality of discovered topics"""
    topics = topic_results['topics']

    quality_metrics = {
        'coherence_score': topic_results.get('coherence_score', None),
        'perplexity': topic_results.get('perplexity', None),
        'num_topics': len(topics),
        'avg_topic_diversity': calculate_topic_diversity(topics)
    }

    return quality_metrics

def calculate_topic_diversity(topics):
    """Calculate diversity of topics"""
    all_words = set()
    topic_words = []

    for topic in topics:
        words = set(topic['top_words'][:10])
        topic_words.append(words)
        all_words.update(words)

    # Calculate Jaccard distance between topics
    diversities = []
    for i in range(len(topic_words)):
        for j in range(i+1, len(topic_words)):
            intersection = len(topic_words[i] & topic_words[j])
            union = len(topic_words[i] | topic_words[j])
            diversity = 1 - (intersection / union if union > 0 else 0)
            diversities.append(diversity)

    return np.mean(diversities) if diversities else 0

def visualize_topic_distribution(doc_topic_distributions, num_topics):
    """Visualize distribution of topics across documents"""
    # Create matrix of topic proportions
    topic_matrix = np.zeros((len(doc_topic_distributions), num_topics))

    for i, dist in enumerate(doc_topic_distributions):
        for topic_id, prob in dist:
            topic_matrix[i, topic_id] = prob

    # Heatmap
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(topic_matrix.T, cmap='YlOrRd', ax=ax, cbar_kws={'label': 'Topic Probability'})
    ax.set_xlabel('Document')
    ax.set_ylabel('Topic')
    ax.set_title('Document-Topic Distribution')

    return fig

def create_topic_word_clouds(topics, max_words=50):
    """Create word clouds for each topic"""
    from wordcloud import WordCloud

    figures = []

    for topic in topics:
        # Create word frequency dict
        word_freq = {word: prob for word, prob in topic['words'][:max_words]}

        # Generate word cloud
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='viridis'
        ).generate_from_frequencies(word_freq)

        # Plot
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        ax.set_title(f"Topic {topic['topic_id']}: {', '.join(topic['top_words'][:3])}")

        figures.append(fig)

    return figures
```

OUTPUT REQUIREMENTS:
1. Discovered topics with top keywords and weights
2. Topic coherence scores and quality metrics
3. Document-topic distributions
4. Topic interpretations and labels
5. Representative documents per topic
6. Topic diversity and overlap analysis
7. Interactive visualizations (pyLDAvis, BERTopic plots)
8. Topic evolution over time (if applicable)
9. Optimal number of topics recommendation
10. Topic model comparison (if multiple methods used)
```

## Variables

### Data Configuration
- [TEXT_DATA_SOURCE] - Source of text for topic modeling
- [DATA_SOURCE_TYPE] - Type of data source
- [TEXT_VOLUME] - Volume of text to analyze
- [NUMBER_DOCUMENTS] - Total number of documents
- [DOMAIN_AREA] - Subject domain
- [TIME_PERIOD] - Time period covered

### Topic Modeling Configuration
- [TOPIC_OBJECTIVES] - Goals of topic modeling
- [TOPIC_MODELING_METHODS] - Methods to use (LDA, NMF, BERTopic, HDP)
- [NUM_TOPICS] - Number of topics (or 'auto' for automatic detection)
- [TOPIC_MODEL_TYPE] - Specific model type
- [COHERENCE_THRESHOLD] - Minimum acceptable coherence
- [TOPIC_QUALITY_METRICS] - Metrics for evaluating topics

### Model Parameters
- [PASSES] - Number of training passes (LDA)
- [ITERATIONS] - Number of iterations
- [ALPHA_PARAMETER] - Alpha parameter for LDA
- [BETA_PARAMETER] - Beta/eta parameter for LDA
- [MIN_TOPIC_SIZE] - Minimum topic size (BERTopic)
- [MIN_DF] - Minimum document frequency
- [MAX_DF] - Maximum document frequency

### Advanced Options
- [TOPIC_GRANULARITY] - Level of topic granularity
- [HIERARCHICAL_TOPICS] - Enable hierarchical modeling
- [DYNAMIC_TOPICS] - Enable temporal topic modeling
- [HAS_TIMESTAMPS] - Whether data has timestamps
- [TIMESTAMPS] - Timestamp data
- [NUM_TIME_SLICES] - Number of time periods
- [EVALUATE_NUM_TOPICS] - Evaluate optimal topic count

## Usage Examples

### Example 1: News Article Topic Discovery
```
TEXT_DATA_SOURCE: "News articles from major publications"
NUM_TOPICS: "auto"
TOPIC_MODEL_TYPE: "BERTopic"
DOMAIN_AREA: "current events"
COHERENCE_THRESHOLD: 0.5
```

### Example 2: Academic Literature Topics
```
TEXT_DATA_SOURCE: "Research paper abstracts"
NUM_TOPICS: 15
TOPIC_MODEL_TYPE: "LDA"
HIERARCHICAL_TOPICS: true
EVALUATE_NUM_TOPICS: true
```

### Example 3: Customer Feedback Topics
```
TEXT_DATA_SOURCE: "Customer support tickets"
NUM_TOPICS: 10
TOPIC_MODEL_TYPE: "NMF"
TOPIC_GRANULARITY: "fine-grained"
MIN_TOPIC_SIZE: 5
```

## Best Practices

1. **Preprocess thoroughly**: Clean text impacts topic quality significantly
2. **Evaluate multiple topic counts**: Test different numbers of topics
3. **Use coherence metrics**: Don't rely solely on perplexity
4. **Interpret topics carefully**: Validate with domain experts
5. **Consider method strengths**: LDA for probabilistic, NMF for sparse, BERTopic for semantic
6. **Remove very common/rare words**: Filter extremes in dictionary
7. **Use representative documents**: Help interpret topics
8. **Validate stability**: Run multiple times with different seeds
9. **Consider hierarchical structure**: Topics may have subtopics
10. **Track temporal changes**: Monitor how topics evolve
