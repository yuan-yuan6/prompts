---
title: Security Assessment Framework
category: security
tags:
- security
- security-assessment
- vulnerability-scanning
- risk-analysis
use_cases:
- Conducting comprehensive security assessments with vulnerability scanning, penetration testing, control reviews achieving risk-based remediation prioritization
- Performing compliance-driven security audits for PCI-DSS, HIPAA, SOC 2 including threat modeling, CVSS scoring, remediation roadmaps
- Red team exercises simulating advanced persistent threats with MITRE ATT&CK-mapped techniques, privilege escalation, lateral movement testing
related_templates:
- security/Security-Operations/penetration-testing.md
- security/Security-Operations/vulnerability-management.md
- security/Cybersecurity/security-operations.md
industries:
- technology
- financial-services
- healthcare
- government
- retail
type: framework
difficulty: intermediate
slug: security-assessment
---

# Security Assessment Framework

## Purpose
Conduct comprehensive security assessments covering threat modeling, vulnerability scanning, penetration testing, security control review, and risk analysis achieving prioritized remediation roadmaps aligned with business impact and compliance requirements.

## 🚀 Quick Security Assessment Prompt

> Conduct security assessment for **[SYSTEM]** covering **[SCOPE]** (infrastructure/web app/API/cloud). Methodology: **[NIST/OWASP/PTES]**. Activities: asset inventory, threat modeling, vulnerability scanning **[TOOLS]**, penetration testing **[OWASP_TOP_10/MITRE_ATT&CK]**, control review **[FRAMEWORK]**. Prioritize by **[CVSS + BUSINESS_IMPACT]**. Compliance: **[PCI/HIPAA/SOC2]**. Deliverables: executive summary, detailed findings with POCs, remediation roadmap.

---

## Template

Conduct security assessment for {TARGET_SYSTEM} covering {ASSESSMENT_SCOPE} using {METHODOLOGY} achieving {COMPLIANCE_REQUIREMENTS} validation with {TIMELINE} schedule.

**ASSESSMENT PLANNING AND SCOPING**

Define clear assessment boundaries and objectives. Scope definition: target systems (IP ranges, domains, applications in scope), explicitly list out-of-scope systems (production databases with live data, third-party services, critical infrastructure), assessment type (vulnerability assessment, penetration testing, red team exercise, compliance audit), testing window (dates, times, blackout periods for critical operations). Assessment methodology: NIST SP 800-115 (technical security testing), OWASP Testing Guide (web application security), PTES (Penetration Testing Execution Standard), OSSTMM (Open Source Security Testing Methodology Manual), industry-specific (PCI-DSS ASV scanning, HIPAA Security Rule assessment).

Rules of engagement: authorized activities (network scanning, exploitation, social engineering), prohibited activities (DoS attacks, data destruction, physical security testing unless authorized), notification procedures (emergency contact for critical findings, daily status updates), documentation requirements (evidence collection, chain of custody, report format). Stakeholder alignment: CISO/security leadership (assessment objectives, risk appetite), system owners (maintenance windows, known issues), compliance team (regulatory requirements, control mapping), legal (authorization, liability, breach notification).

**THREAT MODELING AND RISK ANALYSIS**

Identify threats relevant to the target environment. Asset identification: critical systems and data (customer PII databases, payment processing, intellectual property, authentication systems), supporting infrastructure (Active Directory, cloud control plane, network devices), third-party dependencies (APIs, cloud services, SaaS applications). Threat actors: external attackers (financially motivated cybercriminals, nation-state APTs, hacktivists), insiders (disgruntled employees, negligent users, contractors), supply chain threats (compromised vendors, malicious updates).

Attack vectors and scenarios: internet-facing applications (SQL injection, XSS, authentication bypass), network infrastructure (VPN vulnerabilities, firewall misconfigurations, unpatched services), cloud services (IAM misconfigurations, public S3 buckets, insecure APIs), social engineering (phishing, pretexting, physical access), supply chain (dependency vulnerabilities, compromised build pipeline). Attack surface mapping: external perimeter (public IPs, domains, exposed services), internal network (flat networks, lateral movement paths), cloud attack surface (public endpoints, IAM policies, storage permissions), application layer (authentication endpoints, file upload, API endpoints).

