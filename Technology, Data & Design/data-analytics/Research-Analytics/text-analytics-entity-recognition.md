---
category: data-analytics
last_updated: 2025-11-10
related_templates:
- data-analytics/Research-Analytics/text-analytics-preprocessing.md
- data-analytics/Research-Analytics/text-analytics-advanced-methods.md
- data-analytics/Research-Analytics/text-analytics-overview.md
tags:
- automation
- data-analytics
- ai-ml
title: Text Analytics - Named Entity Recognition
use_cases:
- Extract and classify named entities (people, organizations, locations, dates) from
  text using spaCy and transformer models.
- Link entities to knowledge bases for disambiguation and enrichment.
- Analyze entity relationships and co-occurrence patterns to understand connections
  in text data.
industries:
- finance
- healthcare
- technology
type: template
difficulty: intermediate
slug: text-analytics-entity-recognition
---

# Text Analytics - Named Entity Recognition

## Purpose
Extract, classify, and analyze named entities from text using state-of-the-art NER models including spaCy, BERT, and RoBERTa. Perform entity linking to knowledge bases, extract entity relationships, and analyze co-occurrence patterns to discover connections and insights in unstructured text data.

## Quick Entity Prompt
Extract named entities from [X] documents using spaCy and RoBERTa. Identify Person, Organization, Location, Date, Money, and Product entities. Link organizations to knowledge base, extract entity relationships (person-company, company-acquisition), analyze co-occurrence patterns, and track entity mentions over time. Provide entity frequency tables and relationship network visualization.

## Quick Start

**Example: Extract Key Entities from News Articles**

```
You are a named entity recognition expert. Extract and analyze entities from 500 business news articles to understand key players, organizations, and events.

TEXT DATA:
- Source: Business news articles (WSJ, Bloomberg, Reuters)
- Volume: 500 articles from Q1 2024
- Average length: 600 words per article
- Domain: Technology sector M&A and partnerships
- Format: JSON with fields (article_id, title, content, date, source)

NER REQUIREMENTS:
1. Extract all entities: Person, Organization, Location, Date, Money, Product
2. Use both spaCy (fast baseline) and RoBERTa (high accuracy)
3. Link organizations to knowledge base (company database)
4. Extract relationships between entities (e.g., CEO-Company, Company-Acquisition)
5. Identify co-occurring entities (which companies are mentioned together)
6. Track entity mentions over time

ENTITY TYPES OF INTEREST:
- Persons: CEOs, executives, founders, board members
- Organizations: Companies, subsidiaries, investors, competitors
- Locations: Headquarters, market regions, expansion areas
- Money: Deal values, investment amounts, market caps
- Dates: Announcement dates, closure dates, fiscal periods
- Products: Software, platforms, services mentioned

EXPECTED OUTPUT:
- Entity frequency table (top 50 entities by type)
- Entity relationship network graph
- Co-occurrence matrix for top organizations
- Timeline of key entities and events
- Linked entity information from knowledge base
- Entity mention context (example sentences)
- Insights on M&A trends and key players
```

## Template

```
You are a named entity recognition expert. Extract entities from [TEXT_DATA_SOURCE] containing [TEXT_VOLUME] to identify [ENTITY_TYPES] using [NER_METHODS].

TEXT DATA:
- Data source: [DATA_SOURCE_TYPE]
- Volume: [NUMBER_DOCUMENTS] documents
- Domain: [DOMAIN_AREA]
- Entity focus: [ENTITY_TYPES]

NAMED ENTITY RECOGNITION:

### Comprehensive Entity Extraction
```python
import spacy
from spacy import displacy
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification
import pandas as pd
from collections import defaultdict
import re

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
spacy_entities = ner_system.extract_entities_spacy([TEXT_DATA])
transformer_entities = ner_system.extract_entities_transformer([TEXT_DATA])

# Custom entity extraction
custom_patterns = {
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'phone': r'\b\d{3}-\d{3}-\d{4}\b',
    'currency': r'\$\d+(?:,\d{3})*(?:\.\d{2})?',
    'date': r'\b\d{1,2}/\d{1,2}/\d{4}\b'
}
custom_entities = ner_system.extract_custom_entities([TEXT_DATA], custom_patterns)

# Entity relationship extraction
entity_relationships = ner_system.entity_relationship_extraction([TEXT_DATA])

# Co-occurrence analysis
cooccurrence_analysis = ner_system.entity_cooccurrence_analysis([ENTITY_RESULTS])

# Entity linking (if knowledge base available)
if [KNOWLEDGE_BASE_AVAILABLE]:
    linked_entities = ner_system.entity_linking([EXTRACTED_ENTITIES], [KNOWLEDGE_BASE])
