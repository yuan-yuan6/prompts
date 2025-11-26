---
category: ai-ml-applications
last_updated: 2025-11-12
title: AI UX & Interaction Design
tags:
- ai-ml
- ux-design
- interaction-design
- user-experience
- product-design
use_cases:
- Designing user experiences for AI-powered features
- Creating interaction patterns for AI systems
- Handling AI uncertainty and errors gracefully
- Building trust and transparency in AI products
related_templates:
- ai-ml-applications/AI-Product-Development/ai-feature-development.md
- ai-ml-applications/LLM-Applications/conversational-ai-chatbots.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: template
difficulty: intermediate
slug: ai-ux-interaction-design
---

# AI UX & Interaction Design Template

## Purpose
Design intuitive, trustworthy user experiences for AI-powered features that manage user expectations, handle uncertainty gracefully, and build confidence in AI capabilities.

---

## 🚀 Quick Prompt

**Copy and use this generic prompt to design any AI user experience:**

> I'm designing the UX for **[AI FEATURE]** in **[PRODUCT]** for **[TARGET USERS]** who want to **[USER GOAL]**. Help me design: (1) **Interaction pattern**—should this be AI suggestions, automation, collaboration, or conversational, and what level of user control is needed (initiation, approval, editing, override)? (2) **State design**—what are the loading, success, error, and edge case states, with specific UI components, progressive disclosure, and messaging for each? (3) **Trust & transparency**—how do we disclose AI involvement, show confidence levels, provide explanations, and give users control? (4) **Error handling**—how do we gracefully handle AI failures, low confidence, hallucinations, and unexpected outputs with clear recovery paths? Provide wireframe recommendations, a UX writing guide, and an accessibility checklist.

**Usage:** Fill in the brackets and use as a prompt to an AI assistant or as your UX design framework.

---

## Quick Start

### Minimal Example
```
AI Feature: Document summarization
UX Pattern: AI Enhancement

User Flow:
1. User uploads document → Shows "Analyzing..." (10-15 sec estimate)
2. AI generates summary → Displays with confidence indicator
3. User reviews → Can regenerate, edit, or accept
4. Provide feedback → Thumbs up/down for future improvement

Key UX Principles:
- Show AI is working (progress indicator)
- Manage expectations (estimated time)
- Give control (edit, regenerate)
- Be transparent (confidence score)
- Learn from feedback (improvement loop)
```

### When to Use This
- Designing any AI-powered feature or product
- Improving existing AI feature usability
- Building user trust in AI capabilities
- Handling AI errors and edge cases
- Creating consistent AI interaction patterns

### Basic 4-Step Workflow
1. **Choose AI Pattern** - Select appropriate interaction pattern for your AI feature
2. **Design States** - Plan loading, success, error, and edge case states
3. **Build Trust** - Add transparency, explanations, and control mechanisms
4. **Handle Uncertainty** - Design for AI mistakes, low confidence, errors

---

## Template

```
You are a UX design expert specializing in AI-powered products. Design the user experience for [AI_FEATURE_NAME] in [PRODUCT_CONTEXT] for [TARGET_USERS], ensuring trust, transparency, and graceful handling of AI limitations.

AI FEATURE OVERVIEW:
- Feature name: [AI_FEATURE_NAME]
- AI capability: [AI_CAPABILITY] (e.g., generation, classification, prediction, recommendation)
- Product context: [PRODUCT_CONTEXT]
- Target users: [TARGET_USERS]
- User goal: [USER_GOAL]
- AI confidence range: [CONFIDENCE_RANGE] (e.g., 70-95% accuracy)

### 1. AI INTERACTION PATTERN

Pattern Selection:
- Pattern type: [PATTERN_TYPE]
  - AI Enhancement: AI augments user work (e.g., autocomplete, suggestions)
  - AI Automation: AI performs task autonomously (e.g., auto-tagging, categorization)
  - AI Collaboration: User and AI work together iteratively (e.g., co-writing, design generation)
  - AI Decision Support: AI provides recommendations, user decides (e.g., analytics insights)
  - AI Conversation: Natural language dialogue for complex tasks (e.g., chatbots, assistants)
  - AI Agent: AI takes autonomous actions with oversight (e.g., scheduling, purchasing)

User Control Level:
- Initiation: [USER/SYSTEM/HYBRID] - Who triggers the AI?
- Approval: [REQUIRED/OPTIONAL/NONE] - Does user review before action?
- Editing: [FULL/PARTIAL/NONE] - Can user modify AI output?
- Override: [ALWAYS/CONDITIONAL/NEVER] - Can user reject AI?
- Undo: [ALWAYS/LIMITED/NONE] - Can user reverse AI actions?

### 2. STATE DESIGN

Loading State:
- Trigger: [WHAT_INITIATES_AI]
- Duration estimate: [TYPICAL_TIME]
- Progress indicator: [TYPE] (spinner, progress bar, skeleton, animation)
- User messaging: "[LOADING_MESSAGE]"
- Cancelable: [YES/NO]
- Background processing option: [YES/NO]

**Streaming/Progressive Output (for LLMs):**
```
Streaming State Design:
- Enable streaming: [YES/NO]
- Reveal pattern: [CHARACTER/WORD/SENTENCE/PARAGRAPH]
- Typing indicator: [CURSOR/DOTS/NONE]
- Partial actions: Can user act on partial output? [YES/NO]
- Stop generation: [BUTTON_PLACEMENT]
- Resume/regenerate: [UX_PATTERN]

