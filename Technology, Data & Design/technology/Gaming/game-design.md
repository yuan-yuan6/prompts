---
category: technology
related_templates:
- technology/Gaming/game-design-framework.md
tags:
- game-design
- player-experience
- monetization
- live-ops
title: Game Design Quick Reference
use_cases:
- Rapid game design planning for indie to mid-size studios requiring core loop validation, retention targets, and monetization planning
- Quick scoping for prototypes, game jams, or MVP validation before full production commitment
- Streamlined framework for mobile/casual games with straightforward mechanics and live ops needs
industries:
- technology
type: framework
difficulty: intermediate
slug: game-design
---

# Game Design Quick Reference

## Purpose
Streamlined game design framework for rapid planning covering core gameplay loop, retention targets (D1 40-50%, D7 20-30%, D30 10-15%), monetization model (premium/F2P/hybrid), and live operations cadence achieving player engagement and revenue goals.

## Template

Design {GAME_TITLE} in {GENRE} for {PLATFORM} with {TEAM_SIZE} team, {BUDGET} budget, {TIMELINE} timeline achieving {RETENTION_D7}% D7 retention and {REVENUE_TARGET} revenue.

**CORE DESIGN FOUNDATIONS**

Define 30-second gameplay loop players repeat every session. Match-3 puzzle: swap tiles (2s) → match clears (1s) → cascades trigger (2s) → score updates and stars earned (1s) → next move or level complete, total 6-10 seconds maintaining flow state. Roguelike dungeon: enter room → identify enemy patterns → execute combat (dodge/attack cycle 10-20s) → collect loot → progress to next room, 30-60 seconds per encounter. Building strategy: gather resources (10s) → place structures (5s) → defend against waves (15s) → upgrade and expand, 30-45 second micro-loops within longer sessions. Validate loop fun factor through paper prototype or 2-week digital MVP before production investment.

Set retention targets driving all other decisions. Mobile F2P benchmarks: D1 retention 40-50% (excellent onboarding and first-session hooks), D7 retention 20-30% (daily engagement loops habituating players), D30 retention 10-15% (long-term content and social features sustaining engagement). Premium games higher: D1 60-70% (paid users more committed), D7 40-50% (content-driven not habit-driven), D30 20-30% (narrative or mastery sustains). Session targets: casual mobile 5-15 minutes supporting snacking behavior, mid-core 20-45 minutes allowing meaningful progression, hardcore 60+ minutes for deep systems engagement.

Choose monetization model matching platform and audience. Premium ($20-60) for PC/console: upfront payment recovers development costs, complete experience without IAP, DLC expansions ($15-30) extend lifetime 6-12 months post-launch. Free-to-play for mobile/live-service: 2-5% conversion rate (100K downloads → 2K-5K payers), ARPU $3-10 across all users, ARPPU $50-100 for paying segment, LTV $50-100 total over 180 days. Hybrid buy-to-play: $20-40 base game plus optional cosmetics ($5-15), balances upfront revenue with long-tail monetization, battle pass ($10/season) drives engagement and recurring revenue.

**LIVE OPERATIONS PLANNING**

Structure content cadence sustaining engagement. Mobile F2P aggressive update schedule: 2-4 content updates monthly (new levels, characters, features maintaining freshness), weekly events (limited-time modes, challenges, exclusive rewards creating urgency), daily login bonuses (streak-based escalating rewards habituating daily check-ins). Premium games moderate cadence: monthly patches (bug fixes, balance, small features), quarterly DLC (10-20 hours new content, $15-30 price point), seasonal events (holiday themes, limited cosmetics building community). Mid-core balance: bi-weekly updates (balance patches, new content items), monthly major updates (new game modes, systems, progression), quarterly seasons (battle pass, ranked resets, meta shifts).

Design battle pass driving seasonal engagement. 100-tier structure: free track (20% rewards enticing purchase), premium track $10 (full rewards worth $50 if bought separately), completion requires 40-60 hours over 3-month season. Reward pacing front-loaded: tiers 1-25 require 1 hour each (instant gratification hooking buyers), tiers 26-75 require 2 hours (steady progression maintaining engagement), tiers 76-100 require 3-4 hours (prestige completion for dedicated players). Renewal targets 70% of season 1 buyers purchasing season 2 (proven value, sunk cost continuing investment, FOMO for exclusive rewards never returning).

