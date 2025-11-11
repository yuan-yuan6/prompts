# Function-First Migration Plan

**Date:** 2025-11-11
**Purpose:** Detailed plan for reorganizing repository from hybrid classification to function-first taxonomy

---

## Executive Summary

**Scope:** Reorganize 500 templates from 13 categories to 18 function-based categories
**Estimated Effort:** 40-60 hours total
**Approach:** Incremental migration with validation at each step
**Risk:** High - affects all templates, links, and documentation

---

## New Directory Structure

```
/prompts/
├── strategy/                    [NEW] ← FROM business/Strategic Management + parts of professional-services
├── operations/                  [NEW] ← FROM business/Operations & Processes + parts of professional-services
├── finance/                     [MERGE] ← FROM finance/ + business/Finance & Accounting
├── sales-marketing/             [NEW] ← FROM business/Sales & Marketing + creative/Marketing Creative
├── human-resources/             [NEW] ← FROM business/Human Resources + professional-services/human-resources
├── communication/               [NEW] ← FROM professional-services/communication
├── technology/                  [KEEP] ← KEEP as-is (minus moved cybersecurity)
├── data-analytics/              [KEEP] ← KEEP as-is
├── security/                    [EXPAND] ← Already expanded in Phase 1
├── design/                      [NEW] ← FROM creative/Design & Visual
├── content-creation/            [NEW] ← FROM creative/Content Creation
├── media-journalism/            [NEW] ← FROM creative/journalism
├── legal-compliance/            [NEW] ← FROM professional-services/legal-compliance
├── clinical-healthcare/         [RENAME] ← FROM healthcare/
├── education/                   [KEEP] ← KEEP as-is
├── personal/                    [KEEP] ← KEEP as-is
├── government/                  [KEEP] ← KEEP as-is
├── nonprofit/                   [KEEP] ← KEEP as-is
└── [REMOVE] industry/           Templates distributed to functional categories with industry tags
└── [REMOVE] business/           Templates distributed to strategy, operations, finance, sales-marketing, hr
└── [REMOVE] professional-services/ Templates distributed to communication, hr, legal-compliance
└── [REMOVE] creative/           Templates distributed to design, content-creation, media-journalism, sales-marketing
```

---

## Migration Phases

### Phase 2A: Merge Finance Categories (4-6 hours)
**Status:** High Priority

**Steps:**
1. Create comprehensive /finance/ directory structure:
   ```
   /finance/
   ├── Corporate-Finance/
   ├── Investment-Management/
   ├── Banking/
   ├── Insurance/
   ├── Risk-Management/
   ├── Economics/
   └── Wealth-Management/
   ```

2. Move from business/Finance & Accounting/ → /finance/Corporate-Finance/:
   - audit-compliance.md
   - budget-management.md
   - financial-analysis.md
   - investment-evaluation.md
   - treasury-management.md
   - trading-portfolio-management.md (Investment & Trading/)
   - risk-assessment.md (Investment & Trading/)

3. Consolidate existing /finance/ templates (already in correct location)

4. Update all category metadata

5. Fix related_templates links

---

### Phase 2B: Split Creative by Profession (6-8 hours)
**Status:** High Priority

**Steps:**

1. **Create /design/ category:**
   ```
   /design/
   ├── UX-UI/
   ├── Graphic-Design/
   ├── Motion-Graphics/
   ├── Product-Design/
   └── 3D-Design/
   ```

   Move from creative/Design & Visual/:
   - ux-ui-design.md, ux-ui-design-comprehensive.md
   - graphic-design.md, graphic-design-comprehensive.md
   - motion-graphics.md, motion-graphics-comprehensive.md
   - product-design.md
   - 3d-design.md

2. **Create /content-creation/ category:**
   ```
   /content-creation/
   ├── Writing/
   ├── Video-Production/
   ├── Audio-Production/
   └── Social-Media/
   ```

   Move from creative/Content Creation/:
   - article-writing.md
   - creative-writing.md
   - video-scripts.md
   - podcast-content.md
   - social-media-content.md

   Also move:
   - creative/creative-writing-framework.md
   - creative/video-production-pipeline.md

3. **Create /media-journalism/ category:**
   ```
   /media-journalism/
   ├── News-Production/
   ├── Digital-Publishing/
   └── Digital-Media/
   ```

   Move from creative/journalism/:
   - All investigative reporting, content strategy, publishing templates

