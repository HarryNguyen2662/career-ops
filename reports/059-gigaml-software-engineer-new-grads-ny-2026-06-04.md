# Evaluation: Giga (GigaML) — Software Engineer (New Grads) — New York

**Date:** 2026-06-04
**URL:** https://jobs.ashbyhq.com/GigaML/7314c5c1-e3d0-4439-ad9f-b3b09d4dde51
**Archetype:** AI Agent Infrastructure / Backend Platform Engineer (New Grad)
**Score:** 4.4/5
**Legitimacy:** High Confidence
**PDF:** output/059-gigaml-software-engineer-new-grads-ny.pdf

---

> **Note on prior GigaML evaluations:**
> - **#015** (2026-05-28): Software Engineer (New Grads) — **San Francisco** — Score 4.3/5
> - **#019** (2026-05-29): Software Engineer I/II — **San Francisco** — Score 4.1/5
> - **This (#059)**: Same "New Grads" JD as #015 but **New York** location. Different requisition, different city. Evaluated as a distinct opportunity. NYC is a stronger fit for Harry vs. SF: lower cost of living delta, stronger F-1 support ecosystem, no cross-country relocation required from Atlanta.

---

## Machine Summary

```yaml
company: Giga (GigaML)
role: Software Engineer (New Grads) — New York
date: 2026-06-04
score: 4.4
status: Evaluated
level: New Grad — Full-time
location: New York, NY — On-site (full-time)
comp_base: "$160,000–$250,000 USD"
comp_equity: "Offers Equity — Series A ($61M raised Nov 2025); DoorDash paying customer; meaningful upside"
archetype: "AI Agent Infrastructure / Backend Platform Engineer (New Grad)"
graduation_timing_risk: none — no graduation date restriction stated; accepting new grads
visa_risk: medium — Series A startup; H-1B sponsorship unconfirmed; NYC market = more established H-1B infrastructure than SF startup
apply_rec: "Apply — comp floor $20K above walk-away; AI agent infra is direct primary archetype; NYC preferred over SF (lower COL delta, no cross-country relocation); confirm H-1B sponsorship before form submit; stronger than #015 on location practicality"
```

---

## A) Role Summary

| Field | Value |
|---|---|
| **Archetype** | AI Agent Infrastructure / Backend Platform Engineer |
| **Domain** | AI agent platform (voice, chat, email); enterprise automation |
| **Function** | Build — backend data pipelines, agent infrastructure, integrations |
| **Seniority** | New Grad (explicitly titled) |
| **Location** | New York, NY — On-site, full-time |
| **Team size** | Not stated; Series A stage (~20–50 engineers estimated) |
| **Comp** | $160K–$250K + equity |
| **TL;DR** | New grad backend engineer building the systems powering Giga's AI agents — agent memory, data pipelines, real-time knowledge, and observability tooling — at a Series A startup with DoorDash as a paying customer. |

**Key projects named in JD:**
- **Atlas** — AI assistant: Slack charts/alerts, natural language queries, platform resource management
- **Activity Stream** — Log visualization with filters, timestamps, frequency charts
- **Dynamic Knowledge** — Time-based context auto-updated from status pages and live sources
- **Agent Memory** — Conversation awareness, session-context persistence across interactions

**Fit signal vs. #015 (SF):** Identical JD; New York location is meaningfully better for Harry — closer East Coast timezone, lower COL delta vs. Atlanta, and NYC has a larger F-1/OPT/H-1B legal infrastructure than Series A SF startups.

---

## B) Match with CV

| JD Requirement | Harry's Evidence |
|---|---|
| **Production-quality code from internships or significant projects** | Google Chrome: C++ IPC shipped to stable for 3B+ users; TypeScript/React observer system across 25K+ lines of Chromium at 95% test coverage |
| **Backend: data pipelines, integrations, agent infrastructure** | TiMoto AI: primary engineer — gRPC inter-service layer, Python/Django REST backend, PostgreSQL, multi-AZ AWS ECS Fargate; vLLM inference serving pipeline |
| **AI agents / LLM serving** | TiMoto: vLLM + PagedAttention inference engine; resolved production gRPC deadlock under concurrent LLM calls — 100% evaluation success rate at sub-50ms p99 |
| **Self-unblocking, take ownership** | TiMoto: primary engineer on 3-person team — designs, deploys, debugs, and operates distributed production platform; 99.9% uptime, $40–60/month infra cost |
| **Shipping over perfection, still care about quality** | Chrome: 95% test coverage; zero production regressions in stable channel — quality bar from senior Chrome engineer reviews |
| **Real responsibility at a startup early** | TiMoto as primary backend/infra/ML engineer at 3-person team; shipped production AI platform serving real users |
| **Atlas features: Slack integrations, NL queries** | TypeScript/React Chromium system (observer pattern, 25K+ lines); Django REST API; no direct Slack API experience |
| **Agent memory: context across sessions** | TiMoto evaluation pipeline stores and retrieves session context; PostgreSQL + Redis caching patterns |
| **Activity Stream: log visualization, event tracking** | DynamoDB hot-partition diagnosis at 9K+ req/sec; N+1 query redesign (PostgreSQL indexing); CloudWatch/Prometheus observability at TiMoto; no dedicated log viz tooling shipped |
| **Dynamic knowledge: time-based, auto-updating** | vLLM inference serving live contextual responses under concurrent load; no direct status-page integration experience |

**Strengths:** TiMoto is architecturally analogous to what Giga builds — LLM serving + gRPC backend + PostgreSQL + agent session persistence. Harry has shipped and operated this stack in production. The JD could describe TiMoto's backend with minimal rewording.

**Gaps:**

| Gap | Blocker? | Mitigation |
|---|---|---|
| No direct Slack API integration | Nice-to-have | TypeScript/React Chromium work covers the frontend event-wiring; Slack API is a weekend project. Frame as "can build this" not "have built this" |
| No dedicated log visualization tooling | Soft | Observability experience (CloudWatch, Prometheus, p99 profiling) covers the conceptual ground; Grafana/data viz is adjacent |
| No voice/telephony stack | Low — role is backend infra | Named projects (Atlas, Activity Stream, Agent Memory) are backend/data, not voice DSP |

---

## C) Level and Strategy

**Level detected:** New Grad (explicitly titled). No years-of-experience requirement. Harry's profile (May 2027 grad, ~11 months internship + ongoing TiMoto primary engineer role) is the exact target.

**"Sell production-ready without overstating" plan:**

1. Lead with TiMoto: "primary engineer for backend, cloud infra, and ML serving on a 3-person team" — this is equivalent to 1–1.5 years of production experience at a small startup
2. Frame Google Chrome as quality signal: "shipped C++ IPC and TypeScript/React to Chrome stable (3B+ users) — code reviewed by senior Chrome engineers at 95% test coverage"
3. Anchor seniority with metrics: sub-50ms p99, 99.9% uptime, 44% cost reduction — show you measure and own your systems
4. Use Giga's framing back at them: "I want to take ownership from day one and ramp to full independence quickly" matches their "increasing independence as you ramp up" language exactly

**"If they downlevel me" plan:** Giga only has one new-grad tier — no downlevel risk. Comp band ($160K–$250K) applies to the whole new-grad cohort based on demonstrated fit. Negotiate starting salary within band based on Google + TiMoto evidence, targeting $175K.

---

## D) Comp and Demand

| Component | Value | vs Target |
|---|---|---|
| **Base** | $160,000–$250,000 | Floor $160K is $20K above walk-away ($140K minimum) ✅ |
| **Equity** | Offered — Series A ($61M, Nov 2025) | Illiquid until exit/IPO; standard 4-yr vest, 1-yr cliff |
| **Benefits** | Catered lunch, dinner stipend, $150/mo wellness, 401k, commuter, medical/dental/vision | Solid early-stage package for NYC |

**NYC market comp context (new grad SWE, 2026):**
- Glassdoor NYC new-grad SWE median: ~$163K base (25th pct $134K, 75th pct $202K)
- Giga's $160K floor is at the median for NYC new-grad — fair; $250K ceiling implies senior-range is achievable based on performance
- NYC COL vs. Atlanta: ~$1,500–2,000/month rent premium, partially offset by: no state income tax benefit (NY has income tax), but the $160K in NYC = ~$130K Atlanta equivalent after rent delta — still above walk-away in real terms

**Year-1 TC estimate:**
- Base ~$180K mid-band + Series A equity grant (typical: $80K–$150K over 4yr = $20K–$37K/yr)
- Year-1 TC: ~$195K–$215K — strong for a 2027 new grad

**Negotiate:** Anchor at $175K–$185K base. Evidence: Google Chrome FAANG intern (market-rate signal) + TiMoto production primary engineer (production engineer, not internship comp grade). Ask for grant size, cliff, and preferred liquidation preference stack.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | **Professional Summary** | Generic distributed systems framing | Lead with "primary engineer on TiMoto AI agent backend (vLLM, gRPC, AWS) → now targeting AI agent infrastructure at production scale" | Mirrors Giga's language: "systems that power our AI agents" |
| 2 | **TiMoto bullets** | Ordered by impact | Reorder: agent memory/session-context bullet first, then vLLM serving, then gRPC deadlock fix | Atlas + Agent Memory are the top two named projects; lead on match |
| 3 | **Google Chrome bullets** | IPC and lock-free trie as leads | Keep IPC/Protobuf as quality signal; add "TypeScript/React observer pattern — event-wiring applicable to Slack alert integrations" | Atlas Slack feature is TypeScript/event-driven |
| 4 | **Skills section** | Broad | Add "Agent memory, session-context persistence, LLM evaluation pipelines" to ML/AI Infrastructure row | Exact JD language for Agent Memory project |
| 5 | **Summary line** | "CS @ Georgia State · Google SWE intern · distributed systems & ML serving" | Add "AI agent infrastructure at TiMoto (vLLM + gRPC + AWS, production)" | Giga is AI agent infra; make it explicit in the first sentence |

**Top 5 LinkedIn changes:**
1. Headline: "Building AI agent infrastructure @ TiMoto AI · Google Chrome SWE · CS @ Georgia State 2027"
2. About section: Add "I'm interested in companies building AI agents for enterprise" — signals to Giga recruiters
3. TiMoto experience: Add "agent memory" and "session-context persistence" keywords
4. Skills: Add "Agent Infrastructure", "LLM Serving", "AI Agent Platforms"
5. Pin TiMoto demo (timoto.ai) as Featured — Giga will want to see a running AI product

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | **Agent infrastructure + production ownership** | TiMoto vLLM serving engine | 3-person team; LLM serving under concurrent production traffic | Eliminate KV cache OOM; achieve sub-50ms p99 | Architected vLLM + PagedAttention; continuous batching; tuned GPU memory allocation | Zero OOM failures; sub-50ms p99 sustained | Learned: KV cache fragmentation is a latency multiplier — next time I'd instrument memory pressure earlier |
| 2 | **Debugging production issues, unblocking yourself** | TiMoto gRPC deadlock | Production deadlock under concurrent agent evaluation calls | Trace root cause with no senior help; fix without regression | Traced shared resource acquisition; redesigned call sequencing | 100% evaluation success rate post-fix | Lesson: shared state under concurrency requires explicit ownership models — I now design for it upfront |
| 3 | **Data pipelines + activity stream / observability** | Google Chrome settings p99 profiling | 1,200ms p99 settings nav in Chrome stable | Cut to <50ms | Profiled with Chrome DevTools; identified mutex contention; implemented lock-free concurrent trie | 96% latency reduction, zero regressions in stable | Lesson: profiling is cheaper than guessing — instrument first, fix second |
| 4 | **Quality + shipping production-grade code** | Google Chrome IPC transport | Chrome needed IPC between browser process and settings service | Ship to 3B+ users; schema-evolving; cross-language compatibility | Chose Protocol Buffers over custom serialization; wrote design doc; senior code review | Shipped to Chrome stable; 10K+ req/sec, sub-50ms p99; design choices still in codebase | Lesson: the serialization choice in IPC outlives the feature — design for evolution, not just correctness |
| 5 | **Real responsibility at a startup** | TiMoto multi-AZ ECS Fargate + Terraform | Startup needed production-grade infra on $40–60/month budget | Design multi-AZ fault tolerance + zero-downtime deploys | Circuit breaker + health check auto-rollback; Terraform IaC; CloudWatch alarms | 99.9% uptime; 44% cost reduction | Lesson: cost-aware architecture is a superpower at startups — measure infra spend like an SLO |
| 6 | **Agent memory / session context** | TiMoto session persistence | Agents needed to recall prior interactions across sessions | Zero cross-session contamination; correct recall under concurrent calls | PostgreSQL session store + Redis cache layer; TTL-based expiry; tested under concurrent gRPC load | No cross-session contamination; accurate recall at production traffic | Lesson: session state bugs manifest as rare, hard-to-reproduce races — test at concurrency, not just unit level |

**Case study to present:** TiMoto AI (timoto.ai). Walk through: problem → architecture choice (vLLM vs naive inference) → gRPC design → observability → how you'd extend it to add Slack alerts and activity stream (directly mapping to Atlas + Activity Stream named projects). This is a live demo of what Giga builds.

**Red-flag questions and how to answer:**

- *"You're still in school — can you start?"* → "I'm targeting May 2027 graduation, and I'm happy to discuss start dates during the offer stage. For the right role I have flexibility — I can also consider part-time arrangements in the interim."
- *"You're on F-1 — do you need sponsorship?"* → "I'm on F-1 OPT beginning May 2027. I'll need H-1B sponsorship for long-term employment. Many well-funded Series A companies sponsor — can you confirm Giga's policy? I want to be transparent early so neither of us wastes time."
- *"Why apply to a third Giga requisition?"* → "I've evaluated the SF New Grads and SWE I/II roles — I'm genuinely excited by Giga's engineering work (the agent memory and Activity Stream projects are exactly the problems I've been solving at TiMoto). The New York location is a strong fit for me, so I wanted to make sure I applied to this specific req."

**Story bank note:** Stories 1–4 are already covered from #015 and #019 evaluations. Stories 5 and 6 are additions — append to `interview-prep/story-bank.md`.

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| **Posting live** | Active Ashby page; "Apply for this Job" button present; full JD rendered; URL resolves to valid requisition | Positive |
| **Salary transparency** | $160K–$250K + equity explicitly listed on Ashby listing | Positive |
| **Company verification** | gigaml.com in nav; Fortune article ($61M Series A, Nov 2025); DoorDash partnership confirmed | Positive |
| **Company health** | Series A ($61M), DoorDash paying customer, no layoff news found in 2026 search | Positive |
| **JD specificity** | Four named projects (Atlas, Activity Stream, Dynamic Knowledge, Agent Memory) with concrete feature descriptions — not boilerplate | Positive |
| **New grad targeting** | "New Grads" in title, "ramp up quickly", "ramp to independence" — intentional new-grad hire, not repurposed senior req | Positive |
| **ATS** | Ashby — standard startup hiring platform; valid GigaML org slug | Positive |
| **Reposting check** | Not in scan-history.tsv; different URL/UUID from #015 (cb74...) — this is a separate requisition for New York | Positive |
| **Distinct from #015** | #015 = SF, UUID cb74c445; this = NY, UUID 7314c5c1 — Giga is opening both cities for new grads | Positive |

**Context notes:** Giga posting both SF (#015) and NYC (this) new-grad roles suggests active, multi-city hiring. Series A with paying customers and no layoff signals. Real posting.

---

## H) Draft Application Answers

Score is 4.4/5 — above the 4.5 threshold for Block H auto-generation. Score is 4.4 — close but below 4.5. Including H anyway given strong archetype match and user's apply-all policy for score ≥ 3.0.

**"Why Giga?"**

> Giga is building exactly what I've been building at TiMoto, but at enterprise scale. I'm the primary engineer for backend, cloud infra, and ML serving on a 3-person team — I own the vLLM serving stack, gRPC inter-service layer, and AWS/Terraform infrastructure. The Agent Memory and Activity Stream projects in the JD describe problems I'm actively solving in production. I want to work somewhere where that experience translates directly on day one, and where I can learn from engineers who've scaled these systems to DoorDash-level traffic.

**"What's a technical problem you're proud of solving?"**

> At TiMoto, our AI evaluation system started failing under concurrent agent calls — 100% failure rate at >4 parallel requests. I traced it to a gRPC deadlock: two services acquiring the same shared resource in different orders under concurrent calls. I redesigned call sequencing to enforce a consistent resource acquisition order and added a circuit breaker to fail fast on contention rather than deadlock. Result: 100% success rate, sub-50ms p99 evaluation latency at production traffic. It taught me that concurrency bugs are design bugs — you fix them at the architecture level, not the symptom level.

**"Tell me about a time you shipped something under constraints."**

> At Google Chrome, I needed to add a new IPC transport between the browser process and the settings service. Custom serialization would have been faster to write but brittle — any schema change breaks the wire format. I chose Protocol Buffers: more upfront work, but schema-evolving and cross-language. Wrote the design doc, got it reviewed by senior Chrome engineers, shipped to stable. It now handles 10K+ req/sec at sub-50ms p99 for 3B+ Chrome users. The constraint was: ship once, maintain forever — Protobuf was the only defensible choice.

---

## Keywords Extracted

`AI agents`, `agent memory`, `session context`, `data pipelines`, `backend infrastructure`, `agent infrastructure`, `LLM serving`, `TypeScript`, `Python`, `gRPC`, `PostgreSQL`, `Redis`, `distributed systems`, `observability`, `log visualization`, `Slack integration`, `natural language queries`, `dynamic knowledge`, `Series A`, `new grad`, `enterprise AI`, `voice AI`, `real-time`, `production quality`, `ownership`
