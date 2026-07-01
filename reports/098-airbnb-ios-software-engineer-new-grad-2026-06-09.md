# Evaluation: Airbnb — iOS Software Engineer, New Grad

**Date:** 2026-06-09
**URL:** https://careers.airbnb.com/positions/7859317/?gh_jid=7859317
**Archetype:** iOS / Mobile Engineer (not in Harry's target archetypes)
**Score:** 2.0/5
**Legitimacy:** High Confidence
**PDF:** ❌ (score below 3.0 threshold)

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | iOS / Mobile Engineer — Quality Reputation team (customer-facing product; trip quality signals, host/guest reputation, proactive enforcement) |
| Domain | Consumer mobile product — iOS app used by Airbnb's global host and guest community |
| Function | Build — iOS features, bug fixes, UI components; AI-assisted tooling mention (Claude Code) as workflow accelerator |
| Seniority | New Grad (explicitly: "less than 1 year of full-time professional experience"); BS or MS |
| Location | San Francisco, CA or Seattle, WA — 3 days/week hybrid; domestic relocation support provided |
| Team | Quality Reputation — collaborative with design, product, data science, legal, marketing |
| Comp | $128,000–$142,000 USD + bonus + equity + Employee Travel Credits |
| TL;DR | Airbnb iOS New Grad — Swift + UIKit/SwiftUI required. Harry's stack is Python, C++, TypeScript (web), gRPC, AWS. No iOS experience in CV. Domain mismatch. Score 2.0/5 — SKIP. **Do not apply without first learning iOS development.** |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| Proficiency in Swift | Not in CV — no Swift experience listed | ❌ Hard gap |
| SwiftUI or UIKit for iOS applications | Not in CV — Chrome TypeScript/React is web browser UI, not iOS mobile | ❌ Hard gap |
| iOS development concepts (networking, caching, client storage, accessibility, async) | REST APIs ✅; async patterns (gRPC, event-driven) ✅; but iOS-specific patterns (URLSession, NSCache, UserDefaults, MainActor) = absent | ⚠️ Adjacent but not iOS-specific |
| Strong CS fundamentals (data structures, algorithms, design patterns, systems) | Georgia State CS GPA 3.75; Distributed Systems, OS, DB, Networks coursework; lock-free trie, gRPC, Raft/Paxos | ✅ Strong |
| REST APIs; GraphQL a plus | TiMoto: FastAPI/Django REST; Chrome: Protocol Buffers IPC | ✅ REST direct; GraphQL absent |
| Less than 1 year full-time professional experience | Harry is new grad (May 2027); current role is while still a student | ✅ Direct |
| Leadership/mentoring bonus points | N/A — relevant experience not emphasized for this archetype | Neutral |
| Work authorization (H-1B) | F-1 — Airbnb is a large public company; sponsorship expected but not confirmed in this evaluation | ⚠️ Expected but unverified |

**Gaps:**

1. **Swift — hard blocker.** The primary technical requirement is Swift proficiency. Harry does not have Swift in his skills, experience, or projects. TypeScript/React for Chrome's web UI is not equivalent — iOS development is a fundamentally different ecosystem (UIKit, SwiftUI, Grand Central Dispatch, memory management in Swift, Apple's Human Interface Guidelines). This is not a stretch gap; it is an absent domain.

2. **iOS development ecosystem — hard blocker.** The role requires foundational iOS concepts: URLSession networking, NSCache/NSUserDefaults client storage, accessibility APIs, async/await in Swift, UIKit view lifecycle, or SwiftUI state management. Harry's async experience is gRPC/event-driven on backend — architecturally different from iOS async patterns.

3. **Domain — no path.** Harry's target archetypes (Backend/Distributed Systems, ML/AI Infrastructure, SRE, Platform/Cloud) have zero overlap with iOS mobile engineering as a career path. Applying here would not progress Harry toward his North Star. The Quality Reputation team builds iOS product features, not infrastructure.

4. **Comp below minimum.** $128K–$142K range, with floor $128K — $12K below Harry's $140K walk-away. Even the ceiling ($142K) is below Harry's $150K target.

5. **Relocation required (SF or Seattle).** Atlanta-based; Airbnb provides relocation support, but 3-days/week hybrid requires physical move. Not a blocker on its own, but compound with domain and comp gaps.

---

## C) Level and Strategy

**Level detected:** New Grad explicitly — this is appropriate for Harry's profile chronologically. Airbnb explicitly designed this role for "less than 1 year full-time experience."

**Why the score is 2.0/5 and not higher despite good CS fundamentals:**
The Airbnb iOS New Grad role could be a good fit for a CS grad with iOS coursework or personal iOS projects. Harry has the CS fundamentals but zero iOS exposure. A recruiter screening for Swift proficiency would pass immediately. "Strong CS fundamentals" only gets you to a phone screen — the technical bar is iOS-specific.

