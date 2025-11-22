---
category: ai-ml-applications
last_updated: 2025-11-12
title: Conversational AI & Chatbot Development
tags:
- ai-ml
- llm
- chatbot
- conversational-ai
- customer-service
use_cases:
- Building customer service chatbots for websites and apps
- Creating internal AI assistants for employee support
- Developing voice assistants and conversational interfaces
- Building domain-specific chat experiences (sales, support, HR)
related_templates:
- ai-ml-applications/LLM-Applications/llm-application-development.md
- ai-ml-applications/LLM-Applications/rag-systems.md
- ai-ml-applications/LLM-Applications/prompt-engineering-workflows.md
- ai-ml-applications/AI-Product-Development/ai-ux-interaction-design.md
industries:
- technology
- finance
- healthcare
- retail
- manufacturing
type: template
difficulty: intermediate
slug: conversational-ai-chatbots
---

# Conversational AI & Chatbot Development Template

## Purpose
Design and build production-grade conversational AI systems and chatbots that provide natural, helpful, and context-aware interactions while maintaining reliability and user satisfaction.

## Quick Start

**Need to build a chatbot quickly?** Use this streamlined approach:

### Minimal Example
```python
# Simple stateful chatbot
from anthropic import Anthropic

client = Anthropic()

class SimpleChatbot:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt
        self.conversation_history = []

    def chat(self, user_message: str) -> str:
        """Send message and get response"""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Get response from Claude
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=2048,
            system=self.system_prompt,
            messages=self.conversation_history
        )

        assistant_message = response.content[0].text

        # Add assistant response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })

        return assistant_message

# Use it
chatbot = SimpleChatbot(
    system_prompt="You are a helpful customer service agent for TechCorp. Be friendly and professional."
)

response1 = chatbot.chat("What are your business hours?")
response2 = chatbot.chat("And what about holidays?")  # Maintains context
```

### When to Use This
- Customer service automation (support tickets, FAQ)
- Sales assistance (product recommendations, lead qualification)
- Internal tools (HR assistant, IT helpdesk)
- User onboarding and tutorials
- Appointment scheduling and booking

### Basic 5-Step Workflow
1. **Define Scope** - What topics chatbot handles, success metrics
2. **Design Conversation Flow** - Map user journeys and bot responses
3. **Build Core System** - Implement conversation management and LLM integration
4. **Add Intelligence** - Context awareness, personalization, knowledge base
5. **Test & Optimize** - Iterate on conversation quality and user satisfaction

---

## Template

```
You are an expert in building conversational AI systems and chatbots. Help me design a chatbot for [USE_CASE] that handles [CONVERSATION_TYPES] for [TARGET_USERS] using [LLM_PROVIDER] with [SUCCESS_CRITERIA].

CHATBOT CONTEXT:
Project Overview:
- Chatbot name: [BOT_NAME]
- Primary use case: [USE_CASE]
- Deployment: [WEBSITE/MOBILE_APP/SLACK/WHATSAPP/VOICE]
- Target users: [USER_DEMOGRAPHICS]
- Expected volume: [CONVERSATIONS_PER_DAY]
- Success metrics: [KEY_METRICS]

Conversation Scope:
- Topics handled: [LIST_OF_TOPICS]
- Out of scope: [WHAT_BOT_CANNOT_HELP_WITH]
- Average conversation length: [NUMBER_OF_TURNS]
- Escalation conditions: [WHEN_TO_HANDOFF_TO_HUMAN]
- Languages: [SUPPORTED_LANGUAGES]

Business Context:
- Company/Product: [COMPANY_INFO]
- Brand voice: [BRAND_PERSONALITY]
- Integration points: [CRM/TICKETING/KNOWLEDGE_BASE]
- Compliance requirements: [REGULATIONS/POLICIES]

### 1. CONVERSATION DESIGN

Chatbot Personality & Voice:
```
Name: [BOT_NAME]
Persona: [PERSONALITY_DESCRIPTION]

