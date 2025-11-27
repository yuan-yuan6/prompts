---
category: technology
last_updated: 2025-11-09
related_templates:
- technology/cloud-architecture-framework.md
- technology/site-reliability-engineering.md
- technology/cloud-migration-strategy.md
tags:
- frontend-development
- react-vue-angular
- responsive-design
- pwa
title: Frontend Development & Web Application Framework
use_cases:
- Creating comprehensive framework for frontend web development including modern javascript
  frameworks, responsive design, performance optimization, accessibility standards,
  and progressive web applications.
- Project planning and execution
- Strategy development
industries:
- manufacturing
- technology
type: template
difficulty: intermediate
slug: frontend-development
---

# Frontend Development & Web Application Framework

## Purpose
Comprehensive framework for frontend web development including modern JavaScript frameworks, responsive design, performance optimization, accessibility standards, and progressive web applications.

## Quick Frontend Prompt
Build [application type] with [React/Vue/Next.js] + TypeScript. Stack: [UI: Tailwind/MUI], [state: Redux/Zustand], [API: React Query/SWR]. Features: [component list]. Performance: Lighthouse >90, code splitting, lazy loading. Accessibility: WCAG AA, keyboard nav, ARIA. Testing: [Jest/Vitest] + [Cypress/Playwright]. Deploy: [Vercel/Netlify/AWS].

## Quick Start

**Build production-ready frontend in 5 steps:**

1. **Bootstrap Project**: Initialize with Vite/Create-React-App/Next.js, configure TypeScript, ESLint, Prettier, Git hooks
2. **Set Up Component Library**: Install UI framework (Material-UI/Tailwind), create design system with atoms/molecules/organisms
3. **Implement State Management**: Configure Redux Toolkit/Zustand/Context API, set up API client (React Query/SWR)
4. **Optimize Performance**: Enable code splitting, lazy loading, image optimization, caching; target Lighthouse score >90
5. **Ensure Accessibility**: Implement ARIA labels, keyboard navigation, color contrast (WCAG AA), test with screen readers

**Quick React Setup:**
```bash
# Create project
npm create vite@latest my-app -- --template react-ts
cd my-app && npm install

# Add essential dependencies
npm install @tanstack/react-query axios tailwindcss
npm install -D @testing-library/react vitest

# Configure Tailwind
npx tailwindcss init -p
```

```tsx
// Quick component with best practices
import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';

export function UserList() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: () => fetch('/api/users').then(r => r.json())
  });

  if (isLoading) return <div role="status">Loading...</div>;
  if (error) return <div role="alert">Error loading users</div>;

  return (
    <ul className="space-y-2" aria-label="User list">
      {data.map(user => (
        <li key={user.id} className="p-4 hover:bg-gray-100">
          {user.name}
        </li>
      ))}
    </ul>
  );
}
```

## Template

Develop frontend application [APP_NAME] using [FRAMEWORK] targeting [USER_BASE] users, with [PAGE_COUNT] pages/views, [COMPONENT_COUNT] components, achieving [PERFORMANCE_SCORE] Lighthouse score, and [ACCESSIBILITY_LEVEL] accessibility compliance.

### 1. Technology Stack & Architecture

| **Stack Layer** | **Technology** | **Version** | **Purpose** | **Alternatives Considered** | **Decision Rationale** |
|----------------|---------------|------------|-----------|---------------------------|----------------------|
| Framework | [FRAMEWORK_CHOICE] | [FRAMEWORK_VER] | [FRAMEWORK_PURPOSE] | [FRAMEWORK_ALT] | [FRAMEWORK_REASON] |
| State Management | [STATE_CHOICE] | [STATE_VER] | [STATE_PURPOSE] | [STATE_ALT] | [STATE_REASON] |
| Styling Solution | [STYLE_CHOICE] | [STYLE_VER] | [STYLE_PURPOSE] | [STYLE_ALT] | [STYLE_REASON] |
| Build Tool | [BUILD_CHOICE] | [BUILD_VER] | [BUILD_PURPOSE] | [BUILD_ALT] | [BUILD_REASON] |
| Testing Framework | [TEST_CHOICE] | [TEST_VER] | [TEST_PURPOSE] | [TEST_ALT] | [TEST_REASON] |
| Package Manager | [PACKAGE_CHOICE] | [PACKAGE_VER] | [PACKAGE_PURPOSE] | [PACKAGE_ALT] | [PACKAGE_REASON] |

### 2. Component Architecture

**Component Design System:**
```
Atomic Design Structure:
Atoms (Base Components):
- Buttons: [BUTTON_VARIANTS]
- Inputs: [INPUT_TYPES]
- Typography: [TYPE_SCALES]
- Icons: [ICON_COUNT]
- Colors: [COLOR_PALETTE]

Molecules (Composite Components):
- Forms: [FORM_COMPONENTS]
- Cards: [CARD_VARIANTS]
- Navigation Items: [NAV_ITEMS]
- Alerts: [ALERT_TYPES]
- Modals: [MODAL_TYPES]

Organisms (Complex Components):
- Headers: [HEADER_VARIANTS]
- Footers: [FOOTER_VARIANTS]
- Navigation: [NAV_PATTERNS]
- Data Tables: [TABLE_FEATURES]
- Dashboards: [DASHBOARD_TYPES]

Templates (Page Structures):
- Landing Pages: [LANDING_TEMPLATES]
- Admin Pages: [ADMIN_TEMPLATES]
- User Pages: [USER_TEMPLATES]
- Auth Pages: [AUTH_TEMPLATES]
- Error Pages: [ERROR_TEMPLATES]
```

## Variables

