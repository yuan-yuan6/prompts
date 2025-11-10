# Prompt Splitting Plan - Extremely Long Prompts (2,000+ lines)

## Overview

This document details the splitting strategy for 7 extremely long prompts that exceed 2,000 lines.

**Total Impact:**
- 7 monolithic prompts → 34 focused sub-prompts + 7 overview/navigation files
- Average reduction: 2,229 lines → 450-700 lines per sub-prompt
- Improved usability, faster loading, better focus

---

## 1. research-design.md (2,509 lines)

**Location:** `education/Academic Research/`

**Split into 5 sub-prompts:**

1. **research-design-foundation.md** (550-650 lines)
   - Research foundations, theoretical frameworks, methodology selection
   - Focus: "Why and how" - conceptual backbone

2. **research-design-sampling-data.md** (500-600 lines)
   - Sampling strategies, participant recruitment, data collection methods
   - Focus: "Who and what" - operational planning

3. **research-design-analysis-quality.md** (550-650 lines)
   - Analytical methods (quant/qual/mixed) + quality assurance/validity
   - Focus: Rigorous analysis planning with built-in quality

4. **research-design-ethics-implementation.md** (650-750 lines)
   - Ethical compliance, project management, risk mitigation
   - Focus: Making research happen responsibly

5. **research-design-impact.md** (600-700 lines)
   - Dissemination, knowledge translation, innovation, evaluation
   - Focus: Maximizing research impact and sustainability

**Overview file:** `research-design-overview.md`

---

## 2. network-analysis.md (2,293 lines)

**Location:** `data-analytics/Research Analytics/`

**Split into 4 sub-prompts:**

1. **network-analysis-data-preparation.md** (450 lines)
   - Data loading, preprocessing, cleaning, quality validation
   - Focus: Getting network data ready for analysis

2. **network-analysis-centrality-community.md** (600 lines)
   - Centrality analysis + community detection
   - Focus: Important nodes and cohesive groups

3. **network-analysis-paths-temporal.md** (650 lines)
   - Path analysis, connectivity, robustness, temporal evolution
   - Focus: Network dynamics and information flow

4. **network-analysis-visualization.md** (750 lines)
   - Visualization, reports, variables, examples, best practices
   - Focus: Presentation and comprehensive reference

**Overview file:** `network-analysis-overview.md`

---

## 3. text-analytics.md (2,260 lines)

**Location:** `data-analytics/Research Analytics/`

**Split into 5 sub-prompts:**

1. **text-analytics-preprocessing.md** (550-600 lines)
   - Text cleaning, preprocessing, feature engineering
   - Focus: Foundation for all NLP tasks

2. **text-analytics-sentiment-analysis.md** (450-500 lines)
   - VADER, TextBlob, transformers, aspect-based sentiment, emotion
   - Focus: Comprehensive sentiment toolkit

3. **text-analytics-topic-modeling.md** (550-600 lines)
   - LDA, BERTopic, NMF, HDP, dynamic topics
   - Focus: Topic discovery and evaluation

4. **text-analytics-entity-recognition.md** (500-550 lines)
   - NER, entity linking, relationship extraction
   - Focus: Knowledge extraction

5. **text-analytics-advanced-methods.md** (700-750 lines)
   - Clustering, similarity, summarization, reporting, visualization
   - Focus: Advanced analytics with full reporting suite

**Overview file:** `text-analytics-overview.md`

---

## 4. literature-reviews.md (2,232 lines)

**Location:** `education/Academic Research/`

**Split into 5 sub-prompts:**

1. **literature-review-protocol-search.md** (550-650 lines)
   - Protocol development, search strategy design
   - Focus: Critical planning phase

2. **literature-review-selection-quality.md** (500-600 lines)
   - Study screening, selection, quality assessment
   - Focus: Systematic selection and bias evaluation

3. **literature-review-extraction-synthesis.md** (600-700 lines)
   - Data extraction, thematic analysis, evidence synthesis
   - Focus: Analytical heart of literature reviews

4. **literature-review-analysis-implications.md** (650-750 lines)
   - Critical evaluation, theoretical contributions, practical implications
   - Focus: Interpretation and actionable insights

5. **literature-review-reporting-dissemination.md** (650-750 lines)
   - Manuscript preparation, stakeholder engagement, knowledge translation
   - Focus: Communication and real-world impact

