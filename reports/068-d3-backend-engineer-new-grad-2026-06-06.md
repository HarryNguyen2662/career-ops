# Evaluation: D3 — Backend Engineer, New Grad

**Date:** 2026-06-06
**URL:** https://job-boards.greenhouse.io/embed/job_app?for=d3&token=4915295008
**Archetype:** Founding / Early-Stage Software Engineer + Backend / Distributed Systems Engineer
**Score:** 3.4/5
**Legitimacy:** Proceed with Caution
**PDF:** output/cv-harry-d3-2026-06-06.pdf ✅

---

## A) Role Summary

| Field | Detail |
|---|---|
| **Archetype** | Founding / Early-Stage SWE + Backend |
| **Domain** | Web2/Web3 domain registrar + blockchain (DomainFi) |
| **Function** | Build backend services, payment integrations, blockchain connectors |
| **Seniority** | Entry-level / New Grad (0–2 YOE) |
| **Location** | Hybrid — Los Angeles, CA |
| **Team size** | ~40 employees (early-stage) |
| **TL;DR** | Early-stage crypto startup building a blockchain for domain names; solid backend fit but Web3 focus diverges from distributed systems / ML infra trajectory; comp likely below walk-away. |

---

## B) Match with CV

| JD Requirement | Harry's Match | CV Source |
|---|---|---|
| Backend development (0–2 YOE) | ✅ Strong — TiMoto (SWE, Sep 2025–Present), Google Chrome intern, Develop for Good | cv.md — all experience |
| Python / Node.js / JS backend | ✅ Django, FastAPI, Node.js | cv.md Skills |
| PostgreSQL / MySQL | ✅ N+1 fix → sub-100ms on 10K+ records | cv.md — Develop for Good |
| Git / collaborative dev | ✅ Chromium 25K+ lines, upstream Pulumi contributions | cv.md — Google + Pulumi |
| CS degree | ✅ Georgia State CS, GPA 3.75, May 2027 | cv.md Education |
| AWS / GCP exposure (nice-to-have) | ✅ AWS ECS Fargate, Terraform, multi-AZ | cv.md — TiMoto |
| Distributed systems coursework / projects (nice-to-have) | ✅ Distributed Systems coursework + TiMoto production + Pulumi Raft/Paxos | cv.md |
| Web3 / blockchain interest (nice-to-have) | ⚠️ No direct blockchain work; Pulumi distributed state is adjacent | cv.md — Pulumi |
| NestJS / GraphQL (nice-to-have) | ❌ Gap — not listed | — |
| Payment integrations | ⚠️ Partial — Develop for Good AWS BaaS; no explicit payments work | — |

**Gaps:**
1. **No blockchain / Web3 experience** — Nice-to-have only ("not required — you'll learn here"). Mitigate with Pulumi distributed state + willingness-to-learn framing.
2. **NestJS / GraphQL** — Minor. Skip in application.
3. **Payment integrations** — Lean into AWS BaaS stateless design; don't over-claim.

**F-1 note:** JD silent on sponsorship. Clarify early — do not skip application for this reason.

---

## C) Level and Strategy

**Level:** Entry-level New Grad — matches Harry's 2027 timeline perfectly.

**Sell strong without lying:**
- Lead with TiMoto "primary engineer, 3-person team" — maps to D3's zero-to-one framing.
- Google Chrome production scale (3B+ users) establishes quality bar.
- gRPC + Terraform + AWS SLOs signals no hand-holding needed.

**If downleveled:** Already entry-level. Accept if comp is fair. Negotiate 6-month review with explicit ownership of a backend service.

---

## D) Comp and Demand

No published salary band. D3 is ~40 people, Series A ($25M, Jan 2025, Paradigm + Coinbase Ventures).

| Source | Data |
|---|---|
| Glassdoor — Backend Engineer US avg | $175K TC (25th–75th: $136K–$230K) |
| Levels.fyi — SWE Los Angeles avg | $175K TC (range $126K–$240K) |
| D3 Principal Blockchain Engineer (web3.career) | $122K–$150K base (senior) |
| Early-stage crypto startup new grad estimate | $110K–$140K base + equity |

