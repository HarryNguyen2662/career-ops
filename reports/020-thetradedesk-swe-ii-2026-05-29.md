# 020 — The Trade Desk — Software Engineer II

**Date:** 2026-05-29
**Score:** 3.8/5
**URL:** https://job-boards.greenhouse.io/thetradedesk/jobs/5102422007
**PDF:** ✅
**Legitimacy:** High Confidence

---

## Machine Summary

```yaml
company: The Trade Desk
role: Software Engineer II
date: 2026-05-29
score: 3.8
status: Evaluated
level: SWE II — entry-to-mid (2+ years typical); no explicit experience floor in JD
location: San Francisco, CA — remote within commuting distance (hybrid; relocation needed from Atlanta)
comp_base: "$151,400–$227,000 USD"
comp_equity: "Stock-based compensation + ESPP with discount option"
archetype: "Backend / Distributed Data Engineering"
graduation_timing_risk: medium — form asks 'Do you have a BS in CS?' (Harry expected May 2027); flag in form
visa_risk: low — The Trade Desk is a large public company (NASDAQ: TTD); one of the largest H-1B sponsors in adtech
apply_rec: "Conditional Apply — below 4.0 threshold; proceed only because: (1) TTD H-1B is near-certain, (2) Python accepted (no Scala needed), (3) $151K+ floor is above walk-away, (4) best US-eligible SWE II on their board. Flag degree completion status honestly in form. Apache Spark gap is real — do not overclaim."
```

---

## Selection Rationale

The Trade Desk has 193 open roles. After filtering for US-eligible, non-Senior SWE positions, 5 "Software Engineer II" roles appear. Of those, only **SF** and **Bellevue/Seattle** (Full Stack) are US-based. This SF SWE II was selected as the best archetype match for Harry's backend/distributed systems profile vs. the Full Stack alternative.

**Why not the Full Stack SWE II (Bellevue)?** Overlapping skills, but "Full Stack" skews frontend-heavier. The SF SWE II focuses on backend services, data processing, and infrastructure — closer to Harry's primary archetype.

---

## Block A — Match with CV

**Score: 3.6/5**

| JD Requirement | Harry's Evidence |
|---|---|
| **Python** (Java/Scala/Python) | TiMoto: Python/Django REST backend, FastAPI; Develop for Good: AWS BaaS in Python ✅ |
| **Kubernetes / Docker** | TiMoto: ECS Fargate orchestration (K8s-equivalent), Docker containers; listed in skills ✅ |
| **ECS** | TiMoto: multi-AZ ECS Fargate with Terraform IaC — exact match ✅ |
| **REST APIs** | TiMoto: Django REST backend; Develop for Good: BaaS REST APIs ✅ |
| **RPC / gRPC** | TiMoto: gRPC inter-service layer; production deadlock fix at sub-50ms p99 ✅ |
| **CI/CD workflows** | Develop for Good: CI/CD with GitHub Actions; 90% deployment time reduction ✅ |
| **Observability / metrics / profiling** | Google Chrome: profiled p99 bottleneck at 1,200ms; TiMoto: circuit breaker + health-check monitoring ✅ |
| **Debugging with logs / profiling tools** | Chrome: traced settings nav bottleneck to mutex contention; TiMoto: traced gRPC deadlock to circular resource acquisition ✅ |
| **Apache Spark / distributed data processing** | Not present — no Spark experience. DynamoDB redesign at 9K+ req/sec is adjacent but not Spark ❌ |
| **Java** | Listed in Harry's skills; not the primary language; minimal production evidence ⚠️ |
| **Asynchronous messaging patterns** | TiMoto: gRPC + circuit breakers; Redis at CoderPush — adjacent but no Kafka/SQS messaging experience explicitly ⚠️ |
| **Bachelor's degree in CS** | In progress — Expected May 2027; form asks if Harry "has" the degree → must answer accurately ⚠️ |

**Key strength:** Harry's ECS Fargate + gRPC + Python REST + Docker + CI/CD stack is a near-exact match for everything except Spark. The Trade Desk processes programmatic ad auctions at petabyte scale — Harry's distributed systems work (DynamoDB at 9K+ req/sec, Chrome at 3B+ users) establishes he can operate at scale.

**Key gap:** Apache Spark is the clearest miss. The JD says "build data processing workflows with Apache Spark." Harry has no Spark experience — do not claim any.

---

## Block B — North Star Alignment

**Score: 3.8/5**

The Trade Desk's engineering org processes trillions of ad auction impressions per day — one of the highest-throughput real-time systems in existence. The SF SWE II role focuses on backend services, distributed data pipelines, and infrastructure that powers this bidding engine.

**Where it aligns:**
- **Distributed systems at extreme scale** — TTD's bidding system is among the highest-throughput distributed systems in the world. Harry's profile (Chrome 3B+ users, TiMoto sub-50ms p99, DynamoDB 9K+ req/sec) shows genuine distributed systems thinking.
- **Cloud-native infrastructure (ECS Fargate)** — Harry runs TiMoto on ECS Fargate. TTD uses ECS. This is a direct operational skill, not abstract cloud knowledge.
- **gRPC / RPC inter-service communication** — core to TTD's microservice bidding stack.
- **Python + backend services** — Python is Harry's strongest production language; TTD explicitly accepts it.
- **Large public company = sponsorship certainty** — NASDAQ:TTD; thousands of H-1B filings historically.

