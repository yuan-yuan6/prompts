---
title: Wireframe Design & Information Architecture
category: creative/Design & Visual
tags: [creative, design, wireframe, information-architecture, ux]
use_cases:
  - Create low-fidelity wireframes for user testing (2-3 hours for 5-7 screens)
  - Design information architecture for a new website or app section
  - Map out responsive layouts before visual design begins
related_templates:
  - prototype-development.md
  - design-system-creation.md
  - ux-ui-design-overview.md
last_updated: 2025-11-09
---

# Wireframe Design & Information Architecture

## Purpose
Create comprehensive wireframe designs and information architecture for digital products, establishing the structural foundation for user interfaces and navigation systems.

## Quick Start

**Need to create wireframes quickly?** Use this minimal example:

### Minimal Example
```
Create low-fidelity wireframes for a task management mobile app. Include: login/signup screen, task list view, task detail view, create/edit task screen, and settings. Focus on information hierarchy, navigation flow, and responsive layout for iOS and Android. Target users: busy professionals aged 25-40.
```

### When to Use This
- Starting UX design for new products or features
- Communicating structure and layout to stakeholders
- User testing before investing in high-fidelity designs
- Documenting information architecture and navigation

### Basic 3-Step Workflow
1. **Define structure** - Site map, user flows, navigation hierarchy
2. **Sketch layouts** - Low-fidelity wireframes for key screens
3. **Annotate and document** - Add notes, interactions, responsive behavior

**Time to complete**: 2-4 hours for 5-7 screens, 1-2 days for complete app

---

## Template

