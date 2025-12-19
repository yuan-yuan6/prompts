---
category: design
title: UX/UI Design Process - Navigation Guide
tags:
- ux-design
- ui-design
- design-workflow
- template-navigation
use_cases:
- Selecting appropriate UX/UI design template for current project phase
- Planning comprehensive design project workflows across multiple deliverables
- Understanding design process phases and typical sequencing
- Estimating timelines and resources for design initiatives
related_templates:
- design/wireframe-design.md
- design/prototype-development.md
- design/design-system-creation.md
- design/usability-testing-plan.md
type: framework
difficulty: intermediate
slug: ux-ui-design-overview
---

# UX/UI Design Process - Navigation Guide

## Purpose
Guide template selection and workflow planning across UX/UI design phases from wireframing through usability testing, enabling efficient navigation to appropriate templates based on project needs, deliverables, and current phase.

## 🚀 Quick Navigation Prompt

> I need to design **[PRODUCT_TYPE]** for **[USERS]** currently in **[PHASE]**. Primary goal: **[OBJECTIVE]**. Navigate me across: (1) **Current needs**—what deliverables (wireframes, prototypes, design system, test plan) address current objective? (2) **Workflow sequence**—what template order from research through validation? (3) **Timeline estimate**—what duration per phase given team size and complexity? (4) **Integration strategy**—how do deliverables connect across phases? Recommend template sequence with 3-step workflow and time estimates.

---

## Template Selection Guide

**Choosing Based on Current Phase and Objective**

Select template matching immediate deliverable need and project phase. Wireframe design serves early-stage structural planning: information architecture definition, navigation system design, responsive layout planning, content organization taking 1-2 weeks with 1-2 designers producing sitemaps, annotated wireframes, component hierarchies. Prototype development follows validating interactions: building clickable mockups, designing micro-interactions, preparing user testing materials, stakeholder presentations requiring 1-3 weeks with 1-3 designers delivering interactive prototypes, animation specifications, simulated flows.

Design system creation addresses scalability and consistency: establishing design foundations, building component libraries, creating reusable patterns, documenting standards for development teams demanding 4-12 weeks with 2-5 designers producing comprehensive token documentation, component libraries with states, typography/color systems, accessibility guidelines. Usability testing validates decisions: planning research sessions, collecting user feedback, measuring effectiveness, identifying iteration opportunities spanning 2-4 weeks with 2-4 researchers delivering test plans, recruitment materials, data collection instruments, prioritized findings.

Choose wireframe design when starting new products or features, defining information architecture, planning responsive layouts, mapping user flows, working on structural foundation before visual polish. Choose prototype development when ready to test interactions, validating design concepts with users or stakeholders, presenting to decision-makers, designing animations and transitions, preparing for usability testing requiring realistic simulation.

Choose design system creation when scaling across products, establishing standards for multiple teams, creating reusable components preventing inconsistency, preparing for development handoff with clear specifications, building long-term design infrastructure supporting growth. Choose usability testing when validating design decisions with real users, testing prototypes or live products, measuring effectiveness through quantitative metrics, identifying usability issues for iteration, planning research studies informing strategy.

**Typical Project Workflow and Sequencing**

Most comprehensive projects follow progressive refinement sequence starting broad and narrowing to specifics. Wireframe design establishes foundation: create information architecture and navigation structure (weeks 1-2), define layout systems and component hierarchy, establish responsive behavior and breakpoints. Prototype development validates interactions: build interactive prototypes showing realistic flows (weeks 3-5), design micro-interactions and animations, prepare testing materials with realistic data, iterate based on stakeholder feedback.

Usability testing measures effectiveness: conduct user testing sessions with 5-8 participants per iteration (weeks 6-7), collect feedback and quantitative metrics (task completion, time-on-task, satisfaction), identify issues for iteration prioritizing by severity and frequency, address critical findings before proceeding. Design system creation formalizes patterns: extract reusable components from validated designs (weeks 8-16), create comprehensive token systems and documentation, build developer-ready specifications, establish governance and contribution models.

Phase durations vary by project complexity and team capacity. Simple feature additions complete wireframe-prototype-test cycle in 3-4 weeks. New product launches require 8-12 weeks covering full workflow. Enterprise design systems demand 4-6 months for comprehensive documentation and adoption. MVP projects compress timeline sacrificing comprehensiveness: essential wireframes only (1 week), high-fidelity prototype of core flow (2 weeks), lightweight component library versus full system (2 weeks), guerrilla testing versus formal research.