Brand Voice Guidelines:
- Tone: [PROFESSIONAL/FRIENDLY/CASUAL/FORMAL]
- Language style: [CONVERSATIONAL/TECHNICAL/SIMPLE]
- Personality traits: [HELPFUL/EMPATHETIC/EFFICIENT/WITTY]

Do's:
- [DO_1]
- [DO_2]
- [DO_3]

Don'ts:
- [DONT_1]
- [DONT_2]
- [DONT_3]

Example messages:
Good: "I'd be happy to help you with that! Let me look into your order status."
Bad: "I will process your request. Please wait."
```

System Prompt Design:
```python
SYSTEM_PROMPT = """You are {bot_name}, a {personality} AI assistant for {company}.

Your role:
{role_description}

Your capabilities:
- {capability_1}
- {capability_2}
- {capability_3}

Guidelines:
1. Be {tone} and {style}
2. Keep responses concise (2-3 sentences typically)
3. Use {language_style} language
4. Always {key_behavior}
5. Never {prohibited_behavior}

When you don't know something:
{uncertainty_handling}

When escalating to human:
{escalation_protocol}

Context awareness:
- Remember key information from earlier in conversation
- Refer back to previous mentions naturally
- Don't ask for information the user already provided

Available resources:
{knowledge_base_description}
"""

# Example for customer service bot
CUSTOMER_SERVICE_SYSTEM = """You are SupportBot, a friendly and efficient customer service AI for TechCorp.

Your role:
Help customers with account issues, order tracking, product questions, and technical support.

Your capabilities:
- Look up order status
- Reset passwords
- Answer product questions from knowledge base
- Troubleshoot common technical issues
- Escalate complex issues to human agents

Guidelines:
1. Be empathetic and professional
2. Keep responses concise and actionable
3. Use simple, jargon-free language
4. Always acknowledge the customer's frustration or concern
5. Never make promises you can't keep (refunds, specific timelines)

When you don't know something:
"I don't have that specific information, but I can connect you with a specialist who can help."

When escalating to human:
"This needs a specialist's attention. I'm transferring you to our {team} team now. They'll have access to our full conversation."

Available resources:
- Order database (via order_lookup tool)
- Knowledge base (via search_kb tool)
- Customer profile (via get_customer tool)
"""
```

Conversation Flows:
```
Core User Journeys:

Journey 1: Order Status Check
User: "Where's my order?"
Bot: Greet, ask for order number
User: Provides order number
Bot: Look up status, provide update
Bot: Offer tracking link
Bot: Ask if anything else needed

Journey 2: Technical Issue
User: "The app isn't working"
Bot: Empathize, ask clarifying questions
User: Provides details
Bot: Suggest troubleshooting steps
User: Tries steps
Bot: Check if resolved
  → If yes: Great! Anything else?
  → If no: Escalate to technical support