```
You are a UX wireframing expert. Create wireframes for [PRODUCT_NAME] targeting [USER_GROUP] with a focus on [WIREFRAME_GOAL].

PROJECT CONTEXT:
- Product name: [PRODUCT_NAME]
- Product type: [PRODUCT_TYPE] (Web App/Mobile App/Desktop/Cross-platform)
- Wireframe fidelity: [FIDELITY_LEVEL] (Low/Mid/High)
- Timeline: [PROJECT_TIMELINE]
- Primary use case: [PRIMARY_USE_CASE]
- Key user actions: [KEY_USER_ACTIONS]

### INFORMATION ARCHITECTURE

Site Structure:
- Site map: [SITE_MAP_STRUCTURE]
- Navigation hierarchy: [NAV_HIERARCHY]
- Content taxonomy: [CONTENT_TAXONOMY]
- User flow paths: [FLOW_PATHS]
- Search structure: [SEARCH_ARCHITECTURE]
- Content priorities: [CONTENT_PRIORITIES]

Navigation Design:
- Primary navigation: [PRIMARY_NAV]
- Secondary navigation: [SECONDARY_NAV]
- Mobile navigation: [MOBILE_NAV]
- Breadcrumb strategy: [BREADCRUMB_STRATEGY]
- Footer navigation: [FOOTER_NAV]
- Sitemap access: [SITEMAP_ACCESS]

Content Organization:
- Content hierarchy: [CONTENT_HIERARCHY]
- Content grouping: [CONTENT_GROUPING]
- Labeling system: [LABELING_SYSTEM]
- Content relationships: [CONTENT_RELATIONSHIPS]
- Cross-linking strategy: [CROSSLINK_STRATEGY]

### LAYOUT SYSTEM

Grid Framework:
- Grid system: [GRID_SYSTEM] (12-column/16-column/Custom)
- Breakpoints:
  - Mobile: [MOBILE_BREAKPOINT] (e.g., 320px-767px)
  - Tablet: [TABLET_BREAKPOINT] (e.g., 768px-1023px)
  - Desktop: [DESKTOP_BREAKPOINT] (e.g., 1024px-1439px)
  - Large: [LARGE_BREAKPOINT] (e.g., 1440px+)
- Container widths: [CONTAINER_WIDTHS]
- Column gaps: [COLUMN_GAPS]

Spacing System:
- Margins: [MARGIN_SPECS]
- Padding: [PADDING_SPECS]
- Gutters: [GUTTER_SPECS]
- Vertical rhythm: [VERTICAL_RHYTHM]
- White space strategy: [WHITESPACE_STRATEGY]

Layout Patterns:
- Layout type: [LAYOUT_TYPE] (Fixed/Fluid/Hybrid)
- Content alignment: [CONTENT_ALIGNMENT]
- Sidebar configuration: [SIDEBAR_CONFIG]
- Multi-column layouts: [MULTICOLUMN_LAYOUT]
- Content width limits: [WIDTH_LIMITS]

### WIREFRAME COMPONENTS

Header Components:
- Main header structure: [HEADER_WIREFRAME]
  - Logo placement: [LOGO_POSITION]
  - Logo size: [LOGO_SIZE]
- Primary navigation: [NAV_WIREFRAME]
  - Menu items: [MENU_ITEMS]
  - Dropdown structure: [DROPDOWN_STRUCTURE]
- Search functionality: [SEARCH_WIREFRAME]
  - Search placement: [SEARCH_POSITION]
  - Search behavior: [SEARCH_BEHAVIOR]
- User menu: [USER_MENU_WIREFRAME]
  - Profile access: [PROFILE_ACCESS]
  - Settings access: [SETTINGS_ACCESS]
- Mobile header: [MOBILE_HEADER_WIREFRAME]
  - Hamburger menu: [HAMBURGER_MENU]

Hero Section:
- Hero layout: [HERO_WIREFRAME]
- Headline placement: [HEADLINE_POSITION]
- Subheadline: [SUBHEADLINE_POSITION]
- Call-to-action: [CTA_PLACEMENT]
- Hero media: [HERO_MEDIA] (Image/Video/None)
- Hero height: [HERO_HEIGHT]

Content Sections:
- Feature blocks: [FEATURE_WIREFRAME]
  - Feature count: [FEATURE_COUNT]
  - Feature layout: [FEATURE_LAYOUT]
- Content cards: [CARD_WIREFRAME]
  - Card grid: [CARD_GRID]
  - Card elements: [CARD_ELEMENTS]
- List layouts: [LIST_WIREFRAME]
  - List style: [LIST_STYLE]
  - List item structure: [LIST_ITEM_STRUCTURE]
- Gallery layouts: [GALLERY_WIREFRAME]
  - Gallery grid: [GALLERY_GRID]
  - Image aspect ratio: [IMAGE_RATIO]
- Sidebar content: [SIDEBAR_WIREFRAME]
  - Widget structure: [WIDGET_STRUCTURE]

Form Wireframes:
- Form layout: [FORM_WIREFRAME]
  - Form orientation: [FORM_ORIENTATION] (Vertical/Horizontal)
  - Label placement: [LABEL_PLACEMENT]
- Input fields: [INPUT_WIREFRAME]
  - Field types: [FIELD_TYPES]
  - Field widths: [FIELD_WIDTHS]
  - Required indicators: [REQUIRED_INDICATORS]
- Button placement: [BUTTON_WIREFRAME]
  - Primary action: [PRIMARY_ACTION]
  - Secondary actions: [SECONDARY_ACTIONS]
  - Button alignment: [BUTTON_ALIGNMENT]
- Validation states: [VALIDATION_WIREFRAME]
  - Error messages: [ERROR_MESSAGE_PLACEMENT]
  - Success indicators: [SUCCESS_INDICATORS]
  - Help text: [HELP_TEXT_PLACEMENT]
- Multi-step forms: [MULTISTEP_WIREFRAME]
  - Step indicators: [STEP_INDICATORS]
  - Navigation controls: [FORM_NAV_CONTROLS]

Modal Wireframes:
- Dialog boxes: [DIALOG_WIREFRAME]
  - Modal size: [MODAL_SIZE]
  - Modal positioning: [MODAL_POSITION]
- Confirmation modals: [CONFIRM_WIREFRAME]
  - Confirmation message: [CONFIRM_MESSAGE_STRUCTURE]
  - Action buttons: [CONFIRM_BUTTONS]
- Form modals: [FORM_MODAL_WIREFRAME]
  - Modal form structure: [MODAL_FORM_STRUCTURE]
- Image galleries: [GALLERY_MODAL_WIREFRAME]
  - Gallery navigation: [GALLERY_NAV]
  - Thumbnail strip: [THUMBNAIL_STRUCTURE]
- Close mechanisms: [CLOSE_MECHANISMS]

Footer Components:
- Footer structure: [FOOTER_WIREFRAME]
- Footer columns: [FOOTER_COLUMNS]
- Footer links: [FOOTER_LINKS]
- Social media: [SOCIAL_MEDIA_PLACEMENT]
- Newsletter signup: [NEWSLETTER_WIREFRAME]
- Copyright info: [COPYRIGHT_PLACEMENT]

### PAGE WIREFRAMES

Key Pages:
1. Homepage: [HOMEPAGE_WIREFRAME]
   - Above fold content: [HOMEPAGE_ABOVE_FOLD]
   - Below fold content: [HOMEPAGE_BELOW_FOLD]

2. Product/Service page: [PRODUCT_PAGE_WIREFRAME]
   - Product details: [PRODUCT_DETAILS_STRUCTURE]
   - Product images: [PRODUCT_IMAGE_STRUCTURE]
   - Purchase flow: [PURCHASE_FLOW_WIREFRAME]

3. List/Archive page: [LIST_PAGE_WIREFRAME]
   - Filtering options: [FILTER_WIREFRAME]
   - Sorting controls: [SORT_CONTROLS]
   - Pagination: [PAGINATION_WIREFRAME]

4. Detail page: [DETAIL_PAGE_WIREFRAME]
   - Content structure: [DETAIL_CONTENT_STRUCTURE]
   - Related content: [RELATED_CONTENT_WIREFRAME]

5. User dashboard: [DASHBOARD_WIREFRAME]
   - Dashboard widgets: [DASHBOARD_WIDGETS]
   - Data visualization: [DATA_VIZ_WIREFRAME]

### RESPONSIVE BEHAVIOR

Mobile Wireframes ([MOBILE_SIZE]):
- Mobile layout: [MOBILE_LAYOUT]
- Content stacking: [CONTENT_STACKING]
- Mobile navigation: [MOBILE_NAV_PATTERN]
- Touch targets: [TOUCH_TARGET_SIZE] (minimum 44x44px)
- Mobile forms: [MOBILE_FORM_LAYOUT]
- Thumb zone optimization: [THUMB_ZONE_LAYOUT]

Tablet Wireframes ([TABLET_SIZE]):
- Tablet layout: [TABLET_LAYOUT]
- Multi-column support: [TABLET_COLUMNS]
- Orientation handling: [ORIENTATION_LAYOUT]
- Tablet navigation: [TABLET_NAV]
- Content density: [TABLET_CONTENT_DENSITY]

Desktop Wireframes ([DESKTOP_SIZE]):
- Desktop layout: [DESKTOP_LAYOUT]
- Sidebar usage: [DESKTOP_SIDEBAR]
- Advanced features: [DESKTOP_FEATURES]
- Multi-panel interface: [MULTI_PANEL_LAYOUT]

### INTERACTION NOTES

User Interactions:
- Click targets: [CLICK_TARGETS]
- Hover states: [HOVER_STATE_NOTES]
- Active states: [ACTIVE_STATE_NOTES]
- Disabled states: [DISABLED_STATE_NOTES]
- Loading states: [LOADING_STATE_NOTES]

Navigation Flow:
- Entry points: [ENTRY_POINTS]
- Primary paths: [PRIMARY_PATHS]
- Alternative paths: [ALTERNATIVE_PATHS]
- Exit points: [EXIT_POINTS]
- Error recovery: [ERROR_RECOVERY_PATHS]

### WIREFRAME OUTPUT

[Generate comprehensive wireframes with annotations]

Project: [PRODUCT_NAME]
Fidelity Level: [FIDELITY_LEVEL]
Total Screens: [SCREEN_COUNT]

Deliverables:
- Site map diagram: [SITEMAP_DELIVERABLE]
- User flow diagrams: [USERFLOW_DELIVERABLE]
- Wireframe screens: [WIREFRAME_DELIVERABLE]
- Annotation document: [ANNOTATION_DELIVERABLE]
- Component inventory: [COMPONENT_INVENTORY]

OUTPUT: Deliver complete wireframe package with:
1. Information architecture documentation
2. Annotated wireframes for all key screens
3. Responsive layout specifications
4. Component structure definitions
5. Navigation and user flow diagrams
6. Interaction notes and specifications
```

