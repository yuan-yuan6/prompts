---
category: design
last_updated: 2025-11-09
related_templates:
- design/wireframe-design.md
- design/prototype-development.md
- design/ux-ui-design-overview.md
tags:
- design
title: Design System & Component Library
use_cases:
- Creating comprehensive design systems and style guides
- Building reusable component libraries
- Establishing brand consistency across products
industries:
- healthcare
- technology
type: template
difficulty: intermediate
slug: design-system-creation
---

# Design System & Component Library

## Purpose
Create comprehensive design systems with reusable components, design tokens, and style guidelines to ensure consistency, scalability, and efficiency across digital products.

## Quick Start

To use this template effectively:

1. **Establish Foundations** - Start with color palette, typography scale, and spacing system before building components
2. **Define Design Principles** - Create 3-5 core principles that guide all design decisions
3. **Build Core Components** - Begin with the most-used elements: buttons, form inputs, cards, and navigation
4. **Create Design Tokens** - Abstract your design values (colors, spacing, typography) into reusable tokens
5. **Document Everything** - For each component, include anatomy, usage guidelines, states, and code examples

**Pro Tip**: Audit your existing designs first to identify the most frequently used patterns, then standardize those before creating new components.

## Template

```
You are a design system expert. Create a comprehensive design system for [PRODUCT_NAME] targeting [USER_GROUP] with a focus on [SYSTEM_GOAL].

PROJECT CONTEXT:
- Product name: [PRODUCT_NAME]
- Brand identity: [BRAND_IDENTITY]
- Platform scope: [PLATFORM_SCOPE] (Web/Mobile/Cross-platform)
- System scale: [SYSTEM_SCALE] (Single product/Product family)
- Design language: [DESIGN_LANGUAGE]
- Implementation framework: [FRAMEWORK] (React/Vue/Angular/Native)

### DESIGN FOUNDATIONS

Brand Principles:
- Brand mission: [BRAND_MISSION]
- Design philosophy: [DESIGN_PHILOSOPHY]
- Core values: [CORE_VALUES]
- Visual personality: [VISUAL_PERSONALITY]
- Voice and tone: [VOICE_TONE]

Design Principles:
1. [PRINCIPLE_1]: [PRINCIPLE_1_DESCRIPTION]
2. [PRINCIPLE_2]: [PRINCIPLE_2_DESCRIPTION]
3. [PRINCIPLE_3]: [PRINCIPLE_3_DESCRIPTION]
4. [PRINCIPLE_4]: [PRINCIPLE_4_DESCRIPTION]
5. [PRINCIPLE_5]: [PRINCIPLE_5_DESCRIPTION]

### COLOR SYSTEM

Primary Palette:
- Primary color: [PRIMARY_COLOR]
  - Primary 50: [PRIMARY_50]
  - Primary 100: [PRIMARY_100]
  - Primary 200: [PRIMARY_200]
  - Primary 300: [PRIMARY_300]
  - Primary 400: [PRIMARY_400]
  - Primary 500: [PRIMARY_500] (Base)
  - Primary 600: [PRIMARY_600]
  - Primary 700: [PRIMARY_700]
  - Primary 800: [PRIMARY_800]
  - Primary 900: [PRIMARY_900]

- Secondary color: [SECONDARY_COLOR]
  - Secondary shades: [SECONDARY_SHADES]

- Tertiary color: [TERTIARY_COLOR]
  - Tertiary shades: [TERTIARY_SHADES]

Neutral Palette:
- Gray scale: [GRAY_SCALE]
  - Gray 50: [GRAY_50] (Lightest)
  - Gray 100-900: [GRAY_SHADES]
  - Gray 950: [GRAY_950] (Darkest)
- Black: [BLACK_VALUE]
- White: [WHITE_VALUE]

Semantic Colors:
- Success: [SUCCESS_COLOR]
  - Success shades: [SUCCESS_SHADES]
- Warning: [WARNING_COLOR]
  - Warning shades: [WARNING_SHADES]
- Error: [ERROR_COLOR]
  - Error shades: [ERROR_SHADES]
- Info: [INFO_COLOR]
  - Info shades: [INFO_SHADES]

Background Colors:
- Primary background: [BG_PRIMARY]
- Secondary background: [BG_SECONDARY]
- Tertiary background: [BG_TERTIARY]
- Overlay background: [BG_OVERLAY]
- Elevated background: [BG_ELEVATED]

Text Colors:
- Primary text: [TEXT_PRIMARY]
- Secondary text: [TEXT_SECONDARY]
- Tertiary text: [TEXT_TERTIARY]
- Disabled text: [TEXT_DISABLED]
- Link text: [TEXT_LINK]

### TYPOGRAPHY SYSTEM

Font Families:
- Primary font: [PRIMARY_FONT]
  - Font fallback: [PRIMARY_FALLBACK]
  - Character sets: [PRIMARY_CHARSET]
- Secondary font: [SECONDARY_FONT]
  - Font fallback: [SECONDARY_FALLBACK]
  - Use cases: [SECONDARY_USAGE]
- Monospace font: [MONO_FONT]
  - Use cases: [MONO_USAGE]

Type Scale:
- Display: [DISPLAY_SIZE] / [DISPLAY_LINE_HEIGHT] / [DISPLAY_WEIGHT]
- H1: [H1_SIZE] / [H1_LINE_HEIGHT] / [H1_WEIGHT]
- H2: [H2_SIZE] / [H2_LINE_HEIGHT] / [H2_WEIGHT]
- H3: [H3_SIZE] / [H3_LINE_HEIGHT] / [H3_WEIGHT]
- H4: [H4_SIZE] / [H4_LINE_HEIGHT] / [H4_WEIGHT]
- H5: [H5_SIZE] / [H5_LINE_HEIGHT] / [H5_WEIGHT]
- H6: [H6_SIZE] / [H6_LINE_HEIGHT] / [H6_WEIGHT]
- Body Large: [BODY_L_SIZE] / [BODY_L_LINE_HEIGHT] / [BODY_L_WEIGHT]
- Body: [BODY_SIZE] / [BODY_LINE_HEIGHT] / [BODY_WEIGHT]
- Body Small: [BODY_S_SIZE] / [BODY_S_LINE_HEIGHT] / [BODY_S_WEIGHT]
- Caption: [CAPTION_SIZE] / [CAPTION_LINE_HEIGHT] / [CAPTION_WEIGHT]
- Overline: [OVERLINE_SIZE] / [OVERLINE_LINE_HEIGHT] / [OVERLINE_WEIGHT]

Typography Properties:
- Letter spacing: [LETTER_SPACING_SCALE]
- Text transform: [TEXT_TRANSFORM_RULES]
- Text decoration: [TEXT_DECORATION_RULES]
- Font smoothing: [FONT_SMOOTHING]

### SPACING SYSTEM

Spacing Scale:
- 0: [SPACE_0] (0px)
- 1: [SPACE_1] (4px)
- 2: [SPACE_2] (8px)
- 3: [SPACE_3] (12px)
- 4: [SPACE_4] (16px)
- 5: [SPACE_5] (24px)
- 6: [SPACE_6] (32px)
- 7: [SPACE_7] (48px)
- 8: [SPACE_8] (64px)
- 9: [SPACE_9] (96px)
- 10: [SPACE_10] (128px)

Layout Spacing:
- Container padding: [CONTAINER_PADDING]
- Section spacing: [SECTION_SPACING]
- Component spacing: [COMPONENT_SPACING]
- Element spacing: [ELEMENT_SPACING]

### LAYOUT SYSTEM

Grid System:
- Grid columns: [GRID_COLUMNS]
- Grid gap: [GRID_GAP]
- Container max-width: [CONTAINER_MAX_WIDTH]
- Breakpoints:
  - xs: [BREAKPOINT_XS]
  - sm: [BREAKPOINT_SM]
  - md: [BREAKPOINT_MD]
  - lg: [BREAKPOINT_LG]
  - xl: [BREAKPOINT_XL]
  - 2xl: [BREAKPOINT_2XL]

### COMPONENT LIBRARY

Button Components:
- Primary button:
  - Default: [PRIMARY_BTN_DEFAULT]
  - Hover: [PRIMARY_BTN_HOVER]
  - Active: [PRIMARY_BTN_ACTIVE]
  - Disabled: [PRIMARY_BTN_DISABLED]
  - Sizes: [PRIMARY_BTN_SIZES]
  - Padding: [PRIMARY_BTN_PADDING]
  - Border radius: [PRIMARY_BTN_RADIUS]

- Secondary button:
  - Default: [SECONDARY_BTN_DEFAULT]
  - States: [SECONDARY_BTN_STATES]
  - Sizes: [SECONDARY_BTN_SIZES]

- Tertiary/Ghost button:
  - Default: [TERTIARY_BTN_DEFAULT]
  - States: [TERTIARY_BTN_STATES]
  - Sizes: [TERTIARY_BTN_SIZES]

- Icon button:
  - Default: [ICON_BTN_DEFAULT]
  - States: [ICON_BTN_STATES]
  - Sizes: [ICON_BTN_SIZES]

Form Components:
- Text input:
  - Height: [INPUT_HEIGHT]
  - Padding: [INPUT_PADDING]
  - Border: [INPUT_BORDER]
  - Border radius: [INPUT_RADIUS]
  - States: [INPUT_STATES]
  - Variants: [INPUT_VARIANTS]

- Select dropdown:
  - Design: [SELECT_DESIGN]
  - Menu styling: [SELECT_MENU]
  - States: [SELECT_STATES]

- Checkbox:
  - Size: [CHECKBOX_SIZE]
  - Design: [CHECKBOX_DESIGN]
  - States: [CHECKBOX_STATES]

- Radio button:
  - Size: [RADIO_SIZE]
  - Design: [RADIO_DESIGN]
  - States: [RADIO_STATES]

- Toggle switch:
  - Size: [TOGGLE_SIZE]
  - Design: [TOGGLE_DESIGN]
  - Animation: [TOGGLE_ANIMATION]

- Textarea:
  - Min height: [TEXTAREA_MIN_HEIGHT]
  - Resize: [TEXTAREA_RESIZE]
  - States: [TEXTAREA_STATES]

Card Components:
- Base card:
  - Background: [CARD_BACKGROUND]
  - Border: [CARD_BORDER]
  - Border radius: [CARD_RADIUS]
  - Padding: [CARD_PADDING]
  - Shadow: [CARD_SHADOW]

- Card variants:
  - Elevated: [CARD_ELEVATED]
  - Outlined: [CARD_OUTLINED]
  - Interactive: [CARD_INTERACTIVE]

- Card sections:
  - Header: [CARD_HEADER]
  - Body: [CARD_BODY]
  - Footer: [CARD_FOOTER]

Navigation Components:
- Top navigation:
  - Height: [TOPNAV_HEIGHT]
  - Background: [TOPNAV_BG]
  - Items: [TOPNAV_ITEMS]
  - Dropdown: [TOPNAV_DROPDOWN]

- Side navigation:
  - Width: [SIDENAV_WIDTH]
  - Collapsed width: [SIDENAV_COLLAPSED]
  - Items: [SIDENAV_ITEMS]
  - Submenus: [SIDENAV_SUBMENU]

- Tabs:
  - Height: [TAB_HEIGHT]
  - Active indicator: [TAB_INDICATOR]
  - States: [TAB_STATES]

- Breadcrumbs:
  - Separator: [BREADCRUMB_SEPARATOR]
  - Styling: [BREADCRUMB_STYLE]

- Pagination:
  - Design: [PAGINATION_DESIGN]
  - States: [PAGINATION_STATES]

Modal Components:
- Basic modal:
  - Width: [MODAL_WIDTH]
  - Max height: [MODAL_MAX_HEIGHT]
  - Background: [MODAL_BG]
  - Overlay: [MODAL_OVERLAY]
  - Border radius: [MODAL_RADIUS]

- Dialog variants:
  - Confirmation: [DIALOG_CONFIRM]
  - Form: [DIALOG_FORM]
  - Alert: [DIALOG_ALERT]

Feedback Components:
- Alert/Banner:
  - Variants: [ALERT_VARIANTS]
  - Icons: [ALERT_ICONS]
  - Close button: [ALERT_CLOSE]

- Toast/Snackbar:
  - Position: [TOAST_POSITION]
  - Duration: [TOAST_DURATION]
  - Variants: [TOAST_VARIANTS]

- Progress indicators:
  - Linear: [PROGRESS_LINEAR]
  - Circular: [PROGRESS_CIRCULAR]
  - Skeleton: [PROGRESS_SKELETON]

### ICONOGRAPHY

Icon System:
- Icon library: [ICON_LIBRARY]
- Icon sizes: [ICON_SIZES]
- Icon colors: [ICON_COLORS]
- Icon style: [ICON_STYLE] (Filled/Outlined/Rounded)
- Custom icons: [CUSTOM_ICONS]

### ELEVATION & SHADOWS

Shadow Scale:
- Shadow none: [SHADOW_NONE]
- Shadow sm: [SHADOW_SM]
- Shadow md: [SHADOW_MD]
- Shadow lg: [SHADOW_LG]
- Shadow xl: [SHADOW_XL]
- Shadow 2xl: [SHADOW_2XL]
- Shadow inner: [SHADOW_INNER]

Elevation Levels:
- Level 0: [ELEVATION_0] (Flat)
- Level 1: [ELEVATION_1] (Cards)
- Level 2: [ELEVATION_2] (Dropdowns)
- Level 3: [ELEVATION_3] (Modals)
- Level 4: [ELEVATION_4] (Overlays)

### ANIMATION & MOTION

Timing Functions:
- Linear: [TIMING_LINEAR]
- Ease: [TIMING_EASE]
- Ease-in: [TIMING_EASE_IN]
- Ease-out: [TIMING_EASE_OUT]
- Ease-in-out: [TIMING_EASE_IN_OUT]
- Custom: [TIMING_CUSTOM]

Duration Scale:
- Instant: [DURATION_INSTANT] (0ms)
- Fast: [DURATION_FAST] (100ms)
- Normal: [DURATION_NORMAL] (200ms)
- Moderate: [DURATION_MODERATE] (300ms)
- Slow: [DURATION_SLOW] (500ms)

### ACCESSIBILITY STANDARDS

WCAG Compliance:
- Target level: [WCAG_LEVEL] (A/AA/AAA)
- Color contrast: [CONTRAST_RATIOS]
  - Normal text: [CONTRAST_NORMAL] (minimum 4.5:1)
  - Large text: [CONTRAST_LARGE] (minimum 3:1)
- Focus indicators: [FOCUS_INDICATORS]
- Touch targets: [TOUCH_TARGET_MIN] (minimum 44x44px)
- Font size minimums: [FONT_SIZE_MIN]

### DESIGN TOKENS

Token Structure:
- Color tokens: [COLOR_TOKENS]
- Spacing tokens: [SPACING_TOKENS]
- Typography tokens: [TYPOGRAPHY_TOKENS]
- Shadow tokens: [SHADOW_TOKENS]
- Border radius tokens: [RADIUS_TOKENS]
- Animation tokens: [ANIMATION_TOKENS]

### DOCUMENTATION

Component Documentation:
- Component anatomy: [COMPONENT_ANATOMY]
- Usage guidelines: [USAGE_GUIDELINES]
- Best practices: [COMPONENT_BEST_PRACTICES]
- Accessibility notes: [ACCESSIBILITY_NOTES]
- Code examples: [CODE_EXAMPLES]

### DESIGN SYSTEM OUTPUT

[Generate comprehensive design system documentation]

System Name: [SYSTEM_NAME]
Version: [SYSTEM_VERSION]
Platform: [PLATFORM_SCOPE]

Deliverables:
- Design token file: [TOKEN_FILE]
- Component library: [COMPONENT_LIBRARY]
- Style guide: [STYLE_GUIDE]
- Icon set: [ICON_SET]
- Pattern library: [PATTERN_LIBRARY]
- Implementation guide: [IMPLEMENTATION_GUIDE]

OUTPUT: Deliver complete design system with:
1. Comprehensive design tokens
2. Full component library with all states
3. Typography and color systems
4. Spacing and layout specifications
5. Accessibility guidelines
6. Implementation documentation
7. Usage examples and best practices
```

