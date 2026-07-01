# Evaluation: Palantir Technologies — Software Engineer, New Grad - Production Infrastructure

**Date:** 2026-06-01
**URL:** https://jobs.lever.co/palantir/e1a6c138-98bf-45e2-97f7-2c70371cc38a
**Archetype:** SRE / Platform Engineer (primary) + Systems Software Engineer
**Score:** 3.5/5
**Legitimacy:** High Confidence
**PDF:** output/027-palantir-harry-nguyen-2026-06-01.pdf

---

## A) Role Summary

| Field | Value |
|-------|-------|
| Archetype | SRE / Platform Engineer (primary) + Systems Software Engineer |
| Domain | Production infrastructure, fleet deployment, observability |
| Function | Build — full product lifecycle ownership |
| Seniority | New Grad |
| Location | New York, NY — Hybrid |
| Team size | Small teams within Production Infrastructure org |
| TL;DR | Own Kubernetes-based PaaS, fleet-wide deployment (Apollo), and observability (Signals) for Palantir's most critical government and enterprise deployments worldwide |

---

## B) Match with CV

| JD Requirement | CV Match | Strength |
|----------------|----------|----------|
| Kubernetes-based PaaS, production clusters | K8s in skills; ECS Fargate + Terraform at TiMoto | Strong |
| Fleet deployment / change-management (Apollo) | CI/CD, health-check auto-rollback, Terraform (TiMoto) | Strong |
| Observability / alerting (Signals) | CloudWatch, Prometheus, Grafana at TiMoto | Strong |
| Java, Go backend | Go (skills + Pulumi), Java (skills) | Strong |
| Cilium, Envoy, Grafana, React, Redux | Grafana (skills), React/TypeScript (Chrome, TiMoto); gap: Cilium/Envoy | Partial |
| Data structures, storage, cloud infra | PostgreSQL, Redis, AWS, Terraform — end-to-end | Strong |
| C++, Python, JavaScript/TypeScript | C++ (Chrome), Python + TypeScript (TiMoto, Chrome) | Strong |
| On-call, incident response, runbooks | TiMoto: on-call rotation, root-cause analysis, runbooks | Strong |
| **Security clearance or eligibility to obtain** | **F-1 visa — structurally ineligible for US security clearance** | **Critical risk** |

**Gaps:**

1. **Security clearance (HARD structural concern)** — US security clearances require US citizenship or lawful permanent residency. F-1 holders are ineligible. Palantir's Production Infrastructure primarily serves defense/gov agencies. Mitigation: Apply and immediately ask recruiter whether an uncleared commercial track (Foundry/AIP) exists within this org. If clearance is hard-required, this is likely disqualifying.
2. **Cilium/Envoy** — K8s networking tools not in CV. Adjacent to gRPC service mesh patterns; learnable in weeks.
3. **Apollo/Rubix/Mission Manager** — internal Palantir products; on-the-job learning.

---

## C) Level and Strategy

Level match: **perfect** — title explicitly says "New Grad."

**"Ship without underselling" plan:**
- "I ran distributed production systems across gRPC, ML serving, and AWS/Terraform with 99.9% uptime on a 3-person team — the Production Infrastructure org is where I want to scale that."
- Tie Chrome to scale: "Shipped C++ IPC to 3B+ users at 95% test coverage with senior Chrome engineer review."
- "K8s in production at TiMoto; Grafana for inference SLOs; Apollo's rollback pattern is what I built on ECS."

**"If they ask about clearance" plan:** "I'm on F-1 and understand that limits clearance eligibility. Is there an uncleared commercial track within Production Infrastructure? If clearance is a day-one hard requirement, I'd rather know now."

---

## D) Comp and Demand

| Metric | Value | Source |
|--------|-------|--------|
| JD base | $145,000–$155,000/year + RSUs + sign-on | Palantir JD (Lever) |
| Palantir new grad TC | $152,989 median; $127K–$187K range | Glassdoor |
| Palantir SWE NYC (all levels) | $154K–$315K | Levels.fyi |
| Harry's target | $150K–$200K TC | profile.yml |
| Harry's minimum | $140K base | profile.yml |

