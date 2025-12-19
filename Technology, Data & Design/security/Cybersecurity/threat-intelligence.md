---
category: security
title: Threat Intelligence Program Framework
tags:
- security
- threat-intelligence
- mitre-attack
- ioc
use_cases:
- Building threat intelligence program with strategic/tactical/operational intel achieving proactive threat detection, PIR-driven collection, MITRE ATT&CK mapping
- Implementing threat intelligence platform (MISP/ThreatConnect) with IOC feeds integrated to SIEM/EDR/firewalls for automated threat blocking
- Establishing intelligence sharing with ISACs, peers using TLP classification achieving collaborative defense and early warning
related_templates:
- security/Cybersecurity/security-operations.md
- security/Security-Operations/siem-security-monitoring.md
- security/Cybersecurity/incident-response.md
industries:
- financial-services
- healthcare
- government
- technology
- energy
type: framework
difficulty: intermediate
slug: threat-intelligence
---

# Threat Intelligence Program Framework

## Purpose
Build comprehensive threat intelligence program covering priority intelligence requirements, collection from OSINT/commercial/government sources, analysis using MITRE ATT&CK/Diamond Model, intelligence products (strategic/tactical/operational), and sharing via TLP achieving proactive threat detection and response.

## 🚀 Quick Threat Intel Prompt

> Build threat intelligence for **[INDUSTRY]** organization. PIRs: **[THREAT_ACTORS]** targeting **[ASSETS]**. Collection: OSINT + **[COMMERCIAL_FEEDS]** (Recorded Future/CrowdStrike/Mandiant) + **[ISAC]** + internal telemetry. Analysis: **[MITRE_ATT&CK]** mapping, confidence assessment **[ADMIRALTY_SCALE]**. Products: strategic **[REPORTS]**, tactical **[IOC_FEEDS]**, operational **[PLAYBOOKS]**. Integration: **[SIEM/EDR/FIREWALL]**. Sharing: **[TLP]** classification, **[ISAC]** participation.

---

## Template

Build threat intelligence program for {ORGANIZATION} in {INDUSTRY} tracking {THREAT_ACTORS} achieving {INTELLIGENCE_OBJECTIVES} with {TIME_HORIZON} strategic planning.

**INTELLIGENCE REQUIREMENTS DEFINITION**

Establish what intelligence is needed and why. Priority intelligence requirements (PIRs): specific questions that intelligence must answer to support decision-making (What ransomware gangs are targeting healthcare? What TTPs are nation-state actors using against financial institutions? What zero-days are being exploited in our technology stack?). PIR development: align with business risk (crown jewel assets, compliance requirements, board concerns), involve stakeholders (CISO for strategic direction, SOC for tactical needs, IR team for operational playbooks), prioritize by impact and urgency (PIR matrix: high impact + high urgency = priority 1), review quarterly (threat landscape evolves, adjust PIRs accordingly).

Intelligence objectives by level: strategic intelligence (12-18 month horizon, threat landscape trends, emerging threat actors, geopolitical impact on cyber threats, inform executive decisions and long-term investments), tactical intelligence (30-90 day horizon, active campaigns, adversary TTPs, IOCs for current threats, inform SOC detection and hunting), operational intelligence (real-time to 30 days, immediate threat warnings, incident-specific intelligence, response playbooks, inform active incident response).

Threat actor prioritization: nation-state APTs (groups targeting your sector—APT28/29 for government/defense, APT41 for healthcare/tech, Lazarus for financial, long-term persistent threats with sophisticated TTPs), cybercrime groups (financially motivated—ransomware gangs like LockBit/BlackCat, banking trojans like Emotet/TrickBot, shorter attack timelines but higher volume), hacktivists (ideologically motivated, DDoS and defacement, episodic based on current events), insider threats (malicious or negligent employees, hardest to detect via external intelligence, rely on internal indicators).

Intelligence consumers and use cases: SOC analysts (tactical IOCs, detection rules, hunting queries), incident responders (adversary playbooks, TTPs, infrastructure for attribution), vulnerability management (exploited CVEs, weaponized vulnerabilities, prioritization beyond CVSS), risk management (strategic threat assessments, quantitative risk modeling, board reporting), executive leadership (threat landscape briefings, peer breach analysis, investment justification).

**COLLECTION MANAGEMENT**

