# Evaluation: Skydio -- Software Engineer, Full Stack

**Date:** 2026-06-06
**URL:** https://www.skydio.com/jobs/067e1f47-9fba-4abf-b986-874d4d569706
**Archetype:** Full-Stack Engineer (adjacent to Backend / Distributed Systems)
**Score:** 3.5/5
**Legitimacy:** High Confidence
**PDF:** output/067-skydio-harry-nguyen.pdf

---

## A) Role Summary

| Field | Details |
|-------|---------|
| **Archetype** | Full-Stack Engineer (product-facing cloud platform) |
| **Domain** | Autonomous drone cloud platform (DFR, site security, inspection) |
| **Function** | Build/maintain backend services + React/TypeScript UI for cloud ops |
| **Seniority** | Junior / Mid (1-3+ years exp) |
| **Location** | San Mateo, CA — hybrid 3 days/week in office |
| **Comp range** | $110K--$180K base + equity (stock options) |
| **Team context** | Cross-functional: frontend, backend, autonomy, product, field teams |
| **TL;DR** | Build and maintain the cloud platform UI/backend for Skydio's autonomous drone ecosystem — React/TypeScript front, REST/GraphQL APIs back, AWS/K8s infra bonus. |

**Key responsibilities:**
- Implement and maintain backend services and APIs powering frontend experiences
- Enhance performance and reliability across the stack
- Build and iterate on UI/UX in Skydio's cloud platform
- Collaborate with autonomy, product, and field teams using real-world operational feedback

**Required:**
- 1-3+ years shipping customer-facing software across the stack
- Backend services experience (REST/GraphQL, service communication, data pipelines)
- Cloud/distributed architecture familiarity
- Performance, reliability, and maintainability understanding
- Modern web dev (React, TypeScript)
- Product intuition for time-sensitive, high-stakes environments
- Cross-team collaboration

**Bonus:** AWS/K8s/Temporal; interest in autonomy/robotics

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|---|---|---|
| Backend services / REST APIs | TiMoto: Django/FastAPI serving layer; Develop for Good: stateless BaaS on AWS with JWT | Strong |
| React / TypeScript | Google Chrome: event-driven TypeScript/React observer pattern, 68% delivery acceleration, 25K+ lines Chromium | Strong |
| Cloud / distributed architecture | TiMoto: multi-AZ ECS Fargate, Terraform IaC, CloudWatch; Develop for Good: AWS BaaS, auto-scaling | Strong |
| Performance and reliability | Google Chrome: 96% latency reduction (lock-free trie); TiMoto: 99.9% uptime, sub-50ms p99, circuit breaker | Strong |
| gRPC / service communication | TiMoto: gRPC inter-service layer, deadlock fix, production concurrency | Strong |
| Collaboration across teams | Google Chrome: collaborated with Chrome infra team, senior engineer reviews, design docs | Strong |
| 1-3+ years experience | TiMoto (Sep 2025--Present) + Google intern + Develop for Good -- ~1.5 years total (intern + current role) | Moderate |
| Data pipelines | Not directly mentioned in CV; adjacent via distributed systems work | Weak |
| Kubernetes (bonus) | Listed in skills (EKS); TiMoto infra experience | Moderate |
| AWS (bonus) | TiMoto: ECS Fargate, S3, RDS; Develop for Good: EC2/Lambda | Strong |
| Temporal (bonus) | Not in CV | Gap |
| Autonomy/robotics interest (bonus) | Not in CV; adjacent via production ML serving | Adjacent |

**Gaps:**

| Gap | Blocker? | Mitigation |
|-----|----------|-----------|
| Data pipelines | Nice-to-have | TiMoto's ML serving + PostgreSQL indexing covers adjacent territory; mention in cover letter |
| Temporal (workflow engine) | Bonus only | Not a blocker; acknowledge willingness to learn if asked |
| Robotics/autonomy domain | Bonus | Frame TiMoto ML serving + distributed systems as "production-critical systems under real-time constraints" -- analogous to autonomy stack concerns |
| 1-3 years exp | Potential | Harry has ~1.5 years total (internships + current); combined with Google Chrome pedigree this is defensible as 1+ years shipping production software |