Risk rating methodology: CVSS scoring (base score for severity, environmental score for context, temporal score for exploit availability), business impact (data sensitivity, system criticality, regulatory consequences), exploitability (attack complexity, required privileges, user interaction), likelihood (threat actor capability, attack surface exposure, existing controls). Risk prioritization: Critical (high CVSS + high business impact + exploitable), High (high CVSS or high business impact), Medium (moderate severity with mitigating factors), Low (minimal impact or difficult to exploit).

**VULNERABILITY ASSESSMENT**

Systematically identify security weaknesses. Scanning approach: external scanning (unauthenticated scans of internet-facing systems, simulate external attacker perspective), internal scanning (authenticated scans with credentials, deeper vulnerability detection), credentialed scans (Windows domain credentials, Linux SSH keys, cloud API keys for comprehensive coverage). Scanning tools: network scanners (Nessus Professional, Qualys VMDR, OpenVAS), web application scanners (Burp Suite Professional, OWASP ZAP, Acunetix), cloud scanners (ScoutSuite, Prowler, Cloud Custodian), container scanners (Trivy, Snyk, Aqua).

Vulnerability categories: infrastructure vulnerabilities (unpatched systems, misconfigurations, weak protocols), web application vulnerabilities (OWASP Top 10—injection, broken authentication, sensitive data exposure), API vulnerabilities (broken object level authorization, excessive data exposure, lack of rate limiting), cloud misconfigurations (public storage, overprivileged IAM, unencrypted data), container vulnerabilities (vulnerable base images, privileged containers, secrets in images).

False positive analysis and validation: verify scanner findings manually (confirm exploitability, validate impact), eliminate false positives (scanner misinterpretations, business exceptions, acceptable risks), document true positives with evidence (screenshots, proof-of-concept commands, affected versions). CVSS scoring with context: use CVSS 3.1 base score as starting point, adjust environmental score (confidentiality/integrity/availability requirements), factor in compensating controls (WAF protecting vulnerable app, network segmentation limiting exposure).

**PENETRATION TESTING**

Validate vulnerabilities through controlled exploitation. Testing methodology: black-box (no prior knowledge, simulates external attacker), gray-box (limited credentials, simulates compromised user), white-box (full access to source code and architecture, maximum coverage). Testing phases: reconnaissance (OSINT, subdomain enumeration, service fingerprinting), scanning (port scanning, vulnerability identification, service enumeration), exploitation (validate vulnerabilities, gain access, demonstrate impact), post-exploitation (privilege escalation, lateral movement, persistence, data access).

Exploitation techniques: web application attacks (SQL injection for data extraction, XSS for session hijacking, SSRF for internal network access, deserialization for RCE), network attacks (credential attacks, man-in-the-middle, protocol abuse), privilege escalation (kernel exploits, SUID binaries, sudo misconfigurations, Windows privilege escalation), Active Directory attacks (Kerberoasting, AS-REP roasting, DCSync, Golden Ticket), cloud exploitation (IAM privilege escalation, metadata service abuse, storage enumeration).

