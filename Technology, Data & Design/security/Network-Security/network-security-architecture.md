---
category: security
title: Network Security Architecture
tags:
- security
- network-security
- firewall
- segmentation
use_cases:
- Designing secure network architectures with defense-in-depth implementing micro-segmentation, NGFW, and IDS/IPS achieving PCI-DSS/HIPAA compliance
- Modernizing legacy flat networks to zero trust with software-defined perimeter, SASE, and identity-based access replacing VPN-centric security
- Implementing network security for hybrid multi-cloud environments with consistent policy enforcement across on-premises, AWS, Azure, and GCP
related_templates:
- security/Cloud-Security/cloud-security-architecture.md
- security/Identity-Access-Management/zero-trust-architecture.md
- security/Identity-Access-Management/privileged-access-management.md
industries:
- technology
- financial-services
- healthcare
- government
- retail
type: framework
difficulty: intermediate
slug: network-security-architecture
---

# Network Security Architecture

## Purpose
Design and implement secure network architectures with defense-in-depth, micro-segmentation, firewall policies, IDS/IPS, secure remote access, and zero trust networking achieving regulatory compliance and protection against lateral movement.

## 🚀 Quick Network Security Prompt

> Design network security for **[ORGANIZATION]** with **[LOCATIONS]** sites, **[USERS]** users, **[INFRASTRUCTURE]** (on-prem/cloud/hybrid). Segmentation: **[ZONES]** (DMZ, internal, PCI, IoT). Controls: NGFW (**[VENDOR]**), IDS/IPS (**[PLATFORM]**), NAC (**[802.1X/PROFILING]**). Remote access: **[VPN/ZTNA/SASE]**. Monitoring: flow analysis, **[NDR]**, SIEM integration. Compliance: **[PCI-DSS/HIPAA/SOC2]**. Target: zero implicit trust, encrypted everywhere, <1 min detection.

---

## Template

Design network security architecture for {ORGANIZATION} with {NETWORK_SIZE} users across {LOCATIONS} achieving {COMPLIANCE_REQUIREMENTS} compliance with {ARCHITECTURE_MODEL} security model.

**NETWORK SEGMENTATION**

Design zones based on data sensitivity and compliance requirements. Zone architecture: internet-facing DMZ (web servers, reverse proxies, API gateways), internal zones by function (corporate, development, production), high-security zones (PCI cardholder data environment, PHI systems, privileged access), specialized zones (IoT/OT isolated, guest wireless, partner extranet). Micro-segmentation: move beyond VLAN-based to workload-level using software-defined (VMware NSX, Cisco ACI, Illumio), cloud-native (AWS Security Groups, Azure NSGs, GCP Firewall Rules), or host-based firewalls. Segmentation enforcement: default deny between all segments, explicit allow for required flows only, application-aware policies (not just port-based), east-west traffic inspection for lateral movement detection.

**FIREWALL ARCHITECTURE**

Deploy defense-in-depth firewall strategy. Perimeter: next-generation firewalls (Palo Alto, Fortinet, Cisco Firepower, Check Point) with application identification, threat prevention, URL filtering, and SSL/TLS inspection. Internal: micro-segmentation firewalls for east-west traffic, software-defined firewalls for cloud workloads, host-based firewalls on endpoints. Web application: WAF for internet-facing applications (F5, Cloudflare, AWS WAF), API gateway protection, bot mitigation, OWASP Top 10 coverage. Rule management: infrastructure-as-code for firewall policies (Terraform, Ansible), change control with approval workflow, quarterly rule audits removing stale entries, automatic rule expiration for temporary access.

**INTRUSION DETECTION AND PREVENTION**

Implement layered detection capabilities. Network-based IDS/IPS: inline prevention at network chokepoints, signature-based for known threats (Snort, Suricata, commercial solutions), behavioral detection for anomalies, threat intelligence integration for IOC matching. Placement strategy: north-south at perimeter, east-west between security zones, cloud-native (AWS Network Firewall, Azure Firewall Premium) for cloud segments. Tuning: baseline normal traffic patterns during deployment, reduce false positives through exclusions and threshold adjustment, custom signatures for application-specific threats, continuous tuning based on analyst feedback.

**SECURE REMOTE ACCESS**