## Variables

**Core Variables** (reduce from 50+ to essentials):
- `[PRODUCT_NAME]` - Name of the product/application
- `[USER_GROUP]` - Primary target users
- `[KEY_USER_ACTIONS]` - Top 3-5 user tasks to support
- `[PRODUCT_TYPE]` - Platform (Web/Mobile/Both)
- `[FIDELITY_LEVEL]` - Low-fidelity sketch or mid-fidelity clickable
- `[SCREEN_COUNT]` - Number of unique screens needed

## Usage Examples

### Example 1: E-commerce Product Catalog
```
PRODUCT_NAME: "ShopEasy Marketplace"
USER_GROUP: "Online shoppers aged 25-45"
WIREFRAME_GOAL: "Streamlined product discovery and checkout"
PRODUCT_TYPE: "Responsive Web App"
FIDELITY_LEVEL: "Mid-fidelity"
GRID_SYSTEM: "12-column grid"
```

### Example 2: Mobile Banking App
```
PRODUCT_NAME: "QuickBank Mobile"
USER_GROUP: "Mobile banking users"
WIREFRAME_GOAL: "Secure and intuitive financial management"
PRODUCT_TYPE: "Mobile App"
FIDELITY_LEVEL: "High-fidelity"
GRID_SYSTEM: "8-column mobile grid"
```

### Example 3: SaaS Admin Dashboard
```
PRODUCT_NAME: "AdminPro Dashboard"
USER_GROUP: "System administrators"
WIREFRAME_GOAL: "Efficient system management interface"
PRODUCT_TYPE: "Web App"
FIDELITY_LEVEL: "Low-fidelity"
GRID_SYSTEM: "16-column grid"
```

## Best Practices

1. **Start with paper sketches, not software** - 10 rough sketches beat 1 perfect wireframe for ideation
2. **Use real content, not Lorem Ipsum** - "Join 50,000 users" reveals layout issues that placeholder text hides
3. **Show mobile and desktop side-by-side** - Catch responsiveness issues early, not after development starts
4. **Annotate interactions, don't assume** - "User clicks → dropdown appears" prevents costly misunderstandings
5. **Test wireframes with 3-5 users before polishing** - One round of feedback saves weeks of revision

## Tips for Success

- Use real content when possible instead of Lorem Ipsum
- Establish clear visual hierarchy with size and spacing
- Design for thumb-friendly mobile interactions
- Include annotations for dynamic content and interactions
- Create wireframes for key user flows, not just individual screens
- Consider edge cases and error states in your wireframes
- Validate navigation structure with card sorting exercises
- Test information architecture with tree testing
- Use wireframe components consistently across screens
- Document design decisions and rationale for stakeholders
