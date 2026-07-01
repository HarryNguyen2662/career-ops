# 057 — IMC Trading — Software Engineer, Early Career

**Date:** 2026-06-04
**URL:** https://job-boards.eu.greenhouse.io/imc/jobs/4577504101
**Archetype:** Systems Software / High-Throughput Performance Engineer
**Score:** 4.4/5
**Legitimacy:** High Confidence
**PDF:** ✅

---

> **Re-evaluation note:** This is the same posting as report #021 (2026-05-29), now surfaced on the EU Greenhouse domain (`job-boards.eu.greenhouse.io`). Job token `4577504101` and all JD content are identical. Location is Chicago, United States. The EU domain likely reflects IMC's global ATS routing — the role is unchanged. Primary purpose of this re-evaluation: confirm liveness, generate LaTeX CV (missing from #021), and refresh report for pipeline tracking.

---

## Machine Summary

```yaml
company: IMC Trading
role: Software Engineer, Early Career
date: 2026-06-04
score: 4.4
status: Evaluated
level: Early Career -- 1-3 years post-graduation; new grad band at HFT firm
location: Chicago, IL -- on-site (relocation from Atlanta required)
comp_base: "$200,000 USD"
comp_bonus: "Discretionary (HFT norm: 50-100%+ of base); Year-1 TC estimate $250K-$300K+"
comp_equity: "Not mentioned -- IMC is a private firm"
archetype: "Systems Software / High-Throughput Performance Engineer"
graduation_timing_risk: medium -- form asks degree completion; Harry graduates May 2027
visa_risk: low -- IMC Americas: 34 LCAs filed FY2025, 100% approval rate; Software Developer is a sponsored role
apply_rec: "Apply -- 4.4/5 above threshold; highest-compensated role in pipeline; C++/lock-free/systems fit; disclose degree timeline accurately"
prior_report: "021 (2026-05-29) -- same posting, US Greenhouse domain"
url_change: "US domain -> EU domain; same token 4577504101; content unchanged"
```

---

## A) Role Summary

| Dimension | Detail |
|---|---|
| **Archetype** | Systems Software / High-Throughput Backend -- trading platform |
| **Domain** | Quantitative / algorithmic trading infrastructure (HFT) |
| **Function** | Build + maintain trading platform and software stack |
| **Seniority** | Early Career -- 1-3 years post-graduation |
| **Location** | Chicago, IL -- on-site |
| **Remote** | On-site only |
| **Preferred languages** | Java or C++ |
| **Team** | Cross-functional with Traders, Quant Researchers, global engineering |
| **TL;DR** | IMC wants a C++/Java systems engineer with deep algorithms/DS fundamentals to build trading platform software -- latency, correctness, collaborative culture |

---

## B) Match with CV

**Score: 4.2/5**

| JD Requirement | Harry's Evidence | Fit |
|---|---|---|
| **C++ proficiency (preferred)** | Google Chrome: C++ IPC transport layer with Protobuf; lock-free concurrent trie search; 96% latency reduction; shipped to stable (3B+ users, sub-50ms p99, 10K+ req/sec) | Strong |
| **Algorithms & data structures** | Lock-free trie (concurrent tree structure); Raft/Paxos analysis in Pulumi contribution; Data Structures coursework; DynamoDB hot-partition redesign | Strong |
| **Performance / low-latency focus** | Chrome: p99 bottleneck at 1,200ms profiled + 96% reduction; TiMoto: sub-50ms p99 inference; gRPC deadlock traced and resolved under concurrent load | Strong |
| **Collaborative, cross-functional** | Chrome: design docs reviewed by senior engineers; Develop for Good: cross-team delivery; Pulumi: upstream code review with core maintainers | Strong |
| **Java (preferred)** | Listed in skills; no production Java evidence in CV | Listed, undemonstrated |
| **1-3 years post-graduation** | ~11 months of internship + TiMoto production ownership; technically below stated floor | Borderline -- Google quality compensates |
| **BA/BSc in CS or Engineering** | In progress -- Expected May 2027 | Must disclose |
| **Financial markets interest** | No background; JD explicitly says NOT required | Non-issue per JD |

**Gaps and mitigations:**

1. **No production Java** -- Hard blocker? No. C++ shares the same concurrency primitives IMC cares about (lock-free structures, memory models). Mitigation: frame Java as readable (coursework), emphasize C++ depth as primary.
2. **Experience below 1-year floor** -- Not a hard blocker for HFT firms that hire from CS programs. Mitigation: Google Chrome production quality at 3B+ users lifts credibility above year-count.
3. **Degree in progress** -- Disclose proactively on form. IMC asks explicitly. Start date May 2027 is consistent with early-career cohort.