| Variable | Description | Example |
|----------|-------------|----------|
| `[APP_NAME]` | Name of the app | "ShopFront", "AdminDashboard", "CustomerPortal", "MarketingHub" |
| `[FRAMEWORK]` | Specify the framework | "React 18 with Next.js 14", "Vue 3 with Nuxt 3", "Angular 17", "Svelte with SvelteKit" |
| `[USER_BASE]` | Specify the user base | "100K monthly active users", "1M+ consumer users", "5K enterprise employees", "Global audience across 50 countries" |
| `[PAGE_COUNT]` | Specify the page count | "10" |
| `[COMPONENT_COUNT]` | Specify the component count | "10" |
| `[PERFORMANCE_SCORE]` | Specify the performance score | "90+ Lighthouse score", "95+ for mobile", "LCP < 2.5s, FID < 100ms", "Core Web Vitals passing" |
| `[ACCESSIBILITY_LEVEL]` | Specify the accessibility level | "WCAG 2.1 AA", "WCAG 2.1 AAA for critical paths", "Section 508 compliant", "Full keyboard navigation support" |
| `[FRAMEWORK_CHOICE]` | Specify the framework choice | "React 18", "Next.js 14", "Vue 3", "Angular 17", "Svelte 4" |
| `[FRAMEWORK_VER]` | Specify the framework ver | "18.2.0", "14.0.0", "3.4.0", "17.0.0", "4.2.0" |
| `[FRAMEWORK_PURPOSE]` | Specify the framework purpose | "Component-based UI with virtual DOM", "Full-stack React with SSR/SSG", "Progressive framework for SPAs", "Enterprise-scale applications" |
| `[FRAMEWORK_ALT]` | Specify the framework alt | "Vue 3, Angular, Svelte", "Remix, Gatsby", "React, Angular", "React, Vue" |
| `[FRAMEWORK_REASON]` | Specify the framework reason | "Large ecosystem, team expertise, hiring pool", "Built-in SSR, file-based routing, API routes", "Gentle learning curve, excellent docs", "Full TypeScript support, enterprise features" |
| `[STATE_CHOICE]` | Specify the state choice | "Redux Toolkit", "Zustand", "Pinia", "NgRx", "React Query" |
| `[STATE_VER]` | Specify the state ver | "2.0.0", "4.4.0", "2.1.0", "17.0.0", "5.0.0" |
| `[STATE_PURPOSE]` | Specify the state purpose | "Global state with predictable updates", "Lightweight state management", "Vue-native state management", "Server state caching and sync" |
| `[STATE_ALT]` | Specify the state alt | "Zustand, Jotai, MobX", "Redux, Context API", "Vuex (legacy)", "Apollo Client, SWR" |
| `[STATE_REASON]` | Specify the state reason | "DevTools support, middleware, team familiarity", "Minimal boilerplate, TypeScript-first", "Official Vue solution, composable stores", "Automatic caching, background refetch" |
| `[STYLE_CHOICE]` | Specify the style choice | "Tailwind CSS", "styled-components", "CSS Modules", "Emotion", "Sass/SCSS" |
| `[STYLE_VER]` | Specify the style ver | "3.4.0", "6.1.0", "N/A (built-in)", "11.11.0", "1.69.0" |
| `[STYLE_PURPOSE]` | Specify the style purpose | "Utility-first rapid styling", "Component-scoped CSS-in-JS", "Scoped CSS without runtime", "Flexible CSS-in-JS with theming" |
| `[STYLE_ALT]` | Specify the style alt | "CSS Modules, Sass", "Emotion, vanilla-extract", "Tailwind, styled-components", "styled-components, CSS Modules" |
| `[STYLE_REASON]` | Specify the style reason | "Fast development, consistent design system", "Co-located styles, dynamic theming", "Zero runtime overhead, familiar CSS", "Theme provider, TypeScript support" |
| `[BUILD_CHOICE]` | Specify the build choice | "Vite", "Webpack 5", "Turbopack", "esbuild", "Rollup" |
| `[BUILD_VER]` | Specify the build ver | "5.0.0", "5.89.0", "1.0.0", "0.19.0", "4.9.0" |
| `[BUILD_PURPOSE]` | Specify the build purpose | "Fast HMR, ESM-native bundling", "Mature ecosystem, extensive plugins", "Next.js optimized bundler", "Extremely fast bundling" |
| `[BUILD_ALT]` | Specify the build alt | "Webpack, Parcel", "Vite, esbuild", "Vite, Webpack", "Vite, Webpack" |
| `[BUILD_REASON]` | Specify the build reason | "10x faster HMR, native ESM support", "Plugin ecosystem, custom configuration", "Integrated with Next.js, incremental builds", "Speed for large codebases" |
| `[TEST_CHOICE]` | Specify the test choice | "Vitest", "Jest", "Playwright", "Cypress", "Testing Library" |
| `[TEST_VER]` | Specify the test ver | "1.0.0", "29.7.0", "1.40.0", "13.6.0", "14.1.0" |
| `[TEST_PURPOSE]` | Specify the test purpose | "Unit/integration testing with Vite", "Full-featured test runner", "Cross-browser E2E testing", "E2E with real browser" |
| `[TEST_ALT]` | Specify the test alt | "Jest, Mocha", "Vitest, Mocha", "Cypress, Selenium", "Playwright, Puppeteer" |
| `[TEST_REASON]` | Specify the test reason | "Native Vite support, fast execution", "Mature ecosystem, snapshot testing", "Multi-browser, auto-wait, codegen", "Real browser testing, great DX" |
| `[PACKAGE_CHOICE]` | Specify the package choice | "pnpm", "npm", "yarn", "bun" |
| `[PACKAGE_VER]` | Specify the package ver | "8.10.0", "10.2.0", "4.0.0", "1.0.0" |
| `[PACKAGE_PURPOSE]` | Specify the package purpose | "Fast, disk-efficient package management", "Default Node.js package manager", "Workspaces, plug'n'play", "All-in-one JavaScript runtime" |
| `[PACKAGE_ALT]` | Specify the package alt | "npm, yarn", "pnpm, yarn", "npm, pnpm", "npm, pnpm, yarn" |
| `[PACKAGE_REASON]` | Specify the package reason | "3x faster installs, shared dependencies", "Universal availability, no setup", "Monorepo support, caching", "Fastest package installation" |
| `[BUTTON_VARIANTS]` | Specify the button variants | "Primary, Secondary, Outline, Ghost, Link, Destructive", "Solid, Soft, Plain, Icon-only", "With icon, Loading state, Disabled" |
| `[INPUT_TYPES]` | Type or category of input s | "Standard" |
| `[TYPE_SCALES]` | Type or category of scales | "Standard" |
| `[ICON_COUNT]` | Specify the icon count | "10" |
| `[COLOR_PALETTE]` | Specify the color palette | "Primary: blue-600, Secondary: gray-500, Accent: amber-400, Success: green-500, Error: red-500", "Brand colors with semantic variants" |
| `[FORM_COMPONENTS]` | Specify the form components | "Input, Select, Checkbox, Radio, DatePicker, FileUpload, Autocomplete", "Form groups with validation states" |
| `[CARD_VARIANTS]` | Specify the card variants | "Basic, Elevated, Outlined, Interactive, Image card, Stat card", "Horizontal and vertical layouts" |
| `[NAV_ITEMS]` | Specify the nav items | "NavLink, NavDropdown, NavDivider, NavGroup", "Mobile hamburger menu, Breadcrumbs" |
| `[ALERT_TYPES]` | Type or category of alert s | "Standard" |
| `[MODAL_TYPES]` | Type or category of modal s | "Standard" |
| `[HEADER_VARIANTS]` | Specify the header variants | "Sticky header, Transparent header, Minimal header, Dashboard header with search", "Mobile-responsive with drawer" |
| `[FOOTER_VARIANTS]` | Specify the footer variants | "Simple footer, Multi-column footer, Newsletter footer, Minimal copyright footer" |
| `[NAV_PATTERNS]` | Specify the nav patterns | "Top navigation bar, Sidebar navigation, Bottom tab bar (mobile), Mega menu", "Collapsible sidebar with icons" |
| `[TABLE_FEATURES]` | Specify the table features | "Sorting, Filtering, Pagination, Row selection, Column resizing, Export to CSV", "Virtual scrolling for large datasets" |
| `[DASHBOARD_TYPES]` | Type or category of dashboard s | "Standard" |
| `[LANDING_TEMPLATES]` | Specify the landing templates | "Hero with CTA, Feature grid, Pricing table, Testimonials, FAQ accordion", "Product showcase, Newsletter signup" |
| `[ADMIN_TEMPLATES]` | Specify the admin templates | "Dashboard overview, Data tables, Settings page, User management, Analytics view", "CRUD interfaces, Form wizards" |
| `[USER_TEMPLATES]` | Specify the user templates | "Profile page, Settings, Notifications, Activity feed, Favorites/Saved items", "Order history, Account management" |
| `[AUTH_TEMPLATES]` | Specify the auth templates | "Login form, Registration, Password reset, Email verification, 2FA setup", "Social login buttons, Magic link" |
| `[ERROR_TEMPLATES]` | Specify the error templates | "404 Not Found, 500 Server Error, 403 Forbidden, Maintenance mode", "Offline fallback, Session expired" |
| `[MOBILE_DEVICES]` | Specify the mobile devices | "iPhone 12/13/14, Samsung Galaxy S21+, Pixel 6", "320px-767px viewport range" |
| `[MOBILE_LAYOUT]` | Specify the mobile layout | "Single column, stacked navigation, bottom sheet modals", "Touch-optimized buttons (44px min), swipe gestures" |
| `[MOBILE_BUDGET]` | Budget allocation for mobile | "$500,000" |
| `[MOBILE_TESTING]` | Specify the mobile testing | "Chrome DevTools device mode, BrowserStack real devices, Sauce Labs", "Manual testing on iOS Safari and Chrome Android" |
| `[MOBILE_USAGE]` | Specify the mobile usage | "55% of total traffic", "Primary platform for consumer apps", "Growing mobile-first user base" |
| `[TABLET_DEVICES]` | Specify the tablet devices | "iPad Air/Pro, Samsung Galaxy Tab, Surface Pro", "768px-1023px viewport range" |
| `[TABLET_LAYOUT]` | Specify the tablet layout | "Two-column layouts, side navigation visible", "Hybrid touch/pointer interactions", "Split-view support" |
| `[TABLET_BUDGET]` | Budget allocation for tablet | "$500,000" |
| `[TABLET_TESTING]` | Specify the tablet testing | "BrowserStack iPad testing, Chrome tablet emulation", "Landscape and portrait orientations" |
| `[TABLET_USAGE]` | Specify the tablet usage | "15% of total traffic", "Common for content consumption and light productivity" |
| `[DESKTOP_DEVICES]` | Specify the desktop devices | "Windows PC, MacBook, iMac, Linux workstations", "1024px-1439px viewport range" |
| `[DESKTOP_LAYOUT]` | Specify the desktop layout | "Multi-column layouts, persistent sidebars, hover states", "Full navigation menus, keyboard shortcuts" |
| `[DESKTOP_BUDGET]` | Budget allocation for desktop | "$500,000" |
| `[DESKTOP_TESTING]` | Specify the desktop testing | "Cross-browser testing (Chrome, Firefox, Safari, Edge)", "Playwright/Cypress E2E on CI" |
| `[DESKTOP_USAGE]` | Specify the desktop usage | "25% of total traffic", "Primary platform for enterprise/productivity apps" |
| `[LARGE_DEVICES]` | Specify the large devices | "4K monitors, ultra-wide displays, 27\"+ screens", "1440px+ viewport range" |
| `[LARGE_LAYOUT]` | Specify the large layout | "Max-width containers (1280px), centered content", "Multi-pane layouts, data-dense views" |
| `[LARGE_BUDGET]` | Budget allocation for large | "$500,000" |
| `[LARGE_TESTING]` | Specify the large testing | "4K display testing, ultra-wide viewport testing", "Ensure layouts don't break at extreme widths" |
| `[LARGE_USAGE]` | Specify the large usage | "5% of total traffic", "Power users and designers" |
| `[PRINT_SUPPORT]` | Specify the print support | "@media print stylesheets, print-specific layouts", "Remove navigation, optimize for paper" |
| `[PRINT_LAYOUT]` | Specify the print layout | "Single column, black text on white, no backgrounds", "Page breaks at logical points" |
| `[PRINT_TESTING]` | Specify the print testing | "Chrome print preview, actual printer testing", "PDF export validation" |
| `[PRINT_USAGE]` | Specify the print usage | "2% of users print reports/invoices", "Enterprise users print documentation" |
| `[FCP_CURRENT]` | Specify the fcp current | "1.8s", "2.5s", "1.2s (fast)", "3.2s (needs improvement)" |
| `[FCP_TARGET]` | Target or intended fcp | "< 1.8s (good)", "< 1.5s (excellent)", "< 1.0s (optimal)" |
| `[FCP_STRATEGY]` | Strategy or approach for fcp | "Inline critical CSS, preload fonts, server-side rendering", "Reduce render-blocking resources" |
| `[FCP_IMPACT]` | Specify the fcp impact | "User perception of speed, bounce rate reduction", "SEO ranking factor" |
| `[FCP_PRIORITY]` | Specify the fcp priority | "High" |
| `[LCP_CURRENT]` | Specify the lcp current | "2.8s", "3.5s", "1.9s (good)", "4.2s (poor)" |
| `[LCP_TARGET]` | Target or intended lcp | "< 2.5s (good)", "< 2.0s (excellent)", "< 1.5s (optimal)" |
| `[LCP_STRATEGY]` | Strategy or approach for lcp | "Optimize hero images (WebP, responsive), preload LCP image", "Use CDN, lazy load below-fold content" |
| `[LCP_IMPACT]` | Specify the lcp impact | "Core Web Vital metric, SEO ranking", "User engagement and conversion rates" |
| `[LCP_PRIORITY]` | Specify the lcp priority | "High" |
| `[FID_CURRENT]` | Specify the fid current | "120ms", "85ms (good)", "250ms (poor)", "50ms (excellent)" |
| `[FID_TARGET]` | Target or intended fid | "< 100ms (good)", "< 50ms (excellent)", "< 25ms (optimal)" |
| `[FID_STRATEGY]` | Strategy or approach for fid | "Break up long tasks, use web workers, defer non-critical JS", "Code splitting, reduce main thread work" |
| `[FID_IMPACT]` | Specify the fid impact | "Interactive responsiveness, user frustration reduction", "Form submission and click response" |
| `[FID_PRIORITY]` | Specify the fid priority | "High" |
| `[CLS_CURRENT]` | Specify the cls current | "0.15", "0.08 (good)", "0.25 (poor)", "0.02 (excellent)" |
| `[CLS_TARGET]` | Target or intended cls | "< 0.1 (good)", "< 0.05 (excellent)", "0 (optimal)" |
| `[CLS_STRATEGY]` | Strategy or approach for cls | "Set explicit dimensions for images/videos, reserve space for ads", "Avoid inserting content above existing content" |
| `[CLS_IMPACT]` | Specify the cls impact | "Visual stability, prevents accidental clicks", "User trust and reading experience" |
| `[CLS_PRIORITY]` | Specify the cls priority | "High" |
| `[TTI_CURRENT]` | Specify the tti current | "4.5s", "3.2s (good)", "6.0s (poor)", "2.5s (excellent)" |
| `[TTI_TARGET]` | Target or intended tti | "< 3.8s (good)", "< 2.5s (excellent)", "< 2.0s (optimal)" |
| `[TTI_STRATEGY]` | Strategy or approach for tti | "Minimize JavaScript payload, code splitting, tree shaking", "Defer non-essential scripts, progressive hydration" |
| `[TTI_IMPACT]` | Specify the tti impact | "Full interactivity timing, user can engage with all features", "Critical for SPAs and interactive apps" |
| `[TTI_PRIORITY]` | Specify the tti priority | "High" |
| `[BUNDLE_CURRENT]` | Specify the bundle current | "350KB gzipped", "180KB (good)", "500KB (needs work)", "120KB (excellent)" |
| `[BUNDLE_TARGET]` | Target or intended bundle | "< 200KB gzipped (good)", "< 150KB (excellent)", "< 100KB initial (optimal)" |
| `[BUNDLE_STRATEGY]` | Strategy or approach for bundle | "Code splitting by route, dynamic imports, tree shaking", "Analyze with bundle-analyzer, remove unused deps" |
| `[BUNDLE_IMPACT]` | Specify the bundle impact | "Download time, parse time, mobile data usage", "Initial load performance" |
| `[BUNDLE_PRIORITY]` | Specify the bundle priority | "High" |
| `[STORE_STRUCTURE]` | Specify the store structure | "Feature-based slices (auth, user, products, cart)", "Domain-driven store organization", "Normalized entities with IDs" |
| `[STATE_SHAPE]` | Specify the state shape | "{ auth: AuthState, user: UserState, ui: UIState, entities: NormalizedEntities }", "Typed interfaces for each slice" |
| `[MIDDLEWARE_STACK]` | Specify the middleware stack | "Redux Thunk for async actions, RTK Query for API", "Logger middleware (dev only), error reporting middleware" |
| `[PERSIST_STRATEGY]` | Strategy or approach for persist | "redux-persist with localStorage for auth/preferences", "sessionStorage for temporary state, IndexedDB for large data" |
| `[DEVTOOLS_CONFIG]` | Specify the devtools config | "Redux DevTools with action history, state diff", "React Query DevTools for cache inspection" |
| `[COMP_STATE]` | Specify the comp state | "useState for local UI state (open/closed, selected)", "useReducer for complex local state with multiple actions" |
| `[FORM_STATE]` | Specify the form state | "React Hook Form for performance, controlled inputs", "Zod/Yup schema validation, field-level errors" |
| `[UI_STATE]` | Specify the ui state | "Modal open state, sidebar collapsed, theme preference", "Toast notifications queue, loading overlays" |
| `[CACHE_STRATEGY]` | Strategy or approach for cache | "Stale-while-revalidate with 5min staleTime", "Cache invalidation on mutations, optimistic updates" |
| `[API_CLIENT]` | Specify the api client | "Axios with interceptors for auth", "fetch with React Query wrapper", "RTK Query for Redux integration" |
| `[REQUEST_STRATEGY]` | Strategy or approach for request | "Dedupe concurrent requests, retry on failure (3x)", "AbortController for cancellation, request queuing" |
| `[ERROR_HANDLING]` | Specify the error handling | "Error boundaries for component failures", "Toast notifications for API errors, retry prompts" |
| `[LOADING_STATES]` | Specify the loading states | "Skeleton loaders for content, spinners for actions", "Progressive loading, optimistic UI updates" |
| `[OPTIMISTIC_UPDATES]` | Specify the optimistic updates | "2025-01-15" |
| `[WEBSOCKET_IMPL]` | Specify the websocket impl | "Socket.io client with auto-reconnect", "Native WebSocket with custom wrapper", "Pusher/Ably for managed WebSockets" |
| `[POLLING_STRATEGY]` | Strategy or approach for polling | "Long polling fallback for WebSocket", "Interval polling (30s) for non-critical data", "Smart polling with backoff" |
| `[SSE_IMPL]` | Specify the sse impl | "EventSource API for server updates", "Notifications stream, activity feed", "Fallback to polling if SSE fails" |
| `[SYNC_STRATEGY]` | Strategy or approach for sync | "Optimistic updates with rollback", "Conflict resolution (last-write-wins)", "Offline queue with sync on reconnect" |
| `[KEYBOARD_IMPL]` | Specify the keyboard impl | "Tab navigation through all interactive elements", "Enter/Space for button activation", "Escape to close modals" |
| `[KEYBOARD_TEST]` | Specify the keyboard test | "Manual keyboard-only navigation testing", "Automated a11y testing with axe-core" |
| `[KEYBOARD_LEVEL]` | Specify the keyboard level | "WCAG 2.1 AA compliant", "Full keyboard accessibility", "Power user shortcuts" |
| `[KEYBOARD_IMPACT]` | Specify the keyboard impact | "Motor impairment users, power users", "Productivity improvement, legal compliance" |
| `[KEYBOARD_FIX]` | Specify the keyboard fix | "Add tabindex where needed, implement focus trap in modals", "Add skip links, visible focus indicators" |
| `[SCREEN_IMPL]` | Specify the screen impl | "ARIA labels on all interactive elements", "Semantic HTML structure", "Live regions for dynamic content" |
| `[SCREEN_TEST]` | Specify the screen test | "VoiceOver (Mac), NVDA (Windows) testing", "Automated testing with axe-core/pa11y" |
| `[SCREEN_LEVEL]` | Specify the screen level | "WCAG 2.1 AA compliant", "Full screen reader support" |
| `[SCREEN_IMPACT]` | Specify the screen impact | "Blind and low-vision users", "Legal compliance, broader user reach" |
| `[SCREEN_FIX]` | Specify the screen fix | "Add aria-labels, aria-describedby", "Improve heading hierarchy, add alt text" |
| `[COLOR_IMPL]` | Specify the color impl | "4.5:1 contrast ratio for normal text", "3:1 for large text and UI components" |
| `[COLOR_TEST]` | Specify the color test | "Contrast checker tools (WebAIM)", "Color blindness simulation testing" |
| `[COLOR_LEVEL]` | Specify the color level | "WCAG 2.1 AA (4.5:1)", "AAA for critical text (7:1)" |
| `[COLOR_IMPACT]` | Specify the color impact | "Low vision users, color blind users", "Readability in various lighting conditions" |
| `[COLOR_FIX]` | Specify the color fix | "Darken text colors, increase contrast", "Don't rely solely on color for information" |
| `[FOCUS_IMPL]` | Specify the focus impl | "Visible focus indicators (:focus-visible)", "Focus trap in modals and drawers" |
| `[FOCUS_TEST]` | Specify the focus test | "Tab through all interactive elements", "Verify focus order is logical" |
| `[FOCUS_LEVEL]` | Specify the focus level | "WCAG 2.1 AA compliant", "Clear visual focus indicators" |
| `[FOCUS_IMPACT]` | Specify the focus impact | "Keyboard users, screen reader users", "Navigation clarity" |
| `[FOCUS_FIX]` | Specify the focus fix | "Add focus-visible styles, remove outline:none", "Implement focus management in SPAs" |
| `[ARIA_IMPL]` | Specify the aria impl | "aria-label for icon buttons, aria-expanded for toggles", "role attributes for custom components" |
| `[ARIA_TEST]` | Specify the aria test | "axe-core automated testing", "Manual screen reader verification" |
| `[ARIA_LEVEL]` | Specify the aria level | "WCAG 2.1 AA compliant", "Proper ARIA usage" |
| `[ARIA_IMPACT]` | Specify the aria impact | "Screen reader users, assistive technology", "Component accessibility" |
| `[ARIA_FIX]` | Specify the aria fix | "Add missing aria attributes", "Remove redundant ARIA (semantic HTML first)" |
| `[FORM_A11Y_IMPL]` | Specify the form a11y impl | "Label elements for all inputs", "aria-describedby for error messages" |
| `[FORM_TEST]` | Specify the form test | "Screen reader form navigation", "Error announcement testing" |
| `[FORM_LEVEL]` | Specify the form level | "WCAG 2.1 AA compliant", "Accessible form patterns" |
| `[FORM_IMPACT]` | Specify the form impact | "All users filling forms", "Data entry accuracy" |
| `[FORM_FIX]` | Specify the form fix | "Associate labels with inputs", "Provide clear error messages, required indicators" |
| `[UNIT_TARGET]` | Target or intended unit | "80% coverage for utilities and hooks", "90% for business logic" |
| `[UNIT_TOOLS]` | Specify the unit tools | "Vitest/Jest with React Testing Library", "Mock Service Worker for API mocking" |
| `[UNIT_FREQ]` | Specify the unit freq | "Every commit (pre-commit hook)", "CI pipeline on every PR" |
| `[UNIT_TIME]` | Specify the unit time | "< 30 seconds for full suite", "Parallelized execution" |
| `[UNIT_EFFORT]` | Specify the unit effort | "Low maintenance, high value", "Test critical paths first" |
| `[COMP_TARGET]` | Target or intended comp | "70% coverage for UI components", "100% for shared components" |
| `[COMP_TOOLS]` | Specify the comp tools | "React Testing Library, Storybook interaction tests", "Chromatic for visual testing" |
| `[COMP_FREQ]` | Specify the comp freq | "Every commit, Storybook CI check", "Visual regression on PRs" |
| `[COMP_TIME]` | Specify the comp time | "1-2 minutes for component tests", "Parallel execution" |
| `[COMP_EFFORT]` | Specify the comp effort | "Medium maintenance, reusable patterns", "Component stories double as tests" |
| `[INT_TARGET]` | Target or intended int | "60% coverage for user flows", "Critical paths fully covered" |
| `[INT_TOOLS]` | Specify the int tools | "Testing Library with MSW", "Real component integration tests" |
| `[INT_FREQ]` | Specify the int freq | "Every PR, full suite on main", "Nightly for comprehensive runs" |
| `[INT_TIME]` | Specify the int time | "2-5 minutes for integration suite", "Selective runs on affected areas" |
| `[INT_EFFORT]` | Specify the int effort | "Medium-high maintenance", "Focus on critical user flows" |
| `[E2E_TARGET]` | Target or intended e2e | "Critical user journeys covered", "Login, checkout, key workflows" |
| `[E2E_TOOLS]` | Specify the e2e tools | "Playwright for cross-browser", "Cypress for developer experience" |
| `[E2E_FREQ]` | Specify the e2e freq | "On main branch merges", "Nightly full regression suite" |
| `[E2E_TIME]` | Specify the e2e time | "5-15 minutes for E2E suite", "Parallelized across browsers" |
| `[E2E_EFFORT]` | Specify the e2e effort | "High maintenance, high confidence", "Flaky test management needed" |
| `[VIS_TARGET]` | Target or intended vis | "All shared components covered", "Key pages snapshot tested" |
| `[VIS_TOOLS]` | Specify the vis tools | "Chromatic for Storybook", "Percy for page snapshots", "Playwright visual comparisons" |
| `[VIS_FREQ]` | Specify the vis freq | "Every PR with component changes", "Baseline updates on releases" |
| `[VIS_TIME]` | Specify the vis time | "3-5 minutes for visual diffs", "Async approval workflow" |
| `[VIS_EFFORT]` | Specify the vis effort | "Low-medium maintenance", "Manual approval for intentional changes" |
| `[PERF_TARGET]` | Target or intended perf | "Lighthouse > 90, Web Vitals passing", "Bundle size regression alerts" |
| `[PERF_TOOLS]` | Specify the perf tools | "Lighthouse CI, webpack-bundle-analyzer", "Core Web Vitals monitoring" |
| `[PERF_FREQ]` | Specify the perf freq | "Every deploy, weekly audits", "Alerts on regression" |
| `[PERF_TIME]` | Specify the perf time | "1-2 minutes for Lighthouse CI", "Real User Monitoring continuous" |
| `[PERF_EFFORT]` | Specify the perf effort | "Low maintenance, automated", "Performance budgets enforced" |
| `[DEV_BUILD_TIME]` | Specify the dev build time | "< 2 seconds cold start with Vite", "Instant HMR updates" |
| `[HOT_RELOAD]` | Specify the hot reload | "Vite HMR with React Fast Refresh", "State preservation on code changes" |
| `[DEV_SOURCEMAPS]` | Specify the dev sourcemaps | "Inline source maps for debugging", "Full TypeScript mapping" |
| `[DEV_SERVER]` | Specify the dev server | "Vite dev server on port 3000", "HTTPS for local development" |
| `[DEV_PROXY]` | Specify the dev proxy | "Proxy /api to backend server", "Mock server for offline development" |
| `[PROD_BUILD_TIME]` | Specify the prod build time | "2-5 minutes with optimizations", "Cached builds for faster CI" |
| `[PROD_OPTIMIZE]` | Specify the prod optimize | "Terser minification, CSS purging", "Image optimization, compression" |
| `[CODE_SPLIT]` | Specify the code split | "Route-based splitting, dynamic imports", "Vendor chunk separation" |
| `[TREE_SHAKE]` | Specify the tree shake | "ES modules for tree-shaking", "Dead code elimination" |
| `[MINIFICATION]` | Specify the minification | "Terser for JS, cssnano for CSS", "HTML minification" |
| `[ASSET_OPT]` | Specify the asset opt | "Image optimization (WebP, AVIF)", "Font subsetting, asset hashing" |
| `[HOSTING_PLATFORM]` | Specify the hosting platform | "Vercel for Next.js", "Netlify for static sites", "AWS S3 + CloudFront" |
| `[CDN_PROVIDER]` | Specify the cdn provider | "Vercel Edge Network", "CloudFront", "Cloudflare" |
| `[VERSION_STRATEGY]` | Strategy or approach for version | "Git commit hash in build", "Semantic versioning for releases", "Immutable deployments" |
| `[ROLLBACK_PLAN]` | Specify the rollback plan | "Instant rollback on Vercel/Netlify", "Previous deployment promotion" |
| `[MONITOR_TOOLS]` | Specify the monitor tools | "Sentry for errors, Datadog for APM", "Google Analytics for usage" |
| `[CHROME_MIN]` | Specify the chrome min | "Chrome 90+", "Last 2 versions", "Chrome 88+ for enterprise" |
| `[CHROME_SHARE]` | Specify the chrome share | "65% of users", "Primary browser target" |
| `[CHROME_FEATURES]` | Specify the chrome features | "Full ES2022+ support, CSS Grid/Flexbox", "All modern APIs" |
| `[CHROME_POLY]` | Specify the chrome poly | "None required for Chrome 90+", "Optional core-js for older" |
| `[CHROME_PRIORITY]` | Specify the chrome priority | "High" |
| `[FIREFOX_MIN]` | Specify the firefox min | "Firefox 88+", "Last 2 versions", "ESR for enterprise" |
| `[FIREFOX_SHARE]` | Specify the firefox share | "8% of users", "Developer preference" |
| `[FIREFOX_FEATURES]` | Specify the firefox features | "Full ES2022+ support, excellent DevTools", "Strong privacy features" |
| `[FIREFOX_POLY]` | Specify the firefox poly | "None required for modern Firefox", "Container queries polyfill if needed" |
| `[FIREFOX_PRIORITY]` | Specify the firefox priority | "High" |
| `[SAFARI_MIN]` | Specify the safari min | "Safari 14+", "Last 2 versions", "iOS Safari 14+" |
| `[SAFARI_SHARE]` | Specify the safari share | "18% of users", "Primary for Mac/iOS users" |
| `[SAFARI_FEATURES]` | Specify the safari features | "Good ES2022 support, WebKit-specific CSS", "PWA limitations on iOS" |
| `[SAFARI_POLY]` | Specify the safari poly | "ResizeObserver polyfill for Safari 13", "Smooth scroll polyfill" |
| `[SAFARI_PRIORITY]` | Specify the safari priority | "High" |
| `[EDGE_MIN]` | Specify the edge min | "Edge 90+ (Chromium)", "Last 2 versions" |
| `[EDGE_SHARE]` | Specify the edge share | "5% of users", "Enterprise Windows users" |
| `[EDGE_FEATURES]` | Specify the edge features | "Chromium-based, full modern feature support", "Same as Chrome" |
| `[EDGE_POLY]` | Specify the edge poly | "None required for Chromium Edge", "Legacy Edge not supported" |
| `[EDGE_PRIORITY]` | Specify the edge priority | "High" |
| `[MOBILE_SAF_MIN]` | Specify the mobile saf min | "iOS Safari 14+", "Last 2 iOS versions" |
| `[MOBILE_SAF_SHARE]` | Specify the mobile saf share | "25% of mobile users", "Primary iOS browser" |
| `[MOBILE_SAF_FEATURES]` | Specify the mobile saf features | "Touch events, viewport units, safe area insets", "Limited PWA support" |
| `[MOBILE_SAF_POLY]` | Specify the mobile saf poly | "Scroll behavior polyfill", "Touch event normalization" |
| `[MOBILE_SAF_PRIORITY]` | Specify the mobile saf priority | "High" |
| `[MOBILE_CHR_MIN]` | Specify the mobile chr min | "Chrome Android 90+", "Last 2 versions" |
| `[MOBILE_CHR_SHARE]` | Specify the mobile chr share | "45% of mobile users", "Primary Android browser" |
| `[MOBILE_CHR_FEATURES]` | Specify the mobile chr features | "Full PWA support, Web Share API", "All modern features" |
| `[MOBILE_CHR_POLY]` | Specify the mobile chr poly | "None required for Chrome 90+", "Service Worker supported" |
| `[MOBILE_CHR_PRIORITY]` | Specify the mobile chr priority | "High" |
| `[ERROR_TOOL]` | Specify the error tool | "Sentry", "Bugsnag", "LogRocket", "Rollbar" |
| `[ERROR_METRICS]` | Specify the error metrics | "Error rate, error count by type, affected users", "Stack traces, browser/device info" |
| `[ERROR_THRESHOLD]` | Specify the error threshold | "Error rate > 1% triggers alert", "New error type immediate notification" |
| `[ERROR_RESPONSE]` | Specify the error response | "< 15 minutes for P1 errors", "< 4 hours for P2 errors" |
| `[ERROR_ACTION]` | Specify the error action | "Assign to on-call engineer, create incident ticket", "Rollback if error rate spikes" |
| `[PERF_TOOL]` | Specify the perf tool | "Datadog RUM", "New Relic Browser", "SpeedCurve", "Lighthouse CI" |
| `[PERF_METRICS]` | Specify the perf metrics | "Core Web Vitals (LCP, FID, CLS)", "Page load time, TTFB, bundle size" |
| `[PERF_THRESHOLD]` | Specify the perf threshold | "LCP > 2.5s, FID > 100ms, CLS > 0.1", "Bundle size increase > 10%" |
| `[PERF_RESPONSE]` | Specify the perf response | "< 24 hours for performance regression", "Immediate for severe degradation" |
| `[PERF_ACTION]` | Specify the perf action | "Investigate with profiler, optimize critical path", "Block deploy if budgets exceeded" |
| `[ANALYTICS_TOOL]` | Specify the analytics tool | "Google Analytics 4", "Mixpanel", "Amplitude", "PostHog" |
| `[ANALYTICS_METRICS]` | Specify the analytics metrics | "Page views, unique users, session duration", "Conversion rates, funnel completion" |
| `[ANALYTICS_THRESHOLD]` | Specify the analytics threshold | "Bounce rate > 60%, conversion drop > 10%", "Traffic anomalies" |
| `[ANALYTICS_RESPONSE]` | Specify the analytics response | "Weekly review of dashboards", "Immediate alert for major changes" |
| `[ANALYTICS_ACTION]` | Specify the analytics action | "A/B test improvements, user research", "Funnel optimization" |
| `[AB_TOOL]` | Specify the ab tool | "LaunchDarkly", "Optimizely", "Split.io", "VWO" |
| `[AB_METRICS]` | Specify the ab metrics | "Conversion rate, engagement, revenue per user", "Statistical significance" |
| `[AB_THRESHOLD]` | Specify the ab threshold | "95% statistical significance", "Minimum 1000 users per variant" |
| `[AB_RESPONSE]` | Specify the ab response | "2-4 weeks experiment duration", "Early stopping if clear winner" |
| `[AB_ACTION]` | Specify the ab action | "Roll out winner, document learnings", "Iterate on losing variants" |
| `[SESSION_TOOL]` | Specify the session tool | "LogRocket", "FullStory", "Hotjar", "Smartlook" |
| `[SESSION_METRICS]` | Specify the session metrics | "Session recordings, heatmaps, click maps", "Rage clicks, error sessions" |
| `[SESSION_THRESHOLD]` | Specify the session threshold | "Rage clicks > 5%, frustrated sessions > 10%", "Error sessions increasing" |
| `[SESSION_RESPONSE]` | Specify the session response | "Weekly UX review sessions", "Immediate investigation of rage clicks" |
| `[SESSION_ACTION]` | Specify the session action | "UX improvements based on recordings", "Fix pain points identified" |
| `[UPTIME_TOOL]` | Specify the uptime tool | "Pingdom", "StatusCake", "UptimeRobot", "Better Uptime" |
| `[UPTIME_METRICS]` | Specify the uptime metrics | "Availability percentage, response time", "Downtime duration, incident count" |
| `[UPTIME_THRESHOLD]` | Specify the uptime threshold | "99.9% uptime SLA", "Response time > 2s" |
| `[UPTIME_RESPONSE]` | Specify the uptime response | "< 5 minutes for downtime alert", "Immediate escalation for outages" |
| `[UPTIME_ACTION]` | Specify the uptime action | "Page on-call team, status page update", "Post-incident review" |