Gather intelligence from diverse sources. Open source intelligence (OSINT): free and publicly available (VirusTotal for malware samples, Shodan for exposed infrastructure, Twitter/X for real-time threat discussion, security blogs for research, GitHub for leaked credentials and tooling, AlienVault OTX for community IOCs, MISP communities for sharing). Collection approach: automated scrapers for high-volume sources, manual monitoring for specialized forums, keyword alerts for breaking news, attribution via pseudonymous accounts for dark web.

Commercial threat intelligence feeds: vendor selection criteria (coverage of your threat landscape, feed quality and false positive rate, integration with your security stack, analyst support and custom research, pricing model—subscription vs consumption). Leading vendors: Recorded Future (comprehensive coverage, real-time alerts, integration platform), Mandiant Threat Intelligence (APT focus, incident-driven, deep adversary analysis), CrowdStrike Falcon Intelligence (endpoint-focused, malware analysis, adversary tracking), Intel 471 (cybercrime underground, ransomware, carding forums), Flashpoint (physical security convergence, illicit communities). Feed types: structured IOCs (IPs, domains, file hashes, YARA rules), TTPs mapped to MITRE ATT&CK, threat actor profiles and campaigns, vulnerability intelligence, dark web monitoring.

Government and industry sources: government agencies (CISA alerts and advisories, FBI IC3 for cybercrime, NSA/CSS cybersecurity guidance, sector-specific—FinCEN for finance, HHS for healthcare), Information Sharing and Analysis Centers (ISACs) by industry (FS-ISAC for financial services, H-ISAC for healthcare, E-ISAC for energy, IT-ISAC for technology, membership-based, peer sharing, early warning), international agencies (Europol EC3, ENISA for Europe, NCSC for UK, CERT/CC for vulnerabilities).

Internal intelligence sources: own telemetry is most relevant (SIEM logs for attack patterns, EDR telemetry for malware samples, email gateway for phishing campaigns, firewall logs for reconnaissance, DNS logs for C2 communication, honeypots for attacker TTPs, incident post-mortems for lessons learned). Enrichment: correlate internal observations with external intelligence, validate external IOCs against your environment, feedback loop improves collection priorities.

**ANALYSIS AND PROCESSING**

Transform raw data into actionable intelligence. Analysis frameworks: MITRE ATT&CK (TTP categorization, adversary behavior mapping, coverage gap analysis, 14 tactics × 100+ techniques, standard language for sharing), Diamond Model (adversary, capability, infrastructure, victim analysis, pivoting for attribution and expansion), Cyber Kill Chain (reconnaissance → weaponization → delivery → exploitation → installation → C2 → actions on objectives, identify defensive opportunities at each stage), F3EAD (find, fix, finish, exploit, analyze, disseminate—iterative cycle for continuous intelligence operations).

Analytical tradecraft: structured analytic techniques (Analysis of Competing Hypotheses for attribution, Key Assumptions Check to challenge biases, Red Team Analysis to test conclusions, Scenario Development for predictive intelligence), link analysis (connect IOCs to infrastructure to adversaries, visualize relationships with Maltego/i2 Analyst Notebook, identify pivot points for expansion), behavioral analysis (identify adversary patterns beyond IOCs—operational tempo, tooling preferences, target selection, TTP evolution), temporal analysis (timeline of attack activity, identify preparation phases, predict future activity windows).

Confidence assessment methodology: Admiralty Scale for source reliability and information credibility (A = completely reliable source, B = usually reliable, C = fairly reliable... F = reliability cannot be judged; 1 = confirmed by other sources, 2 = probably true, 3 = possibly true... 6 = truth cannot be judged), confidence levels in intelligence products (High confidence >80%: corroborated by multiple independent sources, Medium confidence 50-80%: single credible source or multiple sources with some conflict, Low confidence <50%: uncorroborated, contradictory sources), analytic caveats (state assumptions, identify information gaps, acknowledge alternative explanations).

Indicator analysis and enrichment: IOC validation (verify before dissemination, check false positive history, validate against benign infrastructure), IOC contextualization (who uses this? when was it active? what does it indicate? associated campaigns?), IOC aging (recent IOCs more valuable, implement decay scoring, expire stale indicators), YARA rule development (signature-based detection for malware families, balance specificity vs generality, test against benign corpus).

Campaign and adversary tracking: campaign definition (related activities with shared objective, TTPs, infrastructure, timeframe), adversary profiling (motivations, capabilities, targeting patterns, TTP preferences, infrastructure reuse), campaign evolution tracking (how TTPs change over time, tool adoption, defensive countermeasure adaptation), threat actor attribution (technical attribution via infrastructure/malware, behavioral attribution via TTPs/targeting, confidence levels for attribution claims).

