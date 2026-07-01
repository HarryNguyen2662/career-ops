# Evaluation: Discord — Software Engineer, Database Infrastructure

**Date:** 2026-06-07
**URL:** https://job-boards.greenhouse.io/discord/jobs/8487457002
**Archetype:** Backend / Distributed Systems Engineer + Systems Software Engineer
**Score:** 3.7/5
**Legitimacy:** High Confidence
**PDF:** output/085-discord-software-engineer-database-infrastructure-harry-nguyen-2026-06-07.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Backend / Distributed Systems Engineer (primary) + Systems Software Engineer (secondary) |
| Domain | Database Infrastructure — ScyllaDB, PostgreSQL, ElasticSearch, Rust-based data access services |
| Function | Build + Operate — large-scale data systems for 200M+ MAU; storage primitives for all Discord |
| Seniority | Mid-level (2–4 years) — but Discord values technical depth over exact years |
| Remote | SF Bay Area (onsite/hybrid) |
| Team size | Small team (high-impact, few engineers) |
| Comp | $160,000–$180,000 base + equity + benefits |
| TL;DR | Discord's database infra team stores trillions of messages for 200M+ users — ScyllaDB, PostgreSQL, Rust. Harry's gRPC/PostgreSQL/Rust/C++ profile hits every preferred skill. The 2–4 year requirement is the main risk (Harry ~9 months full-time at TiMoto); Discord's technical culture favors depth over YOE. Comp ($160K–$180K base, ~$280K+ TC with equity) clears Harry's target. H-1B confirmed sponsor (29 approved petitions FY2025). Apply — flag experience gap, lead with production depth. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| Backend infrastructure (2–4 years) | TiMoto: primary engineer backend+infra+ML serving (~9 months); Google Chrome: SWE intern; Develop for Good: AWS BaaS | ⚠️ ~9 months full-time (gap vs 2–4 yrs) |
| Statically-typed language: Rust, Go, Java, C, C++ | Skills: Rust, Go, C++; Chrome: C++ IPC; Pulumi: Go CLI | ✅ Three of five listed |
| Distributed systems + concurrency control fundamentals | TiMoto: gRPC inter-service, deadlock fix via resource conflict tracing; Pulumi: Raft/Paxos study | ✅ Direct |
| Troubleshoot/debug complex production systems | TiMoto: gRPC deadlock root-cause; Chrome: lock-free trie for mutex contention; Develop for Good: N+1 query diagnosis | ✅ Strong |
| Fast-paced environment ownership | TiMoto: primary engineer on 3-person startup, 0→1; on-call rotation | ✅ |
| ScyllaDB/Cassandra/distributed DB experience | No ScyllaDB or Cassandra in CV | ❌ Bonus gap |
| Rust experience (bonus) | Rust in Skills row | ✅ Present (no Rust production work yet) |
| Terraform/Kubernetes (bonus) | TiMoto: Terraform IaC multi-AZ; Skills: Kubernetes, Docker | ✅ Direct |
| PostgreSQL | Develop for Good: diagnosed N+1, PostgreSQL indexing sub-100ms for 10K+ records | ✅ |
| H-1B / sponsorship | F-1 — Discord confirmed H-1B sponsor: 29 approved petitions FY2025, 100% approval rate | ✅ Positive |
| Bay Area onsite/hybrid | Harry Atlanta-based; open to relocation | ⚠️ Relocation needed |

**Gaps:**

1. **Experience (2–4 years vs ~9 months full-time).** Main risk. Harry's TiMoto work is production-quality distributed systems, but only ~9 months full-time. Mitigation: Frame TiMoto as equivalent of 2 years for most candidates — primary engineer with no senior safety net, production incidents, on-call, circuit breakers, SLOs. The quality of the experience exceeds the quantity of time. Chrome intern further adds production systems depth.
2. **No ScyllaDB/Cassandra experience.** The team runs ScyllaDB for message storage. Harry has PostgreSQL and Redis. Mitigation: distributed DB fundamentals (Raft/Paxos study in Pulumi project, exactly-once semantics in Skills) show the right mental model. ScyllaDB is CQL-compatible with Cassandra — learnable quickly.
3. **Rust is on CV but no production Rust shipped.** Discord switched from Go to Rust as a core value. Mitigation: Rust in Skills is real; Harry can demonstrate systems programming depth through Chrome C++/lock-free as the conceptual proxy, and commit to Rust ramping.
4. **Relocation to SF Bay Area.** Harry is Atlanta-based. Not a blocker — Harry is open to relocation.

