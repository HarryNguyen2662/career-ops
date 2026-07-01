# Evaluation: OpenAI — Software Engineer, Full Stack - Cybersecurity Products

**Date:** 2026-06-10
**URL:** https://jobs.ashbyhq.com/openai/88654e7f-4e23-4e75-8e54-18c10d09b093
**Archetype:** Full Stack Engineer + Backend / AI Product Engineer
**Score:** 3.7/5
**Legitimacy:** High Confidence
**PDF:** output/108-openai-software-engineer-full-stack-cybersecurity-harry-nguyen-2026-06-10.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Full Stack Engineer — end-to-end product workflows, async backend services, API/data modeling, observability, for an AI-powered security product (Codex Security) |
| Domain | Cybersecurity / AI security products — vulnerability discovery, security scanning, red teaming, findings review, remediation; applied AI tooling for defenders |
| Function | Build + Operate — product surfaces (frontend + API), backend services for long-running security work, async orchestration, durable state, developer workflow integrations |
| Seniority | Not stated; $230K–$325K range maps to OpenAI L3–L4 (new grad to mid-level); OpenAI hires exceptional new grads at L3 (~$200K–$250K) |
| Location | San Francisco, CA — hybrid (3 days/week in office); relocation assistance provided |
| Comp | $230,000–$325,000 base + equity + bonuses; comprehensive benefits (medical, 401k, parental leave, learning stipend, meals) |
| Company | OpenAI — leading AI research and deployment company; mission-driven, frontier model work; Cybersecurity Products = Applied AI department building Codex Security |
| TL;DR | Full stack AI product role at OpenAI building Codex Security — the AI-powered vulnerability scanner. Harry's Chrome TypeScript/React (3B users) + TiMoto backend + AI product ownership (vLLM, LLM APIs, async pipelines) are directly relevant. Cybersecurity domain explicitly optional. Main risk: seniority gap ($230K floor suggests L3+ expectations). H-1B: confirmed at OpenAI scale. Comp is exceptional — $30K+ above Harry's target ceiling at the floor. Apply. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| "Shipping production full-stack products across modern web frontends and backend services" | Chrome: TypeScript/React event-driven system (25K+ lines, 3B users, 95% coverage); TiMoto: FastAPI/Django REST APIs, PostgreSQL + Redis data layer | ✅ Direct — frontend (Chrome) + backend (TiMoto) both in production at scale |
| "Design clear APIs and data models" | TiMoto: FastAPI/Django REST APIs + PostgreSQL schema design; gRPC inter-service contracts with Protocol Buffers; Develop for Good: N+1 analysis + composite indexing | ✅ Direct |
| "Reason about asynchronous systems" | TiMoto: gRPC async pipeline with exactly-once delivery; deadlock diagnosis via happens-before analysis; circuit breaker + auto-rollback | ✅ Direct |
| "Diagnose reliability or performance problems" | Chrome: 1,200ms → sub-50ms settings nav (96% reduction), lock-free trie; TiMoto: gRPC deadlock fix, 99.9% uptime SLO; DfG: N+1 → sub-100ms | ✅ Direct — multiple examples across different systems |
| "AI-powered product" context | TiMoto: vLLM inference engine, LLM API integration (Claude, GPT), LLM-as-a-judge evaluation pipeline, LangChain orchestration — Harry IS building an AI product in production | ✅ Direct — TiMoto is structurally equivalent to what Codex Security needs |
| "Long-running workflows, large repositories, sensitive data" | TiMoto: async ML evaluation pipeline (LLM-as-a-judge, batch jobs); gRPC exactly-once for durable state across services | ✅ Adjacent — async pipelines and durable state present; not specifically code-scanning scale |
| "Observability, reliability" | TiMoto: CloudWatch + Prometheus + Grafana two-layer observability; on-call rotation, runbooks, post-mortems; 99.9% uptime SLO | ✅ Direct |
| "Privacy, security, correctness judgment" | Chrome: 95% test coverage, code review discipline, design docs reviewed by senior engineers; TiMoto: circuit breakers, exactly-once delivery for correctness | ✅ Indirect — strong quality signal; zero direct security engineering background |
| **Application-security / cybersecurity experience** | **Zero** — no AppSec, pen testing, vulnerability research background | ⚠️ Gap — JD says "helpful, not required" |
| "Build end-to-end vulnerability discovery, scanning, red teaming workflows" | Zero domain-specific background for these workflows | ⚠️ Domain gap — but building workflows themselves is a general engineering problem |

**Gaps:**