### 3. Responsive Design Strategy

| **Breakpoint** | **Device Target** | **Layout Changes** | **Performance Budget** | **Testing Coverage** | **Usage Analytics** |
|---------------|------------------|-------------------|----------------------|--------------------|--------------------|
| Mobile (<768px) | [MOBILE_DEVICES] | [MOBILE_LAYOUT] | [MOBILE_BUDGET] KB | [MOBILE_TESTING]% | [MOBILE_USAGE]% |
| Tablet (768-1024px) | [TABLET_DEVICES] | [TABLET_LAYOUT] | [TABLET_BUDGET] KB | [TABLET_TESTING]% | [TABLET_USAGE]% |
| Desktop (1024-1440px) | [DESKTOP_DEVICES] | [DESKTOP_LAYOUT] | [DESKTOP_BUDGET] KB | [DESKTOP_TESTING]% | [DESKTOP_USAGE]% |
| Large (>1440px) | [LARGE_DEVICES] | [LARGE_LAYOUT] | [LARGE_BUDGET] KB | [LARGE_TESTING]% | [LARGE_USAGE]% |
| Print | [PRINT_SUPPORT] | [PRINT_LAYOUT] | N/A | [PRINT_TESTING]% | [PRINT_USAGE]% |

### 4. Performance Optimization