Example Implementation:
"Generating response..."
↓ (streaming begins)
[Visible text appears progressively]
↓ (generation complete)
[Full response with action buttons]
```

Success State:
- Output presentation: [HOW_RESULTS_DISPLAYED]
- Confidence indicator: [DISPLAY_METHOD] (score, label, visual cue)
- Explanation available: [YES/NO]
- Actions available: [ACCEPT/EDIT/REGENERATE/REJECT]
- Feedback mechanism: [TYPE]

Error State:
- Error types: [ERROR_CATEGORIES]
- User messaging: "[ERROR_MESSAGE_TEMPLATE]"
- Recovery options: [RETRY/MANUAL_FALLBACK/CONTACT_SUPPORT]
- Graceful degradation: [FALLBACK_BEHAVIOR]

Edge Cases:
- Low confidence handling: [APPROACH]
- No results handling: [APPROACH]
- Partial results handling: [APPROACH]
- Timeout handling: [APPROACH]

### 3. TRUST & TRANSPARENCY

Transparency Elements:
- AI disclosure: [HOW_USERS_KNOW_IT'S_AI]
- Source attribution: [IF_APPLICABLE]
- Confidence display: [METHOD]
- Limitations disclosure: [WHERE_AND_HOW]

Explanation Design:
- Explanation type: [TYPE]
  - Feature attribution: "Based on X, Y, Z factors"
  - Example-based: "Similar to these examples..."
  - Counterfactual: "If X were different, result would be..."
  - Confidence breakdown: "High confidence in A, lower in B"
- Detail level: [SUMMARY/DETAILED/BOTH]
- Accessibility: [WHO_CAN_ACCESS]

User Control for Trust:
- Preferences: [USER_CUSTOMIZATION_OPTIONS]
- Data visibility: [WHAT_DATA_AI_USES]
- Opt-out option: [IF_APPLICABLE]
- Feedback impact: [HOW_FEEDBACK_IMPROVES_AI]

### 4. ERROR HANDLING PATTERNS

Proactive Prevention:
- Input validation: [APPROACH]
- Expectation setting: [HOW]
- Scope communication: [WHAT_AI_CAN_AND_CANNOT_DO]

Error Recovery:
- Automatic retry: [LOGIC]
- Manual retry: [USER_ACTION]
- Alternative path: [FALLBACK_FLOW]
- Support escalation: [TRIGGER_AND_PATH]

Error Messaging:
- Tone: [TONE] (apologetic, matter-of-fact, helpful)
- Blame attribution: [NEVER_USER/TECHNICAL_ISSUE/LIMITATION]
- Actionability: [WHAT_USER_CAN_DO]
- Template: "[ERROR_MESSAGE_EXAMPLE]"

### 5. FEEDBACK LOOP DESIGN

Feedback Collection:
- Explicit feedback: [TYPE] (thumbs up/down, star rating, correction)
- Implicit feedback: [TYPE] (acceptance rate, edit frequency, time spent)
- Feedback timing: [WHEN_TO_ASK]
- Feedback friction: [LOW/MEDIUM] - Balance insight with interruption

Feedback Display:
- Acknowledgment: [HOW_USER_KNOWS_FEEDBACK_RECEIVED]
- Impact communication: [HOW_FEEDBACK_HELPS]
- Aggregate insights: [IF_SHARED_WITH_USER]

### 6. ACCESSIBILITY CONSIDERATIONS

Screen Reader Support:
- AI status announcements: [APPROACH]
- Result announcements: [APPROACH]
- Error announcements: [APPROACH]

Keyboard Navigation:
- Focus management during AI processing: [APPROACH]
- Result navigation: [APPROACH]
- Action shortcuts: [IF_APPLICABLE]

Cognitive Accessibility:
- Clear language: [GUIDELINES]
- Reduced motion option: [FOR_ANIMATIONS]
- Extended time options: [IF_APPLICABLE]

### 7. PERFORMANCE EXPECTATIONS

Response Time Targets:
- Instant (< 1s): [FEATURES]
- Fast (1-5s): [FEATURES]
- Medium (5-30s): [FEATURES]
- Long (30s+): [FEATURES_WITH_BACKGROUND_OPTION]

Perceived Performance:
- Skeleton loading: [WHERE_USED]
- Progressive results: [IF_APPLICABLE]
- Optimistic UI: [IF_APPLICABLE]

### 8. CONVERSATIONAL AI UX PATTERNS

Chat Interface Design:
```
Message Types:
- User messages: [STYLING]
- AI responses: [STYLING]
- System messages: [STYLING]
- Error messages: [STYLING]