1. **Cybersecurity/AppSec domain** (low-medium): JD explicitly says "Application-security or cybersecurity experience is helpful, but not required." Harry has zero security research or pen-testing background. However, Codex Security is fundamentally a software product — the security domain knowledge comes from security researchers on the team; engineers build the workflows, APIs, and product surface. Harry can build the infra; the domain is learnable on the job.

2. **Seniority expectations** (medium-high): $230K–$325K maps to OpenAI L3–L4. L3 is the bottom of the range and is where exceptional new grads land at OpenAI. Harry's Chrome 3B users + TiMoto primary engineer is an unusual profile for a new grad but may still be screened out at resume stage when competing against candidates with 2-4 years of experience. Per policy: apply and let the interview decide.

3. **"Long-running workflows" at code-scanning scale** (low): Codex Security scans large codebases — potentially millions of lines with long analysis jobs. Harry's async experience (TiMoto pipeline, gRPC) covers the principles. The engineering primitives are the same (durable state, job queuing, async orchestration) — the difference is scale and data type (code vs ML inputs).

4. **Full-stack as "adjacent" archetype** (low): Harry's primary archetypes are Backend/Distributed Systems, ML Infra, SRE, Platform. Full Stack is listed as adjacent. The AI product context elevates this — Codex Security is an AI product and Harry's TiMoto work is directly analogous. The frontend work (Chrome TypeScript/React) is strong. Not a primary archetype but genuinely covered.

---

## C) Level and Strategy

**Level detected:** OpenAI L3 (new grad entry) to L4 (mid-level). Floor $230K = top-of-market for new grads. OpenAI does hire exceptional new grads — the company has hired directly from top internships and strong school candidates. Harry's Chrome stable + TiMoto production AI system is an unusual new grad profile. Realistic: L3 offer at $220K–$240K base + equity.

**Core pitch:**
> "I build exactly what Codex Security needs. TiMoto is an AI product in production — I own the backend, the AI inference layer (vLLM, LLM APIs, LLM-as-a-judge evaluation), and the async pipelines that make it reliable. At Chrome I shipped TypeScript/React to 3 billion users with 95% test coverage. I've debugged async production deadlocks at scale, designed data models under correctness requirements, and run observable systems at 99.9% uptime. I haven't worked in cybersecurity, but I've built AI-powered product systems — and that's what Codex Security is. The domain is learnable; the engineering discipline is what you're hiring."

**On cybersecurity gap:**
> "I don't have AppSec background. The JD said it's helpful, not required, which I read as: you need engineers who build AI product systems, and security researchers handle the domain expertise. TiMoto is an AI system I built and operate in production — same primitives as Codex Security: async jobs, LLM APIs, reliable evaluation pipelines, product surfaces for non-technical users. I'll learn the vulnerability taxonomy on the job."

**On seniority:**
> "9 months of scope that most engineers don't get in 2 years. I'm the primary engineer for backend, ML serving, and infra at TiMoto — simultaneously. At Google I shipped to 3 billion users with design documents reviewed by senior Chrome engineers. I'm a new grad by timestamp, not by production impact."

**On H-1B (OpenAI):**
> H-1B is effectively a non-issue at OpenAI. They employ hundreds of international engineers and have a standard sponsorship process. Mention F-1 proactively but with confidence — it won't be a differentiating blocker.

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| OpenAI stated range | $230,000–$325,000 base + equity + bonuses |
| Harry target | $150K–$200K |
| Harry minimum | $140K |
| Assessment | Floor ($230K) is $30K+ above Harry's TARGET ceiling — this role pays more than Harry expected to earn; even an L3 OpenAI offer will exceed his target range |
| Realistic new grad band | $220K–$250K base at L3; equity cliff at 4-year vest with strong exit potential |
| Benefits | Full medical, 401k match, 24-week parental leave, annual learning stipend, meals — exceptional package |

**OpenAI market position:** OpenAI pays top-of-FAANG for all levels, including new grads. An L3 offer ($220K–$240K) would be the best offer Harry could receive in his job search by a wide margin. The equity component at OpenAI pre-IPO adds significant additional upside. This role should be treated as a top-priority application.