**Overview file:** `literature-reviews-overview.md`

---

## 5. pipeline-development.md (2,167 lines)

**Location:** `data-analytics/Analytics Engineering/`

**Split into 5 sub-prompts:**

1. **pipeline-ingestion.md** (550-600 lines)
   - Batch, streaming, CDC ingestion patterns
   - Focus: Data extraction layer

2. **pipeline-transformation.md** (500-550 lines)
   - Medallion architecture (Bronze → Silver → Gold), data quality
   - Focus: Business logic and transformation

3. **pipeline-orchestration.md** (450-500 lines)
   - Airflow DAGs, workflow patterns, task dependencies
   - Focus: Workflow automation

4. **pipeline-observability.md** (650-700 lines)
   - Monitoring, alerting, error handling, recovery
   - Focus: Operational excellence

5. **pipeline-infrastructure.md** (600-650 lines)
   - IaC, containerization, performance optimization, scaling
   - Focus: Deployment and infrastructure

**Overview file:** `pipeline-development-overview.md`

---

## 6. query-optimization.md (2,076 lines)

**Location:** `data-analytics/Analytics Engineering/`

**Split into 5 sub-prompts:**

1. **query-optimization-baseline-analysis.md** (400-450 lines)
   - Performance baseline, query profiling, diagnostics
   - Focus: Initial performance assessment

2. **query-optimization-indexing-strategies.md** (450-500 lines)
   - Index design, analysis, maintenance
   - Focus: Complete indexing guide

3. **query-optimization-query-rewriting.md** (400-450 lines)
   - SQL optimization techniques, execution plan improvements
   - Focus: Application-level optimization

4. **query-optimization-monitoring-tuning.md** (550-600 lines)
   - Real-time monitoring, alerting, automated tuning
   - Focus: Ongoing performance management

5. **query-optimization-resource-concurrency.md** (750-800 lines)
   - Memory, storage, concurrency optimization
   - Focus: Infrastructure and resource management

**Overview file:** `query-optimization-overview.md`

---

## 7. experimental-design.md (2,065 lines)

**Location:** `data-analytics/Research Analytics/`

**Split into 5 sub-prompts:**

1. **experimental-design-setup.md** (440 lines)
   - 8 design types (RCT, A/B testing, factorial, etc.)
   - Focus: Selecting and configuring experiment structure

2. **randomization-and-power-analysis.md** (512 lines)
   - Randomization methods + power/sample size calculations
   - Focus: Pre-experiment planning

3. **treatment-effect-analysis.md** (372 lines)
   - Causal inference, treatment effect estimation
   - Focus: Core statistical analysis

4. **validity-and-diagnostics.md** (408 lines)
   - Experimental validity assessment, diagnostic checks
   - Focus: Quality assurance

5. **variables-and-implementation.md** (334 lines)
   - Complete reference: 400+ variables, examples, best practices
   - Focus: Implementation guide and reference

**Overview file:** `experimental-design-overview.md`

---

## Implementation Strategy

### Phase 1: Create Sub-Prompts (Parallel)
- Split each original file into focused sub-prompts
- Each sub-prompt includes:
  - Relevant frontmatter and metadata
  - Quick Start section
  - Focused content from original
  - Relevant variables
  - Domain-specific examples
  - Best practices

### Phase 2: Create Overview Files
- Navigation pages linking to all sub-prompts
- Decision trees for selecting appropriate sub-prompt
- Workflow guidance
- Integration patterns

### Phase 3: Archive Originals
- Move original monolithic files to `.archive/` or similar
- Update any references in other files
- Commit with clear messages

### Phase 4: Verification
- Ensure all sub-prompts have Quick Start sections
- Verify all content from originals is preserved
- Test navigation from overview files

---

## Benefits

1. **Faster Loading**: 400-700 line files vs 2,000+ line files
2. **Better Focus**: Users get exactly what they need
3. **Easier Maintenance**: Smaller, focused files
4. **Improved Discovery**: Overview files help navigation
5. **Reduced Cognitive Load**: Less overwhelming for users
6. **Better Version Control**: Smaller diffs, clearer changes

---

## Success Metrics

- ✓ 7 monolithic files split into 34 focused sub-prompts
- ✓ 7 overview/navigation files created
- ✓ All sub-prompts have Quick Start sections
- ✓ No content loss from original files
- ✓ Clear navigation and integration guidance