Implement daily engagement loops. Login rewards: day 1-7 small rewards (soft currency, consumables), day 8-14 better rewards (premium currency, rare items), day 15+ best rewards (legendary items, exclusive cosmetics), streak breaks reset creating anxiety. Daily quests: 3-5 simple objectives (play 3 matches, complete 1 dungeon, deal 10K damage), 30-60 minute total completion time, rewards soft currency and battle pass XP. First-win-of-day bonus: doubles rewards encouraging at least one session, resets midnight UTC, stacks versus punishes missed days based on design philosophy.

**TECHNICAL AND TEAM SCOPING**

Select game engine matching team expertise and platform targets. Unity for mobile and indie PC: cross-platform deployment (iOS/Android/PC/console from single codebase), large asset store accelerating development, C# accessible to programmers, free under $100K revenue. Unreal for high-fidelity console/PC: photorealistic graphics (Nanite geometry, Lumen lighting), Blueprint visual scripting for designers, 5% royalty after $1M revenue. Godot for budget-conscious indies: completely free (no royalties ever), lightweight and fast iteration, smaller ecosystem requiring more custom development.

Structure team for scope and timeline. Indie 5-person team (18-month development, $300K budget): 2 programmers (client + server), 1.5 artists (2D/3D generalist + outsource support), 1 designer (systems + levels), 0.5 producer (part-time PM), targeting 20K-200K sales $20-30 premium game. Mid-size 25-person team (18-month mobile F2P, $2M budget): 8 programmers, 10 artists, 4 designers, 2 QA, 1 producer, targeting 10M downloads Year 1 with $0.10 ARPDAU = $365K daily at 1M DAU. AAA 150-person team (4-year console AAA, $50M budget): 50 programmers, 60 artists, 20 designers, 15 QA, 5 producers, targeting 5M sales $70 = $350M gross revenue.

Plan milestones and validation gates. Month 1-3 pre-production: paper prototype validating core loop fun, technical proof-of-concept (engine chosen, basic systems working), vertical slice 15-30 minutes demonstrating vision. Month 4-9 production: core systems implemented (progression, combat, UI), content production ramping (first 20% of final content volume), first playable build with 2-3 hours gameplay. Month 10-15 alpha: feature complete (all systems implemented), content 70% complete, first external playtests gathering feedback, balance iteration based on data. Month 16-21 beta: content 100% complete, polish pass (effects, audio, UI refinement), stress testing (multiplayer load, device compatibility), soft launch for live-service validating metrics. Month 22-24 launch: final certification (console approval, app store review), marketing campaign coordination, launch day monitoring and hotfix readiness.

Deliver game design as:

1. **CORE LOOP DEFINITION** - 30-second gameplay loop description, flow chart showing action → feedback → reward, prototype validation results

2. **RETENTION TARGETS** - D1/D7/D30 benchmarks, session length and frequency goals, churn analysis and improvement plan

3. **MONETIZATION MODEL** - Revenue model selection (premium/F2P/hybrid), pricing strategy, conversion and ARPU targets, ethical guidelines

4. **CONTENT ROADMAP** - Launch content volume, post-launch update cadence, live ops calendar (events, seasons, updates), 12-month vision

5. **TECHNICAL SCOPE** - Engine selection, platform targets, performance benchmarks (60fps, load times <5s), team structure and budget

6. **SUCCESS METRICS** - Player count targets, revenue goals, Metacritic/review score targets, competitive positioning versus similar games

---

## Usage Examples

### Example 1: Mobile Match-3 Casual
**Prompt:** Design PuzzleBlast match-3 for iOS/Android with 5-person team, $500K budget, 12 months achieving D1 45%, D7 20%, D30 10% and $0.85 ARPDAU.