**Negotiation note:** Harry's stated targets are well below what OpenAI offers. In negotiation, anchor to market data for OpenAI specifically (Levels.fyi), not his personal target range. Say "I'm targeting market rate for this role and level" rather than citing his own $150K–$200K target, which is below their floor.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet 1 (AI product) | ML infra framing | Lead with: "Built end-to-end AI product for 3-person engineering team — LLM API integration (Claude, GPT), vLLM inference engine with PagedAttention, LLM-as-a-judge evaluation pipeline for automated quality metrics; async ML workflows with exactly-once delivery; sub-50ms p99 at production traffic" | Codex Security is an AI product with async workflows — make TiMoto look exactly like it |
| 2 | TiMoto bullet 2 (backend APIs) | Observability framing | Lead with: "Designed Python (FastAPI/Django) REST APIs and PostgreSQL + Redis data layer; CloudWatch + Prometheus + Grafana observability; 99.9% uptime SLO; on-call rotation with runbooks; gRPC inter-service layer with exactly-once delivery for durable distributed state" | Backend services + reliable state + observability = core JD requirements |
| 3 | Chrome bullet 1 | C++ IPC leads | **Swap order** — TypeScript/React bullet first, then C++: "Architected event-driven TypeScript/React system with observer pattern decoupling UI state propagation — 68% feature delivery acceleration across 25K+ lines of Chromium at 95% test coverage; shipped to 3B+ active users" | Full-stack role cares about frontend engineering quality — Chrome React is the strongest proof |
| 4 | Chrome bullet 2 | Performance framing | Keep C++ IPC but second: "Designed C++ IPC transport layer with Protocol Buffers — selected Protocol Buffers for schema evolution and cross-language compatibility; shipped to Chrome stable at sub-50ms p99, 10K+ req/sec, 3B+ active users" | Production reliability + correct schema design = directly relevant to Codex Security's API design |
| 5 | Skills section | Backend/infra leads | Frameworks & Frontend leads (React, TypeScript, FastAPI, Django prominent); ML & AI Infrastructure second group; Cloud & Infra third | Full-stack role: frontend + backend + AI product context should all be immediately visible |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Ship production full-stack products | TiMoto AI product + Chrome React | TiMoto needed a full AI product — backend, AI serving, and product layer; Chrome needed TypeScript/React at 3B scale | Ship a working AI product in production; ship React changes to 3B users at 95% coverage | TiMoto: FastAPI/Django REST APIs + LLM serving + LLM-as-a-judge eval loop; Chrome: observer-pattern TypeScript/React decoupling for 68% faster delivery | TiMoto: production AI system at 99.9% uptime; Chrome: 3B users, 95% test coverage | Full-stack means you can see the whole system — when a user doesn't get a finding, you can trace whether it's the frontend rendering, the API layer, the async job, or the model output. Without the full picture, debugging security products is guesswork |
| 2 | Design APIs and data models | TiMoto FastAPI + gRPC schemas | TiMoto's ML pipeline needed inter-service contracts that would evolve without breaking production | Define APIs and data models for a production AI system serving evolving ML workflows | FastAPI REST APIs for product layer; Protocol Buffers for gRPC inter-service contracts; explicitly chose Protobuf for schema evolution over custom serialization; PostgreSQL schema design with N+1 analysis | Zero schema-migration incidents; exactly-once delivery; sub-100ms queries at production load | Schema design is a long-term decision disguised as a short-term choice. Choose for v5, not for v1. Codex Security's findings schema will evolve as models improve — building schema evolution in from day 1 is the decision that saves you 6 months later |
| 3 | Async systems + reliability | TiMoto gRPC deadlock | Production gRPC pipeline dropping data under concurrent load — silent failure until load test | Zero data loss at sub-50ms p99 with exactly-once delivery | Traced happens-before graph across 3 services; identified lock ordering violation in concurrent gRPC calls; redesigned call sequencing with explicit lock hierarchy; added observability to catch future violations | Zero data loss at production traffic; failure mode eliminated at design level | Async systems fail silently when you don't instrument every state transition. For Codex Security's long-running scan jobs, the scariest failure mode is "scan completed successfully" with missing findings. Exactly-once semantics + per-step state logging makes silent failures visible |
| 4 | Long-running workflows / durable state | TiMoto async ML eval pipeline | LLM-as-a-judge evaluation pipeline ran batch jobs over minutes — needed durability across restarts and partial failures | Durable, restartable batch evaluation pipeline | Async job execution with idempotent state checkpointing; circuit breaker wrapping LLM API calls for transient failures; CloudWatch alerting on job latency anomalies | Zero evaluation job data loss; circuit breaker caught 3 LLM API outages transparently | Long-running workflows need progress checkpointing, not just completion signals. For Codex Security scanning a 500K-line repo, a job that fails after 80% completion should resume from checkpoint, not restart. The cost of restarting a 20-minute job repeatedly is exactly the kind of reliability problem that erodes user trust |
| 5 | Observability + diagnostics | TiMoto two-layer observability | Production distributed system needed multi-layer visibility: infra health + pipeline correctness | "Is the system alive?" AND "Is it producing correct outputs?" simultaneously visible | CloudWatch for infra SLOs (uptime, latency, scaling events); Prometheus + Grafana for application correctness (eval success rate, OOM rate, gRPC latency); on-call rotation with runbooks | 99.9% uptime SLO; zero undetected pipeline failures | For security products, observability has a higher bar than typical products. A missed vulnerability finding is worse than a visible error. You need metrics on coverage, not just throughput — which scans ran, which code paths were skipped, and whether the quality bar was met |
| 6 | AI product + user trust | TiMoto LLM-as-a-judge pipeline | AI product needed users to trust its evaluation quality — not just run LLM calls and trust output | Automated quality metrics for AI output that a non-ML engineer could understand | LLM-as-a-judge: secondary model evaluates primary model output with structured rubric; quality score surfaced in Grafana dashboard; degradation alerts on eval score drops | Quantifiable quality signal; automated catch of model regressions before production | Codex Security has the same problem: if the model starts flagging false positives at 3x the normal rate, you need to know before users start ignoring all findings. "The model found things" is not enough — you need a quality signal that earns user trust over time |

