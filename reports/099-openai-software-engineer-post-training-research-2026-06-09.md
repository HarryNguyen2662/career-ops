# Evaluation: OpenAI — Software Engineer, Post-Training Research

**Date:** 2026-06-09
**URL:** https://jobs.ashbyhq.com/openai/f381868f-7b0a-4b22-b215-71c7f5c1b498
**Archetype:** AI Platform / LLMOps + AI/ML Engineer (Inference & Serving) — Research Engineering (internal tooling + evaluation systems for post-training team)
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** output/099-openai-software-engineer-post-training-research-harry-nguyen-2026-06-09.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform / LLMOps + Research Engineering — build internal tools and evaluation systems for the team that trains ChatGPT and API models |
| Domain | Post-training research infrastructure — RLHF/DPO/reward modeling pipeline tooling, evaluation visualization, experiment configuration systems; directly powers ChatGPT, OpenAI API |
| Function | Build — rapid prototyping of internal tools and visualization for researchers; refactoring and maintaining research codebases; evaluation system design |
| Seniority | "Seasoned engineer" — no explicit years requirement, but comp ($255K–$405K) implies L5+/Staff equivalent; scrappy + fast shipping culture, not process-heavy |
| Location | San Francisco, CA — 3 days/week hybrid; relocation assistance provided |
| Team | Post-Training — closest team to the actual model training process; "final step before real world deployment to millions of users" |
| Comp | $255,000–$405,000 + equity ("offers equity" stated) |
| TL;DR | OpenAI Post-Training Research Engineering — build internal tools for the team that trains ChatGPT. Python + evaluation pipelines + rapid prototyping. Harry's LLM-as-a-judge evaluation pipeline and vLLM serving are the most relevant signals in the pipeline for this role. Seniority gap ("seasoned" vs new grad) is the primary risk, but no explicit years requirement and OpenAI hires by ability. Comp floor ($255K) is 80% above Harry's target. **Apply — differentiated pitch exists, exceptional upside if they're willing to look at a strong new grad.** |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| Proficiency with Python | TiMoto: Python (FastAPI/Django, vLLM, LangChain) — primary production language; TiMoto entire backend in Python | ✅ Direct — production Python |
| Build evaluation tooling and visualization for researchers | TiMoto: LLM-as-a-judge evaluation pipeline — 100% evaluation success rate at sub-50ms p99; structured output schema validation | ✅ Direct — evaluation pipeline is Harry's TiMoto work |
| Rapid prototyping and shipping with fast-changing priorities | TiMoto: primary engineer on 3-person team, owns backend + infra + ML — shipped all three layers simultaneously | ✅ Direct — startup-speed shipping |
| Navigate large codebases independently | Google Chrome: 25K+ lines of Chromium; Pulumi: active upstream Go/TypeScript contributor in large OSS codebase | ✅ Direct — Chromium is one of the largest codebases in existence |
| Debug through complex systems | TiMoto: gRPC deadlock fix (traced shared resource acquisition conflicts across two services); Develop for Good: N+1 root cause diagnosis | ✅ Direct |
| Maintainable, testable, clean code | Google Chrome: 95% test coverage standard; design documents reviewed by senior Chrome engineers; changes adopted into production branch | ✅ Direct — Chrome test culture |
| T-shaped: expert in one area | Harry's expert area: ML serving infrastructure (vLLM, PagedAttention, continuous batching, LLM-as-a-judge) — primary TiMoto work | ✅ Direct — ML infra is the expert axis |
| Experience building internal tools or products users interface with | TiMoto: production ML platform serving real users; LLM-as-a-judge pipeline for evaluation; Django/FastAPI REST APIs | ✅ Direct |
| Team player, scrappy, fast | TiMoto: primary engineer on 3-person team — designs, builds, deploys, debugs alone; no dedicated SRE or QA | ✅ Direct — startup velocity |
| Understand post-training "on a high level" | TiMoto: production LLM serving (vLLM, inference side); LLM-as-a-judge evaluation pipeline (reward signal modeling); LangChain orchestration | ⚠️ Inference/serving side strong; RLHF/DPO/reward modeling not listed — adjacency claim only |

**Gaps:**