**INTELLIGENCE PRODUCTS AND DELIVERABLES**

Produce intelligence in consumable formats. Strategic intelligence products: quarterly/annual threat landscape reports (macro trends, emerging threats, geopolitical analysis, threat actor evolution, for executive audience), industry-specific threat assessments (peer breach analysis, sector targeting trends, regulatory implications, competitive intelligence on security maturity), risk quantification reports (use FAIR methodology, potential loss estimates, threat probability assessment, ROI for security investments), board-level briefings (business language not technical jargon, risk to business objectives, strategic recommendations, 10-15 minute presentations).

Tactical intelligence products: daily/weekly IOC feeds (machine-readable formats—STIX/TAXII, CSV, JSON, integration with SIEM/EDR/firewalls, automated blocking or alerting), detection rules (SIEM correlation rules, EDR behavioral detections, Snort/Suricata signatures, YARA rules for malware), threat hunting queries (KQL for Sentinel, SPL for Splunk, Lucene for Elastic, hypothesis-driven based on intelligence), adversary infrastructure maps (C2 domains and IPs, malware distribution sites, phishing infrastructure, blocklist candidates).

Operational intelligence products: incident response playbooks (playbook per threat type—ransomware, BEC, DDoS, supply chain, includes TTPs to look for, containment steps, eradication guidance, recovery procedures), adversary emulation plans (purple team exercises, red team scenarios based on real adversary TTPs, test detection coverage), vulnerability intelligence (exploited CVEs in wild, vulnerability-exploit timeline, patch prioritization beyond CVSS, PoC availability), situational awareness alerts (breaking threats, zero-day disclosures, major breaches in sector, immediate action required).

Technical intelligence products: malware analysis reports (static and dynamic analysis, YARA signatures, IOCs, TTPs used, attribution indicators), campaign deep-dives (comprehensive analysis of specific campaign, timeline, infrastructure, victims, adversary profile), indicator packages (curated IOC collections for specific campaigns, context and confidence included, distribution via MISP/ThreatConnect).

**INTELLIGENCE DISSEMINATION AND SHARING**

Distribute intelligence to right stakeholders at right time. Internal distribution strategy: distribution lists by intelligence type and role (strategic to executives monthly, tactical to SOC daily, operational to IR as-needed), delivery mechanisms (email for reports, TIP portal for self-service, SIEM integration for automated IOCs, Slack/Teams for urgent alerts, executive dashboards for metrics), timeliness requirements (strategic can be scheduled, tactical within 24 hours, urgent alerts within 15 minutes).

Traffic Light Protocol (TLP) classification: TLP:CLEAR (public disclosure authorized, can share widely including internet), TLP:GREEN (community sharing, can share with peers and partners, not public internet), TLP:AMBER (limited distribution, recipients only, no further sharing without permission), TLP:AMBER+STRICT (organization only, cannot share externally), TLP:RED (personal only, cannot share with anyone). Usage: mark all intelligence products with appropriate TLP, respect TLP markings on received intelligence, sanitize before elevating TLP (remove attribution/sources to upgrade RED→AMBER).

External intelligence sharing: ISAC participation (active member not passive consumer, contribute intelligence not just consume, attend working groups and conferences, reciprocal sharing builds community), peer sharing arrangements (bilateral agreements with similar organizations, focus on tactical IOCs and campaigns, establish trust before sharing sensitive intelligence), vendor reporting (report novel threats to security vendors, helps entire community, may get free analysis in return), law enforcement coordination (FBI InfraGard program, IC3 reporting for incidents, build relationship before you need them).

Automated intelligence integration: STIX/TAXII for structured sharing (STIX = Structured Threat Information eXpression, TAXII = Trusted Automated eXchange of Indicator Information, standard formats for machine-to-machine sharing), threat intelligence platform (MISP open-source, ThreatConnect commercial, centralized intelligence repository, correlation and enrichment, API for integration), automated IOC import to security tools (SIEM for alerting/correlation, EDR for blocking/detection, firewalls for network blocking, email gateway for phishing prevention, DNS for malicious domain blocking), automated response actions (auto-block known-bad IOCs, auto-isolate on critical alerts, create tickets for investigation).

**INTELLIGENCE PROGRAM OPERATIONS**

