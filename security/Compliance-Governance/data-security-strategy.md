---
title: "Data Security Strategy & Classification Framework"
category: security
tags: [security, data-protection, encryption, compliance, governance, risk-management]
description: "Comprehensive framework for data security including classification, encryption, access controls, data lifecycle management, DLP, and compliance with GDPR, CCPA, and other regulations."
related_templates:
  - data-privacy-framework.md
  - ../Cloud-Security/cloud-security-architecture.md
  - security-compliance-framework.md
  - ../Identity-Access-Management/zero-trust-architecture.md
  - ../Cybersecurity/security-architecture.md
version: 2.0
last_updated: 2025-11-12
---

# Data Security Strategy & Classification Framework

## Purpose
This framework provides a comprehensive approach to protecting organizational data throughout its lifecycle. It covers data discovery and classification, encryption strategies, access controls, data loss prevention (DLP), backup and recovery, and compliance with data protection regulations including GDPR, CCPA, HIPAA, and PCI-DSS.

## Quick Start

1. **Discover & Classify Data**: Identify all data assets, classify by sensitivity (Public, Internal, Confidential, Restricted), and map data flows
2. **Implement Protection Controls**: Apply encryption (at-rest, in-transit), access controls, DLP policies based on classification
3. **Secure Data Lifecycle**: Implement controls for data creation, storage, processing, sharing, archival, and destruction
4. **Monitor & Audit**: Deploy monitoring for data access, exfiltration attempts, and policy violations
5. **Ensure Compliance**: Meet regulatory requirements (GDPR, CCPA, HIPAA) with appropriate technical and organizational measures

---

## Minimal Example

**SCENARIO**: A SaaS company storing customer data needs to implement comprehensive data security for SOC 2 compliance.

**Data Discovery & Classification**:
- **Restricted**: Customer PII (names, emails, SSNs), payment information
- **Confidential**: Customer business data, contracts, proprietary algorithms
- **Internal**: Employee information, internal documentation
- **Public**: Marketing materials, public website content

**Protection Controls by Classification**:

| Classification | Encryption | Access Control | DLP | Retention |
|----------------|-----------|----------------|-----|-----------|
| **Restricted** | AES-256 at rest, TLS 1.3 in transit | MFA required, need-to-know basis | Block external sharing | 7 years, secure deletion |
| **Confidential** | AES-256 at rest, TLS 1.3 in transit | Role-based access | Alert on external sharing | 3 years, secure deletion |
| **Internal** | TLS 1.3 in transit | Authenticated employees only | Monitor external sharing | 1 year, standard deletion |
| **Public** | TLS 1.3 in transit (optional) | No restrictions | None | Indefinite |

**Key Controls Implemented**:
- **Encryption**: AWS KMS for key management, field-level encryption for PII
- **Access**: RBAC with principle of least privilege, MFA for sensitive data access
- **DLP**: Automated detection of PII, blocking emails with SSNs/credit cards
- **Monitoring**: CloudWatch logs for data access, alerts on unusual patterns
- **Backup**: Daily encrypted backups, tested quarterly recovery

**Compliance Mapping**:
- **GDPR**: Data classification, encryption, access controls, data subject rights (access, deletion)
- **SOC 2**: Access controls, encryption, monitoring, incident response
- **CCPA**: Consumer data rights, opt-out mechanisms, data inventory

**Result**: SOC 2 Type II certified, GDPR compliant, zero data breaches in 2 years.

---

## Comprehensive Framework

### PHASE 1: Data Discovery & Classification

#### 1.1 Data Discovery

**Automated Data Discovery Tools**:
- **Cloud**: AWS Macie, Azure Purview, Google Cloud DLP
- **On-Premise**: BigID, Varonis, Spirion
- **Database**: Database activity monitoring (DAM) tools
- **Endpoints**: Endpoint DLP solutions

**Discovery Scope**:
- **Structured Data**: Databases, data warehouses, CRM systems
- **Unstructured Data**: File shares, SharePoint, emails, cloud storage
- **Data in Motion**: API traffic, network traffic
- **Shadow IT**: Unapproved cloud services, personal devices

**Data Inventory**:

| Data Asset | Location | Data Type | Owner | Classification | Sensitivity Reason |
|------------|----------|-----------|-------|----------------|-------------------|
| Customer DB | AWS RDS us-east-1 | PII, Payment | Engineering | Restricted | SSNs, credit cards |
| CRM System | Salesforce | Contact info | Sales | Confidential | Customer business data |
| File Share | SharePoint | Documents | All depts | Mixed | Various, needs review |
| Logs | S3 bucket | System logs | IT Ops | Internal | May contain PII |

**Data Flow Mapping**:
```
Customer → Web App → API Gateway → Application → Database
                                  ↓
                            Analytics Pipeline → Data Warehouse
                                  ↓
                            Third-party CRM (Salesforce)
```

#### 1.2 Data Classification

**Classification Levels**:

**Level 4: Restricted** (Highest Sensitivity)
- **Definition**: Data requiring highest protection, severe impact if compromised
- **Examples**:
  - Personal: SSN, passport numbers, financial account numbers, medical records
  - Business: Trade secrets, M&A plans, unreleased financials
  - Security: Encryption keys, passwords, authentication tokens
- **Impact of Breach**: Legal liability, regulatory fines, business extinction
- **Controls**: Strongest encryption, MFA, DLP, strict access controls, audit logging

**Level 3: Confidential**
- **Definition**: Internal data with significant impact if disclosed
- **Examples**:
  - Personal: Employee personal information, customer contact details
  - Business: Contracts, pricing, customer lists, product roadmaps
  - Technical: Source code, architecture diagrams, security configurations
- **Impact of Breach**: Competitive disadvantage, reputational damage, legal issues
- **Controls**: Encryption, role-based access, DLP monitoring, access logging

**Level 2: Internal**
- **Definition**: Internal-use data, limited impact if disclosed
- **Examples**:
  - Internal policies, procedures, org charts
  - Internal communications, meeting notes
  - Non-sensitive business metrics
- **Impact of Breach**: Minor embarrassment, limited business impact
- **Controls**: Authentication required, basic access controls, optional encryption

**Level 1: Public**
- **Definition**: Data intended for public consumption
- **Examples**: Marketing materials, press releases, public website content, product documentation
- **Impact of Breach**: None (already public)
- **Controls**: Integrity protection, availability protection

**Classification Criteria Decision Tree**:
```
Is data regulated (GDPR, HIPAA, PCI-DSS)?
  → YES: Restricted
  → NO: ↓

Would unauthorized disclosure cause severe harm (legal, financial, reputational)?
  → YES: Restricted
  → NO: ↓

Would disclosure give competitors advantage or harm customer trust?
  → YES: Confidential
  → NO: ↓

Is data intended for internal use only?
  → YES: Internal
  → NO: Public
```