**Web Vitals & Performance Metrics:**
| **Metric** | **Current Score** | **Target** | **Optimization Strategy** | **Impact** | **Priority** |
|-----------|------------------|-----------|-------------------------|-----------|-------------|
| First Contentful Paint | [FCP_CURRENT] ms | [FCP_TARGET] ms | [FCP_STRATEGY] | [FCP_IMPACT] | [FCP_PRIORITY]/10 |
| Largest Contentful Paint | [LCP_CURRENT] ms | [LCP_TARGET] ms | [LCP_STRATEGY] | [LCP_IMPACT] | [LCP_PRIORITY]/10 |
| First Input Delay | [FID_CURRENT] ms | [FID_TARGET] ms | [FID_STRATEGY] | [FID_IMPACT] | [FID_PRIORITY]/10 |
| Cumulative Layout Shift | [CLS_CURRENT] | [CLS_TARGET] | [CLS_STRATEGY] | [CLS_IMPACT] | [CLS_PRIORITY]/10 |
| Time to Interactive | [TTI_CURRENT] s | [TTI_TARGET] s | [TTI_STRATEGY] | [TTI_IMPACT] | [TTI_PRIORITY]/10 |
| Bundle Size | [BUNDLE_CURRENT] KB | [BUNDLE_TARGET] KB | [BUNDLE_STRATEGY] | [BUNDLE_IMPACT] | [BUNDLE_PRIORITY]/10 |

