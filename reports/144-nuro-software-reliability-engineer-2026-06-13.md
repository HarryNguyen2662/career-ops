# 144 · Nuro — Software Reliability Engineer (Temporary FTE)

**Date:** 2026-06-13
**Score:** 3.3/5
**URL:** https://www.nuro.ai/careersitem?gh_jid=7999651&gh_src=bcd22a501us
**PDF:** ✅
**Legitimacy:** Tier 1 — Active (Greenhouse embed, Apply form fully loaded, "New" badge confirmed via Playwright)
**Verification:** confirmed (Playwright)

---

## Block A — Role Fit

**Archetype match: SRE / Platform Infrastructure** — strong alignment on paper.

The Robotics Reliability Engineering (RRE) team role maps directly to Harry's SRE archetype: fleet-scale observability pipelines, automated triage/correlation, on-call rotation, root-cause analysis, and SLO enforcement. These are exactly what Harry built at TiMoto (99.9% uptime SLO, circuit breakers, on-call, post-mortems) and the language stack (Python, Go, C++) is a perfect overlap.

**BUT — critical structural flags:**
- **Temporary FTE (12 months):** This is a contract-to-hire with "potential for extension based on performance and business needs." Not a permanent headcount offer. For an F-1 OPT holder, a 12-month temp role that doesn't convert leaves Harry without employer sponsorship continuity — a real visa risk.
- **Domain:** Autonomous vehicles / robotics. Not Harry's primary AI/ML infra focus. The RRE work is fleet operations and hardware-adjacent reliability, not LLM infrastructure or distributed ML serving.

**Score: A = 3.8/5** (strong SRE signal, damped by temp nature and domain mismatch)

---

## Block B — Experience Match

**Required qualifications (all met):**
- ✅ Experience writing and shipping software with ownership mindset → TiMoto primary engineer, Chrome 3B+ users shipped
- ✅ Python, Go, Bash, C++ → Harry's full primary stack
- ✅ SSH + CLI, Linux system inspection → TiMoto on-call, AWS ECS/EC2 operations
- ✅ Interest in reliability engineering as growth path → SRE archetype confirmed

**Harry's proof points that map directly:**
- TiMoto: multi-AZ AWS ECS Fargate, circuit breaker, auto-rollback → fleet infrastructure patterns
- TiMoto: 99.9% uptime SLO, on-call rotation, root-cause analysis, runbooks, post-mortems → exact RRE workflow
- TiMoto: CloudWatch + Prometheus/Grafana observability → fleet signal pipelines
- TiMoto: gRPC inter-service layer, exactly-once semantics → distributed systems for AV data pipelines
- Google Chrome: C++ IPC transport layer, sub-50ms p99 → performance-minded systems engineer

**Gap:** No robotics/AV-specific experience. No fleet hardware context. But JD doesn't require it — "interest in reliability engineering as growth path" is the signal for a junior hire.

**Score: B = 4.3/5**

---

## Block C — Compensation

| Component | Details |
|-----------|---------|
| Base range | $109,250 – $163,370 |
| Bonus | Annual performance bonus |
| Equity | Mentioned but likely limited for temp role |
| **Harry's floor** | **$140K** |

Bottom of range ($109K) is **below Harry's $140K floor**. Top ($163K) is above. As a temp role, negotiating to the upper band is harder than for permanent headcount.

Realistic landing zone: $130K–$145K base for a new grad / early-career temp hire. This is at the edge or below floor.

**Score: C = 3.0/5**

---

## Block D — Location / Work Mode

**Location:** Mountain View, CA (HQ) + San Francisco, CA
**Work mode:** Hybrid — **4 days/week in office** (Thursday at MV HQ, remaining 3 days at MV or SF)

This is functionally near-full on-site. Harry is currently at Georgia State University (Expected May 2027) in Atlanta. This role would require:
1. **Relocation to Bay Area while still enrolled** — effectively requires a leave of absence or dropping to part-time enrollment
2. Commuting between Mountain View and San Francisco regularly

This is the single biggest practical constraint. Harry may have his own plans (graduation, co-op, gap year) — flagging prominently but not blocking per apply policy.

**Score: D = 2.0/5**

---

## Block E — Growth / Company