**Automated Classification**:
```python
# Pattern-based classification
import re

def classify_data(text):
    # SSN pattern
    if re.search(r'\b\d{3}-\d{2}-\d{4}\b', text):
        return 'RESTRICTED'

    # Credit card pattern
    if re.search(r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b', text):
        return 'RESTRICTED'

    # Email pattern (possible PII)
    if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text):
        return 'CONFIDENTIAL'

    return 'INTERNAL'  # Default
```

#### 1.3 Data Ownership & Governance

**Data Ownership Model**:

**Data Owner** (Business Role):
- Accountable for data security and compliance
- Defines access requirements and classification
- Approves access requests
- Reviews access regularly (quarterly)

**Data Custodian** (IT Role):
- Implements technical controls
- Manages day-to-day security (backups, encryption, monitoring)
- Responds to security incidents

**Data Steward** (Business + IT):
- Ensures data quality and consistency
- Enforces data governance policies
- Manages master data

**Data Governance Structure**:
```
Data Governance Council (Executive level)
    ↓
Data Classification Committee
    ↓
Data Owners (by domain: Customer, Employee, Financial, Product)
    ↓
Data Custodians (IT/Security teams)
```

**Data Governance Policy**:
- Data must be classified within 30 days of creation
- Access reviewed quarterly, recertified annually
- Sensitive data access requires business justification
- Data retention per classification and regulatory requirements
- Secure disposal required for Restricted/Confidential data

---

### PHASE 2: Data Protection Controls

#### 2.1 Encryption Strategy

**Encryption at Rest**:

**Full Disk Encryption (FDE)**:
- **Use Case**: Laptops, desktops, physical servers
- **Technology**: BitLocker (Windows), FileVault (macOS), LUKS (Linux)
- **Key Management**: TPM chip or recovery key in secure vault

**Database Encryption**:
- **Transparent Data Encryption (TDE)**: Entire database encrypted
  - SQL Server TDE, Oracle TDE, PostgreSQL encryption
- **Column-Level Encryption**: Specific sensitive columns
  - Useful for PII fields in mixed-sensitivity tables
- **Application-Level Encryption**: Encrypt before storing
  - Maximum control, but performance impact

**File/Object Storage Encryption**:
- **Cloud Storage**: S3 encryption, Azure Storage encryption, GCS encryption
- **File Shares**: EFS encryption (AWS), Azure Files encryption

**Example: AWS S3 Bucket Encryption**:
```terraform
resource "aws_s3_bucket" "data_bucket" {
  bucket = "customer-data-bucket"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm     = "aws:kms"
        kms_master_key_id = aws_kms_key.data_key.arn
      }
    }
  }
}

resource "aws_kms_key" "data_key" {
  description             = "Customer data encryption key"
  deletion_window_in_days = 30
  enable_key_rotation     = true
}
```

**Encryption in Transit**:

**TLS/SSL Configuration**:
```nginx
# Strong TLS configuration
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384';
ssl_prefer_server_ciphers on;
ssl_session_cache shared:SSL:10m;
ssl_session_timeout 10m;

# HSTS
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
```

**VPN for Data Transfer**:
- Site-to-site VPN for office-to-cloud
- Client VPN for remote access
- IPsec or WireGuard for encryption

**API Encryption**:
- Enforce HTTPS for all APIs
- Mutual TLS (mTLS) for service-to-service
- API gateway with TLS termination

**Encryption for Data in Use** (Advanced):
- **Homomorphic Encryption**: Compute on encrypted data (research stage)
- **Secure Enclaves**: Intel SGX, AMD SEV, AWS Nitro Enclaves
- **Confidential Computing**: Process sensitive data in trusted execution environments

#### 2.2 Key Management

**Key Management Hierarchy**:
```
Master Key (HSM or KMS)
    ↓
Data Encryption Keys (DEKs)
    ↓
Encrypted Data
```

**Key Management Best Practices**:

**1. Use Key Management Service (KMS)**:
- **Cloud**: AWS KMS, Azure Key Vault, Google Cloud KMS
- **On-Premise**: HashiCorp Vault, Thales CipherTrust
- **Benefits**: Centralized, audited, FIPS 140-2 compliance

**2. Key Rotation**:
- **Frequency**: Annually for data keys, quarterly for high-risk keys
- **Automated**: Use KMS automatic rotation features
- **Process**: Generate new key, re-encrypt data, retire old key

**3. Key Separation**:
- Different keys for different data classifications
- Separate keys per environment (dev, staging, prod)
- Separate keys per customer (multi-tenant SaaS)

**4. Key Access Control**:
- Principle of least privilege
- MFA for key access
- Audit all key usage

**5. Key Backup & Recovery**:
- Encrypted backup of keys
- Secure storage (safe deposit box, split knowledge)
- Tested recovery procedures

**Example: AWS KMS Key Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Enable IAM policies",
      "Effect": "Allow",
      "Principal": {"AWS": "arn:aws:iam::123456789012:root"},
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "Allow application to encrypt/decrypt",
      "Effect": "Allow",
      "Principal": {"AWS": "arn:aws:iam::123456789012:role/AppRole"},
      "Action": [
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "*"
    },
    {
      "Sid": "Deny key deletion",
      "Effect": "Deny",
      "Principal": "*",
      "Action": [
        "kms:ScheduleKeyDeletion",
        "kms:Delete*"
      ],
      "Resource": "*"
    }
  ]
}
```

#### 2.3 Access Controls

**Access Control Models**:

**Role-Based Access Control (RBAC)**:
```yaml
# RBAC Example
roles:
  - name: DataAnalyst
    permissions:
      - read:customer_analytics
      - read:sales_data
    data_access:
      - classification: Internal, Confidential
      - exclude_fields: [ssn, credit_card]

  - name: CustomerSupport
    permissions:
      - read:customer_profile
      - update:customer_contact
    data_access:
      - classification: Confidential
      - masking: [ssn, credit_card]

  - name: DataScientist
    permissions:
      - read:anonymized_customer_data
    data_access:
      - classification: Internal
      - anonymization: required
```

**Attribute-Based Access Control (ABAC)**:
```python
# ABAC Policy Example
def check_access(user, resource, action):
    # User attributes
    user_dept = user.department
    user_role = user.role
    user_clearance = user.clearance_level

    # Resource attributes
    data_classification = resource.classification
    data_owner_dept = resource.owner_department

    # Environmental attributes
    time = datetime.now()
    location = user.location

    # Policy rules
    if data_classification == 'RESTRICTED':
        if user_clearance < 4:
            return False
        if not user.mfa_verified:
            return False
        if location not in ['office', 'vpn']:
            return False

    if data_classification == 'CONFIDENTIAL':
        if user_dept == data_owner_dept or user_role == 'Admin':
            return True
        if user_clearance >= 3 and action == 'read':
            return True

    return False
