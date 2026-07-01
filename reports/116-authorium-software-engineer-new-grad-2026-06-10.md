# Evaluation: Authorium — Software Engineer, New Grad

**Date:** 2026-06-10
**URL:** https://jobs.ashbyhq.com/Authorium/e9384068-af40-47b2-83cf-ec76fd8b7222?utm_source=Simplify&ref=Simplify
**Archetype:** Backend / Distributed Systems + Founding / Early-Stage Software Engineer
**Score:** 3.2/5
**Legitimacy:** High Confidence
**PDF:** output/116-authorium-software-engineer-new-grad-harry-nguyen-2026-06-10.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Founding-track new grad — ship complex SaaS features (versioning, approval workflows, permissions), participate in architecture decisions, AI-native workflow mandatory |
| Domain | GovTech SaaS — procurement, grants, and budgeting workflows for state/local governments; replaces legacy systems managing billions in public funds |
| Function | Build — full-stack features on a SaaS platform, ADR participation, quality engineering, AI-native tooling |
| Seniority | New grad — explicitly "not on a new grad track"; high ownership expectations from day one |
| Location | San Francisco — **hybrid Mon–Thu in office**; relocation from Atlanta required |
| Comp | **$102K–$138K + equity** + 100% employee health benefits + 401K + flexible PTO + home office stipend + commuter stipend |
| Company | Authorium — 43 people, 45% YoY growth, path to profitability Q4 2026; customers: California CDSS, CalPERS, EDD; Florida and Washington state agencies |
| TL;DR | Excellent new-grad archetype fit (production internship depth, systems thinking, high-agency, quality-obsessed, AI-native) and a genuinely interesting GovTech mission — but two hard concerns: (1) the entire comp range ($102K–$138K ceiling) sits below Harry's $140K minimum; (2) the backend stack is Rails (Ruby on Rails), which Harry has never used. Score 3.2 — apply if comp can be negotiated up or if Harry values mission and early equity over base salary. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|-------------|----------|
| 3+ terms of co-op/internship experience shipping to production | Google Chrome (SWE intern, shipped to 3B users), Develop for Good (SWE intern), TiMoto AI (FT SWE, primary engineer, ongoing) — 3 roles all shipping to production | ✅ Direct — exactly "Waterloo-style co-op depth" |
| Systems Thinker: data models, system boundaries, tradeoffs | TiMoto: gRPC inter-service layer, exactly-once semantics, circuit breaker pattern, PostgreSQL schema + Redis data layer; Chrome: C++ IPC + Protobuf schema design tradeoffs | ✅ Strong |
| High-Agency: fast-moving, no hand-holding | TiMoto: primary engineer on 3-person team, end-to-end ownership, no PM or design | ✅ Direct |
| Quality Obsessed: clean code, tests, readable PRs | Chrome: 95% test coverage discipline; design documents reviewed by senior Chrome engineers | ✅ Strong |
| AI-Native Workflow: Cursor + Claude, agentic testing | Daily Claude Code + Cursor + GitHub Copilot + Codex; TiMoto uses LLM-as-a-judge evaluation — agentic testing analog | ✅ Direct — "we expect new grads to push this frontier" |
| Security Minded: authorization models, defensive coding | TiMoto: JWT-based stateless auth (Develop for Good); gRPC authentication; ⚠️ no deep RBAC/permission system experience | ⚠️ Basic auth done, not permission-system depth |
| Modern Frontend — React/Next.js (nice-to-have) | Chrome: production TypeScript/React, observer-pattern state, 25K+ lines; TiMoto: React frontend | ✅ Bonus hit |
| Infrastructure curiosity: AWS, deployment pipelines (nice-to-have) | TiMoto: AWS ECS Fargate, Terraform IaC, GitHub Actions CI/CD, CloudWatch; Develop for Good: AWS BaaS, GitHub Actions | ✅ Bonus hit — strong infrastructure background |
| Early-stage startup experience (nice-to-have) | TiMoto: 3-person team, primary engineer, 0→1 product ownership | ✅ Bonus hit |
| Document/data pipeline work (nice-to-have) | TiMoto: batch + real-time ML data pipelines, PostgreSQL/Redis data layer | ✅ Bonus hit |
| **Ruby on Rails (nice-to-have)** | **None** — Harry's backend is Python (FastAPI/Django); no Rails experience | ❌ Key stack gap |
| Regulated industry: GovTech/FinTech/HealthTech (nice-to-have) | No regulated industry experience | ❌ Gap |
| SF-based / available Mon–Thu in-office | Atlanta-based; open to relocation; SF hybrid is feasible | ⚠️ Relocation needed |

