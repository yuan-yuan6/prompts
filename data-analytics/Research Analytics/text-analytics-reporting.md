---
title: Text Analytics Reporting and Visualization
category: data-analytics/Research Analytics
tags: [data-analytics, data-visualization, nlp, reporting, template, text-analytics]
use_cases:
  - Creating comprehensive text analytics reports
  - Building interactive dashboards for NLP insights
  - Visualizing sentiment, topics, and entity analysis
  - Communicating text analytics findings to stakeholders
related_templates:
  - text-analytics-overview.md
  - sentiment-analysis.md
  - topic-modeling.md
  - named-entity-recognition.md
  - dashboard-design-patterns.md
last_updated: 2025-11-09
---

# Text Analytics Reporting and Visualization

## Purpose
Create comprehensive reports and visualizations for text analytics results including sentiment analysis, topic modeling, entity extraction, and advanced NLP insights with interactive dashboards and actionable recommendations.

## Template

```
You are a text analytics reporting expert. Create comprehensive reports for [ANALYSIS_RESULTS] covering [REPORT_SECTIONS] with visualizations for [STAKEHOLDERS] focusing on [KEY_INSIGHTS].

REPORTING REQUIREMENTS:
- Report type: [REPORT_TYPE] (executive summary/technical/comprehensive)
- Audience: [STAKEHOLDERS]
- Key metrics: [KEY_METRICS]
- Visualization style: [VISUALIZATION_STYLE] (static/interactive/dashboard)
- Insights focus: [INSIGHTS_FOCUS]
- Deliverable format: [DELIVERABLE_FORMAT]

Generate comprehensive text analytics report:

### COMPREHENSIVE TEXT ANALYTICS REPORTING

Report Generation Framework:
```python
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from wordcloud import WordCloud