**Nuro:** Self-driving technology company founded 2016, pivoted to licensing its Nuro Driver™ platform. Backed by SoftBank, Toyota, T-Mobile. Significant headcount reductions in 2022-2023; now leaner team licensing AV tech to automakers.

**Growth trajectory:**
- Pro: Hands-on fleet reliability at scale in a specialized AV environment — uncommon experience
- Pro: Direct path into distributed systems + embedded reliability engineering
- Con: Temp role limits long-term career trajectory at Nuro
- Con: AV domain is narrower than general ML infra / cloud platforms where Harry's skills are more broadly applicable
- Con: Company has had significant layoffs; temp headcount suggests capacity uncertainty

**Score: E = 2.8/5**

---

## Block F — Red Flags

🔴 **TEMP ROLE (12 months):** Critical for F-1 OPT. Harry's STEM OPT authorization is employer-tied. A temporary position that doesn't convert means Harry may need a new employer within 12 months, adding visa instability. **Ask explicitly: "Is this role eligible for conversion to permanent headcount? What % of temp hires convert?"**

🔴 **LOCATION — 4 days/week Mountain View:** Effectively requires relocation and/or leave of absence from Georgia State. Harry is enrolled through May 2027.

🟡 **VISA SPONSORSHIP RISK:** Application form asks "Do you now, or will you in the future, require sponsorship?" — Yes for H-1B. Companies sometimes balk at sponsoring temp roles. Confirm Nuro's willingness before investing time.

🟡 **COMPANY STABILITY:** Nuro has had restructuring. Using "temporary FTE" framing may indicate budget constraints.

🟡 **COMP RANGE BOTTOM:** $109K is well below Harry's $140K floor. Must negotiate to upper band.

**Score: F = 2.0/5**

---

## Block G — Posting Legitimacy

- Source: Greenhouse embed on nuro.ai/careersitem
- Apply form fully rendered with name/email/resume fields active
- "New" badge visible on posting
- Confirmed active via Playwright browser_snapshot
- **Tier 1 — Active**

---

## Overall Score: 3.3/5

| Block | Score |
|-------|-------|
| A — Role Fit | 3.8 |
| B — Experience | 4.3 |
| C — Comp | 3.0 |
| D — Location | 2.0 |
| E — Growth | 2.8 |
| F — Red Flags | 2.0 |
| **Overall** | **3.3/5** |

**Recommendation: Apply with eyes open — but address red flags FIRST.**

Harry is a strong technical fit (SRE archetype, matching stack, production reliability credentials). But three structural issues make this a below-floor offer: (1) temp contract jeopardizes OPT continuity, (2) near-full on-site in Mountain View while enrolled at Georgia State, (3) comp range starts below floor.

**Before applying, confirm with recruiter:**
1. "Is this role eligible for conversion to permanent headcount, and what's the typical conversion rate?"
2. "Does Nuro sponsor H-1B for temporary FTE positions?"
3. "Is there flexibility on in-office days given I'd be relocating?"

If conversion rate is high and H-1B sponsorship is confirmed, this is worth pursuing. Otherwise, the SRE III roles at Google (#140-142, 4.4/5) are strictly better for Harry's profile.

---

## Pitch Angle

> "I've been running exactly this SRE playbook at TiMoto — multi-AZ fleet infrastructure, circuit breakers, on-call rotations, 99.9% uptime SLO enforcement, and post-mortem-driven improvement loops. I shipped a C++ IPC transport layer at Chrome scale. The RRE mission at Nuro — turning fleet signals into durable engineering improvements — is the work I want to be doing."

---

## Machine Summary

```yaml
report: 144
company: Nuro
role: Software Reliability Engineer (Temporary FTE)
score: 3.3
score_breakdown:
  role_fit: 3.8
  experience: 4.3
  compensation: 3.0
  location: 2.0
  growth: 2.8
  red_flags: 2.0
location: Mountain View, CA (HQ) + San Francisco, CA
work_mode: hybrid_heavy (4 days/week in-office)
employment_type: temporary_fte_12mo
comp_base_range: [109250, 163370]
comp_floor_met: false
legitimacy: tier1_active
visa_flag: temp_role_otp_continuity_risk
location_flag: relocation_required_student_enrolled
apply: apply_with_caution
top_skills_matched: [SRE, Python, Go, C++, observability, distributed_systems, on-call, reliability]
archetypes: [SRE, Platform Infrastructure]
```
