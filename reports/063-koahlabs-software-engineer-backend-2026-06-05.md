# Evaluation: Koah Labs — Software Engineer, Backend

**Date:** 2026-06-05
**URL:** https://jobs.ashbyhq.com/koahlabs/43616243-f485-480d-b31a-f89589a4b09d
**Archetype:** Backend / Distributed Systems Engineer + Founding / Early-Stage Software Engineer
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** pending

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Backend / Distributed Systems Engineer (primary) + Founding/Early-Stage (secondary) |
| Domain | Ad-tech platform — publisher monetization + advertiser targeting for AI-native apps |
| Function | Build — scalable data models, low-latency systems, ad bidding schemas |
| Seniority | Mid-level implied (no explicit YOE stated); ownership signals suggest 2–4 YOE floor |
| Remote | On-site (San Francisco or New York) |
| Team size | ~16 employees total (Series A, Feb 2026); tight-knit engineering team |
| TL;DR | Early-stage ad network building "AdSense for AI" — backend engineer to own low-latency ad delivery, impression data models, and frequency capping on a small team. |

**Visa note:** No sponsorship mention in JD. Company is a 16-person Series A startup — sponsorship at this stage is possible but uncertain. Flag with recruiter early per policy.

---

## B) Match with CV

### Requirements vs CV Mapping

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Build scalable data models for high-volume impressions | TiMoto: "gRPC inter-service layer... resolved production deadlock under concurrent calls... 100% evaluation success rate at sub-50ms p99"; Develop for Good: "N+1 query bottleneck... PostgreSQL indexing... sub-100ms for 10,000+ records" | Strong |
| Low-latency frequency capping system | TiMoto: "sub-50ms p99" inference serving; Google: "96% latency reduction, zero production regressions" via lock-free concurrent trie | Strong |
| Design abstractions for flexible engagement event tracking | Google Chrome: "event-driven TypeScript/React system with observer pattern decoupling UI state propagation — accelerated feature delivery 68% across 25K+ lines" | Strong |
| High-volume ad bidding schemas (ClickHouse, Kafka, PostgreSQL) | PostgreSQL: Develop for Good + TiMoto; Kafka listed in Skills; ClickHouse is a gap | Moderate (ClickHouse gap) |
| Debugging and optimizing performance | Google: "Identified settings navigation as p99 bottleneck at 1,200ms... 96% latency reduction"; TiMoto: "resolved production deadlock... tracing shared resource acquisition conflicts" | Strong |
| Detail-oriented, good abstractions others rely on | Google Chrome: production C++ IPC with Protobuf + 95% test coverage; TiMoto: "gRPC inter-service layer" relied on across services | Strong |
| Experimentation, measuring, creating reliable systems | TiMoto: "99.9% uptime, 44% cost reduction, auto-rollback on health check failure"; Google: "95% test coverage, changes adopted into production branch reviewed by senior engineers" | Strong |
| Ruby on Rails (core app) | Not in CV — gap | Gap |
| Redis | Listed in Skills + implied in distributed caching work | Moderate |
| Kafka | Listed in Skills | Moderate (no explicit production story) |
| ClickHouse | Not in CV | Gap |
| Terraform / AWS | TiMoto: "Architected multi-AZ ECS Fargate with Terraform IaC" | Strong |
| Small team / startup ownership | TiMoto: primary engineer on 3-person team, owns backend + infra + ML end-to-end | Strong |

### Gaps & Mitigation

| Gap | Blocker? | Mitigation |
|-----|----------|------------|
| Ruby on Rails | Soft — JD says "core app" but backend engineers at startups often learn the stack | Mention TypeScript/Python/Django fluency + fast ramp history. Strong distributed systems > language fluency at early-stage. |
| ClickHouse | Soft — nice-to-have for analytics | Note: "familiar with columnar store concepts (PostgreSQL analytical queries, Redis caching); quick to ramp ClickHouse" |
| No explicit ad-tech experience | Soft | Low-latency frequency capping + event tracking are generic backend problems Harry has solved (TiMoto inference SLOs, Google trie optimization) |
| Mid-level expectation vs new grad | Moderate | TiMoto primary engineer framing + production metrics are strong counters; company is early-stage where ownership > title |

---

## C) Level and Strategy

**Level detected:** JD doesn't state YOE. "Build scalable data models," "design abstractions," "create schemas" — all individual contributor deliverables. Stack ownership at a 16-person startup implies 2–5 YOE floor in traditional hiring, but early-stage companies often hire on proof, not years.

**Harry's position:** New grad 2027 with production backend at TiMoto + Google internship. This is above-average for a new grad but below a typical mid-level hire in years. Risk: screened out before reaching technical. Mitigation: lead with outcomes, not dates.

