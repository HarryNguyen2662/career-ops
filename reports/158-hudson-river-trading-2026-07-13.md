# Evaluation: Hudson River Trading — Software Engineer (C++ or Python), 2027 Grads

**Date:** 2026-07-13
**URL:** https://www.hudsonrivertrading.com/hrt-job/software-engineer-c-or-python-2027-grads/
**Via:** — (direct)
**Archetype:** Systems Software Engineer + Performance Engineer (dual primary fit)
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** output/158-hrt-swe-harry-nguyen-2026-08-06.pdf (refreshed 2026-08-06, see addendum below)

---

## Machine Summary

```yaml
company: Hudson River Trading
role: "Software Engineer (C++ or Python), 2027 Grads"
date: 2026-07-13
url: https://www.hudsonrivertrading.com/hrt-job/software-engineer-c-or-python-2027-grads/
score: 4.5
archetype: "Systems Software Engineer + Performance Engineer"
location: "Austin, TX; Chicago, IL; New York, NY; Singapore (onsite)"
comp_range: "$300,000 base (stated) + discretionary bonus + benefits; L1 total comp median ~$403K per Levels.fyi"
advertised_comp: "300,000 USD base per year"
visa_risk: "F-1 — HRT sponsorship stance unconfirmed for this role; visa sponsorship question is in the application form itself"
legitimacy_tier: "High Confidence"
via: null
EOF_MARKER: true
```

## A) Role Summary