```

**Principle of Least Privilege**:
- Users have minimum access needed for job function
- Time-bound access for temporary needs
- Just-in-time (JIT) access for privileged operations
- Regular access reviews (quarterly)

**Privileged Access Management (PAM)**:
- Separate privileged accounts from regular accounts
- MFA required for privileged access
- Session recording for privileged sessions
- Break-glass procedures for emergencies

#### 2.4 Data Loss Prevention (DLP)

**DLP Architecture**:
```
Data at Rest DLP → Scans file servers, databases, endpoints
    ↓
Data in Motion DLP → Monitors network, email, web traffic
    ↓
Data in Use DLP → Monitors application usage, clipboard, screenshots
```

**DLP Policies**:

**Policy 1: Block SSN Exfiltration**:
- **Trigger**: Content contains SSN pattern (XXX-XX-XXXX)
- **Scope**: Email, file uploads, messaging apps
- **Action**: Block and alert security team
- **Exception**: Approved business process (with encryption)

**Policy 2: Alert on Confidential Data Sharing**:
- **Trigger**: Files tagged "Confidential" shared externally
- **Scope**: Cloud storage (Drive, Dropbox), email attachments
- **Action**: Alert user and manager, require justification
- **Exception**: Approved partners (via secure portal)

**Policy 3: Monitor PII Access**:
- **Trigger**: Access to customer PII database
- **Scope**: Database queries, API calls
- **Action**: Log access, alert on bulk downloads (>1000 records)
- **Exception**: Approved analytics jobs

**DLP Implementation**:
```python
# Email DLP example
import re

def scan_email(email):
    content = email.body + " ".join([a.content for a in email.attachments])

    # SSN detection
    ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
    if re.search(ssn_pattern, content):
        if email.recipient.external:
            email.block()
            alert_security_team("SSN in external email", email)
            return False

    # Credit card detection
    cc_pattern = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'
    if re.search(cc_pattern, content):
        if email.recipient.external:
            email.block()
            alert_security_team("Credit card in external email", email)
            return False

    # Confidential data
    if has_confidential_classification(email.attachments):
        if email.recipient.external:
            alert_manager("Confidential data shared externally", email)
            require_justification(email)

    return True
```

**DLP Tools**:
- **Endpoint**: Symantec DLP, McAfee DLP, Microsoft Purview
- **Network**: Forcepoint DLP, Digital Guardian
- **Cloud**: Microsoft Purview, Google DLP API, AWS Macie
- **Email**: Proofpoint, Mimecast, Microsoft 365 DLP

---

### PHASE 3: Data Lifecycle Management

#### 3.1 Data Creation & Collection

**Data Minimization**:
- Collect only necessary data (GDPR principle)
- Define purpose before collection
- Retention period defined at collection

**Privacy by Design**:
- Privacy controls built into systems from design
- Data protection impact assessments (DPIA) for high-risk processing
- Consent management for personal data

**Data Quality**:
- Validation at input (format, range, consistency)
- Deduplication to avoid redundant storage
- Data quality metrics and monitoring

#### 3.2 Data Storage & Retention

**Storage Security**:
- Encryption at rest based on classification
- Access controls enforced
- Geographic restrictions (data residency requirements)
- Redundancy for availability (replication, backups)

**Data Retention Policy**:

| Data Type | Retention Period | Basis | Destruction Method |
|-----------|------------------|-------|-------------------|
| Customer PII | 7 years after relationship ends | Legal, GDPR | Secure deletion (3-pass overwrite) |
| Financial records | 7 years | Tax law, SOX | Secure deletion |
| Employee records | 7 years after termination | Labor law | Secure deletion |
| Application logs | 90 days | Operational need | Standard deletion |
| Security logs | 1 year | SOC 2, incident investigation | Standard deletion |
| Backup data | 30 days | Business continuity | Encrypted deletion |

**Retention Implementation**:
```python
# S3 Lifecycle Policy
import boto3

s3 = boto3.client('s3')

lifecycle_policy = {
    'Rules': [
        {
            'ID': 'Delete-old-logs',
            'Status': 'Enabled',
            'Prefix': 'logs/',
            'Expiration': {'Days': 90},
        },
        {
            'ID': 'Archive-financial-records',
            'Status': 'Enabled',
            'Prefix': 'financial/',
            'Transitions': [
                {'Days': 90, 'StorageClass': 'GLACIER'},
                {'Days': 2555, 'StorageClass': 'DEEP_ARCHIVE'},  # ~7 years
            ],
            'Expiration': {'Days': 2920},  # ~8 years (7 + buffer)
        }
    ]
}

s3.put_bucket_lifecycle_configuration(
    Bucket='data-bucket',
    LifecycleConfiguration=lifecycle_policy
)
```

#### 3.3 Data Sharing & Transfer

**Internal Data Sharing**:
- Access control enforcement (RBAC/ABAC)
- Data masking for non-privileged users
- Audit logging of data access

**External Data Sharing**:
- Data Processing Agreements (DPA) with vendors
- Secure transfer methods (SFTP, encrypted email, secure portal)
- Data anonymization/pseudonymization when possible
- Contractual obligations for data protection

**Cross-Border Data Transfer**:
- **GDPR**: Adequacy decisions, Standard Contractual Clauses (SCC), Binding Corporate Rules (BCR)
- **China**: Data localization requirements
- **Russia**: Data localization for Russian citizens
- **Other**: Country-specific requirements

**Example: Secure File Transfer**:
```python
# Encrypt file before transfer
from cryptography.fernet import Fernet

def secure_file_transfer(file_path, recipient):
    # Generate encryption key
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # Encrypt file
    with open(file_path, 'rb') as f:
        encrypted_data = fernet.encrypt(f.read())

    # Transfer encrypted file
    transfer_file(encrypted_data, recipient)

    # Send key via separate secure channel
    send_key_via_secure_channel(key, recipient)

    # Log transfer
    log_data_transfer(file_path, recipient, classification='CONFIDENTIAL')
```

#### 3.4 Data Archival & Destruction

**Data Archival**:
- Long-term retention for compliance
- Cost-effective storage (AWS Glacier, Azure Archive)
- Encryption maintained in archive
- Tested retrieval procedures

**Secure Data Destruction**:

**Digital Data**:
- **Logical Deletion**: Standard file deletion (not secure)
- **Overwriting**: Multi-pass overwriting (DoD 5220.22-M: 3 passes)
- **Cryptographic Erasure**: Destroy encryption keys (if all data encrypted)
- **Physical Destruction**: Shred SSDs/HDDs (for decommissioned hardware)

**Physical Media**:
- Shredding (cross-cut shredder for documents)
- Degaussing (magnetic media)
- Incineration (highest security)
- Certificate of destruction from vendor

**Example: Secure Deletion**:
```python
import os
import secrets

