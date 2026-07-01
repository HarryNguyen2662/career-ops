# Evaluation: Nash — Full Stack Engineer

**Date:** 2026-06-06
**URL:** https://jobs.ashbyhq.com/Nash/9024ea9d-648a-4c92-8678-01b2b5357d1e
**Archetype:** Full-Stack Engineer (product-facing portal)
**Score:** 3.2/5
**Legitimacy:** Proceed with Caution
**PDF:** output/073-nash-full-stack-engineer-harry-nguyen-2026-06-06.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Full-Stack Engineer — product portal (React/TS + Python) |
| Domain | Logistics tech / Autonomic Logistics OS |
| Function | Build — operator-facing portal, React frontend + Python services |
| Seniority | Mid (4+ years required, 5+ preferred) |
| Remote | Hybrid — SF office preferred |
| Company size | ~50-100 eng est. (YC + a16z backed, founded 2021) |
| Comp | Not disclosed — "competitive compensation and equity" |
| TL;DR | Build the portal operators use to run real-time logistics for Walmart, 7-Eleven, Woolworths — React/TS frontend + Python backend, full ownership. Harry's stack matches technically but Full-Stack is adjacent archetype and 4+ year requirement is a real gap. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| React / TypeScript (required) | Google Chrome: 25K+ lines Chromium React/TS, 95% coverage, 68% delivery acceleration | ✅ Strong |
| Python + backend frameworks | TiMoto: Django/FastAPI ML serving + REST APIs | ✅ Strong |
| PostgreSQL / relational DB | Develop for Good: N+1 fix → sub-100ms for 10K+ records | ✅ |
| Cloud platforms (AWS/GCP) | TiMoto: ECS Fargate, Terraform, multi-AZ | ✅ Strong |
| Production systems ownership | TiMoto: 99.9% uptime, sub-50ms p99, primary engineer 3-person team | ✅ |
| RESTful APIs | TiMoto: FastAPI + gRPC inter-service layer | ✅ |
| Full-stack end-to-end delivery | TiMoto: backend + infra + ML serving; Chrome: React + C++ | ✅ |
| Microservices / SOA | TiMoto: gRPC inter-service + ECS services | ✅ |
| 4+ years experience (required) | Harry has ~1.5 years total | ❌ Gap |
| GraphQL | Not in CV | ❌ Gap |
| Flask / SQLAlchemy (bonus) | Django/FastAPI instead — adjacent Python frameworks | ⚠️ Partial |
| Real-time / integration-heavy systems | gRPC async + concurrent batching — adjacent but not logistics integration | ⚠️ Partial |
| Bay Area presence | Atlanta-based; open to relocation | ⚠️ Risk |

**Gaps:**
1. **Experience requirement** — 4+ years required; Harry has ~1.5 years. Mitigation: TiMoto is primary engineer ownership on a 3-person team, which represents mid-level scope; startup stage means this requirement is likely calibrated flexibly.
2. **GraphQL** — Not in CV. REST APIs are strong. Mitigation: mention "familiar with GraphQL patterns, have worked extensively with REST" — easy to learn on the job.
3. **F-1 / H-1B at startup** — Nash is small and new; no public LCA filings found. Mitigation: YC/a16z-backed startup at this stage often sponsors; ask recruiter early.

---

## C) Level and Strategy

**Level detected:** Mid-level SWE (4+ years = ~L3/L4 in FAANG terms). Harry enters at entry/junior band.

**Sell startup ownership as proxy for mid-level scope:**
> "At TiMoto I was the primary engineer for the entire backend: gRPC inter-service layer, Django REST APIs, AWS infrastructure, and ML serving. It's a 3-person team, so I shipped full-stack features end to end — from React/TS frontend decisions to Python APIs to deployment. The scope of that ownership is closer to a mid-level engineer's responsibilities than a typical intern or new grad."

**React/TS angle:**
> "I shipped 25K+ lines of Chromium React/TypeScript to 3B+ users at Google. I understand component-driven architecture, observer patterns for state propagation, and what it costs to ship a broken UI to millions of users."

**If pushed on years:**
> "I'm a 2027 new grad with production depth that most 4-year engineers haven't touched — Chrome stable channel, gRPC deadlocks in prod, TiMoto from zero to 99.9% uptime. I calibrate on impact, not calendar time."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Nash stated comp | Not disclosed — "competitive + equity" |
| SF full-stack SWE mid-level (est.) | $150K–$200K base (Levels.fyi SF mid-band) |
| YC/a16z startup equity | Meaningful early-stage options; liquidity uncertain |
| Harry target | $150K–$200K |
| Harry minimum | $140K |

