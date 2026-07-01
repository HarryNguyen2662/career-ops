# 021 — IMC Trading — Software Engineer, Early Career

**Date:** 2026-05-29
**Score:** 4.4/5
**URL:** https://job-boards.greenhouse.io/embed/job_app?for=imc&token=4577504101
**PDF:** ❌
**Legitimacy:** High Confidence

---

## Machine Summary

```yaml
company: IMC Trading
role: Software Engineer, Early Career
date: 2026-05-29
score: 4.4
status: Evaluated
level: Early Career — 1-3 years post-graduation; new grad band at HFT firm
location: Chicago, IL — on-site (relocation from Atlanta required)
comp_base: "$200,000 USD"
comp_bonus: "Discretionary (HFT norm: 50–100%+ of base); Year-1 TC estimate $250K–$300K+"
comp_equity: "Not mentioned — IMC is a private firm"
archetype: "Systems Software / High-Throughput Performance Engineer"
graduation_timing_risk: medium — form may ask degree completion; Harry graduates May 2027
visa_risk: low — IMC Americas: 34 LCAs filed FY2025, 100% approval rate; Software Developer is a sponsored role
apply_rec: "Apply — 4.4/5 above threshold; highest-compensated role in pipeline; C++/performance/algorithms is primary archetype match; disclose degree completion timeline accurately"
```

---

## Selection Rationale

URL submitted directly — no board search required. IMC's early career engineering program targets top CS talent and trains in-house; financial markets knowledge is explicitly not required. This is their pipeline-building role for systems engineers.

---

## Block A — Role Summary

| Dimension | Detail |
|---|---|
| **Archetype** | Systems Software / High-Throughput Backend — trading platform |
| **Domain** | Quantitative / algorithmic trading infrastructure (HFT) |
| **Function** | Build + maintain trading platform and software stack |
| **Seniority** | Early Career — 1-3 years post-graduation |
| **Location** | Chicago, IL — on-site |
| **Preferred languages** | Java or C++ |
| **Team** | Cross-functional with traders, quant researchers, global engineering |
| **TL;DR** | IMC wants a C++/Java systems engineer with deep algorithms/DS fundamentals to build trading platform software — latency, correctness, collaborative culture |

---

## Block B — Match with CV

**Score: 4.2/5**

| JD Requirement | Harry's Evidence | Fit |
|---|---|---|
| **C++ proficiency (preferred)** | Google Chrome: C++ IPC transport layer with Protobuf; lock-free concurrent trie search; 96% latency reduction; shipped to stable serving 3B+ users | ✅ Strong |
| **Algorithms & data structures** | Lock-free trie (concurrent tree); DynamoDB hot-partition redesign (hash distribution); Raft/Paxos analysis; Data Structures coursework | ✅ Strong |
| **Performance / low-latency focus** | Chrome: p99 bottleneck profiled at 1,200ms → 96% reduction; TiMoto: sub-50ms p99 inference; DynamoDB: 30% throughput improvement at 9K+ req/sec | ✅ Strong |
| **Collaborative cross-functional** | Chrome: design docs reviewed by senior engineers; Develop for Good: cross-team BaaS; Pulumi: upstream code review | ✅ |
| **Java (preferred)** | Listed in skills; no production Java evidence in CV | ⚠️ Listed, not demonstrated |
| **1-3 years post-graduation** | ~11 months internship + TiMoto production ownership; technically below floor | ⚠️ Borderline; Google quality compensates |
| **Financial markets interest** | No markets background; CoderPush payment APIs (exactly-once, idempotency) adjacent; JD explicitly says prior experience unnecessary | ⚠️ Zero; JD says not required |
| **BS/MS in CS or Engineering** | In progress — Expected May 2027 | ⚠️ Must disclose |

**Key strength:** The lock-free trie + C++ IPC at Chrome scale is Harry's highest-signal match for an HFT engineering role. IMC filters for exactly this: algorithmic depth meeting production systems constraints.

**Key gap:** No production Java. C++ is present but only from one internship. No financial markets background (JD says not required).

---

## Block C — Level and Strategy

**Level detected:** "Early Career" = IMC's new grad band. HFT firms (IMC, Jane Street, Citadel) deliberately hire from CS programs and train internally — the 1-3yr floor is soft for top candidates.

**Sell-strong plan:**
- Lead with Chrome C++ lock-free trie: most relevant single bullet for HFT systems hiring
- Frame TiMoto concurrency (deadlock fix at sub-50ms p99) as production correctness evidence
- CoderPush: DynamoDB partition redesign at 9K+ req/sec = throughput-oriented systems thinking
- Algorithms depth from coursework + Raft/Paxos study + data structure choices in production

**If downleveled:** Not applicable — Early Career is the entry band. Accept $200K base. Negotiate bonus guarantee if possible.

---

## Block D — Comp and Demand

**Score: 5.0/5**

| Component | Value | vs Target |
|---|---|---|
| Base | **$200,000** | **$60K above walk-away ($140K); top of Harry's stated target ($150K–200K)** ✅ |
| Bonus | Discretionary | HFT norm: 50–100%+ of base. Year-1 conservatively $50K–$100K. |
| Equity | Not mentioned — IMC is private | No liquid equity; offset by base + bonus |
| Benefits | Paid leave, insurance | Standard |

**Year-1 TC estimate: ~$250K–$300K**

IMC is among the top 5 highest-paying engineering employers globally. $200K base for Early Career is the entry point; Senior SWE at IMC is $350K–$500K+ TC. This is the highest-compensated role in Harry's current pipeline.

