# Evaluation: Google — Software Engineer, Distributed Rate Limiting Services

**Date:** 2026-06-12
**URL:** https://www.google.com/about/careers/applications/jobs/results/128963260668879558-software-engineer-distributed-rate-limiting-services
**Archetype:** Backend / Distributed Systems
**Score:** 4.2/5
**Legitimacy:** Tier 1 — Confirmed Active (Apply button present, full JD visible)
**PDF:** output/138-google-distributed-rate-limiting-harry-nguyen-2026-06-12.pdf

---

## A — Role Summary

**Company:** Google Cloud  
**Team:** QuotaServer / Bouncer — massively distributed platforms powering quota enforcement across Google and Google Cloud  
**Role:** Software Engineer, Distributed Rate Limiting Services  
**Location:** Sunnyvale, CA, USA  
**Level:** Mid (2 YOE requirement)  
**Comp:** $147K–$211K base + 15% bonus + equity → TC ~$200K–$280K  

Google Cloud's foundational rate-limiting infrastructure. QuotaServer and Bouncer enforce quota across virtually all Google-critical services. Mission: develop and maintain planet-scale distributed infrastructure for reliable, accurate rate limiting and quota enforcement for internal Google and Google Cloud clients.

---

## B — CV Match (Gap Analysis)

| Requirement | Harry's Evidence | Strength |
|------------|-----------------|----------|
| Bachelor's degree in CS | Georgia State University, BS CS (Expected May 2027) | ✅ |
| 2 YOE software dev or 1 YOE with advanced degree | ~15 months TiMoto + Google Chrome internship; no advanced degree | ⚠️ Mitigated: production ownership at TiMoto + Chrome internship |
| 2 YOE large-scale infra / distributed systems / networks | TiMoto: multi-AZ ECS Fargate, gRPC service layer, 99.9% uptime; Chrome: IPC transport to 3B+ users | ✅ Strong narrative |
| Data structures / algorithms experience | Lock-free trie (96% latency reduction), Raft/Paxos analysis in Pulumi contribution | ✅ |
| Building distributed processing pipelines at scale | TiMoto: vLLM inference pipeline, continuous batching, gRPC exactly-once | ✅ |
| Architecting distributed systems in HPC/cloud | TiMoto: multi-AZ ECS Fargate + Terraform, AWS infra end-to-end | ✅ |
| Debug planet-scale distributed systems | TiMoto: traced production deadlock under concurrent calls, root-cause analysis, runbooks | ✅ |

**Key Gaps:**
- 2-year threshold: Harry has ~15 months — mitigate with production ownership at TiMoto + Google Chrome internship at scale
- No advanced degree (preferred Master's/PhD) — not a hard blocker

**Strength:** gRPC exactly-once semantics + production deadlock resolution + Chrome IPC transport to 3B+ users maps directly to "debug planet-scale distributed systems." QuotaServer/Bouncer domain aligns tightly with Harry's distributed systems archetype.

---

## C — Level & Strategy

**Target level:** L3/L4 (Mid)  
**Gap:** ~5 months short on raw YOE. Strategy: Frame TiMoto as lead engineer owning distributed infra end-to-end; Chrome internship demonstrates Googler-level bar at 3B+ scale. Emphasize production deadlock resolution and exactly-once gRPC as directly analogous to rate-limiting system correctness.

**Differentiation:** Former Google intern (Chrome) — understands Google infra culture, code review bar, and production engineering norms.

---

## D — Compensation

- **Posted range:** $147K–$211K base + 15% bonus + equity  
- **TC estimate:** ~$200K–$280K (L3/L4)  
- **Harry's target:** $150K–$200K TC  
- **Verdict:** Meets and exceeds target. Equity upside is significant. Top-tier outcome.

---

## E — CV Customization Plan

**Focus archetype:** Distributed Systems  
**Lead story:** gRPC exactly-once semantics + production deadlock debugging (maps to "debug planet-scale distributed systems")

**Bullets to emphasize:**
1. gRPC inter-service layer: deadlock resolution → 100% evaluation success rate, sub-50ms p99
2. Multi-AZ ECS Fargate: Terraform IaC, circuit breaker, 99.9% uptime (infrastructure reliability = rate-limiting reliability)
3. Chrome IPC transport: Protocol Buffers, sub-50ms p99, 3B+ users (planet-scale distribution)
4. Pulumi: Raft/Paxos analysis (consensus theory for correctness guarantees)

**Skills order (Distributed Systems first):** Distributed Systems (gRPC, Protocol Buffers, Exactly-once bolded) → Languages (C++, Go, Python bolded) → Cloud & Infrastructure → ML & AI → Frameworks → AI Dev Tools last

---

## F — Interview Plan (STAR+R Stories)

**Domain:** Distributed rate limiting / quota enforcement

**Story 1 — Production Debugging at Scale**  
S: TiMoto gRPC service experiencing silent failures under concurrent load  
T: Trace root cause of evaluation failures, restore 100% success rate  
A: Used distributed tracing to identify shared resource deadlock; redesigned call sequencing to eliminate lock contention  
R: 100% evaluation success rate, sub-50ms p99  
R: Applied pattern to future service design (lock ordering documentation)

**Story 2 — Infrastructure Reliability**  
S: Need production-grade uptime for TiMoto ML serving layer  
T: Design fault-tolerant multi-AZ architecture  
A: Implemented circuit breaker pattern, auto-rollback on health check failure, CloudWatch alerting  
R: 99.9% SLO achieved, 44% cost reduction  
R: On-call rotation + runbooks prevent recurrence

**Story 3 — Planet-Scale Distribution**  
S: Chrome IPC transport for 3B+ user Chrome browser  
T: Deliver sub-50ms p99 cross-process communication  
A: Designed Protocol Buffers transport layer, selected serialization for schema evolution  
R: Shipped to Chrome stable channel at 10K+ req/sec, zero production regressions  
R: Adopted into production branch by senior Chrome engineers

**Prep areas:** Rate limiting algorithms (token bucket, leaky bucket, sliding window), distributed consensus, quota enforcement patterns, CAP theorem trade-offs for quota systems.

---

## G — Posting Legitimacy

- **Verification:** Confirmed active via Playwright  
- **Apply button:** Present and functional  
- **Full JD:** Visible with Minimum/Preferred qualifications, About the job, Responsibilities  
- **Salary disclosed:** Yes — $147K–$211K USD  
- **Tier:** Tier 1 — Fully legitimate Google Careers posting  

---

## Machine Summary

```yaml
report: 138
date: "2026-06-12"
company: Google
role: "Software Engineer, Distributed Rate Limiting Services"
location: "Sunnyvale, CA, USA"
archetype: "Backend / Distributed Systems"
score: 4.2
legitimacy: "Tier 1"
level: "L3/L4"
comp_base_low: 147000
comp_base_high: 211000
tc_low: 200000
tc_high: 280000
pdf: "output/138-google-distributed-rate-limiting-harry-nguyen-2026-06-12.pdf"
status: Evaluated
key_gaps:
  - "15 months YOE vs 2-year requirement (mitigated by production ownership + Chrome internship)"
  - "No advanced degree (preferred)"
recommendation: Apply — strong distributed systems match, former Google intern advantage
```