| Field | Detail |
|---|---|
| Archetype | Systems Software Engineer + Performance Engineer (dual — role spans both) |
| Domain | Quantitative trading / low-latency systems infrastructure |
| Function | Build (general SWE rotation across HRT's trading infrastructure teams) |
| Seniority | Entry-level / New Grad (L1) — explicitly "2027 Grads," eligible for full-time start in 2027 |
| Remote | Onsite — Austin, TX / Chicago, IL / New York, NY / Singapore, candidate ranks preferred office in the application form |
| Team size | Not stated |
| Culture screen | No `culture_screen.require` set in `config/profile.yml`, scored qualitatively: Blind aggregate 4.4/5 (121 reviews), Compensation 4.8/5, Work-Life-Balance 4.0/5 (HRT's lowest-rated category but still acceptable). Mixed signal on long-term growth ("fun as a new grad, but not great if you're looking to grow professionally," "poor leadership, slow career growth" in some reviews) versus positive comp/smart-colleagues signal. **Pass, with a growth-trajectory caveat** — not a blocker, but worth probing in interviews. |
| TL;DR | Entry-level C++/Python systems engineering role at a top-tier HFT firm, with an exceptional new-grad comp package (~$300K+ base) and a 2027 start that lines up exactly with Harry's May 2027 graduation — plays directly to his lock-free/concurrency systems work from Chrome. |

**Geo-mismatch check:** Structured location field lists four onsite offices (Austin, Chicago, New York, Singapore) with no remote designation; JD body doesn't claim remote either. No contradiction, no flag.

## B) Match with CV

| JD Requirement | CV Evidence |
|---|---|
| Full-time undergrad/master's CS student eligible for full-time roles in 2027 | Georgia State University, BS Computer Science, expected **May 2027** — exact match |
| Excellent design, debugging, and problem-solving skills | **Chrome lock-free concurrent trie** — identified mutex contention via profiling, replaced with lock-free structure, 96% p99 latency cut, zero regressions. **TiMoto gRPC deadlock fix** — traced shared resource acquisition conflict, redesigned call sequencing, 100% eval success rate |
| Working experience with C/C++ or Python required, good CS fundamentals | **C++ IPC transport layer** at Chrome (Protocol Buffers) shipped to stable channel; Python listed in `cv.md` Skills → Languages |
| Knowledge of UNIX operating systems (Linux), system/processor performance, network communication | Chrome's C++ IPC work is literally inter-process/network communication at the systems level; the lock-free trie redesign is direct processor-level concurrency work; TiMoto's gRPC inter-service layer is production network communication experience |
| Interest in low-level architecture, logic design, and/or verification (plus) | Lock-free structure design + **linearizability verification** before shipping (Chrome); **Raft/Paxos consensus analysis** in the Pulumi project — direct evidence of interest in low-level distributed correctness |

**Gaps:**
1. No quantitative-finance or trading-specific experience. **Hard blocker: No** — this JD does not list finance/stats/probability as a qualification; it asks for CS fundamentals + C/C++ or Python + systems knowledge, all of which are covered. Mitigation: don't manufacture a finance angle — lead with the systems/concurrency fit instead, which is the actual ask.
2. Existing proof points are backend/browser systems work, not literally kernel- or network-stack-level HRT-style low-latency trading infrastructure. Mitigation: in interviews, foreground the *mechanism* (lock-free structures, linearizability, concurrency correctness) over the *domain* (browser vs. trading) — the transferable skill is the same.
3. No public C++ systems project on GitHub (Pulumi is Go/IaC). The application form has an optional "GitHub Profile" field — consider whether to leave it as-is or note in interview prep that the strongest C++ evidence is the Chrome work itself, not a repo.

## C) Level and Strategy

**Level detected:** Entry-level / New Grad (L1 equivalent) — matches Harry's target level exactly. No "sell senior" plan needed.

**Core pitch:**
> "I've already shipped performance-critical, concurrency-sensitive C++ code to production at extreme scale: a lock-free concurrent trie that cut Chrome's settings-search p99 latency 96% with zero regressions, and a C++ IPC transport layer serving 3B+ users at sub-50ms p99. That's the same discipline HRT's systems work demands — correctness under concurrency, verified before it ships."

**If they downlevel me:** Not applicable — this is already the entry-level track.

**Note on the AI-tools clause:** The posting states AI tool use during interviews/assessments is strictly prohibited and may result in disqualification or rescission. This applies to the interview/assessment stage only, not to preparing application materials — flagging it here so Harry does not use any AI assistance once he's in HRT's actual interview/OA process.

## D) Comp and Demand

**Company type:** Private, mature, high-margin quantitative trading firm (HFT) — not public, but shares public-big-tech reliability signals: structured L1/L2/L3 levels, large and growing engineering org (~1,454 employees, +19.9% YoY), repeatable annual new-grad hiring pipeline. **Compensation reliability: High.**

| Component | Figure | Source |
|---|---|---|
| Advertised (JD) | $300,000 USD base per year | JD |
| Bonus | Discretionary performance-based, unstated % | JD |
| Benefits | "Competitive benefits package," unspecified | JD |
| Levels.fyi L1 total comp (median) | $403,032/yr (base + stock/profit-share + bonus) | [Levels.fyi — Hudson River Trading L1 Software Engineer](https://www.levels.fyi/companies/hudson-river-trading/salaries/software-engineer/levels/l1) |
| Levels.fyi L1 total comp (range) | $200K–$716K+ | [Levels.fyi — Hudson River Trading L1 Software Engineer](https://www.levels.fyi/companies/hudson-river-trading/salaries/software-engineer/levels/l1) |

Against Harry's target range ($150K–200K TC) and floor ($140K): **the advertised base alone ($300K) is already 1.5x his target ceiling, before bonus.** This is the strongest comp match evaluated to date — well above report #157 (Google AI Career Catalyst, $123K–$175K+bonus) and every other role in the tracker.

**Demand trend:** Hudson River Trading had a round of layoffs in February 2026 ([Blind discussions](https://www.teamblind.com/company/Hudson-River-Trading/posts/hudson-river-trading-layoffs)), but the company is still net-growing — ~1,454 employees as of December 2025, up 19.9% from 2023 ([Revelio Labs](https://www.reveliolabs.com/companies/hudson-river-trading/employees/)) — and continues active hiring, though at a reduced posting volume (153 active postings in 2025, down 24.1% from 2024). This new-grad SWE pipeline role reads as part of HRT's standard annual cohort recruiting, not a signal tied to the February reduction.

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---|---|---|---|
| 1 | Summary | Backend/ML-infra framing | Lead with low-level C++ systems/concurrency work | HRT wants systems engineers, not backend/ML infra — match the actual ask |
| 2 | TiMoto bullet selection | Leads with vLLM/ML serving | Emphasize the gRPC deadlock/concurrency fix over the ML angle | Concurrency correctness is directly relevant; vLLM/LLM serving is not |
| 3 | Chrome bullets | Already strong | Lead with these — most relevant proof points for this role | Lock-free trie + C++ IPC map almost 1:1 to the JD's "low-level architecture... verification" language |
| 4 | Skills — Languages | C++ already listed first | No change needed | Already leads with C++ |
| 5 | Coursework line | Distributed Systems, OS, DB, Networks, Data Structures | No change needed | Already covers "good CS fundamentals" |

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Low-level architecture, logic design, verification | Lock-Free Trie at Google Chrome | Chrome settings search hit 1,200ms p99 for power users | Reduce latency without correctness regression | Identified mutex contention via profiling, replaced with lock-free structure, verified linearizability | 96% latency reduction, zero regressions, shipped to stable | Lock-free structures need proof by construction, not just benchmarks |
| 2 | Debugging, problem-solving under concurrency | gRPC Deadlock Fix at TiMoto | Production AI eval service hit intermittent deadlocks under concurrent gRPC calls | Debug and eliminate the deadlock | Traced shared resource acquisition conflict; redesigned call sequencing | 100% eval success rate, sub-50ms p99, zero recurrence | Instrument concurrent call paths before launch — a lock-order diagram would've caught this pre-production |
| 3 | C/C++ experience, network communication | C++ IPC Transport Layer at Chrome | Chrome needed a new IPC layer for stable-channel deployment | Ship a schema-evolvable, cross-language transport | Chose Protocol Buffers over custom serialization | Shipped to stable, 3B+ users, sub-50ms p99, 10K+ req/sec | Design-doc-first review culture catches serialization tradeoffs before they're expensive to reverse |
| 4 | Low-level correctness under concurrent operations | Raft/Paxos Analysis at Pulumi | Distributed state synchronization layer needed correctness guarantees under partial failure | Study and validate the consensus approach | Analyzed linearizability guarantees under concurrent operations and partial failures | Documented correctness reasoning for an active open-source review | Reading consensus literature before touching the code prevents subtle correctness bugs |
| 5 | General debugging / problem-solving | N+1 Query Fix at Develop for Good | API response time degraded to 3+ seconds on large datasets | Diagnose and fix the bottleneck | Diagnosed N+1 query pattern, redesigned with PostgreSQL indexing | Sub-100ms on 10,000+ record datasets | Profile before optimizing — the fix was obvious once the N+1 was visible |

**Recommended case study:** The Chrome lock-free concurrent trie redesign — walk through the profiling process, the mutex-contention diagnosis, and the linearizability verification together. This is the single closest artifact to HRT's own stated profile ("you can look at code, figure out how it works, and identify how to make it better... describe software designs at a high level... low level... and anywhere in between").

**Red-flag questions and answers:**
- *"You don't have a finance or trading background — how would you ramp up?"* → The JD itself doesn't ask for one — it asks for CS fundamentals, C/C++ or Python, and systems/concurrency knowledge, all of which are covered directly. Reframe as: the trading domain is learnable; the concurrency and correctness discipline is not, and that's already demonstrated.
- *"Why HFT instead of another big tech systems role?"* → Genuine interest in extreme low-latency systems work, citing the sub-50ms p99 Chrome IPC work as evidence this problem space already excites him.

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Posting freshness | "New" tag shown on the live page | Positive |
| Apply button | Active, full multi-section application form present (education, GPA, start-date eligibility, visa question, etc.) | Positive |
| Description quality | Highly specific — named locations, Job ID 571, explicit base salary, distinct Profile/Qualifications/Culture sections | Positive |
| Requirements realism | Entry-level requirements match the entry-level "2027 Grads" title exactly — no staff-level requirements smuggled in | Positive |
| Salary transparency | Explicit $300,000 base stated directly in the JD | Positive |
| Reposting pattern | Not found in `scan-history.tsv` for this exact URL (two *other* HRT roles have been seen — Systems Engineer/Windows, HPC Network Engineer — but not this one) | Neutral (first sighting) |
| Company hiring signal | February 2026 layoffs occurred, but headcount is still up 19.9% YoY and hiring continues, just at a reduced posting volume | Neutral — worth noting, not concerning |
| Role-market fit | Entry-level new-grad SWE pipeline roles at major HFT firms are standard annual-cohort hires | Positive |

**Context notes:** The February 2026 layoffs are worth being aware of, but nothing in the available signals ties them to this new-grad pipeline specifically — annual cohort hiring commonly continues independent of headcount adjustments elsewhere in a firm.

**Employment classification:** No contractor/services-status language present; standard full-time employee framing (base salary, discretionary bonus, benefits all described as employee compensation).

## Cover Letter Draft

> Draft generated at evaluation time. Complete via `/career-ops cover 158-hudson-river-trading-2026-07-13` to fill in angles, confirm research, and generate the PDF.
> Gaps flagged below — address them during the cover flow.

---

**Opening** *(placeholder — refine with your "why this role" angle)*
Hudson River Trading's systems engineering work — squeezing correctness and performance out of concurrent, low-latency infrastructure — is the same problem space I already work in daily, and I want to bring that discipline to HRT's trading systems.

**Profile introduction**
I'm a Computer Science student at Georgia State University (May 2027) and the primary engineer for backend, cloud infrastructure, and ML serving at TiMoto AI, where I've resolved production concurrency bugs under load. My Google Chrome internship shipped a C++ IPC layer and a lock-free performance fix to Chrome's stable channel, serving 3B+ users.

**Key achievements** *(selected from cv.md — exact wording preserved)*
- **Identified settings navigation as a p99 bottleneck at 1,200ms**, designed and implemented a lock-free concurrent trie search — 96% latency reduction, zero production regressions.
- **Designed C++ IPC transport layer with Protocol Buffers**, shipped to Chrome stable channel serving 3B+ active users at sub-50ms p99, 10K+ req/sec.
- **Designed and maintained gRPC inter-service layer**, resolving a production deadlock under concurrent calls by tracing shared resource acquisition conflicts — 100% evaluation success rate at sub-50ms p99.
- **Analyzed Raft/Paxos consensus** in a distributed state synchronization layer, studying linearizability guarantees and correctness under concurrent operations and partial failures.

**Problems I will solve** *(placeholder — requires company research + your input)*
> To be completed: what specific low-latency or systems-performance challenges do HRT's trading infrastructure teams face that you'd want to help solve?

**Closing**
I am happy to discuss further at your convenience.

---

**Gaps flagged:** No quantitative finance / trading background (not a stated requirement in this JD — non-blocking). No public C++ systems repository (Chrome production work is the primary evidence instead).

**JD keywords to mirror** *(extracted for ATS + human read)*
software engineer, C++, Python, UNIX, Linux, system performance, processor performance, network communication, low-level architecture, logic design, verification, debugging, problem solving, computer science fundamentals, algorithmic trading, full-time 2027

---
*Run `/career-ops cover 158-hudson-river-trading-2026-07-13` to complete angles, confirm company research, and generate the PDF.*

---

## Keywords extracted

C++, Python, UNIX, Linux, system performance, processor performance, network communication, low-level architecture, logic design, verification, debugging, problem solving, algorithmic trading, quantitative trading, computer science fundamentals, full-time 2027, New York, Chicago, Austin, Singapore

## Application Answers

**Date:** 2026-07-14
**State:** filled

### Free-text answers

- None captured.

### Selections made

- None captured.

### Other field values

- None captured.

### Files used

- None captured.

---

## Addendum — CV refresh 2026-08-06

Same posting resurfaced via a Greenhouse mirror URL (`job-boards.greenhouse.io/embed/job_app?for=wehrtyou`, token `8052122`) — identical title "Software Engineer (C++ or Python), 2027 Grads," same $300K base, same "no multiple applications" policy noted originally. Not a new role; no re-evaluation performed.

The original CV (generated 2026-07-13, before the `templates/cv-template.tex` spacing fix on 2026-08-05) was missing the NextStep project entirely — only Pulumi was included. Regenerated with the fixed template: both personal projects present, all Experience bullets intact, same tailoring strategy as the original Customization Plan (Chrome's C++ IPC/lock-free-trie bullets leading, TiMoto's gRPC concurrency fix emphasized over the ML-serving angle, Languages leading with C++). Verified 1 page, 18/18 items, 0 stray asterisks. Score and recommendation unchanged (4.5/5, already Applied).

New file: `output/158-hrt-swe-harry-nguyen-2026-08-06.pdf`.