**Assessment:** Likely at or below Harry's $140K walk-away. Equity is speculative (crypto/Web3 category, no Series B visibility 17 months post-Series A). Ask for total package on first recruiter call.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---|---|---|---|
| 1 | Summary | Distributed systems / ML infra | Add "full-stack backend ownership and 0→1 delivery" | D3 values breadth + early-stage ownership |
| 2 | TiMoto bullet 1 | "distributed production systems" | Add "shipped from zero to production" | Aligns to D3 zero-to-one framing |
| 3 | Develop for Good | AWS BaaS + N+1 fix | Emphasize stateless JWT scale — payment-adjacent | Bridges to D3 payment integration ask |
| 4 | Pulumi | IaC + Raft/Paxos | Highlight "distributed state synchronization" | Covers Web3/blockchain nice-to-have softly |
| 5 | Skills | Current order | Move Node.js, Python, PostgreSQL higher | ATS match for D3 stack |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Backend services design | TiMoto gRPC layer | Needed inter-service RPC with strict SLOs | Owned design on 3-person team | Designed gRPC protocol + traced deadlock, redesigned call sequencing | sub-50ms p99, 100% eval success rate | Deadlocks come from circular resource acquisition — trace call graphs early |
| 2 | Payment / transaction systems | Develop for Good AWS BaaS | Stateless auth for 500+ concurrent users | Solo backend intern | JWT over session auth, AWS auto-scaling | 500+ concurrent, 90% deploy time cut | JWT simplicity makes horizontal scale trivial |
| 3 | Clean, testable code | Google Chrome IPC | Chrome stable requires 95% coverage | Shipping C++ IPC to 3B users | Wrote IPC with Protobuf, collaborated with senior infra team | Zero regressions to stable | 95% coverage at Chrome scale prevents billions of broken users |
| 4 | Debug existing codebases | Develop for Good N+1 | 3s+ response on large datasets | Fix under time pressure | Diagnosed N+1, redesigned with PostgreSQL indexing | sub-100ms for 10K+ records | Profile before optimizing — N+1 was invisible without query logs |
| 5 | Cross-team collaboration | Google Chrome React | UI state propagation bottleneck | Deliver across 25K+ lines of Chromium | Event-driven observer pattern decoupling UI state | 68% faster feature delivery, 95% coverage | Decoupling state makes the entire codebase move faster |
| 6 | Web3 / blockchain learning | Pulumi open source | Understand distributed consensus in production | Study Raft/Paxos in Pulumi state sync | Analyzed linearizability under concurrent ops and partial failures | Go CLI contributions accepted | Production code teaches consensus better than papers alone |

**Case study:** TiMoto AI — "I owned backend, infra, and ML serving for a live product. Here's what I built, tradeoffs I made, and what's running in production today." Demo timoto.ai.

**Red-flag Qs:**
- *"Web3 experience?"* → "No production blockchain yet, but studied distributed consensus in Pulumi's state layer (Raft/Paxos). I learn fast in production — TiMoto went from zero to live serving stack quickly."
- *"Work authorization?"* → "F-1, OPT eligible. Will need H-1B long-term — happy to discuss sponsorship policy."
- *"Open to hybrid in LA?"* → "Yes, open to hybrid or onsite in LA. Available to relocate."

---

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|---|---|---|
| Apply button | Active ✅ | Positive |
| JD freshness | No date visible; embed is live and responsive | Neutral |
| Description specificity | Names NestJS, GraphQL, blockchain connectors, payments — reasonably specific | Positive |
| Layoffs / freeze | None found; actively hiring ~40 roles | Positive |
| Reposting | Not in scan-history.tsv | Positive |
| Comp transparency | No salary band | Neutral |
| Role-company fit | New grad backend consistent with early-stage growth | Positive |
| Startup risk | Crypto/Web3 niche; Series A Jan 2025 (17 months); no Series B announced | Concerning |

**Context:** Posting appears legitimate. Caution is about startup risk (crypto market volatility, runway visibility) — not ghost job signals.

---

## Keywords Extracted

backend, Node.js, Python, PostgreSQL, MySQL, distributed systems, blockchain, Web3, DeFi, payment integrations, NestJS, GraphQL, cloud, AWS, REST API, Git, code review, domain registrar, marketplace, crypto payments, entry-level, new grad

---

## Machine Summary

```yaml
company: D3
role: Backend Engineer - New Grad
score: 3.4
archetype: Founding/Early-Stage SWE + Backend
location: Los Angeles, CA (Hybrid)
seniority: New Grad
sponsorship: unconfirmed
recommendation: skip
legitimacy: Proceed with Caution
date: 2026-06-06
```
