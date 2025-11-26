---
category: security
last_updated: 2025-11-23
title: Network Security Architecture Framework
tags:
- security
- infrastructure
- network
use_cases:
- Designing secure network architectures
- Implementing defense-in-depth network security
- Network segmentation and zero trust
- Firewall and IDS/IPS configuration
related_templates:
- security/Cloud-Security/cloud-security-architecture.md
- security/Identity-Access-Management/zero-trust-architecture.md
industries:
- government
- technology
type: template
difficulty: intermediate
slug: network-security-architecture
---

# Network Security Architecture Framework

## Purpose
Comprehensive framework for designing secure network architectures including segmentation, defense-in-depth, firewall policies, IDS/IPS, VPNs, and zero trust networking.

## Quick Network Security Prompt
Design network security for [enterprise] with [X locations], [Y users], [on-prem/cloud/hybrid]. Implement: network segmentation (zones, VLANs), firewall policies (deny-by-default), IDS/IPS deployment, secure remote access (ZTNA/VPN), DNS security, and DDoS protection. Compliance: [PCI-DSS/HIPAA]. Deliver: network architecture diagram, security zone definitions, firewall rule templates, and monitoring strategy.

## Quick Start

**Need to design network security?** Use this minimal example:

```
Design secure network architecture for enterprise with 50 locations, 5000 users, hybrid cloud (AWS + on-prem). Implement network segmentation, firewalls, IDS/IPS, VPN, and zero trust network access replacing traditional perimeter security.
```

### When to Use This
- Designing network security for new data centers or cloud deployments
- Implementing network segmentation for compliance (PCI-DSS, HIPAA)
- Migrating from flat networks to zero trust architecture
- Responding to security incidents requiring network hardening
- Modernizing legacy perimeter-based security

### Basic 3-Step Workflow
1. **Segment Network** - Define zones, VLANs, subnets
2. **Implement Controls** - Firewalls, IDS/IPS, monitoring
3. **Test & Monitor** - Penetration testing, continuous monitoring

---

## Template

```markdown
I need to design a secure network architecture. Please provide comprehensive network security design guidance.

## NETWORK CONTEXT

### Environment
- Network size: [USERS_DEVICES_SITES]
- Architecture: [ON_PREM_CLOUD_HYBRID]
- Connectivity: [MPLS_SD_WAN_INTERNET_VPN]
- Critical systems: [DATA_CENTERS_CLOUD_REGIONS]
- Compliance: [PCI_DSS_HIPAA_ISO27001]

## SECURITY ARCHITECTURE

### 1. Network Segmentation
- DMZ / perimeter network
- Internal network zones
- Management network
- Guest network
- PCI/HIPAA compliance zones
- Development/Test/Production separation

### 2. Firewall Architecture
- Next-generation firewalls (NGFW)
- Web application firewalls (WAF)
- Firewall rule management
- High availability and redundancy
- Logging and monitoring

### 3. Intrusion Detection/Prevention
- Network-based IDS/IPS
- Host-based IDS/IPS
- Signature-based detection
- Anomaly-based detection
- Threat intelligence integration

### 4. VPN & Remote Access
- Site-to-site VPN
- Remote access VPN
- Zero Trust Network Access (ZTNA)
- Multi-factor authentication
- Split tunneling vs full tunneling

### 5. Network Access Control
- 802.1X authentication
- NAC policy enforcement
- Guest network isolation
- BYOD security
- IoT device segmentation

### 6. DDoS Protection
- Volumetric attack mitigation
- Application layer protection
- Rate limiting
- Traffic scrubbing
- CDN integration

### 7. DNS Security
- DNSSEC implementation
- DNS filtering
- DNS firewall
- DGA detection
- DNS tunneling prevention

### 8. Monitoring & Visibility
- Network traffic analysis
- Flow monitoring (NetFlow, sFlow)
- Packet capture and analysis
- Security event correlation
- Behavioral analytics

## OUTPUT REQUIREMENTS

Provide:
1. Network architecture diagram
2. Segmentation strategy
3. Firewall rule sets
4. IDS/IPS policy
5. VPN configuration
6. Monitoring architecture
7. Incident response procedures
```

## Variables

### NETWORK_SIZE
Scale of the network environment.
- Examples: "5,000 users across 50 sites", "500 employees single campus", "100,000 devices globally", "Hybrid cloud with 3 data centers"

### ARCHITECTURE_TYPE
Network architecture model.
- Examples: "On-premises data center", "Hybrid cloud (AWS + on-prem)", "Multi-cloud (AWS, Azure, GCP)", "Full cloud-native", "Edge computing with centralized core"

### CONNECTIVITY_TYPE
WAN and site connectivity solutions.
- Examples: "MPLS with internet backup", "SD-WAN (Cisco Viptela)", "Direct Connect + VPN", "SASE (Zscaler/Palo Alto Prisma)", "Internet-only with ZTNA"

### FIREWALL_PLATFORM
Firewall and NGFW solution.
- Examples: "Palo Alto Networks PA-5200", "Cisco Firepower 4100", "Fortinet FortiGate 600E", "Check Point Quantum", "AWS Network Firewall + Security Groups"