---

## C) Level and Strategy

**Level detected:** "Early Career" = IMC's new grad entry band. HFT firms train internally; the 1-3 year floor is soft for top candidates with strong CS fundamentals and production exposure.

**Sell-strong plan:**
- Lead with Chrome lock-free trie: algorithmic depth + production systems + zero regressions = the IMC filter in one bullet
- Frame TiMoto gRPC deadlock fix as concurrency correctness evidence
- Pulumi: Raft/Paxos study signals distributed systems literacy beyond coursework
- Do NOT lead with ML/vLLM -- irrelevant here; trading engineers care about latency, correctness, algorithms

**If downleveled:** Not applicable -- Early Career is the entry band. Accept $200K base. If possible, negotiate a bonus guarantee for Year 1 (HFT norms: 50-100%+ of base as discretionary).

**Application form notes:**
- Immigration sponsorship: answer "Yes" to both questions (F-1 now, H-1B long-term)
- Programming languages: check Java, C++, Python
- Degree in progress: confirm it lists BSc Computer Science, Expected May 2027
- Offers: answer accurately (N/A if none current)

---

## D) Comp and Demand

**Score: 5.0/5**

| Component | Value | vs Harry's Target |
|---|---|---|
| Base | **$200,000** | At ceiling of target ($150K-$200K) -- exactly at top |
| Bonus | Discretionary | HFT norm: 50-100%+ of base. Year-1 conservatively $50K-$100K |
| Equity | Not mentioned -- IMC is private | Offset by cash base + bonus |
| Benefits | Paid leave, insurance, benefits page linked | Standard |

**Year-1 TC estimate: $250K-$300K+**

IMC is among the top 5 highest-paying engineering employers globally. $200K base for Early Career is the floor; Senior SWE at IMC is $350K-$500K+ TC. This is the highest-compensated role in Harry's current pipeline.

Sources: Levels.fyi ($288K-$394K+ for US SWE), 6figr ($244K-$309K new grad), JD ($200K base stated explicitly).

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---|---|---|---|
| 1 | **Languages (skills row)** | Python listed before C++ | Move C++ to position 1 | IMC prefers C++ or Java; C++ is the HFT signal language |
| 2 | **Google Chrome bullet order** | IPC Protobuf leads | **Lock-free trie first**, then IPC Protobuf, then observer | Lock-free concurrent data structure is the #1 IMC hiring signal |
| 3 | **TiMoto framing** | "ML Serving Platform" emphasis | Add gRPC deadlock diagnosis bullet as first TiMoto bullet; frame as distributed systems correctness | IMC cares about concurrency correctness -- reframe toward systems |
| 4 | **Skills: Distributed Systems** | gRPC, Protobuf, circuit breakers... | Add "lock-free data structures" explicitly | Directly named IMC hiring signal; currently absent from skills row |
| 5 | **Professional summary (if added)** | None | "CS @ GSU (GPA 3.75, May 2027) -- Google Chrome C++ intern (lock-free structures, IPC at 3B-user scale) -- primary engineer for distributed ML serving at TiMoto AI. Targeting systems/backend roles where performance and correctness are non-negotiable." | Anchors recruiter scan on Chrome C++ and production systems, not ML |

---

## F) Interview Plan

IMC interviews: CS fundamentals (algorithms, data structures, OS), competitive-programming-style coding, systems design. No product sense tested.

| # | JD Focus | Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Lock-free / concurrent DS | Chrome: mutex contention → lock-free trie | Settings nav was p99 bottleneck at 1,200ms; no one had profiled it | Redesign the search trie to eliminate mutex contention | Lock-free concurrent trie with atomic compare-and-swap | 96% latency reduction, zero production regressions | Measure before redesigning; profiling saved weeks of blind optimization |
| 2 | Concurrency correctness | TiMoto: production gRPC deadlock | Two services acquiring shared resource in reverse order under concurrent calls | Trace shared resource acquisition sequences across call graph | Redesigned call sequencing to enforce consistent lock ordering | 100% evaluation success rate at sub-50ms p99 | Deadlocks always have ordering patterns; explicit dependency graphs prevent them |
| 3 | Performance profiling | Chrome: settings nav profiling | No profiling data existed for settings search path | Identify bottleneck before committing to a fix | CPU profiling traced hot path to mutex in trie traversal | Root cause confirmed in 2 hours; fix targeted and correct | Latency problems concentrate in one place -- find it before touching anything |
| 4 | High-throughput design | Google IPC transport layer | Chrome needed cross-process communication at 10K+ req/sec with schema evolution | Design IPC serialization format for a stable ABI | Chose Protocol Buffers over custom serialization for schema evolution + cross-language compat | Shipped to Chrome stable serving 3B+ users at sub-50ms p99 | Serialization is a long-term contract; design for evolution from the start |
| 5 | Algorithms / data structures | Pulumi: Raft/Paxos study | Analyzing distributed state sync layer in a 24K-star project | Understand linearizability guarantees under partial failures | Studied Raft consensus and correctness invariants in production Go code | Documented correctness properties for multi-cloud provisioning | Understanding why an algorithm is correct is harder -- and more useful -- than knowing the steps |
| 6 | Production correctness / SLOs | TiMoto: 99.9% uptime | Multi-AZ infra with no auto-recovery mechanism initially | Design a system that recovers from partial failures without manual intervention | Terraform IaC + ECS Fargate + circuit breaker + health-check auto-rollback | 99.9% uptime, 44% cost reduction ($40-60/month) | Circuit breakers are useless without metrics to trigger them -- observability is not optional |
| 7 | Collaborative delivery | Chrome: design docs + code review | 25K+ lines of Chromium, working with senior Chrome engineers | Deliver changes at Chrome quality standards (95% test coverage) | Design documents reviewed and accepted; changes adopted into production branch | 68% feature delivery acceleration across the observer-pattern system | High-bar code review makes you faster, not slower -- it front-loads the hard questions |