### 5. State Management & Data Flow

```
State Management Architecture:
Global State:
- Store Structure: [STORE_STRUCTURE]
- State Shape: [STATE_SHAPE]
- Middleware: [MIDDLEWARE_STACK]
- Persistence: [PERSIST_STRATEGY]
- DevTools: [DEVTOOLS_CONFIG]

Local State:
- Component State: [COMP_STATE]
- Form State: [FORM_STATE]
- UI State: [UI_STATE]
- Cache Strategy: [CACHE_STRATEGY]

### Data Fetching
- API Client: [API_CLIENT]
- Request Strategy: [REQUEST_STRATEGY]
- Error Handling: [ERROR_HANDLING]
- Loading States: [LOADING_STATES]
- Optimistic Updates: [OPTIMISTIC_UPDATES]

Real-time Updates:
- WebSocket: [WEBSOCKET_IMPL]
- Polling: [POLLING_STRATEGY]
- Server-Sent Events: [SSE_IMPL]
- Sync Strategy: [SYNC_STRATEGY]
```

### 6. Accessibility (A11y) Implementation

| **WCAG Criteria** | **Implementation** | **Testing Method** | **Compliance Level** | **User Impact** | **Remediation** |
|------------------|-------------------|-------------------|--------------------|--------------------|-----------------|
| Keyboard Navigation | [KEYBOARD_IMPL] | [KEYBOARD_TEST] | [KEYBOARD_LEVEL] | [KEYBOARD_IMPACT] | [KEYBOARD_FIX] |
| Screen Reader Support | [SCREEN_IMPL] | [SCREEN_TEST] | [SCREEN_LEVEL] | [SCREEN_IMPACT] | [SCREEN_FIX] |
| Color Contrast | [COLOR_IMPL] | [COLOR_TEST] | [COLOR_LEVEL] | [COLOR_IMPACT] | [COLOR_FIX] |
| Focus Management | [FOCUS_IMPL] | [FOCUS_TEST] | [FOCUS_LEVEL] | [FOCUS_IMPACT] | [FOCUS_FIX] |
| ARIA Labels | [ARIA_IMPL] | [ARIA_TEST] | [ARIA_LEVEL] | [ARIA_IMPACT] | [ARIA_FIX] |
| Form Accessibility | [FORM_A11Y_IMPL] | [FORM_TEST] | [FORM_LEVEL] | [FORM_IMPACT] | [FORM_FIX] |