**Summary:** Strong backend/cloud/React foundation. Google Chrome TypeScript/React work is direct evidence for the frontend requirement. TiMoto covers backend services, APIs, and cloud infra. Main pitch gap is lack of domain-specific robotics/autonomy experience -- position around "production systems under real-world constraints."

---

## C) Level and Strategy

**Level detected:** Junior-Mid (1-3+ years, team member, not staff or tech lead)

**Candidate's natural level for this archetype:** Harry fits the low end of this bracket. He has ~1.5 years of real production experience (not counting internships as YoE in the traditional sense, but in terms of shipped code: Google Chrome + TiMoto = both production). This is competitive for a "1-3 years" role.

**"Sell without overreaching" plan:**

1. **Lead with Google Chrome** -- 3B+ users, shipped to stable, reviewed by senior engineers. This establishes production credibility fast.
2. **Frame full-stack as natural state** -- Google (TypeScript/React) + TiMoto (Django/FastAPI APIs) + Google Chrome (IPC/Protobuf backend) = full-stack breadth proved in production.
3. **Autonomy framing** -- "I build systems where reliability and correctness under concurrency aren't optional -- at Chrome that meant 3B users; at TiMoto that means real-time ML inference SLOs. High-stakes production is my default context."
4. **Small team owner** -- Skydio is a hardware/software company; being primary engineer on 3-person backend+infra+ML stack is relevant. Frame as: "I own a production stack end-to-end, not just features in a ticket queue."

**"If they downlevel me" plan:**
- If they offer a lower band, negotiate 6-month performance review clause with explicit leveling criteria
- Base ask: $150K+; Skydio's range is $110K-$180K -- target top of range given Google pedigree and production ownership at TiMoto
- Equity: stock options are meaningful given $3.5B expansion announcement and potential IPO trajectory

---

## D) Comp and Demand

| Source | Data | Notes |
|--------|------|-------|
| Skydio JD (posted) | $110K--$180K base | For this specific role |
| Levels.fyi (general SWE) | $110K--$329K; median $195K total | Broader SWE band |
| Levels.fyi (SWE level) | $180K--$293K total | For confirmed L-band |
| 6figr.com 2026 | $179K--$315K total | All levels |
| H1B data | 33% above $200K, 45% $150K-$200K | Skydio H1B filings 2025-2026 |

**Analysis:**
- Posted base range ($110K-$180K) is on the lower end for Bay Area. For Harry at new-grad/junior level, realistic offer is likely $120K-$150K base + equity.
- Total comp target ($150K-$200K) requires significant equity to reach; Skydio is still private (stock options, not RSUs).
- Skydio's options value is speculative -- the $3.5B expansion signals potential IPO trajectory but pre-IPO options carry liquidity risk.
- Harry's walk-away is $140K total. This is achievable with a $130K+ base and some equity value, but base alone may land below minimum if offer is at $110K-$120K.
- **Comp risk: moderate.** Worth applying; negotiate hard for top of range.

**Demand trend:** High -- Skydio announced $3.5B manufacturing expansion (April 2026), creating 2,000+ direct jobs + 3,000 supplier roles. Engineering hiring is actively growing. 992 employees currently, significant headcount growth expected.

