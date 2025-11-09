---
title: Advanced NLP Techniques
category: data-analytics/Research Analytics
tags: [advanced-nlp, data-analytics, deep-learning, machine-learning, nlp, template, text-analytics]
use_cases:
  - Implementing word embeddings and semantic search
  - Document clustering and similarity analysis
  - Text summarization and generation
  - Using transformer models (BERT, GPT, RoBERTa)
related_templates:
  - text-analytics-overview.md
  - text-preprocessing.md
  - text-classification.md
  - topic-modeling.md
last_updated: 2025-11-09
---

# Advanced NLP Techniques

## Purpose
Apply advanced NLP methods including word embeddings, transformer models, document clustering, semantic similarity, text summarization, and state-of-the-art deep learning techniques for sophisticated text analysis.

## Template

```
You are an advanced NLP expert. Apply advanced techniques to [TEXT_DATA_SOURCE] to achieve [ADVANCED_NLP_OBJECTIVE] using [ADVANCED_METHODS] with focus on [SPECIFIC_APPLICATION].

TEXT DATA OVERVIEW:
- Data source: [DATA_SOURCE_TYPE]
- Volume: [TEXT_VOLUME]
- Domain: [DOMAIN_AREA]
- Complexity: [TEXT_COMPLEXITY]

ADVANCED NLP CONFIGURATION:
- Techniques: [ADVANCED_TECHNIQUES]
- Embedding type: [EMBEDDING_TYPE] (Word2Vec/GloVe/BERT/Sentence-BERT)
- Transformer model: [TRANSFORMER_MODEL]
- Clustering method: [CLUSTERING_METHOD]
- Similarity metric: [SIMILARITY_METRIC]
- Application: [SPECIFIC_APPLICATION]

Apply advanced NLP methods:

### ADVANCED NLP METHODS

Word Embeddings and Semantic Analysis:
```python
import numpy as np
import pandas as pd
from gensim.models import Word2Vec, Doc2Vec, FastText
from gensim.models.doc2vec import TaggedDocument
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from umap import UMAP
import matplotlib.pyplot as plt
import seaborn as sns

