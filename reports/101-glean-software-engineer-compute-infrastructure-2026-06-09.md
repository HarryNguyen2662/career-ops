# Evaluation: Glean — Software Engineer, Compute Infrastructure

**Date:** 2026-06-09
**URL:** https://job-boards.greenhouse.io/gleanwork/jobs/4704106005
**Archetype:** Platform / Cloud Infrastructure Engineer + Site Reliability Engineer
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** output/101-glean-software-engineer-compute-infrastructure-harry-nguyen-2026-06-09.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Platform / Cloud Infrastructure Engineer + SRE — Kubernetes runtime, multi-cloud (GCP/AWS/Azure), IaC, SLOs, cost optimization for AI/search workloads |
| Domain | Work AI infrastructure — Kubernetes-based runtime platform powering Glean's search, AI assistant, and agentic workloads; 1000+ employees, 50+ industries, 5x growth target |
| Function | Build — Kubernetes runtime primitives, multi-cloud infrastructure, IaC patterns, observability, cost attribution, on-call rotation |
| Seniority | Unlabeled SWE — "backend/platform engineer who enjoys working close to the metal"; comp ($140K–$220K) suggests mid-level; no explicit years requirement |
| Location | Mountain View, CA — **4 days/week hybrid** (also stated as Palo Alto office Mon/Wed/Fri in form); relocation from Atlanta required; no explicit relocation support mentioned |
| Team | Platforms organization — Runtime Infra; partners with platform, data, and product engineering |
| Comp | $140,000–$220,000 base + equity |
| TL;DR | Glean Compute Infrastructure — Kubernetes + multi-cloud + IaC + SLOs + AI workloads. Harry's TiMoto infra stack (ECS Fargate, EKS, Terraform, circuit breakers, Prometheus/Grafana, 99.9% uptime) and Pulumi multi-cloud K8s contributions are a direct match. Comp floor ($140K) is at Harry's walk-away minimum. Location (4-day Mountain View hybrid) requires relocation from Atlanta; no explicit relocation support. H-1B expected. **Apply — strong platform/SRE archetype match; negotiate comp toward $165K+ and confirm relocation support in first recruiter call.** |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| Kubernetes-based runtime primitives, service orchestration, autoscaling | TiMoto: EKS (Kubernetes) in production; Pulumi: Go CLI for multi-cloud K8s/AWS/Azure/GCP provisioning; Skills: Kubernetes | ✅ Direct — K8s in production + multi-cloud OSS |
| Multi-cloud infrastructure (GCP, AWS, Azure) | AWS: ECS Fargate, EKS, EC2, S3, RDS (production); Pulumi: AWS/Azure/GCP provisioning contributions; Skills: GCP listed | ✅ Direct — AWS production; GCP/Azure via Pulumi |
| Infrastructure-as-code patterns | TiMoto: Terraform IaC for ECS Fargate, multi-AZ, auto-scaling; Skills: Terraform; Pulumi OSS contributor | ✅ Direct |
| Observability — SLOs, dashboards, alerts, safe rollout/rollback | TiMoto: CloudWatch + Prometheus + Grafana; 99.9% uptime SLO; auto-rollback on health check failure; on-call rotation | ✅ Direct |
| Cost optimization for platform services | TiMoto: 44% cost reduction ($40–60/month); cost-conscious infra design; Terraform policies for auto-scaling | ✅ Direct — cost awareness is explicit in CV |
| Distributed systems fundamentals | TiMoto: gRPC, circuit breakers, exactly-once semantics, multi-AZ; Pulumi: Raft/Paxos study | ✅ Direct |
| High-throughput, low-latency production services | Google Chrome: sub-50ms p99, 10K+ req/sec, 3B+ users; TiMoto: sub-50ms p99, 99.9% uptime | ✅ Direct |
| End-to-end ownership: design, implementation, deployment, operations | TiMoto: primary engineer on 3-person team — owns all three layers | ✅ Direct — startup ownership model |
| On-call rotation, incident response, runbooks | TiMoto: on-call rotation, root-cause analysis, runbooks documented (in cv.md) | ✅ Direct |
| Python/Go/Java/C++ proficiency | Python: TiMoto production; Go: Pulumi OSS; C++: Google Chrome; Java: listed in Skills | ✅ Python + Go + C++ direct |
| AI workloads context | TiMoto: vLLM, PagedAttention, ML serving, LLM-as-a-judge evaluation — directly relevant to Glean's AI search/agent infrastructure | ✅ Direct — AI workload experience |
| H-1B | F-1 — Glean: 1000+ employees, 25+ countries, well-funded; H-1B expected but unverified by LCA in this session | ⚠️ Expected; confirm in process |
| Mountain View 4-day hybrid | Harry Atlanta-based; 4-day in-office = effectively full relocation; no explicit relocation support in JD | ⚠️ Relocation required; must confirm support |