---

## C) Level and Strategy

**Level detected:** The JD says "2–4 years" which maps to L3 (mid-level). Harry is below that by tenure but above it by demonstrated systems depth.

**Strategy: Lead with production evidence, not tenure.**
> "I know the JD says 2–4 years. At TiMoto I was the primary engineer responsible for backend, cloud infra, and ML serving on a 3-person team — no senior engineer above me in the stack. I traced production deadlocks in gRPC, designed multi-AZ ECS Fargate with Terraform, and maintained 99.9% uptime at $40–60/month. Before that I shipped a C++ IPC transport layer and lock-free concurrent data structure to 3 billion Chrome users. The time on paper is short; the problems I've solved are not."

**On Discord's Rust culture:**
> "Discord switching from Go to Rust is one of the reasons I read your blog. The latency guarantees and memory safety story you described are the same tradeoffs I think about in production. I have C++ and Rust in my toolkit — the mental model is directly transferable."

**On ScyllaDB gap:**
> "I've worked with PostgreSQL at the query and indexing level, and I've studied Raft/Paxos for distributed consensus in the context of the Pulumi state sync layer. ScyllaDB is a new surface area, not a new paradigm — I'll ramp fast."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Discord stated base | $160,000–$180,000 |
| Discord L3 SWE TC (Levels.fyi) | ~$285K–$415K (median $354K in US) |
| Discord H-1B average prevailing wage | $253,458 (h1bgrader.com) |
| Harry target | $150K–$200K base |
| Harry minimum | $140K |

Base ($160K–$180K) clears Harry's $140K minimum and hits the $150K–$200K target range. TC with equity is compelling — Discord SWE L3 median is ~$354K total. Discord is a private company (last valued ~$15B); equity is illiquid but meaningful. Comp picture is strong.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Languages row | C++ first | Rust, Go, C++, Python first | Discord primary language is Rust; Go is secondary; C++ shows systems depth |
| 2 | TiMoto bullet order | gRPC deadlock varies | Lead with gRPC inter-service + deadlock fix | Distributed systems + production debugging = primary Discord signal |
| 3 | Chrome bullet order | C++ IPC leads | Keep C++ IPC leading + lock-free trie second | Systems programming at Chrome scale is direct evidence for "extreme low-latency" work Discord cites in their blog |
| 4 | Skills row order | Distributed Systems leads | Distributed Systems leads, then Languages (Rust/Go/C++ first) | Database infra team is distributed systems first |
| 5 | Develop for Good | AWS BaaS | Add PostgreSQL indexing bullet emphasis | PostgreSQL is one of Discord's three main DB systems |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Distributed systems + concurrency | TiMoto gRPC deadlock | Production deadlock under concurrent gRPC calls | 100% evaluation success at sub-50ms p99 | Traced shared resource acquisition conflicts; redesigned call sequencing | Resolved, zero recurrence | Deadlocks are resource ordering violations hidden by happy-path testing — you need to map every acquisition path, not just the critical path |
| 2 | Large-scale systems debugging | Chrome lock-free trie | 1,200ms p99 settings navigation, mutex contention under production Chrome load | 96% latency reduction without correctness regression | Identified lock contention; designed lock-free concurrent trie; proved linearizability | 96% cut, zero regressions | Concurrent code needs a proof, not just tests — tests sample interleavings, proofs cover them all |
| 3 | PostgreSQL + data access layer | Develop for Good N+1 | 3s+ response time on large datasets due to N+1 query | sub-100ms for 10,000+ records | Diagnosed ORM-generated N+1 pattern; redesigned with PostgreSQL indexing | Consistent sub-100ms | N+1 is a symptom of abstraction hiding SQL costs — always read the generated query plan |
| 4 | Production reliability + SLOs | TiMoto multi-AZ | Distributed AI product; failure modes span gRPC + DB + ML serving | 99.9% uptime with auto-rollback | Circuit breaker pattern, CloudWatch alerts, multi-AZ failover, Terraform IaC | 44% cost cut, zero unplanned downtime | Reliability is designed in, not bolted on — circuit breakers need to be part of the initial schema |
| 5 | Systems programming depth | Chrome C++ IPC | Chrome needed IPC transport across browser process boundaries | Ship to 3B users with zero breaking schema changes | C++ Protocol Buffers; design doc; schema evolution rationale; senior review | Chrome stable, sub-50ms p99, 10K+ req/sec, adopted into Chromium | Schema choices in distributed systems are API contracts you'll live with for years — design for how they change |