class AdvancedNLPAnalytics:
    def __init__(self):
        self.models = {}
        self.embeddings = {}
        self.results = {}

    def train_word2vec(self, tokenized_texts, vector_size=300, window=5, min_count=5):
        """Train Word2Vec embeddings"""
        model = Word2Vec(
            sentences=tokenized_texts,
            vector_size=vector_size,
            window=window,
            min_count=min_count,
            workers=4,
            epochs=100,
            sg=1  # Skip-gram
        )

        self.models['word2vec'] = model
        return model

    def train_doc2vec(self, texts, vector_size=300, window=5, min_count=5):
        """Train Doc2Vec embeddings"""
        # Create tagged documents
        tagged_docs = [
            TaggedDocument(words=text.split() if isinstance(text, str) else text, tags=[i])
            for i, text in enumerate(texts)
        ]

        # Train model
        model = Doc2Vec(
            documents=tagged_docs,
            vector_size=vector_size,
            window=window,
            min_count=min_count,
            workers=4,
            epochs=100,
            dm=1  # PV-DM
        )

        self.models['doc2vec'] = model

        # Get document vectors
        doc_vectors = np.array([model.dv[i] for i in range(len(texts))])
        self.embeddings['doc2vec'] = doc_vectors

        return model, doc_vectors

    def create_sentence_embeddings(self, texts, model_name='all-MiniLM-L6-v2'):
        """Create sentence embeddings using Sentence-BERT"""
        sentence_model = SentenceTransformer(model_name)
        embeddings = sentence_model.encode(texts, show_progress_bar=True)

        self.models['sentence_transformer'] = sentence_model
        self.embeddings['sentence_bert'] = embeddings

        return embeddings

    def document_clustering(self, embeddings, method='kmeans', n_clusters=5):
        """Cluster documents based on embeddings"""
        if method == 'kmeans':
            clusterer = KMeans(n_clusters=n_clusters, random_state=42)
        elif method == 'dbscan':
            clusterer = DBSCAN(eps=0.5, min_samples=5)
        elif method == 'hierarchical':
            clusterer = AgglomerativeClustering(n_clusters=n_clusters)

        cluster_labels = clusterer.fit_predict(embeddings)

        return {
            'labels': cluster_labels,
            'model': clusterer,
            'n_clusters': len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)
        }

    def semantic_similarity(self, texts, embeddings=None):
        """Calculate semantic similarity between documents"""
        if embeddings is None:
            embeddings = self.create_sentence_embeddings(texts)

        # Cosine similarity
        similarity_matrix = cosine_similarity(embeddings)

        # Find most similar pairs
        similarity_pairs = []
        n_texts = len(texts)

        for i in range(n_texts):
            for j in range(i+1, n_texts):
                similarity_pairs.append({
                    'text1_index': i,
                    'text2_index': j,
                    'similarity': similarity_matrix[i][j],
                    'text1_preview': texts[i][:100],
                    'text2_preview': texts[j][:100]
                })

        # Sort by similarity
        similarity_pairs.sort(key=lambda x: x['similarity'], reverse=True)

        return {
            'similarity_matrix': similarity_matrix,
            'top_similar_pairs': similarity_pairs[:20],
            'least_similar_pairs': similarity_pairs[-20:]
        }

    def semantic_search(self, query, documents, top_k=10):
        """Perform semantic search using embeddings"""
        if 'sentence_transformer' not in self.models:
            model = SentenceTransformer('all-MiniLM-L6-v2')
            self.models['sentence_transformer'] = model
        else:
            model = self.models['sentence_transformer']

        # Encode query and documents
        query_embedding = model.encode([query])

        if 'sentence_bert' in self.embeddings:
            doc_embeddings = self.embeddings['sentence_bert']
        else:
            doc_embeddings = model.encode(documents)
            self.embeddings['sentence_bert'] = doc_embeddings

        # Calculate similarities
        similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

        # Get top results
        top_indices = similarities.argsort()[-top_k:][::-1]

        results = []
        for idx in top_indices:
            results.append({
                'document': documents[idx],
                'similarity': similarities[idx],
                'rank': len(results) + 1
            })

        return results

    def extractive_summarization(self, texts, summary_ratio=0.3):
        """Generate extractive summaries"""
        from nltk.tokenize import sent_tokenize
        from sklearn.feature_extraction.text import TfidfVectorizer

        summaries = []

        for text in texts:
            sentences = sent_tokenize(text)
            if len(sentences) <= 3:
                summaries.append(text)
                continue

            # Create TF-IDF vectors for sentences
            vectorizer = TfidfVectorizer(stop_words='english')
            sentence_vectors = vectorizer.fit_transform(sentences)

            # Calculate sentence scores
            sentence_scores = sentence_vectors.sum(axis=1).A1

            # Select top sentences
            num_sentences = max(1, int(len(sentences) * summary_ratio))
            top_indices = sentence_scores.argsort()[-num_sentences:][::-1]
            top_indices.sort()  # Maintain original order

            summary_sentences = [sentences[i] for i in top_indices]
            summary = ' '.join(summary_sentences)

            summaries.append(summary)

        return summaries

    def abstractive_summarization(self, texts, max_length=150, min_length=30):
        """Generate abstractive summaries using transformers"""
        try:
            from transformers import pipeline

            summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
            summaries = []

            for text in texts:
                # Truncate if too long
                if len(text) > 1024:
                    text = text[:1024]

                summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
                summaries.append(summary[0]['summary_text'])

            return summaries

        except Exception as e:
            print(f"Abstractive summarization failed: {e}")
            return self.extractive_summarization(texts)

    def readability_analysis(self, texts):
        """Analyze text readability using multiple metrics"""
        from textstat import (
            flesch_reading_ease, flesch_kincaid_grade,
            automated_readability_index, coleman_liau_index
        )
        from nltk.tokenize import sent_tokenize

        readability_scores = []

        for text in texts:
            scores = {
                'flesch_reading_ease': flesch_reading_ease(text),
                'flesch_kincaid_grade': flesch_kincaid_grade(text),
                'automated_readability_index': automated_readability_index(text),
                'coleman_liau_index': coleman_liau_index(text),
                'word_count': len(text.split()),
                'sentence_count': len(sent_tokenize(text)),
                'avg_sentence_length': len(text.split()) / len(sent_tokenize(text)) if len(sent_tokenize(text)) > 0 else 0
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

    def dimensionality_reduction(self, embeddings, method='tsne', n_components=2):
        """Reduce dimensionality for visualization"""
        if method == 'tsne':
            reducer = TSNE(n_components=n_components, random_state=42, perplexity=min(30, len(embeddings)-1))
        elif method == 'pca':
            reducer = PCA(n_components=n_components, random_state=42)
        elif method == 'umap':
            reducer = UMAP(n_components=n_components, random_state=42)

        reduced_embeddings = reducer.fit_transform(embeddings)
        return reduced_embeddings

    def keyword_extraction(self, texts, method='tfidf', top_k=20):
        """Extract keywords using various methods"""
        from sklearn.feature_extraction.text import TfidfVectorizer

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
                'keywords': keyword_scores[:top_k]
            }

        elif method == 'keybert':
            try:
                from keybert import KeyBERT

                kw_model = KeyBERT()
                all_keywords = []

                for text in texts:
                    keywords = kw_model.extract_keywords(text, top_n=top_k)
                    all_keywords.extend(keywords)

                # Aggregate and sort
                keyword_dict = {}
                for kw, score in all_keywords:
                    keyword_dict[kw] = keyword_dict.get(kw, 0) + score

                sorted_keywords = sorted(keyword_dict.items(), key=lambda x: x[1], reverse=True)

                return {
                    'method': 'keybert',
                    'keywords': sorted_keywords[:top_k]
                }

            except Exception as e:
                print(f"KeyBERT failed: {e}")
                return self.keyword_extraction(texts, method='tfidf', top_k=top_k)

    def transformer_text_classification(self, texts, labels=None, model_name='distilbert-base-uncased'):
        """Use transformer models for classification"""
        from transformers import pipeline

        if labels is None:
            # Zero-shot classification
            classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')
            candidate_labels = ["positive", "negative", "neutral"]

            results = []
            for text in texts:
                result = classifier(text, candidate_labels)
                results.append(result)

            return results

        else:
            # Fine-tuning would go here
            pass

    def question_answering(self, context, questions):
        """Answer questions using transformer QA models"""
        from transformers import pipeline

        qa_pipeline = pipeline('question-answering', model='distilbert-base-cased-distilled-squad')

        answers = []
        for question in questions:
            result = qa_pipeline(question=question, context=context)
            answers.append({
                'question': question,
                'answer': result['answer'],
                'confidence': result['score'],
                'start': result['start'],
                'end': result['end']
            })

        return answers

