# Evaluation: Palantir — Backend Software Engineer, Infrastructure Foundations

**Date:** 2026-06-09
**URL:** https://jobs.lever.co/palantir/fb2d3222-dbd8-4e03-8d39-47b820e9509c
**Archetype:** Backend / Distributed Systems Engineer + Systems Software Engineer
**Score:** 3.4/5
**Legitimacy:** High Confidence
**PDF:** output/096-palantir-backend-swe-infrastructure-foundations-harry-nguyen-2026-06-09.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Backend / Distributed Systems Engineer + Systems Software Engineer — infrastructure foundations layer (storage, auth, search, container orchestration) for Foundry + Gotham |
| Domain | Data platform infrastructure — lowest layers of Palantir Foundry (commercial) and Gotham (government); distributed systems, search/indexing, large-scale data processing |
| Function | Build — production infrastructure: distributed storage, search ecosystems, container orchestration, security primitives, scalable APIs |
| Seniority | Unlabeled SWE — "Backend Software Engineers" with no explicit years req; intermediate-to-senior framing based on JD scope |
| Location | New York, NY — Hybrid |
| Team | Palantir infrastructure (product teams of ~5–10 engineers); world-leading data platform serving intelligence, defense, commercial enterprise |
| Comp | $135,000–$200,000 base + RSUs + sign-on bonus (Palantir is public PLTR; RSUs are liquid) |
| TL;DR | Palantir Infrastructure Foundations — distributed systems, storage, search, container orchestration. Harry's C++ and Python are explicitly listed in the JD. Distributed systems depth (gRPC, Kafka, K8s, circuit breakers) maps to Cassandra/Elasticsearch/Kafka/K8s stack. H-1B confirmed. Three concerns: (1) $135K floor below $140K minimum — but RSU + sign-on at public company likely pushes TC above target; (2) F-1 + Palantir government work = cannot obtain US security clearance (ask about commercial/Foundry track); (3) Java is the primary language in practice (Harry's production experience is C++/Python, not Java). Score 3.4/5 — conditional apply: confirm commercial track placement and negotiate toward $160K+ base. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| Strong coding in Java, C++, Python, Rust, or similar | Google Chrome: C++ IPC transport layer + lock-free trie (production at 3B-user scale); TiMoto: Python (FastAPI/Django/vLLM); Skills: Java, Rust, Go listed | ✅ C++ and Python are direct; Java/Rust are listed only |
| Distributed systems (storage, auth, compute orchestration) | TiMoto: multi-AZ ECS Fargate, Terraform, circuit breakers, gRPC inter-service layer, PostgreSQL + Redis; Pulumi: K8s, multi-cloud provisioning; Skills: Kafka, Kubernetes | ✅ Strong conceptual match (not Cassandra/Elasticsearch specifically) |
| Search and indexing ecosystem | Not in CV | ❌ Gap (Elasticsearch not present; lock-free trie is adjacent) |
| Container orchestration (K8s, Flink, Spark) | TiMoto: ECS Fargate + EKS + Kubernetes (Skills); Pulumi: multi-cloud K8s | ✅ K8s present; Flink/Spark not in CV |
| Open-source contributions | Pulumi: Go CLI features and bug fixes, under active review by core maintainers | ✅ Direct OSS contribution signal |
| Cloud infrastructure + data processing | TiMoto: AWS (ECS Fargate, EKS, EC2, S3, RDS), Terraform IaC; Skills: Kubernetes, Docker, CloudWatch | ✅ Strong |
| High availability + fault tolerance | TiMoto: 99.9% uptime, circuit breakers, auto-rollback, multi-AZ | ✅ Direct |
| Security clearance (beneficial, not required) | F-1 — US security clearances are not available to F-1 visa holders in general; Palantir has both cleared (Gotham) and uncleared (Foundry commercial) teams | ⚠️ Must confirm commercial/Foundry track placement |
| CS/Math/Physics background | Georgia State BS CS, GPA 3.75 | ✅ Direct |
| H-1B | F-1 — Palantir confirmed active H-1B sponsor: 8 LCAs filed FY2026, 100% approval rate (h1bgrader.com) | ✅ Confirmed |
| NYC hybrid | Harry Atlanta-based; relocation needed; open per profile | ⚠️ Relocation required |

