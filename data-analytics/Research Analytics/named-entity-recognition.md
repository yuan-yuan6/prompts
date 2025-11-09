---
title: Named Entity Recognition
category: data-analytics/Research Analytics
tags: [data-analytics, information-extraction, machine-learning, nlp, template, text-analytics]
use_cases:
  - Extracting people, organizations, and locations from text
  - Building knowledge graphs from unstructured text
  - Entity relationship mapping and analysis
  - Information extraction for structured databases
related_templates:
  - text-analytics-overview.md
  - text-preprocessing.md
  - text-classification.md
  - advanced-nlp-techniques.md
last_updated: 2025-11-09
---

# Named Entity Recognition

## Purpose
Extract and classify named entities (people, organizations, locations, dates, etc.) from text using multiple NER models, perform entity linking to knowledge bases, analyze relationships, and conduct co-occurrence analysis.

## Template

```
You are a named entity recognition expert. Extract entities from [TEXT_DATA_SOURCE] to identify [ENTITY_OBJECTIVES] using [NER_METHODS] with focus on [ENTITY_TYPES].

TEXT DATA OVERVIEW:
- Data source: [DATA_SOURCE_TYPE]
- Volume: [TEXT_VOLUME]
- Domain: [DOMAIN_AREA]
- Language: [LANGUAGE]

ENTITY EXTRACTION CONFIGURATION:
- Entity types: [ENTITY_TYPES] (PERSON, ORG, LOC, DATE, etc.)
- NER models: [NER_MODELS] (spaCy, BERT, domain-specific)
- Custom entities: [CUSTOM_ENTITY_PATTERNS]
- Entity linking: [ENTITY_LINKING_ENABLED]
- Confidence threshold: [CONFIDENCE_THRESHOLD]
- Relationship extraction: [EXTRACT_RELATIONSHIPS]

Perform comprehensive entity extraction and analysis:

### COMPREHENSIVE ENTITY EXTRACTION

Multi-Model Named Entity Recognition:
```python
import spacy
from spacy import displacy
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification
import pandas as pd
from collections import defaultdict
import re
import networkx as nx

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
            print(f"Error loading transformer NER models: {e}")

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
                    'confidence': 1.0  # spaCy doesn't provide confidence scores
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
                            'subject_type': subj_ents[0][1],
                            'predicate': token.head.text,
                            'object': obj_ents[0][0],
                            'object_type': obj_ents[0][1],
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

    def build_entity_network(self, ner_results, min_cooccurrence=2):
        """Build network graph of entity relationships"""
        G = nx.Graph()

        # Add nodes (entities)
        all_entities = defaultdict(int)
        for result in ner_results:
            for entity in result['entities']:
                all_entities[entity['text']] += 1

        for entity, count in all_entities.items():
            G.add_node(entity, count=count)

        # Add edges (co-occurrences)
        for result in ner_results:
            entities = [e['text'] for e in result['entities']]
            for i, entity1 in enumerate(entities):
                for entity2 in entities[i+1:]:
                    if G.has_edge(entity1, entity2):
                        G[entity1][entity2]['weight'] += 1
                    else:
                        G.add_edge(entity1, entity2, weight=1)

        # Filter edges by minimum co-occurrence
        edges_to_remove = [(u, v) for u, v, d in G.edges(data=True) if d['weight'] < min_cooccurrence]
        G.remove_edges_from(edges_to_remove)

        return G

    def entity_type_statistics(self, ner_results):
        """Calculate statistics by entity type"""
        type_stats = defaultdict(lambda: {'count': 0, 'entities': []})

        for result in ner_results:
            for entity in result['entities']:
                entity_type = entity['label']
                type_stats[entity_type]['count'] += 1
                type_stats[entity_type]['entities'].append(entity['text'])

        # Calculate unique entities per type
        for entity_type in type_stats:
            type_stats[entity_type]['unique_count'] = len(set(type_stats[entity_type]['entities']))
            type_stats[entity_type]['top_entities'] = pd.Series(
                type_stats[entity_type]['entities']
            ).value_counts().head(10).to_dict()

        return dict(type_stats)

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
spacy_entities = ner_system.extract_entities_spacy([TEXT_DATA], model_name='spacy_sm')

if [USE_TRANSFORMER_MODELS]:
    transformer_entities = ner_system.extract_entities_transformer(
        [TEXT_DATA],
        model_name='[TRANSFORMER_MODEL]'
    )

# Custom entity extraction
if [HAS_CUSTOM_PATTERNS]:
    custom_patterns = {
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phone': r'\b\d{3}-\d{3}-\d{4}\b',
        'currency': r'\$\d+(?:,\d{3})*(?:\.\d{2})?',
        'date': r'\b\d{1,2}/\d{1,2}/\d{4}\b'
    }
    custom_entities = ner_system.extract_custom_entities([TEXT_DATA], custom_patterns)

# Entity relationship extraction
if [EXTRACT_RELATIONSHIPS]:
    entity_relationships = ner_system.entity_relationship_extraction([TEXT_DATA])

# Co-occurrence analysis
cooccurrence_analysis = ner_system.entity_cooccurrence_analysis([ENTITY_RESULTS])

# Entity network
entity_network = ner_system.build_entity_network([ENTITY_RESULTS])

# Entity type statistics
type_stats = ner_system.entity_type_statistics([ENTITY_RESULTS])
```

Entity Analysis and Visualization:
```python
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