Journey 3: Product Question
User: "What's the difference between Plan A and B?"
Bot: Search knowledge base
Bot: Provide clear comparison
Bot: Offer to help with purchase decision
User: Asks follow-up
Bot: Provide additional details
Bot: Suggest next steps
```

### 2. CONVERSATION STATE MANAGEMENT

Session State:
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class ConversationState:
    """Track conversation state"""
    session_id: str
    user_id: Optional[str]
    started_at: datetime
    last_activity: datetime

    # Conversation history
    messages: list[dict]

    # Extracted entities
    entities: dict  # e.g., {"order_id": "12345", "product": "Pro Plan"}

    # Context tracking
    current_topic: Optional[str]
    intent: Optional[str]
    sentiment: str  # positive, neutral, negative, frustrated

    # Flags
    needs_human: bool = False
    resolved: bool = False
    escalated: bool = False

    # Metadata
    metadata: dict = None

class ConversationManager:
    """Manage conversation state and history"""

    def __init__(self, storage):
        self.storage = storage
        self.active_sessions = {}

    def start_conversation(self, user_id: str = None) -> str:
        """Initialize new conversation"""
        session_id = generate_session_id()

        state = ConversationState(
            session_id=session_id,
            user_id=user_id,
            started_at=datetime.now(),
            last_activity=datetime.now(),
            messages=[],
            entities={},
            current_topic=None,
            intent=None,
            sentiment="neutral"
        )

        self.active_sessions[session_id] = state
        return session_id

    def add_message(self, session_id: str, role: str, content: str):
        """Add message to conversation"""
        state = self.get_state(session_id)

        state.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now()
        })

        state.last_activity = datetime.now()

        # Persist state
        self.storage.save(session_id, state)

    def get_state(self, session_id: str) -> ConversationState:
        """Retrieve conversation state"""
        if session_id in self.active_sessions:
            return self.active_sessions[session_id]

        # Load from storage
        state = self.storage.load(session_id)
        self.active_sessions[session_id] = state
        return state

    def update_context(self, session_id: str, updates: dict):
        """Update conversation context"""
        state = self.get_state(session_id)

        # Update entities
        if "entities" in updates:
            state.entities.update(updates["entities"])

        # Update topic/intent
        if "topic" in updates:
            state.current_topic = updates["topic"]
        if "intent" in updates:
            state.intent = updates["intent"]
        if "sentiment" in updates:
            state.sentiment = updates["sentiment"]

        self.storage.save(session_id, state)
```

Context Window Management:
```python
def build_llm_context(state: ConversationState, max_tokens: int = 8000) -> list:
    """Build context for LLM, managing token budget"""

    messages = []

    # Always include recent messages
    recent_messages = state.messages[-10:]  # Last 10 messages

    # If conversation is long, summarize older parts
    if len(state.messages) > 10:
        older_messages = state.messages[:-10]
        summary = summarize_conversation(older_messages)

        messages.append({
            "role": "user",
            "content": f"Previous conversation summary: {summary}"
        })

    # Add recent messages
    messages.extend(recent_messages)

    # Add relevant context
    if state.entities:
        context_note = f"Key information from conversation: {format_entities(state.entities)}"
        messages.append({
            "role": "user",
            "content": context_note
        })

    return messages
```

### 3. INTENT RECOGNITION & ENTITY EXTRACTION

Intent Classification:
```python
async def classify_intent(message: str, context: dict) -> str:
    """Classify user intent"""

    intents = {
        "order_status": "Check order status",
        "technical_support": "Get technical help",
        "billing_question": "Billing or payment question",
        "product_inquiry": "Product information",
        "complaint": "File a complaint",
        "general_question": "General question",
        "chitchat": "Small talk"
    }

    prompt = f"""Classify the user's intent from this message.

Available intents:
{format_intents(intents)}

Message: "{message}"
Previous context: {context.get('current_topic', 'None')}

Return only the intent name."""

    intent = await llm.complete(prompt)
    return intent.strip()
```

Entity Extraction:
```python
async def extract_entities(message: str, intent: str) -> dict:
    """Extract structured entities from message"""

    # Define entities to extract based on intent
    entity_schemas = {
        "order_status": ["order_id", "order_date", "customer_email"],
        "product_inquiry": ["product_name", "feature", "plan_type"],
        "technical_support": ["issue_type", "error_message", "device_type"]
    }

    schema = entity_schemas.get(intent, [])

    if not schema:
        return {}

    prompt = f"""Extract these entities from the message:
Entities to extract: {schema}

Message: "{message}"

Return as JSON. Use null for missing entities."""

    result = await llm.complete(prompt)
    entities = json.loads(result)

    return entities
```