**Gaps:**

1. **Comp ceiling below minimum (primary):** $102K–$138K — the entire band sits below Harry's $140K minimum ($2K below ceiling). This is the top constraint. Negotiating above band would be necessary, and at a 43-person startup the band is usually firm. Consider applying only if Harry is open to equity weighting or the mission/trajectory matters more than base.

2. **Ruby on Rails (high):** The JD lists Rails as a "nice-to-have" but at a company where it's likely the primary backend framework, "Rails exposure" is really "can you read and write Rails code." Harry uses Python/Django (same MVC paradigm) but has never written a Rails controller. The mental model transfers but there's a real onboarding cost.

3. **Permission system depth (medium):** The JD specifically calls out "permission models" and "authorization models as design constraint." Harry has JWT stateless auth and knows the basics, but building complex RBAC/permissions for government workflows is a different level. Authorium's platform includes approval workflows, grants management, and budget controls — permission correctness is safety-critical.

4. **F-1 at 43-person company (medium):** Small company H-1B sponsorship is expensive and uncertain. 43 people is below the threshold where most companies have a formalized H-1B process. Ask early; this may be a dealbreaker.

5. **Regulated industry (low):** GovTech is a new domain. Government procurement and budgeting workflows have specific compliance constraints (SOC 2, FISMA, etc.) Harry has no exposure to. Learnable, but it's a real context shift.

---

## C) Level and Strategy

**Level detected:** New grad / early-career — explicitly "new grad" role but with high autonomy expectations.

**Core pitch:**
> "I match your 'Waterloo co-op depth' requirement exactly — Google Chrome (shipped C++ and TypeScript/React to 3 billion users), Develop for Good (PostgreSQL optimization, AWS scale), and TiMoto (primary engineer on 3-person team, distributed ML systems, end-to-end ownership). I write Claude Code and Cursor daily and have built LLM-as-a-judge evaluation pipelines — your 'AI-native workflow' requirement is my daily reality, not a line item. My backend is Python/Django, not Rails, and I haven't worked in GovTech — but the production engineering depth and quality discipline are there."

**On comp:**
> "The posted range ($102K–$138K) is below my current floor of $140K. Is there flexibility at the top of the band, or does equity make up a meaningful portion of total comp at this stage?"

**On Rails:**
> "My backend production experience is Python (FastAPI, Django) — same MVC paradigm, similar ORM patterns, different syntax. I haven't shipped a Rails app, but I can read a Rails codebase and ramp in weeks, not months. I'd be transparent that this is a small gap."

**On GovTech domain:**
> "I haven't built for regulated government workflows specifically — no FISMA, no procurement compliance. The engineering challenges (permissions, data integrity, approval workflows) map to distributed systems problems I've solved before, but the domain context is new."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Authorium stated range | $102,000–$138,000 + equity |
| Harry target | $150K–$200K TC |
| Harry minimum | $140K |
| Assessment | **Entire band below Harry's minimum ($140K).** Ceiling is $2K below walk-away floor. Equity could bridge the gap — but at a 43-person startup at unknown valuation, equity value is highly speculative. Unless Authorium is growing toward a meaningful exit, the comp risk is real. |
| Equity | Pre-Series-B startup equity; 45% YoY growth and "path to profitability Q4 2026" are positive signals, but illiquid and uncertain |
| Benefits | 100% employee health premium, 401K, flexible PTO, home office + commuter stipends — solid startup benefits |