def secure_delete_file(file_path, passes=3):
    """DoD 5220.22-M compliant file deletion"""
    file_size = os.path.getsize(file_path)

    with open(file_path, 'wb') as f:
        # Pass 1: Write random data
        f.write(secrets.token_bytes(file_size))
        f.flush()
        os.fsync(f.fileno())

        # Pass 2: Write complement (bitwise NOT)
        f.seek(0)
        f.write(bytes([~b & 0xFF for b in secrets.token_bytes(file_size)]))
        f.flush()
        os.fsync(f.fileno())

        # Pass 3: Write random data again
        f.seek(0)
        f.write(secrets.token_bytes(file_size))
        f.flush()
        os.fsync(f.fileno())

    # Delete file
    os.remove(file_path)

    # Log deletion
    log_secure_deletion(file_path)
```

---

### PHASE 4: Compliance & Regulatory Requirements

#### 4.1 GDPR (General Data Protection Regulation)

**GDPR Principles**:
1. **Lawfulness, Fairness, Transparency**: Legal basis for processing, clear privacy notices
2. **Purpose Limitation**: Data collected for specific, legitimate purposes
3. **Data Minimization**: Collect only necessary data
4. **Accuracy**: Data kept accurate and up-to-date
5. **Storage Limitation**: Retained only as long as necessary
6. **Integrity and Confidentiality**: Appropriate security measures
7. **Accountability**: Demonstrate compliance

**Data Subject Rights**:
- **Right to Access**: Provide copy of personal data (within 1 month)
- **Right to Rectification**: Correct inaccurate data
- **Right to Erasure** ("Right to be Forgotten"): Delete data when no longer necessary
- **Right to Restrict Processing**: Limit processing in certain circumstances
- **Right to Data Portability**: Provide data in machine-readable format
- **Right to Object**: Object to processing for direct marketing or legitimate interests

**GDPR Technical Measures**:
```python
# GDPR data subject request handler
class GDPRRequestHandler:
    def handle_access_request(self, user_id):
        """Right to access - export all user data"""
        user_data = {
            'personal_info': get_user_profile(user_id),
            'orders': get_user_orders(user_id),
            'preferences': get_user_preferences(user_id),
            'consent_history': get_consent_history(user_id),
        }
        return export_to_json(user_data)

    def handle_erasure_request(self, user_id):
        """Right to erasure - delete all user data"""
        # Check if legal obligation to retain (e.g., financial records)
        if has_legal_retention_requirement(user_id):
            return {"status": "cannot_delete", "reason": "Legal retention requirement"}

        # Anonymize or delete
        anonymize_user_profile(user_id)
        delete_user_orders(user_id)
        delete_user_preferences(user_id)

        log_erasure_request(user_id)
        return {"status": "deleted"}

    def handle_portability_request(self, user_id):
        """Right to data portability - machine-readable format"""
        user_data = get_user_data(user_id)
        return export_to_csv(user_data)  # or JSON, XML
```

**GDPR Breach Notification**:
- Notify supervisory authority within 72 hours of breach discovery
- Notify affected data subjects if high risk to rights and freedoms
- Document all breaches (even if not reported)

#### 4.2 CCPA (California Consumer Privacy Act)

**CCPA Consumer Rights**:
- **Right to Know**: What personal information is collected, used, shared
- **Right to Delete**: Delete personal information held by business
- **Right to Opt-Out**: Opt out of sale of personal information
- **Right to Non-Discrimination**: No discrimination for exercising rights

**CCPA Requirements**:
- "Do Not Sell My Personal Information" link on website
- Privacy policy disclosing categories of data collected
- Respond to consumer requests within 45 days
- Verify identity of requestor

**CCPA vs GDPR Differences**:
| Aspect | GDPR | CCPA |
|--------|------|------|
| **Scope** | EU residents | California residents |
| **Legal Basis** | Requires lawful basis | No legal basis requirement |
| **Opt-In/Out** | Opt-in for consent | Opt-out for data sale |
| **Fines** | Up to €20M or 4% revenue | Up to $7,500 per violation |

#### 4.3 HIPAA (Health Insurance Portability and Accountability Act)

**Protected Health Information (PHI)**:
- Any individually identifiable health information
- Demographics, medical records, payment information, any data linked to individual

**HIPAA Security Rule Requirements**:

**Administrative Safeguards**:
- Risk analysis and management
- Workforce security (authorization, supervision)
- Security awareness training
- Contingency planning (backup, disaster recovery)

**Physical Safeguards**:
- Facility access controls
- Workstation security
- Device and media controls

**Technical Safeguards**:
- Access controls (unique user IDs, automatic logoff, encryption)
- Audit controls (logging all ePHI access)
- Integrity controls (prevent improper alteration/destruction)
- Transmission security (encryption in transit)

**HIPAA Breach Notification**:
- Notify affected individuals within 60 days
- Notify HHS (if >500 individuals, immediately; if <500, annually)
- Notify media (if >500 individuals in jurisdiction)

#### 4.4 PCI-DSS (Payment Card Industry Data Security Standard)

**PCI-DSS Requirements** (12 Requirements, 6 Goals):

**Goal 1: Build and Maintain Secure Network**
- Requirement 1: Firewall configuration
- Requirement 2: No vendor-supplied defaults

**Goal 2: Protect Cardholder Data**
- Requirement 3: Protect stored cardholder data (encryption)
- Requirement 4: Encrypt transmission (TLS)

**Goal 3: Maintain Vulnerability Management**
- Requirement 5: Anti-malware
- Requirement 6: Secure systems and applications

**Goal 4: Implement Strong Access Control**
- Requirement 7: Restrict access to cardholder data (need-to-know)
- Requirement 8: Unique IDs for users
- Requirement 9: Restrict physical access

**Goal 5: Regularly Monitor and Test Networks**
- Requirement 10: Track and monitor all access to network resources and cardholder data
- Requirement 11: Regularly test security systems and processes

**Goal 6: Maintain Information Security Policy**
- Requirement 12: Information security policy

**PCI-DSS Compliance Levels**:
| Level | Transaction Volume | Assessment |
|-------|-------------------|------------|
| **Level 1** | >6M transactions/year | Annual onsite assessment by QSA |
| **Level 2** | 1-6M transactions/year | Annual Self-Assessment Questionnaire (SAQ) |
| **Level 3** | 20K-1M e-commerce transactions/year | Annual SAQ |
| **Level 4** | <20K e-commerce transactions/year | Annual SAQ |

**PCI-DSS Data Storage**:
- **Never Store**: Full magnetic stripe, CAV2/CVC2/CVV2/CID, PIN/PIN block
- **May Store (if encrypted)**: PAN (Primary Account Number), cardholder name, expiration date, service code

**Tokenization** (PCI-DSS Scope Reduction):
```python
# Use payment processor tokenization
import stripe

