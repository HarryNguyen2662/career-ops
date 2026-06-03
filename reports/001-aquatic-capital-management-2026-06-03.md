# Evaluation: Aquatic Capital Management — Software Engineer, Early Career

**Date:** 2026-06-03
**URL:** https://job-boards.greenhouse.io/aquaticcapitalmanagement/jobs/8489233002
**Archetype:** Systems Software Engineer (HFT / Quant Infrastructure)
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| **Archetype** | Systems Software Engineer — High-Performance / Quant Infrastructure |
| **Domain** | Trading infrastructure, distributed systems, high-performance computing |
| **Function** | Build — rotate through 2-3 technology teams contributing to trading systems |
| **Seniority** | Early Career / New Grad (explicit) |
| **Location** | Chicago, IL (onsite) |
| **Team size** | Small firm (~50-100 engineers, founded 2019) |
| **Comp (base)** | $150K–$200K base + significant discretionary bonus |
| **Comp (total)** | $325K–$425K+ total per Levels.fyi |

**TL;DR:** Ex-Citadel quant hedge fund rotating early-career engineers through C++/Python trading infrastructure teams — relaxed culture, top-tier comp, direct profit impact. One of the best new-grad roles in quant engineering.

---

## B) Match with CV

| JD Requirement | Harry's CV Evidence | Strength |
|----------------|---------------------|----------|
| C++ experience | Google Chrome: C++ IPC transport layer w/ Protocol Buffers, shipped to 3B+ users | ✅ Strong |
| Python experience | TiMoto AI: Django/FastAPI backend; ML serving with vLLM | ✅ Strong |
| Building software that contributes directly to profitability | TiMoto: primary engineer for revenue-critical ML serving + backend infra | ✅ Strong |
| High-performance / distributed systems | TiMoto: gRPC, multi-AZ ECS, sub-50ms p99; Google: lock-free trie, 96% latency cut | ✅ Strong |
| Production systems ownership | TiMoto: end-to-end infra on 3-person team, on-call, incident response, runbooks | ✅ Strong |
| Performance engineering mindset | Google: identified p99 bottleneck, lock-free fix; TiMoto: deadlock root-cause analysis | ✅ Strong |
| Early career / new grad level | GSU CS May 2027, 3.75 GPA, 2 internships + current SWE role | ✅ Perfect fit |

### Gaps

| Gap | Type | Mitigation |
|-----|------|------------|
| No finance / trading domain experience | Nice-to-have | Aquatic explicitly hires for CS fundamentals, not finance background. Frame systems expertise. |
| F-1 visa (sponsorship needed) | Risk flag | Many quant firms sponsor H-1B — verify early. Not a hard blocker; ask recruiter upfront. |
| Chicago onsite (Harry is in Atlanta) | Logistical | Open to relocation per profile. State this clearly in application. |

---

## C) Level and Strategy

**Level detected:** Early Career / New Grad — Harry is a perfect archetype fit. The rotation program is explicitly designed for candidates at his level.

**"Sell strong without lying" plan:**
- Lead with **production ownership at TiMoto** — not "intern who built features" but "primary engineer who owned distributed systems in production." This is rare for a new grad.
- Frame Google Chrome work as **systems at scale**: C++ IPC shipped to 3B+ users, design docs reviewed by senior Chrome engineers.
- Emphasize **quantified performance wins**: 96% latency reduction (Google), sub-50ms p99 (TiMoto), zero OOM failures. Quant firms love this.
- Highlight **correctness under concurrency**: gRPC deadlock fix, lock-free trie, Raft/Paxos literacy from Pulumi. This signals systems thinking at the level quant shops value.

**"If they probe on finance knowledge":** Acknowledge no trading domain experience directly, then pivot — "My background is in building the infrastructure layer: low-latency systems, concurrent data pipelines, fault-tolerant services. That's directly transferable, and I'm excited to learn the trading domain context on the job."

---

## D) Comp and Demand

| Source | Data |
|--------|------|
| Job posting (base) | $150K–$200K anticipated base salary |
| Levels.fyi (total) | $325K–$425K+ median total comp |
| Bonus note | Discretionary bonus "can be a significant portion of total compensation" |
| Harry's target | $150K–$200K TC, minimum $140K |

**Assessment:** This role is **well above Harry's targets**. Base alone matches his TC target range; total comp is 2x+ his minimum. For a new grad, this is top-of-market — comparable to Google/Meta new grad packages and significantly above typical startup comp.

**Demand:** Quant/HFT firms hiring C++/Python engineers at this level is highly competitive. Aquatic is small and selective; they post few roles and have long tenures. A hire here is a strong signal.