Sentiment Analysis:
```python
async def analyze_sentiment(message: str, history: list) -> str:
    """Analyze user sentiment"""

    prompt = f"""Analyze the sentiment of this customer message.

Recent conversation:
{format_history(history[-3:])}

Current message: "{message}"

Classify sentiment as:
- positive (happy, satisfied)
- neutral (just asking questions)
- negative (dissatisfied, annoyed)
- frustrated (angry, urgent)

Return only the sentiment label."""

    sentiment = await llm.complete(prompt)
    return sentiment.strip().lower()
```

### 4. KNOWLEDGE BASE INTEGRATION

```python
class KnowledgeBaseConnector:
    """Connect chatbot to knowledge base"""

    def __init__(self, vector_db, fallback_responses):
        self.vector_db = vector_db
        self.fallback_responses = fallback_responses

    async def search_knowledge(self, query: str, context: dict) -> dict:
        """Search knowledge base for relevant information"""

        # Enhance query with context
        enhanced_query = self.enhance_query(query, context)

        # Search vector DB
        results = self.vector_db.query(
            query_texts=[enhanced_query],
            n_results=3,
            where={"category": context.get("topic")}  # Filter by topic if known
        )

        if not results or results["distances"][0][0] > 0.5:
            # No good match found
            return {
                "found": False,
                "response": self.get_fallback_response(context)
            }

        # Format knowledge for bot
        knowledge = self.format_knowledge(results)

        return {
            "found": True,
            "knowledge": knowledge,
            "sources": results["metadatas"]
        }

    def enhance_query(self, query: str, context: dict) -> str:
        """Add context to improve search"""
        if context.get("current_topic"):
            return f"{context['current_topic']}: {query}"
        return query

    def format_knowledge(self, results: dict) -> str:
        """Format KB results for bot consumption"""
        docs = results["documents"][0]
        formatted = "Relevant information:\n"
        for i, doc in enumerate(docs, 1):
            formatted += f"{i}. {doc}\n"
        return formatted

    def get_fallback_response(self, context: dict) -> str:
        """Get appropriate fallback when no KB match"""
        topic = context.get("current_topic", "general")
        return self.fallback_responses.get(
            topic,
            "I don't have specific information about that. Let me connect you with someone who can help."
        )
```

### 5. RESPONSE GENERATION

Multi-Source Response Generation:
```python
async def generate_response(
    user_message: str,
    conversation_state: ConversationState,
    knowledge: dict,
    tools: dict
) -> str:
    """Generate contextual response using multiple sources"""

    # Build context for LLM
    context_parts = []

    # 1. Conversation history
    context_parts.append(
        format_conversation_history(conversation_state.messages[-5:])
    )

    # 2. User profile/preferences
    if conversation_state.user_id:
        profile = get_user_profile(conversation_state.user_id)
        context_parts.append(f"User context: {profile}")

    # 3. Knowledge base information
    if knowledge.get("found"):
        context_parts.append(f"Knowledge base:\n{knowledge['knowledge']}")

    # 4. Sentiment-aware instruction
    if conversation_state.sentiment == "frustrated":
        context_parts.append(
            "IMPORTANT: User seems frustrated. Be extra empathetic and helpful."
        )

    # Generate response
    full_context = "\n\n".join(context_parts)

    response = await llm.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{
            "role": "user",
            "content": f"{full_context}\n\nUser message: {user_message}\n\nRespond naturally:"
        }]
    )

    bot_response = response.content[0].text

    # Post-process response
    bot_response = apply_brand_voice(bot_response)
    bot_response = check_safety_filters(bot_response)

    return bot_response
```

Personalization:
```python
def personalize_response(response: str, user_profile: dict) -> str:
    """Personalize response based on user"""

    # Use user's name
    if user_profile.get("name"):
        response = response.replace("{user_name}", user_profile["name"])

    # Adjust complexity based on user expertise
    if user_profile.get("expertise_level") == "beginner":
        response = simplify_language(response)

    # Adjust tone based on preferences
    if user_profile.get("preferred_tone") == "casual":
        response = make_more_casual(response)

    return response
```