def visualize_entity_distribution(ner_results):
    """Visualize distribution of entity types"""
    all_labels = []
    for result in ner_results:
        all_labels.extend([e['label'] for e in result['entities']])

    label_counts = pd.Series(all_labels).value_counts()

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Bar chart
    label_counts.plot(kind='bar', ax=axes[0])
    axes[0].set_title('Entity Type Distribution')
    axes[0].set_xlabel('Entity Type')
    axes[0].set_ylabel('Count')
    axes[0].tick_params(axis='x', rotation=45)

    # Pie chart
    axes[1].pie(label_counts.values, labels=label_counts.index, autopct='%1.1f%%')
    axes[1].set_title('Entity Type Proportions')

    plt.tight_layout()
    return fig

def visualize_entity_network(G, top_n=30):
    """Visualize entity co-occurrence network"""
    # Get top entities by degree
    degrees = dict(G.degree())
    top_nodes = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:top_n]
    top_node_names = [node for node, degree in top_nodes]

    # Create subgraph
    subgraph = G.subgraph(top_node_names)

    # Draw network
    fig, ax = plt.subplots(figsize=(14, 10))

    pos = nx.spring_layout(subgraph, k=0.5, iterations=50)

    # Node sizes based on degree
    node_sizes = [degrees[node] * 100 for node in subgraph.nodes()]

    # Edge widths based on weight
    edge_widths = [subgraph[u][v]['weight'] * 0.5 for u, v in subgraph.edges()]

    nx.draw_networkx_nodes(subgraph, pos, node_size=node_sizes,
                          node_color='lightblue', alpha=0.7, ax=ax)
    nx.draw_networkx_edges(subgraph, pos, width=edge_widths,
                          alpha=0.5, ax=ax)
    nx.draw_networkx_labels(subgraph, pos, font_size=8, ax=ax)

    ax.set_title('Entity Co-occurrence Network')
    ax.axis('off')

    plt.tight_layout()
    return fig

def create_entity_timeline(ner_results, timestamps):
    """Create timeline of entity mentions"""
    entity_timeline = defaultdict(list)

    for result, timestamp in zip(ner_results, timestamps):
        for entity in result['entities']:
            entity_timeline[entity['text']].append(timestamp)

    return entity_timeline
```

OUTPUT REQUIREMENTS:
1. Extracted entities with types and confidence scores
2. Entity frequency and distribution statistics
3. Entity type breakdown and top entities per type
4. Entity co-occurrence matrix
5. Entity relationship graph
6. Entity network visualization
7. Linked entities (if knowledge base provided)
8. Entity timeline (if timestamps available)
9. Model comparison results (if multiple models used)
10. Custom entity extraction results
```

## Variables

### Data Configuration
- [TEXT_DATA_SOURCE] - Source of text for entity extraction
- [DATA_SOURCE_TYPE] - Type of data source
- [TEXT_VOLUME] - Volume of text to analyze
- [DOMAIN_AREA] - Domain/industry area
- [LANGUAGE] - Primary language

### Entity Extraction Configuration
- [ENTITY_OBJECTIVES] - Goals of entity extraction
- [NER_METHODS] - NER methods to use
- [ENTITY_TYPES] - Types of entities to extract
- [NER_MODELS] - Specific NER models to use
- [CUSTOM_ENTITY_PATTERNS] - Custom regex patterns

### Model Configuration
- [USE_TRANSFORMER_MODELS] - Use transformer-based models
- [TRANSFORMER_MODEL] - Specific transformer model
- [CONFIDENCE_THRESHOLD] - Minimum confidence threshold
- [ENTITY_LINKING_ENABLED] - Enable entity linking
- [KNOWLEDGE_BASE] - Knowledge base for linking

### Analysis Options
- [EXTRACT_RELATIONSHIPS] - Extract entity relationships
- [HAS_CUSTOM_PATTERNS] - Use custom entity patterns
- [MIN_COOCCURRENCE] - Minimum co-occurrence for network
- [ENTITY_RESULTS] - Results from entity extraction

### Output Options
- [TEXT_DATA] - Text data to process
- [HAS_TIMESTAMPS] - Whether data has timestamps
- [TIMESTAMPS] - Timestamp data

## Usage Examples

### Example 1: News Article Entity Extraction
```
TEXT_DATA_SOURCE: "News articles"
ENTITY_TYPES: ["PERSON", "ORG", "GPE", "DATE", "EVENT"]
NER_MODELS: ["spacy_lg", "bert_ner"]
EXTRACT_RELATIONSHIPS: true
CONFIDENCE_THRESHOLD: 0.7
```

### Example 2: Biomedical Entity Extraction
```
TEXT_DATA_SOURCE: "Medical research papers"
ENTITY_TYPES: ["DISEASE", "DRUG", "GENE", "PROTEIN"]
NER_MODELS: ["biobert"]
ENTITY_LINKING_ENABLED: true
KNOWLEDGE_BASE: "UMLS"
```

### Example 3: Business Document Analysis
```
TEXT_DATA_SOURCE: "Business contracts"
ENTITY_TYPES: ["ORG", "PERSON", "MONEY", "DATE", "LAW"]
CUSTOM_ENTITY_PATTERNS: {"contract_id": r"CNT-\d{6}"}
EXTRACT_RELATIONSHIPS: true
```

## Best Practices

1. **Use domain-specific models**: BioBERT for medical, FinBERT for financial
2. **Combine multiple models**: Ensemble improves coverage and accuracy
3. **Validate entity types**: Check extracted entities match expected types
4. **Normalize entities**: "Apple Inc." and "Apple" should be same entity
5. **Handle ambiguity**: "Apple" could be company or fruit
6. **Consider context**: Entity type may depend on surrounding text
7. **Set appropriate confidence thresholds**: Balance precision and recall
8. **Link to knowledge bases**: Disambiguate and enrich entities
9. **Track entity mentions**: Count frequency and distribution
10. **Visualize relationships**: Networks reveal connections
