---
category: technology/Cybersecurity
last_updated: 2025-11-09
related_templates:
- cloud-architecture-framework.md
- site-reliability-engineering.md
- cloud-migration-strategy.md
tags:
- data-science
- design
- machine-learning
- marketing
- research
- strategy
- technology
- template
title: Threat Intelligence Template
use_cases:
- Creating comprehensive threat intelligence program including collection, analysis,
  dissemination, and actionable intelligence for proactive threat detection, prevention,
  and response.
- Project planning and execution
- Strategy development
---

# Threat Intelligence Template

## Purpose
Comprehensive threat intelligence program including collection, analysis, dissemination, and actionable intelligence for proactive threat detection, prevention, and response.

## Quick Start

**Set Your Foundation:**
1. Define intelligence objectives: threat actors, attack vectors, industry-specific threats
2. Identify priority intelligence requirements (PIRs) aligned with business risk
3. Set geographic and industry scope for threat monitoring

**Configure Key Parameters:**
4. Select collection sources: OSINT (free), commercial feeds (Recorded Future, CrowdStrike), government (FBI, CISA)
5. Choose analysis framework: Diamond Model, Cyber Kill Chain, or MITRE ATT&CK
6. Define intelligence products: strategic reports, tactical IOCs, operational playbooks

**Implement & Deploy (Ongoing):**
7. Deploy SIEM and threat intelligence platform (TIP) like MISP or ThreatConnect
8. Integrate IOC feeds into security tools (EDR, firewall, IDS/IPS)
9. Establish intelligence sharing with ISACs and sector-specific groups
10. Create daily/weekly intelligence reports and distribute to stakeholders

**Pro Tips:** Start with MITRE ATT&CK framework for standardization, use TLP (Traffic Light Protocol) for sharing classification, focus on actionable intelligence over volume, and maintain feedback loop with SOC teams for validation.

## Template Structure

### Intelligence Requirements
- **Intelligence Objectives**: [INTELLIGENCE_OBJECTIVES]
- **Priority Intelligence Requirements**: [PIR]
- **Threat Actors**: [THREAT_ACTORS]
- **Attack Vectors**: [ATTACK_VECTORS]
- **Industry Focus**: [INDUSTRY_FOCUS]
- **Geographic Scope**: [GEOGRAPHIC_SCOPE]
- **Time Horizon**: [TIME_HORIZON]
- **Intelligence Consumers**: [INTELLIGENCE_CONSUMERS]
- **Decision Support**: [DECISION_SUPPORT]
- **Success Metrics**: [INTELLIGENCE_SUCCESS_METRICS]

### Collection Framework
- **Collection Sources**: [COLLECTION_SOURCES]
- **Collection Methods**: [COLLECTION_METHODS]
- **OSINT Sources**: [OSINT_SOURCES]
- **Commercial Feeds**: [COMMERCIAL_FEEDS]
- **Government Sources**: [GOVERNMENT_SOURCES]
- **Industry Sharing**: [INDUSTRY_SHARING]
- **Internal Sources**: [INTERNAL_SOURCES]
- **Technical Collection**: [TECHNICAL_COLLECTION]
- **Human Intelligence**: [HUMAN_INTELLIGENCE]
- **Collection Planning**: [COLLECTION_PLANNING]

### Analysis and Processing
- **Analysis Framework**: [ANALYSIS_FRAMEWORK]
- **Analytical Methods**: [ANALYTICAL_METHODS]
- **Threat Modeling**: [THREAT_MODELING]
- **Attribution Analysis**: [ATTRIBUTION_ANALYSIS]
- **Indicator Analysis**: [INDICATOR_ANALYSIS]
- **Campaign Tracking**: [CAMPAIGN_TRACKING]
- **Trend Analysis**: [TREND_ANALYSIS]
- **Predictive Analysis**: [PREDICTIVE_ANALYSIS]
- **Confidence Assessment**: [CONFIDENCE_ASSESSMENT]
- **Quality Control**: [ANALYSIS_QUALITY_CONTROL]

### Intelligence Products
- **Strategic Intelligence**: [STRATEGIC_INTELLIGENCE]
- **Tactical Intelligence**: [TACTICAL_INTELLIGENCE]
- **Operational Intelligence**: [OPERATIONAL_INTELLIGENCE]
- **Technical Intelligence**: [TECHNICAL_INTELLIGENCE]
- **IOC Feeds**: [IOC_FEEDS]
- **Threat Reports**: [THREAT_REPORTS]
- **Briefings**: [INTELLIGENCE_BRIEFINGS]
- **Alerts**: [INTELLIGENCE_ALERTS]
- **Hunting Guidance**: [HUNTING_GUIDANCE]
- **Risk Assessments**: [INTELLIGENCE_RISK_ASSESSMENTS]