# Initialize advanced NLP analytics
advanced_nlp = AdvancedNLPAnalytics()

# Create embeddings
if '[EMBEDDING_TYPE]' == 'sentence-bert':
    embeddings = advanced_nlp.create_sentence_embeddings([TEXT_DATA])
elif '[EMBEDDING_TYPE]' == 'doc2vec':
    model, embeddings = advanced_nlp.train_doc2vec([TEXT_DATA])

# Document clustering
if [PERFORM_CLUSTERING]:
    clustering_results = advanced_nlp.document_clustering(
        embeddings,
        method='[CLUSTERING_METHOD]',
        n_clusters=[NUM_CLUSTERS]
    )

# Semantic similarity
similarity_results = advanced_nlp.semantic_similarity([TEXT_DATA], embeddings)

# Semantic search
if [HAS_QUERY]:
    search_results = advanced_nlp.semantic_search([QUERY], [TEXT_DATA], top_k=[TOP_K])

# Text summarization
if [GENERATE_SUMMARIES]:
    if '[SUMMARIZATION_TYPE]' == 'extractive':
        summaries = advanced_nlp.extractive_summarization([TEXT_DATA])
    else:
        summaries = advanced_nlp.abstractive_summarization([TEXT_DATA])

# Readability analysis
readability_scores = advanced_nlp.readability_analysis([TEXT_DATA])

# Keyword extraction
keywords = advanced_nlp.keyword_extraction([TEXT_DATA], method='[KEYWORD_METHOD]')
```

Visualization:
```python
def visualize_embeddings(embeddings, labels=None, method='tsne'):
    """Visualize document embeddings in 2D"""
    from advanced_nlp import dimensionality_reduction

    # Reduce to 2D
    if method == 'tsne':
        reducer = TSNE(n_components=2, random_state=42)
    elif method == 'pca':
        reducer = PCA(n_components=2)
    elif method == 'umap':
        reducer = UMAP(n_components=2, random_state=42)

    reduced = reducer.fit_transform(embeddings)

    # Plot
    fig, ax = plt.subplots(figsize=(12, 8))

    if labels is not None:
        scatter = ax.scatter(reduced[:, 0], reduced[:, 1], c=labels, cmap='viridis', alpha=0.6)
        plt.colorbar(scatter)
    else:
        ax.scatter(reduced[:, 0], reduced[:, 1], alpha=0.6)

    ax.set_title(f'Document Embeddings ({method.upper()})')
    ax.set_xlabel('Component 1')
    ax.set_ylabel('Component 2')

    plt.tight_layout()
    return fig