**Gaps:**

1. **Location — 4-day Mountain View hybrid.** The most significant practical barrier. Harry is in Atlanta; 4 days/week in Mountain View is effectively full relocation. The JD does not explicitly mention relocation support (unlike Airbnb which called it out, or Plaid which didn't mention it). Must confirm in first recruiter call: "Is relocation support available?" The form shows the Palo Alto office is Mon/Wed/Fri (3 days) — the JD's "4 days" may be aspirational or reflect a recent policy change. Either way, relocation from Atlanta is required.

2. **Scale gap on Kubernetes.** Glean targets "5x customers and traffic" — their K8s footprint is significantly larger than TiMoto's EKS deployment. Mitigation: Pulumi multi-cloud K8s provisioning contributions (AWS/Azure/GCP) demonstrate K8s knowledge at cross-cloud depth. Chrome at 3B+ users demonstrates the scale instinct.

3. **Comp floor at minimum.** $140K floor = Harry's walk-away minimum. For a 4-day hybrid in Mountain View (high cost of living), $140K base would be uncomfortable relative to SF/NYC offers. Target negotiating toward $165K–$185K — well within the range's upper half.

4. **Java.** Form asks "years of experience with Go/Python/Java/C++?" Harry's Java is coursework-level (no Java production bullets in CV). Python + Go + C++ are the strong answers; Java is honest-but-thin. Not a blocker.

---

## C) Level and Strategy

**Level detected:** Mid-level SWE. The $140K–$220K range without explicit years = L3–L4 equivalent at a growth-stage startup. Harry enters at the lower end of the range given 9 months TiMoto.

**Core pitch — infrastructure that keeps AI alive:**
> "At TiMoto I built the cloud infrastructure layer from scratch — multi-AZ ECS Fargate, Terraform IaC, circuit breakers, auto-rollback, 99.9% uptime at $40–60/month cost. That's the same problem Glean's Compute Infrastructure team solves: reliable, cost-efficient runtime for AI workloads. I didn't just configure AWS — I designed for failure modes, built the cost controls, and ran on-call. Glean's AI search runs on infrastructure like what I've built."

**On multi-cloud:**
> "AWS is my production environment. My Pulumi contributions touch all three — AWS, Azure, GCP — for K8s and infrastructure provisioning. I've studied how the primitives differ across clouds; I haven't operated GCP at production scale. That's the ramp."

**On comp:**
> "Given the Mountain View cost of living and 4-day hybrid, I'm targeting $165K–$185K base. The Glean range supports that. I have offers in NYC at $176K+ base; Mountain View should be comparable or higher."

**On relocation:**
> "Open to relocating to the Bay Area — I'd want to confirm relocation support is available before moving forward. Given the 4-day office requirement, this is a full relocation, not a hybrid situation."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Glean stated range | $140,000–$220,000 base + equity |
| Glean funding/valuation | Well-funded growth-stage company; 1000+ employees; meaningful equity upside |
| Platform/Cloud Infra SWE (mid-level, Bay Area, 2026) | $175K–$250K TC at comparable-stage companies (Databricks, Figma, Notion) |
| Expected Glean offer for Harry's profile | $155K–$180K base (lower half of range, reflecting early career) |
| Harry target | $150K–$200K |
| Harry minimum | $140K (floor matches JD floor — comp floor is tight) |

The $140K floor is a concern. At Mountain View cost of living, $140K base is functionally lower than $176K in NYC. Target negotiating to at least $165K base — mid-range of Glean's band — before accepting. Use Plaid ($176K+) and Baseten ($165K+) as leverage.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet order | vLLM or gRPC first | Lead with infra: "Architected multi-AZ ECS Fargate with Terraform IaC, CloudWatch + Prometheus + Grafana observability, circuit breaker pattern — 99.9% uptime, 44% cost reduction; auto-rollback on health check failure; on-call rotation" | SRE/infra archetype — lead with the SLO story |
| 2 | TiMoto bullet 2 | Varies | "Designed and maintained gRPC inter-service layer; resolved production deadlock by tracing shared resource acquisition conflicts — exactly-once delivery at sub-50ms p99" | Distributed systems fundamentals signal |
| 3 | Skills: row order | ML & AI or Distributed leads | Cloud & Infrastructure first (AWS/EKS/Terraform/K8s); Distributed Systems second | Glean wants platform/infra engineering first |
| 4 | Pulumi project | Go/IaC framing | Lead with multi-cloud K8s: "Submitted Go CLI features enabling multi-cloud K8s, AWS/Azure/GCP provisioning — under active review by core maintainers" | Glean is multi-cloud; Pulumi = direct K8s multi-cloud signal |
| 5 | TiMoto bullet 3 | Backend/LLM | Mention AI workloads context: "Led Python (FastAPI/Django) backend + vLLM ML serving for a 3-person team — production AI workflows powering intelligent search and LLM evaluation pipelines" | Glean's product is AI search; show you understand AI workloads from the infra side |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Reliable platform infrastructure — SLOs, auto-rollback | TiMoto multi-AZ + circuit breakers | 3-person startup, no dedicated SRE; needed production HA without operational overhead | 99.9% uptime SLO, $40–60/month infra cost | Multi-AZ ECS Fargate, Terraform IaC, circuit breaker with fail-open degraded mode, CloudWatch alerting, auto-rollback on health check failure | 44% cost reduction; zero unplanned downtime | HA is an architecture decision made on day 1. Circuit breakers should fail into a degraded state, not silently — that's the difference between "service is slow" and "users see errors" |
| 2 | Kubernetes + multi-cloud infrastructure | Pulumi multi-cloud K8s contributions | Pulumi needed Go CLI features for cross-cloud K8s and infrastructure provisioning | Go features under active review by core maintainers (AWS/Azure/GCP K8s) | Submitted Go CLI for multi-cloud provisioning; tested across cloud providers; analyzed Raft/Paxos for distributed state correctness | OSS K8s multi-cloud contributions under active review | Multi-cloud K8s looks simple until you hit provider-specific scheduling semantics. The hard part isn't writing the manifests; it's the autoscaling policies that differ by cloud |
| 3 | Cost optimization for compute platform | TiMoto cost reduction | Ad-hoc AWS infra was expensive and non-reproducible; no cost attribution or auto-scaling | 44% cost reduction ($40–60/month), zero config drift | Terraform IaC with explicit resource sizing; auto-scaling policies tied to business metrics; CloudWatch cost alerts; circuit breaker reduces waste on degraded traffic | 44% cost reduction without sacrificing reliability | The cost optimization problem is really a resource attribution problem. Once you can see which service is spending what, the waste becomes obvious. Terraform + CloudWatch cost alarms is the minimum viable cost control for a production system |
| 4 | Observability — SLOs, dashboards, alerts | TiMoto Prometheus + Grafana + CloudWatch | Production AI system needed both infra SLOs (uptime, latency) and model quality metrics (output correctness) — different monitoring layers | 99.9% uptime SLO compliance; LLM-as-a-judge evaluation at 100% success rate | CloudWatch for infra SLOs; Prometheus + Grafana for latency/throughput dashboards; LLM-as-a-judge for model quality; structured alerts at each layer | Two separate observability layers for AI systems — infra tells you the service is up; model metrics tell you the outputs are correct | An AI system can be 100% "up" by infra metrics while producing garbage outputs. You need both layers or you're flying blind on the part that matters to users |
| 5 | Incident response + production debugging | TiMoto gRPC deadlock | Production system stopped under concurrent load — silent failure, no clear error | Restore 100% processing | Traced happens-before graph across two services; identified lock ordering violation; redesigned call sequencing; added monitoring for the specific failure mode | Zero recurrence; new monitoring alert catches future violations | Incident response starts with reproducing the failure in a controlled environment before touching production. The second step is understanding the system's concurrency model well enough to predict where else the same bug could exist |
| 6 | End-to-end ownership in fast-moving startup | TiMoto — 3-person primary engineer | Startup with shifting priorities; Harry owns backend + infra + ML simultaneously | Production SLOs (99.9% uptime, sub-50ms p99) despite context-switching | Designed for replaceability: IaC, runbooks, CI/CD with auto-rollback; built monitoring first; prioritized by business impact | Zero unplanned downtime on startup timeline | Ownership without documentation is a single point of failure — you. Runbooks and IaC are the way to make a system survivable when you're context-switching between three layers |

**Recommended case study:** TiMoto infra stack — walk through: Terraform IaC design → multi-AZ circuit breaker → CloudWatch SLO monitoring → auto-rollback on health check failure → cost reduction. Frame as "this is what Glean's runtime platform looks like at startup scale — the engineering decisions transfer directly."

**Red-flag questions:**
- *"Relocation — are you available for Mountain View 4 days/week?"* → "Open to relocating to the Bay Area for the right role. I'd want to confirm relocation support is available — can you clarify what Glean offers? With 4-day hybrid, I'm treating this as a full relocation decision, not a remote setup."
- *"Years of Go/Python/Java experience?"* → "Python: ~2 years in production (TiMoto + DfG internship). Go: ~1 year via OSS contributions to Pulumi (multi-cloud K8s). C++: ~1 year production at Google Chrome. Java: coursework, not production. Python and Go are my primary cloud/infra languages for this role."
- *"Years of GCP/AWS/Azure experience?"* → "AWS: ~2 years production (TiMoto: EKS/ECS/EC2/S3/RDS; DfG: BaaS). GCP + Azure: ~1 year via Pulumi multi-cloud contributions (provisioning across all three). AWS is my primary production cloud; GCP/Azure I know via tooling."
- *"What AI tools do you use?"* → "Claude Code for development workflows — writing code, debugging, architecture design. GitHub Copilot for autocomplete in the IDE. Codex for scripting and automation tasks. Cursor for context-aware code navigation. At TiMoto, I also built with the LLM APIs directly (Claude, GPT) — that's a different level of familiarity than just using them as dev tools."
- *"Comp expectations?"* → "Given Mountain View cost of living and the 4-day office requirement, I'm targeting $165K–$185K base. I have offers in the $176K+ range in NYC; Bay Area should be comparable or higher. The Glean equity story matters to me — can you share the equity grant range for this level?"

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active ("Apply") on Greenhouse | Positive |
| Comp disclosed | $140K–$220K explicitly stated | Positive |
| Company status | Glean — recognized by Fast Company Top 10 (2025), CNBC Disruptor 50, Bloomberg AI Startups (2026), Forbes AI 50; 1000+ employees; enterprise customers across 50+ industries | Positive |
| JD specificity | Named responsibilities (K8s runtime, multi-cloud, IaC, SLOs, cost attribution, on-call), named example work (autoscaling patterns, scheduling integrations, multitenancy) | Positive |
| Application form specificity | Role-specific form questions (Go/Python years, GCP/AWS years, hybrid policy, AI tools usage) — not generic | Positive |
| "New" badge | Greenhouse shows "New" label — freshly posted | Positive |
| H-1B | 1000+ employees, 25+ countries — H-1B sponsorship standard at this scale | Positive (expected) |
| AI-First Mindset section | Company-wide AI fluency mandate with interview exercise — genuine culture signal, not marketing | Positive |

---

## Application Form Answers

**Q: Are you willing and able to commit to the hybrid policy if hired?**
> Yes, with the expectation of relocating to the Bay Area. I'm currently in Atlanta and would treat this as a full relocation decision. I'd want to confirm relocation support is available before accepting — please connect me with someone on the People team to discuss. I'm fully committed to 4-day in-office once I'm local.

**Q: How did you hear about Glean?**
→ [Fill in your actual source — job board, LinkedIn, referral, etc.]

**Q: Years of experience with Go/Python/Java/C++?**
> Python: ~2 years (production at TiMoto + DfG internship). Go: ~1 year (Pulumi OSS contributions, multi-cloud K8s). C++: ~1 year production (Google Chrome internship). Java: coursework. Primary languages for this role: Python + Go.

**Q: Years of experience GCP/AWS/Azure?**
> AWS: ~2 years production (TiMoto: EKS, ECS Fargate, EC2, S3, RDS; DfG: AWS BaaS). GCP + Azure: ~1 year via Pulumi multi-cloud contributions across all three clouds. AWS is my primary production cloud.

**Q: What AI tools are you currently using today and how?**
> Daily: Claude Code for architecture design, debugging complex systems, and code generation. GitHub Copilot for inline autocomplete and refactoring. Cursor for context-aware code navigation in large codebases. At TiMoto I also build directly with LLM APIs (Claude, GPT) for production workflows — that's using the tools to build AI systems, not just to write code faster. The distinction matters for Glean's infrastructure role: I understand AI workloads from both the developer tool side and the production serving side.

---

## Keywords extracted

Kubernetes, multi-cloud, GCP, AWS, Azure, infrastructure-as-code, Terraform, SLOs, observability, Prometheus, Grafana, autoscaling, multitenancy, circuit breakers, runtime infrastructure, compute platform, Python, Go, distributed systems, cost optimization, on-call, incident response, AI workloads, Mountain View, hybrid

---

## Machine Summary

```yaml
company: Glean
role: Software Engineer, Compute Infrastructure
date: 2026-06-09
url: https://job-boards.greenhouse.io/gleanwork/jobs/4704106005
score: 4.0
archetype: Platform / Cloud Infrastructure Engineer + Site Reliability Engineer
location: Mountain View, CA — 4-day hybrid; full relocation from Atlanta required; no explicit relocation support mentioned in JD
comp_range: "$140K–$220K base + equity; floor at Harry's walk-away minimum — negotiate toward $165K+"
visa_risk: "F-1 — H-1B expected (1000+ employees, 25+ countries, well-funded); unverified by LCA in this session"
legitimacy: High Confidence
recommendation: "Apply — primary archetype match (Platform/Cloud Infra + SRE). K8s + multi-cloud + Terraform + SLOs + AI workloads = exact TiMoto+Pulumi stack. Comp floor ($140K) at minimum — negotiate toward $165K+ citing Plaid ($176K) and Baseten ($165K) offers as leverage. Must confirm relocation support in first recruiter call (4-day Mountain View = full relocation from Atlanta)."
```