---

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---------|---------------|-----------------|-----|
| 1 | Summary | "distributed systems & ML serving" focus | Add: "React/TypeScript at Chromium scale; full-stack cloud platform development" | JD is explicitly full-stack; front-end credibility is critical for this role |
| 2 | TiMoto bullets | Backend/infra/ML focus | Add/emphasize: API design and Django serving layer; data pipeline aspects | JD requires backend services experience specifically |
| 3 | Google Chrome bullets | IPC/Protobuf + lock-free trie + React | Lead with the TypeScript/React observer pattern bullet (68% delivery acceleration) | Full-stack JD weights front-end more; Chrome React work is the strongest signal |
| 4 | Skills section | Distributed Systems lead | Add or promote "React, TypeScript" and "REST/GraphQL APIs" higher; Temporal if possible | JD specifically calls out React, TypeScript, REST/GraphQL |
| 5 | Cover letter | None in standard flow | Write 1-page cover: Skydio mission relevance (production systems for real-world safety) + specific proof points (Chrome React + TiMoto APIs + AWS infra) | Skydio operates in high-stakes contexts; mission alignment is a differentiator |

**LinkedIn:** Add "Skydio" as followed company; update headline to include "Full-Stack" + "Cloud Platform" keywords; ensure React/TypeScript pinned prominently in skills endorsements.

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | React/TypeScript at scale | React Observer Pattern at Chrome | Chrome settings UI state coupling causing cascading failures | Decouple state propagation across 25K+ lines Chromium React/TS | Designed observer-pattern event system; components subscribe to state events | 68% feature delivery acceleration, 95% test coverage, shipped to production | Decouple state model early; retrofitting at Chromium scale is expensive |
| 2 | Backend services / APIs | gRPC Deadlock Fix at TiMoto | Concurrent gRPC calls causing deadlocks in production evaluation service | Debug and eliminate deadlock | Traced shared resource acquisition; redesigned call sequencing | 100% evaluation success, sub-50ms p99 | Always instrument concurrent call paths before launch |
| 3 | Performance / reliability | Lock-Free Trie at Google Chrome | Chrome settings search at 1,200ms p99 | Reduce latency without correctness regression | Lock-free concurrent trie, linearizability verification | 96% latency reduction, zero regressions | Prove correctness by construction, not just benchmarks |
| 4 | Cloud / infrastructure | Multi-AZ Circuit Breaker at TiMoto | Single-AZ with no failover | Design multi-AZ failover with auto-rollback | ECS Fargate, Terraform, CloudWatch, circuit breaker, health checks | 99.9% uptime, 44% cost reduction | AZ isolation is Day 1, not retrofit work |
| 5 | Cross-team collaboration | Chromium Code Review Culture | Joining Chrome infra team as intern with zero Chromium context | Ramp quickly, ship within internship window | Read design docs first; followed Chrome's code review rigor; changes reviewed by senior engineers | Shipped to stable channel (3B+ users); changes adopted into production branch | Reading code is 70% of the job on large codebases |
| 6 | High-stakes environments | vLLM Production Serving | TiMoto needed concurrent LLM inference without OOM under user load | Build production inference layer with reliability SLOs | Compared naive vs vLLM/PagedAttention; deployed with continuous batching + gRPC | Zero OOM failures, sub-50ms p99 | Document architecture decisions; future team members need the "why" |
| 7 | Data pipelines / backend | N+1 Fix at Develop for Good | 3s+ response degradation on large datasets | Diagnose and fix | N+1 diagnosis via profiling; PostgreSQL indexing redesign | Sub-100ms on 10K+ records | Profile before optimizing; assumptions about query shape are wrong |
| 8 | Product intuition for high-stakes | TiMoto end-to-end ownership | 3-person team, full backend+infra+ML stack, production SLOs | Own entire stack, build with reliability guarantees from Day 1 | Designed systems with SLOs in mind: circuit breakers, uptime targets, cost caps | $40-60/month infra, 99.9% uptime, zero unplanned outages | High-stakes production requires reliability by design, not by luck |

**Recommended case study:** TiMoto AI platform (timoto.ai) -- end-to-end production stack with quantified SLOs. Frame as: "I own a backend + cloud infra + ML serving stack for a production product. Here's how it's architected and what tradeoffs I made." This maps directly to Skydio's need for someone who can own cross-stack work.

