# Evaluation: Doppel — Software Engineer, Infrastructure

**Date:** 2026-06-09
**URL:** https://jobs.ashbyhq.com/doppel/aba5c986-7e85-4f79-8553-e85634400b78
**Archetype:** Platform / Cloud Infrastructure Engineer + SRE
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** output/107-doppel-software-engineer-infrastructure-harry-nguyen-2026-06-09.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Platform / Cloud Infrastructure + SRE — Terraform IaC, Kubernetes, observability, staging environments, CI/CD for a high-scale security platform |
| Domain | Cybersecurity / social engineering defense — monitors 150B+ entities daily; detects phishing, impersonation, fraud across domains, social media, dark web |
| Function | Build — scale engineering infrastructure: IaC, K8s clusters, observability stack, staging environments, distributed tracing |
| Seniority | "Experienced backend engineer" — JD sparse on explicit requirements; Series C startup velocity suggests 2-4 years preferred, flexible for strong candidates |
| Location | San Francisco or New York — hybrid |
| Comp | $150,000–$400,000 + equity (wide range spanning multiple levels; realistic mid-band for non-senior: $165K–$220K base + Series C equity) |
| Company | Doppel — Series C; backed by a16z + Bessemer VP; AI-native digital risk protection platform |
| TL;DR | Platform/infra role at a Series C cybersecurity AI startup. JD is notably thin on explicit requirements but the work examples — Terraform IaC, Kubernetes, observability/tracing, staging environments — map directly to Harry's TiMoto production stack. Cybersecurity domain is new territory but not technically required to do this work. Primary gaps: Elasticsearch (mentioned explicitly), "experienced" seniority language, H-1B unconfirmed. Strong archetype match — apply. |

---

## B) Match with CV

| JD Requirement / Work Example | CV Evidence | Strength |
|-------------------------------|------------|----------|
| Terraform IaC — reproducible, version-controlled environments | TiMoto: multi-AZ ECS Fargate with Terraform IaC, explicit lifecycle management (create/update/scale/destroy); 44% cost reduction; Pulumi: Go CLI for multi-cloud IaC provisioning | ✅ Direct — production Terraform + IaC OSS contribution |
| Kubernetes — self-hosted workloads at scale | EKS in TiMoto AWS stack; Kubernetes in skills section | ✅ Listed; no standalone K8s-first project |
| Observability + distributed tracing (metrics, logging, tracing) | TiMoto: CloudWatch + Prometheus + Grafana for infra SLOs + ML pipeline correctness; on-call rotation with runbooks and post-mortems | ✅ Direct — built production observability stack from scratch |
| Staging environment + CI/CD + automated integration testing | Develop for Good: 90% deployment time reduction via CI/CD (GitHub Actions); TiMoto: ECS auto-rollback on health check failure; auto-scaling policy | ✅ Direct |
| Backend engineering at scale | TiMoto: gRPC inter-service layer, exactly-once delivery, 99.9% uptime, circuit breaker + auto-rollback; Google Chrome: 3B+ users, sub-50ms p99, 10K+ req/sec | ✅ Direct — production scale at multiple levels |
| PostgreSQL / database systems | TiMoto: PostgreSQL + Redis data layer; Develop for Good: composite indexing, N+1 diagnosis, sub-100ms queries | ✅ Direct |
| Multi-cloud (implied by Kubernetes + Terraform scope) | TiMoto: AWS (ECS Fargate, EKS, EC2, S3, RDS), GCP; Pulumi: AWS/Azure/GCP multi-cloud provisioning | ✅ Direct |
| AI-agentic platform context | TiMoto: vLLM serving + LLM-as-a-judge eval pipeline for AI agent workflows; LangChain orchestration | ✅ Adjacent — Harry builds AI agent infrastructure; Doppel deploys AI SOC agents |
| **Elasticsearch** | **Zero Elasticsearch exposure in CV** | ❌ Gap — mentioned explicitly in work examples |
| Cybersecurity / social engineering defense domain | Zero cybersecurity background | ⚠️ Domain gap — but infrastructure work is domain-agnostic |

**Gaps:**

