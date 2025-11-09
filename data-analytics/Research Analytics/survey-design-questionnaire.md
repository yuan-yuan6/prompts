---
title: Survey Design and Questionnaire Development Template
category: data-analytics/Research Analytics
tags: [data-analytics, design, development, research, strategy, template, testing]
use_cases:
  - Design comprehensive survey questionnaires with proper question structure, scale development, and cognitive testing to ensure valid and reliable measurement instruments.
  - Project planning and execution
  - Strategy development
related_templates:
  - survey-analysis-overview.md
  - survey-sampling-methodology.md
  - survey-statistical-validation.md
last_updated: 2025-11-09
---

# Survey Design and Questionnaire Development Template

## Purpose
Design comprehensive survey questionnaires with proper question structure, scale development, and cognitive testing to ensure valid and reliable measurement instruments for your research objectives.

## Template

```
You are a survey research expert. Design a comprehensive questionnaire for [RESEARCH_PURPOSE] targeting [TARGET_POPULATION] to investigate [RESEARCH_QUESTIONS].

SURVEY DESIGN FRAMEWORK:
Research Objectives:
- Primary objective: [PRIMARY_OBJECTIVE]
- Secondary objectives: [SECONDARY_OBJECTIVES]
- Research questions: [RESEARCH_QUESTIONS]
- Hypotheses: [RESEARCH_HYPOTHESES]
- Expected outcomes: [EXPECTED_OUTCOMES]
- Policy/business implications: [PRACTICAL_IMPLICATIONS]

Target Population:
- Population definition: [POPULATION_DEFINITION]
- Geographic scope: [GEOGRAPHIC_SCOPE]
- Demographic characteristics: [TARGET_DEMOGRAPHICS]
- Inclusion criteria: [INCLUSION_CRITERIA]
- Exclusion criteria: [EXCLUSION_CRITERIA]
- Population size: [POPULATION_SIZE]
- Accessibility: [POPULATION_ACCESSIBILITY]

QUESTIONNAIRE DEVELOPMENT:

Question Design Principles:
```python
# Question type framework
question_types = {
    'demographic': {
        'age': {'type': 'numeric', 'validation': 'range(18, 120)'},
        'gender': {'type': 'categorical', 'options': ['Male', 'Female', 'Other', 'Prefer not to say']},
        'education': {'type': 'ordinal', 'scale': '1-7 education levels'},
        'income': {'type': 'ordinal', 'scale': 'income brackets'}
    },

    'attitudinal': {
        'satisfaction': {'type': 'likert', 'scale': '1-5 or 1-7', 'anchors': 'Very dissatisfied to Very satisfied'},
        'agreement': {'type': 'likert', 'scale': '1-5', 'anchors': 'Strongly disagree to Strongly agree'},
        'importance': {'type': 'likert', 'scale': '1-5', 'anchors': 'Not important to Very important'},
        'frequency': {'type': 'ordinal', 'options': ['Never', 'Rarely', 'Sometimes', 'Often', 'Always']}
    },

    'behavioral': {
        'usage': {'type': 'frequency', 'measurement': 'times per period'},
        'purchase': {'type': 'binary', 'options': ['Yes', 'No']},
        'preference': {'type': 'ranking', 'method': 'rank order or forced choice'}
    },

    'open_ended': {
        'opinion': {'type': 'text', 'length': 'short to medium'},
        'experience': {'type': 'text', 'length': 'medium to long'},
        'suggestions': {'type': 'text', 'length': 'variable'}
    }
}

# Question validation framework
def validate_questions(questions_list):
    """Validate survey questions for common issues"""

    validation_results = {}

    for i, question in enumerate(questions_list):
        issues = []

        # Check for leading questions
        leading_words = ['don\'t you think', 'wouldn\'t you agree', 'isn\'t it true']
        if any(word in question.lower() for word in leading_words):
            issues.append('Potential leading question')

        # Check for double-barreled questions
        if ' and ' in question and '?' in question:
            issues.append('Potential double-barreled question')

        # Check for negative wording
        negative_words = ['not', 'never', 'without', 'unless']
        if any(word in question.lower() for word in negative_words):
            issues.append('Contains negative wording')

        # Check question length
        if len(question.split()) > 20:
            issues.append('Question may be too long')

        # Check for jargon/technical terms
        technical_indicators = ['utilize', 'implementation', 'methodology']
        if any(term in question.lower() for term in technical_indicators):
            issues.append('May contain jargon')

        validation_results[f'Question_{i+1}'] = {
            'question': question,
            'issues': issues,
            'quality_score': max(0, 5 - len(issues))
        }

    return validation_results

