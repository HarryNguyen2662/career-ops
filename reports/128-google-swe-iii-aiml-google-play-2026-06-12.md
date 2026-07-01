# Evaluation: Google — Software Engineer III, AI/ML, Google Play

**Date:** 2026-06-12
**URL:** https://www.google.com/about/careers/applications/jobs/results/79222149197243078-software-engineer-iii-aiml-google-play
**Archetype:** ML/AI Infrastructure
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** output/128-google-swe-iii-aiml-google-play-harry-nguyen-2026-06-12.pdf

---

## A — Role Summary

| Field | Detail |
|-------|--------|
| Role | Software Engineer III, AI/ML, Google Play |
| Domain | ML Infrastructure — model deployment, optimization, data processing |
| Team | Google Play (Android & Mobile ecosystem) |
| Seniority | L4 (SWE III — "Mid" level indicated) |
| Location | Mountain View, CA, USA |
| Comp | $147K–$211K base + 15% bonus + equity → TC ~$200K–$280K |

Google Play's ML engineering scope: backend systems powering app store ML signals (recommendations, search ranking, content moderation). SWE III = L4, typically 2–5 YOE, interview loop same as L3 for new grad adjacents.

---

## B — CV Match Table

| Requirement | Harry's Evidence | Strength |
|-------------|-----------------|----------|
| BS CS or equivalent | Georgia State BS CS, GPA 3.75, Expected May 2027 | ✅ |
| 2 yrs Python/C++ | ~15 months total: Chrome C++ (IPC, lock-free trie, Protocol Buffers); TiMoto Python (FastAPI, LangChain, vLLM). Short by ~9 months. | ⚠️ |
| 1 yr ML infra (model deployment, eval, optimization, data processing, debugging) | TiMoto: vLLM/PagedAttention deployment, LLM-as-a-judge eval pipeline, continuous batching, production debugging. ~9–10 months genuine production depth. | ⚠️ |
| 1 yr ML specialty (speech/RL/ML infra) | TiMoto ML infra directly satisfies "ML infrastructure" specialty option | ✅ |
| 2 yrs data structures/algorithms (preferred) | Google Chrome lock-free trie (CAS), Pulumi Raft/Paxos analysis, GSU coursework | ✅ |
| Master's/PhD (preferred) | BS only — not met | ❌ |
| Accessible technology experience (preferred) | Chrome 3B+ users product, some accessibility adjacency | ⚠️ |

**Gap Analysis:**
- **2-year Python/C++ gap**: Harry has ~15 months combined. Mitigate: Chrome intern shipped to 3B+ users under Googler code review — same quality bar. TiMoto production ML systems in Python with genuine debugging ownership.
- **ML infra depth**: vLLM + PagedAttention + LLM-as-a-judge evaluation pipeline is exactly what Google means. Borderline on duration but high on specificity.
- **F-1 / graduation**: Google sponsors H-1B. Disclose: "F-1 OPT at graduation May 2027; H-1B long-term."

---

## C — Level & Interview Strategy

**Target level:** L3/L4 crossover. Google may peg Harry at L3 given graduation 2027; push for L4 given production ownership at TiMoto.

**Interview loop (Google standard):**
- 2–3 coding rounds (LeetCode M/H: trees, graphs, dynamic programming)
- 1 system design (ML infra focus: model serving pipeline, feature stores, evaluation infrastructure)
- 1 Googleyness/behavioral

**ML-specific prep angles:**
- Model serving latency optimization (explain vLLM PagedAttention rationale vs naive KV cache)
- Evaluation pipeline design (LLM-as-a-judge: criteria, calibration, bias)
- Data processing at scale (batching strategies, throughput vs latency tradeoffs)
- Debugging ML systems in production (OOM, latency spikes, model regressions)

**Coding focus:** Lock-free algorithms (Chrome trie), distributed consistency (Pulumi Paxos), graph traversal (app store recommendation graphs).