**Risk:** Startup comp at this stage may anchor below $140K base with equity offset. Nash does not disclose salary. Comp risk is real — press during recruiter screen before investing in prep.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet order | gRPC deadlock first | Lead with "Led backend, cloud infra, ML serving for 3-person team" | Full ownership story is the core sell for full-stack role |
| 2 | Chrome bullet order | C++ IPC leads | Lead with TypeScript/React observer pattern (68% delivery) | React/TS is the primary frontend requirement |
| 3 | Skills: Languages row | C++ first | Python, TypeScript first | Python + TypeScript are the two required languages |
| 4 | Skills row order | Distributed Systems leads | Languages leads, then Frameworks & Databases second | Full-stack role cares about Python/TS + Django/FastAPI/React/PostgreSQL |
| 5 | TiMoto vLLM bullet | High prominence | Move to 4th (de-emphasize ML) | Portal role is product-facing, not ML infra |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Full-stack end-to-end ownership | TiMoto full product | 3-person team, no senior eng to offload to | Ship backend + infra + ML serving in production | Designed gRPC + Django + ECS as unified system | 99.9% uptime, sub-50ms p99, $40-60/mo cost | Small team forces systems thinking — you own the whole thing, not just your ticket |
| 2 | React/TS production quality | Chrome observer pattern | Chrome settings UI had state scattered across 25K+ lines | Decouple state from components with minimal regression | Observer pattern, 95% coverage, Chrome infra code review | 68% feature delivery acceleration | UI architecture decisions compound — the right pattern pays dividends on every future feature |
| 3 | PostgreSQL / backend perf | Develop for Good N+1 | 3s+ response times under load on large datasets | Fix without schema migration or downtime | Diagnosed N+1 with query logs; redesigned with PostgreSQL indexing | Sub-100ms for 10,000+ records | Profile before adding infra — most database problems are query problems |
| 4 | Production debugging | gRPC deadlock root-cause | Production deadlock under concurrent gRPC evaluation calls | Find root cause without senior help | Traced shared resource acquisition via logging; redesigned call sequencing | 100% success rate restored | Concurrent code requires explicit ownership maps; instrument from day one |
| 5 | Cloud deployment + reliability | TiMoto ECS + circuit breaker | Single-AZ deployment with no observability | Zero-downtime multi-region with auto-rollback | Multi-AZ ECS Fargate + CloudWatch + circuit breaker + Terraform | 99.9% uptime, 44% cost reduction | Circuit breakers and health checks are not over-engineering — they're the difference between alerting and paging |

**Recommended case study:** TiMoto full-stack ownership — "I built the backend, infra, and ML serving as the primary engineer. Here's the stack, the decisions I made (vLLM vs naive inference, gRPC vs REST for internal calls, Fargate vs EC2), and what I'd do differently for a portal at Nash's scale."

**Red-flag questions:**
- *"4+ years required — you have 1.5?"* → "I've run production systems end-to-end as the primary engineer: gRPC deadlocks, AWS multi-AZ, 99.9% uptime. The scope at TiMoto is mid-level work, not intern work. Calendar time is not the constraint."
- *"Visa sponsorship?"* → "F-1 OPT from May 2027. Will need H-1B sponsorship. YC/a16z-backed companies at Nash's stage typically have sponsorship options — can you confirm your policy?"
- *"GraphQL experience?"* → "Haven't used GraphQL in production; I've built extensively with REST + gRPC. GraphQL is a query layer I can ramp on quickly — it's a matter of days with the right documentation."

---

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active on Ashby | Positive |
| JD specificity | Named tech (React, TypeScript, Python, GraphQL, PostgreSQL, Flask/SQLAlchemy), real customers named, role scope well defined | Positive |
| Company status | YC + a16z backed, real enterprise customers (Walmart, 7-Eleven, Woolworths, Coles) | Positive |
| Posting age | Not visible on Ashby | Neutral |
| Comp disclosure | Not disclosed | Concerning |
| H-1B track record | No public LCA filings found — company too small/new | Concerning |
| Prior Nash entries | No prior Nash in scan-history | Neutral |

**Context:** Nash is an early-stage startup (~2021). The lack of LCA history is expected, not necessarily a negative signal. Sponsorship depends on willingness, not track record. The posting quality is strong — specific stack, real customers named, clear ownership scope. The caution is around comp opacity and unverified H-1B policy.

---

## Keywords extracted

React, TypeScript, Python, Full Stack, GraphQL, RESTful APIs, PostgreSQL, NoSQL, Redis, microservices, AWS, GCP, CI/CD, logistics, real-time systems, Flask, SQLAlchemy, WebSockets, component-driven architecture, production debugging, observability, system design, startup, end-to-end ownership

---

## Machine Summary

```yaml
company: Nash
role: Full Stack Engineer
date: 2026-06-06
url: https://jobs.ashbyhq.com/Nash/9024ea9d-648a-4c92-8678-01b2b5357d1e
score: 3.2
archetype: Full-Stack Engineer (product portal)
location: San Francisco, CA (hybrid)
comp_range: "undisclosed; est. $150K-$190K base for target level"
visa_risk: "F-1 — H-1B unverified (no public LCA history; small startup); ask recruiter early"
legitimacy: Proceed with Caution
recommendation: "Conditional apply — strong React/TS + Python match; experience gap manageable given TiMoto ownership depth; verify H-1B policy and comp before heavy investment"
```