```
```

## Variables

### NER Configuration
- [NER_MODEL] - Named entity recognition model (spacy_sm/spacy_lg/bert/roberta/biobert)
- [NER_METHODS] - List of NER methods to apply
- [ENTITY_TYPES] - Types of entities to extract (PERSON/ORG/LOC/DATE/MONEY/etc.)
- [CUSTOM_ENTITY_TYPES] - Domain-specific entity types
- [ENTITY_CONFIDENCE_THRESHOLD] - Minimum confidence for entity extraction (default: 0.5)
- [AGGREGATION_STRATEGY] - Strategy for aggregating subword tokens (simple/first/average/max)

### Entity Extraction
- [EXTRACT_PERSONS] - Extract person names (True/False)
- [EXTRACT_ORGANIZATIONS] - Extract organization names (True/False)
- [EXTRACT_LOCATIONS] - Extract location names (True/False)
- [EXTRACT_DATES] - Extract date expressions (True/False)
- [EXTRACT_MONEY] - Extract monetary amounts (True/False)
- [EXTRACT_PRODUCTS] - Extract product names (True/False)
- [EXTRACT_EVENTS] - Extract event names (True/False)
- [BIOMEDICAL_ENTITIES] - Include biomedical entity types (True/False)

### Entity Linking
- [ENTITY_LINKING] - Enable entity linking to knowledge base (True/False)
- [KNOWLEDGE_BASE] - Knowledge base for entity linking
- [KNOWLEDGE_BASE_AVAILABLE] - Whether knowledge base is accessible (True/False)
- [FUZZY_MATCHING] - Use fuzzy matching for entity linking (True/False)
- [MATCHING_THRESHOLD] - Threshold for fuzzy matching (default: 0.8)
- [DISAMBIGUATION_METHOD] - Method for entity disambiguation (context/popularity/hybrid)

### Custom Entity Patterns
- [CUSTOM_ENTITY_PATTERNS] - Regex patterns for custom entity types
- [EMAIL_PATTERN] - Pattern for email addresses
- [PHONE_PATTERN] - Pattern for phone numbers
- [URL_PATTERN] - Pattern for URLs
- [CURRENCY_PATTERN] - Pattern for monetary amounts
- [DATE_PATTERN] - Pattern for date expressions
- [SOCIAL_MEDIA_PATTERN] - Pattern for social media handles

### Relationship Extraction
- [RELATION_EXTRACTION] - Extract entity relationships (True/False)
- [RELATIONSHIP_TYPES] - Types of relationships to extract (employment/ownership/location/etc.)
- [DEPENDENCY_PARSING] - Use dependency parsing for relations (True/False)
- [COREFERENCE_RESOLUTION] - Enable coreference resolution (True/False)
- [RELATIONSHIP_CONFIDENCE] - Minimum confidence for relationships (default: 0.6)

### Co-occurrence Analysis
- [COOCCURRENCE_ANALYSIS] - Analyze entity co-occurrence (True/False)
- [COOCCURRENCE_WINDOW] - Window size for co-occurrence (sentence/paragraph/document)
- [MIN_COOCCURRENCE_COUNT] - Minimum co-occurrence frequency (default: 2)
- [NETWORK_ANALYSIS] - Create entity network graph (True/False)
- [CENTRALITY_MEASURES] - Calculate network centrality (True/False)

### Entity Normalization
- [ENTITY_NORMALIZATION] - Normalize entity mentions (True/False)
- [CASE_NORMALIZATION] - Normalize case (True/False)
- [ABBREVIATION_EXPANSION] - Expand abbreviations (True/False)
- [ALIAS_RESOLUTION] - Resolve entity aliases (True/False)
- [ENTITY_CLUSTERING] - Cluster similar entities (True/False)

### Input Data Variables
- [TEXT_DATA] - Text data for entity extraction
- [TEXT_DATA_SOURCE] - Source of text data
- [NUMBER_DOCUMENTS] - Number of documents to process
- [DOMAIN_AREA] - Domain or industry area
- [DATA_SOURCE_TYPE] - Type of data source

### Output Variables
- [EXTRACTED_ENTITIES] - Extracted entities with labels and positions
- [ENTITY_COUNTS] - Frequency counts for each entity
- [ENTITY_RESULTS] - Complete NER results
- [LINKED_ENTITIES] - Entities linked to knowledge base
- [ENTITY_RELATIONSHIPS] - Extracted relationships between entities
- [COOCCURRENCE_MATRIX] - Entity co-occurrence matrix
- [TOP_ENTITIES] - Most frequent entities by type

## Usage Examples