**Recommended case study:** TiMoto as a "mini Codex Security" — AI-powered system with async jobs (LLM evaluation pipeline), backend APIs, product surfaces, and observability. "I've already built a smaller version of what you're building. The difference is the domain — security findings vs ML evaluation results. The engineering problem is the same."

**Red-flag questions:**
- *"You don't have cybersecurity experience."* → "Correct. The JD said it was helpful, not required — I read that as: you need engineers who build reliable AI product systems, not security researchers. I've built one: TiMoto is an AI product in production with async pipelines, LLM APIs, evaluation metrics, and 99.9% uptime. The vulnerability taxonomy I'll learn from your security researchers. The engineering discipline is why I'm applying."
- *"You're a new grad — we expect L3+ experience."* → "I'm a new grad by graduation date. At Google I shipped to 3 billion users. At TiMoto I'm the primary engineer for backend, ML serving, and infra simultaneously. Those aren't 'summer internship projects' — they're production systems. Evaluate the impact of what I shipped, not when I got my diploma."
- *"Work authorization?"* → "F-1 status. OpenAI sponsors H-1Bs — I'd want to confirm the timeline for this role, but I'm not concerned about it being a blocker here."
- *"Why cybersecurity? You have no security background."* → "Because Codex Security is an AI product that happens to serve security use cases — and building AI products in production is what I do. Also: AI is going to redefine application security entirely. Being at the team that defines that standard, inside the company building the most capable models, is exactly where I want to be."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active ("Apply for this Job") on Ashby | Positive |
| Comp disclosed | $230K–$325K explicitly stated with full benefits breakdown | Positive |
| JD specificity | Specific team (Cybersecurity Products), specific product (Codex Security), concrete responsibilities (vulnerability discovery, scanning, red teaming, remediation workflows) | Positive |
| Company status | OpenAI — the leading AI company; publicly active, growing; hired extensively post-2024 | Positive |
| H-1B | OpenAI employs hundreds of international engineers; confirmed H-1B sponsor at scale | ✅ Confirmed |
| Relocation support | Explicitly offered ("relocation assistance to new employees") | Positive |
| Department clarity | Applied AI department — clear team context; not a generic evergreen posting | Positive |

---

## Keywords extracted

Full stack, software engineer, cybersecurity, Codex Security, vulnerability discovery, security scanning, red teaming, findings review, remediation, async orchestration, durable state, long-running workflows, backend services, APIs, data models, observability, reliability, privacy, correctness, TypeScript, React, Python, FastAPI, PostgreSQL, AI-powered, product engineering, Applied AI, San Francisco, hybrid, OpenAI

---

## Machine Summary

```yaml
company: OpenAI
role: "Software Engineer, Full Stack - Cybersecurity Products"
date: 2026-06-10
url: https://jobs.ashbyhq.com/openai/88654e7f-4e23-4e75-8e54-18c10d09b093
score: 3.7
archetype: Full Stack Engineer + Backend / AI Product Engineer
location: "San Francisco, CA — hybrid (3 days/week); relocation assistance provided"
comp_range: "$230K–$325K base + equity + bonuses; floor is $30K+ above Harry's target ceiling; treat as top-priority application"
visa_risk: "F-1 — H-1B confirmed at OpenAI scale; standard sponsorship process; mention proactively but not a blocker"
legitimacy: High Confidence
recommendation: "Apply (3.7/5) — OpenAI top-priority application. Full-stack match (Chrome TypeScript/React + TiMoto backend). AI product context (TiMoto = async AI pipelines, LLM APIs, eval loop) maps directly to Codex Security. Cybersecurity domain explicitly optional. Comp ($230K floor) far exceeds Harry's target — best possible outcome if hired. Main risk: seniority gap ($230K range targets L3+); Chrome scale + TiMoto primary engineer make this a defensible application for exceptional new grad track."
```
