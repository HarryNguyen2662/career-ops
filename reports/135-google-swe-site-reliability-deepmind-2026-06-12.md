# Evaluation: Google — Software Engineer, Site Reliability (DeepMind)

**Date:** 2026-06-12
**URL:** https://www.google.com/about/careers/applications/jobs/results/90934529409065670-software-engineer-site-reliability
**Archetype:** SRE · Platform/Cloud Infrastructure
**Score:** 4.1/5
**Legitimacy:** High Confidence
**PDF:** output/135-google-swe-site-reliability-deepmind-harry-nguyen-2026-06-12.pdf

---

## A — Role Summary

| Field | Detail |
|-------|--------|
| Title | Software Engineer, Site Reliability |
| Team | Google DeepMind |
| Seniority | Mid (L4 equivalent, "Mid" badge) |
| Location | Mountain View, CA, USA (hybrid allowed per Google policy) |
| Comp | $149,400–$211,000 base + 15% bonus + equity → TC ~$200K–$280K |
| Domain | SRE for AI research infrastructure; reliability, scalability, distributed systems |

**What the team does:** SRE for Google DeepMind — supporting the reliability and scalability of AI research infrastructure. Directly at the intersection of Harry's SRE archetype and ML infrastructure background. DeepMind SRE = production ownership of AI training/serving systems.

---

## B — CV Match

| Requirement | Harry's Evidence | Strength |
|-------------|-----------------|----------|
| BS CS or related + 2 yrs experience | Georgia State BS CS (May 2027) + ~15 months total production experience | ⚠️ ~9 months short |
| Designing/writing/testing/maintaining software | Chrome IPC (C++, 95% test coverage), TiMoto gRPC, DfG BaaS | ✅ Strong |
| Algorithms and data structures for scale/speed/reliability | Lock-free trie (96% latency reduction), PostgreSQL indexing, gRPC redesign | ✅ Strong |
| Troubleshooting/RCA on large-scale distributed systems | TiMoto: production deadlock RCA + redesign; Chrome infrastructure collaboration; on-call rotation documented | ✅ Strong |
| Anticipating/managing risks to systems | TiMoto: circuit breaker pattern, auto-rollback, health check failure recovery; 99.9% uptime | ✅ Strong |
| Simplifying/automating processes | TiMoto: Terraform IaC, CI/CD, 44% cost reduction; DfG: 90% deploy time reduction via CI/CD | ✅ Strong |

**Gap analysis:**
- **Experience gap (~9 months):** The 2-year threshold is standard Google SWE minimum. Mitigated by: Google Chrome internship (proven at Google scale), TiMoto production ownership (99.9% uptime, on-call rotation).
- **No explicit language requirement** in this posting — strong advantage for Harry whose profile spans C++ and Python.
- **DeepMind context** means this SRE role will touch ML training infrastructure — Harry's vLLM/ML serving background is directly additive.
- **Strongest SRE candidate profile** of all 5 roles in this batch.

---

## C — Level & Interview Strategy

**Target level:** L3 (new grad) or L4 (stretch with production credentials)

**Interview format (Google SRE):**
1. Coding (LC medium, focus on systems/algorithms)
2. Systems Design: distributed system, reliability engineering, capacity planning
3. SRE-specific: on-call, incident response, SLO/SLI/SLA, toil reduction
4. Behavioral (Googleyness, ownership, reliability mindset)

**Strategy:**
- Lead with TiMoto SRE credentials: 99.9% uptime, on-call rotation, RCA documentation, runbooks, post-mortem learnings
- Chrome: quantify production impact (3B users, sub-50ms p99 at 10K+ req/sec)
- TiMoto circuit breaker + auto-rollback = textbook SRE patterns
- DeepMind context: frame ML infrastructure ownership (vLLM) as additive signal — "I can support both the reliability layer and understand the ML workloads I'm supporting"
- Systems Design prep: load balancer design, global traffic management, distributed rate limiting, on-call rotation design
- Disclose: "F-1 OPT at graduation May 2027; H-1B long-term. Google sponsors H-1B."

---

## D — Comp & Market

| Component | Range |
|-----------|-------|
| Base (L3) | $149,400–$175K |
| Base (L4) | $175K–$211K |
| Bonus | 15% target |
| Equity | Alphabet RSUs (4-yr vest) |
| TC estimate | $200K–$280K |

Meets Harry's $150K–$200K TC target at L3. DeepMind brand + SRE track = excellent long-term career trajectory.

---

## E — CV Customization Plan

**Skills row ordering (SRE role):**
1. Cloud & Infrastructure (first — AWS, Terraform, Kubernetes, CloudWatch, Prometheus, Grafana)
2. Distributed Systems (gRPC, fault tolerance, circuit breakers, multi-AZ)
3. Languages (C++ and Python co-equal)
4. ML & AI Infrastructure (additive context for DeepMind)
5. Frameworks & Databases
6. AI Dev Tools (last)