### 7. Testing Strategy

**Frontend Testing Pyramid:**
| **Test Type** | **Coverage Target** | **Tools** | **Run Frequency** | **Execution Time** | **Maintenance Effort** |
|--------------|-------------------|----------|------------------|-------------------|---------------------|
| Unit Tests | [UNIT_TARGET]% | [UNIT_TOOLS] | [UNIT_FREQ] | [UNIT_TIME] | [UNIT_EFFORT]/10 |
| Component Tests | [COMP_TARGET]% | [COMP_TOOLS] | [COMP_FREQ] | [COMP_TIME] | [COMP_EFFORT]/10 |
| Integration Tests | [INT_TARGET]% | [INT_TOOLS] | [INT_FREQ] | [INT_TIME] | [INT_EFFORT]/10 |
| E2E Tests | [E2E_TARGET]% | [E2E_TOOLS] | [E2E_FREQ] | [E2E_TIME] | [E2E_EFFORT]/10 |
| Visual Regression | [VIS_TARGET]% | [VIS_TOOLS] | [VIS_FREQ] | [VIS_TIME] | [VIS_EFFORT]/10 |
| Performance Tests | [PERF_TARGET]% | [PERF_TOOLS] | [PERF_FREQ] | [PERF_TIME] | [PERF_EFFORT]/10 |