stripe.api_key = 'sk_live_...'

# Create token (in client-side JS, not server)
# token = stripe.createToken(card_element)

# Server-side: Create charge with token (no PAN storage)
def process_payment(token_id, amount):
    charge = stripe.Charge.create(
        amount=amount,
        currency='usd',
        source=token_id,  # Token, not actual card number
        description='Order #12345'
    )
    return charge
```

---

### PHASE 5: Monitoring, Auditing & Incident Response

#### 5.1 Data Access Monitoring

**What to Monitor**:
- Access to sensitive data (Restricted/Confidential)
- Bulk data downloads (>1000 records)
- Unusual access patterns (off-hours, unusual locations)
- Failed access attempts (authorization failures)
- Data modification/deletion events
- Privileged account usage

**Monitoring Tools**:
- **SIEM**: Splunk, ELK Stack, Azure Sentinel
- **Database Activity Monitoring**: Imperva, IBM Guardium
- **Cloud**: AWS CloudTrail, Azure Monitor, GCP Cloud Audit Logs
- **DLP**: Integrated DLP monitoring

**Alerting Thresholds**:
```yaml
alerts:
  - name: Bulk data download
    condition: records_accessed > 1000 in 1 hour
    severity: HIGH
    action: Alert security team, suspend account

  - name: Off-hours sensitive data access
    condition: classification == 'RESTRICTED' AND time NOT BETWEEN 6am-8pm
    severity: MEDIUM
    action: Alert security team, log for review

  - name: Geographic anomaly
    condition: user_location != usual_location AND classification == 'CONFIDENTIAL'
    severity: MEDIUM
    action: Require MFA re-authentication
```

#### 5.2 Data Auditing

**Audit Log Requirements**:
- **Who**: User identity (unique ID, name)
- **What**: Action performed (read, write, delete, export)
- **When**: Timestamp (UTC, with timezone)
- **Where**: Source IP, device, application
- **What Data**: Data accessed (table, file, field)
- **Result**: Success or failure

**Audit Log Example**:
```json
{
  "timestamp": "2025-01-15T14:32:01Z",
  "user_id": "john.doe@company.com",
  "action": "READ",
  "resource": "customer_database.customers.ssn",
  "classification": "RESTRICTED",
  "source_ip": "192.168.1.100",
  "device": "laptop-jdoe-01",
  "application": "CRM-App",
  "result": "SUCCESS",
  "records_accessed": 1,
  "business_justification": "Customer support case #12345"
}
```

**Audit Log Protection**:
- Append-only storage (prevent tampering)
- Encrypted at rest
- Separate access controls (only security team)
- Retention per compliance requirements (1-7 years)
- Regular integrity checks

**Compliance Auditing**:
- SOC 2: Annual audit of controls
- HIPAA: Risk assessments, audit log reviews
- GDPR: Data protection impact assessments (DPIA)
- PCI-DSS: Quarterly vulnerability scans, annual penetration testing

#### 5.3 Data Breach Response

**Data Breach Response Plan**:

**Phase 1: Detection & Analysis** (Hours 0-4)
```
1. Alert received (DLP, SIEM, user report)
2. Triage incident (severity, scope)
3. Activate incident response team
4. Preserve evidence (logs, forensics)
5. Assess impact (what data, how many individuals)
```

**Phase 2: Containment** (Hours 4-24)
```
1. Isolate affected systems
2. Revoke compromised credentials
3. Block unauthorized access
4. Prevent further data exfiltration (DLP, firewall rules)
5. Assess if ongoing breach
```

**Phase 3: Eradication** (Days 1-7)
```
1. Remove malware, backdoors
2. Patch vulnerabilities exploited
3. Reset credentials
4. Improve security controls
```

**Phase 4: Recovery** (Days 7-30)
```
1. Restore systems from clean backups
2. Verify system integrity
3. Resume normal operations
4. Enhanced monitoring for re-occurrence
```

**Phase 5: Notification** (Within regulatory timelines)
```
1. Legal review of notification obligations
2. Notify regulators (GDPR: 72 hours, HIPAA: 60 days)
3. Notify affected individuals
4. Public disclosure (if required)
5. Offer credit monitoring, identity protection (if PII breach)
```

**Phase 6: Post-Incident** (Days 30-90)
```
1. Root cause analysis
2. Lessons learned
3. Update incident response plan
4. Implement preventive measures
5. Security awareness training (if human factor)
```

**Breach Notification Template**:
```
Subject: Important Security Notice

Dear [Customer Name],

We are writing to inform you of a data security incident that may have affected your personal information.

WHAT HAPPENED:
On [Date], we discovered unauthorized access to our [System]. The incident was immediately investigated and contained on [Date].

WHAT INFORMATION WAS INVOLVED:
The accessed data may have included: [List: name, email, address, SSN, etc.]

WHAT WE ARE DOING:
- We have secured our systems and implemented additional security measures
- We are working with law enforcement and cybersecurity experts
- We are offering [12 months] of free credit monitoring services

WHAT YOU CAN DO:
- Enroll in credit monitoring: [Link]
- Monitor your accounts for suspicious activity
- Consider placing fraud alert or credit freeze
- Change your password if you used the same password on other sites

For more information, please contact [Email/Phone].

We sincerely apologize for this incident and are committed to protecting your information.