def plot_similarity_heatmap(similarity_matrix, labels=None):
    """Plot similarity heatmap"""
    fig, ax = plt.subplots(figsize=(10, 8))

    sns.heatmap(similarity_matrix, cmap='YlOrRd', ax=ax,
                xticklabels=labels if labels else False,
                yticklabels=labels if labels else False)

    ax.set_title('Document Similarity Matrix')
    plt.tight_layout()
    return fig

def create_word_cloud_from_embeddings(model, max_words=100):
    """Create word cloud from word embeddings"""
    from wordcloud import WordCloud

    if hasattr(model, 'wv'):
        vocab = list(model.wv.index_to_key)[:max_words]
        word_freq = {word: model.wv.get_vecattr(word, "count") for word in vocab}

        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            colormap='viridis'
        ).generate_from_frequencies(word_freq)

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        ax.set_title('Word Embedding Vocabulary')

        plt.tight_layout()
        return fig

    return None
```

OUTPUT REQUIREMENTS:
1. Document embeddings (Word2Vec, Doc2Vec, or Sentence-BERT)
2. Clustering results with cluster assignments
3. Similarity matrix and top similar document pairs
4. Semantic search results (if applicable)
5. Text summaries (extractive or abstractive)
6. Readability scores and analysis
7. Keyword extraction results
8. Dimensionality reduction visualizations
9. Model performance metrics
10. Recommendations for applications
```

## Variables

### Data Configuration
- [TEXT_DATA_SOURCE] - Source of text for analysis
- [DATA_SOURCE_TYPE] - Type of data source
- [TEXT_VOLUME] - Volume of text
- [DOMAIN_AREA] - Domain/industry area
- [TEXT_COMPLEXITY] - Complexity level of text

### Advanced NLP Configuration
- [ADVANCED_NLP_OBJECTIVE] - Primary objective
- [ADVANCED_METHODS] - Methods to apply
- [ADVANCED_TECHNIQUES] - Specific techniques
- [SPECIFIC_APPLICATION] - Application type

### Embedding Configuration
- [EMBEDDING_TYPE] - Type of embeddings (Word2Vec/Doc2Vec/BERT)
- [TRANSFORMER_MODEL] - Transformer model name
- [VECTOR_SIZE] - Embedding dimension
- [WINDOW_SIZE] - Context window size

### Clustering & Similarity
- [CLUSTERING_METHOD] - Clustering algorithm
- [SIMILARITY_METRIC] - Similarity metric
- [NUM_CLUSTERS] - Number of clusters
- [PERFORM_CLUSTERING] - Perform clustering

### Application-Specific
- [HAS_QUERY] - Has search query
- [QUERY] - Search query
- [TOP_K] - Top K results
- [GENERATE_SUMMARIES] - Generate summaries
- [SUMMARIZATION_TYPE] - Type of summarization
- [KEYWORD_METHOD] - Keyword extraction method
- [TEXT_DATA] - Text data to process

## Usage Examples

### Example 1: Semantic Document Search
```
EMBEDDING_TYPE: "sentence-bert"
SPECIFIC_APPLICATION: "semantic search engine"
HAS_QUERY: true
TOP_K: 10
SIMILARITY_METRIC: "cosine"
```

### Example 2: Document Clustering
```
EMBEDDING_TYPE: "doc2vec"
CLUSTERING_METHOD: "kmeans"
NUM_CLUSTERS: 8
PERFORM_CLUSTERING: true
DIMENSIONALITY_REDUCTION: "umap"
```

### Example 3: Automatic Summarization
```
GENERATE_SUMMARIES: true
SUMMARIZATION_TYPE: "abstractive"
TRANSFORMER_MODEL: "facebook/bart-large-cnn"
KEYWORD_METHOD: "keybert"
```

## Best Practices

1. **Choose appropriate embeddings**: Sentence-BERT for semantic search, Word2Vec for word-level
2. **Optimize embedding dimension**: Balance between quality and computational cost
3. **Use pre-trained models**: Leverage transfer learning when possible
4. **Validate clusters**: Check if clusters are meaningful
5. **Consider context**: Embeddings capture context better than traditional methods
6. **Test similarity metrics**: Cosine vs Euclidean for different applications
7. **Fine-tune transformers**: Adapt pre-trained models to your domain
8. **Monitor computational cost**: Transformers are resource-intensive
9. **Validate summaries**: Check if summaries preserve key information
10. **Combine methods**: Use multiple techniques for robust results