1. **Post-training research depth (RLHF, DPO, reward modeling).** The role is "Post-Training Research" — the team trains models via reinforcement learning from human feedback, direct preference optimization, and reward model development. Harry's LLM experience is on the *inference/serving* side (vLLM, PagedAttention, production deployment). He has not built reward models, preference datasets, or RLHF/DPO training pipelines. Mitigation: The JD says "understand how post training works on a **high level**" — not requires direct experience. Harry can demonstrate the evaluation side (LLM-as-a-judge = reward signal proxy) and production serving side; the training research side is a ramp. Strong signal: Harry's LLM-as-a-judge pipeline is conceptually adjacent to reward modeling.

2. **Seniority gap — "seasoned engineer."** OpenAI's $255K–$405K comp range implies L5+ or Staff-equivalent. Harry is a new grad (May 2027) with 9 months production experience at TiMoto + 3 months at Google Chrome. The JD doesn't specify years but the "seasoned" language and compensation signal a more experienced hire. Mitigation: (a) OpenAI explicitly hires by ability, not years. (b) Harry's production systems depth (gRPC, vLLM, ML serving, Chromium IPC) is unusual for a new grad — the CV reads like an experienced engineer. (c) Post-Training has used contractors and interns as Research Engineers historically. (d) The role values "scrappy + fast" over "senior + process" — new grad energy can be an asset.

3. **Visualization/frontend for research tooling.** Example project #1 is "visualization for our evaluation of models." This implies frontend work (charts, dashboards). Harry has TypeScript/React from Chrome — this is transferable but not highlighted as a visualization specialty. Mitigation: Harry's Chrome TypeScript/React event-driven system + React state propagation is directly relevant to visualization tooling.

4. **SF hybrid (relocation from Atlanta).** Relocation assistance explicitly provided. Not a blocker.

---

## C) Level and Strategy

**Level detected:** Unlabeled but comp ($255K–$405K) = L5/Staff equivalent. OpenAI doesn't use traditional leveling — engineers are grouped into broad bands.

**For a new grad at this level:**
Harry's pitch must NOT be "I'm a new grad." Harry's pitch is: *"I've built the exact systems your team uses — from the serving layer. At TiMoto, I built the LLM-as-a-judge evaluation pipeline that measures what post-training is trying to optimize for. I understand inference from the inside (vLLM, PagedAttention, continuous batching). The post-training team builds evaluation systems to measure model quality — I've built evaluation systems to measure serving quality. The tools are different; the problem structure is the same."*

**On the "seasoned" concern:**
> "I'm graduating May 2027, but my experience is production, not academic. I've shipped C++ IPC to 3B Chrome users, debugged gRPC deadlocks under concurrent load, and built production ML serving from scratch. I don't have 5 years of experience but I have the production instincts that come from shipping distributed systems that can't go down."

**On post-training knowledge gap:**
> "I know the inference side — PagedAttention, continuous batching, vLLM architecture — deeply. I've built LLM-as-a-judge evaluation pipelines that measure what quality means in production. The RLHF/DPO training side I know conceptually and I'm ready to ramp. I'm not the researcher; I'm the engineer who builds the tools the researchers use. That boundary is what I want to maintain and be great at."

**On tools/visualization:**
> "At TiMoto, I built the evaluation pipeline in Python — structured output schema validation, result aggregation, metric tracking. If you need visualization on top of that, I've built React/TypeScript event-driven systems in Chromium. I'd start with whatever the researchers actually need to see, not what looks good on a dashboard."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| OpenAI stated range | $255,000–$405,000 + equity |
| OpenAI equity | Profit Participation Units (PPUs); OpenAI valuation ~$300B (2026); meaningful upside at staff-level equity grants |
| Research Engineer (L5/Staff, SF, 2026) | $280K–$450K TC at OpenAI/Anthropic/Google DeepMind (Levels.fyi) |
| Expected offer for Harry's profile | Floor estimation: $255K–$290K base (below midpoint of range, reflecting new grad seniority entry) — still exceptional |
| Harry target | $150K–$200K TC |
| Harry minimum | $140K |
| Gap to Harry's target | Comp floor ($255K) is 70% above Harry's $150K target — **no comp concern at this role** |

OpenAI is the highest-paying employer in this pipeline by a large margin. Even at the floor entry ($255K), total comp exceeds every other role evaluated so far. The equity story (PPUs in $300B+ valuation company) adds significant additional upside.