class TextAnalyticsReporter:
    def __init__(self):
        self.report_sections = {}
        self.visualizations = {}
        self.insights = {}

    def create_executive_summary(self, analysis_results):
        """Create executive summary of analysis"""
        summary = {
            'total_documents': len(analysis_results.get('documents', [])),
            'analysis_date': pd.Timestamp.now().strftime('%Y-%m-%d'),
            'key_findings': [],
            'recommendations': []
        }

        # Extract key metrics
        if 'sentiment' in analysis_results:
            sentiment_data = analysis_results['sentiment']
            positive_ratio = sum(1 for s in sentiment_data if s.get('label') == 'positive') / len(sentiment_data)
            summary['overall_sentiment'] = 'Positive' if positive_ratio > 0.6 else 'Negative' if positive_ratio < 0.4 else 'Mixed'
            summary['sentiment_confidence'] = f"{positive_ratio*100:.1f}%"

        if 'topics' in analysis_results:
            summary['num_topics_discovered'] = len(analysis_results['topics'])
            summary['top_topics'] = [t.get('label', f"Topic {t['topic_id']}") for t in analysis_results['topics'][:3]]

        if 'entities' in analysis_results:
            all_entities = []
            for doc in analysis_results['entities']:
                all_entities.extend([e['text'] for e in doc.get('entities', [])])
            top_entities = pd.Series(all_entities).value_counts().head(5).index.tolist()
            summary['top_entities'] = top_entities

        return summary

    def create_sentiment_visualizations(self, sentiment_results):
        """Create comprehensive sentiment visualizations"""
        # Extract sentiment data
        sentiments = [r['vader']['label'] for r in sentiment_results]
        compound_scores = [r['vader']['compound'] for r in sentiment_results]
        polarities = [r['textblob']['polarity'] for r in sentiment_results]
        subjectivities = [r['textblob']['subjectivity'] for r in sentiment_results]

        # Create figure with subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=[
                'Sentiment Distribution',
                'Sentiment Score Distribution',
                'Polarity vs Subjectivity',
                'Sentiment Over Time (if available)'
            ],
            specs=[
                [{"type": "pie"}, {"type": "histogram"}],
                [{"type": "scatter"}, {"type": "scatter"}]
            ]
        )

        # 1. Sentiment distribution pie chart
        sentiment_counts = pd.Series(sentiments).value_counts()
        fig.add_trace(
            go.Pie(labels=sentiment_counts.index, values=sentiment_counts.values, name="Sentiment"),
            row=1, col=1
        )

        # 2. Compound score histogram
        fig.add_trace(
            go.Histogram(x=compound_scores, name="Compound Scores", nbinsx=30),
            row=1, col=2
        )

        # 3. Polarity vs Subjectivity scatter
        fig.add_trace(
            go.Scatter(x=polarities, y=subjectivities, mode='markers',
                      marker=dict(size=5, opacity=0.6), name="Documents"),
            row=2, col=1
        )

        fig.update_layout(height=800, showlegend=True, title_text="Sentiment Analysis Dashboard")
        return fig

    def create_topic_visualizations(self, topic_results):
        """Create topic modeling visualizations"""
        topics = topic_results['topics']

        # Topic word importance
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=[
                'Topic Size Distribution',
                'Topic Coherence Scores',
                'Top Words per Topic',
                'Document-Topic Distribution'
            ]
        )

        # 1. Topic sizes (if available)
        if 'doc_topic_distributions' in topic_results:
            topic_counts = {}
            for dist in topic_results['doc_topic_distributions']:
                for topic_id, prob in dist:
                    topic_counts[topic_id] = topic_counts.get(topic_id, 0) + 1

            fig.add_trace(
                go.Bar(x=list(topic_counts.keys()), y=list(topic_counts.values())),
                row=1, col=1
            )

        # 2. Create word clouds for each topic
        topic_wordclouds = []
        for topic in topics[:6]:  # Limit to 6 topics
            word_freq = {word: prob for word, prob in topic.get('words', [])[:50]}

            wordcloud = WordCloud(
                width=400,
                height=300,
                background_color='white',
                colormap='viridis'
            ).generate_from_frequencies(word_freq)

            topic_wordclouds.append({
                'topic_id': topic['topic_id'],
                'wordcloud': wordcloud,
                'top_words': topic.get('top_words', [])[:10]
            })

        return {
            'dashboard': fig,
            'wordclouds': topic_wordclouds
        }

    def create_entity_visualizations(self, entity_results):
        """Create named entity visualizations"""
        # Extract all entities
        all_entities = []
        entity_types = []

        for doc_result in entity_results:
            for entity in doc_result.get('entities', []):
                all_entities.append(entity['text'])
                entity_types.append(entity['label'])

        # Create visualizations
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=[
                'Entity Type Distribution',
                'Top 20 Most Frequent Entities',
                'Entity Co-occurrence Network',
                'Entities per Document'
            ],
            specs=[
                [{"type": "pie"}, {"type": "bar"}],
                [{"type": "scatter"}, {"type": "histogram"}]
            ]
        )

        # 1. Entity type distribution
        type_counts = pd.Series(entity_types).value_counts()
        fig.add_trace(
            go.Pie(labels=type_counts.index, values=type_counts.values),
            row=1, col=1
        )

        # 2. Top entities
        entity_counts = pd.Series(all_entities).value_counts().head(20)
        fig.add_trace(
            go.Bar(x=entity_counts.values, y=entity_counts.index, orientation='h'),
            row=1, col=2
        )

        # 3. Entities per document
        entities_per_doc = [len(doc.get('entities', [])) for doc in entity_results]
        fig.add_trace(
            go.Histogram(x=entities_per_doc, nbinsx=20),
            row=2, col=2
        )

        fig.update_layout(height=800, showlegend=False, title_text="Entity Analysis Dashboard")
        return fig

    def create_comprehensive_dashboard(self, analysis_results):
        """Create comprehensive analytics dashboard"""
        fig = make_subplots(
            rows=3, cols=3,
            subplot_titles=[
                'Overall Sentiment', 'Topic Distribution', 'Entity Types',
                'Document Length Distribution', 'Reading Level', 'Top Keywords',
                'Sentiment Trend', 'Topic Evolution', 'Entity Timeline'
            ],
            specs=[
                [{"type": "pie"}, {"type": "bar"}, {"type": "pie"}],
                [{"type": "histogram"}, {"type": "pie"}, {"type": "bar"}],
                [{"type": "scatter"}, {"type": "heatmap"}, {"type": "scatter"}]
            ]
        )

        # Populate dashboard with available data
        # This would include all the specific plotting code

        fig.update_layout(
            height=1200,
            showlegend=False,
            title_text="Text Analytics Comprehensive Dashboard"
        )

        return fig

    def generate_insights(self, analysis_results):
        """Generate actionable insights from analysis"""
        insights = {
            'key_findings': [],
            'sentiment_insights': [],
            'topic_insights': [],
            'entity_insights': [],
            'content_quality_insights': [],
            'recommendations': []
        }

        # Sentiment insights
        if 'sentiment' in analysis_results:
            sentiment_data = analysis_results['sentiment']
            positive_count = sum(1 for s in sentiment_data if s.get('vader', {}).get('label') == 'positive')
            negative_count = sum(1 for s in sentiment_data if s.get('vader', {}).get('label') == 'negative')
            total = len(sentiment_data)

            positive_ratio = positive_count / total if total > 0 else 0

            insights['sentiment_insights'].append(
                f"Overall sentiment is {positive_ratio*100:.1f}% positive, {(negative_count/total*100):.1f}% negative"
            )

            if positive_ratio < 0.3:
                insights['recommendations'].append("High negative sentiment detected - investigate root causes")
            elif positive_ratio > 0.7:
                insights['recommendations'].append("Strong positive sentiment - leverage for marketing")

        # Topic insights
        if 'topics' in analysis_results:
            topic_data = analysis_results['topics']
            insights['topic_insights'].append(f"Identified {len(topic_data)} distinct topics")

            if 'coherence_score' in analysis_results:
                coherence = analysis_results['coherence_score']
                insights['topic_insights'].append(f"Topic coherence score: {coherence:.3f}")

        # Entity insights
        if 'entities' in analysis_results:
            all_entities = []
            for doc in analysis_results['entities']:
                all_entities.extend([e['text'] for e in doc.get('entities', [])])

            unique_entities = len(set(all_entities))
            total_entities = len(all_entities)

            insights['entity_insights'].append(
                f"Extracted {total_entities} entity mentions ({unique_entities} unique)"
            )

        return insights

    def create_word_cloud(self, texts, max_words=100):
        """Create word cloud from texts"""
        combined_text = ' '.join(texts)

        wordcloud = WordCloud(
            width=1200,
            height=600,
            max_words=max_words,
            background_color='white',
            colormap='viridis',
            stopwords=set(['the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at'])
        ).generate(combined_text)

        fig, ax = plt.subplots(figsize=(15, 8))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        ax.set_title('Word Cloud - Most Frequent Terms', fontsize=20, fontweight='bold')

        plt.tight_layout()
        return fig

    def create_statistical_summary(self, analysis_results):
        """Create statistical summary tables"""
        summary_stats = {}

        # Document statistics
        if 'documents' in analysis_results:
            docs = analysis_results['documents']
            summary_stats['document_stats'] = {
                'total_documents': len(docs),
                'avg_length': np.mean([len(d.split()) for d in docs]),
                'median_length': np.median([len(d.split()) for d in docs]),
                'std_length': np.std([len(d.split()) for d in docs])
            }

        # Sentiment statistics
        if 'sentiment' in analysis_results:
            sentiment_data = analysis_results['sentiment']
            compound_scores = [s['vader']['compound'] for s in sentiment_data]

            summary_stats['sentiment_stats'] = {
                'mean_sentiment': np.mean(compound_scores),
                'median_sentiment': np.median(compound_scores),
                'std_sentiment': np.std(compound_scores),
                'positive_count': sum(1 for s in compound_scores if s > 0.05),
                'negative_count': sum(1 for s in compound_scores if s < -0.05),
                'neutral_count': sum(1 for s in compound_scores if -0.05 <= s <= 0.05)
            }

        return pd.DataFrame(summary_stats).T

    def generate_final_report(self, analysis_results):
        """Generate final comprehensive report"""
        report = f"""
# TEXT ANALYTICS COMPREHENSIVE REPORT

## Executive Summary
Analysis of {analysis_results.get('total_documents', 'N/A')} documents completed on {pd.Timestamp.now().strftime('%Y-%m-%d')}.

### Key Metrics
- Overall Sentiment: {analysis_results.get('overall_sentiment', 'N/A')}
- Topics Discovered: {analysis_results.get('num_topics', 'N/A')}
- Entities Extracted: {analysis_results.get('total_entities', 'N/A')}
- Average Document Quality: {analysis_results.get('quality_score', 'N/A')}/10

## Detailed Findings

### 1. Sentiment Analysis
{self._format_sentiment_section(analysis_results)}

### 2. Topic Analysis
{self._format_topic_section(analysis_results)}

### 3. Entity Analysis
{self._format_entity_section(analysis_results)}

### 4. Content Quality Assessment
{self._format_quality_section(analysis_results)}

## Insights and Recommendations
{self._format_insights_section(analysis_results)}

## Methodology
{self._format_methodology_section(analysis_results)}

## Appendix
- Processing Time: {analysis_results.get('processing_time', 'N/A')}
- Models Used: {', '.join(analysis_results.get('models_used', []))}
- Confidence Level: {analysis_results.get('confidence_level', 'N/A')}
        """

        return report

    def _format_sentiment_section(self, results):
        """Format sentiment analysis section"""
        if 'sentiment' not in results:
            return "No sentiment analysis data available."

        return f"""
- Positive documents: {results.get('positive_count', 0)}
- Negative documents: {results.get('negative_count', 0)}
- Neutral documents: {results.get('neutral_count', 0)}
- Average sentiment score: {results.get('avg_sentiment', 0):.3f}
        """

    def _format_topic_section(self, results):
        """Format topic analysis section"""
        if 'topics' not in results:
            return "No topic modeling data available."

        topics_text = "\\n".join([
            f"- Topic {i+1}: {', '.join(t.get('top_words', [])[:5])}"
            for i, t in enumerate(results.get('topics', [])[:5])
        ])

        return topics_text

    def _format_entity_section(self, results):
        """Format entity analysis section"""
        if 'entities' not in results:
            return "No entity extraction data available."

        return f"""
- Total entities: {results.get('total_entities', 0)}
- Unique entities: {results.get('unique_entities', 0)}
- Top entity types: {', '.join(results.get('top_entity_types', []))}
        """

    def _format_quality_section(self, results):
        """Format content quality section"""
        return f"""
- Average reading level: {results.get('avg_reading_level', 'N/A')}
- Average document length: {results.get('avg_doc_length', 'N/A')} words
- Lexical diversity: {results.get('lexical_diversity', 'N/A')}
        """

    def _format_insights_section(self, results):
        """Format insights and recommendations section"""
        insights = results.get('insights', {})
        recommendations = insights.get('recommendations', [])

        if not recommendations:
            return "No specific recommendations at this time."

        return "\\n".join([f"- {rec}" for rec in recommendations])

    def _format_methodology_section(self, results):
        """Format methodology section"""
        return f"""
This analysis employed the following methods:
- Text Preprocessing: {results.get('preprocessing_method', 'Standard NLP pipeline')}
- Sentiment Analysis: {results.get('sentiment_method', 'Multi-model ensemble')}
- Topic Modeling: {results.get('topic_method', 'LDA and BERTopic')}
- Entity Recognition: {results.get('ner_method', 'spaCy and transformers')}
        """