**If Harry wanted to change direction toward iOS (not recommended):**
- Minimum viable: Build 1-2 personal iOS apps in Swift (SwiftUI preferred) + publish to App Store or GitHub. 3–4 months of evenings.
- The archetype pivot would require abandoning his primary ML infra / backend pitch, which has stronger momentum.

**Recommendation: SKIP.** Harry's backend/ML infra pipeline has multiple live high-fit opportunities (#093 ElevenLabs 4.0, #095 Brellium 4.0, #097 Baseten 4.5). Investing time in this application at 2.0/5 match is a poor use of Harry's application energy.

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Airbnb stated range | $128,000–$142,000 + bonus + equity + travel credits |
| Harry target | $150K–$200K |
| Harry minimum | $140K |
| Airbnb new grad SWE (Levels.fyi 2026) | iOS new grad at Airbnb: ~$135K–$180K TC including equity and bonus |
| Gap | Base ceiling ($142K) is still below Harry's TC target; equity would need to bridge significantly |

Comp is the weakest in the current pipeline. The $128K floor is $12K below walk-away. Even if equity brings TC above target, the base is a yellow flag for a public company of Airbnb's size.

Note: Airbnb's comp for new grads has compressed post-2022 layoffs. The $128K–$142K range reflects this tighter band for non-senior mobile roles.

---

## E) Customization Plan

**N/A — domain mismatch makes CV customization irrelevant.** The required skill (Swift/iOS) is absent from Harry's profile. No amount of CV optimization addresses the lack of Swift experience.

If Harry were to apply against advice:
| # | Section | Proposed | Why |
|---|---------|----------|-----|
| 1 | Chrome TypeScript/React | Emphasize "mobile-adjacent UI" angle | Closest existing signal to iOS product engineering |
| 2 | TiMoto LangChain/LLM integration | Mention AI-assisted development (JD mentions Claude Code) | JD explicitly calls out AI tooling; Harry uses Claude Code |
| 3 | Skills | Add Swift if Harry has any exposure | Only honest if true |

These are weak pivots that would not compensate for zero iOS experience in a recruiter screen.

---

## F) Interview Plan

**N/A for this role** — the interview would include iOS-specific technical screening (UIKit layout, Swift concurrency model, Core Data, memory management) where Harry has no preparation path.

If Harry were to proceed (not recommended):

| # | JD Requirement | Closest Story | Honest Gap |
|---|---|---|---|
| 1 | Swift + iOS app development | No equivalent story | Hard gap — no path to spin |
| 2 | CS fundamentals | Chrome lock-free trie, gRPC distributed systems | Strong signals for CS depth, but iOS interview asks different questions |
| 3 | REST API familiarity | TiMoto FastAPI/Django, Develop for Good BaaS | Transferable networking concepts |
| 4 | Async programming | gRPC async, TiMoto event-driven | Backend async ≠ Swift async/await / MainActor |

**Red-flag question to expect:**
- *"What iOS apps have you built?"* → No honest answer with current experience. Fabrication is not an option.

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active ("Apply Now") on careers.airbnb.com via Greenhouse | Positive |
| Comp disclosed | $128K–$142K USD base explicitly stated (California pay transparency law) | Positive |
| Company status | Airbnb — NYSE: ABNB; $70B+ market cap; global consumer platform; 5M+ hosts | Positive |
| JD specificity | Named team (Quality Reputation), named technologies (Swift, SwiftUI, UIKit), specific day-in-life activities, 3-day hybrid, relocation support | Positive |
| New Grad positioning | Explicit "less than 1 year" requirement signals real junior headcount, not vague pipeline hiring | Positive |
| AI tooling mention | "Claude Code or similar" referenced as workflow tool — signal of forward-looking team with real AI tooling adoption | Positive |
| Location specificity | SF or Seattle only (Greenhouse post) — not "anywhere" ghost job behavior | Positive |

---

## Keywords extracted

iOS, Swift, SwiftUI, UIKit, mobile, networking, caching, client storage, accessibility, asynchronous programming, REST APIs, GraphQL, Quality Reputation, new grad, San Francisco, Seattle, hybrid, Airbnb, consumer mobile, AI-assisted development

---

## Machine Summary

```yaml
company: Airbnb
role: iOS Software Engineer, New Grad
date: 2026-06-09
url: https://careers.airbnb.com/positions/7859317/?gh_jid=7859317
score: 2.0
archetype: iOS / Mobile Engineer (not in Harry's target archetypes)
location: SF or Seattle — 3-day hybrid; relocation support provided
comp_range: "$128K–$142K base + bonus + equity; below $140K minimum"
visa_risk: "F-1 — Airbnb large public company, sponsorship expected but unverified in this evaluation"
legitimacy: High Confidence
recommendation: "SKIP — hard domain mismatch. Swift/UIKit/SwiftUI required; not in Harry's skills or experience. Comp below minimum. iOS is not on Harry's archetype path. Harry has stronger live opportunities (#097 Baseten 4.5/5, #093 ElevenLabs 4.0/5, #095 Brellium 4.0/5) that align with his backend/ML infra track."
```