### Dissemination and Sharing
- **Distribution Lists**: [DISTRIBUTION_LISTS]
- **Classification Levels**: [CLASSIFICATION_LEVELS]
- **Sharing Protocols**: [SHARING_PROTOCOLS]
- **TLP Handling**: [TLP_HANDLING]
- **Automation**: [DISSEMINATION_AUTOMATION]
- **Integration**: [INTELLIGENCE_INTEGRATION]
- **Feedback Mechanisms**: [FEEDBACK_MECHANISMS]
- **Metrics and Reporting**: [DISSEMINATION_METRICS]
- **External Sharing**: [EXTERNAL_SHARING]
- **Legal Considerations**: [LEGAL_CONSIDERATIONS]

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
| `[INTELLIGENCE_OBJECTIVES]` | Specify the intelligence objectives | "Increase efficiency by 30%" |
| `[PIR]` | Specify the pir | "[specify value]" |
| `[THREAT_ACTORS]` | Specify the threat actors | "[specify value]" |
| `[ATTACK_VECTORS]` | Specify the attack vectors | "[specify value]" |
| `[INDUSTRY_FOCUS]` | Specify the industry focus | "Technology" |
| `[GEOGRAPHIC_SCOPE]` | Specify the geographic scope | "[specify value]" |
| `[TIME_HORIZON]` | Specify the time horizon | "[specify value]" |
| `[INTELLIGENCE_CONSUMERS]` | Specify the intelligence consumers | "[specify value]" |
| `[DECISION_SUPPORT]` | Specify the decision support | "[specify value]" |
| `[INTELLIGENCE_SUCCESS_METRICS]` | Specify the intelligence success metrics | "[specify value]" |
| `[COLLECTION_SOURCES]` | Specify the collection sources | "[specify value]" |
| `[COLLECTION_METHODS]` | Specify the collection methods | "[specify value]" |
| `[OSINT_SOURCES]` | Specify the osint sources | "[specify value]" |
| `[COMMERCIAL_FEEDS]` | Specify the commercial feeds | "[specify value]" |
| `[GOVERNMENT_SOURCES]` | Specify the government sources | "[specify value]" |
| `[INDUSTRY_SHARING]` | Specify the industry sharing | "Technology" |
| `[INTERNAL_SOURCES]` | Specify the internal sources | "[specify value]" |
| `[TECHNICAL_COLLECTION]` | Specify the technical collection | "[specify value]" |
| `[HUMAN_INTELLIGENCE]` | Specify the human intelligence | "[specify value]" |
| `[COLLECTION_PLANNING]` | Specify the collection planning | "[specify value]" |
| `[ANALYSIS_FRAMEWORK]` | Specify the analysis framework | "[specify value]" |
| `[ANALYTICAL_METHODS]` | Specify the analytical methods | "[specify value]" |
| `[THREAT_MODELING]` | Specify the threat modeling | "[specify value]" |
| `[ATTRIBUTION_ANALYSIS]` | Specify the attribution analysis | "[specify value]" |
| `[INDICATOR_ANALYSIS]` | Specify the indicator analysis | "[specify value]" |
| `[CAMPAIGN_TRACKING]` | Specify the campaign tracking | "[specify value]" |
| `[TREND_ANALYSIS]` | Specify the trend analysis | "[specify value]" |
| `[PREDICTIVE_ANALYSIS]` | Specify the predictive analysis | "[specify value]" |
| `[CONFIDENCE_ASSESSMENT]` | Specify the confidence assessment | "[specify value]" |
| `[ANALYSIS_QUALITY_CONTROL]` | Specify the analysis quality control | "[specify value]" |
| `[STRATEGIC_INTELLIGENCE]` | Specify the strategic intelligence | "[specify value]" |
| `[TACTICAL_INTELLIGENCE]` | Specify the tactical intelligence | "[specify value]" |
| `[OPERATIONAL_INTELLIGENCE]` | Specify the operational intelligence | "[specify value]" |
| `[TECHNICAL_INTELLIGENCE]` | Specify the technical intelligence | "[specify value]" |
| `[IOC_FEEDS]` | Specify the ioc feeds | "[specify value]" |
| `[THREAT_REPORTS]` | Specify the threat reports | "[specify value]" |
| `[INTELLIGENCE_BRIEFINGS]` | Specify the intelligence briefings | "[specify value]" |
| `[INTELLIGENCE_ALERTS]` | Specify the intelligence alerts | "[specify value]" |
| `[HUNTING_GUIDANCE]` | Specify the hunting guidance | "[specify value]" |
| `[INTELLIGENCE_RISK_ASSESSMENTS]` | Specify the intelligence risk assessments | "[specify value]" |
| `[DISTRIBUTION_LISTS]` | Specify the distribution lists | "[specify value]" |
| `[CLASSIFICATION_LEVELS]` | Specify the classification levels | "[specify value]" |
| `[SHARING_PROTOCOLS]` | Specify the sharing protocols | "[specify value]" |
| `[TLP_HANDLING]` | Specify the tlp handling | "[specify value]" |
| `[DISSEMINATION_AUTOMATION]` | Specify the dissemination automation | "[specify value]" |
| `[INTELLIGENCE_INTEGRATION]` | Specify the intelligence integration | "[specify value]" |
| `[FEEDBACK_MECHANISMS]` | Specify the feedback mechanisms | "[specify value]" |
| `[DISSEMINATION_METRICS]` | Specify the dissemination metrics | "[specify value]" |
| `[EXTERNAL_SHARING]` | Specify the external sharing | "[specify value]" |
| `[LEGAL_CONSIDERATIONS]` | Specify the legal considerations | "[specify value]" |



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Threat Intelligence Template)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/Cybersecurity](../../technology/Cybersecurity/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating comprehensive threat intelligence program including collection, analysis, dissemination, and actionable intelligence for proactive threat detection, prevention, and response.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Align intelligence requirements with business risk**
2. **Use multiple sources and validate information**
3. **Focus on actionable intelligence over volume**
4. **Integrate intelligence into security operations**
5. **Measure effectiveness and adjust continuously**