Sincerely,
[CEO Name]
```

---

## Variables Table

| Variable | Description | Example Values | Notes |
|----------|-------------|----------------|-------|
| `{DATA_CLASSIFICATION}` | Sensitivity level | Restricted, Confidential, Internal, Public | Drives all security controls |
| `{ENCRYPTION_ALGORITHM}` | Encryption standard | AES-256, TLS 1.3, RSA-2048 | Use FIPS 140-2 approved algorithms |
| `{KEY_ROTATION_FREQUENCY}` | How often keys rotate | 90 days, 1 year, 3 years | More frequent for high-risk data |
| `{RETENTION_PERIOD}` | How long to keep data | 7 years, 3 years, 90 days | Based on legal and business needs |
| `{ACCESS_CONTROL_MODEL}` | Access control type | RBAC, ABAC, MAC | RBAC most common, ABAC for complex needs |
| `{DLP_ACTION}` | DLP response | Block, Alert, Quarantine, Encrypt | Block for Restricted, Alert for Confidential |
| `{COMPLIANCE_FRAMEWORK}` | Regulatory requirement | GDPR, CCPA, HIPAA, PCI-DSS, SOC 2 | Determines specific controls |
| `{AUDIT_LOG_RETENTION}` | Audit log retention | 1 year, 7 years | Per compliance requirements |
| `{DATA_RESIDENCY}` | Geographic location | US, EU, specific country | Data sovereignty requirements |
| `{BREACH_NOTIFICATION_TIMELINE}` | Notification deadline | 72 hours (GDPR), 60 days (HIPAA) | Regulatory requirement |
| `{BACKUP_FREQUENCY}` | How often backups run | Daily, Hourly, Real-time | Based on RPO requirements |
| `{MFA_REQUIREMENT}` | When MFA required | All access, Restricted data only, Privileged users | Risk-based approach |

---

## Usage Examples

### Example 1: Financial Services Data Security (PCI-DSS + SOC 2)

**Context**: Online payment platform storing credit card data, requires PCI-DSS Level 1 compliance.

**Data Classification**:
- **Restricted**: Credit card numbers (PANs), CVVs, magnetic stripe data, bank account numbers
- **Confidential**: Customer PII, transaction history, merchant data
- **Internal**: System logs, internal documentation
- **Public**: Marketing materials, help documentation

**PCI-DSS Implementation**:

**Requirement 3: Protect Stored Cardholder Data**:
- **Tokenization**: Full PANs replaced with tokens (via Stripe, Adyen)
- **No Storage**: CVV, magnetic stripe never stored
- **Encryption**: If any cardholder data stored, encrypted with AES-256
- **Key Management**: Keys in AWS KMS, rotated annually

```python
# Payment processing with tokenization
import stripe

stripe.api_key = os.environ['STRIPE_SECRET_KEY']

def process_payment(token, amount):
    """Process payment with token (no PAN storage)"""
    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            source=token,  # Token instead of card number
            description='Payment for order'
        )

        # Store only last 4 digits + token
        store_payment_info({
            'token_id': token,
            'last4': charge.source.last4,
            'brand': charge.source.brand,
            'amount': amount
        })

        return {'status': 'success', 'charge_id': charge.id}
    except stripe.error.CardError as e:
        log_payment_failure(e)
        return {'status': 'failed', 'error': e.user_message}
```

**Requirement 10: Track and Monitor All Access**:
- All cardholder data access logged
- Logs centralized in Splunk SIEM
- Automated alerts on unusual patterns
- Quarterly log reviews

```python
# Audit logging for cardholder data access
import logging
import json

def audit_log(user_id, action, resource, result):
    audit_entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'user_id': user_id,
        'action': action,
        'resource': resource,
        'classification': 'RESTRICTED' if 'payment' in resource else 'CONFIDENTIAL',
        'source_ip': request.remote_addr,
        'result': result
    }

    # Send to SIEM
    logging.info(json.dumps(audit_entry))

    # Real-time alerting for sensitive access
    if audit_entry['classification'] == 'RESTRICTED':
        check_anomaly_detection(audit_entry)
```

**PCI-DSS Network Segmentation**:
```
DMZ (Public)
    ↓ Firewall
Cardholder Data Environment (CDE) - Strict access control
    - Tokenization service
    - Payment processing
    ↓ Firewall
Internal Network (Non-CDE)
    - Application servers
    - Databases (no cardholder data)
```

**Annual PCI-DSS Compliance**:
- Quarterly vulnerability scans (by ASV)
- Annual penetration testing (by QSA)
- Annual onsite assessment (Level 1)
- Report on Compliance (ROC) submitted to card brands

**Results**:
- PCI-DSS Level 1 compliance maintained 4 consecutive years
- SOC 2 Type II certified
- Zero cardholder data breaches
- 99.99% payment processing uptime

### Example 2: Healthcare Data Security (HIPAA Compliance)

**Context**: Telehealth platform storing electronic protected health information (ePHI), serving 500K patients.

**Data Classification**:
- **Restricted**: Medical records, diagnoses, treatment plans, prescriptions, SSNs
- **Confidential**: Patient demographics, appointment schedules, billing information
- **Internal**: System configuration, internal communications
- **Public**: General health information, public website

**HIPAA Technical Safeguards Implementation**:

**Access Controls**:
```python
# Role-based access control for ePHI
class HIPAAAccessControl:
    ROLES = {
        'physician': ['read_medical_record', 'write_medical_record', 'prescribe'],
        'nurse': ['read_medical_record', 'write_notes'],
        'receptionist': ['read_demographics', 'schedule_appointment'],
        'billing': ['read_demographics', 'read_billing', 'process_payment'],
        'patient': ['read_own_records']
    }

    def check_access(self, user, action, patient_id):
        # Check role permissions
        if action not in self.ROLES.get(user.role, []):
            self.audit_log(user, action, patient_id, 'DENIED_INSUFFICIENT_PERMISSIONS')
            return False

        # Verify relationship (except for break-glass)
        if user.role != 'patient':
            if not self.has_treatment_relationship(user, patient_id) and not user.break_glass_active:
                self.audit_log(user, action, patient_id, 'DENIED_NO_RELATIONSHIP')
                return False
        else:
            # Patients can only access their own records
            if user.patient_id != patient_id:
                self.audit_log(user, action, patient_id, 'DENIED_NOT_OWN_RECORD')
                return False

        # Log successful access
        self.audit_log(user, action, patient_id, 'SUCCESS')
        return True

    def activate_break_glass(self, user, patient_id, justification):
        """Emergency access (break-glass)"""
        # Activate break-glass (time-limited)
        user.break_glass_active = True
        user.break_glass_expires = datetime.now() + timedelta(hours=1)

        # Alert security team
        alert_security("Break-glass activated", {
            'user': user.id,
            'patient': patient_id,
            'justification': justification
        })

        # Audit log
        self.audit_log(user, 'BREAK_GLASS_ACTIVATED', patient_id, 'SUCCESS', justification)
```

**Encryption**:
- **At Rest**: Database TDE (Transparent Data Encryption), field-level encryption for medical records
- **In Transit**: TLS 1.3 for all connections, VPN for clinician mobile access
- **Backups**: Encrypted backups to AWS S3 with separate encryption keys

**Audit Controls**:
- All ePHI access logged (who, what, when, why)
- Logs retained for 6 years (HIPAA requirement)
- Monthly audit log reviews by compliance team
- Automated alerts for unusual access patterns

```sql
-- Audit log query: Find unusual access patterns
SELECT user_id, COUNT(*) as access_count, COUNT(DISTINCT patient_id) as unique_patients
FROM audit_logs
WHERE action = 'READ'
  AND classification = 'RESTRICTED'
  AND timestamp >= NOW() - INTERVAL '24 hours'
GROUP BY user_id
HAVING COUNT(DISTINCT patient_id) > 50  -- Alert if accessing >50 patients/day
ORDER BY unique_patients DESC;
```

**Automatic Logoff**:
```javascript
// Session timeout after 15 minutes of inactivity (HIPAA requirement)
let inactivityTimer;