### 6. ESCALATION & HANDOFF

Escalation Decision Logic:
```python
def should_escalate(state: ConversationState) -> tuple[bool, str]:
    """Determine if conversation should escalate to human"""

    # Explicit user request
    if any(phrase in state.messages[-1]["content"].lower()
           for phrase in ["speak to human", "talk to person", "real person"]):
        return True, "User requested human agent"

    # Sentiment-based escalation
    if state.sentiment == "frustrated" and len(state.messages) > 6:
        return True, "User frustrated after multiple turns"

    # Intent-based escalation
    high_priority_intents = ["complaint", "refund_request", "legal_issue"]
    if state.intent in high_priority_intents:
        return True, f"High priority intent: {state.intent}"

    # Loop detection
    if detect_conversation_loop(state.messages):
        return True, "Conversation stuck in loop"

    # Bot confidence
    if state.metadata.get("bot_confidence", 1.0) < 0.5:
        return True, "Bot confidence too low"

    # Complexity threshold
    if state.metadata.get("complexity_score", 0) > 0.8:
        return True, "Issue too complex for bot"

    return False, None

def handoff_to_human(state: ConversationState, reason: str) -> dict:
    """Prepare handoff to human agent"""

    # Generate conversation summary
    summary = generate_handoff_summary(state)

    # Create handoff package
    handoff = {
        "session_id": state.session_id,
        "user_id": state.user_id,
        "reason": reason,
        "summary": summary,
        "entities": state.entities,
        "sentiment": state.sentiment,
        "full_history": state.messages,
        "priority": calculate_priority(state)
    }

    # Route to appropriate team
    team = route_to_team(state.intent)

    # Notify human agent
    notify_agent(team, handoff)

    return {
        "escalated": True,
        "team": team,
        "message": "I'm connecting you with a specialist now. They'll have our full conversation history."
    }

def generate_handoff_summary(state: ConversationState) -> str:
    """Summarize conversation for human agent"""

    prompt = f"""Summarize this customer conversation for a human agent taking over.

Include:
- Customer's main issue/question
- Key information gathered (order #, account details, etc.)
- What's been tried/discussed
- Customer sentiment
- Why escalating

Conversation:
{format_conversation(state.messages)}

Provide concise summary (3-4 sentences)."""

    summary = llm.complete(prompt)
    return summary
```

### 7. MULTI-CHANNEL DEPLOYMENT

Platform Adapters:
```python
class WebChatAdapter:
    """Adapter for web chat widget"""

    def format_message(self, bot_response: str, metadata: dict) -> dict:
        """Format response for web chat"""
        return {
            "type": "text",
            "content": bot_response,
            "timestamp": datetime.now().isoformat(),
            "quick_replies": metadata.get("quick_replies", []),
            "attachments": metadata.get("attachments", [])
        }

class SlackAdapter:
    """Adapter for Slack"""

    def format_message(self, bot_response: str, metadata: dict) -> dict:
        """Format response for Slack"""
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": bot_response
                }
            }
        ]

        # Add action buttons if present
        if metadata.get("actions"):
            blocks.append({
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": action["label"]},
                        "action_id": action["id"]
                    }
                    for action in metadata["actions"]
                ]
            })

        return {"blocks": blocks}

class WhatsAppAdapter:
    """Adapter for WhatsApp"""

    def format_message(self, bot_response: str, metadata: dict) -> dict:
        """Format response for WhatsApp"""

        # WhatsApp has 4096 character limit
        if len(bot_response) > 4000:
            # Split into multiple messages
            return self.split_message(bot_response)

        message = {
            "messaging_product": "whatsapp",
            "to": metadata["phone_number"],
            "type": "text",
            "text": {"body": bot_response}
        }

        return message
```

### 8. TESTING & EVALUATION