# Cognitive testing framework
def cognitive_testing_protocol():
    """Framework for cognitive testing of survey questions"""

    protocol = {
        'think_aloud': {
            'description': 'Respondents verbalize thoughts while answering',
            'sample_size': '5-10 per major demographic group',
            'analysis': 'Qualitative analysis of verbal protocols'
        },

        'probing': {
            'comprehension_probes': [
                'What does this question mean to you?',
                'How did you arrive at that answer?',
                'What were you thinking about when you answered?'
            ],
            'retrieval_probes': [
                'How easy or difficult was it to remember this information?',
                'How certain are you about this answer?'
            ],
            'judgment_probes': [
                'How did you decide on your answer?',
                'What does [term] mean to you?'
            ]
        },

        'response_analysis': {
            'response_time': 'Measure time taken to answer each question',
            'response_patterns': 'Identify straight-lining or other response biases',
            'item_non_response': 'Track questions with high skip rates'
        }
    }

    return protocol
```

Question Structure:
- Total questions: [TOTAL_QUESTIONS]
- Demographic questions: [DEMOGRAPHIC_QUESTIONS]
- Core content questions: [CORE_QUESTIONS]
- Screening questions: [SCREENING_QUESTIONS]
- Open-ended questions: [OPEN_ENDED_QUESTIONS]
- Scale questions: [SCALE_QUESTIONS]
- Estimated completion time: [COMPLETION_TIME] minutes

SCALE DEVELOPMENT:
```python
# Likert scale development and validation
def develop_likert_scale(construct, items, scale_points=5):
    """Develop and validate Likert scales"""

    scale_design = {
        'construct': construct,
        'number_of_items': len(items),
        'scale_points': scale_points,
        'anchors': {
            3: ['Disagree', 'Neutral', 'Agree'],
            5: ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'],
            7: ['Strongly Disagree', 'Disagree', 'Somewhat Disagree', 'Neutral',
                'Somewhat Agree', 'Agree', 'Strongly Agree']
        }[scale_points],
        'items': items
    }

    # Item analysis guidelines
    analysis_criteria = {
        'item_total_correlation': 'Should be > 0.30',
        'cronbachs_alpha': 'Should be > 0.70 for scale',
        'factor_loading': 'Should be > 0.40 in EFA',
        'communality': 'Should be > 0.25',
        'item_difficulty': 'Proportion endorsing each response category'
    }

    return scale_design, analysis_criteria

# Semantic differential scale
def semantic_differential_scale(concept, bipolar_pairs):
    """Design semantic differential scales"""

    scale_structure = {
        'concept': concept,
        'scale_points': 7,  # Standard for semantic differential
        'bipolar_pairs': bipolar_pairs,
        'randomization': 'Randomize direction of positive pole',
        'instructions': f'Rate [CONCEPT] on each of the following scales'
    }

    return scale_structure

# Rating scale optimization
def optimize_rating_scale(scale_type, research_context):
    """Optimize rating scale design based on research context"""

    recommendations = {
        'number_of_points': {
            'satisfaction': '5 or 7 points - good discrimination',
            'agreement': '5 points - clear conceptual anchors',
            'frequency': 'Verbal labels preferred over numbers',
            'importance': '5 points with explicit "not applicable" option'
        },

        'labeling': {
            'fully_labeled': 'All points labeled - reduces ambiguity',
            'end_anchored': 'Only endpoints labeled - allows for more gradation',
            'verbal_labels': 'Use consistent verbal descriptors'
        },

        'response_format': {
            'horizontal': 'Traditional and familiar to respondents',
            'vertical': 'May work better on mobile devices',
            'slider': 'Continuous response, good user experience',
            'buttons': 'Clear selection, works well across devices'
        }
    }

    return recommendations.get(scale_type, recommendations)
```

OUTPUT REQUIREMENTS:
Deliver comprehensive questionnaire design including:

1. **Question Design Documentation**
   - Question development process
   - Question types and formats
   - Cognitive testing results
   - Pilot testing findings
   - Question revision history

2. **Scale Development**
   - Scale construction methodology
   - Item development procedures
   - Psychometric properties
   - Scoring guidelines
   - Interpretation framework

3. **Questionnaire Layout**
   - Question ordering strategy
   - Visual design elements
   - Skip logic patterns
   - Progress indicators
   - Completion instructions

4. **Quality Assurance**
   - Question validation results
   - Expert review feedback
   - Pilot test findings
   - Revision documentation
   - Final quality assessment
```

## Variables

