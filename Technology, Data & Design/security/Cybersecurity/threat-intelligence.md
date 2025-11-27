---
category: security
last_updated: 2025-11-23
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- security
- threat-intelligence
- mitre-attack
- ioc
title: Threat Intelligence Template
use_cases:
- Creating comprehensive threat intelligence program including collection, analysis,
  dissemination, and actionable intelligence for proactive threat detection, prevention,
  and response.
- Project planning and execution
- Strategy development
industries:
- finance
- technology
type: template
difficulty: intermediate
slug: threat-intelligence
---

# Threat Intelligence Template

## Purpose
Comprehensive threat intelligence program including collection, analysis, dissemination, and actionable intelligence for proactive threat detection, prevention, and response.

## Quick Threat Intel Prompt
Build threat intelligence program for [industry] organization. Define PIRs (priority intelligence requirements) aligned with business risks. Sources: OSINT + [commercial feeds: Recorded Future/CrowdStrike] + [ISACs]. Framework: MITRE ATT&CK for TTP mapping. Deliver: IOC feeds integrated with SIEM/EDR, weekly threat reports, threat actor profiles relevant to [industry], and intelligence sharing procedures (TLP classification).

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

### Healthcare Threat Intelligence Program
```
Implement threat intelligence program for HealthCare Systems protecting PHI data across 50 hospital locations.

Intelligence Requirements:
- Counter healthcare-specific ransomware, data theft intelligence objectives
- Focus on Ryuk, Conti, BlackCat targeting healthcare priority intelligence requirements
- Track ransomware gangs, hacktivists, insider threats threat actors
- Monitor ransomware, supply chain, credential theft attack vectors
- Cover United States, India (offshore operations) geographic scope

Collection Framework:
- Collect from H-ISAC, HHS, FBI government sources
- Use Mandiant, Intel 471, Flashpoint commercial feeds
- Monitor ransomware leak sites, medical forums OSINT sources
- Share via H-ISAC, regional healthcare consortiums industry sharing
- Analyze EHR access logs, medical device telemetry internal sources

Analysis and Processing:
- Apply MITRE ATT&CK for Healthcare analytical framework
- Use TTP correlation, behavioral analysis analytical methods
- Track ransomware evolution, new variants campaign tracking
- Map threats to HIPAA security controls confidence assessment
- Validate with clinical operations, medical device teams quality control

Intelligence Products:
- Produce monthly board-level risk assessments strategic intelligence
- Generate IOC feeds for medical device networks tactical intelligence
- Create ransomware response playbooks operational intelligence
- Develop medical device vulnerability reports technical intelligence
- Distribute ransomware alerts within 15 minutes intelligence alerts
```

### Critical Infrastructure (Energy Sector)
```
Implement threat intelligence for PowerGrid Utility protecting SCADA/ICS systems across power generation and distribution.

Intelligence Requirements:
- Counter nation-state OT attacks, destructive malware intelligence objectives
- Focus on Industroyer, TRITON, Pipedream priority intelligence requirements
- Track APT28, Sandworm, Volt Typhoon threat actors
- Monitor ICS exploits, supply chain, living-off-the-land attack vectors
- Cover North America, Eastern Europe (threat origins) geographic scope

Collection Framework:
- Collect from E-ISAC, CISA ICS-CERT, DOE government sources
- Use Dragos, Claroty, Nozomi commercial feeds
- Monitor ICS-focused forums, vendor advisories OSINT sources
- Share via E-ISAC, regional grid operators industry sharing
- Analyze SCADA logs, historian data, network flows internal sources

Analysis and Processing:
- Apply MITRE ATT&CK for ICS analytical framework
- Use OT-specific threat modeling analytical methods
- Track ICS malware variants, nation-state campaigns campaign tracking
- Correlate with NERC CIP compliance requirements confidence assessment
- Validate with OT engineers, control room operators quality control

Intelligence Products:
- Produce quarterly executive threat landscape strategic intelligence
- Generate Snort/YARA rules for ICS protocols tactical intelligence
- Create ICS incident response procedures operational intelligence
- Develop malware analysis for OT-specific threats technical intelligence
- Distribute grid emergency alerts via secure channels intelligence alerts
```