### 8. Build & Deployment Pipeline

```
Build Configuration:
Development Build:
- Build Time: [DEV_BUILD_TIME]
- Hot Reload: [HOT_RELOAD]
- Source Maps: [DEV_SOURCEMAPS]
- Dev Server: [DEV_SERVER]
- Proxy Config: [DEV_PROXY]

Production Build:
- Build Time: [PROD_BUILD_TIME]
- Optimization: [PROD_OPTIMIZE]
- Code Splitting: [CODE_SPLIT]
- Tree Shaking: [TREE_SHAKE]
- Minification: [MINIFICATION]
- Asset Optimization: [ASSET_OPT]

### Deployment Strategy
- Hosting: [HOSTING_PLATFORM]
- CDN: [CDN_PROVIDER]
- Caching: [CACHE_STRATEGY]
- Versioning: [VERSION_STRATEGY]
- Rollback: [ROLLBACK_PLAN]
- Monitoring: [MONITOR_TOOLS]
```

### 9. Browser Compatibility

| **Browser** | **Min Version** | **Usage Share** | **Feature Support** | **Polyfills** | **Testing Priority** |
|------------|----------------|----------------|-------------------|--------------|-------------------|
| Chrome | [CHROME_MIN] | [CHROME_SHARE]% | [CHROME_FEATURES] | [CHROME_POLY] | [CHROME_PRIORITY]/10 |
| Firefox | [FIREFOX_MIN] | [FIREFOX_SHARE]% | [FIREFOX_FEATURES] | [FIREFOX_POLY] | [FIREFOX_PRIORITY]/10 |
| Safari | [SAFARI_MIN] | [SAFARI_SHARE]% | [SAFARI_FEATURES] | [SAFARI_POLY] | [SAFARI_PRIORITY]/10 |
| Edge | [EDGE_MIN] | [EDGE_SHARE]% | [EDGE_FEATURES] | [EDGE_POLY] | [EDGE_PRIORITY]/10 |
| Mobile Safari | [MOBILE_SAF_MIN] | [MOBILE_SAF_SHARE]% | [MOBILE_SAF_FEATURES] | [MOBILE_SAF_POLY] | [MOBILE_SAF_PRIORITY]/10 |
| Chrome Mobile | [MOBILE_CHR_MIN] | [MOBILE_CHR_SHARE]% | [MOBILE_CHR_FEATURES] | [MOBILE_CHR_POLY] | [MOBILE_CHR_PRIORITY]/10 |

