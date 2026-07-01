# Evaluation: Google — Software Engineer III, Site Reliability Engineering (Pittsburgh)

**Date:** 2026-06-12
**URL:** https://www.google.com/about/careers/applications/jobs/results/115062974825013958-software-engineer-iii-site-reliability-engineering
**Archetype:** SRE / Platform & Cloud Infrastructure
**Score:** 4.4/5
**Legitimacy:** Tier 1 — Confirmed Active (Apply button present, full JD visible)
**PDF:** output/140-google-sre-iii-pittsburgh-harry-nguyen-2026-06-12.pdf

---

## A — Role Summary

**Company:** Google  
**Team:** Site Reliability Engineering  
**Role:** Software Engineer III, Site Reliability Engineering  
**Location:** Pittsburgh, PA, USA  
**Level:** Mid/L4 (2 YOE minimum)  
**Comp:** $147K–$211K base + 15% bonus + equity → TC ~$200K–$280K  

Google SRE: treat operations as a software problem. Keep Google's public services (Search, Ads, Gmail, YouTube) running at planetary scale. Span from disk driver I/O to continental-level service capacity. Mission: progress, protect, and provide for software and systems — with full code access and authority.

---

## B — CV Match (Gap Analysis)

| Requirement | Harry's Evidence | Strength |
|------------|-----------------|----------|
| Bachelor's degree in CS | Georgia State University, BS CS (Expected May 2027) | ✅ |
| 2 YOE software development in any language | TiMoto (Sep 2025–Present) + Google Chrome intern (May–Aug 2025) + Develop for Good intern | ✅ Meets threshold |
| Large-scale distributed systems design & troubleshooting (preferred) | TiMoto: multi-AZ ECS Fargate, gRPC, circuit breaker, 99.9% uptime, on-call; Chrome: 3B+ users | ✅ Strong |
| Triage product/system issues and debug | TiMoto: root-cause analysis, runbooks, post-mortems, on-call rotation | ✅ Direct SRE evidence |
| Write product/system development code | TiMoto: full backend + infra stack; Chrome: C++ IPC, TypeScript/React | ✅ |
| Code review + best practices | Chrome: 95% test coverage, design docs reviewed by senior Chrome engineers | ✅ |
| Design review participation | Chrome: collaborated with Chrome infra team, design documents | ✅ |

**Key Strengths:**
- TiMoto SRE story is directly aligned: 99.9% uptime SLO, circuit breaker + auto-rollback, CloudWatch + Prometheus/Grafana observability, on-call rotation, root-cause analysis, runbooks, post-mortem
- Former Google intern: same SRE culture, production engineering norms, zero production regression record at 3B+ scale
- 44% cost reduction = SRE capacity optimization ethos