**Where it misses:**
- **Adtech domain** — programmatic advertising (DSP, RTB, bid pricing) is specialized; Harry has no adtech background. The learning curve is real.
- **Spark / data engineering** — TTD's data layer relies heavily on Spark for batch and streaming processing. This is a gap Harry will need to close on the job.
- **Degree completion** — TTD's form explicitly asks for a completed CS degree. Harry's is in progress (May 2027). This could be a hard screen.
- **North Star archetype** — adtech backend is adjacent to Harry's target (ML infra, platform engineering) but not on the direct path. TTD does have ML/AI bidding optimization work internally, but this specific role is data infrastructure.

---

## Block C — Compensation

**Score: 4.5/5**

| Component | Value | vs Target |
|---|---|---|
| Base | $151,400–$227,000 | **Floor $151K is $11K above walk-away minimum ($140K)** ✅ |
| Stock | Stock-based compensation + ESPP discount | Liquid NASDAQ stock (TTD) — immediate liquidity |
| 401k | Company match | Standard |
| Vacation | 120 hrs Year-1, 160 hrs thereafter | Generous |
| Healthcare | Full premium coverage | Strong |

**Year-1 TC estimate:**
- Base ~$175K mid-band + stock grant for SWE II (~$40K–$80K/4yr = ~$10K–$20K/yr)
- ESPP discount provides additional upside on TTD stock purchases
- Year-1 TC: ~$185K–$200K

TTD stock (NASDAQ: TTD) is publicly traded and liquid — no startup illiquidity risk.

---

## Block D — Cultural Signals

**Score: 4.0/5**

**Positive signals:**
- Large public company ($10B+ market cap) — stable, profitable adtech leader
- H-1B sponsorship is near-certain at TTD scale
- "Remote within commuting distance" → flexible hybrid, not 5-day mandatory onsite
- SF office: strong engineering culture, access to adtech ecosystem
- ESPP = Harry benefits directly from TTD stock growth
- SWE II is a leveled title — internal mobility to Senior/Staff is a documented path

**Friction signals:**
- Adtech culture can be sales-driven (DSP serves agencies and brands) — engineering may feel downstream of business cycles
- Spark/data engineering orientation may not build the ML-infra depth Harry targets
- SF relocation from Atlanta still required (even with hybrid flexibility)
- Degree-in-progress may create friction at screening stage

---

## Block E — Red Flags

| Flag | Severity | Action |
|---|---|---|
| **Score 3.8/5 — below 4.0 apply threshold** | HIGH | Flagging explicitly. Proceeding because: (1) near-certain H-1B, (2) Python accepted, (3) comp above walk-away, (4) best US-eligible SWE II on TTD board. Harry should decide consciously. |
| **Apache Spark gap** | HIGH | Do not claim Spark experience in resume or form. In interviews: "No Spark production experience; familiar with distributed data patterns (DynamoDB at 9K+ req/sec, Raft/Paxos study). Ready to ramp on Spark." |
| **Degree-in-progress** | HIGH | Form asks: "Do you have a Bachelor's degree in CS?" Harry does not yet. Options in the dropdown may include "in progress" or "expected." Answer accurately. If only Yes/No, answer No and note expected graduation May 2027. Do NOT answer Yes. |
| **SF relocation** | MEDIUM | Open to relocation per profile. "Remote within commuting distance" means hybrid — may ease relocation timing. Confirm exact office cadence in recruiter call. |
| **SWE II experience expectation** | MEDIUM | TTD doesn't state an explicit year floor in the JD, but SWE II typically implies 2-3 years. Harry's Google + 2 internships + TiMoto are near this. Google Chrome FAANG quality compensates significantly. |

---

## Block F — Global Score

**3.8/5 — Conditional Apply**

| Dimension | Score | Driver |
|---|---|---|
| CV Match | 3.6 | Python + ECS + gRPC + CI/CD strong; Spark absent; degree in progress |
| North Star | 3.8 | Distributed systems at TTD scale is compelling; adtech domain not primary archetype |
| Compensation | 4.5 | $151K+ floor; liquid NASDAQ stock; ESPP; full benefits |
| Culture | 4.0 | Large public company; H-1B near-certain; hybrid flexibility; stable |
| Red flag adj. | -0.5 | Score threshold (-0.1), Spark gap (-0.2), degree question (-0.2) |
| **Global** | **3.8** | |

**Recommendation: Conditional Apply** — below the 4.0 strong-apply threshold. Proceed with awareness that:
1. The degree question may screen Harry out at the form stage
2. Spark will come up in interviews — be honest about the gap
3. This is not Harry's North Star archetype — adtech data infra is a detour unless TTD's ML bidding team is the destination

---

## Block G — Posting Legitimacy

**Tier: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Posting live | Active Greenhouse form with full JD and explicit salary | Positive |
| Salary transparency | $151,400–$227,000 — explicit with bonus/equity details | Positive |
| Company verification | The Trade Desk (NASDAQ: TTD) — large public adtech company | Positive |
| Company health | Publicly traded, profitable, market leader in DSP | Positive |
| JD specificity | Named tech stack (Spark, ECS, GitLab CI, Kubernetes); specific work described | Positive |
| ATS | Greenhouse `thetradedesk` board — verified | Positive |

Real posting at a publicly traded company. No ghost signals.