### 10. Monitoring & Analytics

**Frontend Monitoring Stack:**
| **Monitoring Area** | **Tool/Service** | **Metrics Tracked** | **Alert Threshold** | **Response Time** | **Action Plan** |
|-------------------|-----------------|-------------------|-------------------|------------------|---------------|
| Error Tracking | [ERROR_TOOL] | [ERROR_METRICS] | [ERROR_THRESHOLD] | [ERROR_RESPONSE] | [ERROR_ACTION] |
| Performance | [PERF_TOOL] | [PERF_METRICS] | [PERF_THRESHOLD] | [PERF_RESPONSE] | [PERF_ACTION] |
| User Analytics | [ANALYTICS_TOOL] | [ANALYTICS_METRICS] | [ANALYTICS_THRESHOLD] | [ANALYTICS_RESPONSE] | [ANALYTICS_ACTION] |
| A/B Testing | [AB_TOOL] | [AB_METRICS] | [AB_THRESHOLD] | [AB_RESPONSE] | [AB_ACTION] |
| Session Recording | [SESSION_TOOL] | [SESSION_METRICS] | [SESSION_THRESHOLD] | [SESSION_RESPONSE] | [SESSION_ACTION] |
| Uptime Monitoring | [UPTIME_TOOL] | [UPTIME_METRICS] | [UPTIME_THRESHOLD] | [UPTIME_RESPONSE] | [UPTIME_ACTION] |

## Usage Examples

## Best Practices

1. **Start with clear objectives** - Define what success looks like before beginning
2. **Use data to inform decisions** - Base choices on evidence and measurable outcomes
3. **Iterate and improve continuously** - Treat implementation as an ongoing process
4. **Engage stakeholders early** - Include key participants in planning and execution
5. **Document thoroughly** - Maintain clear records for reference and knowledge transfer
6. **Communicate regularly** - Keep all parties informed of progress and changes
7. **Address challenges proactively** - Identify potential issues before they become problems
8. **Celebrate milestones** - Recognize achievements to maintain motivation
9. **Learn from experience** - Reflect on what works and adjust accordingly
10. **Stay flexible** - Be ready to adapt based on feedback and changing circumstances

## Tips for Success

- Break complex tasks into manageable steps with clear milestones
- Set realistic timelines that account for dependencies and constraints
- Allocate sufficient resources including time, budget, and personnel
- Use templates and frameworks to ensure consistency and quality
- Seek feedback from users and stakeholders throughout the process
- Build in checkpoints to assess progress and make adjustments
- Maintain quality standards while remaining practical and efficient
- Document lessons learned for future reference and improvement
- Foster collaboration across teams and departments
- Stay current with industry best practices and emerging trends
### Example 1: E-commerce SPA
```
Framework: React 18 + Next.js
State: Redux Toolkit + RTK Query
Styling: Tailwind CSS + CSS Modules
Components: 150+ custom components
Performance: 95+ Lighthouse score
PWA: Full offline support
Testing: 85% coverage
Accessibility: WCAG 2.1 AA
```

### Example 2: Enterprise Dashboard
```
Framework: Angular 15
State: NgRx
UI Library: Angular Material
Charts: D3.js + Chart.js
Real-time: WebSocket + SignalR
Testing: Jasmine + Karma + Cypress
Build: Nx monorepo
Deployment: Azure + CDN
```

### Example 3: Marketing Website
```
Framework: Vue 3 + Nuxt
Animation: GSAP + Lottie
CMS: Headless (Strapi)
Performance: <2s load time
SEO: SSR + structured data
Analytics: GA4 + Hotjar
A/B Testing: Optimizely
Hosting: Vercel Edge
```



## Related Resources

### Complementary Templates

Enhance your workflow by combining this template with:

- **[Cloud Architecture Framework](cloud-architecture-framework.md)** - Complementary approaches and methodologies
- **[Site Reliability Engineering](site-reliability-engineering.md)** - Complementary approaches and methodologies
- **[Cloud Migration Strategy](cloud-migration-strategy.md)** - Strategic planning and execution frameworks

### Suggested Workflow

**Typical implementation sequence**:

1. Start with this template (Frontend Development & Web Application Framework)
2. Use [Cloud Architecture Framework](cloud-architecture-framework.md) for deeper analysis
3. Apply [Site Reliability Engineering](site-reliability-engineering.md) for execution
4. Iterate and refine based on results

### Explore More in This Category

Browse all **[technology/Software Development](../../technology/Software Development/)** templates for related tools and frameworks.

### Common Use Case Combinations

- **Creating comprehensive framework for frontend web development including modern javascript frameworks, responsive design, performance optimization, accessibility standards, and progressive web applications.**: Combine this template with related analytics and strategy frameworks
- **Project planning and execution**: Combine this template with related analytics and strategy frameworks
- **Strategy development**: Combine this template with related analytics and strategy frameworks

## Customization Options

### 1. Framework Choice
- React/Next.js
- Angular
- Vue/Nuxt
- Svelte/SvelteKit
- Vanilla JavaScript

### 2. Application Type
- Single Page Application (SPA)
- Server-Side Rendered (SSR)
- Static Site Generation (SSG)
- Progressive Web App (PWA)
- Hybrid Approach

### 3. Styling Approach
- CSS-in-JS
- CSS Modules
- Utility-First (Tailwind)
- Component Libraries
- Custom Design System

### 4. Performance Target
- Mobile-First
- Desktop-Optimized
- Offline-First
- Real-Time Priority
- SEO-Focused

### 5. Team Size
- Solo Developer
- Small Team (2-5)
- Medium Team (5-15)
- Large Team (15+)
- Enterprise Scale