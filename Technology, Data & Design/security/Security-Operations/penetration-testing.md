---
category: security
title: Penetration Testing Framework
tags:
- security
- penetration-testing
- red-team
- exploitation
use_cases:
- Planning and executing penetration tests for web applications, infrastructure, APIs, and cloud environments with PTES methodology
- Conducting compliance-driven security assessments for PCI-DSS (annual/quarterly), HIPAA technical safeguards, and SOC 2 validation
- Red team exercises simulating advanced persistent threats with phased attack chains and lateral movement testing
related_templates:
- security/Cybersecurity/security-assessment.md
- security/Application-Security/secure-code-review.md
- security/Security-Operations/vulnerability-management.md
industries:
- technology
- financial-services
- healthcare
- government
type: framework
difficulty: intermediate
slug: penetration-testing
---

# Penetration Testing Framework

## Purpose
Plan and execute penetration tests covering scope definition, reconnaissance, vulnerability discovery, exploitation, post-exploitation, and reporting with actionable remediation guidance achieving security validation and compliance requirements.

## 🚀 Quick Penetration Testing Prompt

> Plan penetration test for **[ORGANIZATION]** targeting **[SCOPE]** (web apps/infrastructure/APIs/cloud). Type: **[BLACK-BOX/GRAY-BOX/WHITE-BOX]**. Focus: **[OWASP_TOP_10/NETWORK/CLOUD]**. Window: **[DATES]**. Methodology: **[PTES/OWASP_TG]**. Deliverables: executive summary, technical findings with POCs, CVSS scores, remediation priority. Compliance: **[PCI-DSS/HIPAA/SOC2]**.

---

## Template

Execute penetration test for {ORGANIZATION} targeting {SCOPE} using {TEST_TYPE} methodology achieving {COMPLIANCE_REQUIREMENTS} validation with {TIMELINE} timeline.

**ENGAGEMENT PLANNING**

Define scope and rules of engagement before testing begins. Scope definition: specific IP ranges, domains, and applications in scope, explicitly list out-of-scope systems (production databases, third-party services, specific hosts), testing window with start/end dates and times. Test type selection: black-box (no prior knowledge, simulates external attacker), gray-box (limited credentials, simulates compromised user), white-box (full access to source code and architecture, deepest coverage). Authorization: written authorization from asset owner required, emergency contact list for critical issues, communication protocols for discovered critical vulnerabilities. Rules of engagement: no denial-of-service testing unless explicitly approved, no social engineering unless in scope, no physical access testing unless authorized, data handling requirements for discovered sensitive information.

**RECONNAISSANCE AND INFORMATION GATHERING**

Passive reconnaissance without touching target systems. OSINT: domain enumeration (WHOIS, DNS records, certificate transparency logs), employee discovery (LinkedIn, organizational charts), technology stack identification (Wappalyzer, BuiltWith), leaked credentials (breach databases, paste sites), previous vulnerability disclosures (CVE databases, bug bounty reports). Infrastructure mapping: subdomain enumeration (Subfinder, Amass, certificate transparency), IP range identification (BGP, ASN lookups), cloud asset discovery (bucket enumeration, API endpoints).

Active reconnaissance touching target systems. Network scanning: port scanning (Nmap, Masscan), service identification and version detection, operating system fingerprinting. Web reconnaissance: directory and file enumeration (Gobuster, Feroxbuster), parameter discovery, API endpoint mapping. Technology fingerprinting: web server identification, framework detection, CMS version identification, database technology inference.

**VULNERABILITY DISCOVERY**

Automated scanning for broad coverage. Infrastructure scanning: vulnerability scanners (Nessus, Qualys, OpenVAS), authenticated and unauthenticated scans, configuration assessment. Web application scanning: DAST tools (Burp Suite, OWASP ZAP), API scanning, authenticated crawling. Cloud assessment: cloud-native scanners (AWS Inspector, Azure Defender, ScoutSuite), IAM policy analysis, storage misconfiguration detection.