Conversation Features:
- Message editing: [YES/NO]
- Response regeneration: [YES/NO]
- Conversation branching: [YES/NO]
- History persistence: [DURATION]
- Export/share: [FORMAT]

Input Features:
- Suggested prompts: [WHEN_TO_SHOW]
- Template responses: [IF_APPLICABLE]
- Voice input: [YES/NO]
- File attachments: [SUPPORTED_TYPES]
- Multi-modal input: [IMAGES/FILES/CODE]
```

Conversation Recovery:
```
When AI seems stuck:
- Message: "Let me try a different approach..."
- Action: Offer to restart or clarify

When AI misunderstands:
- Detection: [HOW_TO_DETECT]
- Response: "I may have misunderstood. Did you mean...?"
- Options: [CLARIFICATION_BUTTONS]

Long conversations:
- Context summary: "Here's what we've discussed so far..."
- Topic reset: "Start new topic" option
- Reference previous: "As we discussed earlier..."
```

### 9. MULTI-MODAL AI UX

Image Generation/Editing:
```
Input UX:
- Text prompt: [PROMPT_GUIDELINES]
- Reference images: [UPLOAD_UX]
- Style selection: [UI_PATTERN]
- Aspect ratio: [SELECTION_METHOD]

Output UX:
- Generation progress: [VISUALIZATION]
- Multiple options: Grid of [N] variations
- Refinement: "Make it more [X]" buttons
- Download/export: [FORMATS]
```

Document/File Processing:
```
Upload UX:
- Drag-and-drop: [SUPPORTED]
- File types: [SUPPORTED_TYPES]
- Size limits: [LIMITS_AND_MESSAGING]
- Processing indicator: [PROGRESS_TYPE]

Results UX:
- Inline annotations: [IF_APPLICABLE]
- Summary view: [LAYOUT]
- Source citations: [LINK_TO_ORIGINAL]
```

AI UX OUTPUT:
Generate comprehensive UX design for [AI_FEATURE_NAME] including:
1. Interaction flow with all states
2. UI component specifications
3. Copy/messaging for all scenarios
4. Wireframe recommendations
5. Accessibility checklist
6. Testing scenarios
```

## Variables

### AI_FEATURE_NAME
The name of the AI-powered feature being designed.
- Examples: "Smart Document Summarizer", "AI Writing Assistant", "Predictive Search", "Automated Report Generator"

### PRODUCT_CONTEXT
The product or platform where this AI feature lives.
- Examples: "B2B document management platform", "Consumer mobile app", "Enterprise analytics dashboard"

### TARGET_USERS
The primary users who will interact with this AI feature.
- Examples: "Knowledge workers processing 50+ documents daily", "Casual users writing social media posts", "Data analysts creating weekly reports"

### AI_CAPABILITY
The core AI function powering the feature.
- Examples: "Text generation (GPT-4)", "Image classification (custom CNN)", "Predictive analytics (XGBoost)", "Recommendation engine (collaborative filtering)"

### USER_GOAL
What the user is trying to accomplish with this feature.
- Examples: "Save time on repetitive writing tasks", "Find relevant products faster", "Get insights without SQL knowledge"

### PATTERN_TYPE
The AI interaction pattern that best fits the use case.
- Examples: "AI Enhancement", "AI Automation", "AI Collaboration", "AI Decision Support"

### CONFIDENCE_RANGE
The typical accuracy or confidence range of the AI output.
- Examples: "85-95% accuracy for common queries", "70-80% for complex edge cases", "90%+ for trained categories"

---

## Usage Examples

### Example 1: AI Document Summarizer
```
AI_FEATURE_NAME: "Smart Summary"
PRODUCT_CONTEXT: "Legal document management platform"
TARGET_USERS: "Paralegals reviewing contracts"
AI_CAPABILITY: "Extractive and abstractive summarization"
USER_GOAL: "Quickly understand key contract terms without reading full document"
PATTERN_TYPE: "AI Enhancement"
CONFIDENCE_RANGE: "90-95% for standard contracts, 75-85% for complex/unusual terms"

Key UX Decisions:
- Show summary with highlighted source passages
- Display confidence per section (high/medium/low)
- Allow inline editing of summary
- "View original" button for each point
- Feedback: "Was this summary helpful?" with quick rating
```