### IDS_IPS_SOLUTION
Intrusion detection and prevention system.
- Examples: "Cisco Firepower IPS", "Suricata open-source", "Snort with Talos rules", "Palo Alto Threat Prevention", "AWS GuardDuty + Network Firewall"

### REMOTE_ACCESS_METHOD
Remote access and VPN solution.
- Examples: "Cisco AnyConnect VPN", "Zscaler Private Access (ZPA)", "Cloudflare Access", "Palo Alto GlobalProtect", "WireGuard with MFA"

---

## Usage Examples

### Example 1: Retail Chain PCI-DSS Compliance
```
NETWORK_SIZE: 500 retail stores + 2 data centers + AWS
ARCHITECTURE_TYPE: Hybrid with centralized PCI cardholder data environment
CONNECTIVITY_TYPE: SD-WAN (Silver Peak) with MPLS backup
FIREWALL_PLATFORM: Palo Alto PA-3200 at data centers, PA-220 at stores
IDS_IPS_SOLUTION: Palo Alto Threat Prevention with WildFire
REMOTE_ACCESS_METHOD: GlobalProtect with MFA for store support

Key Network Security Implementations:
- Segmentation: PCI CDE isolated in separate VLAN with micro-segmentation
- Firewall: Application-aware policies blocking non-POS traffic
- IDS/IPS: Signature + behavioral detection for card skimming patterns
- Store Networks: Isolated guest WiFi, POS on dedicated VLAN
- Encryption: TLS 1.3 for all payment data in transit
- Monitoring: NetFlow to Splunk for anomaly detection
- Compliance: Quarterly network scans, annual penetration testing
```

### Example 2: Healthcare Multi-Site Network
```
NETWORK_SIZE: 20 hospitals + 100 clinics + cloud EHR
ARCHITECTURE_TYPE: Hybrid with Epic EHR in private cloud
CONNECTIVITY_TYPE: MPLS primary, SD-WAN overlay for cloud access
FIREWALL_PLATFORM: Cisco Firepower 4100 at hospitals, Meraki MX at clinics
IDS_IPS_SOLUTION: Cisco Firepower IPS with medical device signatures
REMOTE_ACCESS_METHOD: Cisco AnyConnect + Duo MFA

Key Network Security Implementations:
- Segmentation: Medical devices on isolated IoMT VLANs
- Firewall: Healthcare-specific application profiles
- IDS/IPS: Medical device vulnerability detection
- Clinical Networks: Separate networks for clinical vs admin
- Guest Access: Patient WiFi isolated from clinical networks
- Encryption: IPsec tunnels for inter-site HL7/FHIR traffic
- NAC: 802.1X for all wired devices with profiling
- Monitoring: Claroty for medical device network visibility
```

### Example 3: Financial Services Zero Trust
```
NETWORK_SIZE: 10,000 users, 3 data centers, full AWS migration
ARCHITECTURE_TYPE: Zero trust with software-defined perimeter
CONNECTIVITY_TYPE: SASE (Zscaler) replacing MPLS
FIREWALL_PLATFORM: Cloud-native (AWS Network Firewall + Zscaler)
IDS_IPS_SOLUTION: AWS GuardDuty + Zscaler Cloud IPS
REMOTE_ACCESS_METHOD: Zscaler Private Access (zero VPN)

Key Network Security Implementations:
- Zero Trust: Identity-based access, no network trust
- Micro-segmentation: AWS Security Groups + Illumio
- Firewall: Zscaler Cloud Firewall for all internet egress
- DDoS: AWS Shield Advanced + Cloudflare
- DNS Security: Zscaler DNS filtering + DNSSEC
- Encryption: mTLS between all services
- SASE: Single policy engine for all users/locations
- Monitoring: VPC Flow Logs + Zscaler logs to Splunk
- No Perimeter: All applications accessed via ZTNA
```

---

## Best Practices

1. **Defense in depth** - Layer multiple security controls; never rely on a single protection mechanism
2. **Segment by sensitivity** - Create network zones based on data classification and compliance requirements
3. **Default deny** - Block all traffic by default, explicitly allow only required communications
4. **Encrypt everywhere** - Use TLS/IPsec for all traffic, even internal communications
5. **Inspect encrypted traffic** - Deploy TLS inspection for outbound traffic to detect threats
6. **Monitor east-west traffic** - Internal lateral movement is where attackers live; visibility is critical
7. **Automate firewall rules** - Use infrastructure-as-code to prevent configuration drift
8. **Regular rule reviews** - Quarterly audits of firewall rules to remove stale entries
9. **Test your defenses** - Regular penetration testing and red team exercises
10. **Plan for failure** - Design redundant paths and test failover scenarios

## Common Pitfalls

❌ **Flat networks** - No segmentation allowing unrestricted lateral movement
✅ Instead: Implement micro-segmentation with least-privilege access

❌ **Overly permissive rules** - "Any-any" firewall rules for convenience
✅ Instead: Specific source/destination/port rules with regular audits

❌ **Ignoring internal traffic** - Only monitoring north-south, not east-west
✅ Instead: Deploy network detection and response (NDR) for internal visibility

❌ **Trusting the VPN** - Full network access once connected to VPN
✅ Instead: Zero trust network access with per-application policies

❌ **Stale firewall rules** - Rules accumulate without cleanup
✅ Instead: Automated rule lifecycle management with expiration dates