### Example 1: News Article Entity Extraction
```
TEXT_DATA_SOURCE: "Business news articles"
NER_MODEL: "roberta_ner"
ENTITY_TYPES: ["PERSON", "ORG", "GPE", "MONEY", "DATE"]
ENTITY_CONFIDENCE_THRESHOLD: 0.7
COOCCURRENCE_ANALYSIS: True
NETWORK_ANALYSIS: True
```

### Example 2: Biomedical Text Mining
```
TEXT_DATA_SOURCE: "Clinical trial reports"
NER_MODEL: "biobert"
BIOMEDICAL_ENTITIES: True
ENTITY_TYPES: ["DISEASE", "DRUG", "GENE", "PROTEIN"]
ENTITY_LINKING: True
KNOWLEDGE_BASE: "UMLS"
```

### Example 3: Legal Document Analysis
```
TEXT_DATA_SOURCE: "Legal contracts"
NER_MODEL: "spacy_lg"
CUSTOM_ENTITY_PATTERNS: {
    "case_number": r"\d{2}-CV-\d{4,}",
    "statute": r"\d+\s+U\.S\.C\.\s+§\s+\d+",
    "monetary_penalty": r"\$[\d,]+(?:\.\d{2})?"
}
RELATION_EXTRACTION: True
DEPENDENCY_PARSING: True
```

### Example 4: Social Media Monitoring
```
TEXT_DATA_SOURCE: "Twitter posts"
NER_MODEL: "spacy_sm"
CUSTOM_ENTITY_PATTERNS: {
    "hashtag": r"#\w+",
    "mention": r"@\w+",
    "url": r"https?://\S+"
}
ENTITY_NORMALIZATION: True
COOCCURRENCE_WINDOW: "document"
```

### Example 5: Resume Parsing
```
TEXT_DATA_SOURCE: "Job candidate resumes"
NER_MODEL: "bert_ner"
ENTITY_TYPES: ["PERSON", "ORG", "GPE", "DATE"]
CUSTOM_ENTITY_PATTERNS: {
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "phone": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
    "degree": r"(B\.?S\.?|M\.?S\.?|Ph\.?D\.?|MBA)"
}
RELATION_EXTRACTION: True
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Text Analytics Preprocessing](text-analytics-preprocessing.md)** - Leverage data analysis to drive informed decisions
- **[Text Analytics Advanced Methods](text-analytics-advanced-methods.md)** - Leverage data analysis to drive informed decisions
- **[Text Analytics Overview](text-analytics-overview.md)** - Leverage data analysis to drive informed decisions

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Text Analytics - Named Entity Recognition)
2. Use [Text Analytics Preprocessing](text-analytics-preprocessing.md) for deeper analysis
3. Apply [Text Analytics Advanced Methods](text-analytics-advanced-methods.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[data-analytics/Research Analytics](../../data-analytics/Research Analytics/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Extract and classify named entities (people, organizations, locations, dates) from text using spaCy and transformer models.**: Combine this template with related analytics and strategy frameworks
- **Link entities to knowledge bases for disambiguation and enrichment.**: Combine this template with related analytics and strategy frameworks
- **Analyze entity relationships and co-occurrence patterns to understand connections in text data.**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Choose appropriate model** - Use spaCy for speed, transformers for accuracy
2. **Set confidence thresholds** - Filter low-confidence predictions to reduce noise
3. **Validate entity types** - Review extracted entities to ensure correct classification
4. **Use domain-specific models** - Apply BioBERT for biomedical, FinBERT for financial text
5. **Implement entity linking** - Connect entities to knowledge bases for disambiguation
6. **Handle entity variations** - Normalize aliases and abbreviations (IBM, International Business Machines)
7. **Extract entity context** - Keep surrounding text for interpretation
8. **Analyze relationships** - Go beyond extraction to understand entity connections
9. **Visualize entity networks** - Create graphs to show entity relationships
10. **Iterate and refine** - Add custom patterns for domain-specific entities

## Tips for Success

- spaCy models are faster and work well for standard entity types
- Transformer models provide better accuracy but require more compute
- Use custom patterns for highly structured entities (emails, phone numbers)
- Entity linking improves disambiguation for common names
- Dependency parsing helps extract subject-verb-object relationships
- Co-occurrence analysis reveals hidden connections between entities
- Normalize entities to merge variations (Apple Inc., Apple, AAPL)
- Track entity mentions over time for trend analysis
- Combine NER with sentiment analysis for entity-level opinions
- Use larger spaCy models (en_core_web_lg) for better accuracy
- Filter entities by document frequency to focus on important ones
- Create knowledge base from extracted entities for future linking
- Use coreference resolution to connect pronouns to entities
- Validate results with domain experts, especially for critical applications