This is the best comp opportunity in the pipeline if Harry can get through the bar.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet 1 | Varies | Lead with: "Led development of LLM-as-a-judge evaluation pipeline — built structured output schema validation and automated quality metrics for production AI workflows; 100% evaluation success rate at sub-50ms p99" | Evaluation pipeline is the most direct signal for post-training research tooling |
| 2 | TiMoto bullet 2 | gRPC or vLLM | "Architected vLLM inference engine with PagedAttention for production LLM serving — designed concurrent request scheduling, zero OOM failures at production traffic; enables inference for model quality evaluation" | Post-training team cares about inference; bridge from serving to evaluation |
| 3 | Skills: row order | ML & AI Infrastructure leads | ML & AI Infrastructure first (LLM-as-a-judge, vLLM, evaluation pipeline); Python first in Languages | Python proficiency is explicitly stated; evaluation tooling is the core relevance signal |
| 4 | Chrome bullet 1 | C++ IPC or lock-free trie | Lead with rapid delivery + scale + code quality: "Architected event-driven TypeScript/React system with observer pattern — 68% feature delivery acceleration across 25K+ lines of Chromium at 95% test coverage" | Post-training values shipping fast + code quality at scale; Chromium demonstrates both |
| 5 | Pulumi project | Go/IaC framing | Reframe as "large codebase navigation + distributed systems design" rather than IaC focus | JD specifically calls out "navigate large code bases independently and quickly" — Pulumi OSS is the signal |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Build evaluation tooling for researchers | TiMoto LLM-as-a-judge pipeline | Production AI system needed automated quality evaluation — manual review at scale was infeasible | 100% evaluation success rate, structured output schema validation, sub-50ms p99 pipeline latency | Built LLM-as-a-judge framework: prompt template design, structured output schema, result aggregation, metric tracking; automated across all evaluation runs | Fully automated quality signal — researchers no longer review outputs manually | The hardest part wasn't the judge model; it was defining what "correct" meant in schema terms. Once the schema was right, the evaluation became a first-class software product, not an ad-hoc script |
| 2 | Navigate large codebases quickly | Google Chrome — 25K+ lines Chromium | New intern joining one of the largest codebases in software engineering; no dedicated onboarding docs for the specific subsystem | Ship production TypeScript/React system to 3B+ active users in 12 weeks | Mapped module dependencies without documentation; identified observer pattern as the right abstraction; wrote design doc reviewed by senior Chrome engineers; 68% feature acceleration | Production Chromium with 95% test coverage | You navigate large codebases by reading tests first. Tests are the documentation the author intended; code comments are the documentation they wrote in a hurry |
| 3 | Debug through complex systems | TiMoto gRPC deadlock | Production evaluation pipeline stopped processing under concurrent load; no clear error log | Restore 100% evaluation success rate | Traced happens-before graph across two gRPC services; identified lock ordering violation at the intersection of two concurrent call paths; redesigned with explicit lock hierarchy | Zero recurrence at production traffic | Distributed deadlocks are invisible until they kill you. The fix is never "add more timeouts" — it's "draw the concurrency model and find where the invariant breaks" |
| 4 | Rapid prototyping with fast-changing priorities | TiMoto — primary engineer on 3-person team | 3-person startup; Harry owns backend + infrastructure + ML serving simultaneously; priorities shift by the day | Ship production-quality systems (99.9% uptime, sub-50ms p99) despite context-switching across domains | Designed for replaceability: clean interfaces, documented runbooks, IaC for reproducible infra; shipped incrementally with feature flags; built monitoring first | Zero unplanned downtime despite rapid feature velocity | The only way to move fast without breaking things is to instrument everything before you need it. Monitoring is day 1, not day 30 |
| 5 | Clean, testable code; code quality | Google Chrome — 95% test coverage | Chromium has an extremely high quality bar; changes reviewed by senior engineers; shipped to stable channel | Produce code at Chrome's quality standard within internship timeline | Wrote unit tests for every new function, integration tests for the IPC layer, design documents for architectural decisions; adopted into production branch without rework | 0 post-ship regressions | High test coverage is a consequence of designing for testability first. If a function is hard to test, the abstraction is wrong |
| 6 | T-shaped: expert in ML serving/inference | TiMoto vLLM + PagedAttention | Production LLM serving experiencing OOM failures under concurrent load | Zero OOM failures, continuous batching at sub-50ms p99, production-ready serving | Selected vLLM over naive inference; implemented PagedAttention for KV cache management; designed continuous batching policy for throughput-latency tradeoff | Production LLM serving without OOM — the defining infrastructure decision for LLM-powered products | The ML serving problem is fundamentally a memory allocation problem dressed up as a model problem. PagedAttention solved the right layer; everything else (throughput, latency) followed from that |