Manage ongoing intelligence operations. Intelligence team structure: small org (1-2 analysts, generalist skillset, heavy automation and vendor reliance), medium org (4-6 analysts, specialized by collection/analysis/dissemination, tier 2 threat hunters, manager), large org (10+ analysts, strategic/tactical/operational teams, malware reverse engineers, threat hunters, intelligence developers, director-level leadership). Analyst skills: understanding of adversary tactics, technical skills (networking, OS internals, malware analysis), analytical thinking (structured analysis, critical thinking, hypothesis testing), communication (translate technical to business, written reports, verbal briefings), tools (SIEM, Python for automation, intel platforms, analysis tools).

Collection planning and tasking: collection requirements management (PIRs drive collection priorities, gap analysis identifies missing sources, new requirements from stakeholders), source evaluation (reliability assessment, coverage evaluation, cost-benefit analysis, contract renewals), collection automation (scrapers for OSINT, API integration for feeds, scheduled collection jobs, alerting for high-priority intelligence).

Analysis workflow and quality assurance: standardized analysis process (intake → enrichment → analysis → peer review → dissemination), peer review requirements (second analyst validates high-confidence assessments, manager approval for strategic products, red team review for critical intelligence), quality metrics (timeliness—days from collection to dissemination, accuracy—false positive rate on IOCs, relevance—stakeholder satisfaction surveys, completeness—coverage of PIRs).

Intelligence metrics and program evaluation: effectiveness metrics (threats detected via intelligence before incident, MTTD improvement attributed to intelligence, blocked attacks using IOCs, influenced security decisions), efficiency metrics (intelligence products produced, timeliness by product type, cost per intelligence product, analyst productivity), stakeholder satisfaction (consumer surveys, actionability rating, utilization of products), program maturity (CMM model—initial, repeatable, defined, managed, optimizing, annual assessment and improvement).

Feedback and continuous improvement: consumer feedback loop (post-incident reviews with IR team, SOC feedback on IOC quality, executive feedback on strategic products, adjust priorities and methods), lessons learned process (quarterly review of intelligence successes and failures, what did we miss? what was waste? process improvements documented), threat landscape monitoring (how is threat environment changing? new adversaries? new TTPs? adjust PIRs and collection accordingly), competitive intelligence (what are peers doing for threat intelligence? industry benchmarking, adopt best practices).

Deliver threat intelligence program as:

1. **INTELLIGENCE REQUIREMENTS** - PIRs by stakeholder, threat actor priorities, intelligence consumer matrix

2. **COLLECTION PLAN** - Source inventory (OSINT/commercial/government/internal), collection automation, gap analysis

3. **ANALYSIS FRAMEWORK** - MITRE ATT&CK mapping procedures, analytical methods, confidence assessment methodology

4. **INTELLIGENCE PRODUCTS** - Product catalog (strategic/tactical/operational), templates, production schedule

5. **DISSEMINATION STRATEGY** - Distribution lists, TLP classification guide, automation integration, ISAC participation

6. **TIP IMPLEMENTATION** - Platform selection (MISP/ThreatConnect), data model, API integrations, user access

7. **METRICS FRAMEWORK** - Effectiveness measures, efficiency tracking, stakeholder satisfaction, maturity assessment

---

## Usage Examples

### Example 1: Financial Services Threat Intelligence
**Prompt:** Build threat intelligence for GlobalBank tracking banking trojans, nation-state threats achieving proactive fraud prevention and PCI compliance support.