Choose remote access model matching security requirements. Traditional VPN: site-to-site IPsec for branch connectivity, remote access VPN (Cisco AnyConnect, GlobalProtect, Pulse) for legacy applications, always-on VPN for full-tunnel corporate traffic. Zero Trust Network Access: replace VPN with per-application access (Zscaler Private Access, Cloudflare Access, Palo Alto Prisma), verify identity and device posture before every connection, no network-level access—only application-level, continuous verification throughout session. SASE: converged security (SWG, CASB, FWaaS, ZTNA) for distributed workforce, single policy engine across all users and locations, replace MPLS with internet-first connectivity.

**NETWORK ACCESS CONTROL**

Enforce device authentication and posture. 802.1X: wired and wireless authentication with RADIUS (Cisco ISE, Aruba ClearPass, ForeScout), certificate-based for corporate devices, MAB (MAC Authentication Bypass) for devices without 802.1X capability. Posture assessment: verify device compliance (OS patched, AV running, encryption enabled) before network access, quarantine non-compliant devices with remediation portal. Guest and BYOD: separate network segments for untrusted devices, application-level access only (web portal, limited services), no access to internal resources from guest networks. IoT/OT: device profiling and automatic segmentation, dedicated IoT VLANs with restricted communication paths, east-west isolation between IoT devices.

**DDoS PROTECTION**

Layer DDoS defenses by attack type. Volumetric: upstream scrubbing services (Cloudflare, Akamai, AWS Shield), CDN absorption of traffic spikes, ISP-level blackholing for extreme attacks. Protocol: rate limiting at network edge, SYN flood protection, connection timeouts and limits. Application layer: WAF with rate limiting, bot detection and CAPTCHA challenges, behavioral analysis for low-and-slow attacks. Hybrid: on-premises appliances for instant response, cloud scrubbing for large-scale attacks, automatic failover between on-prem and cloud.

**DNS SECURITY**

Secure DNS infrastructure against threats. DNSSEC: sign zones to prevent spoofing, validate responses from upstream resolvers. DNS filtering: block known malicious domains (Cisco Umbrella, Zscaler, Infoblox), category-based filtering for policy enforcement, block newly registered domains (high-risk). Threat detection: detect DNS tunneling (exfiltration via DNS queries), identify DGA (domain generation algorithm) patterns, monitor for DNS rebinding attacks. Internal DNS: private DNS zones for internal resources, split-horizon DNS for hybrid environments, DNS firewall for internal resolution security.

**MONITORING AND VISIBILITY**

Build comprehensive network visibility. Traffic analysis: NetFlow/sFlow/IPFIX collection from all network devices, full packet capture at critical points (SPAN, TAP), encrypted traffic analysis (JA3 fingerprinting, metadata analysis). Network Detection and Response: behavioral analytics for lateral movement detection (Darktrace, Vectra, Corelight), asset discovery and classification, threat hunting with network telemetry. Centralized logging: SIEM integration for correlation (Splunk, Sentinel, Elastic), retention per compliance requirements, real-time alerting on security events. Visualization: network topology maps, traffic flow visualization, attack surface mapping.

**IMPLEMENTATION APPROACH**

Phase 1 Foundation (Months 1-2): network discovery and asset inventory, baseline traffic analysis, firewall rule audit and documentation, quick wins (block known-bad, enable logging).

Phase 2 Segmentation (Months 3-4): implement priority segmentation (PCI, PHI, production isolation), deploy east-west inspection, enable micro-segmentation for critical workloads.

Phase 3 Advanced Controls (Months 5-6): IDS/IPS tuning and optimization, NAC deployment with phased enforcement, ZTNA pilot for remote users.

Phase 4 Visibility (Ongoing): NDR deployment for behavioral detection, continuous monitoring and alerting, regular penetration testing, quarterly rule reviews.

Deliver network security architecture as:

1. **ARCHITECTURE DESIGN** - Network topology, zone definitions, traffic flows, security control placement

2. **SEGMENTATION PLAN** - Zone design, VLAN/subnet scheme, micro-segmentation approach, migration plan

3. **FIREWALL POLICIES** - Rule templates, management procedures, audit schedule, IaC automation

4. **IDS/IPS CONFIGURATION** - Sensor placement, signature policies, tuning procedures, escalation workflow

5. **REMOTE ACCESS** - VPN/ZTNA design, authentication integration, device posture requirements

6. **NAC POLICIES** - 802.1X configuration, posture assessment, guest/BYOD procedures, IoT segmentation

7. **MONITORING STRATEGY** - Flow analysis, NDR, SIEM integration, alerting thresholds, response playbooks

---

## Usage Examples