# Initialize reporter
reporter = TextAnalyticsReporter()

# Create visualizations
sentiment_viz = reporter.create_sentiment_visualizations([SENTIMENT_RESULTS])
topic_viz = reporter.create_topic_visualizations([TOPIC_RESULTS])
entity_viz = reporter.create_entity_visualizations([ENTITY_RESULTS])

# Create comprehensive dashboard
dashboard = reporter.create_comprehensive_dashboard([ANALYSIS_RESULTS])

# Generate insights
insights = reporter.generate_insights([ANALYSIS_RESULTS])

# Create final report
final_report = reporter.generate_final_report([ANALYSIS_RESULTS])
```

Export and Delivery:
```python
def export_report_to_html(report_content, visualizations, output_path='report.html'):
    """Export report to HTML format"""
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Text Analytics Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #333; }}
            h2 {{ color: #666; }}
            .metric {{ background-color: #f0f0f0; padding: 10px; margin: 10px 0; }}
        </style>
    </head>
    <body>
        {report_content}
        <div id="visualizations">
            {visualizations}
        </div>
    </body>
    </html>
    """

    with open(output_path, 'w') as f:
        f.write(html_template)

def export_to_pdf(report_content, output_path='report.pdf'):
    """Export report to PDF format"""
    # Would use libraries like reportlab or weasyprint
    pass

def create_powerpoint_presentation(analysis_results, output_path='presentation.pptx'):
    """Create PowerPoint presentation"""
    from pptx import Presentation
    from pptx.util import Inches

    prs = Presentation()

    # Title slide
    title_slide = prs.slides.add_slide(prs.slide_layouts[0])
    title = title_slide.shapes.title
    subtitle = title_slide.placeholders[1]
    title.text = "Text Analytics Report"
    subtitle.text = f"Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d')}"

    # Add more slides with visualizations and insights

    prs.save(output_path)

OUTPUT REQUIREMENTS:
1. Executive summary with key metrics
2. Sentiment analysis visualizations and insights
3. Topic modeling results and word clouds
4. Entity extraction charts and statistics
5. Comprehensive interactive dashboard
6. Statistical summary tables
7. Actionable insights and recommendations
8. Methodology documentation
9. Exportable reports (HTML, PDF, PPT)
10. Data quality assessment
```

## Variables

### Reporting Configuration
- [ANALYSIS_RESULTS] - Results from text analytics
- [REPORT_SECTIONS] - Sections to include in report
- [STAKEHOLDERS] - Target audience
- [KEY_INSIGHTS] - Key insights to highlight
- [REPORT_TYPE] - Type of report
- [KEY_METRICS] - Metrics to feature
- [VISUALIZATION_STYLE] - Visualization style
- [INSIGHTS_FOCUS] - Focus area for insights
- [DELIVERABLE_FORMAT] - Output format

### Data Sources
- [SENTIMENT_RESULTS] - Sentiment analysis results
- [TOPIC_RESULTS] - Topic modeling results
- [ENTITY_RESULTS] - Entity extraction results

## Usage Examples

### Example 1: Executive Dashboard
```
REPORT_TYPE: "executive summary"
STAKEHOLDERS: "C-suite executives"
VISUALIZATION_STYLE: "interactive dashboard"
KEY_METRICS: ["overall_sentiment", "top_topics", "key_entities"]
DELIVERABLE_FORMAT: "interactive HTML"
```

### Example 2: Technical Report
```
REPORT_TYPE: "technical comprehensive"
STAKEHOLDERS: "data science team"
VISUALIZATION_STYLE: "static detailed"
INSIGHTS_FOCUS: "methodology and performance"
DELIVERABLE_FORMAT: "PDF with code snippets"
```

### Example 3: Stakeholder Presentation
```
REPORT_TYPE: "presentation"
STAKEHOLDERS: "business stakeholders"
VISUALIZATION_STYLE: "clear and simple"
KEY_INSIGHTS: "actionable recommendations"
DELIVERABLE_FORMAT: "PowerPoint"
```

## Best Practices

1. **Know your audience**: Tailor complexity to stakeholder expertise
2. **Lead with insights**: Start with key findings, not methodology
3. **Use clear visualizations**: Avoid cluttered or confusing charts
4. **Provide context**: Explain what metrics mean for the business
5. **Be actionable**: Include specific recommendations
6. **Show confidence**: Include uncertainty and confidence intervals
7. **Tell a story**: Connect findings into coherent narrative
8. **Use interactive elements**: Dashboards engage stakeholders
9. **Document methodology**: Transparency builds trust
10. **Follow up**: Track whether recommendations are implemented