**Gaps:**

1. **Java is the primary language in practice.** The JD lists Java, Rust, and Go as the backend languages, with C++ and Python as alternatives in "What We Require." In reality, Palantir's infrastructure stack is heavily Java-based (Foundry backend, internal tooling). Harry has Java listed in Skills but no Java production bullets in the CV. This is the most significant technical gap. Mitigation: Harry's C++ (Chrome IPC, lock-free data structures) demonstrates systems-level proficiency — Java's runtime model is different but the systems thinking (memory, concurrency, latency) is transferable.

2. **Clearance concern for F-1.** US security clearances are generally not available to non-US citizens including F-1 holders. The JD calls clearance "beneficial, not necessary" — but Palantir's Gotham platform powers classified intelligence and DoD systems. F-1 engineers can work on Palantir Foundry (commercial) but are categorically excluded from Gotham classified work. This limits team placement and career paths within Palantir. Mitigation: **Ask explicitly in first recruiter call: "Is this role on the Foundry commercial track, and does it require current or future security clearance eligibility?"** Previous Palantir evaluation (#027) flagged the same concern.

3. **$135K comp floor below minimum.** The stated base range starts at $135K — $5K below Harry's $140K walk-away. Mitigation: Palantir is a public company — RSUs are liquid and sign-on bonuses are common. Realistic TC at the entry level for this role is likely $180K–$220K including equity. Negotiate base toward $155K–$165K and use competing offers (Plaid $176K+ base, LangChain $165K+ base) as leverage. If base stays below $140K, equity + sign-on must compensate.

4. **Search/indexing domain.** The first bullet is "building a performant search and indexing ecosystem." Harry has no Elasticsearch or search infrastructure experience. Mitigation: The Chrome lock-free trie is a search data structure. Distributed systems fundamentals (indexing, data locality, query planning) transfer. Not a hard blocker for a generalist infra role.

---

## C) Level and Strategy

**Level detected:** Mid-level (unlabeled). Palantir doesn't use traditional ladders — engineers grow by impact, not title. Entry point is likely similar to L3/E3 at other companies.

**Core pitch — lead with systems depth, not AI/ML:**
> "I've shipped C++ IPC at Chrome scale (3B+ users, sub-50ms p99, Protocol Buffers schema evolution) and operated distributed production systems at TiMoto (gRPC, multi-AZ ECS, circuit breakers, 99.9% uptime). I don't have Elasticsearch or Cassandra production experience, but I have the systems thinking: you design for the failure modes first, then build the happy path."

**On Java gap:**
> "My production languages are C++ and Python — both listed in your requirements. I've built systems at Chrome scale in C++. Java's garbage collection and concurrency model are well-documented; I can ramp in weeks. The hard part of infrastructure engineering isn't the language — it's understanding linearizability, exactly-once semantics, and when to sacrifice consistency for availability."

**On clearance (must clarify):**
> "I'm F-1 — I can't obtain a US security clearance. I want to confirm upfront: is this role on the Foundry commercial track, and is security clearance eligibility a requirement for this team's work or career path? I want to make sure we're aligned before going further."

**On Palantir's mission:**
> "The clearance constraint aside, what draws me to Palantir Infrastructure is the quality bar. The code you write here powers intelligence analysts and aerospace engineers and economic forecasters simultaneously. That's a different kind of correctness requirement than most SaaS backends. I want to work at that bar."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Palantir stated base | $135,000–$200,000 + RSUs + sign-on |
| Palantir public stock (PLTR) | Liquid — RSUs vest over 4 years; current PLTR market cap ~$100B+ (2026) |
| NYC infra SWE (mid-level, 2026) | $170K–$250K TC (Levels.fyi for Palantir) |
| Palantir SWE Levels.fyi NYC | Base: $155K–$190K; TC: $200K–$280K with equity |
| Harry target | $150K–$200K base |
| Harry minimum | $140K walk-away |