Conversation Quality Metrics:
```python
def evaluate_conversation(session_id: str) -> dict:
    """Evaluate conversation quality"""

    state = conversation_manager.get_state(session_id)

    metrics = {
        # Efficiency
        "num_turns": len(state.messages) // 2,
        "resolution_time": (state.last_activity - state.started_at).seconds,

        # Effectiveness
        "resolved": state.resolved,
        "escalated": state.escalated,

        # User experience
        "final_sentiment": state.sentiment,
        "bot_understanding": calculate_understanding_score(state),

        # Quality
        "response_relevance": calculate_relevance(state),
        "coherence": calculate_coherence(state.messages)
    }

    return metrics

def calculate_understanding_score(state: ConversationState) -> float:
    """Did bot understand user correctly?"""

    # Check if bot asked for clarification
    clarification_requests = sum(
        1 for msg in state.messages
        if msg["role"] == "assistant" and is_clarification(msg["content"])
    )

    # Check if intent matched user behavior
    intent_accuracy = evaluate_intent_accuracy(state)

    # Fewer clarifications + accurate intent = better understanding
    score = intent_accuracy - (clarification_requests * 0.1)
    return max(0, min(1, score))
```

Automated Testing:
```python
def test_chatbot(test_conversations: list[dict]):
    """Test chatbot against scenarios"""

    results = []

    for test in test_conversations:
        # Start conversation
        session_id = chatbot.start_conversation()

        # Simulate user messages
        for turn in test["conversation"]:
            response = chatbot.chat(session_id, turn["user_message"])

            # Evaluate response
            evaluation = {
                "user_message": turn["user_message"],
                "bot_response": response,
                "expected_intent": turn.get("expected_intent"),
                "detected_intent": get_intent(session_id),
                "contains_required_info": check_required_info(
                    response,
                    turn.get("required_info", [])
                ),
                "appropriate_tone": check_tone(response, test["brand_voice"])
            }

            results.append(evaluation)

    # Aggregate results
    return analyze_test_results(results)
```

### 9. PRODUCTION DEPLOYMENT