**Bullet emphasis:**
- TiMoto: Lead with reliability bullets: 99.9% uptime, circuit breaker, auto-rollback, on-call rotation, RCA/runbooks
- TiMoto: Terraform IaC + CloudWatch observability = textbook SRE tooling
- TiMoto: 44% cost reduction = SRE toil/efficiency metric
- Chrome: IPC transport reliability at 3B users + 95% test coverage
- DfG: 90% deploy time reduction = SRE automation value

**Skills to surface explicitly:**
- Prometheus, Grafana (listed in skills but make prominent)
- On-call rotation (explicitly mention in TiMoto bullet)
- Post-mortem/runbook culture

---

## F — Interview Preparation

### STAR+R Stories

**"Production incident + RCA"**
> Situation: TiMoto production gRPC deadlock under concurrent calls. Task: identify root cause and fix without downtime. Action: traced shared resource acquisition conflicts under concurrency; redesigned call sequencing to eliminate deadlock; documented RCA in runbook. Result: 100% evaluation success rate maintained, zero recurrence. Reflection: this is exactly what SRE on-call looks like at scale — systematic debugging, fast mitigation, permanent fix.

**"Reliability architecture at scale"**
> Situation: TiMoto needed production-grade infrastructure for ML serving. Task: architect for 99.9% uptime with minimal budget. Action: multi-AZ ECS Fargate with Terraform IaC, CloudWatch alarms, circuit breaker pattern, health check auto-rollback. Result: 99.9% uptime, $40-60/month (44% cost reduction). Reflection: the SRE mindset — design for failure, automate recovery, eliminate toil.

**"Chrome reliability at 3B-user scale"**
> Situation: Chrome settings navigation at 1,200ms p99 degrading user experience at 3B-user scale. Task: eliminate latency bottleneck. Action: profiled bottleneck as mutex contention in settings trie; implemented lock-free CAS search. Result: 96% latency reduction, zero production regressions. Reflection: reliability engineering at Google scale demands both strong algorithms and rigorous production testing.

### SRE interview prep topics:
- SLO/SLI/SLA definitions and tradeoffs
- Error budget concept and burn rate alerts
- Distributed tracing: OpenTelemetry, Jaeger
- Capacity planning and load testing
- Toil definition and automation strategies
- Incident management: severity levels, escalation, post-mortem culture
- Google SRE book chapters: Chapter 1 (Introduction), Chapter 6 (Monitoring), Chapter 13 (Emergency Response)

---

## G — Posting Legitimacy

**Verdict: High Confidence**

- Apply button present and functional (verified via Playwright)
- Full JD with responsibilities, qualifications, and compensation
- Official Google Careers domain; explicitly says "Google DeepMind"
- Comp explicitly stated: "$149,400 - $211,000 + 15% bonus target + equity"
- Location confirmed: Mountain View, CA (hybrid allowed)

---

## Summary & Recommendation

**Score: 4.1/5 — Good match, apply**

**Strengths:** Strongest SRE fit in this batch. Harry's TiMoto credentials map directly to every minimum qual: production distributed systems, RCA, circuit breaker/reliability patterns, on-call, Terraform IaC, CloudWatch observability. Chrome internship proves Google-bar production quality. DeepMind SRE context leverages ML infrastructure background as additive signal.

**Gaps:** ~9 months short of 2-year experience threshold. No Prometheus/Grafana in a dedicated SRE context (has it as a skill but not in bullet-level experience). No explicit Google-scale SRE tools (Borg, Borgmon).

**This is Harry's strongest Google application in this batch.** The DeepMind team is especially valuable — SRE supporting AI research infra is a career-accelerating position.

**Visa note:** F-1 OPT → H-1B. Google sponsors H-1B. Disclose proactively.

---

## Machine Summary

```yaml
report_num: 135
company: Google
role: Software Engineer, Site Reliability
team: Google DeepMind
date: 2026-06-12
score: 4.1
archetype: SRE · Platform/Cloud Infrastructure
seniority: Mid (L4 target, L3 floor)
location: Mountain View, CA, USA
comp_base_range: "$149,400-$211,000"
comp_tc_est: "$200K-$280K"
legitimacy: High Confidence
apply_button: true
visa_flag: F-1 OPT → H-1B (Google sponsors)
exp_gap: ~9 months short of 2-year minimum
key_strengths:
  - TiMoto 99.9% uptime with SRE patterns (circuit breaker, auto-rollback, RCA, runbooks, on-call)
  - Terraform IaC + CloudWatch observability
  - Chrome production at 3B-user scale
  - ML infra background additive for DeepMind context
key_gaps:
  - ~9 months short of 2-year experience minimum
  - No Prometheus/Grafana in dedicated SRE context
recommendation: Apply (strongest fit in batch)
```