Base at the low end of target. Total comp with RSUs + sign-on likely $175K–$210K for new grad — within range. RSU vesting schedule not disclosed; ask during offer stage.

**Hiring status:** IT/recruiting layoffs in early 2026 but Palantir is actively hiring engineers in summer 2026.

---

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | TiMoto bullet 4 | Strengthen Kubernetes; call out "health-check-based auto-rollback" explicitly | Apollo is K8s-native |
| 2 | TiMoto bullet 5 | Keep as-is — on-call, runbooks, RCA maps to Signals/SRE | Direct language match |
| 3 | Skills — Cloud | Elevate Kubernetes; add "service mesh / Envoy" | JD names Cilium, Envoy |
| 4 | Cover letter | "Production Infrastructure at TiMoto → Production Infrastructure at Palantir" | Clear narrative continuity |
| 5 | Pulumi project | Emphasize multi-cloud provisioning + Raft/Paxos correctness | Maps to fleet deployment and consensus guarantees |

---

## F) Interview Plan

| # | JD Requirement | Story | Result | Reflection |
|---|----------------|-------|--------|------------|
| 1 | Production reliability, incident response | **TiMoto gRPC deadlock** — concurrent calls caused deadlock; traced shared resource conflicts, redesigned sequencing | 100% eval success, sub-50ms p99 | Would add distributed tracing earlier |
| 2 | Kubernetes/fleet deployment | **TiMoto multi-AZ ECS + Terraform + auto-rollback** | 99.9% uptime, 44% cost cut | K8s gives finer pod scheduling; next step from ECS |
| 3 | Observability (Signals) | **TiMoto CloudWatch + Prometheus/Grafana** for vLLM SLOs | Zero OOM failures; real-time batch saturation visibility | Add anomaly detection vs threshold-only alerts earlier |
| 4 | Scale + correctness | **Google Chrome: lock-free trie** eliminating mutex contention | 96% latency reduction, shipped to 3B+ users, zero regressions | Perf benchmarks in CI gate would catch regressions pre-PR |
| 5 | Go/Java, rapid learner | **Pulumi Go CLI contributions** to 24K-star open source | PRs under active review | Read consensus-layer code before guessing at invariants |
| 6 | End-to-end ownership | **TiMoto vLLM selection** — PagedAttention vs naive inference, owned deployment | Zero OOM at production traffic | Document tradeoff analysis, not just the decision |

**Recommended case study:** TiMoto Production Infrastructure (vLLM + gRPC + Terraform/ECS). Walk through architecture → deadlock incident → SLO setup.

**Red-flag questions:**
- *"You don't have deep Kubernetes experience"* → "I run K8s at TiMoto. The scheduler, health check, and rollback patterns are the same across ECS/EKS. Apollo's model is conceptually identical to what I built."
- *"Can you get a security clearance?"* → "I'm on F-1, which limits clearance eligibility. Is there an uncleared commercial track within Production Infrastructure? If cleared work is hard-required from day one, I'd want to know before both of us invest further."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active, direct apply link renders | Positive |
| Posting age | First seen in scan-history 2026-06-01 | Positive |
| Salary disclosed | $145K–$155K + RSU + sign-on explicitly stated | Positive |
| JD specificity | Names Apollo, Rubix, Signals, Mission Manager + specific tech (K8s, Cilium, Envoy) | Positive |
| Requirements realism | New Grad title + entry-level requirements, no contradiction | Positive |
| Hiring signals | Aggressively hiring engineers in summer 2026 | Positive |
| Repost pattern | No prior URL in scan-history for this role | Positive |

**Context:** Production Infrastructure Internship version (bc5c4098) expired; this New Grad version is freshly posted and active.

---

## Keywords Extracted

Production Infrastructure, Kubernetes, Kubernetes-based PaaS, Apollo, Rubix, Signals, Mission Manager, observability, alerting, fleet deployment, change-management, microservices, Cilium, Envoy, Grafana, React, Redux, Java, Go, TypeScript, Gradle, GitHub, distributed systems, cloud infrastructure, New Grad, Software Engineer
