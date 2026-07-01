# Evaluation: Google — Software Engineer, Parallel File Systems, AI/ML Storage

**Date:** 2026-06-12
**URL:** https://www.google.com/about/careers/applications/jobs/results/81021783544603334-software-engineer/
**Archetype:** Backend / Distributed Systems Engineer + Performance Engineer + ML / AI Infrastructure Engineer
**Score:** 3.5/5
**Legitimacy:** High Confidence
**PDF:** output/123-google-software-engineer-parallel-file-systems-harry-nguyen-2026-06-12.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Distributed Systems / Storage Infrastructure — build next-generation cloud storage for extreme-scale AI/ML workloads; file system APIs, multi-petabyte distributed systems, performance engineering, cost optimization |
| Domain | Google Cloud — Parallel File Systems, AI/ML Storage; building cloud file storage tailored for generative AI (pre-training, training, RL, inferencing) at up to 10TB/s throughput |
| Function | Build — file system APIs, distributed storage at multi-petabyte scale, data protection (snapshots, backups), performance tooling, cost reduction |
| Seniority | Mid, L3–L4 — "2 years" minimums all OR'd (Golang/Java/C++ OR large-scale infra/distributed systems OR general software development); borderline for Harry's timeline but the OR structure is favorable |
| Location | Seattle, WA |
| Comp | **$147,000–$211,000 base + 15% bonus + equity** — same L3/L4 Google band as #120 |
| Company | Google Cloud — Parallelstore product (GA since 2024) expanding to next-gen AI/ML storage; Parallel File Systems team is building the storage infrastructure for Google's own AI training and inference workloads at scale |
| TL;DR | Genuine fit on distributed systems + performance engineering + C++/Go; storage domain gap is real (no file system background) but distributed systems OR satisfies minimum quals; unique differentiator: Harry built the AI/ML inference workloads this storage needs to serve. Score 3.5 — apply with honest framing on the ML/storage angle. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|-------------|----------|
| **Bachelor's degree or equivalent** | Georgia State BS CS, GPA 3.75, Expected May 2027 | ✅ Direct |
| **2 years programming with Golang, Java, or C++** | Chrome: C++ IPC transport + lock-free trie (3-month internship at Google's standard); Pulumi: Go CLI contributions; both listed prominently in cv.md | ⚠️ Soft gap — strong evidence but ~3–6 months per language vs 2 years production; former intern mitigates |
| **2 years large-scale infrastructure, distributed systems, or storage systems** | TiMoto: gRPC exactly-once, multi-AZ ECS Fargate, circuit breakers, 99.9% uptime SLO (~9 months non-internship); Chrome: 3B+ user scale — distributed systems axis satisfied; storage systems axis: no file system or storage background | ⚠️ Distributed systems ✅; storage systems ❌ (no file system experience); same timeline constraint as #120 |
| **2 years software development or 1 year with advanced degree** | TiMoto ~9 mo + Chrome 3 mo + Develop for Good 3 mo = ~15 months total professional | ⚠️ Borderline — identical to #120 AI-Empowered Security (3.8 approved) |
| **Build and launch APIs for file systems** | TiMoto: gRPC service-to-service APIs + Django/FastAPI REST; Develop for Good: AWS BaaS APIs for 500+ concurrent users | ✅ API design present; file system APIs specifically are new domain |
| **Design distributed systems at multi-petabyte scale** | TiMoto: gRPC exactly-once, multi-AZ, deadlock diagnosis, circuit breakers; Pulumi: Raft/Paxos consensus literacy | ✅ Distributed systems discipline is core pitch; multi-petabyte absolute scale is aspirational |
| **Investigate bottlenecks, deliver performance improvements** | Chrome: 1,200ms → sub-50ms (96% latency reduction) via lock-free CAS on critical path; TiMoto: KV cache memory fragmentation → zero OOM; Develop for Good: N+1 → sub-100ms | ✅ **Strong** — performance engineering is a signature strength with quantified proof points |
| **Implement optimizations to reduce cost** | TiMoto: 44% infrastructure cost reduction ($40–60/mo); Terraform right-sizing; circuit breaker preventing cost spikes from failure cascades | ✅ Quantified cost engineering |
| **Data protection: snapshots, backups, security** | No experience with file system snapshots, storage-layer backup systems, or storage security primitives | ❌ Storage domain gap |
| **C++ or Go preferred** | Chrome: C++ IPC transport + lock-free trie at Google's standard; Pulumi: Go CLI features | ✅ Both present; depth is the soft gap |
| **AI/ML workloads (pre-training, training, RL, inferencing)** | TiMoto: vLLM/PagedAttention production LLM serving; KV cache optimization under concurrent inference load; continuous batching throughput engineering | ✅ **Unique differentiator** — Harry knows exactly what this storage needs to support from the consumer side |
| **Data structures and algorithms preferred (2 yrs)** | Chrome: lock-free trie + CAS; Pulumi: Raft/Paxos analysis; coursework: Data Structures | ✅ Present, partially academic |
| Master's/PhD (preferred) | Undergrad, May 2027 | ❌ Preferred miss |
| Accessible technologies (preferred) | None | ❌ Preferred miss |

**Gaps:**

1. **Storage systems domain (moderate gap, primary):** This role is explicitly about file systems — POSIX semantics, snapshot/backup mechanisms, storage-layer security, data protection. Harry has zero direct experience here. The JD's "OR distributed systems" minimum qualification saves him on the baseline, but the role's day-to-day work has significant storage-specific learning curve.

2. **Experience years (soft gap, same as #120):** 2-year minimums on all three paths vs Harry's ~15 months. Google applies judgment for strong candidates — flagged in #120 (score 3.8) with the same framing and approved. Apply here with identical handling.

3. **C++/Go depth:** Chrome C++ is 3-month internship; Pulumi Go is open-source contributions. Strong signal, not sustained production use at 2 years.

4. **Multi-petabyte scale:** Harry's largest scale context is Chrome's 3B+ users (code correctness, not throughput) and TiMoto's concurrent production load (~99.9% uptime). The absolute scale of 10TB/s is beyond current experience — methodology transfers, absolute numbers don't.

---

## C) Level and Strategy

**Level detected:** L3–L4 — same comp range ($147K–$211K base) and "Mid" filter as #120. This is the standard Google new-hire band.

**The AI/ML storage angle (core differentiator):**
> "I've been on the other side of this stack — I built production LLM inference infrastructure at TiMoto: vLLM with PagedAttention, KV cache management under concurrent load, continuous batching to maximize throughput. I understand what AI/ML workloads demand from storage because I've hit the limits where storage becomes the bottleneck. I want to build the storage layer that makes inference fast."

**Distributed systems + performance framing:**
> "My gRPC deadlock diagnosis taught me that concurrent systems correctness requires understanding the full call graph — the same discipline applies to building linearizable file system APIs. My Chrome performance work (profiled 1,200ms to find mutex contention, redesigned with lock-free CAS for 96% reduction) is exactly 'investigate bottlenecks, deliver performance improvements' in practice."

**Former intern advantage:** Harry passed Google's code review bar in C++ on a production codebase (Chrome). That's directly relevant for a C++ file system engineering role at Google.

**If asked about storage domain gap:**
> "File systems are new to me — I haven't built POSIX-layer storage, snapshot systems, or storage-layer security. What I bring is the performance engineering methodology (profile → identify root cause → quantified fix), distributed systems correctness thinking (exactly-once, fault tolerance, linearizability), and direct knowledge of the AI/ML workloads this storage needs to serve. The domain-specific storage knowledge is learnable from this team; the systems thinking and performance discipline are harder to develop."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Google stated base | $147,000–$211,000 |
| Bonus | 15% target (~$22K–$32K at midpoint) |
| Equity (L3 RSU) | ~$100K–$200K/4yr at L3; higher at L4 |
| Estimated TC | **$200K–$280K** at L3/L4 (Levels.fyi Google L3 median ~$211K TC) |
| Harry target | $150K–$200K TC |
| Harry minimum | $140K |
| Assessment | Strongly meets target — identical comp band as #120. Base alone plus 15% bonus exceeds Harry's $200K ceiling before equity. Outstanding for new grad level. |
| Google H-1B | Google sponsors H-1B. Seattle-based Google Cloud teams have historically strong sponsorship track record. F-1 OPT → H-1B path viable. |
| AI/ML storage demand | Google Cloud Parallelstore entered GA in 2024; next-gen AI/ML storage is a stated strategic priority. Parallel File Systems team is building infrastructure for Google's own AI training at scale. High hiring demand. |

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto lead bullet | Varies | **Lead with concurrent systems + performance**: gRPC deadlock diagnosis → redesigned call sequencing → 100% success rate at sub-50ms p99 | JD: "Investigate bottlenecks, deliver performance improvements" — this is exactly that pattern; shows correctness under concurrency |
| 2 | TiMoto second bullet | ML serving | Infrastructure reliability + cost optimization: multi-AZ Fargate + circuit breaker + Terraform + 99.9% uptime + 44% cost reduction | JD: "Design distributed systems"; "Implement optimizations to reduce cost" |
| 3 | TiMoto third bullet | Observability | AI/ML workload framing: vLLM/PagedAttention — connects Harry to the storage consumer perspective | JD: "AI/ML includes... inferencing" — unique angle this team won't see from other candidates |
| 4 | Chrome lead bullet | IPC transport first | **Lead with lock-free CAS performance**: profiled 1,200ms bottleneck → lock-free trie → 96% latency reduction | Performance engineering is JD's primary responsibility; demonstrates the exact methodology |
| 5 | Chrome second bullet | Lock-free trie | C++ IPC transport + Protocol Buffers at Google's standard → 3B+ users, sub-50ms p99 | C++/Go requirement; former intern credibility at Google's code bar |
| 6 | Skills row order | Various | **Distributed Systems first** (gRPC, exactly-once, circuit breakers, Raft/Paxos); Languages second (C++/Go/Python prominent); Cloud & Infrastructure; ML & AI; Frameworks; AI Dev Tools last | Role core = distributed systems + C++/Go; recruiter scans these first |

---

## F) Interview Plan

| # | JD Area | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Investigate bottlenecks, performance improvements | Chrome lock-free trie optimization | Chrome settings navigation at 1,200ms p99 — affecting 3B+ users on every settings interaction | Find and fix root cause without regression risk | Profiled critical path; identified mutex contention in trie search; designed lock-free implementation with CAS operations; validated zero regressions at 95% test coverage | 96% latency reduction; adopted by senior Chrome engineers; zero production regressions | Performance engineering for file systems follows the same methodology — profile the hot path (metadata lookup, I/O scheduling, buffer management), identify contention, redesign for concurrent correctness. The specific data structure changes; the approach doesn't. |
| 2 | Distributed systems correctness under concurrency | TiMoto gRPC deadlock diagnosis | Production deadlock under concurrent gRPC calls — system hung under load | Find root cause of concurrent failure and redesign for exactly-once correctness | Traced shared resource acquisition conflicts via production telemetry; redesigned call sequencing for exactly-once delivery | 100% evaluation success rate; sub-50ms p99; zero deadlocks post-fix | Exactly-once semantics in file system APIs is critical — concurrent writers need linearizable guarantees. My gRPC work taught me that concurrent system correctness requires modeling the full call graph, not just individual locks. Same discipline for concurrent file system metadata operations. |
| 3 | Cost optimization + infrastructure design | TiMoto Terraform + circuit breaker infrastructure | Production infrastructure over-provisioned with no auto-recovery | Architect for reliability and cost efficiency simultaneously | Multi-AZ ECS Fargate with circuit breaker pattern and auto-rollback on health check failure; right-sized via CloudWatch alarms; Terraform IaC | 44% cost reduction ($40–60/mo); 99.9% uptime SLO; zero manual intervention on health failures | Storage cost optimization at Google's scale requires the same discipline — right-size the storage tier (SSD vs HDD vs cold), automate data lifecycle, prevent over-provisioning. My approach: measure → set targets → automate enforcement. |
| 4 | Build APIs for distributed systems | TiMoto + Develop for Good + Chrome IPC | Needed reliable APIs across different scales: service-to-service, public HTTP, cross-process | Design APIs for concurrency correctness + horizontal scale + schema evolution | gRPC with exactly-once semantics (TiMoto); JWT stateless BaaS 500+ concurrent users (Develop for Good); Protocol Buffers with schema evolution analysis (Chrome IPC) | Sub-50ms p99 gRPC; 500+ concurrent users on BaaS; shipped Chrome IPC to stable for 3B+ users | File system API design faces the same challenges — schema evolution (clients must not break on storage API changes), exactly-once writes (write once, visible once), concurrent access ordering. Protobuf's schema evolution lesson applies directly. |
| 5 | AI/ML workloads (unique angle) | TiMoto vLLM/PagedAttention | Production LLM serving had OOM failures under concurrent inference load | Deploy production-grade ML inference without memory fragmentation | Evaluated vLLM's PagedAttention design (OS virtual memory analogy for attention weights); deployed with continuous batching; benchmarked KV cache utilization vs naive HF inference | Zero OOM failures at production traffic; quantified throughput improvement; sub-50ms inference SLO | I built the inference layer that depends on storage like this. When vLLM does KV cache paging, it's making virtual-to-physical mapping decisions for attention weights — the same I/O patterns Parallel File Systems needs to optimize. I understand storage access patterns for AI inference from the inside. |

**Recommended case study:** Chrome lock-free trie + TiMoto gRPC deadlock as a "how I approach distributed performance problems" narrative. Show the methodology: observe symptoms → profile the critical path → identify the concurrency root cause → redesign for correctness → validate with quantified results. This covers both JD axes: performance improvements and distributed systems correctness.

**Red-flag questions:**
- *"No file system or storage background."* → "Correct — file system semantics (POSIX, snapshot/backup mechanisms) are new for me. What I bring is the performance engineering methodology and distributed systems correctness discipline. I also bring something few candidates will have: I've built the AI/ML inference workloads that depend on storage like this. I understand the access patterns, latency requirements, and throughput demands of LLM training and inference from direct production experience."
- *"2 years experience required, you have 15 months."* → "15 months with real production ownership: on-call rotation, incident response, runbooks, post-mortems at TiMoto. At May 2027 graduation I'll be at 24 months. The density of that experience — debugging production deadlocks, diagnosing OOM failures under load, shipping to 3B+ Chrome users — compresses the equivalent of more time at typical internship-only backgrounds."
- *"Work authorization?"* → "F-1 — OPT at graduation (May 2027), H-1B long-term. Can you confirm Google Cloud's sponsorship policy for this team?"
- *"Why storage specifically?"* → "I came at it from the AI/ML inference side — I've been optimizing KV cache paging and continuous batching throughput, and storage kept appearing as the next constraint. Parallel File Systems at 10TB/s is the infrastructure that makes AI/ML at scale possible. I want to build the layer I've been depending on."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active "Apply" on Google Careers — confirmed via Playwright snapshot | Positive |
| Comp disclosed | $147,000–$211,000 + 15% bonus + equity — transparent | Positive |
| WA state benefits disclosure | Full Washington state benefits package legally disclosed — confirms active Seattle posting with compliance | Positive |
| JD specificity | Named team (Parallel File Systems, AI/ML Storage), specific throughput target (10TB/s), specific workload types (pre-training, RL, inferencing), specific data protection scope (snapshots, backups, security) | Positive |
| Google Cloud AI/ML storage strategy | Google Cloud Parallelstore (POSIX parallel file system for AI/ML) entered GA in 2024 at Google Cloud Next; this team is building the next generation of that product | Positive |
| "Mid" filter + comp range | Signals real hiring intent for junior/mid engineers, not a senior-only search | Positive |

**Context:** Google Cloud Parallelstore was publicly announced at Google Cloud Next 2024 and has been in GA. The Parallel File Systems team is now expanding. The explicit AI/ML workload focus, 10TB/s throughput target, and data protection scope are all consistent with what Google has publicly described for Parallelstore's next-generation roadmap. No concerns — this is a real, active, high-priority hiring effort.

---

## Keywords extracted

Software Engineer, Parallel File Systems, AI/ML Storage, Google Cloud, distributed systems, storage systems, Golang, Go, C++, Java, large-scale infrastructure, performance engineering, throughput, multi-petabyte, data protection, snapshots, backups, cost optimization, AI/ML workloads, pre-training, inferencing, file systems, Seattle, Parallelstore

---

## Machine Summary

```yaml
company: Google
role: "Software Engineer, Parallel File Systems, AI/ML Storage"
date: 2026-06-12
url: https://www.google.com/about/careers/applications/jobs/results/81021783544603334-software-engineer/
score: 3.5
archetype: "Backend / Distributed Systems + Performance Engineer + ML / AI Infrastructure"
location: "Seattle, WA"
comp_range: "$147,000–$211,000 base + 15% bonus + equity; TC ~$200K–$280K at L3/L4; strongly meets Harry's $150K–$200K target"
visa_risk: "F-1 — Google Cloud sponsorship historically strong; Seattle office; lower risk than consumer product teams"
legitimacy: High Confidence
recommendation: "Apply (3.5/5) — genuine fit on distributed systems + performance engineering + C++/Go; storage domain gap is real (no file system background) but distributed systems OR satisfies minimum quals; unique angle: Harry built the AI/ML inference workloads this storage serves. Same experience-year gap as #120 (3.8 approved). Frame: performance engineer who understands the full stack from storage consumer (vLLM/PagedAttention) to infrastructure (distributed systems). Generate LaTeX CV."
```