Sources: [Levels.fyi — Aquatic](https://www.levels.fyi/companies/aquatic/salaries/software-engineer) · [Glassdoor — Aquatic](https://www.glassdoor.com/Salary/Aquatic-Capital-Management-Salaries-E5115879.htm)

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | CV Summary (add one) | No summary | "CS @ Georgia State (May 2027) · Distributed systems + C++ at Google Chrome (3B+ users) · Primary SWE for production ML infra at TiMoto AI · Seeking early-career systems engineering role" | Quant recruiters read the top 3 lines. Lead with C++ + systems. |
| 2 | TiMoto bullets | Good, but ML-forward | Reorder: lead with gRPC deadlock fix + distributed systems; push vLLM bullet down | Aquatic wants systems engineers, not ML engineers |
| 3 | Google Chrome bullets | IPC + perf = great | Keep as-is; consider bolding "C++" explicitly in first bullet | C++ is their primary language signal |
| 4 | Skills section | Lists vLLM, LangChain prominently | Move C++, Go, Python to front of Languages; move Distributed Systems + Cloud to top of skills | Match scan order of a quant recruiter |
| 5 | Pulumi project | Good systems signal | Add explicit mention of studying distributed state correctness (Raft/Paxos) + concurrent operations | Quant firms deeply care about correctness under concurrency |

**Cover letter focus:** Open with the lock-free trie story (performance diagnosis + fix), bridge to systems ownership at TiMoto, close with why Aquatic specifically (rotation program, direct infra-to-profit connection, small-team ownership culture).

---

## F) Interview Plan

| # | JD Signal | STAR+R Story | S | T | A | R | Reflection |
|---|-----------|-------------|---|---|---|---|------------|
| 1 | High-performance systems | Google Chrome: lock-free trie | Settings nav degrading to 1,200ms p99 at scale | Eliminate mutex contention on search path | Profiled bottleneck, designed lock-free concurrent trie | 96% latency reduction, zero regressions, adopted in production | Would have instrumented earlier — learned to add p99 dashboards at rollout |
| 2 | C++ production systems | Google Chrome: C++ IPC transport | Needed cross-process communication with schema evolution | Design IPC that survives protocol changes across Chrome versions | Chose Protocol Buffers over custom serialization; designed transport layer | Shipped to stable, 3B+ users, 10K+ req/sec, sub-50ms p99 | Explicit tradeoff decision (Protobuf vs. custom) — quant interviewers love this |
| 3 | Debugging concurrent systems | TiMoto: gRPC deadlock | Production deadlock under concurrent gRPC calls — 100% evaluation failure rate | Find root cause without reproducing in staging | Traced shared resource acquisition conflicts via logs + call graph | Redesigned call sequencing; 100% success rate at sub-50ms p99 | Learned to document lock acquisition order as part of design review |
| 4 | Distributed systems correctness | TiMoto: circuit breaker + auto-rollback | 3-person team running multi-AZ production infra with no platform team | Design for failure without ops overhead | Terraform IaC, circuit breakers, health check auto-rollback | 99.9% uptime, 44% cost reduction | Would add chaos engineering earlier in the lifecycle |
| 5 | Performance diagnosis | Develop for Good: N+1 fix | Response time degrading to 3s+ on large datasets | Fix without rewriting the data layer | Diagnosed N+1 pattern, added PostgreSQL indexes + query restructure | Sub-100ms for 10,000+ records | Learned to always check query plans before adding indexes |
| 6 | Systems at scale | Pulumi: Raft/Paxos study | Contributing to distributed state synchronization in open-source IaC | Understand linearizability guarantees for correctness | Analyzed Raft consensus implementation; submitted Go CLI fixes | Contributions under review by core maintainers | Deepened understanding of exactly-once semantics — directly applicable to trading systems |

**Recommended case study to present:** Google Chrome IPC — clean systems tradeoff narrative (Protobuf vs. custom), production scale (3B+ users), and C++ — directly maps to quant infrastructure work.

**Red-flag questions:**
- *"Do you have finance experience?"* → "No trading domain background, but my focus has been the infrastructure layer: low-latency systems, concurrent data pipelines, fault tolerance. That's the layer that matters in trading infra, and I'm a fast learner on domain context."
- *"You're in Atlanta — will you relocate to Chicago?"* → "Yes, absolutely. I'm open to relocation for the right opportunity and Chicago is a great market."
- *"You graduate in 2027 — when can you start?"* → "I'm currently a full-time SWE at TiMoto AI while finishing my degree. I can discuss timing — whether that's an internship for Summer 2026 or a full-time start after graduation in May 2027."

**Story bank:** Append all 6 stories above to `interview-prep/story-bank.md`.

---

## G) Posting Legitimacy

**Assessment: High Confidence** ✅

| Signal | Finding | Weight |
|--------|---------|--------|
| Active Greenhouse posting | Direct apply URL functional, multiple active roles on board | Positive |
| Multiple concurrent roles | Early Career SWE (8489226002, 8489233002), SWE intern (7990895002), SWE general | Positive — active hiring cycle |
| Company active on GitHub | [aquanauts](https://github.com/aquanauts) org is active | Positive |
| Founded 2019, ex-Citadel | Established quant firm, not a ghost shell | Positive |
| Comp range disclosed | $150K–$200K stated in posting | Positive |
| No layoff signals found | No hiring freeze or RIF news found | Positive |
| Posting age | Cannot confirm exact date; multiple similar roles suggest rolling hire | Neutral |

**Context:** Small quant firms often run "evergreen" early career postings during recruiting seasons. The presence of two similar Early Career SWE postings (8489226002, 8489233002) may indicate Chicago vs. NY positions or rolling intake — not a ghost signal.

---

## Keywords extracted

C++, Python, distributed systems, high-performance systems, trading infrastructure, quantitative research, low-latency, early career, software engineer, hedge fund, Chicago, New York, technology teams, profitability, systems engineering, production systems, performance, new grad, university, campus recruiting

---

## Machine Summary

```yaml
company: Aquatic Capital Management
role: Software Engineer, Early Career
score: 4.5
status: Evaluated
archetype: Systems Software Engineer (HFT/Quant Infra)
location: Chicago IL (onsite)
comp_base: "$150K-$200K"
comp_total: "$325K-$425K+"
visa_risk: F-1 sponsorship needed — verify early
recommendation: Apply — strong match, top-of-market comp, explicit new grad role
```