### Research Design Variables
- [RESEARCH_PURPOSE] - Primary purpose of the survey research
- [TARGET_POPULATION] - Population of interest for the survey
- [RESEARCH_QUESTIONS] - List of research questions to address
- [PRIMARY_OBJECTIVE] - Main research objective
- [SECONDARY_OBJECTIVES] - Additional research objectives
- [RESEARCH_HYPOTHESES] - Research hypotheses to test
- [EXPECTED_OUTCOMES] - Expected findings or outcomes
- [PRACTICAL_IMPLICATIONS] - Real-world applications of findings
- [POPULATION_DEFINITION] - Precise definition of target population
- [GEOGRAPHIC_SCOPE] - Geographic boundaries of the study
- [TARGET_DEMOGRAPHICS] - Demographic characteristics of interest
- [INCLUSION_CRITERIA] - Criteria for including participants
- [EXCLUSION_CRITERIA] - Criteria for excluding participants
- [POPULATION_SIZE] - Estimated size of target population
- [POPULATION_ACCESSIBILITY] - Level of access to target population

### Questionnaire Design Variables
- [TOTAL_QUESTIONS] - Total number of questions in survey
- [DEMOGRAPHIC_QUESTIONS] - Number of demographic questions
- [CORE_QUESTIONS] - Number of core content questions
- [SCREENING_QUESTIONS] - Number of screening questions
- [OPEN_ENDED_QUESTIONS] - Number of open-ended questions
- [SCALE_QUESTIONS] - Number of scaled response questions
- [COMPLETION_TIME] - Estimated completion time in minutes
- [QUESTION_TYPES] - Types of questions included
- [SCALE_TYPE] - Types of scales used (Likert, semantic differential, etc.)
- [RESPONSE_OPTIONS] - Response option formats
- [SKIP_LOGIC] - Skip pattern complexity
- [RANDOMIZATION] - Question or option randomization used
- [COGNITIVE_TESTING] - Cognitive testing procedures performed
- [PILOT_TESTING] - Pilot testing procedures and results
- [QUESTION_ORDER] - Question ordering strategy
- [VISUAL_DESIGN] - Visual design elements and layout

### Scale Development Variables
- [SCALE_CONSTRUCTION] - Scale construction methodology
- [ITEM_DEVELOPMENT] - Item development procedures
- [SCALE_VALIDATION] - Scale validation procedures
- [RELIABILITY_MEASURES] - Reliability measures calculated
- [VALIDITY_EVIDENCE] - Types of validity evidence collected
- [SCALE_SCORING] - Scale scoring procedures
- [SCALE_INTERPRETATION] - Guidelines for scale interpretation
- [CUT_POINTS] - Meaningful cut points or categories

## Usage Examples

### Example 1: Customer Satisfaction Survey
```
RESEARCH_PURPOSE: "Measure customer satisfaction with service quality"
TARGET_POPULATION: "Current customers who used service in past 12 months"
TOTAL_QUESTIONS: "25 questions"
SCALE_TYPE: "5-point Likert satisfaction scales"
COMPLETION_TIME: "8 minutes"
```

### Example 2: Employee Engagement Survey
```
RESEARCH_PURPOSE: "Measure employee engagement and organizational culture"
TARGET_POPULATION: "All full-time and part-time employees"
SCALE_CONSTRUCTION: "Multi-item engagement and culture scales"
QUESTION_TYPES: "Mix of Likert scales and open-ended feedback"
PILOT_TESTING: "50 employees across departments"
```

## Best Practices

1. **Keep questions clear and concise** - Use simple language that all respondents understand
2. **Avoid leading or biased questions** - Ensure questions don't suggest desired answers
3. **Use appropriate response scales** - Match scale types to measurement objectives
4. **Conduct cognitive testing** - Test questions with representative respondents
5. **Pilot test thoroughly** - Validate questionnaire before full deployment
6. **Minimize respondent burden** - Keep surveys as short as possible
7. **Ensure logical flow** - Order questions to maintain engagement
8. **Provide clear instructions** - Help respondents understand what's expected
9. **Consider mobile optimization** - Design for various device types
10. **Test skip logic carefully** - Verify branching works correctly

## Tips for Success

- Start with research objectives and work backward to questions
- Use established scales when possible for comparability
- Balance closed and open-ended questions appropriately
- Consider cultural sensitivity and language clarity
- Build in attention checks for online surveys
- Randomize question or response order to reduce bias
- Allow "don't know" or "not applicable" options when appropriate
- Keep rating scales consistent throughout the survey
- Use visual aids sparingly and purposefully
- Document all design decisions for methodological transparency
