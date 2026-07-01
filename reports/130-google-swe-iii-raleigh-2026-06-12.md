# Evaluation: Google — Software Engineer III

**Date:** 2026-06-12
**URL:** https://www.google.com/about/careers/applications/jobs/results/135744170068189894-software-engineer-iii
**Archetype:** Backend/Distributed Systems
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** output/130-google-swe-iii-raleigh-harry-nguyen-2026-06-12.pdf

---

## A — Role Summary

| Field | Detail |
|-------|--------|
| Role | Software Engineer III |
| Domain | Generalist SWE — product/system development code, large-scale systems |
| Team | Unspecified (Google generic SWE III posting) |
| Seniority | L4 (SWE III — "Mid" indicated) |
| Location | Raleigh, NC, USA; Durham, NC, USA |
| Comp | $147K–$211K base + 15% bonus + equity → TC ~$200K–$280K |

Generic SWE III Google posting — applies to a range of teams. Preferred qualifications emphasize large-scale systems data analysis, visualization, debugging, and code health. Location is Raleigh/Durham (NC) — good for Harry if targeting non-Bay Area Google offices.

---

## B — CV Match Table

| Requirement | Harry's Evidence | Strength |
|-------------|-----------------|----------|
| BS CS or equivalent | Georgia State BS CS, GPA 3.75, Expected May 2027 | ✅ |
| 2 yrs C++/Python/Java | ~15 months combined C++ (Chrome IPC, lock-free trie) + Python (TiMoto FastAPI, vLLM). Short by ~9 months | ⚠️ |
| 2 yrs data structures/algorithms (preferred) | Chrome lock-free trie (CAS), Pulumi Raft/Paxos, GSU coursework | ✅ |
| 2 yrs large-scale systems, data analysis, debugging (preferred) | Chrome: 3B+ users IPC layer, lock-free trie (96% latency); TiMoto: gRPC deadlock RCA, vLLM production debugging; DfG: N+1 query bottleneck diagnosis | ✅ |
| Accessible technologies (preferred) | Chrome 3B+ users — broad reach | ⚠️ |
| Code/system health, test engineering (preferred) | Chrome: 95% test coverage; TiMoto: on-call rotation, runbooks, post-mortems | ✅ |

**Gap Analysis:**
- **2-year C++/Python threshold**: Harry is ~15 months combined. Mitigate with Chrome intern quality bar (Googler review, 95% coverage) and production systems ownership at TiMoto.
- **Generalist posting advantage**: No specific domain focus allows Harry to highlight his broadest strengths — C++ systems + Python ML + TypeScript tooling.
- **Location note**: Raleigh/Durham is a Google office hub (not headquarters) — slightly less competitive than Mountain View.
- **F-1 / graduation**: Google sponsors H-1B. Disclose: "F-1 OPT at graduation May 2027; H-1B long-term."

---

## C — Level & Interview Strategy

**Target level:** L3/L4. Generic posting — team match happens after offer; Harry can express interest in distributed systems, platform, or ML infra teams during team matching.

**Interview loop (Google standard):**
- 2–3 coding rounds: LeetCode M/H — focus on C++ specifics (memory management, STL, templates) and Python
- 1 system design: Large-scale distributed system (message queue, caching layer, or sharded database)
- 1 Googleyness/behavioral

**Prep angles:**
- Code quality and test engineering (Chrome 95% test coverage story)
- Performance debugging methodology (Chrome trie bottleneck analysis, TiMoto gRPC deadlock RCA)
- Large-scale data analysis (cloud metrics: CloudWatch, Prometheus/Grafana)
- Design reviews with stakeholders (Chrome infra team collaboration)

---

## D — Comp & Market

| Band | Range |
|------|-------|
| Google L3 base | $147K–$175K |
| Google L4 base | $180K–$211K |
| Bonus | 15% target |
| Equity | RSUs 4-year vest |
| TC (L3) | ~$200K–$240K |
| TC (L4) | ~$240K–$280K |

Meets Harry's $150K–$200K TC target. NC cost-of-living is lower than Bay Area — $200K TC goes further in Raleigh/Durham.

---

## E — CV Customization Plan

**Skills row order (Distributed Systems first — generalist SWE III emphasis):**
1. Distributed Systems — gRPC, protocol buffers, circuit breakers, fault tolerance
2. Languages — C++ **bolded**, Python, Go
3. Cloud & Infrastructure — AWS, Terraform, Kubernetes
4. ML & AI Infrastructure — vLLM, LLM-as-a-judge
5. Frameworks & Databases — FastAPI, PostgreSQL
6. AI Dev Tools — LAST

**Bullet ordering adjustments:**
- Chrome: Lead with C++ IPC transport bullet (C++ requirement match), then lock-free trie (data structures + debugging), then TypeScript/React
- TiMoto: Lead with gRPC deadlock RCA bullet (system health + debugging preferred), then vLLM infra, then AWS/Terraform
- DfG: Keep N+1 query diagnosis (debugging/performance preferred match)
- Emphasize "code and system health" language — on-call rotation, runbooks, post-mortems

---

## F — Interview Plan (STAR+R Stories)

**"Write product or system development code"**
- Chrome: C++ IPC transport layer — designed, shipped to 3B+ users, sub-50ms p99.

**"Participate/lead design reviews"**
- Chrome: Led design review with Chrome infrastructure team on Protocol Buffers transport architecture; presented tradeoffs vs custom serialization.

**"Review code developed by other developers"**
- Chrome: Code reviews at 95% test coverage, changes adopted by senior Chrome engineers; documented style and testability standards.

**"Triage product/system issues and debug"**
- TiMoto: gRPC deadlock RCA — traced shared resource acquisition, redesigned call sequencing → 100% success rate.
- Chrome: Settings p99 bottleneck at 1,200ms → lock-free trie → 96% latency reduction.
- DfG: N+1 query bottleneck at 3s+ → PostgreSQL indexing → sub-100ms.

**"Contribute to documentation"**
- TiMoto: Runbooks post-incident; Pulumi PR documentation on Raft/Paxos.

---

## G — Posting Legitimacy

- **Apply button visible and functional** ✅
- Full JD with salary range ($147K–$211K) present ✅
- Legitimate Google Careers URL ✅
- Location note/selector present (Raleigh/Durham) ✅
- **Legitimacy: High Confidence**

---

## Machine Summary

```yaml
company: Google
role: "Software Engineer III"
date: 2026-06-12
url: https://www.google.com/about/careers/applications/jobs/results/135744170068189894-software-engineer-iii
score: 4.0
archetype: "Backend/Distributed Systems"
location: "Raleigh, NC, USA; Durham, NC, USA"
comp_range: "$147K–$211K base + 15% bonus + equity; TC ~$200K–$280K"
visa_risk: "F-1 — Google sponsors H-1B; OPT at graduation May 2027; H-1B path viable"
legitimacy: High Confidence
recommendation: "Apply (4.0/5) — generic SWE III posting ideal for breadth profile; C++/Python/debugging preferred quals well-matched; NC location less competitive than MTV"
```