4. **Move to /sales-marketing/:**
   ```
   /sales-marketing/Marketing-Creative/
   ```

   Move from creative/Marketing Creative/:
   - ad-copy.md, ad-copy-comprehensive.md
   - brand-storytelling.md, brand-storytelling-comprehensive.md
   - campaign-concepts.md, campaign-concepts-comprehensive.md
   - email-marketing.md, email-marketing-comprehensive.md
   - landing-pages.md, landing-pages-comprehensive.md

5. **Handle Entertainment** (defer or create /entertainment/):
   - screenwriting, music-audio, comedy-writing, entertainment-game-design, interactive-media
   - DECISION: Create /entertainment/ subcategory under /content-creation/ OR move to /content-creation/Entertainment/

6. **Handle Arts & Culture:**
   - cultural-institution.md, digital-exhibition-curation.md
   - DECISION: Move to /education/ or keep in /content-creation/Arts-Culture/

---

### Phase 2C: Distribute Business & Professional-Services (12-16 hours)
**Status:** High Priority - Most complex

**Distribution Map:**

#### TO /strategy/:
FROM business/Strategic Management/:
- business-planning.md
- digital-transformation.md
- growth-strategy.md
- innovation-strategy.md
- risk-management.md
- strategic-digital-transformation-roadmap.md
- strategic-financial-planning.md
- strategic-market-analysis.md
- strategic-performance-management.md

FROM business/ (root):
- digital-transformation-roadmap.md
- okr-implementation-framework.md
- swot-analysis-template.md

FROM professional-services/:
- Various strategic planning templates (if any)

#### TO /operations/:
FROM business/Operations & Processes/:
- project-management.md
- quality-assurance.md
- process-optimization templates
- supply-chain templates (from industry/)

FROM professional-services/:
- project-management/ templates
- customer-service/ templates (operations focus)

#### TO /human-resources/:
FROM business/Human Resources/:
- compensation-benefits.md
- employee-relations.md
- performance-reviews.md
- recruitment.md
- training-programs.md

FROM professional-services/human-resources/:
- employee-engagement-program.md
- hr-performance-management.md (Talent Management/)
- performance-review-system.md
- talent-acquisition-strategy.md

#### TO /sales-marketing/:
FROM business/Sales & Marketing/:
- customer-engagement.md
- lead-generation.md
- lead-scoring.md (Lead Generation/)
- market-research.md

FROM professional-services/marketing-sales/:
- marketing-brand-strategy-development.md

ALSO FROM creative/Marketing Creative/ (see Phase 2B)

#### TO /communication/:
FROM professional-services/communication/ (ENTIRE DIRECTORY):
- Customer Support/
- Internal Communication/
- Public Communication/
- Stakeholder Management/
- Team Communication/
- All communication templates

#### TO /legal-compliance/:
FROM professional-services/legal-compliance/ (ENTIRE DIRECTORY):
- Contract Management/
- Corporate Legal/
- Intellectual Property/
- Regulatory Compliance/
- All legal templates

---

### Phase 2D: Rationalize Industry Category (8-10 hours)
**Status:** Medium Priority

**Approach:** Distribute industry-specific templates to functional categories with industry tags

**Distribution:**

#### Manufacturing → /operations/Manufacturing/
- quality-management.md
- lean-manufacturing.md
- supply-chain templates

#### Retail/E-commerce → /sales-marketing/Retail-Ecommerce/
- catalog-management-system.md
- customer-experience templates
- inventory management

#### Hospitality → /operations/Service-Operations/
- hotel-management templates
- service-design templates

#### Real Estate → /finance/Real-Estate/ OR /sales-marketing/Real-Estate/
- property-development templates
- transactions templates

#### Telecommunications → /technology/Telecommunications/
- 5g-network-deployment.md
- telecom infrastructure templates

#### Energy & Utilities → /operations/Energy-Utilities/
- generation, renewable energy, customer services templates

#### Transportation & Logistics → /operations/Transportation-Logistics/
- logistics, supply-chain templates

#### Automotive → /technology/Automotive/ OR /industry/Automotive/
- autonomous-vehicle-systems.md, electric-vehicles templates

#### Agriculture → /operations/Agriculture/ OR /industry/Agriculture/
- precision-agriculture templates

#### Fashion & Beauty → /sales-marketing/Fashion-Beauty/ OR /design/Fashion/
- fashion design and retail templates

#### Sports & Recreation → /operations/Sports-Recreation/ OR keep in /industry/
- athlete-performance-optimization.md

#### Construction → /operations/Construction/
- construction-planning.md
- project management templates