## Variables

**Essential Variables** (10):
- `[PRODUCT_NAME]` - Product or system name
- `[BRAND_IDENTITY]` - Brand characteristics
- `[SYSTEM_GOAL]` - Purpose of the design system
- `[PLATFORM_SCOPE]` - Platforms covered
- `[PRIMARY_COLOR]` - Main brand color
- `[PRIMARY_FONT]` - Main typeface
- `[GRID_COLUMNS]` - Grid structure
- `[WCAG_LEVEL]` - Accessibility target
- `[FRAMEWORK]` - Implementation technology
- `[SYSTEM_VERSION]` - Version number

## Usage Examples

### Example 1: SaaS Product Design System
```
PRODUCT_NAME: "CloudOps Platform"
BRAND_IDENTITY: "Professional, trustworthy, modern"
SYSTEM_GOAL: "Unified experience across product suite"
PLATFORM_SCOPE: "Web application"
PRIMARY_COLOR: "#0066FF"
PRIMARY_FONT: "Inter"
WCAG_LEVEL: "AA"
```

### Example 2: Mobile App Design System
```
PRODUCT_NAME: "FitLife Health App"
BRAND_IDENTITY: "Energetic, friendly, motivating"
SYSTEM_GOAL: "Consistent mobile experience"
PLATFORM_SCOPE: "iOS and Android"
PRIMARY_COLOR: "#00D084"
PRIMARY_FONT: "SF Pro / Roboto"
WCAG_LEVEL: "AA"
```

