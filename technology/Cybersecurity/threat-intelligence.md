---
title: Threat Intelligence Template
category: technology/Cybersecurity
tags: [data-science, design, machine-learning, marketing, research, strategy, technology, template]
use_cases:
  - Implementing comprehensive threat intelligence program including collection, analysis, dissem...
  - Project planning and execution
  - Strategy development
related_templates:
  - cloud-architecture-framework.md
  - site-reliability-engineering.md
  - cloud-migration-strategy.md
last_updated: 2025-11-09
---

# Threat Intelligence Template

## Purpose
Comprehensive threat intelligence program including collection, analysis, dissemination, and actionable intelligence for proactive threat detection, prevention, and response.

## Template Structure

### Intelligence Requirements
- **Intelligence Objectives**: {intelligence_objectives}
- **Priority Intelligence Requirements**: {pir}
- **Threat Actors**: {threat_actors}
- **Attack Vectors**: {attack_vectors}
- **Industry Focus**: {industry_focus}
- **Geographic Scope**: {geographic_scope}
- **Time Horizon**: {time_horizon}
- **Intelligence Consumers**: {intelligence_consumers}
- **Decision Support**: {decision_support}
- **Success Metrics**: {intelligence_success_metrics}

### Collection Framework
- **Collection Sources**: {collection_sources}
- **Collection Methods**: {collection_methods}
- **OSINT Sources**: {osint_sources}
- **Commercial Feeds**: {commercial_feeds}
- **Government Sources**: {government_sources}
- **Industry Sharing**: {industry_sharing}
- **Internal Sources**: {internal_sources}
- **Technical Collection**: {technical_collection}
- **Human Intelligence**: {human_intelligence}
- **Collection Planning**: {collection_planning}

### Analysis and Processing
- **Analysis Framework**: {analysis_framework}
- **Analytical Methods**: {analytical_methods}
- **Threat Modeling**: {threat_modeling}
- **Attribution Analysis**: {attribution_analysis}
- **Indicator Analysis**: {indicator_analysis}
- **Campaign Tracking**: {campaign_tracking}
- **Trend Analysis**: {trend_analysis}
- **Predictive Analysis**: {predictive_analysis}
- **Confidence Assessment**: {confidence_assessment}
- **Quality Control**: {analysis_quality_control}

### Intelligence Products
- **Strategic Intelligence**: {strategic_intelligence}
- **Tactical Intelligence**: {tactical_intelligence}
- **Operational Intelligence**: {operational_intelligence}
- **Technical Intelligence**: {technical_intelligence}
- **IOC Feeds**: {ioc_feeds}
- **Threat Reports**: {threat_reports}
- **Briefings**: {intelligence_briefings}
- **Alerts**: {intelligence_alerts}
- **Hunting Guidance**: {hunting_guidance}
- **Risk Assessments**: {intelligence_risk_assessments}

### Dissemination and Sharing
- **Distribution Lists**: {distribution_lists}
- **Classification Levels**: {classification_levels}
- **Sharing Protocols**: {sharing_protocols}
- **TLP Handling**: {tlp_handling}
- **Automation**: {dissemination_automation}
- **Integration**: {intelligence_integration}
- **Feedback Mechanisms**: {feedback_mechanisms}
- **Metrics and Reporting**: {dissemination_metrics}
- **External Sharing**: {external_sharing}
- **Legal Considerations**: {legal_considerations}

Please provide detailed collection plans, analysis workflows, intelligence products, and sharing frameworks.

## Usage Examples

