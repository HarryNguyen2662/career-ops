# Evaluation: Jane Street — Software Engineer

**Date:** 2026-06-06
**URL:** https://job-boards.greenhouse.io/embed/job_app?for=janestreet&token=4274288002
**Archetype:** Systems Software Engineer / Backend / Distributed Systems
**Score:** 3.5/5
**Legitimacy:** High Confidence
**PDF:** output/076-jane-street-software-engineer-harry-nguyen-2026-06-06.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Systems Software Engineer — trading infrastructure, market data, execution systems |
| Domain | Quantitative trading / financial technology |
| Function | Build — systems, tooling, infrastructure, trading systems (team assigned after hire) |
| Seniority | All levels (evergreen posting) |
| Remote | On-site New York City |
| Comp | $200K–$300K base + discretionary bonus; new grad TC est. $347K–$631K (6figr.com) |
| TL;DR | Jane Street's perpetual evergreen SWE posting. No specific role scope — team assignment after hire. Chrome C++ lock-free work is exactly what Jane Street's systems team wants to see. School prestige gap (Georgia State vs. MIT/Cornell/CMU pipeline) is the main risk. H-1B + green card sponsor. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| Top-notch programming skills | Chrome: C++ IPC transport, lock-free trie with correctness proof; TiMoto: gRPC, distributed systems | ✅ Strong |
| Deep experience with technology | Chrome: 3B users, Chromium production; TiMoto: ML serving, AWS infrastructure | ✅ |
| Systems / low-level engineering | Chrome: C++ IPC, lock-free concurrent trie, Protocol Buffers; 96% p99 reduction | ✅ Direct |
| Python (research / ML) | TiMoto: Django/FastAPI, vLLM/PyTorch | ✅ |
| Strong interpersonal skills | Chrome: design docs + senior code review; cross-team delivery | ✅ |
| Algorithmic thinking | Lock-free trie (linearizability proof by construction); Raft/Paxos study in Pulumi | ✅ |
| OCaml / functional programming | Not in CV — Jane Street says not required | ❌ Expected |
| Finance / quant / trading domain | Not in CV — Jane Street says not required | ❌ Expected |
| Target school profile (MIT/CMU/Cornell) | Georgia State — not a typical Jane Street feeder school | ⚠️ Risk |

**Gaps:**
1. **School prestige** — Jane Street heavily recruits from MIT, CMU, Princeton, Cornell, Harvard, Stanford. Georgia State is a regional school without the pipeline. Mitigation: Chrome internship at Google + production systems work is a stronger signal than most students from target schools have. Let the work speak.
2. **OCaml / functional programming** — Not in CV. Jane Street explicitly states: "We don't expect you to have experience with functional programming, OCaml, Python, or finance." Mitigation: show correctness reasoning (lock-free trie linearizability proof) as the closest functional programming analog.
3. **Finance domain** — Not required per JD; not a real gap.

---

## C) Level and Strategy

**Level detected:** Evergreen posting — all levels. Harry enters as new grad / junior SWE.

**Sell the systems depth over school brand:**
> "I designed a lock-free concurrent trie for settings navigation in Chrome — proved linearizability by construction, eliminated mutex contention, shipped to 3B users with zero regressions. That's the kind of correctness reasoning Jane Street's systems work requires."

**On OCaml / functional programming gap:**
> "I don't have OCaml experience, but I reason about correctness formally. The lock-free trie I built required a linearizability proof — that's the same first-principles thinking you apply in functional programming. I can learn the syntax; the mindset is already there."

**On school gap:**
> "I'm at Georgia State, not MIT. What I have instead: production C++ at Chrome's scale, a gRPC deadlock I traced and fixed at TiMoto without senior help, and a lock-free data structure that shipped to production. I'd rather be judged on that."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Jane Street stated base | $200,000–$300,000 |
| Jane Street new grad TC (est.) | $347K–$631K (6figr.com, 2026) |
| Jane Street SWE TC range | $300K–$873K (25th–90th percentile) |
| Harry target | $150K–$200K base |
| Harry minimum | $140K |

Comp is exceptional at every level. New grad base ($200K) is already above Harry's $200K target. Total comp with discretionary bonus is the highest of all roles evaluated. Equity is private company — less liquid but Jane Street bonus is cash-heavy.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Chrome bullet order | React/TS or C++ IPC varies | Lead with C++ IPC transport layer (production systems) | Jane Street cares about systems + C++ depth |
| 2 | Chrome bullet 2 | vLLM or lock-free varies | Lock-free concurrent trie second — algorithmic correctness | Linearizability proof signals the formal reasoning Jane Street prizes |
| 3 | TiMoto bullet order | varies | gRPC inter-service + deadlock root-cause leads | Production systems debugging is the clearest Jane Street signal |
| 4 | Skills: Languages | C++ varies in position | C++, Python first | Both are Jane Street's core languages |
| 5 | Skills row order | varies | Languages leads, then Distributed Systems | Jane Street is systems-first; lead with the language + systems depth |