function resetTimer() {
    clearTimeout(inactivityTimer);
    inactivityTimer = setTimeout(logout, 15 * 60 * 1000);  // 15 minutes
}

document.addEventListener('mousemove', resetTimer);
document.addEventListener('keypress', resetTimer);
document.addEventListener('click', resetTimer);

function logout() {
    // Clear session
    fetch('/api/logout', { method: 'POST' });
    // Redirect to login
    window.location.href = '/login?reason=inactivity';
}
```

**Business Associate Agreements (BAA)**:
- BAAs with all vendors handling ePHI:
  - AWS (cloud infrastructure)
  - SendGrid (email notifications)
  - Twilio (SMS notifications)
  - Analytics vendor (de-identified data only)

**Patient Rights**:
```python
# HIPAA patient rights implementation
class PatientRightsHandler:
    def handle_access_request(self, patient_id):
        """Right to access medical records (within 30 days)"""
        records = get_patient_records(patient_id)
        # Export to PDF or medical record format (CCD)
        return generate_medical_record_export(records)

    def handle_amendment_request(self, patient_id, amendment_text):
        """Right to amend medical records"""
        # Clinician must approve amendment
        amendment_request = create_amendment_request(patient_id, amendment_text)
        notify_clinician(amendment_request)
        return {"status": "pending_clinician_review"}

    def handle_accounting_disclosure(self, patient_id, date_range):
        """Right to accounting of disclosures"""
        disclosures = get_disclosures(patient_id, date_range)
        # HIPAA requires accounting for past 6 years
        return disclosures
```

**Results**:
- HIPAA compliance maintained for 5 years
- HITRUST CSF certification achieved
- Zero reportable breaches (affecting 500+ individuals)
- Annual security risk assessments completed
- 95%+ patient satisfaction with privacy controls

### Example 3: Global SaaS Platform (GDPR + CCPA + SOC 2)

**Context**: B2B SaaS platform with 10K enterprise customers across 50 countries, handling employee data.

**Multi-Region Data Architecture**:
```
EU Region (Frankfurt) → EU customer data (GDPR compliance, data residency)
    ↓
US Region (Virginia) → US customer data (CCPA compliance for CA customers)
    ↓
APAC Region (Singapore) → APAC customer data (local regulations)
```

**GDPR Compliance**:

**Data Subject Rights Implementation**:
```python
# GDPR data subject request automation
class GDPRAutomation:
    def handle_access_request(self, data_subject_email):
        """Right to access - automated export"""
        # Verify identity
        if not self.verify_identity(data_subject_email):
            return {"status": "identity_verification_failed"}

        # Gather all personal data
        user_id = get_user_id(data_subject_email)
        personal_data = {
            'profile': get_user_profile(user_id),
            'activity': get_user_activity(user_id),
            'preferences': get_user_preferences(user_id),
            'consent_history': get_consent_history(user_id),
            'third_party_sharing': get_third_party_disclosures(user_id)
        }

        # Export to machine-readable format
        export_file = generate_gdpr_export(personal_data, format='JSON')

        # Send via secure link (encrypted, time-limited)
        secure_link = create_secure_download_link(export_file, expires_hours=48)
        send_email(data_subject_email, secure_link)

        # Log request (compliance record)
        log_gdpr_request(user_id, 'ACCESS', 'COMPLETED')

        return {"status": "completed", "delivery": "email"}

    def handle_erasure_request(self, data_subject_email):
        """Right to erasure (right to be forgotten)"""
        user_id = get_user_id(data_subject_email)

        # Check if legal obligation to retain
        if self.has_legal_retention_requirement(user_id):
            return {
                "status": "cannot_erase",
                "reason": "Legal retention requirement (e.g., financial records for 7 years)"
            }

        # Anonymize instead of delete (preserve analytics)
        anonymize_user_data(user_id)

        # Delete from backups (within backup retention period)
        schedule_backup_deletion(user_id)

        # Notify third parties (processors)
        notify_processors_of_erasure(user_id)

        log_gdpr_request(user_id, 'ERASURE', 'COMPLETED')

        return {"status": "erased"}

    def handle_portability_request(self, data_subject_email):
        """Right to data portability"""
        user_id = get_user_id(data_subject_email)

        # Export in structured, machine-readable format
        data = get_user_data(user_id)
        csv_export = generate_csv_export(data)
        json_export = generate_json_export(data)

        return {
            "status": "completed",
            "formats": ["CSV", "JSON"],
            "download_links": {
                "csv": create_secure_link(csv_export),
                "json": create_secure_link(json_export)
            }
        }
```

**Consent Management**:
```python
# GDPR consent tracking
class ConsentManager:
    def record_consent(self, user_id, purpose, consent_given):
        """Record user consent with full audit trail"""
        consent_record = {
            'user_id': user_id,
            'purpose': purpose,  # e.g., 'marketing_emails', 'analytics', 'third_party_sharing'
            'consent_given': consent_given,
            'timestamp': datetime.utcnow(),
            'consent_version': get_current_privacy_policy_version(),
            'consent_method': 'explicit_opt_in',  # vs implied
            'ip_address': request.remote_addr,
            'user_agent': request.headers.get('User-Agent')
        }

        store_consent(consent_record)

        # If consent withdrawn, stop processing
        if not consent_given:
            stop_processing(user_id, purpose)

    def check_consent(self, user_id, purpose):
        """Check if valid consent exists"""
        consent = get_latest_consent(user_id, purpose)

        if not consent:
            return False

        # Check if consent is still valid (not withdrawn, not expired)
        if consent.withdrawn or consent.expired:
            return False

        return True
```

**Data Protection Impact Assessment (DPIA)**:
```yaml
# DPIA for new feature: AI-powered resume screening
dpia:
  feature: "AI Resume Screening"
  description: "Use ML to rank job applicants"

  data_processed:
    - type: "Resume content"
      sensitivity: "CONFIDENTIAL"
      volume: "10,000 resumes/month"
    - type: "Candidate demographics"
      sensitivity: "RESTRICTED"
      legal_basis: "Legitimate interest"

  risks:
    - risk: "Algorithmic bias (discrimination)"
      likelihood: "MEDIUM"
      impact: "HIGH"
      mitigation: "Bias testing, human review, explainability"

    - risk: "Data breach (resume data exposure)"
      likelihood: "LOW"
      impact: "HIGH"
      mitigation: "Encryption, access controls, DLP"

  necessity_proportionality:
    - necessary: "Yes (job application process)"
    - proportionate: "Yes (minimal data collected)"
    - alternatives_considered: "Manual screening (less efficient, still has bias risk)"

  data_subject_rights:
    - right_to_object: "Candidates can opt-out of AI screening"
    - right_to_explanation: "Candidates can request explanation of decision"

  approval:
    - dpo_approval: "Required"
    - legal_review: "Required"
    - management_approval: "Required"