**Market note:** Authorium is a 43-person GovTech startup on a growth trajectory. If they raise a Series B and scale toward $100M+ ARR, early employee equity could be significant. But the base comp risk is real for Harry at this stage. The mission (government infrastructure, civic tech) is meaningful; the financial case requires believing in the equity story.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Experience order | Google Chrome first (cv.md default) | **TiMoto first** — founding-engineer + systems ownership is the primary signal | "High-agency," "systems thinker," "ship real features from day one" all map to TiMoto primary engineer role |
| 2 | TiMoto bullets | ML infra leads | Lead with system design + ownership: "designed gRPC inter-service architecture (exactly-once semantics, circuit breaker); owned data model (PostgreSQL + Redis); end-to-end product delivery" | "Systems thinker: data models, system boundaries, tradeoffs" is the #1 Must Have |
| 3 | Chrome bullets | C++ IPC leads | Emphasize quality signals: "95% test coverage, design documents, code reviews with senior Chrome engineers; TypeScript/React reusable components" | "Quality Obsessed" is a must-have; 95% coverage at Chrome is the strongest signal available |
| 4 | AI-Native note | AI Dev Tools row (last) | Keep last but make AI-native identity visible in TiMoto bullets: "uses Claude Code + Cursor daily; LLM-as-a-judge evaluation = agentic testing analog" | Authorium explicitly wants new grads who will "push the AI-native frontier" — this is a differentiator |
| 5 | Skills | Distributed Systems leads | Backend + Systems first (gRPC, exactly-once, circuit breakers, PostgreSQL); then Cloud/Infra (AWS, Terraform, CI/CD); then Languages (Python, TypeScript prominent); then AI Dev Tools last | Permissions, workflows, data integrity — backend systems is the core |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Internship depth + production shipping | TiMoto primary engineer | 3-person team building production AI product, no playbook | Primary engineer — own backend, infra, and ML serving end-to-end | Designed gRPC services, PostgreSQL schema, AWS ECS Fargate, Terraform IaC; debugged production deadlock; maintained 99.9% uptime | Production AI product; resolved production incidents; shipped end-to-end | The difference between internship depth and junior depth is owning what breaks at 2am. At TiMoto I carry the pager — that changed how I think about every architectural decision |
| 2 | Systems Thinker: data models, system boundaries, tradeoffs | TiMoto gRPC + Protobuf choice | Production ML system needed reliable IPC between services | Design inter-service communication with explicit schema contract | Chose gRPC + Protocol Buffers over REST; documented schema evolution strategy; implemented exactly-once semantics | Zero message loss; schema backward compatibility maintained | System boundaries are contracts. Getting the contract right before you implement means you can evolve both sides independently. I'd bring this same "contract-first" thinking to Authorium's permission and workflow models |
| 3 | Quality Obsessed: tests, clean code, reviews | Chrome 95% test coverage | Chromium codebase with strict quality bar for shipping to 3B users | Write production-grade TypeScript/React with comprehensive test coverage | Event-driven architecture, reusable components, design documents reviewed by senior Chrome engineers; 95% coverage maintained | 68% faster feature delivery; zero production regressions | High test coverage isn't bureaucracy — it's the thing that lets you refactor without fear. I came out of Chrome with that discipline ingrained; it's how I write code everywhere now |
| 4 | AI-Native Workflow: Cursor + Claude | TiMoto daily AI tooling + LLM-as-a-judge | Production AI product needed reliable LLM outputs + fast feature development | Build AI evaluation pipeline + use AI tools as force multiplier | LLM-as-a-judge evaluation catches regressions automatically; Claude Code + Cursor handle boilerplate and let me focus on complex design | Measurable velocity increase; eval pipeline catches issues before production | The Authorium JD says "agentic testing and automated reviews" — I've built exactly this (LLM-as-a-judge is agentic testing for AI outputs). The same pattern applies to automated code review and test generation. This is where I'd want to push the frontier |
| 5 | High-Agency + ADR participation | TiMoto architectural decisions | No PM, no design, no senior review — had to make architectural calls solo | Own the architecture for a production distributed system | Chose vLLM over naive inference (memory + throughput tradeoffs documented); chose ECS Fargate vs EC2 (operational overhead vs flexibility tradeoff); documented decisions for team | Architectural decisions that held up in production | Architecture decision records are useful because they force you to write down what you knew when you decided. I already make these decisions — I'd just be formalizing what I do at TiMoto |