**Recommended case study:** Chrome lock-free trie -- algorithmic problem-solving at production scale, zero regressions. Mirrors IMC's environment exactly: constrained system, correctness requirement, measurable before/after.

**Red-flag questions:**
- *"No production Java"* -- "My production C++ is from Chrome at 3B-user scale. Java and C++ share the concurrency primitives IMC cares about -- lock-free structures, memory ordering. I can ramp on idioms fast; the concepts transfer."
- *"Interested in trading/finance?"* -- "What draws me is the engineering constraints: low latency, concurrency correctness, systems that can't fail quietly. Trading makes those constraints harder and more interesting -- I'm optimizing for the environment."
- *"Still in school?"* -- "Graduating May 2027. I've been shipping at production scale while finishing -- Chrome stable channel, TiMoto primary engineer. I'm targeting the May 2027 cohort, or an earlier start if the timeline allows."

---

## G) Posting Legitimacy

**Tier: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| **Posting active** | Live EU Greenhouse form; full JD; Apply button present; form fields render | Positive |
| **URL change note** | EU domain (`job-boards.eu.greenhouse.io`) vs prior US domain; same token 4577504101; content and location (Chicago) unchanged | Neutral -- ATS routing, not a ghost signal |
| **Salary transparency** | $200,000 base explicitly stated in JD -- rare for a private firm, strong legitimacy signal | Positive |
| **JD specificity** | Named preferences (Java/C++, algorithms/DS, 1-3 years); non-generic requirements | Positive |
| **Company health** | IMC is a highly profitable private HFT firm; no layoffs; active global hiring in 2025-2026 | Positive |
| **H-1B sponsorship** | IMC Americas: 34 LCAs FY2025, 100% approval rate; Software Developer is a sponsored role | Positive |
| **Reposting pattern** | Previously seen as report #021 on US domain (2026-05-29); same role, different URL scheme -- consistent with a global ATS, not a ghost repost | Neutral |
| **Role-company fit** | Early Career SE at HFT = canonical new grad pipeline posting; IMC hires continuously at this level | Positive |

Real, active posting. EU domain reflects IMC's global Greenhouse setup. No ghost signals.

---

## H) Draft Application Answers

*(Score 4.4/5 -- above 4.0 threshold; including per apply policy)*

**Will you require immigration sponsorship to begin working for IMC?**
> Yes -- I am on F-1 status (OPT eligible from May 2027). I will need work authorization support to begin.

**Will you require immigration sponsorship in the future to continue working for IMC?**
> Yes -- I will need H-1B sponsorship for long-term employment. IMC's strong LCA record (34 filings, 100% approval rate in FY2025) suggests this is a well-supported process.

**Please confirm the education section includes all degrees earned:**
> Confirmed -- I am currently completing a Bachelor of Science in Computer Science at Georgia State University (Expected May 2027, GPA 3.75). No other degrees.

**Do you currently have any offers?**
> No. N/A.

**Programming languages you are proficient in (select all that apply):**
> Check: C++, Java, Python

**Privacy Statement / Interview Code of Conduct:**
> Select: I agree / I have read and agree (as appropriate)

---

## Keywords Extracted

lock-free, concurrent data structures, algorithms, C++, Java, Python, low-latency, trading platform, high-throughput, performance engineering, systems software, distributed systems, financial markets, software development lifecycle, cross-functional collaboration, quant research, early career, correctness, protocol buffers, concurrency