**Recommended case study:** TiMoto end-to-end — frame as "I've built what post-training teams use: evaluation pipeline (LLM-as-a-judge) + model serving infrastructure (vLLM). I've seen both sides of the boundary between research and production. That's the specific gap the Post-Training Research Engineering role fills."

**Red-flag questions:**
- *"You're a new grad — this is a senior role."* → "I understand the expectation. My production experience is unusual for my timeline — Google Chrome IPC at 3B+ users, gRPC distributed systems, production vLLM serving. The quality bar I operate at comes from Chrome, not from years. What matters to me is whether the problems here are hard — and post-training evaluation infrastructure clearly is."
- *"What's your post-training background?"* → "Production serving side: vLLM, PagedAttention, continuous batching — I know how models are served. Evaluation side: LLM-as-a-judge pipeline that measures output quality. I don't have direct RLHF/DPO experience but I understand the feedback loop conceptually. I'm applying to build the tools, not to run the experiments."
- *"Comp expectations?"* → "Given OpenAI's stated range of $255K–$405K, I'm calibrating to whatever level the team determines is appropriate for my experience. The equity story matters to me at this company specifically — I'd want to understand the PPU grant alongside base."
- *"SF relocation timeline?"* → "Flexible. I can commit to SF on whatever timeline works for the team — OpenAI's relocation support makes this straightforward."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active ("Apply for this Job") on Ashby | Positive |
| Comp disclosed | $255K–$405K + equity explicitly stated with full benefits breakdown | Positive |
| Company status | OpenAI — $300B+ valuation (2026); ChatGPT, GPT-4o, o3 deployed to hundreds of millions of users; Research department | Positive |
| JD specificity | Named team (Post-Training), named example projects (evaluation visualization, codebase refactor, experiment config), specific candidate qualities | Positive |
| H-1B | OpenAI — world's leading AI company; sponsors H-1B for engineering roles (expected with high confidence; not verified by LCA check in this session) | Positive (expected) |
| Ashby listing | OpenAI uses Ashby for all engineering postings — this is their standard hiring infrastructure | Positive |
| Active hiring signals | OpenAI is scaling rapidly in 2025–2026; post-training team is core to product pipeline | Positive |

---

## Keywords extracted

Python, post-training, evaluation, tooling, visualization, internal tools, rapid prototyping, code quality, refactoring, debugging, T-shaped engineer, clean code, testable code, research engineering, LLM, model evaluation, experiment configuration, San Francisco, hybrid, equity, fast-paced, scrappy, OpenAI, ChatGPT

---

## Machine Summary

```yaml
company: OpenAI
role: Software Engineer, Post-Training Research
date: 2026-06-09
url: https://jobs.ashbyhq.com/openai/f381868f-7b0a-4b22-b215-71c7f5c1b498
score: 4.0
archetype: AI Platform / LLMOps + Research Engineering (internal tooling + evaluation systems)
location: San Francisco, CA — 3-day hybrid; relocation assistance provided
comp_range: "$255K–$405K base + equity (PPUs); floor is 70% above Harry's $150K target"
visa_risk: "F-1 — OpenAI expected to sponsor H-1B with high confidence (unverified by LCA in this session)"
legitimacy: High Confidence
recommendation: "Apply — strong Python + evaluation pipeline + LLM serving match. Seniority gap ('seasoned engineer') is the primary risk but no explicit years req; OpenAI hires by ability. Harry's LLM-as-a-judge pipeline + vLLM experience is the most relevant signal in the pipeline for post-training tooling. Exceptional comp upside ($255K+ floor). Pitch: built evaluation systems and LLM serving infrastructure; understand the research↔production interface from both sides."
```