**Expected Output:** Scope: global financial institution, crown jewels (core banking, SWIFT, customer account databases, ATM network), high-value target for cybercrime and espionage. PIRs: What banking trojans are actively targeting our sector? (Emotet, TrickBot, Zeus variants), What nation-state APTs are conducting financial espionage? (Lazarus, FIN7 evolved to APT), What ATM malware is in circulation? (ATMJackpot, Ploutus, GreenDispenser), What phishing campaigns are impersonating our brand?, What vulnerabilities are being exploited in financial software? (core banking platforms, payment processing). Collection: FS-ISAC membership (threat sharing with 7,000+ financial institutions, daily bulletins, flash alerts for immediate threats), commercial feeds (Recorded Future $250K/year for comprehensive coverage, CrowdStrike $150K for malware intelligence, Intel 471 $100K for cybercrime underground), government (FBI financial crimes division, Secret Service, FinCEN advisories), OSINT (dark web monitoring for card dumps, ransomware leak sites, security researcher blogs), internal (fraud detection system alerts, EDR telemetry from 50K endpoints, SWIFT transaction anomalies). Analysis framework: Diamond Model for adversary attribution (link malware to infrastructure to threat actors), MITRE ATT&CK for technique mapping (T1566 phishing, T1078 valid accounts, T1021 lateral movement), Kill Chain for defensive planning (block at delivery with email security, detect at installation with EDR, respond at C2 with SIEM). Intelligence products: strategic (quarterly board briefing on financial sector threat landscape, peer breach analysis, fraud trends, geopolitical risks to operations), tactical (daily IOC feed with 500-1,000 indicators, SIEM correlation rules for banking trojans, hunting queries for credential theft, phishing domain blocklist), operational (ransomware response playbook tested quarterly, wire fraud incident procedures, insider threat investigation guide, APT response with FBI coordination). Integration: MISP (on-prem for sensitive threat sharing), SIEM integration (Splunk ingests IOCs, auto-creates alerts), EDR blocking (CrowdStrike auto-blocks known-bad hashes), email gateway (Proofpoint blocks phishing domains within 5 minutes of intelligence), fraud system (correlates fraud alerts with threat intelligence on active campaigns). Metrics: 45% of fraud prevented via intelligence (early warning from FS-ISAC), MTTD improved from 30 days to 12 hours (tactical intelligence feeding SOC), 2,000 malicious IPs blocked before attack (proactive blocking). Team: 6 analysts (2 strategic, 3 tactical, 1 malware reverse engineer), $850K annual budget (personnel + commercial feeds + platform).

### Example 2: Healthcare Threat Intelligence
**Prompt:** Build threat intelligence for HealthSystem (8 hospitals, Epic EHR) tracking ransomware gangs, protecting PHI achieving HIPAA compliance and business continuity.

**Expected Output:** Scope: healthcare delivery organization, critical for patient safety (Epic EHR downtime = patient care impact), ransomware primary threat (Ryuk, Conti, BlackCat targeting healthcare 300% increase), PHI valuable on dark web ($250/record vs $1 for credit card). PIRs: Which ransomware gangs are actively targeting healthcare? (BlackCat/ALPHV, LockBit 3.0, Royal, Hive before disruption), What TTPs do they use? (initial access via phishing, privilege escalation via PrintNightmare, lateral movement via RDP, backup deletion before encryption), What vulnerabilities are they exploiting in healthcare environments? (unpatched Windows servers, vulnerable VPN appliances—FortiGate/Pulse Secure, medical device vulnerabilities), What is the ransom demand trend? ($1M-$5M for hospitals, data leak threat if unpaid), How long is typical recovery? (2-4 weeks for full EHR restoration). Collection: H-ISAC membership ($25K annual, healthcare-specific threat sharing, 1,500+ members, ransomware early warnings), commercial (Mandiant $180K for incident-driven intelligence and adversary tracking, Flashpoint $90K for ransomware gang monitoring and leak site tracking), government (HHS 405(d) alerts, FBI healthcare alerts, CISA advisories), OSINT (ransomware leak sites—monitor for healthcare victims and TTPs, medical device vendor advisories, healthcare security forums), internal (Claroty for medical device monitoring—300+ connected devices, EDR logs—25K endpoints, email gateway—phishing attempts 500/day, Epic access logs—unusual PHI access patterns). Analysis: MITRE ATT&CK for Healthcare (ransomware attack chain—T1566.001 spearphishing attachment → T1204.002 user execution → T1486 data encrypted for impact), threat modeling (what if Epic down? manual charting procedures, patient safety risks, financial impact $1M/day), campaign tracking (BlackCat evolution—double extortion, intermittent encryption, VMware ESXi targeting). Intelligence products: strategic (monthly executive briefing—ransomware trends, peer breach lessons learned, cyber insurance implications, board presentation quarterly with business continuity impact), tactical (daily IOC feed—ransomware infrastructure, Snort rules for ransomware C2 protocols, YARA rules for ransomware families, phishing domain blocklist), operational (ransomware playbook—isolate infected systems, activate Epic downtime procedures, notify HHS within 60 days if PHI breach, FBI notification, forensic investigation, backup restoration from immutable storage, lessons learned). Dissemination: TLP:AMBER internal distribution (cannot share PHI context externally), TLP:GREEN for H-ISAC (sanitized IOCs and TTPs), ransomware alerts within 15 minutes to all IT staff, monthly newsletter to clinical leadership (patient safety focus). Integration: Microsoft Sentinel ($400K annual, HIPAA-compliant log retention), Defender for Endpoint (auto-quarantine on ransomware behavior), Veeam immutable backups (ransomware cannot encrypt), network segmentation (medical device VLANs isolated, cannot spread to business network). Outcomes: zero successful ransomware incidents (3 attempts detected and blocked via intelligence), PHI breach prevention ($1.5M+ potential OCR fines avoided), 75% reduction in phishing click rate (intelligence-driven training on active campaigns). Team: 3 analysts (1 strategic, 1 tactical, 1 split with IR), $450K budget (lean operation, heavy MSSP reliance).