**"Sell senior without lying" plan:**
- Lead with: "Primary engineer for backend, infra, and ML serving on TiMoto's 3-person team — production systems at sub-50ms p99, 99.9% uptime."
- On Ruby on Rails gap: "I ramp fast. I was the first to own gRPC + vLLM at TiMoto with no prior production reference; same approach for Rails."
- On data systems: "I've diagnosed and fixed N+1 at scale, designed distributed caching, and built event-driven abstractions relied on across 25K lines in Chrome stable."
- Position ad-tech match: "Frequency capping is a rate-limiting problem with a cardinality constraint — same shape as the concurrent gRPC deadlock I resolved at TiMoto."

**"If they downlevel me" plan:** Koah is pre-product-market-fit scale. A lower title with the right scope and equity is a strong trade. Accept if equity + comp still meets $140K minimum; negotiate 6-month review tied to shipping first major data model.

---

## D) Comp and Demand

| Metric | Data | Source |
|--------|------|--------|
| JD posted comp | $180K–$250K + equity | Ashby JD (direct) |
| Harry's target range | $150K–$200K | config/profile.yml |
| Harry's walk-away | $140K | config/profile.yml |
| Market: backend SWE, SF, early-stage | $140K–$200K base (new grad at top-tier startup); $180K–$220K for mid-level | Glassdoor, Levels.fyi general data |
| Company funding | $26.5M total ($5M seed Sep 2025 + $20.5M Series A Feb 2026) | PRNewswire, TechCrunch |
| Investors | Theory Ventures (led Series A), Forerunner, South Park Commons, Andrew Karam (AppLovin co-founder) | SiliconANGLE |
| Team size | ~16 employees | SiliconANGLE Feb 2026 |
| Traction | 2M MAU, 35M+ ad impressions, 175M queries served | SiliconANGLE |

**Comp assessment:** The JD band ($180K–$250K) is above Harry's target floor and well above walk-away. Even at the bottom of the band ($180K base) this is a strong comp outcome for a new grad. The equity component at a freshly-funded Series A with real traction is meaningful upside.

**Risk:** As a new grad Harry may be offered the lower end or a new-grad-adjusted offer. Still likely above $150K floor given the JD band. Negotiation leverage: production outcomes at TiMoto + Google.

---

## E) Customization Plan

### CV Changes (top 5)

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet 1 | "distributed production systems end-to-end" | Add: "...including high-throughput data pipelines and event tracking across gRPC and PostgreSQL" | Mirrors JD's engagement event tracking + data model language |
| 2 | TiMoto bullet 3 | vLLM/PagedAttention focus | Add parenthetical: "applied same low-latency discipline to Redis caching layer" | Signals Redis + caching intent for frequency capping |
| 3 | Skills — Frameworks & Databases | "Django, FastAPI, Node.js, React, REST APIs, PostgreSQL, Redis, MongoDB" | Add "Kafka" explicitly as a standalone (already in distributed systems row but not surfaced here) | JD lists Kafka prominently in Data stack |
| 4 | Google bullet 3 | "event-driven TypeScript/React system with observer pattern" | Rephrase: "Designed event-driven abstraction layer (observer pattern) for UI state propagation — adopted across 25K+ lines of Chromium, 95% test coverage" | "Abstraction" + "relied on by others" language directly mirrors JD fit signals |
| 5 | Develop for Good bullet 1 | AWS BaaS / JWT auth | Add: "...designed schema for horizontal read/write scale (PostgreSQL + indexing strategy)" | Reinforces schema design capability — JD explicitly calls for "creating schemas" |

### LinkedIn Changes (top 5)

| # | Section | Change |
|---|---------|--------|
| 1 | Headline | Add "ad-tech backend" or "high-throughput data systems" to target keyword for ad-tech recruiter searches |
| 2 | TiMoto description | Add: "Redis-based caching, event-driven service abstractions" to match Koah stack |
| 3 | Skills | Ensure Kafka, ClickHouse, Redis, PostgreSQL all pinned in top 10 |
| 4 | About section | One line: "I build systems that stay fast under load — gRPC, Kafka, Postgres, vLLM" |
| 5 | Featured | Pin TiMoto demo (timoto.ai) — startup investors love seeing working products |

---

## F) Interview Plan

### STAR+R Stories