**Red-flag questions:**

- *"Do you have 1-3 years of experience?"* -- Answer: "I've been shipping production software since May 2025 -- Google Chrome internship (3B+ users, C++ IPC + React) and primary engineer at TiMoto AI from September 2025 to present. The total calendar time is ~1.5 years, but the production depth is beyond what most 1-year engineers have seen."
- *"Do you need visa sponsorship?"* -- Answer: "I'm on F-1 status and eligible for OPT starting May 2027. I'll need H-1B sponsorship for long-term employment. Based on your LCA filings, Skydio has a strong sponsorship track record -- 21 approvals in FY2025."
- *"Why drones / Skydio?"* -- Answer: "I build systems where failures cost more than a slow page load -- at TiMoto, an inference failure means a user's workflow breaks; at Skydio, a cloud platform failure affects first responders in the field. That high-stakes context is where I do my best work."

**Stories added to bank:** Stories 1-4 already in bank. Stories 5, 8 are new framings.

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active -- full application form visible (Ashby ATS) | Positive |
| JD specificity | Named technologies (React, TypeScript, REST/GraphQL, AWS, K8s, Temporal), team context, realistic 1-3 year exp req | Positive |
| Company hiring phase | $3.5B expansion (April 2026), 5,000+ jobs planned, 85 open roles on ZipRecruiter | Positive |
| Layoff signals | None recent; company in active growth phase | Positive |
| Reposting pattern | Not found in scan-history.tsv -- first seen | Positive |
| Salary posted | Yes ($110K-$180K) | Positive |
| Posting age | Not visible explicitly; page fully rendered with application form active | Neutral |
| Requirements realism | 1-3 years for junior role at hardware/software startup -- realistic | Positive |

**Context:** Skydio committed $3.5B to US manufacturing expansion in April 2026 with 2,000+ direct new hires. Engineering headcount (992 employees) is actively growing. This posting is consistent with active expansion. No concerns.

---

## H) Draft Application Answers

*(Score 3.5/5 -- below 4.0 threshold for Block H; recommend applying with manual review of form)*

---

## Keywords Extracted

React, TypeScript, REST API, GraphQL, distributed architecture, backend services, data pipelines, cloud-based systems, performance optimization, reliability, maintainability, full-stack development, AWS, Kubernetes, Temporal, autonomy, robotics, cross-functional collaboration, UI/UX, cloud platform, high-stakes environments

---

## Machine Summary

```yaml
report: "067"
company: "Skydio"
role: "Software Engineer, Full Stack"
date: "2026-06-06"
score: 3.5
archetype: "Full-Stack Engineer"
legitimacy: "High Confidence"
location: "San Mateo, CA"
remote: "hybrid"
comp_range: "$110K-$180K base"
visa_risk: "low"
sponsorship_confirmed: true
sponsorship_notes: "Skydio filed 21 H-1B petitions FY2025, all approved; strong track record"
apply_recommendation: "Conditional apply — full-stack role is adjacent to Harry's primary backend/systems profile; strong React/TS Chrome evidence; comp may undershoot walk-away floor without equity; negotiate top of range"
red_flags:
  - "Comp base floor $110K well below walk-away $140K; must land at $130K+ base"
  - "Hybrid 3 days/week San Mateo requires relocation from Atlanta"
  - "Pre-IPO stock options — liquidity risk"
  - "Full-stack framing is adjacent, not primary archetype fit"
green_flags:
  - "Skydio confirmed H-1B sponsor (21/21 approvals FY2025)"
  - "Active $3.5B hiring expansion — real, active opening"
  - "1-3 year exp requirement matches Harry's ~1.5 years production experience"
  - "Google Chrome TypeScript/React work is direct full-stack evidence"
  - "AWS + K8s bonus qualifications covered in CV"
```