Manual testing for depth and business logic. Authentication testing: password policy enforcement, brute force protection, multi-factor bypass, session management weaknesses. Authorization testing: horizontal privilege escalation (access other users' data), vertical privilege escalation (access admin functions), IDOR vulnerabilities. Input validation: SQL injection (SQLi), cross-site scripting (XSS), command injection, XML external entity (XXE), server-side request forgery (SSRF). Business logic: workflow bypass, race conditions, price manipulation, function abuse.

**EXPLOITATION**

Validate vulnerabilities through controlled exploitation. Exploitation approach: verify vulnerability is exploitable (not just theoretical), document proof-of-concept with minimal impact, capture evidence (screenshots, request/response, command output), assess actual impact (data access, privilege level, pivot potential). Common exploitation vectors: SQL injection (data extraction, authentication bypass, command execution), XSS (session hijacking, credential theft, phishing), authentication bypass (direct access, token manipulation, logic flaws), remote code execution (web shell, reverse shell, command injection), privilege escalation (kernel exploits, misconfigured services, credential reuse).

Tool selection: Burp Suite Professional (web application testing), SQLmap (SQL injection automation), Metasploit (exploitation framework), custom scripts (application-specific exploitation). Evidence capture: request/response pairs, command output, screenshots, video recordings for complex attacks.

**POST-EXPLOITATION**

Assess impact of successful exploitation. Privilege escalation: local privilege escalation (kernel exploits, SUID binaries, sudo misconfigurations), domain privilege escalation (Kerberoasting, AS-REP roasting, DCSync), cloud privilege escalation (IAM policy abuse, metadata service exploitation). Lateral movement: credential harvesting (memory, files, registry), network pivoting to internal systems, trust relationship exploitation. Data access: identify accessible sensitive data (PII, credentials, financial data), demonstrate data exfiltration path, document compliance-relevant findings. Persistence: identify persistence mechanisms available (not always establish), document potential attack chains.

**REPORTING**

Structure findings for different audiences. Executive summary: overall security posture assessment, risk level (critical/high/medium/low), top 3-5 most impactful findings, business risk translation, recommended immediate actions. Technical findings: vulnerability description and classification (CWE, OWASP category), affected systems and URLs, CVSS score with vector string, step-by-step proof-of-concept, evidence (screenshots, requests, commands), root cause analysis. Remediation guidance: specific remediation steps for developers/administrators, code examples where applicable, compensating controls if immediate fix not possible, verification steps to confirm remediation.

Finding classification: Critical (remote code execution, authentication bypass, complete data access), High (privilege escalation, sensitive data exposure, stored XSS), Medium (reflected XSS, CSRF on important functions, information disclosure), Low (missing headers, information leakage with minimal impact, self-XSS).

**COMPLIANCE-SPECIFIC TESTING**

Tailor testing to compliance requirements. PCI-DSS: annual penetration test covering internal and external, segmentation testing validating network isolation, re-test after significant changes, quarterly external vulnerability scans by ASV. HIPAA: technical safeguards validation (access controls, audit controls, integrity controls, transmission security), ePHI access testing, encryption verification. SOC 2: security control validation, access control testing, change management verification, monitoring and logging assessment.

Deliver penetration test as:

1. **ENGAGEMENT SUMMARY** - Scope, methodology, timeline, key statistics (hosts tested, vulnerabilities found)

2. **EXECUTIVE REPORT** - Risk summary, critical findings, business impact, strategic recommendations

3. **TECHNICAL FINDINGS** - Detailed vulnerability descriptions, CVSS scores, POCs, evidence

4. **REMEDIATION MATRIX** - Prioritized findings by risk, remediation owner, effort estimate, timeline

5. **RETEST SCOPE** - Vulnerabilities requiring validation after remediation

---

## Usage Examples

### Example 1: E-Commerce Web Application
**Prompt:** Execute penetration test for ShopCorp e-commerce platform (www.shopcorp.com) including web application, APIs, and payment processing achieving PCI-DSS compliance validation.

**Expected Output:** Scope: www.shopcorp.com, api.shopcorp.com, admin.shopcorp.com, payment gateway integration, mobile API endpoints. Test type: gray-box (customer account provided, admin account for authorized testing). Methodology: OWASP Testing Guide v4.2 for web application, PTES for infrastructure. Focus areas: OWASP Top 10, payment flow security, authentication/session management, API security, PCI CDE isolation. Timeline: 2 weeks (40 hours testing, 8 hours reporting). Findings example: Critical—SQL injection in product search allowing database extraction (CVSS 9.8), High—stored XSS in product reviews affecting all customers (CVSS 8.1), High—IDOR allowing access to other customers' order history (CVSS 7.5), Medium—missing rate limiting on login allowing brute force (CVSS 5.3), Low—missing security headers (CVSS 3.1). Remediation: parameterized queries for SQLi, input validation and output encoding for XSS, authorization checks for IDOR, rate limiting with account lockout for brute force. PCI compliance: segmentation testing passed, no critical/high findings in CDE after remediation, quarterly ASV scan scheduled.

### Example 2: Cloud Infrastructure Assessment
**Prompt:** Execute penetration test for TechCorp AWS infrastructure (3 accounts: production, staging, development) including IAM, S3, EC2, Lambda, and API Gateway.

**Expected Output:** Scope: AWS accounts (prod-123456, stage-789012, dev-345678), all regions, IAM policies, S3 buckets, EC2 instances, Lambda functions, API Gateway endpoints. Test type: white-box (ReadOnly IAM access provided for policy analysis, limited credentials for exploitation testing). Methodology: cloud-specific testing (AWS penetration testing policy compliance), ScoutSuite for configuration assessment, manual exploitation testing. Focus areas: IAM privilege escalation, S3 bucket misconfigurations, EC2 security groups, Lambda function vulnerabilities, API Gateway authentication. Timeline: 2 weeks (focus on prod account). Findings example: Critical—overly permissive IAM role allowing privilege escalation to admin (CVSS 9.1), High—S3 bucket with customer data accessible via misconfigured bucket policy (CVSS 8.6), High—EC2 instance metadata service v1 enabling SSRF to credential theft (CVSS 7.5), Medium—Lambda function with hardcoded API keys (CVSS 6.5), Medium—development account credentials with production access (CVSS 6.1). Remediation: least-privilege IAM policies, S3 bucket policies with explicit deny, IMDSv2 enforcement, secrets manager for Lambda, account boundary enforcement.

### Example 3: Financial Services Red Team
**Prompt:** Execute red team engagement for FinanceBank simulating advanced persistent threat targeting customer financial data and trading systems.

**Expected Output:** Scope: full organization (external perimeter, internal network, cloud, social engineering authorized), objective-based (access trading systems, exfiltrate customer PII, demonstrate wire transfer manipulation). Test type: assumed breach + external attack, black-box for external, gray-box for internal (compromised employee workstation). Methodology: MITRE ATT&CK framework, phased approach with weekly objective checkpoints. Attack phases: initial access (phishing campaign targeting finance team, external vulnerability exploitation), execution (malware deployment on compromised workstations), persistence (scheduled tasks, registry run keys), privilege escalation (Kerberoasting, credential dumping), lateral movement (RDP, SMB, WMI), collection (database access, file share enumeration), exfiltration (HTTPS to attacker infrastructure). Timeline: 4 weeks with purple team debrief. Findings: phishing success rate 12% (6/50 targets clicked, 3 provided credentials), domain admin achieved in 72 hours via Kerberoasting, trading system access achieved (read-only, no modification attempted), customer PII (100K records) accessible via compromised database, wire transfer system accessible but controls prevented unauthorized transfer. Recommendations: phishing-resistant MFA, privileged access workstations, network segmentation between trading and corporate, enhanced monitoring for lateral movement TTPs.

---

## Cross-References

- [Vulnerability Management](vulnerability-management.md) - Integration with ongoing vulnerability program
- [Security Assessment](../Cybersecurity/security-assessment.md) - Broader security assessment context
- [Secure Code Review](../Application-Security/secure-code-review.md) - Complementary code-level security review