1. **Elasticsearch** (medium): The first work example explicitly names self-hosted Elasticsearch on Kubernetes. Harry has no Elasticsearch experience. Mitigation: Elasticsearch is a search/analytics layer on top of Kubernetes and distributed systems infrastructure — the K8s + distributed systems knowledge is the harder part. Elasticsearch itself is a learnable tool. Note in cover letter: "I've built distributed systems that serve and index similar high-volume data; I'm actively learning Elasticsearch."

2. **"Experienced backend engineer" seniority** (risk): JD doesn't state years explicitly but "experienced" implies 3+ years. Harry has ~9 months FT. Mitigation: Series C startups prioritize impact over tenure; Doppel's culture signals ("low ego, high ownership, exceptional talent density") suggest merit-based assessment.

3. **Cybersecurity domain** (low): Doppel is a security company. Harry has zero cybersecurity background. But the infrastructure work is domain-agnostic — building K8s clusters and Terraform IaC doesn't require cybersecurity expertise. The domain knowledge comes with the job.

4. **H-1B at Series C** (verify): a16z + Bessemer backed, likely 100-200 employees at Series C. Higher H-1B probability than earlier-stage startups, but not confirmed. Ask in first recruiter contact.

---

## C) Level and Strategy

**Level detected:** Mid-level infra/platform engineer. $150K–$400K spans a wide range; realistic for non-senior: $165K–$220K base + Series C equity. JD doesn't specify level explicitly — interpret as 2-4 year equivalent.

**Core pitch:**
> "I built the exact infrastructure stack Doppel is scaling. Terraform IaC for multi-AZ ECS Fargate with auto-rollback — production in TiMoto. Prometheus + Grafana observability with 99.9% uptime — production in TiMoto. CI/CD automation with 90% deployment time reduction — production at Develop for Good. I don't have Elasticsearch experience, but I've run Kubernetes workloads and distributed data systems at scale; it's a new tool on top of a foundation I already have. And I build AI agent infrastructure — which is what your SOC agents are."

**On Elasticsearch gap:**
> "I haven't operated Elasticsearch in production, but I've run distributed data systems at scale — PostgreSQL with N+1 optimization, Redis with 85% cache hit rates, gRPC pipelines with exactly-once delivery. The K8s operator model and the distributed systems thinking carry over. I'm ramping up on Elasticsearch specifically for this work."

**On seniority:**
> "The scope of my 9 months at TiMoto is unusual for a new grad — I own backend, infra, and ML serving end-to-end as the primary engineer. I've debugged production deadlocks, designed circuit breakers, and operated on-call. The infrastructure is running at 99.9% uptime. I'm asking you to assess the impact, not the timestamp."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Doppel stated range | $150,000–$400,000 + equity |
| Harry target | $150K–$200K |
| Harry minimum | $140K |
| Realistic band for non-senior (Series C) | $165K–$220K base estimated; equity meaningful at Series C stage (a16z + Bessemer backed) |
| Assessment | Floor ($150K) hits Harry's minimum exactly; ceiling is senior/staff; negotiate toward $175K citing production infra ownership |
| Series C equity | More mature than seed/A/B; lower dilution risk; likely 2-5 years from liquidity event at current growth |