| # | JD Requirement | Story Title | S | T | A | R | Reflection |
|---|----------------|-------------|---|---|---|---|------------|
| 1 | Low-latency system design | Google lock-free trie | Settings nav at 1,200ms p99 under concurrent reads | Eliminate mutex contention without changing external API | Designed lock-free concurrent trie replacing RW mutex | 96% latency reduction, zero regressions, shipped to Chrome stable | Should have profiled earlier; assumed contention was in DB, not data structure |
| 2 | Debugging + optimizing performance | TiMoto gRPC deadlock | 100% evaluation failure rate under concurrent gRPC calls | Resolve without service downtime or API change | Traced shared resource acquisition sequence; redesigned call ordering | 100% success rate, sub-50ms p99 restored | Learned to draw resource dependency graphs first before assuming retry logic will help |
| 3 | Build scalable data models | Develop for Good N+1 fix | 3s+ response on large datasets in production | Sub-100ms SLO with no downtime | Diagnosed N+1, redesigned with PostgreSQL indexing + query rewrite | Sub-100ms for 10K+ records, permanent fix | Would have added query profiling to CI earlier to catch regression before prod |
| 4 | Design abstractions others rely on | Google observer pattern | Feature delivery blocked by tightly coupled UI state | Decouple UI state propagation without breaking existing subscribers | Designed event-driven observer-pattern abstraction across 25K lines | 68% feature delivery acceleration, 95% test coverage | Documented design as ADR; adoption accelerated because engineers understood the contract |
| 5 | Experimentation + reliable systems | TiMoto vLLM selection | Naive inference causing OOM under concurrent load | Zero OOM at production traffic, no latency regression | Evaluated vLLM + PagedAttention vs naive batching; chose vLLM for KV cache efficiency | Zero OOM failures, continuous batching at sub-50ms | Explicit benchmarking doc became team runbook — saves debugging time on every inference regression |
| 6 | Schema design for high-volume data | TiMoto ECS + PostgreSQL | Need production DB schema supporting multi-AZ replication | Schema must survive partition events without data loss | Designed schema with Terraform-managed RDS multi-AZ; circuit breaker on health check | 99.9% uptime, auto-rollback on failure | Would use ClickHouse earlier for analytics-side queries; PostgreSQL right for transactional, wrong for aggregation at scale |
| 7 | Small team / early-stage ownership | TiMoto primary engineer framing | 3-person team, no dedicated infra engineer | Own backend + infra + ML serving end-to-end | Chose ECS Fargate over K8s to minimize ops burden; Terraform for reproducibility | 44% cost reduction ($40–60/mo), 99.9% uptime | Startup infra: choose managed services aggressively early, own the complexity only when scale demands it |

**Recommended case study:** TiMoto gRPC deadlock + vLLM selection — demonstrates the two things Koah needs most: (1) low-latency distributed system debugging and (2) production-grade reliability on a small team. Walk through the architecture diagram if asked.

**Red-flag Q&A:**
- "You're a new grad — can you handle this scope?" → "At TiMoto I'm the primary backend engineer for production systems at sub-50ms p99. I've debugged distributed deadlocks, shipped infra changes with Terraform, and owned on-call rotation. I won't need to ramp on what production feels like — I'm already in it."
- "You don't know Ruby on Rails" → "I haven't shipped Rails but I've built production REST backends in Django and FastAPI, and I ramp fast on new frameworks. The distributed data and latency problems in this JD are language-agnostic — I can ship Rails in a few weeks with the same rigor."
- "Do you need visa sponsorship?" → "I'm on F-1 status, currently CPT/OPT eligible. I'll need H-1B sponsorship for long-term employment. Can you confirm the company's sponsorship policy?"

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active — "Apply for this Job" button present and functional | Positive |
| Posting freshness | Posted May 14, 2026 — 22 days ago at time of evaluation | Positive |
| JD specificity | High — names specific stack (ClickHouse, Kafka, Redis, Terraform, LGTM), specific project examples (frequency capping, bidding schemas, impression data models), specific team culture | Positive |
| Company health | $20.5M Series A closed Feb 2026, led by Theory Ventures; real traction (35M+ impressions, 175M queries, 2M MAU) | Positive |
| Layoff / freeze signals | No results found for Koah Labs layoffs or freeze | Positive |
| Repost detection | Not found in scan-history.tsv | Positive |
| Requirements realism | No YOE stated; scope matches a 16-person team hiring for early-stage; no contradictions | Positive |
| Salary transparency | $180K–$250K explicitly stated | Positive |

**Context notes:** This is a recently-funded Series A startup with 16 people actively growing on both publisher and advertiser sides. The JD is highly specific and includes real example projects, which is a strong signal of an active, genuine hire. No concerns.

---

## H) Draft Application Answers

*(Score 3.8 — below 4.0 threshold for Block H. Block H skipped per mode rules.)*

---

## Keywords Extracted

ad network, ad bidding, impression data model, frequency capping, engagement events, low-latency, Ruby on Rails, PostgreSQL, ClickHouse, Redis, Kafka, Python, Terraform, AWS, Cloudflare, scalable data models, schema design, performance optimization, observability, LGTM stack, TypeScript, React, distributed systems, high-volume, ad exchange, publisher monetization

---

## Machine Summary

```yaml
company: Koah Labs
role: Software Engineer - Backend
score: 3.8
archetype: Backend / Distributed Systems Engineer + Founding/Early-Stage
seniority: Mid-level (implied)
location: San Francisco or New York (on-site)
comp_stated: "$180K-$250K + equity"
comp_vs_target: above target range ($150K-$200K)
visa_risk: moderate (no sponsorship mention, 16-person startup)
ruby_rails_gap: true
clickhouse_gap: true
legitimacy: High Confidence
posted: 2026-05-14
series: A ($20.5M, Feb 2026)
team_size: ~16
traction: "2M MAU, 35M+ impressions"
recommendation: apply (above $140K walk-away; real traction; production experience maps well despite gaps)
```