---

## F) Interview Plan

Jane Street SWE interview: multiple rounds of algorithmic coding (harder than FAANG) + systems design.

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Systems + correctness | Chrome lock-free trie | 1,200ms p99 settings navigation in Chrome | 96% latency reduction without correctness regression | Lock-free concurrent trie; linearizability proof by construction | 96% reduction, zero regressions | Profile before optimizing; prove correctness for concurrent code mathematically |
| 2 | Production systems quality | Chrome C++ IPC | Chrome needed IPC between browser process and settings with schema evolution | Ship to 3B users without breaking | Protobuf over custom serialization; design doc; senior review | Chrome stable, sub-50ms p99, 10K+ req/sec | Serialization is an API contract — design for how it will change |
| 3 | Debug complex issues | gRPC deadlock root-cause | Production deadlock under concurrent gRPC calls | Diagnose without senior help, fix without regression | Traced shared resource acquisition; redesigned call sequencing | 100% success rate restored | Concurrent code requires explicit ownership maps — instrument concurrency from day one |
| 4 | Systems ownership | TiMoto 0→1 | Primary engineer on 3-person team, no safety net | Build backend + infra + ML serving from scratch | gRPC + Django + ECS Fargate + vLLM as cohesive production system | 99.9% uptime, sub-50ms p99 | Full ownership means you cannot punt on the hard parts |
| 5 | Algorithmic thinking | Raft/Paxos study (Pulumi) | Studying Pulumi's distributed state synchronization layer | Understand linearizability guarantees under concurrent ops and partial failures | Analyzed Raft/Paxos consensus formally; mapped to correctness properties | Deep literacy in distributed consensus theory | Theory matters: you cannot reason about distributed correctness from first principles without understanding the consensus models |

**Recommended case study:** Chrome lock-free trie — "I designed a concurrent data structure where correctness required a formal proof. Here's the invariant I needed to maintain, how I proved it holds under all interleavings, and how I verified it didn't regress in production." This is exactly what Jane Street's interview tests.

**Red-flag questions:**
- *"No OCaml?"* → "I don't have OCaml syntax, but correctness reasoning is in my work. The lock-free trie I built required a linearizability proof — that's the same disciplined thinking. I'll learn the language; the mindset is there."
- *"Visa sponsorship?"* → "F-1, OPT from May 2027. Will need H-1B. Jane Street filed 43 LCAs last fiscal year with 100% approval and sponsors green cards — happy to discuss timing."
- *"Georgia State?"* → "Yes. What I have is Chrome production C++ to 3B users, a lock-free data structure I proved correct, and a gRPC deadlock I traced and fixed in production. I'd ask to be judged on that."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active on Greenhouse | Positive |
| Posting type | Evergreen — Jane Street explicitly says "always hiring" | Positive (by design) |
| Company status | Jane Street — top-tier quant trading firm, NYC, 30+ years | Positive |
| Comp disclosed | $200K–$300K base on official careers page | Positive |
| H-1B track record | 43 LCAs FY2025, 100% approval; 58 I-129 petitions, 97% approval; green card sponsorship (25 LCs) | Positive |
| JD specificity | Intentionally minimal — Jane Street's standard practice | Neutral |
| Reposting | Perpetual evergreen — not a ghost job signal | Neutral |

**Context:** Jane Street always has this posting open. It is not tied to a specific headcount — it's their application funnel. Applications are reviewed on a rolling basis and candidates proceed to phone screen if they pass an initial review. The lack of JD specificity is intentional, not a ghost job signal.

---

## Keywords extracted

C++, Python, OCaml, functional programming, systems, software engineering, algorithms, data structures, production, correctness, concurrency, distributed systems, trading, finance, New York, lock-free, performance, backend, infrastructure

---

## Machine Summary

```yaml
company: Jane Street
role: Software Engineer
date: 2026-06-06
url: https://job-boards.greenhouse.io/embed/job_app?for=janestreet&token=4274288002
score: 3.5
archetype: Systems Software Engineer
location: New York City (on-site)
comp_range: "$200K-$300K base; new grad TC est. $347K-$631K"
visa_risk: "F-1 — H-1B positive (43 LCAs FY2025, 100% approval; green card sponsor with 25 LCs)"
legitimacy: High Confidence
recommendation: "Apply — Chrome C++ lock-free work is the exact signal Jane Street's systems team wants; school prestige gap is real but production credentials may compensate; comp is exceptional"
```