**Recommended case study:** TiMoto gRPC deadlock + Chrome lock-free trie combo — "I've diagnosed production deadlocks under concurrent load and designed lock-free concurrent data structures for billions of users. Discord's problems — trillions of messages, extreme latency budgets, Rust-based access services — are the same class of problem at larger scale."

**On Discord's Rust blog post (great opening):** "I read 'Why Discord is switching from Go to Rust' when it came out — the read-buffer-invalidation problem you described is exactly the kind of thing you can't catch until production. I want to work somewhere that publishes that level of technical honesty."

**Red-flag questions:**
- *"2–4 years — you're at less than 1?"* → "9 months at TiMoto as primary engineer with no senior above me, plus a Chrome internship where I shipped C++ to 3B users. The year count is short; the production surface area isn't."
- *"No ScyllaDB?"* → "Not yet. But I've studied Raft/Paxos for distributed consensus and worked with PostgreSQL at the query level. Distributed DB fundamentals are the same — the surface syntax differs, not the reasoning."
- *"Work authorization?"* → "F-1, OPT from May 2027. Discord filed 29 H-1B petitions in FY2025, all approved. Happy to walk through the timeline."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active on Greenhouse | Positive |
| Comp disclosed | $160K–$180K explicitly stated | Positive |
| Company status | Discord — 200M+ MAU, private ~$15B valuation, gaming/social platform | Positive |
| H-1B sponsorship | 29 approved H-1B petitions FY2025, 100% approval rate (h1bgrader.com) | Positive |
| JD specificity | Named technologies (ScyllaDB, PostgreSQL, ElasticSearch, Rust, Linux), team size signal ("small team"), blog posts linked, specific comp range | Positive |
| Technical blog credibility | Three real blog posts linked — "How Discord Stores Trillions of Messages," "How Discord Indexes Trillions of Messages" — confirms team exists and ships | Positive |
| Role-company fit | Database Infrastructure is a core function for a 200M-MAU messaging platform | Positive |
| AI usage question | Custom question on AI/LLM workflow — shows team is thoughtful about tooling, not a ghost posting | Positive |

---

## Keywords extracted

Rust, Go, C++, ScyllaDB, PostgreSQL, ElasticSearch, distributed systems, database infrastructure, concurrency, Linux, backend infrastructure, data access services, Terraform, Kubernetes, high availability, fault tolerance, first principles, low latency, production, San Francisco Bay Area, SWE, software engineer

---

## Machine Summary

```yaml
company: Discord
role: Software Engineer, Database Infrastructure
date: 2026-06-07
url: https://job-boards.greenhouse.io/discord/jobs/8487457002
score: 3.7
archetype: Backend / Distributed Systems Engineer + Systems Software Engineer
location: San Francisco Bay Area (onsite/hybrid)
comp_range: "$160,000–$180,000 base + equity; L3 TC est. $285K–$415K"
visa_risk: "F-1 — H-1B positive (29 approved petitions FY2025, 100% rate)"
legitimacy: High Confidence
recommendation: "Apply — Rust/C++/Go/PostgreSQL/Terraform stack matches; experience gap (2–4 yrs vs ~9 months) is the main risk; lead with production depth not tenure; comp $160K–$180K clears target; H-1B confirmed"
```
