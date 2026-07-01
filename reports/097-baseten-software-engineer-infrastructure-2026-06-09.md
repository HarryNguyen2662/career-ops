# Evaluation: Baseten — Software Engineer, Infrastructure

**Date:** 2026-06-09
**URL:** https://jobs.ashbyhq.com/baseten/ae64d1d4-7b0a-4be4-8d77-7f5ce63849a7
**Archetype:** ML / AI Infrastructure Engineer + Platform / Cloud Infrastructure Engineer
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** output/097-baseten-software-engineer-infrastructure-harry-nguyen-2026-06-09.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | ML / AI Infrastructure Engineer + Platform / Cloud Infrastructure Engineer — primary archetype match |
| Domain | ML inference platform — powers Cursor, Notion, OpenEvidence, Abridge, Clay, Gamma, Writer; multi-cloud GPU capacity management, model serving, inference orchestration |
| Function | Build — core ML inference infrastructure: Python + Go, Kubernetes deployments, inference orchestration, monitoring, resource management for ML workloads |
| Seniority | Unlabeled "Software Engineer" — comp range ($165K–$330K at 90th percentile) suggests mid-level; no explicit years requirement |
| Location | San Francisco; New York; Remote — Hybrid (all three options available) |
| Team | Series E; $300M raised; BOND, IVP, Spark Capital, Greylock, Conviction; customers include top AI companies |
| Comp | $165,000–$330,000 + equity ("90th percentile" stated policy) |
| TL;DR | Baseten is Harry's ideal archetype match. The JD is literally Harry's TiMoto job description rewritten at platform scale — Python + Go, Kubernetes, ML model serving, inference orchestration, resource management, monitoring. vLLM + PagedAttention experience is directly what Baseten's customers use. $165K–$330K at 90th percentile = top of Harry's target. H-1B confirmed (validated in #087). Remote option means no relocation needed. **Apply immediately.** |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| Python and Go for infrastructure components | TiMoto: Python (FastAPI/Django, vLLM, LangChain) primary language; Pulumi: Go CLI features and bug fixes under active review | ✅ Direct — Python in production, Go in OSS |
| Kubernetes deployments for model serving | TiMoto: EKS (AWS EKS in Skills); Terraform IaC; Docker containerization; multi-AZ orchestration | ✅ Direct — K8s orchestration experience |
| Inference orchestration for model deployments | TiMoto: vLLM inference engine with PagedAttention; continuous batching; LangChain orchestration | ✅ Direct — *exactly* what Baseten customers deploy |
| Monitoring systems for model performance metrics | TiMoto: CloudWatch + Prometheus + Grafana for production ML serving; LLM-as-a-judge evaluation pipeline | ✅ Direct |
| Efficient resource management for ML workloads | TiMoto: vLLM PagedAttention eliminated KV cache memory fragmentation; zero OOM at production traffic; 44% cost reduction | ✅ Direct — GPU memory management at serving layer |
| Infrastructure automation for ML deployment workflows | TiMoto: Terraform IaC for ECS Fargate; auto-scaling; CI/CD; auto-rollback | ✅ Direct |
| Distributed systems concepts | TiMoto: gRPC inter-service, circuit breakers, exactly-once semantics, multi-AZ; Pulumi: Raft/Paxos study | ✅ Direct |
| ML concepts + model serving | TiMoto: vLLM, PagedAttention, continuous batching, LLM APIs; LLM-as-a-judge evaluation | ✅ Direct — production ML serving is Harry's TiMoto core work |
| Go proficiency (plus) | Pulumi: Go CLI contributions under active maintainer review; Skills: Go | ✅ OSS Go (not production Go, but active contribution) |
| BS CS or higher | Georgia State BS CS, GPA 3.75 | ✅ Direct |
| H-1B | F-1 — Baseten confirmed active H-1B sponsor (validated in #087 evaluation) | ✅ Confirmed |
| SF / NY / Remote | Harry Atlanta-based; Remote option available — no relocation needed | ✅ Remote option removes relocation friction |

**Gaps:**

1. **GPU hardware depth (B200, H100, fractional GPU).** The example initiatives mention B200 GPUs, fractional H100s, multi-node inference. Harry has never worked with GPU hardware directly — his ML serving experience is software-layer vLLM on CPU+AWS. Mitigation: the JD requirements do not ask for GPU hardware experience — just "basic understanding of ML concepts and model serving" and "interest in ML/AI infrastructure and willingness to learn." Harry has production vLLM serving (the software layer that *manages* the GPU) which is a stronger signal than most applicants. Harry doesn't need to know GPU microarchitecture; he needs to know how model serving works, which he does.

2. **Go production experience.** Go is listed as "a plus." Harry has Pulumi OSS contributions in Go (not production service engineering). Mitigation: Pulumi is serious Go codebase — CLI contributions under active review by core maintainers demonstrates real Go proficiency. Not a blocker.

3. **Scale gap.** Baseten serves Cursor (millions of users), Notion, Writer, etc. Harry's production scale is TiMoto (smaller). Mitigation: the engineering principles are identical (PagedAttention, circuit breakers, K8s orchestration). Harry's Chrome experience (3B+ users, 10K+ req/sec) demonstrates scale instinct even if ML serving scale is lower.

---

## C) Level and Strategy

**Level detected:** Mid-level SWE. The $165K–$330K "90th percentile" range without explicit years requirement is a generous bracket. For Harry's profile (new grad 2027 with production ML serving), expect $165K–$200K range at entry, with strong equity.

**Core pitch — this is THE match:**
> "I've built the exact infrastructure Baseten's customers deploy. At TiMoto, I architected vLLM with PagedAttention for production LLM serving — eliminated KV cache memory fragmentation, zero OOM failures under concurrent load, continuous batching at sub-50ms p99. I didn't use a pre-built managed service; I built the serving layer from scratch. Baseten's customers — Cursor, Notion, Abridge — are doing at scale what I did at TiMoto. I understand the problem from both sides."

**On the role scope:**
> "The JD mentions multi-node inference, B200 GPU capacity management, fractional GPUs. I've operated vLLM at the software layer — the memory management, batching policy, and orchestration. The hardware scaling problems (multi-node, fractional GPU) are the next layer up from what I've already built. That's a ramp I want to do at Baseten."

**On Go:**
> "Python is my production language. Go is my OSS language — Pulumi CLI contributions actively reviewed by core maintainers. Baseten's infrastructure uses Python and Go; I'm productive in both, stronger in Python, and comfortable picking up Go service engineering quickly."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Baseten stated range | $165,000–$330,000 + equity ("90th percentile" stated policy) |
| Baseten Series E valuation | Not disclosed; $300M raised; likely $1B+ valuation |
| ML infra SWE (mid-level, SF/NY/Remote, 2026) | $180K–$280K TC at comparable-stage Series D/E companies |
| Expected Baseten offer for Harry's profile | $165K–$210K base estimated (new grad / early career entry into 90th percentile policy) |
| Harry target | $150K–$200K |
| Harry minimum | $140K |

Comp floor ($165K) is above Harry's target range. Even at the entry point of the Baseten "90th percentile" policy, this exceeds Harry's minimum by a significant margin. This is the best comp opportunity so far in the pipeline.

Note: This is the same comp structure as #087 (Baseten Billing/Internal Tooling) — same role level, same policy, different team.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet 1 | Varies | Lead with: "Architected vLLM inference engine with PagedAttention for production ML serving — eliminated KV cache memory fragmentation; zero OOM failures at production traffic; continuous batching achieving sub-50ms p99" | vLLM + PagedAttention = exact Baseten customer use case; show it first |
| 2 | TiMoto bullet 2 | gRPC deadlock | Lead with infra automation: "Architected multi-AZ ECS Fargate with Terraform IaC, CloudWatch + Prometheus + Grafana observability, circuit breaker — 99.9% uptime, 44% cost reduction; auto-rollback" | Monitoring + resource management + infrastructure automation = 3 of 7 JD bullets |
| 3 | Skills: row order | Distributed Systems or ML & AI leads | ML & AI Infrastructure leads (vLLM, PagedAttention, inference stack); then Cloud & Infrastructure (K8s, EKS, Terraform) | JD is ML inference infra — put the inference signals at the top |
| 4 | Languages | C++ or Python first | Python, Go, TypeScript, C++... | Python + Go are the two JD languages; show them first |
| 5 | Pulumi project | Go/TypeScript/IaC | Emphasize Go + distributed state: "Submitted Go CLI features enabling multi-cloud K8s/AWS/Azure/GCP provisioning" | Baseten is multi-cloud (MCM feature in example initiatives); Go + multi-cloud = exact context |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | ML model serving + inference orchestration | TiMoto vLLM + PagedAttention | Production LLM serving experiencing OOM failures under concurrent load; naive inference allocation was fragmented | Zero OOM failures at production traffic; sub-50ms p99 | Architected vLLM with PagedAttention for KV cache memory management; continuous batching for throughput; deployed with monitoring | Production ML serving without OOM — the metric that matters for AI infrastructure | The ML serving problem isn't the model; it's memory. PagedAttention solved the right problem (KV cache fragmentation) and continuous batching solved the wrong tradeoff (latency vs throughput). That's the engineering choice that mattered |
| 2 | Kubernetes deployments + resource management | TiMoto ECS Fargate + EKS + Terraform | ML workloads needed containerized orchestration with auto-scaling, health checks, and cost controls | 99.9% uptime, 44% cost reduction ($40–60/month), zero manual scaling events | Terraform IaC for ECS Fargate (multi-AZ), EKS for ML workloads, auto-scaling policies, CloudWatch-triggered rollback, circuit breaker for service degradation | Production K8s-equivalent orchestration with SLO compliance | The resource management problem for ML workloads is different from web workloads — you're optimizing for GPU utilization, not CPU. The architecture is the same (health checks, auto-scaling, rollback) but the cost function is different |
| 3 | Monitoring for model performance | TiMoto LLM-as-a-judge + CloudWatch + Prometheus | Production AI system needed both infrastructure metrics (latency, uptime) and model quality metrics (output correctness) | 100% evaluation success rate at sub-50ms p99 (model quality); zero downtime events (infra quality) | CloudWatch + Prometheus + Grafana for infra SLOs; LLM-as-a-judge pipeline for model quality evaluation; structured output schema validation | Two separate monitoring layers for AI systems — infra metrics tell you the system is up; model metrics tell you the outputs are correct. You need both | The hardest monitoring problem in AI isn't the infra layer — it's knowing whether the model is doing the right thing. LLM-as-a-judge is the answer I built; Baseten's customers need the same |
| 4 | Infrastructure automation for ML deployment workflows | TiMoto Terraform IaC + CI/CD | Manual AWS infra was non-reproducible and expensive; no deployment automation | Zero config drift; auto-rollback on health check failure; 90% deployment time reduction (Develop for Good) | Terraform ECS Fargate with full IaC; CI/CD pipeline for automated deployments; blue/green rollout pattern; auto-rollback triggered by CloudWatch alarms | Infrastructure code should be boring to operate — the complexity belongs in the comments, not in the manual runbook | ML deployment automation is the same as regular deployment automation except the artifact is a model weight file instead of a binary. The abstraction layer (Kubernetes, Terraform, health checks) doesn't change |
| 5 | Go proficiency (plus) | Pulumi Go CLI contribution | Pulumi multi-cloud CLI needed Go features for cross-cloud provisioning | Go features under active review by Pulumi core maintainers (AWS/Azure/GCP multi-cloud) | Submitted Go CLI features; studied Raft/Paxos for distributed state layer; tested across cloud providers | OSS Go contribution at production quality — reviewed by core maintainers, not just merged | The discipline of OSS contribution is different from production engineering — you write for maintainers who don't know your context, not teammates who do. That made my Go code more defensive and more readable |

**Recommended case study:** TiMoto AI inference stack — walk through: vLLM + PagedAttention design choice → concurrent request handling → LLM-as-a-judge evaluation → ECS Fargate orchestration → CloudWatch observability. This IS the Baseten problem at smaller scale — frame it as "I've built what your customers deploy, from the inside."

**Red-flag questions:**
- *"Comp expectations?"* → "Given Baseten's 90th percentile policy, I'm targeting $180K–$200K base for this level. I have competing offers in that range. The equity story at Series E is meaningful — I'd like to discuss total comp including equity grant."
- *"Work authorization?"* → "F-1, OPT from May 2027. I confirmed Baseten has active H-1B sponsorship before applying. Can you confirm the timeline and process for this role?"
- *"GPU infrastructure experience?"* → "I've operated vLLM at the software layer — KV cache management, batching policy, memory allocation. I've never touched GPU microarchitecture or bare-metal GPU provisioning. The B200/H100 work you're doing is the next layer up. That's the ramp I want to do at Baseten — I know the model serving layer cold; I want to learn the hardware management layer."
- *"Remote vs in-office preference?"* → "Atlanta-based. I'll work remote and can travel to SF or NY for team off-sites. Open to relocation if the team works better in-person — but remote is my preference to start."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active on Ashby | Positive |
| Comp disclosed | $165K–$330K + equity + "90th percentile" policy stated explicitly | Positive |
| Company status | Baseten — $300M Series E; BOND, IVP, Spark Capital, Greylock, Conviction; customers include Cursor, Notion, OpenEvidence, Abridge, Clay | Positive |
| JD specificity | Named technologies (Python, Go, Kubernetes), named example projects (multi-cloud capacity mgmt, B200 GPUs, multi-node inference, fractional H100s) with links to blog posts | Positive |
| H-1B | Confirmed active sponsor — validated in #087 evaluation (same company, different role) | Positive |
| Blog post depth | Links to detailed engineering blog posts (MCM, GPU inference) signal genuine technical team, not generic hiring | Positive |
| Remote option | SF + NY + Remote listed — active global hiring | Positive |

---

## Keywords extracted

Python, Go, Kubernetes, ML inference, model serving, inference orchestration, vLLM, GPU, resource management, monitoring, Prometheus, distributed systems, cloud infrastructure, Terraform, multi-cloud, PagedAttention, continuous batching, containerization, Series E, remote

---

## Machine Summary

```yaml
company: Baseten
role: Software Engineer, Infrastructure
date: 2026-06-09
url: https://jobs.ashbyhq.com/baseten/ae64d1d4-7b0a-4be4-8d77-7f5ce63849a7
score: 4.5
archetype: ML / AI Infrastructure Engineer + Platform / Cloud Infrastructure Engineer
location: SF / NY / Remote Hybrid — Remote option available (no relocation needed)
comp_range: "$165K–$330K base + equity (90th percentile policy); expected $165K–$210K for Harry's level"
visa_risk: "F-1 — H-1B confirmed active sponsor (validated in #087 evaluation, same company)"
legitimacy: High Confidence
recommendation: "Apply immediately — primary archetype match (ML / AI Infrastructure). vLLM + PagedAttention production experience = exactly what Baseten's platform does. $165K+ comp floor above target. Remote option available. H-1B confirmed. This is the top ML infra opportunity in the current pipeline."
```