Sources: Levels.fyi ($288K–$394K+ for US SWE), 6figr ($244K–$309K new grad), official JD ($200K base stated).

---

## Block E — Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---|---|---|---|
| 1 | **Languages (skills)** | Python leads | Move **C++** to position 1 | IMC prefers C++ or Java; C++ is Harry's HFT-signal language |
| 2 | **Google Chrome bullet order** | IPC → observer → lock-free | **Lock-free trie first**, then IPC Protobuf, then observer | Lock-free concurrent data structure is the #1 IMC filter signal |
| 3 | **TiMoto framing** | "ML Serving Platform" | Add **concurrent gRPC deadlock** bullet as first; frame as distributed systems correctness | IMC cares about concurrency correctness; reframe toward systems |
| 4 | **CoderPush** | "payment APIs" | Lead with **"high-throughput data pipeline at 9,000+ req/sec"** | Trading vocabulary aligns; throughput + correctness emphasis |
| 5 | **Skills: Distributed Systems** | gRPC, Protobuf, Circuit breakers... | Add **lock-free data structures** explicitly | Directly named IMC hiring signal |

---

## Block F — Interview Plan

IMC interviews: heavy CS fundamentals (algorithms, data structures, OS), competitive programming-style coding, systems design. No product sense tested.

| # | JD Focus | STAR+R Story | Reflection |
|---|---|---|---|
| 1 | Lock-free / concurrent DS | Chrome: mutex contention identified as p99 bottleneck → lock-free concurrent trie → 96% latency reduction | Measure before redesigning; profiling saved weeks of blind optimization |
| 2 | Performance profiling | Chrome: profiled settings nav to 1,200ms bottleneck; diagnosed contention; zero regressions post-fix | Latency problems concentrate in one place; find it before fixing it |
| 3 | Concurrency correctness | TiMoto: production gRPC deadlock traced to circular resource acquisition; redesigned call sequencing → 100% success rate at sub-50ms p99 | Deadlocks always have ordering patterns; explicit dependency graphs prevent them |
| 4 | High-throughput systems | CoderPush: DynamoDB hot-partition at 9K+ req/sec — access pattern analysis → partition redesign → 30% throughput improvement | Partition key choice is irreversible; get it right before needing to change it |
| 5 | Exactly-once / correctness | CoderPush: idempotent payment APIs with Redis (85% hit rate) + exponential backoff → exactly-once under network partitions | Idempotency keys are cheap; duplicate transactions are expensive — obvious in hindsight |
| 6 | Protocol / schema design | Chrome: Protobuf over custom serialization — schema evolution + zero-copy IPC at 10K+ req/sec | Serialization is a long-term contract; design for evolution from the start |
| 7 | Production SLOs / ownership | TiMoto: multi-AZ ECS + circuit breaker + Terraform IaC → 99.9% uptime, 44% cost reduction | Circuit breakers are useless without metrics to trigger them; observability first |

**Case study:** Chrome lock-free trie — algorithmic problem-solving at production scale, zero regressions.

**Red-flag questions:**
- *"No production Java"* → "My production C++ is from Chrome (3B+ users). Java/C++ share the core concurrency primitives I've used — lock-free structures, memory models. I ramp on idioms quickly."
- *"Interested in finance/trading?"* → "I'm drawn to the engineering constraints — low-latency, concurrency correctness, systems that can't fail. Trading makes those constraints harder and therefore more interesting."
- *"Still in school"* → "Graduating May 2027. I've been shipping at production scale while finishing — Chrome stable channel, TiMoto sole engineer. Starting May 2027."

---

## Block G — Posting Legitimacy

**Tier: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Posting active | Live Greenhouse form + imc.com careers page; full JD | Positive |
| Salary transparency | $200,000 base explicitly stated — rare for a private firm | Positive |
| JD specificity | Named preferences (Java/C++, algorithms/DS, 1-3 years); not generic boilerplate | Positive |
| Company health | IMC is a highly profitable private HFT firm; no layoffs; global hiring | Positive |
| H-1B sponsorship | IMC Americas: 34 LCAs FY2025, 100% approval rate; Software Developer is sponsored role | Positive |
| Role-company fit | Early Career SE at HFT = canonical new grad pipeline posting | Positive |

Real, active posting. No ghost signals.

---

## Global Score

**4.4/5 — Apply**

| Dimension | Score | Driver |
|---|---|---|
| CV Match | 4.2 | C++ lock-free + performance + DS = strong; no production Java; experience gap |
| North Star | 4.0 | Systems Software / Performance is primary archetype; trading domain new but JD says not required |
| Compensation | 5.0 | $200K base; $250K–$300K+ Year-1 TC; highest in current pipeline |
| Culture | 4.0 | Top HFT firm; H-1B sponsors (100% approval); Chicago onsite; meritocratic engineering culture |
| Red flag adj. | -0.3 | Degree in progress (-0.1); experience gap (-0.1); no production Java (-0.1) |
| **Global** | **4.4** | |

**Recommendation: Apply.**

This is the highest-compensated role in Harry's current pipeline. The C++/lock-free/performance angle is primary archetype. IMC's H-1B record is the cleanest of any company evaluated (100% approval, active filings). Chicago onsite requires relocation — Harry is open to this.

**Framing:** Lead with Chrome lock-free trie + C++ Protobuf IPC. Back with TiMoto concurrency (deadlock fix). Frame CoderPush as throughput engineering (9K+ req/sec). Do not lead with ML/vLLM — not relevant here.