### Example 3: E-commerce Design System
```
PRODUCT_NAME: "ShopWave Marketplace"
BRAND_IDENTITY: "Vibrant, trustworthy, easy-to-use"
SYSTEM_GOAL: "Scalable component library"
PLATFORM_SCOPE: "Responsive web"
PRIMARY_COLOR: "#FF6B35"
PRIMARY_FONT: "Poppins"
WCAG_LEVEL: "AAA"
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Wireframe Design](wireframe-design.md)** - Complementary approaches and methodologies
- **[Prototype Development](prototype-development.md)** - Complementary approaches and methodologies
- **[Ux Ui Design Overview](ux-ui-design-overview.md)** - Complementary approaches and methodologies

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Design System & Component Library)
2. Use [Wireframe Design](wireframe-design.md) for deeper analysis
3. Apply [Prototype Development](prototype-development.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[creative/Design & Visual](../../creative/Design & Visual/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating comprehensive design systems and style guides**: Combine this template with related analytics and strategy frameworks
- **Building reusable component libraries**: Combine this template with related analytics and strategy frameworks
- **Establishing brand consistency across products**: Combine this template with related analytics and strategy frameworks

## Best Practices

1. **Start with foundations** - Establish colors, typography, and spacing first
2. **Use design tokens** - Abstract values for easy theming and updates
3. **Document everything** - Clear documentation ensures correct usage
4. **Design for scalability** - Build systems that grow with the product
5. **Maintain consistency** - Use the same patterns across all components
6. **Test accessibility** - Verify WCAG compliance for all components
7. **Version your system** - Track changes and communicate updates
8. **Provide examples** - Show both good and bad usage patterns
9. **Make it searchable** - Easy-to-navigate documentation is essential
10. **Gather feedback** - Regularly collect input from designers and developers

## Tips for Success

- Audit existing designs before creating new components
- Create a component priority list based on usage frequency
- Design components with composition in mind
- Include dark mode from the start if needed
- Build prototypes to test the system before full implementation
- Establish governance for maintaining the design system
- Create Figma/Sketch libraries alongside documentation
- Include real content in examples, not Lorem Ipsum
- Plan for internationalization and localization
- Set up automated accessibility testing where possible