**Recommended framing:** Lead with the "Waterloo co-op depth" match (3 production roles), quality obsession (95% Chrome coverage), and AI-native workflow (Cursor/Claude daily + LLM-as-a-judge eval). Be upfront about the Rails gap and comp gap early in the conversation.

**Red-flag questions:**
- *"Do you know Ruby on Rails?"* → "Not yet. My backend is Python/Django — same MVC paradigm, same ORM patterns, different syntax. I've never shipped a Rails app, but I've read enough Ruby to follow idiomatic code and I ramp on new frameworks fast. I'd be transparent that this is a small gap I'd close in the first couple of weeks."
- *"The comp range is $102K–$138K — your floor is higher."* → "You're right — my floor is $140K base. Is there flexibility at the top of the range, or does the equity component meaningfully bridge that gap? I'm interested in the mission and the trajectory, so I'm willing to have the conversation."
- *"No GovTech experience?"* → "Correct — I haven't worked in regulated government workflows. The engineering challenges (complex permission models, data integrity, approval workflows) are problems I've tackled in distributed systems, just in a different domain. I'd need to ramp on GovTech-specific constraints like FISMA and SOC 2, but the core engineering instincts transfer."
- *"Work authorization?"* → "F-1 — OPT at graduation (May 2027), H-1B sponsorship long-term. At a 43-person company I'd want to understand early whether H-1B sponsorship is something Authorium has done before. Can you share the process?"

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active ("Apply for this Job") on Ashby | Positive |
| Comp disclosed | $102K–$138K + equity explicitly listed | Positive |
| JD specificity | Named customers (CDSS, CalPERS, EDD), specific team size (43 people), specific growth rate (45% YoY), specific products (procurement, grants, budgeting) | Positive |
| Company status | Authorium — verifiable GovTech startup; California agencies are public contracts; "path to profitability Q4 2026" specific claim | Positive |
| "War room" framing | Specific mention of SF office, ADRs, architectural challenges — unusually specific for a ghost posting | Positive |
| Sourced via Simplify | Simplify typically aggregates verified active postings | Positive |

---

## Keywords extracted

New grad, software engineer, GovTech, SaaS, procurement, grants, budgeting, government, Ruby on Rails, React, Next.js, TypeScript, Python, PostgreSQL, AWS, Terraform, CI/CD, systems thinking, authorization, permissions, approval workflows, versioning, ADR, AI-native, Cursor, Claude, agentic testing, San Francisco, hybrid, early-stage startup

---

## Machine Summary

```yaml
company: Authorium
role: "Software Engineer, New Grad"
date: 2026-06-10
url: https://jobs.ashbyhq.com/Authorium/e9384068-af40-47b2-83cf-ec76fd8b7222?utm_source=Simplify&ref=Simplify
score: 3.2
archetype: "Backend / Distributed Systems + Founding / Early-Stage SWE"
location: "San Francisco — hybrid Mon-Thu; relocation from Atlanta required"
comp_range: "$102K–$138K base — ENTIRE RANGE BELOW Harry's $140K minimum; equity upside speculative at this stage"
visa_risk: "F-1 — 43-person startup; H-1B history unknown; expensive for small companies; ask early — potential dealbreaker"
legitimacy: High Confidence
recommendation: "Apply cautiously (3.2/5) — strong new-grad profile fit (3 production roles, quality obsession, AI-native workflow, systems thinking, high-agency all check). But comp is below minimum ($138K ceiling vs $140K floor), the backend stack is Rails (Harry has Python/Django), F-1 at a 43-person company is risky, and GovTech domain is new. Ask about comp flexibility and H-1B in the first recruiter call. Only proceed if they can meet $140K+ or if Harry values equity/mission over base. Below 3.5 conditional-apply bar."
```