Iterate continuously rather than sequential waterfall. Test wireframes with 5 users revealing navigation issues before prototyping investment (Nielsen research: 5 users find 85% of problems). Prototype critical flows only initially rather than comprehensive screens. Build design system incrementally starting with most-used components (buttons, forms, navigation) expanding based on team adoption and feedback. Conduct lightweight testing throughout (hallway testing, prototype validation) supplemented by formal studies at key milestones.

**Integration Strategies Across Templates**

Connect deliverables creating cohesive design narrative. Wireframe annotations specify interaction behaviors informing prototype development: "Clicking product card expands inline details" versus navigating to new page. Prototype realistic data reveals content challenges informing information architecture refinement: extremely long product names require truncation strategies, empty states need guidance, error conditions require recovery paths.

Usability testing findings drive iteration across artifacts. Navigation confusion in testing prompts wireframe restructuring: "7 of 8 participants couldn't locate order history" suggests moving from settings to main navigation. Interaction struggles guide prototype refinement: slow form completion times (average 4 minutes versus 2-minute target) trigger progressive disclosure or field reduction. Accessibility violations caught in testing inform design system standards: insufficient color contrast ratios require palette adjustment, missing focus indicators necessitate component specification updates.

Design system standards emerge from validated patterns. Extract reusable components after testing confirms usability: successful button designs become system standards, effective form layouts template future features. Document decisions preventing future debates: "Primary CTA uses green background (#00A651) with 4.5:1 contrast ratio meeting WCAG AA" establishes consistency. Create usage guidelines based on testing insights: "Search autocomplete appears after 2-3 characters preventing premature results" codifies effective interaction timing.

Maintain single source of truth across deliverables. Figma design files serve as master with wireframes, prototypes, components coexisting enabling version control and reuse. Specifications reference design system tokens: "Use spacing-4 (16px)" versus hard-coded values enabling systematic updates. Testing documents link to specific prototype screens or components: "Task 3 tested using checkout-flow-v2.3" enabling precise result association. Update all artifacts when changes occur: button specification change propagates to wireframes, prototypes, and test materials preventing drift.

Deliver UX/UI design workflow as:

1. **PHASE ASSESSMENT** - Current project state, immediate needs, and appropriate template selection

2. **WORKFLOW ROADMAP** - Template sequence, phase timelines, deliverable dependencies, and milestone planning

3. **INTEGRATION PLAN** - Cross-deliverable connections, version control strategy, and artifact management

4. **RESOURCE ALLOCATION** - Team assignments, timeline estimates, and capacity planning per phase

5. **SUCCESS CRITERIA** - Phase completion definitions, quality gates, and validation checkpoints

---

## Usage Examples

### Example 1: SaaS Product Redesign - 16 Week Timeline
**Prompt:** Navigate UX redesign for B2B project management SaaS with 2 designers, 1 researcher, 8 engineers across 16 weeks targeting 30% task completion improvement and NPS increase from 15 to 35.

**Expected Output:** Phase 1 (weeks 1-4): Wireframe design focusing information architecture audit addressing "navigation confusing" pain point. Conduct card sorting with 15 users discovering natural groupings, tree testing validating findability (target 85%+ success rate for critical tasks). Deliver new navigation structure, annotated wireframes for 15 core screens, responsive specifications (desktop, tablet, mobile). Phase 2 (weeks 5-8): Prototype development creating interactive mockup of core workflows (project creation, task management, team collaboration) with realistic data including edge cases (100+ task lists, long project names). Implement micro-interactions (drag-drop task reordering, inline editing, real-time collaboration indicators). Deliver clickable prototype with 25 connected screens, interaction specifications, test scenarios. Phase 3 (weeks 9-10): Usability testing with 8-10 users split across 2 rounds ($10k budget = $500/participant × 10 participants × 2 rounds = moderate remote testing). Measure task completion (target 85%+), time-on-task (30% reduction versus current), SUS score (target 75+ versus current 61). Identify critical issues for iteration. Phase 4 (weeks 11-16): Design system foundation extracting validated components (navigation patterns, form elements, data tables, status indicators), documenting design tokens (color palette, typography scale, spacing system), creating developer specifications. Gradual rollout strategy using feature flags enabling opt-in beta testing with willing customers, phased by customer segment (small teams first, large enterprise last), monitoring adoption and feedback. Success metrics: 30%+ task completion improvement, NPS 35+ (20-point increase), 50% support ticket reduction, 15%+ mobile usage (from 2%).

### Example 2: Mobile App MVP - 8 Week Sprint
**Prompt:** Navigate design for fitness tracking mobile app MVP with solo designer across 8 weeks requiring iOS/Android support with zero research budget focusing AI-powered form analysis differentiator.

