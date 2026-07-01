# Evaluation: Google — Software Engineer, Search Evaluation Platforms

**Date:** 2026-06-12
**URL:** https://www.google.com/about/careers/applications/jobs/results/81651533124379334-software-engineer-search-evaluation-platforms
**Archetype:** Backend/Distributed Systems
**Score:** 4.2/5
**Legitimacy:** High Confidence
**PDF:** output/129-google-swe-search-eval-platforms-harry-nguyen-2026-06-12.pdf

---

## A — Role Summary

| Field | Detail |
|-------|--------|
| Role | Software Engineer, Search Evaluation Platforms |
| Domain | Search infrastructure / evaluation platform engineering |
| Team | Google Search — evaluation and platform tooling for Search quality |
| Seniority | Mid (L3/L4) |
| Location | Mountain View, CA, USA |
| Comp | $147K–$211K base + 15% bonus + equity → TC ~$200K–$280K |

This role builds the platforms and tooling used to evaluate Search quality at scale — think distributed evaluation pipelines, rater tooling, metric computation infrastructure. Very strong fit for Harry's profile: distributed systems + evaluation pipeline (LLM-as-a-judge directly relevant) + Python/C++.

---

## B — CV Match Table

| Requirement | Harry's Evidence | Strength |
|-------------|-----------------|----------|
| BS CS or equivalent | Georgia State BS CS, GPA 3.75, Expected May 2027 | ✅ |
| 2 yrs software dev in one programming language | ~15 months combined Python (TiMoto FastAPI/LangChain) + C++ (Chrome IPC, lock-free trie). Short by ~9 months — partially offset by advanced degree path note ("1 yr with advanced degree" alt path) | ⚠️ |
| 2 yrs data structures & algorithms (preferred) | Chrome lock-free trie (CAS), Pulumi Raft/Paxos, GSU Distributed Systems coursework | ✅ |
| 2 yrs Java/Python/C++ (preferred) | Python (TiMoto) + C++ (Chrome) combined ~15 months | ⚠️ |
| Distributed systems experience (preferred) | TiMoto: gRPC exactly-once semantics, multi-AZ ECS Fargate, circuit breaker; Pulumi Raft/Paxos analysis | ✅ |
| Accessible technologies (preferred) | Chrome 3B+ users product — broad accessibility adjacency | ⚠️ |

**Gap Analysis:**
- **2-year threshold**: Harry is ~15 months combined. Google note: "1 year with advanced degree" — Harry is undergraduate, so the 2-year bar applies. Mitigate: Chrome intern (same code review bar as full-time Google SWEs); production ownership at TiMoto.
- **Evaluation platform match**: Harry's LLM-as-a-judge pipeline at TiMoto is a direct analog for Search evaluation infrastructure — automated quality scoring, calibration, regression detection.
- **Distributed systems**: Multi-AZ, gRPC, exactly-once, circuit breaker pattern = strong distributed systems credibility.
- **F-1 / graduation**: Google sponsors H-1B. Disclose: "F-1 OPT at graduation May 2027; H-1B long-term."

---

## C — Level & Interview Strategy

**Target level:** L3 (new grad adjacent) or L4 push citing production ownership.

**Interview loop:**
- 2–3 coding rounds: LeetCode M/H — trees, graphs, string processing, DP
- 1 system design: Evaluation platform at scale (design a search quality evaluation pipeline — data ingestion, rater task distribution, metric aggregation, bias detection)
- 1 Googleyness/behavioral

**Key preparation angles:**
- Evaluation pipeline design (Harry's LLM-as-a-judge work maps directly)
- Distributed task coordination (rater assignments at scale → relates to gRPC exactly-once)
- Search quality metrics (precision/recall/NDCG, calibration)
- Platform/developer tooling philosophy (balance short-term delivery vs long-term platform wins)

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

Meets Harry's $150K–$200K TC target comfortably at L3 level.

---

## E — CV Customization Plan

**Skills row order (Distributed Systems first — platform engineering emphasis):**
1. Distributed Systems — gRPC, exactly-once, fault tolerance, event-driven
2. Languages — Python **bolded**, then C++, Go
3. Cloud & Infrastructure — AWS, Terraform, Kubernetes
4. ML & AI Infrastructure — LLM-as-a-judge evaluation (directly relevant for evaluation platforms)
5. Frameworks & Databases — FastAPI, PostgreSQL
6. AI Dev Tools — LAST

**Bullet ordering adjustments:**
- TiMoto: Lead with LLM-as-a-judge evaluation pipeline bullet (search eval platform match), then gRPC/distributed systems, then vLLM/ML serving
- Chrome: Lead with C++ IPC + Protocol Buffers + 95% test coverage bullet (platform code quality match)
- Add "evaluation infrastructure" and "platform improvements" language to TiMoto bullets
- Emphasize cross-team collaboration (Chrome infra team, design docs) for "work with engineering teams" requirement

---

## F — Interview Plan (STAR+R Stories)

**"Write code meeting standards, applying AI tools, ensuring testability"**
- Chrome: C++ IPC transport layer — Protocol Buffers design, 95% test coverage, adopted by senior Chrome engineers; used GitHub Copilot in development flow.
- TiMoto: LLM-as-a-judge pipeline — comprehensive test harness with calibration checks; production-ready evaluation infrastructure.

**"Balance short- and long-term goals / platform improvements for future needs"**
- TiMoto: gRPC deadlock fix — short-term: resolved production incident; long-term: redesigned call sequencing pattern as platform improvement preventing future deadlocks.
- Chrome: TypeScript/React observer pattern — short-term: delivered 68% faster feature releases; long-term: decoupled architecture enabling future UI evolution.

**"Work with team members and cross-functional partners"**
- Chrome: Collaborated with Chrome infrastructure team (design docs, code reviews); aligned with product managers on test coverage targets.
- TiMoto: Primary infrastructure engineer coordinating with frontend/product team members; wrote runbooks for cross-team incident response.

---

## G — Posting Legitimacy

- **Apply button visible and functional** ✅
- Full JD with title + responsibilities + qualifications + salary ($147K–$211K) present ✅
- Legitimate Google Careers URL ✅
- **Legitimacy: High Confidence**

---

## Machine Summary

```yaml
company: Google
role: "Software Engineer, Search Evaluation Platforms"
date: 2026-06-12
url: https://www.google.com/about/careers/applications/jobs/results/81651533124379334-software-engineer-search-evaluation-platforms
score: 4.2
archetype: "Backend/Distributed Systems"
location: "Mountain View, CA, USA"
comp_range: "$147K–$211K base + 15% bonus + equity; TC ~$200K–$280K"
visa_risk: "F-1 — Google sponsors H-1B; OPT at graduation May 2027; H-1B path viable"
legitimacy: High Confidence
recommendation: "Apply (4.2/5) — evaluation pipeline experience (LLM-as-a-judge) directly maps to Search eval platform; distributed systems depth strong; experience gap mitigated by Chrome intern credibility"
```