Attack chain demonstration: initial access (exploit internet-facing vulnerability, phishing simulation), execution (deploy web shell, reverse shell, command execution), persistence (create backdoor accounts, scheduled tasks, registry modifications), privilege escalation (local admin → domain admin → enterprise admin), lateral movement (pass-the-hash, RDP pivoting, WMI execution), data access (database access, file share enumeration, cloud storage), exfiltration (demonstrate data extraction path, don't actually exfiltrate sensitive data).

Evidence collection: screenshot every step, capture network traffic (Wireshark, tcpdump), save command output, document proof-of-concept exploits, record video for complex attack chains. Impact assessment: demonstrate business impact (access to customer data, financial systems, ability to disrupt operations), quantify scope (number of records accessible, systems compromised), identify compliance implications (PCI breach, HIPAA violation, GDPR data exposure).

**SECURITY CONTROLS REVIEW**

Assess effectiveness of existing security controls. Control framework alignment: NIST Cybersecurity Framework (Identify, Protect, Detect, Respond, Recover), CIS Controls v8 (18 critical security controls), ISO 27001 Annex A (114 controls across 14 domains), NIST SP 800-53 (security and privacy controls for federal systems), industry-specific (PCI-DSS, HIPAA Security Rule, SOC 2 trust service criteria).

Control categories: preventive controls (firewalls, encryption, access controls, DLP), detective controls (IDS/IPS, SIEM, vulnerability scanning, log monitoring), corrective controls (patching, incident response, backup restoration), administrative controls (policies, procedures, training, background checks), technical controls (authentication, authorization, encryption, audit logging), physical controls (badge access, CCTV, environmental controls).

Control effectiveness assessment: control existence (is the control implemented?), control design (is it designed correctly for the threat?), control operation (does it operate as intended?), coverage (does it cover all relevant assets/scenarios?). Control testing: configuration review (examine firewall rules, IAM policies, network segmentation), log analysis (verify logging enabled and retained, review access logs), interview personnel (understand procedures, verify awareness), observe operations (witness incident response, watch patching process).

Control gaps and recommendations: identify missing controls (no network segmentation, no MFA, insufficient logging), assess weak controls (outdated antivirus, infrequent patching, excessive permissions), recommend improvements (deploy EDR, implement least privilege, enable audit logging), prioritize by risk reduction (address high-risk gaps first, quick wins vs long-term projects).

**REMEDIATION PLANNING**

Develop actionable remediation roadmap. Finding prioritization: risk-based ranking (CVSS + business impact + exploitability + compliance), quick wins (high impact, low effort fixes first), compliance-driven (PCI critical findings before medium internal findings), dependency consideration (patch OS before applications, fix authentication before other web app issues).

Remediation timeline by severity: Critical (24-48 hours for exploited vulnerabilities, 7 days otherwise), High (7-14 days with compensating controls if delayed), Medium (30 days standard timeline), Low (90 days or next maintenance window). Compensating controls: temporary mitigations until patch available (WAF rules, network segmentation, enhanced monitoring), risk acceptance documentation (business justification, approval, expiration date), alternative solutions (upgrade to supported version, implement different technology).

Remediation tracking: assign ownership (IT for infrastructure, dev team for applications, cloud team for AWS/Azure), set deadlines (based on severity SLAs), require evidence (post-patch scan results, configuration screenshots, validation testing), track exceptions (approved risk acceptances, time-bound with regular review). Validation and retest: verify fixes (rescan after remediation, retest exploits), confirm no regression (didn't break functionality, didn't introduce new issues), document closure (before/after evidence, lessons learned).

Deliver security assessment as:

1. **EXECUTIVE SUMMARY** - Overall risk posture, critical findings (top 5), business impact, recommended immediate actions

2. **THREAT MODEL** - Asset inventory, threat actors, attack scenarios, risk ratings, attack surface map

3. **VULNERABILITY REPORT** - Detailed findings by severity, CVSS scores, affected systems, proof-of-concept, remediation steps

4. **PENETRATION TEST RESULTS** - Attack chains demonstrated, systems compromised, data accessed, evidence (screenshots, commands)

5. **CONTROL ASSESSMENT** - Control effectiveness by framework, gaps identified, recommendations prioritized

6. **REMEDIATION ROADMAP** - Prioritized action items, ownership, timeline, compensating controls, success metrics

---

## Usage Examples

### Example 1: E-Commerce Web Application Assessment
**Prompt:** Conduct security assessment for CustomerShop e-commerce platform covering OWASP Top 10 vulnerabilities with PCI-DSS compliance validation.

**Expected Output:** Scope: CustomerShop web app (www.customershop.com, admin.customershop.com, api.customershop.com), React frontend + Node.js backend + PostgreSQL, payment processing via Stripe integration. Methodology: OWASP Testing Guide v4.2 for web app, PCI-DSS 4.0 for compliance controls. Timeline: 3 weeks (1 week scanning + 1 week testing + 1 week reporting). Threat model: financially motivated attackers targeting customer PII and payment data, insider threats (admin account compromise), attack vectors (SQL injection, XSS, authentication bypass, payment form tampering). Vulnerability assessment: Burp Suite Pro scan found 23 findings (3 critical, 8 high, 12 medium), critical findings (SQL injection in product search, stored XSS in product reviews, session fixation in login), authenticated scans with test account credentials. Penetration testing: exploited SQL injection → extracted 50K customer records (test data), XSS → session hijacking proof-of-concept, authentication bypass → accessed admin panel, demonstrated PCI scope breach (could access cardholder data environment). Controls review: PCI-DSS Requirement 6 (secure coding practices—failed due to SQL injection), Requirement 10 (logging—insufficient for PCI), Requirement 11 (vulnerability scanning—compliant with quarterly scans). Remediation: Critical (parameterized queries for SQLi, input validation + output encoding for XSS, fix session management) 7 days, High (implement rate limiting, enhance logging, deploy WAF) 14 days, Medium (security headers, CSRF tokens, upgrade libraries) 30 days. Compliance: cannot pass PCI-DSS ASV scan until critical/high fixed, quarterly rescan required.

### Example 2: Cloud Infrastructure Assessment (AWS)
**Prompt:** Conduct security assessment for FinTech company AWS infrastructure covering 3 accounts (production, staging, development) with SOC 2 compliance focus.

**Expected Output:** Scope: AWS accounts (prod-123456, stage-789012, dev-345678), all regions, EC2 instances (50), RDS databases (10), S3 buckets (200), Lambda functions (100), IAM users/roles (500). Methodology: NIST SP 800-115 for technical testing, AWS Well-Architected Security Pillar, CIS AWS Foundations Benchmark. Timeline: 2 weeks (5 days scanning + 5 days manual testing + 4 days reporting). Threat model: external attackers exploiting misconfigured services, insider threats with overprivileged IAM, nation-state targeting financial data. Attack surface: 15 public S3 buckets, 5 internet-facing EC2 instances, API Gateway endpoints (10), RDS publicly accessible (2 databases). Vulnerability assessment: ScoutSuite + Prowler found 89 findings (12 critical, 31 high, 46 medium), critical findings (S3 bucket public read on customer data, RDS snapshot public, IAM user with admin wildcard permissions, security group 0.0.0.0/0 on SSH). Penetration testing: accessed public S3 bucket with customer PII (10K records), downloaded public RDS snapshot (staging database copy), exploited overprivileged Lambda role → privilege escalation to admin, demonstrated cross-account access via misconfigured assume role. Controls review: SOC 2 CC6.1 (logical access)—failed due to overprivileged IAM, CC6.6 (encryption)—partial (S3 encrypted but RDS not), CC6.8 (vulnerability management)—no continuous scanning. Remediation: Critical (block public S3, remove public RDS snapshots, revoke wildcard IAM) 24 hours, High (implement least-privilege IAM, enable GuardDuty, enable CloudTrail all regions) 7 days, Medium (enable S3 versioning, RDS encryption, VPC Flow Logs) 30 days. Compliance: SOC 2 audit at risk until IAM and encryption issues resolved, automated compliance (AWS Config rules for CIS benchmark).

### Example 3: Red Team Exercise for Financial Services
**Prompt:** Conduct red team exercise for Bank Corp simulating advanced persistent threat targeting customer financial data and wire transfer systems.

**Expected Output:** Scope: full organization (external perimeter, internal network, cloud, social engineering authorized), objective-based (access customer accounts, manipulate wire transfers, exfiltrate financial records). Methodology: MITRE ATT&CK framework, assume breach + external attack, 4-week engagement with weekly checkpoints. Threat model: nation-state APT (high sophistication, persistent, stealthy), targeting financial data for espionage, wire transfer manipulation for financial gain. Attack chain: initial access (phishing campaign → 15% click rate, 5% credential harvest), execution (deployed Cobalt Strike beacon on finance workstation), persistence (scheduled task + registry run key), privilege escalation (Kerberoasting → service account compromise → domain admin in 48 hours), lateral movement (pass-the-hash across finance department, RDP to server subnet), discovery (BloodHound for AD enumeration, identified path to wire transfer system), credential access (mimikatz for LSASS dump, obtained DBA credentials), collection (accessed customer account database—5M records, wire transfer system—read-only access), exfiltration (demonstrated HTTPS exfil to Dropbox, didn't actually exfiltrate). Findings: achieved domain admin in 48 hours, accessed customer financial data (PCI/GLBA violation), wire transfer system accessible but transfer controls prevented unauthorized transactions, no detection by EDR/SIEM for 2 weeks (poor tuning). Controls tested: email security (failed—phishing successful), EDR (failed—Cobalt Strike not detected), network segmentation (failed—flat network allowed lateral movement), privileged access (failed—no PAM, shared admin accounts), monitoring (partial—SIEM had logs but no alerting). Recommendations: deploy phishing-resistant MFA, implement network micro-segmentation, deploy PAM solution (CyberArk/BeyondTrust), enhance EDR with behavioral analytics, purple team exercises to tune detection, privileged access workstations for admin tasks.

---

## Cross-References

- [Penetration Testing](../Security-Operations/penetration-testing.md) - Detailed penetration testing methodology
- [Vulnerability Management](../Security-Operations/vulnerability-management.md) - Ongoing vulnerability program
- [Security Operations](security-operations.md) - SOC integration with assessment findings