**Expected Output:** Week 1: Wireframe design for essential screens only (5-7 screens: onboarding, workout logging, progress tracking, video recording for AI analysis). Skip comprehensive sitemap focusing core user flow: sign up → record workout video → receive AI form feedback → view progress. Validate structure with stakeholders defining "premium feel" as: clean layouts, high-quality imagery, smooth animations, gesture-based navigation. Weeks 2-3: Prototype development building high-fidelity mockup of core workout flow with native iOS patterns (tab bar navigation, card-based layouts, SF Pro typography). Design micro-interactions: workout start countdown (3-2-1 animation), video recording progress ring, AI analysis loading state (skeleton screen showing body pose overlay), form feedback cards with visual corrections. Create both light/dark mode supporting iOS standards. Week 4: Guerrilla usability testing at local gym with 5 users (30-minute sessions, $0 budget). Validate workout flow completion (target 90%+), AI feedback comprehension (users understand corrections?), premium feel perception (meets brand expectations?). Collect video clips showing struggles for stakeholder communication. Weeks 5-6: Iteration addressing findings plus mini design system: 10 core components (buttons, input fields, cards, navigation bar, video player, progress indicators), color tokens (brand teal, success green, error red, neutral grays), typography scale (SF Pro Display headlines, SF Pro Text body). Document responsive behavior for tablet support. Weeks 7-8: Polish and developer support creating detailed specifications, preparing App Store assets (screenshots, preview video, icon variations), supporting engineering implementation questions, final QA reviewing built app versus designs. Deliverables: 15 screens high-fidelity prototype, component library with 10 elements, basic design documentation (not comprehensive system), App Store marketing assets. Timeline compressed by limiting scope: essential features only, component library versus full system, guerrilla testing versus formal research, stakeholder alignment replacing extensive research.

### Example 3: Enterprise Design System - 18 Month Rollout
**Prompt:** Navigate design system for Fortune 500 company standardizing 15 products across 40 designers, 200 engineers requiring adoption earning versus mandating with no dedicated team (50% allocation).

**Expected Output:** Months 1-3: Design system creation foundations starting with comprehensive audit across 15 products identifying common patterns (navigation, forms, tables, modals), documenting variations and inconsistencies. Establish design tokens first (color palette, typography scale, spacing system, elevation shadows) enabling platform-agnostic definitions supporting React, Angular, Vue, native mobile. Create 10-15 core components (buttons, inputs, dropdowns, checkboxes, cards) with comprehensive state specifications (default, hover, active, focus, disabled, error, success) and accessibility guidelines (WCAG AA minimum, keyboard navigation, screen reader support). Use Wireframe design template concepts for pattern auditing, Design system creation for formal documentation. Months 4-6: Pilot with 2-3 willing teams providing early feedback and demonstrating value. Conduct usability testing using product teams as users: "Can teams find and implement components easily?" Testing prototype components in real products validating usability and technical feasibility. Iterate based on implementation challenges: React team needs different spacing approach versus Angular team, mobile teams require platform-specific variants. Document learnings refining contribution model and governance. Months 7-9: Expand to 5-7 teams building comprehensive component library (30-50 components covering 80% of common UI needs). Establish contribution workflow: teams submit proposals for new components, design systems team reviews for consistency, approved components added to library. Create training program (workshops, documentation, office hours) supporting adoption. Months 10-12: Full rollout inviting all 15 teams with adoption incentives (showcase wins in company meetings, reduce design review friction for system users, provide dedicated support). Launch Figma standardization migrating teams from Sketch/XD. Implement usage tracking measuring adoption rates and component utilization. Months 13-18: Maintenance and continuous improvement based on team feedback. Establish quarterly release cycles for new components and updates. Build governance model defining decision-making (design systems team owns core components, product teams propose additions). Create contribution metrics rewarding teams submitting useful components. Adoption strategy avoiding mandates: demonstrate value through pilot wins (2-3 teams ship 40% faster using system), reduce friction (pre-built components faster than custom), provide excellent support, celebrate early adopters. Success metrics: 70%+ team adoption rate by month 18, 40% reduction in design-to-dev handoff time, 90%+ accessibility compliance (from current failures), unified brand experience across products. Usability testing approach: treat product teams as users testing documentation clarity, component findability, implementation ease with task-based scenarios ("Implement a multi-step form using system components").

---

## Cross-References

- [Wireframe Design](wireframe-design.md) - Information architecture and layout planning
- [Prototype Development](prototype-development.md) - Interactive mockups and testing preparation
- [Design System Creation](design-system-creation.md) - Component libraries and pattern documentation
- [Usability Testing Plan](usability-testing-plan.md) - User research and validation methodology