## Variables

### Intelligence Program Variables
| Variable | Description | Example |
|----------|-------------|----------|
| `[INTELLIGENCE_OBJECTIVES]` | Primary goals for the threat intelligence program | "Reduce mean time to detect by 50%, Proactive threat hunting" |
| `[PIR]` | Priority Intelligence Requirements | "APT activity targeting financial sector, Ransomware trends, Zero-day exploits" |
| `[THREAT_ACTORS]` | Key threat actors to monitor | "APT29, FIN7, Lazarus Group, LockBit ransomware operators" |
| `[ATTACK_VECTORS]` | Primary attack methods to track | "Phishing, Supply chain, Zero-day exploits, Credential stuffing" |
| `[INDUSTRY_FOCUS]` | Target industry vertical | "Financial Services", "Healthcare", "Critical Infrastructure" |
| `[GEOGRAPHIC_SCOPE]` | Geographic coverage area | "North America, Europe, Asia-Pacific", "Global" |
| `[TIME_HORIZON]` | Intelligence planning timeframe | "Strategic: 12-18 months, Tactical: 30-90 days, Operational: Real-time" |

### Collection Variables
| Variable | Description | Example |
|----------|-------------|----------|
| `[INTELLIGENCE_CONSUMERS]` | Recipients of intelligence products | "SOC team, IR team, CISO, Risk committee, IT operations" |
| `[COLLECTION_SOURCES]` | Intelligence data sources | "OSINT, Commercial feeds, ISAC, Internal telemetry, Dark web" |
| `[OSINT_SOURCES]` | Open source intelligence sources | "VirusTotal, Shodan, Twitter/X, Security blogs, GitHub" |
| `[COMMERCIAL_FEEDS]` | Paid threat intelligence feeds | "Recorded Future, Mandiant, CrowdStrike, ThreatConnect" |
| `[GOVERNMENT_SOURCES]` | Government intelligence sources | "CISA, FBI IC3, NCSC, ENISA, sector-specific ISACs" |
| `[INTERNAL_SOURCES]` | Internal data sources | "SIEM logs, EDR telemetry, Firewall data, Email gateway" |

### Analysis Variables
| Variable | Description | Example |
|----------|-------------|----------|
| `[ANALYSIS_FRAMEWORK]` | Framework for analyzing threats | "Diamond Model, Kill Chain, MITRE ATT&CK, F3EAD" |
| `[ANALYTICAL_METHODS]` | Analysis techniques used | "Link analysis, Pattern analysis, Behavioral analysis" |
| `[THREAT_MODELING]` | Threat modeling approach | "STRIDE, PASTA, Attack trees, Threat scenarios" |
| `[CONFIDENCE_ASSESSMENT]` | Confidence rating methodology | "Admiralty Scale (A1-F6), Percentage (High >80%, Medium 50-80%, Low <50%)" |

### Dissemination Variables
| Variable | Description | Example |
|----------|-------------|----------|
| `[TLP_HANDLING]` | Traffic Light Protocol classification | "TLP:RED (restricted), TLP:AMBER (limited), TLP:GREEN (community), TLP:CLEAR (public)" |
| `[CLASSIFICATION_LEVELS]` | Information classification levels | "Confidential, Internal, Public" |
| `[DISTRIBUTION_LISTS]` | Recipients for different intel types | "Strategic: Executive team, Tactical: Security ops, Technical: SOC analysts" |
| `[INTELLIGENCE_INTEGRATION]` | Systems for intel integration | "SIEM, SOAR, EDR, Firewall, Email gateway" |



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