```

**Cross-Border Data Transfer (GDPR)**:
```python
# Standard Contractual Clauses (SCC) for EU to US transfer
class CrossBorderTransfer:
    def transfer_to_us_processor(self, eu_user_data, us_processor):
        """Transfer EU personal data to US processor"""

        # Verify SCC in place
        if not self.has_valid_scc(us_processor):
            raise ComplianceError("No valid SCC with US processor")

        # Verify supplementary measures (encryption, access controls)
        if not self.verify_supplementary_measures(us_processor):
            raise ComplianceError("Insufficient supplementary measures")

        # Log transfer
        log_cross_border_transfer(eu_user_data, us_processor, legal_basis='SCC')

        # Perform transfer (encrypted)
        transfer_encrypted_data(eu_user_data, us_processor)
```

**CCPA Compliance** (California customers):
```python
# CCPA "Do Not Sell" implementation
class CCPACompliance:
    def handle_do_not_sell_request(self, california_resident_id):
        """Opt-out of data sale (CCPA requirement)"""
        # Mark user as opted out
        set_do_not_sell_flag(california_resident_id, True)

        # Stop selling data to third parties
        revoke_third_party_data_access(california_resident_id)

        # Notify third parties to delete data
        notify_third_parties_of_opt_out(california_resident_id)

        log_ccpa_request(california_resident_id, 'DO_NOT_SELL', 'COMPLETED')

        return {"status": "opted_out"}

    def disclose_categories_of_data(self):
        """CCPA requirement: Disclose categories collected/shared"""
        return {
            'categories_collected': [
                'Identifiers (name, email, IP address)',
                'Commercial information (purchase history)',
                'Internet activity (browsing behavior)',
                'Geolocation data'
            ],
            'categories_sold': [
                'Internet activity (to advertising partners)'
            ],
            'categories_disclosed_for_business_purpose': [
                'Identifiers (to payment processors)',
                'Commercial information (to shipping providers)'
            ]
        }
```

**Results**:
- GDPR compliant in EU (no fines or enforcement actions)
- CCPA compliant for California residents
- SOC 2 Type II certified
- 100+ data subject access requests handled annually (average response time: 18 days)
- Zero data breaches affecting >500 individuals
- 98% customer satisfaction with data privacy controls

---

## Best Practices

### Discovery & Classification
- **Automate Discovery**: Use tools to discover data across all systems
- **Classify Early**: Classify data at creation, not retroactively
- **Default to Higher Classification**: When in doubt, classify as more sensitive
- **Regular Review**: Re-classify data as sensitivity changes over time
- **Tag Everything**: Use metadata tags for automated policy enforcement

### Protection Controls
- **Encryption Everywhere**: Default to encryption (at-rest, in-transit)
- **Strong Key Management**: Use KMS/HSM, never hardcode keys
- **Least Privilege**: Minimum necessary access, time-bound access
- **Defense in Depth**: Multiple layers of security controls
- **Monitor Continuously**: Real-time monitoring of data access

### Data Lifecycle
- **Data Minimization**: Collect only necessary data
- **Purpose Limitation**: Use data only for stated purpose
- **Retention Policies**: Delete data when no longer needed
- **Secure Destruction**: Cryptographic erasure or multi-pass overwriting
- **Regular Audits**: Quarterly reviews of data inventory and access

### Compliance
- **Know Your Regulations**: Understand applicable laws (GDPR, CCPA, HIPAA)
- **Privacy by Design**: Build privacy into systems from the start
- **Document Everything**: Maintain records of processing activities
- **Data Subject Rights**: Have processes to handle access, erasure, portability requests
- **Breach Response**: Tested incident response plan with notification procedures

---

## Common Pitfalls

### Classification Errors
- **Over-Classification**: Classifying all data as Restricted (hinders productivity)
- **Under-Classification**: Not recognizing sensitivity (inadequate protection)
- **Inconsistent Classification**: Different teams classifying same data differently
- **No Re-Classification**: Data sensitivity changes over time but not updated

### Encryption Mistakes
- **Weak Algorithms**: Using MD5, DES, or outdated algorithms
- **Hardcoded Keys**: Encryption keys in source code or config files
- **No Key Rotation**: Using same keys indefinitely
- **Encrypt, Then Forget**: Encrypting but losing keys (data unrecoverable)

### Access Control Failures
- **Excessive Permissions**: Granting more access than necessary
- **No Access Reviews**: Access never reviewed or revoked
- **Shared Accounts**: Multiple people using same credentials
- **No Segregation of Duties**: One person has complete control

### Compliance Gaps
- **Ignoring Data Subject Rights**: No process to handle access/erasure requests
- **Slow Breach Notification**: Missing regulatory deadlines (72 hours GDPR)
- **Inadequate Logging**: Not logging data access for compliance
- **No Documentation**: Can't demonstrate compliance (GDPR accountability)

### Data Lifecycle Issues
- **Data Hoarding**: Keeping data indefinitely "just in case"
- **Incomplete Deletion**: Deleting from production but not backups
- **No Retention Policy**: No defined retention periods
- **Shadow IT**: Unmanaged data copies in unapproved systems

---

## Related Templates

- **data-privacy-framework.md**: GDPR, CCPA, HIPAA detailed implementation
- **../Cloud-Security/cloud-security-architecture.md**: Cloud-specific data security
- **security-compliance-framework.md**: Compliance program management
- **../Identity-Access-Management/zero-trust-architecture.md**: Zero trust data access
- **../Cybersecurity/security-architecture.md**: Enterprise security architecture

---

## Additional Resources

**Data Protection Regulations**:
- GDPR Official Text: https://gdpr.eu/
- CCPA Official Text: California OAG
- HIPAA Security Rule: HHS.gov
- PCI-DSS: PCI Security Standards Council

**Standards & Frameworks**:
- ISO 27001/27002: Information security management
- NIST Privacy Framework
- Cloud Security Alliance (CSA) guidance

**Tools**:
- Data Discovery: AWS Macie, Azure Purview, BigID, Varonis
- DLP: Symantec DLP, Microsoft Purview, Forcepoint
- Encryption: AWS KMS, Azure Key Vault, HashiCorp Vault
- Privacy Management: OneTrust, TrustArc, Securiti.ai

**Training & Certification**:
- IAPP Certifications (CIPP, CIPM, CIPT)
- ISACA Certifications (CISM, CISA)
- Cloud provider security training (AWS, Azure, GCP)

---

*This framework provides comprehensive guidance for data security and protection. Data is the lifeblood of modern organizations and requires proportional security controls. Adapt this framework to your specific data types, risk profile, and regulatory obligations. Remember: data security is not just about technology—it requires people, processes, and technology working together.*