**Cybersecurity market:** Social engineering defense is one of the hottest segments post-2024 (AI-powered attacks driving demand). Doppel's 150B entity/day scale + a16z backing indicates strong product-market fit. Series C at this trajectory = exit potential within 3-5 years.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet 2 (infra) | Generic multi-AZ framing | Lead: "Defined core infrastructure using Terraform IaC — multi-AZ ECS Fargate with explicit lifecycle management (create, update, scale, destroy); reproducible, version-controlled environments; 99.9% uptime SLO, 44% cost reduction; auto-rollback on health check failure" | Mirrors Doppel's exact Terraform use case |
| 2 | TiMoto bullet (observability) | Metrics framing | Emphasize tracing: "Built observability and distributed tracing stack — CloudWatch for infra health, Prometheus + Grafana for application metrics, gRPC inter-service tracing for production debugging; on-call rotation with runbooks and post-mortems" | Mirrors Doppel's "metrics, logging, distributed tracing" work example |
| 3 | Develop for Good bullet 1 | CI/CD + JWT | Emphasize staging + CI/CD: "Designed staging environment with automated integration testing — 90% deployment time reduction via CI/CD (GitHub Actions); JWT stateless BaaS enabling 500+ concurrent users with horizontal auto-scaling" | Mirrors Doppel's staging environment work example |
| 4 | Skills section | Distributed Systems leads | Cloud & Infrastructure leads (Kubernetes prominent, Terraform highlighted): "AWS (ECS Fargate, EKS, EC2, S3, RDS), GCP, Terraform, **Kubernetes**, Docker, CI/CD, CloudWatch, Prometheus, Grafana" | Infrastructure-first role; K8s and Terraform should be immediately visible |
| 5 | Pulumi project | Multi-cloud generic | Add Terraform/IaC framing: "Submitted Go CLI features enabling reproducible multi-cloud (AWS/Azure/GCP) provisioning — developer tooling for infrastructure-as-code" | Reinforces IaC contribution at OSS level |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Terraform IaC — reproducible environments | TiMoto ECS Fargate Terraform | 3-person team needed reliable, reproducible infrastructure without a dedicated DevOps engineer | Zero config drift; auto-scaling; auto-rollback; 44% cost reduction | Terraform IaC for ECS Fargate: create/update/scale/destroy lifecycle; explicit dependency graph; health check-triggered rollback; CloudWatch alarms wired to autoscaling | 44% cost reduction; 90% deployment time reduction (DfG); zero unplanned downtime | Terraform's value isn't the initial setup — it's the 6-month review when you need to know exactly why a configuration decision was made. IaC is documentation that's also executable |
| 2 | Observability + distributed tracing | TiMoto Prometheus + Grafana | Production distributed system with ML pipeline — needed visibility across both infra health and pipeline correctness simultaneously | Two-layer observability: infra SLOs + application correctness metrics | CloudWatch for infra (uptime, latency, autoscaling events); Prometheus + Grafana for application metrics (eval success rate, OOM rate, gRPC latency); LLM-as-a-judge for quality | 99.9% uptime SLO; zero undetected pipeline failures | For distributed systems handling high-volume data (like Doppel's 150B entities), you need different metric classes: infra health (is the system alive?), throughput (is it processing?), and correctness (is it making good decisions?). Single-layer observability misses the hard failures |
| 3 | Staging environments + safe releases | Develop for Good CI/CD | Non-profit client needed frequent deployments without risk to production users | 90% deployment time reduction, zero production incidents from bad deploys | GitHub Actions CI/CD pipeline with automated integration tests; staging environment with production-equivalent data; gated promotion to production; rollback scripts for failed deploys | 90% deployment time reduction; maintained production uptime across all release cycles | The staging environment's value isn't catching bugs you already know about — it's catching integration failures you didn't anticipate. The most dangerous bugs are the ones that only appear when multiple services interact under production-like load |
| 4 | Kubernetes at scale | TiMoto EKS + vLLM | TiMoto ML serving needed both container orchestration (ECS) and ML inference (K8s-managed vLLM) | Zero-OOM ML serving at production traffic | ECS Fargate for application services; EKS for ML inference engine with vLLM (PagedAttention for memory management); K8s resource limits and health checks for automatic restarts | Zero OOM failures; zero unplanned downtime during ML serving | K8s is a tradeoff: operational complexity in exchange for scheduling intelligence. For workloads with variable resource demands (like ML inference or Doppel's variable alert volume), K8s wins because it can bin-pack and scale faster than human operators |
| 5 | Backend engineering at scale | Chrome IPC + TiMoto gRPC | Two different scale challenges: Chrome 3B users at <50ms; TiMoto exactly-once delivery at production traffic | Sub-50ms p99 at 3B-user scale; zero data loss in gRPC pipeline | Chrome: Protocol Buffers IPC, lock-free trie replacing mutex-based search; TiMoto: happens-before analysis on gRPC deadlock, lock ordering redesign | 96% settings latency reduction; zero data loss in production pipeline | Scale is a design constraint, not a deployment strategy. You can't add servers to fix a lock contention bug or a schema evolution problem. The architectural decisions made at v1 determine whether v10 runs. |
| 6 | Distributed search + data at scale (Elasticsearch bridge) | TiMoto data pipeline + Pulumi multi-cloud | Harry's analog: querying millions of records efficiently in production; managing multi-cloud distributed state | Sub-100ms PostgreSQL queries at 10K+ records; multi-cloud provisioning | PostgreSQL composite indexing (N+1 → sub-100ms); Pulumi Raft/Paxos study for distributed consensus | 30× query improvement; Pulumi under active review | Elasticsearch solves the full-text and analytics query problem that SQL struggles with at alert-volume scale. The distributed systems principles I've applied to gRPC, PostgreSQL, and multi-cloud IaC carry directly to operating Elasticsearch clusters. The tool is new; the reasoning is the same. |

**Recommended case study:** TiMoto infrastructure stack — frame as "mini Doppel infrastructure": high-volume data ingestion (vLLM + gRPC), Terraform IaC for reproducibility, Prometheus + Grafana observability, 99.9% uptime SLO. "The difference in scale is 6 orders of magnitude. The engineering principles are identical."

**Red-flag questions:**
- *"You don't have Elasticsearch experience."* → "That's accurate. What I have is the K8s and distributed systems foundation that Elasticsearch runs on. I've operated distributed data stores at scale, tuned query performance, and managed cluster lifecycle with Terraform. Elasticsearch is a new tool on top of a foundation I already have. I'm actively learning it."
- *"Experienced backend engineer — you have 9 months."* → "9 months of scope that most engineers don't see in 2 years. I own backend, infra, and ML serving simultaneously at TiMoto. I've debugged production deadlocks, designed circuit breakers, and run on-call. The system runs at 99.9% uptime with 44% lower cost than the initial design. Evaluate the impact, not the timestamp."
- *"Work authorization?"* → "F-1 status. Can you confirm Doppel's H-1B sponsorship policy? I want to make sure we're aligned on the long-term path before investing time on both sides."
- *"Cybersecurity background?"* → "Zero cybersecurity background. But the infrastructure work is domain-agnostic — building reproducible K8s environments and observability stacks doesn't require deep security knowledge. The domain comes with the job; I learn it by building the systems that serve it. My AI agent infra at TiMoto maps closely to what your SOC agents need: reliable serving, low latency, correctness metrics."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active ("Apply for this Job") on Ashby | Positive |
| Comp disclosed | $150K–$400K explicitly stated | Positive |
| JD specificity | Concrete recent work examples (Elasticsearch on K8s, Terraform IaC, staging environment, observability stack) — not generic bullets | Positive |
| Company status | Doppel — Series C; a16z + Bessemer VP backed; active cybersecurity platform scanning 150B entities daily | Positive |
| Investors | a16z + Bessemer = top-tier credibility; funding confirms company is real and scaling | Positive |
| H-1B | Series C, a16z + Bessemer backed — likely 100-200 employees; H-1B probable but unconfirmed | ⚠️ Ask early |
| Growth signal | "Rapidly growing Series C" + "scale up engineering organization" = active hiring, not maintenance mode | Positive |

---

## Keywords extracted

Infrastructure, backend engineer, Kubernetes, Terraform, IaC, Elasticsearch, observability, distributed tracing, metrics, logging, staging environment, CI/CD, multi-cloud, PostgreSQL, social engineering defense, cybersecurity, phishing, impersonation, fraud detection, AI agents, digital risk, Series C, a16z, Bessemer, San Francisco, New York, hybrid

---

## Machine Summary

```yaml
company: Doppel
role: Software Engineer, Infrastructure
date: 2026-06-09
url: https://jobs.ashbyhq.com/doppel/aba5c986-7e85-4f79-8553-e85634400b78
score: 3.8
archetype: Platform / Cloud Infrastructure + SRE
location: "San Francisco or New York — hybrid; relocation from Atlanta required"
comp_range: "$150K–$400K + equity; realistic non-senior band ~$165K–$220K; negotiate toward $175K; Series C equity has upside"
visa_risk: "F-1 — H-1B likely at Series C (a16z + Bessemer, ~100-200 employees) but unconfirmed; ask in first recruiter contact"
legitimacy: High Confidence
recommendation: "Apply (3.8/5) — Platform/Cloud Infrastructure archetype exact match (Terraform, K8s, observability, CI/CD). JD work examples map directly to Harry's TiMoto production stack. Primary gap: Elasticsearch (mentioned explicitly). Cybersecurity domain is new but infrastructure is domain-agnostic. H-1B unconfirmed — ask early."
```