Base floor ($135K) is below minimum. However, Palantir SWE total comp with liquid RSUs + sign-on typically pushes NYC TC to $200K–$240K at this level. The lever is equity, not base. Accept if TC is at target even if base is slightly below; negotiate base toward $155K+ and use competing offers.

Sources: [Palantir H-1B data — h1bgrader.com](https://h1bgrader.com/h1b-sponsors/palantir-technologies-inc-g101og8k75) | [Levels.fyi — Palantir NYC](https://www.levels.fyi/companies/palantir/salaries/software-engineer/locations/new-york-city-area)

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Skills: row order | ML & AI or Distributed Systems leads | Distributed Systems leads, then Systems-focused Languages (C++ first) | Palantir infra is pure systems engineering; AI/ML row less relevant |
| 2 | Languages | Python or Go first | C++, Go, Python, Rust, Java first | C++ is the primary evidence for Palantir-tier systems engineering; Go from Pulumi OSS; Rust is in the JD |
| 3 | TiMoto bullets | LLM-heavy | Lead with distributed systems: gRPC deadlock fix, multi-AZ + circuit breakers, vLLM infra (serving engine = distributed compute) | Palantir infra cares about distributed systems correctness, not LLM product features |
| 4 | Chrome bullets | TypeScript/React or C++ IPC | Lead with C++ IPC: "Designed C++ IPC transport layer with Protocol Buffers — selected for schema evolution and cross-language compatibility; shipped to Chrome stable serving 3B+ users at sub-50ms p99, 10K+ req/sec" | C++ at Chrome scale is the strongest systems signal for Palantir |
| 5 | Pulumi project | TypeScript/IaC framing | Lead with Go + distributed systems: "Submitted Go CLI features; analyzed Raft/Paxos consensus in distributed state synchronization layer — studied linearizability guarantees and correctness under concurrent operations" | Raft/Paxos directly maps to Palantir's distributed storage work |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Distributed systems correctness | TiMoto gRPC deadlock fix | Production deadlock under concurrent gRPC calls — system stops working silently | Restore 100% evaluation success rate | Traced shared resource acquisition across two services; identified lock ordering violation; redesigned call sequencing with explicit lock hierarchy | Zero recurrence at production traffic | Debugging distributed deadlocks starts with drawing the happens-before graph — the bug is always at the intersection of two concurrent paths you didn't model |
| 2 | High-availability systems | TiMoto multi-AZ + circuit breakers | 3-person team, no SRE, needed production-grade HA without operational overhead | 99.9% uptime with $40–60/month infra cost | Multi-AZ ECS Fargate, Terraform IaC, circuit breaker (fail-open with health check), CloudWatch alerting, auto-rollback policy | 44% cost reduction; zero unplanned downtime | HA is an architecture property, not an ops property — you can't on-call your way out of a single point of failure |
| 3 | C++ systems at scale | Chrome C++ IPC + Protocol Buffers | Chrome settings needed a new IPC transport layer for cross-process data sharing | Ship to stable channel (3B+ users, sub-50ms p99, 10K+ req/sec) | Evaluated Protocol Buffers vs custom serialization; chose Protobuf for schema evolution and cross-language compatibility; designed the layer; code-reviewed by senior Chrome engineers | Adopted into production Chrome branch | The right serialization format decision isn't about performance — it's about what happens when the schema needs to change 2 years from now. Custom serialization fails that test; Protobuf passes it |
| 4 | Container orchestration / infrastructure automation | TiMoto Terraform + ECS | Manual AWS infra was fragile, non-reproducible, and expensive | Reproducible infra-as-code with auto-scaling, health checks, rollback | Terraform ECS Fargate with multi-AZ, auto-scaling policies, CloudWatch-triggered rollback, K8s (EKS) for ML workloads | 44% cost reduction; zero config drift | Infrastructure code should be boring to operate and interesting to read — the surprising complexity belongs in the comments, not in the resource graph |
| 5 | Open-source + distributed state | Pulumi Raft/Paxos study | Pulumi's distributed state synchronization layer needed contributions; studied correctness guarantees | Go CLI contributions under review by core maintainers; Raft/Paxos analysis published | Analyzed Raft/Paxos consensus: linearizability, leader election, log replication, correctness under partial failures; submitted Go CLI features | OSS contributions under active review | The hardest distributed systems bugs aren't in the happy path — they're in the 4-node partial partition scenario you can't reproduce in a test. Reading Raft taught me to design for that scenario first |
| 6 | Performance and observability | Chrome lock-free trie | Settings navigation p99 at 1,200ms — a daily-use feature affecting billions of users | 96% latency reduction, zero production regressions | Profiled with Chrome perf tooling; identified mutex contention as root cause; replaced with lock-free concurrent trie | sub-50ms settings navigation | Profile before you optimize. Every latency problem looks like a CPU problem until you find the lock acquisition order in the perf trace |

**Red-flag questions:**
- *"What's your security clearance status?"* → "I'm F-1 — security clearances aren't available to F-1 visa holders. I've already flagged this with the recruiter and confirmed this role is on the Foundry commercial track without clearance requirement. If that changes, I'd need to know early."
- *"Java experience?"* → "My production systems work is C++ (Chrome IPC, lock-free data structures) and Python (Django/FastAPI APIs). I have Java in my skills set. The systems thinking — memory management, concurrency, latency tradeoffs — transfers; the syntax and GC model I ramp on in weeks. I'd rather ship one correct C++ program than five Java programs with hidden GC pauses."
- *"Comp expectations?"* → "For a NYC infrastructure role at this level, I'm targeting $160K–$185K base plus equity. I have competing offers in that range. Palantir's public RSUs matter to me — I'd like to understand the equity grant size alongside base."
- *"NYC relocation?"* → "Fully open to relocation. Palantir NYC is a strong enough role to make the move. No timeline conflicts."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active on Lever | Positive |
| Comp disclosed | $135K–$200K base + RSUs + sign-on explicitly stated | Positive |
| Company status | Palantir — NYSE: PLTR, ~$100B+ market cap (2026); Foundry + Gotham deployed globally for defense, intelligence, commercial enterprise | Positive |
| H-1B | 8 LCAs FY2026, 100% approval rate (h1bgrader.com) | Positive |
| JD specificity | Named technologies (Cassandra, Elasticsearch, Kafka, Kubernetes, Flink, Java, Rust, Go), named responsibilities (search ecosystem, container orchestration, distributed storage) | Positive |
| Fraud warning | Palantir explicitly warns about job offer scams in JD | Positive (meta-signal) |
| Company hiring trajectory | Palantir growing commercial division aggressively in 2025–2026 | Positive |

---

## Keywords extracted

Java, Rust, Go, C++, Python, distributed systems, infrastructure, Cassandra, Elasticsearch, Kafka, Kubernetes, Flink, Spark, storage, auth, search indexing, container orchestration, data processing, backend, API design, performance, observability, high availability, Foundry, Gotham, New York, hybrid, security clearance

---

## Machine Summary

```yaml
company: Palantir
role: Backend Software Engineer, Infrastructure Foundations
date: 2026-06-09
url: https://jobs.lever.co/palantir/fb2d3222-dbd8-4e03-8d39-47b820e9509c
score: 3.4
archetype: Backend / Distributed Systems Engineer + Systems Software Engineer
location: New York City (hybrid) — relocation from Atlanta needed
comp_range: "$135K–$200K base + liquid RSUs + sign-on; NYC TC likely $200K–$240K with equity"
visa_risk: "F-1 — H-1B confirmed (8 LCAs FY2026, 100% approval); CLEARANCE: F-1 ineligible for US security clearance — must confirm Foundry commercial track in first recruiter call"
legitimacy: High Confidence
recommendation: "Conditional apply (3.4/5) — confirm commercial/Foundry track placement before investing. Java gap (C++ and Python are listed alternatives), $135K floor below minimum (but liquid RSU + sign-on bridges gap), clearance concern for F-1. Lead with C++ Chrome scale + distributed systems depth. Negotiate toward $160K+ base."
```