### Financial Services Threat Intelligence
```
Implement comprehensive threat intelligence program for FinancialBank targeting banking trojan campaigns with financial sector industry focus.

Intelligence Requirements:
- Counter banking trojans, ATM malware intelligence objectives
- Focus on Emotet, TrickBot, Zeus priority intelligence requirements
- Track organized cybercrime, nation-state threat actors
- Monitor phishing, malware, social engineering attack vectors
- Cover North America, Europe geographic scope

Collection Framework:
- Collect from FS-ISAC, FBI, DHS government sources
- Use FireEye, CrowdStrike, Recorded Future commercial feeds
- Monitor dark web, social media OSINT sources
- Share via FS-ISAC, regional banking groups industry sharing
- Analyze internal incident data, logs internal sources

### Analysis and Processing
- Apply Diamond Model, Kill Chain analysis framework
- Use structured analytic techniques analytical methods
- Track campaigns by TTPs, infrastructure campaign tracking
- Assess low/medium/high confidence levels confidence assessment
- Validate IOCs, correlate with threat hunting analysis quality control

### Intelligence Products
- Produce weekly executive briefings strategic intelligence
- Generate daily IOC feeds, hunting queries tactical intelligence
- Create incident response playbooks operational intelligence
- Develop malware analysis reports technical intelligence
- Distribute real-time alerts for active campaigns intelligence alerts
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `{intelligence_objectives}` | Specify the intelligence objectives | "Increase efficiency by 30%" |
| `{pir}` | Specify the pir | "[specify value]" |
| `{threat_actors}` | Specify the threat actors | "[specify value]" |
| `{attack_vectors}` | Specify the attack vectors | "[specify value]" |
| `{industry_focus}` | Specify the industry focus | "Technology" |
| `{geographic_scope}` | Specify the geographic scope | "[specify value]" |
| `{time_horizon}` | Specify the time horizon | "[specify value]" |
| `{intelligence_consumers}` | Specify the intelligence consumers | "[specify value]" |
| `{decision_support}` | Specify the decision support | "[specify value]" |
| `{intelligence_success_metrics}` | Specify the intelligence success metrics | "[specify value]" |
| `{collection_sources}` | Specify the collection sources | "[specify value]" |
| `{collection_methods}` | Specify the collection methods | "[specify value]" |
| `{osint_sources}` | Specify the osint sources | "[specify value]" |
| `{commercial_feeds}` | Specify the commercial feeds | "[specify value]" |
| `{government_sources}` | Specify the government sources | "[specify value]" |
| `{industry_sharing}` | Specify the industry sharing | "Technology" |
| `{internal_sources}` | Specify the internal sources | "[specify value]" |
| `{technical_collection}` | Specify the technical collection | "[specify value]" |
| `{human_intelligence}` | Specify the human intelligence | "[specify value]" |
| `{collection_planning}` | Specify the collection planning | "[specify value]" |
| `{analysis_framework}` | Specify the analysis framework | "[specify value]" |
| `{analytical_methods}` | Specify the analytical methods | "[specify value]" |
| `{threat_modeling}` | Specify the threat modeling | "[specify value]" |
| `{attribution_analysis}` | Specify the attribution analysis | "[specify value]" |
| `{indicator_analysis}` | Specify the indicator analysis | "[specify value]" |
| `{campaign_tracking}` | Specify the campaign tracking | "[specify value]" |
| `{trend_analysis}` | Specify the trend analysis | "[specify value]" |
| `{predictive_analysis}` | Specify the predictive analysis | "[specify value]" |
| `{confidence_assessment}` | Specify the confidence assessment | "[specify value]" |
| `{analysis_quality_control}` | Specify the analysis quality control | "[specify value]" |
| `{strategic_intelligence}` | Specify the strategic intelligence | "[specify value]" |
| `{tactical_intelligence}` | Specify the tactical intelligence | "[specify value]" |
| `{operational_intelligence}` | Specify the operational intelligence | "[specify value]" |
| `{technical_intelligence}` | Specify the technical intelligence | "[specify value]" |
| `{ioc_feeds}` | Specify the ioc feeds | "[specify value]" |
| `{threat_reports}` | Specify the threat reports | "[specify value]" |
| `{intelligence_briefings}` | Specify the intelligence briefings | "[specify value]" |
| `{intelligence_alerts}` | Specify the intelligence alerts | "[specify value]" |
| `{hunting_guidance}` | Specify the hunting guidance | "[specify value]" |
| `{intelligence_risk_assessments}` | Specify the intelligence risk assessments | "[specify value]" |
| `{distribution_lists}` | Specify the distribution lists | "[specify value]" |
| `{classification_levels}` | Specify the classification levels | "[specify value]" |
| `{sharing_protocols}` | Specify the sharing protocols | "[specify value]" |
| `{tlp_handling}` | Specify the tlp handling | "[specify value]" |
| `{dissemination_automation}` | Specify the dissemination automation | "[specify value]" |
| `{intelligence_integration}` | Specify the intelligence integration | "[specify value]" |
| `{feedback_mechanisms}` | Specify the feedback mechanisms | "[specify value]" |
| `{dissemination_metrics}` | Specify the dissemination metrics | "[specify value]" |
| `{external_sharing}` | Specify the external sharing | "[specify value]" |
| `{legal_considerations}` | Specify the legal considerations | "[specify value]" |



## Best Practices

1. **Align intelligence requirements with business risk**
2. **Use multiple sources and validate information**
3. **Focus on actionable intelligence over volume**
4. **Integrate intelligence into security operations**
5. **Measure effectiveness and adjust continuously**