**Expected Output:** Core loop (8 seconds): swap adjacent tiles → 3+ match clears with particle effects → cascade combos → earn points toward 3-star completion → progress through level. Retention: D1 45% via generous tutorial completion rewards (50% of session-average gold), D7 20% through daily login streak (gems on day 7), D30 10% via guild/alliance social features (50% of guild members show 3x retention versus solo players). Monetization: F2P lives system (5 lives regenerating 1 per 30 minutes, $0.99 for 5 instant lives), coin shop ($0.99-$9.99 tiers), battle pass $9.99/season. Content: 500 levels at launch (20 per themed world), 15 new levels weekly post-launch, monthly themed events (Halloween, Christmas). Team: 2 programmers (Unity C#), 2 artists (2D casual aesthetic), 1 designer (levels + systems). Timeline: month 1-3 core loop prototype, month 4-6 meta progression and economy, month 7-9 live ops features, month 10-12 content production and soft launch. Success: 1M downloads Year 1, $0.85 ARPDAU at 100K DAU = $85K daily revenue, 3% conversion rate, $28 ARPPU.

### Example 2: PC Indie Premium Roguelike
**Prompt:** Design DungeonMaster roguelike for PC/Steam with 5-person team, $300K budget, 18 months achieving 89% positive reviews and 200K sales $19.99.

**Expected Output:** Core loop (60 seconds): enter procedural dungeon room → identify enemy attack patterns (0.5s telegraphs) → execute dodge/parry/attack combat → defeat enemies collecting random loot → choose upgrade from 3 options → progress to next room. Retention: Premium model less reliant on daily habits, focusing on deep replayability via 50+ weapons with unique movesets, 100+ passive items synergizing unexpectedly, 5 unlockable characters changing playstyle significantly, seeded daily challenge runs with leaderboards. Monetization: $19.99 premium one-time purchase (recovering $300K requires 15K sales at $10 net after Steam 30% cut, break-even at 30K, profitable at 200K = $1.4M revenue), no planned DLC (complete experience, free post-launch content updates building goodwill), optional cosmetic DLC $4.99 (soundtrack + artbook) 6 months later. Content: 10 procedural biomes, 50 weapons, 100 items, 30 enemy types, 10 bosses at launch, post-launch adds new biome month 3, new character month 6, hard mode + endless mode month 12. Team: 2 programmers (combat feel iteration critical), 2 artists (pixel art style), 1 designer (balance + procedural generation algorithms). Success: 200K sales, 89% positive Steam reviews, featured in Steam Next Fest demo generating 50K wishlists, influencer coverage (50 roguelike streamers), active modding community via Steam Workshop extending longevity.

### Example 3: Console AAA Action RPG
**Prompt:** Design OpenWorld RPG for PS5/Xbox Series X/PC with 150-person team, $50M budget, 4 years achieving 85 Metacritic and 5M sales $70.

**Expected Output:** Core loop (45 minutes): explore open world discovering quests and locations → engage action combat encounters (dodge/parry 0.3s windows, weapon combos) → loot gear upgrading character → spend skill points in talent tree → tackle harder content repeating cycle. Retention: Premium single-player less about daily retention, more about completion rate (target 70% finish 40-hour main story, 30% complete 100+ hour side content), high production values (motion-capture cinematics, orchestral score, 200K+ word narrative script) driving critical acclaim and word-of-mouth. Monetization: $70 base game, deluxe $90 (+early access 3 days, cosmetic armor, digital artbook), season pass $30 (3 DLC expansions 10 hours each over Year 1, $15 separately). Content: 40-hour main story, 60+ hours side quests (100 side quests, 20 dungeons, 30 world events), 100+ hour completionist (collectibles, achievements, NG+ mode), post-launch DLC 1 at month 6 (new region), DLC 2 at month 9 (new systems), DLC 3 at month 12 (story conclusion). Team: 50 programmers (Unreal Engine 5 open world), 60 artists (10K unique assets), 20 designers (systems + 500 quests), 15 QA, 5 producers. Timeline: year 1 pre-production (vertical slice 30-minute demo), year 2 production ramp (world blockout, systems implementation), year 3 full production (art, motion capture, VO recording), year 4 polish and optimization (bug fixing 5000+ issues, performance 60fps). Success: 5M sales Year 1 = $350M gross, 85+ Metacritic from reviewers, E3-equivalent announcement 2 years pre-launch, influencer early access 50 RPG creators, quarterly dev diaries building community trust.

---

## Cross-References

- [Game Design Framework](game-design-framework.md) - Comprehensive deep-dive into all game design aspects with detailed examples
- [Mobile Development](../Software-Development/mobile-development.md) - Platform optimization, F2P monetization, app store strategies
- [Architecture Design](../Software-Development/architecture-design.md) - Backend systems for multiplayer, matchmaking, live ops infrastructure