**Key Gaps:**
- ~15 months vs 2-year threshold: mitigated by production ownership + Google Chrome internship
- No advanced degree (preferred Master's) — not a hard blocker

---

## C — Level & Strategy

**Target level:** L3/L4  
**Gap:** Minimal. 2-year threshold is nearly met if Chrome internship + TiMoto totaled together (~18 months). SRE is also more welcoming to candidates with strong ops backgrounds than pure SWE roles.

**Strategy:** Lead with TiMoto SRE narrative: 99.9% uptime, circuit breaker, multi-AZ, on-call, post-mortem, runbooks. This is textbook Google SRE. Position Chrome internship as proof of Google engineering bar.

**Pittsburgh advantage:** Less competitive market than NYC/SF/Seattle — better odds for a near-new-grad candidate.

---

## D — Compensation

- **Posted range:** $147K–$211K base + 15% bonus + equity  
- **TC estimate:** ~$200K–$280K (L3/L4)  
- **Harry's target:** $150K–$200K TC  
- **Verdict:** Meets and exceeds target. Pittsburgh COL is significantly lower than SF/NYC — same TC goes further.

---

## E — CV Customization Plan

**Focus archetype:** SRE  
**Lead story:** TiMoto 99.9% uptime + circuit breaker + on-call rotation (Google SRE ethos)

**Bullets to emphasize:**
1. TiMoto infra: multi-AZ ECS Fargate, CloudWatch + Prometheus/Grafana, circuit breaker + auto-rollback, on-call, root-cause analysis, runbooks, post-mortem → 99.9% SLO
2. TiMoto gRPC: production deadlock debugging, 100% evaluation success, sub-50ms p99
3. Chrome: zero production regressions at 3B+ users, 95% test coverage (SRE: don't break things)
4. Develop for Good: 90% deployment time reduction via CI/CD (SRE: toil elimination)

**Skills order (Cloud & Infrastructure first for SRE):**
Cloud & Infrastructure (AWS ECS Fargate, K8s, Terraform, Docker, CI/CD, CloudWatch, Prometheus, Grafana bolded) → Distributed Systems (Circuit breakers, Multi-AZ, Fault tolerance bolded) → Languages → ML & AI → Frameworks → AI Dev Tools last

---

## F — Interview Plan (STAR+R Stories)

**Domain:** SRE — availability, latency, reliability, capacity, incident response

**Story 1 — 99.9% SLO + Incident Response**  
S: TiMoto ML serving layer needed production-grade reliability  
T: Design fault-tolerant architecture and incident response process  
A: Multi-AZ ECS Fargate, circuit breaker + auto-rollback, CloudWatch alerting, Prometheus/Grafana dashboards; established on-call rotation and runbook documentation  
R: 99.9% uptime SLO, 44% cost reduction, zero unplanned downtime incidents  
R: Post-mortem learnings applied to circuit breaker patterns

**Story 2 — Production Debugging**  
S: gRPC service producing silent failures under concurrent load  
T: Diagnose and resolve without service disruption  
A: Added distributed tracing, identified shared resource deadlock, redesigned call sequencing  
R: 100% evaluation success rate, sub-50ms p99  
R: Documented root-cause analysis; added load test to CI to prevent regression

**Story 3 — Toil Elimination**  
S: Develop for Good deployments taking 90%+ more time than necessary  
T: Reduce deployment toil via automation  
A: Implemented CI/CD via GitHub Actions, automated testing pipeline  
R: 90% deployment time reduction  
R: Pattern adopted across the organization's other projects

**Prep areas:** SLOs/SLIs/error budgets, Spanner/Bigtable architecture basics, Google's SRE Book concepts (eliminating toil, postmortems, capacity planning), on-call practices, observability (Dapper-style tracing).

---

## G — Posting Legitimacy

- **Verification:** Confirmed active via Playwright  
- **Apply button:** Present and functional  
- **Full JD:** Visible with Minimum/Preferred qualifications, About the job, Responsibilities  
- **Salary disclosed:** Yes — $147K–$211K USD  
- **Location:** Pittsburgh, PA, USA  
- **Tier:** Tier 1 — Fully legitimate Google Careers posting  

---

## Machine Summary

```yaml
report: 140
date: "2026-06-12"
company: Google
role: "Software Engineer III, Site Reliability Engineering"
location: "Pittsburgh, PA, USA"
archetype: "SRE / Platform & Cloud Infrastructure"
score: 4.4
legitimacy: "Tier 1"
level: "L3/L4"
comp_base_low: 147000
comp_base_high: 211000
tc_low: 200000
tc_high: 280000
pdf: "output/140-google-sre-iii-pittsburgh-harry-nguyen-2026-06-12.pdf"
status: Evaluated
key_gaps:
  - "~15 months vs 2-year threshold (mitigated by Google internship + TiMoto production ownership)"
  - "No advanced degree (preferred)"
recommendation: "Apply — best SRE fit in batch; TiMoto SRE story maps directly to Google SRE ethos; Pittsburgh is less competitive market"
```