Complete Chatbot Service:
```python
class ProductionChatbot:
    """Production-ready chatbot service"""

    def __init__(self, config: dict):
        self.config = config
        self.llm = initialize_llm(config)
        self.conversation_manager = ConversationManager(storage=init_storage())
        self.knowledge_base = KnowledgeBaseConnector(init_vector_db())
        self.safety = SafetyFilter()
        self.monitor = ChatbotMonitor()

    async def handle_message(
        self,
        user_message: str,
        session_id: str = None,
        user_id: str = None
    ) -> dict:
        """Main message handling endpoint"""

        # Create or retrieve session
        if not session_id:
            session_id = self.conversation_manager.start_conversation(user_id)

        state = self.conversation_manager.get_state(session_id)

        # Input safety check
        if not self.safety.is_safe_input(user_message):
            return {"response": "I'm sorry, I can't process that message."}

        # Add user message to state
        self.conversation_manager.add_message(session_id, "user", user_message)

        # Analyze message
        intent = await classify_intent(user_message, state)
        entities = await extract_entities(user_message, intent)
        sentiment = await analyze_sentiment(user_message, state.messages)

        # Update state
        self.conversation_manager.update_context(session_id, {
            "intent": intent,
            "entities": entities,
            "sentiment": sentiment
        })

        # Check if should escalate
        should_esc, reason = should_escalate(state)
        if should_esc:
            return handoff_to_human(state, reason)

        # Search knowledge base
        knowledge = await self.knowledge_base.search_knowledge(
            user_message,
            {"intent": intent, "topic": state.current_topic}
        )

        # Generate response
        response = await generate_response(
            user_message,
            state,
            knowledge,
            self.config["tools"]
        )

        # Add to conversation
        self.conversation_manager.add_message(session_id, "assistant", response)

        # Log for monitoring
        self.monitor.log_interaction(session_id, {
            "user_message": user_message,
            "bot_response": response,
            "intent": intent,
            "sentiment": sentiment
        })

        return {
            "session_id": session_id,
            "response": response,
            "quick_replies": self.generate_quick_replies(intent, state)
        }
```
```

## Variables

### USE_CASE
The primary use case for your chatbot.
**Examples:**
- "Customer service chatbot for e-commerce website"
- "HR assistant for employee questions about policies"
- "Technical support bot for SaaS product"
- "Sales assistant for lead qualification and product recommendations"

### CONVERSATION_TYPES
Types of conversations the bot handles.
**Examples:**
- "Order tracking, returns, product questions, account issues"
- "Benefits questions, PTO requests, policy lookups, IT support"
- "Troubleshooting, how-to guides, feature questions, bug reports"
- "Product recommendations, pricing questions, demo scheduling"

### TARGET_USERS
Who will interact with the chatbot.
**Examples:**
- "E-commerce customers (ages 25-55, tech-savvy)"
- "Company employees (all departments)"
- "B2B customers (technical users, developers)"
- "Website visitors (sales prospects and existing customers)"

## Best Practices

### Conversation Design
1. **Clear scope** - Define what bot can and cannot help with
2. **Natural conversation** - Don't make it feel like a form
3. **Empathy first** - Acknowledge user feelings, especially frustration
4. **Progressive disclosure** - Ask one question at a time
5. **Quick replies** - Offer buttons/suggestions for common responses

### User Experience
1. **Fast responses** - Users expect <2s response time
2. **Show typing indicator** - Signal that bot is working
3. **Graceful fallback** - Always have a response, never say "Error"
4. **Easy escalation** - Make it easy to reach a human
5. **Conversation reset** - Allow users to start over

### Context Management
1. **Remember key info** - Don't ask twice for order number
2. **Summarize long conversations** - Maintain context without token bloat
3. **Persist across sessions** - Remember returning users
4. **Clear when needed** - Know when to "forget" irrelevant context
5. **User privacy** - Clear PII after conversation ends

### Quality
1. **Diverse testing** - Test with real user messages, not just happy paths
2. **Monitor intent accuracy** - Track if bot understands correctly
3. **Sentiment tracking** - Catch frustrated users early
4. **Loop detection** - Don't get stuck repeating same responses
5. **Regular updates** - Keep knowledge base current

## Common Pitfalls

❌ **No escalation path** - Users stuck with unhelpful bot
✅ Instead: Clear escalation triggers, easy access to human

❌ **Losing context** - Asking for info already provided
✅ Instead: Track entities, reference previous mentions

❌ **Too formal** - Sounds robotic and cold
✅ Instead: Conversational tone, empathy, personality

❌ **No fallback** - Breaking when it doesn't understand
✅ Instead: Graceful "I'm not sure" responses, offer alternatives

❌ **Ignoring sentiment** - Same response to happy and angry users
✅ Instead: Adjust tone and urgency based on sentiment

❌ **Long responses** - Overwhelming wall of text
✅ Instead: Concise responses, break into multiple messages if needed

❌ **No testing with real data** - Only works in demos
✅ Instead: Test with actual user messages, handle typos and variations

❌ **Static knowledge** - Information gets outdated
✅ Instead: Regular KB updates, versioning, freshness checks

## Related Resources

**Platforms:**
- Dialogflow
- Rasa
- Botpress
- Microsoft Bot Framework

**Tools:**
- Voiceflow (conversation design)
- Botmock (prototyping)
- Dashbot (analytics)
- Chatbase (optimization)

**Best Practices:**
- Conversation Design Institute
- Nielsen Norman Group - Chatbot UX
- Google's Conversation Design Guide

---

**Last Updated:** 2025-11-12
**Category:** AI/ML Applications > LLM Applications
**Difficulty:** Intermediate
**Estimated Time:** 2-3 weeks for production-ready chatbot