### Example 1: Retail Chain PCI-DSS Compliance
**Prompt:** Design network security for RetailCorp with 500 stores, 2 data centers, AWS presence achieving PCI-DSS compliance with defense-in-depth protecting cardholder data.

**Expected Output:** Segmentation: PCI CDE in dedicated VLAN (10.x.100.0/24) isolated from corporate, micro-segmentation via Illumio between POS and payment processors, guest WiFi completely isolated on separate internet circuit. Firewall: Palo Alto PA-5250 at data centers (HA pair), PA-220 at each store, App-ID policies allowing only POS applications to CDE, deny-by-default with explicit rules per PCI requirement. IDS/IPS: Palo Alto Threat Prevention with card skimming signatures, inline blocking mode, WildFire for zero-day malware. Store connectivity: SD-WAN (Silver Peak) replacing MPLS, encrypted overlay for all store traffic, local internet breakout for guest only. Remote access: GlobalProtect with MFA for store support, no direct VPN to CDE (jump host required), session recording for CDE access. Monitoring: NetFlow from all devices to Splunk, 90-day retention for PCI, real-time alerts on CDE traffic anomalies, quarterly penetration testing. Compliance: network scans via Qualys (quarterly), firewall rule review (semi-annually), network diagram updates (annually).

### Example 2: Healthcare Multi-Site Network
**Prompt:** Design network security for HealthSystem with 20 hospitals, 100 clinics, Epic EHR achieving HIPAA compliance with medical device isolation.

**Expected Output:** Segmentation: clinical networks (Epic Hyperspace, Citrix) isolated from administrative, medical device VLANs (IoMT) per department with east-west blocking, biomedical equipment on dedicated segments (imaging, infusion pumps, patient monitors). Firewall: Cisco Firepower 4100 at hospital cores, Meraki MX at clinics, application-aware policies for HL7/FHIR traffic, TLS inspection bypass for medical device traffic (compatibility). IDS/IPS: Firepower IPS with medical device vulnerability signatures, behavioral detection for lateral movement, custom rules for Epic traffic patterns. Medical device security: Claroty for OT/IoMT visibility, device profiling and automatic segmentation, vendor remote access via PAM with session recording. NAC: Cisco ISE with 802.1X for all wired, device profiling for medical equipment, automatic VLAN assignment by device type, quarantine for unknown devices. Remote access: Cisco AnyConnect with Duo MFA, clinical remote access to Citrix only (no direct Epic), vendor access via jump host with recording. Compliance: PHI access logging, 7-year log retention, BAA requirements for network vendors.

### Example 3: Financial Services Zero Trust Transformation
**Prompt:** Design network security for FinanceCorp with 10,000 users, 3 data centers migrating to AWS achieving SOC 2 and zero trust architecture replacing legacy perimeter.

**Expected Output:** Zero trust: eliminate network perimeter trust, identity-based access to all applications, continuous verification throughout session, assume breach posture. Architecture: SASE (Zscaler) for all user traffic, retire MPLS in favor of internet-first, AWS Transit Gateway for cloud networking. Segmentation: AWS VPC per application tier, Security Groups with least-privilege, micro-segmentation via Illumio for on-prem, no cross-VPC routing without explicit approval. Remote access: Zscaler Private Access (ZPA) replaces VPN, per-application access with identity and device posture, no network-level access anywhere. Cloud firewall: AWS Network Firewall for centralized inspection, Zscaler Cloud Firewall for all internet egress, no direct internet from VPCs. IDS/IPS: AWS GuardDuty for threat detection, Zscaler Cloud IPS for inline prevention, VPC Flow Logs analysis for anomalies. DDoS: AWS Shield Advanced for all internet-facing resources, Cloudflare in front of public applications. DNS: Zscaler DNS Security for all resolution, internal Route 53 for private zones. Monitoring: VPC Flow Logs and Zscaler logs to Splunk, Darktrace for NDR, real-time correlation across cloud and on-prem. Migration: 6-month phased rollout (pilot 500 users → department by department), parallel VPN operation during transition, VPN decommission after 100% ZPA adoption.

---

## Cross-References

- [Zero Trust Architecture](../Identity-Access-Management/zero-trust-architecture.md) - Zero trust principles for network access
- [Cloud Security Architecture](../Cloud-Security/cloud-security-architecture.md) - Cloud-specific network security patterns
- [Privileged Access Management](../Identity-Access-Management/privileged-access-management.md) - Securing administrative network access