### Example 3: Critical Infrastructure (Energy)
**Prompt:** Build threat intelligence for PowerGrid Utility tracking nation-state OT attacks, protecting SCADA/ICS achieving NERC CIP compliance and grid resilience.

**Expected Output:** Scope: power generation and distribution, 15 substations + control center SCADA, nation-state threat (Sandworm/ELECTRUM responsible for Ukraine grid attacks, CHERNOVITE targeting US grid, Volt Typhoon pre-positioning for disruption), regulatory (NERC CIP-008 incident reporting, CIP-013 supply chain risk management). PIRs: What nation-state actors are targeting North American energy sector? (Russia—Sandworm persistent, China—Volt Typhoon living-off-the-land, Iran—increasing capability), What ICS-specific malware exists? (Industroyer/CrashOverride for substation protocols, TRITON for safety systems, Pipedream modular ICS attack framework, COSMICENERGY circuit breaker manipulation), What are the TTPs for OT intrusion? (IT-to-OT pivot via poorly segmented networks, engineering workstation compromise, supply chain—vendor remote access, living-off-the-land to evade detection), What supply chain risks exist? (compromised firmware updates, malicious field devices, vendor access credentials), What geopolitical events correlate with attacks? (Ukraine conflict, Middle East tensions, US-China relations). Collection: E-ISAC (Electricity ISAC, 1,000+ utilities, threat sharing, tabletop exercises, government liaisons), Dragos ($200K annual, ICS threat intelligence leader, WorldView platform, vulnerability research), CISA ICS-CERT (free advisories, ICS-focused CVEs, incident response support), DOE (energy sector alerts, classified briefings for threats), OSINT (ICS security research, vendor advisories—Siemens/Schneider/ABB, academic papers on ICS attacks), internal (SCADA historian data, OT network traffic via Nozomi, IT/OT boundary monitoring, supply chain vendor assessments). Analysis: MITRE ATT&CK for ICS (12 tactics specific to OT—initial access via engineering workstation, execution via scripting in HMI, persistence via system firmware, lateral movement via OT protocols), OT threat modeling (attack impact—generation capacity loss, transmission disruption, physical damage to equipment, cascading failures, public safety), ICS kill chain adapted (reconnaissance of ICS, intrusion into enterprise, pivot to OT, discovery of control systems, development of attack, deployment and execution, physical impact). Intelligence products: strategic (quarterly threat landscape for executive and board—geopolitical analysis, nation-state capability assessment, risk to grid operations, NERC CIP alignment, investment requirements for OT security), tactical (IOC feeds for IT/OT boundary—Snort/Suricata rules for ICS protocols, YARA for ICS malware, malicious IP blocklist, domain reputation), operational (ICS incident response plan—OT-specific forensics, grid stability during response, vendor coordination, physical security integration, DOE/NERC notification, public communications). Integration: challenges (air-gapped OT networks, cannot install agents on legacy SCADA, passive monitoring only), solution (Nozomi for network visibility $180K, unidirectional gateways IT→OT data flow only, threat intelligence consumed at IT/OT boundary, manual processes for high-side OT network). Sharing: E-ISAC TLP:AMBER (sensitive infrastructure information, limited to energy sector), classified briefings with DOE/FBI (nation-state attribution, government response coordination), regional grid operator sharing (mutual aid during incidents). Compliance: NERC CIP-008 incident reporting (within 1 hour for critical, threat intelligence supports detection), CIP-013 supply chain plan (vendor risk assessments using threat intelligence on compromised vendors). Outcomes: detected Chinese APT reconnaissance (Volt Typhoon, removed before OT access), prevented vendor remote access compromise (intelligence on credential theft campaign), passed NERC audit with zero findings. Team: 2 analysts (1 strategic covering geopolitical, 1 tactical covering IOCs), plus OT engineers with security training, $350K budget (lean, government sources supplement commercial).

---

## Cross-References

- [Security Operations](security-operations.md) - SOC integration with threat intelligence
- [SIEM & Security Monitoring](../Security-Operations/siem-security-monitoring.md) - IOC integration and correlation
- [Incident Response](incident-response.md) - Intelligence-driven incident response