#### Entertainment & Gaming → /content-creation/Entertainment/
- game-design templates

**DECISION POINT:** Some industries may warrant keeping in /industry/ if they don't fit cleanly into functional categories. Recommendation: Distribute most, keep 3-4 truly unique industry verticals.

---

### Phase 2E: Rename Healthcare (1 hour)
**Status:** Low Priority

**Steps:**
1. Rename /healthcare/ → /clinical-healthcare/
2. Update all category metadata: `category: clinical-healthcare`
3. Update INDEX.md and documentation
4. Update related_templates references

---

## Link Update Strategy

**Challenge:** 500 templates with thousands of related_templates links

**Approach:**

1. **Create mapping file:** old_path → new_path for ALL moved templates
2. **Script-based replacement:**
   ```bash
   # Find all related_templates references
   # Replace old paths with new paths
   # Validate all links resolve
   ```

3. **Manual verification:** Spot-check 50 random templates

4. **Automated testing:** Script to verify all related_templates links are valid

---

## Metadata Update Strategy

**Challenge:** Update category field in 500 YAML frontmatter blocks

**Approach:**

1. **Create category mapping:** template_file → new_category
2. **Script-based replacement:**
   ```python
   for template in all_templates:
       update_yaml_category(template, new_category_map[template])
   ```

3. **Validation:** Ensure all templates have valid category metadata

---

## Index and Documentation Updates

**Files to Update:**

1. **INDEX.md** - Complete rewrite with new category structure
2. **README.md** - Update category list and counts
3. **All category READMEs** - Create new READMEs for new categories
4. **navigate.py** - Update to reflect new structure
5. **CLASSIFICATION_GUIDE.md** - Already created, may need minor updates

---

## Risk Mitigation

**Risks:**

1. **Broken links:** Related_templates references break
   - **Mitigation:** Comprehensive link update script + validation

2. **Lost templates:** Templates accidentally deleted or misplaced
   - **Mitigation:** Git tracking, incremental commits, validation counts

3. **User disruption:** Existing users have bookmarks/links that break
   - **Mitigation:** Maintain INDEX.md compatibility, consider redirect mapping

4. **Incomplete migration:** Some templates not moved correctly
   - **Mitigation:** Checklist of all templates, validation at each phase

5. **Metadata errors:** Category fields incorrect after migration
   - **Mitigation:** Automated validation script, spot checks

---

## Validation Checklist

After each phase, validate:

- [ ] Template count matches (no templates lost)
- [ ] All category metadata updated correctly
- [ ] All related_templates links resolve
- [ ] All README files updated
- [ ] INDEX.md reflects new structure
- [ ] Git commit successful with clear message
- [ ] Spot-check 10 random templates for correctness

---

## Timeline Estimate

| Phase | Task | Hours | Status |
|-------|------|-------|--------|
| 1 | Security consolidation | 2 | ✅ DONE |
| 1 | Healthcare flattening | 1 | ✅ DONE |
| 1 | CLASSIFICATION_GUIDE.md | 3 | ✅ DONE |
| 2A | Merge finance categories | 4-6 | Pending |
| 2B | Split creative by profession | 6-8 | Pending |
| 2C | Distribute business/professional-services | 12-16 | Pending |
| 2D | Rationalize industry category | 8-10 | Pending |
| 2E | Rename healthcare | 1 | Pending |
| 3 | Update all links and metadata | 8-12 | Pending |
| 4 | Update INDEX.md and READMEs | 4-6 | Pending |
| 5 | Validation and testing | 4-6 | Pending |
| **TOTAL** | **Full Migration** | **53-75 hours** | **6/75 done** |

---

## Incremental Approach Recommendation

Given the scope, recommend completing in stages:

**Week 1:** Phase 2A (Finance merge) + Phase 2B (Creative split)
**Week 2:** Phase 2C (Business/Professional-services distribution)
**Week 3:** Phase 2D (Industry rationalization) + Phase 3 (Links/metadata)
**Week 4:** Phase 4-5 (Documentation + validation)

**OR**

**Fast-track:** Complete all phases in 2-3 intensive sessions (12-20 hours total)

---

## Current Progress

✅ **Phase 1 Complete** (6 hours)
- Security consolidated (8 templates now visible)
- Healthcare wellness flattened (4 templates moved)
- CLASSIFICATION_GUIDE.md created

🔄 **Phase 2 In Progress**
- Migration plan created
- Ready to begin file movements

---

**Next Step:** Begin Phase 2A (Merge Finance Categories) or seek approval for full migration approach.