---

## D — Comp & Market

| Band | Range |
|------|-------|
| Google L3 base | $147K–$175K |
| Google L4 base | $180K–$211K |
| Bonus | 15% target |
| Equity | RSUs vesting over 4 years (significant for Alphabet) |
| Total (L3) | ~$200K–$240K TC |
| Total (L4) | ~$240K–$280K TC |

Meets Harry's $150K–$200K TC target comfortably even at L3. Negotiate toward L4 citing production ownership and Chrome internship credibility.

---

## E — CV Customization Plan

**Skills row order (ML/AI Infrastructure first):**
1. ML & AI Infrastructure — lead with vLLM, PagedAttention, LLM-as-a-judge
2. Languages — Python **bolded** (primary), then C++, Go
3. Distributed Systems — gRPC, exactly-once, fault tolerance
4. Cloud & Infrastructure — AWS ECS Fargate, Terraform, Kubernetes
5. Frameworks & Databases — FastAPI, Django, PostgreSQL
6. AI Dev Tools — LAST (Claude Code, Copilot, Cursor)

**Bullet ordering adjustments:**
- TiMoto: Lead with vLLM/PagedAttention bullet (ML infra match), then LLM-as-a-judge, then gRPC/infra
- Chrome: Lead with C++ IPC + Protocol Buffers bullet, then lock-free trie, then TypeScript/React
- De-emphasize DfG AWS JWT bullet slightly; keep PostgreSQL indexing for data processing signal

**Keyword insertions:**
- Add "model optimization" and "data processing pipeline" language to TiMoto bullets
- Add "ML evaluation infrastructure" to TiMoto LLM-as-a-judge bullet

---

## F — Interview Plan (STAR+R Stories)

**"Write product or system development code"**
- Chrome: C++ IPC transport layer — designed Protocol Buffers schema, shipped to 3B+ users, sub-50ms p99. Result: zero production regressions.

**"Collaborate through design and code reviews"**
- Chrome: Collaborated with Chrome infrastructure team on design docs; code reviews adopted by senior engineers at 95% test coverage.

**"Triage product/system issues and debug"**
- TiMoto: gRPC deadlock under concurrent calls — traced shared resource acquisition conflict, redesigned call sequencing → 100% evaluation success rate.
- Chrome: Settings navigation p99 bottleneck at 1,200ms → lock-free trie → 96% latency reduction.

**"Implement solutions in ML areas / ML infrastructure"**
- TiMoto: vLLM + PagedAttention deployment — eliminated KV cache fragmentation, zero OOM failures at production traffic.
- TiMoto: LLM-as-a-judge evaluation pipeline — automated quality scoring, surfaced model regressions in CI loop.

**"Contribute to documentation / educational content"**
- TiMoto: Wrote runbooks post-incident; Pulumi contributor PR with documentation on Raft/Paxos analysis.

---

## G — Posting Legitimacy

- **Apply button visible and functional** ✅
- Title + full JD + salary range ($147K–$211K) present ✅
- Legitimate Google Careers URL ✅
- **Legitimacy: High Confidence**

---

## Machine Summary

```yaml
company: Google
role: "Software Engineer III, AI/ML, Google Play"
date: 2026-06-12
url: https://www.google.com/about/careers/applications/jobs/results/79222149197243078-software-engineer-iii-aiml-google-play
score: 4.0
archetype: "ML/AI Infrastructure"
location: "Mountain View, CA, USA"
comp_range: "$147K–$211K base + 15% bonus + equity; TC ~$200K–$280K"
visa_risk: "F-1 — Google sponsors H-1B; OPT at graduation May 2027; H-1B path viable"
legitimacy: High Confidence
recommendation: "Apply (4.0/5) — strong ML infra match via vLLM/LLM-as-a-judge; experience gap (~15 months vs 2yr req) mitigated by Chrome intern credibility and production ownership at TiMoto"
```