### Example 2: AI Writing Assistant
```
AI_FEATURE_NAME: "Writing Copilot"
PRODUCT_CONTEXT: "Email marketing platform"
TARGET_USERS: "Marketing managers creating campaigns"
AI_CAPABILITY: "Text generation and optimization"
USER_GOAL: "Write compelling email copy faster"
PATTERN_TYPE: "AI Collaboration"
CONFIDENCE_RANGE: "N/A - generative, quality varies by prompt"

Key UX Decisions:
- Inline suggestions as user types (ghost text)
- "Generate alternatives" button for selected text
- Tone selector (professional, friendly, urgent)
- A/B variant generator for subject lines
- Feedback: Accept/reject tracked for personalization
```

### Example 3: Predictive Search
```
AI_FEATURE_NAME: "Smart Search"
PRODUCT_CONTEXT: "E-commerce marketplace"
TARGET_USERS: "Shoppers looking for products"
AI_CAPABILITY: "Query understanding + personalized ranking"
USER_GOAL: "Find relevant products with minimal effort"
PATTERN_TYPE: "AI Enhancement"
CONFIDENCE_RANGE: "Top 3 results relevant 85% of the time"

Key UX Decisions:
- Autocomplete with category hints
- "Did you mean..." for typos/alternatives
- Personalized results with "Based on your history" label
- Easy filtering if AI results miss the mark
- Feedback: Click-through and purchase implicit signals
```

### Example 4: AI Chatbot Assistant
```
AI_FEATURE_NAME: "Help Assistant"
PRODUCT_CONTEXT: "SaaS product support"
TARGET_USERS: "Users needing help with product features"
AI_CAPABILITY: "RAG-powered conversational AI"
USER_GOAL: "Get answers without waiting for human support"
PATTERN_TYPE: "AI Conversation"
CONFIDENCE_RANGE: "85% accurate for FAQ, 60% for complex issues"

Key UX Decisions:
- Streaming responses with typing indicator
- Source citations with "Learn more" links
- Suggested follow-up questions
- Easy escalation: "Talk to a human" always visible
- Conversation history saved for context
- Feedback: Thumbs up/down per message
```

### Example 5: AI Code Assistant
```
AI_FEATURE_NAME: "Code Copilot"
PRODUCT_CONTEXT: "IDE/Code editor"
TARGET_USERS: "Software developers"
AI_CAPABILITY: "Code generation, completion, explanation"
USER_GOAL: "Write code faster with fewer errors"
PATTERN_TYPE: "AI Enhancement + AI Collaboration"
CONFIDENCE_RANGE: "Variable by complexity"

Key UX Decisions:
- Ghost text for inline completions (Tab to accept)
- Chat sidebar for complex requests
- Diff view for multi-line suggestions
- Accept/reject with keyboard shortcuts
- "Explain this code" context menu
- Streaming for long generations
```

---

## Best Practices

1. **Set expectations early** - Tell users what AI can and cannot do before they start
2. **Show AI is working** - Never leave users wondering if something is happening
3. **Provide escape hatches** - Always allow users to cancel, edit, or reject AI output
4. **Be honest about uncertainty** - Display confidence when it helps users calibrate trust
5. **Fail gracefully** - Design for AI errors as a normal part of the experience
6. **Explain when helpful** - Offer explanations but don't force them on every user
7. **Learn from feedback** - Close the loop so users know their input matters
8. **Respect user agency** - AI should assist, not take over without permission
9. **Test with real users** - AI UX assumptions often fail in practice
10. **Iterate based on data** - Monitor acceptance rates, edit frequency, and satisfaction

## Common Pitfalls

❌ **Black box AI** - No explanation of how AI reached its output
✅ Instead: Provide appropriate transparency for the context

❌ **Overconfident presentation** - Presenting uncertain AI output as fact
✅ Instead: Use hedging language and confidence indicators

❌ **No user control** - AI makes decisions without user approval
✅ Instead: Default to user confirmation for high-stakes actions

❌ **Poor error messages** - "Something went wrong" with no guidance
✅ Instead: Specific, actionable error messages with recovery paths

❌ **Ignoring feedback** - Collecting feedback but never acting on it
✅ Instead: Show users how their feedback improves the system

❌ **Ignoring streaming** - Making users wait for complete AI response
✅ Instead: Stream long responses progressively for better perceived performance

❌ **Modal overload** - Interrupting user flow with AI confirmations
✅ Instead: Use inline, non-blocking UI patterns where possible

---

**Last Updated:** 2025-11-25
**Category:** AI/ML Applications > AI Product Development
**Difficulty:** Intermediate
**Estimated Time:** 2-3 weeks for complete AI UX design
