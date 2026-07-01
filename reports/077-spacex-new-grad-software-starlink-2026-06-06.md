# Evaluation: SpaceX — New Graduate Engineer, Software (Starlink)

**Date:** 2026-06-06
**URL:** https://job-boards.greenhouse.io/embed/job_app?for=spacex&token=8399140002
**Archetype:** Systems Software Engineer (embedded + distributed)
**Score:** 2.5/5
**Legitimacy:** High Confidence
**PDF:** ❌ (score < 3.0)

---

## Summary

**TWO INDEPENDENT BLOCKERS — each sufficient alone to recommend against:**

1. **ITAR hard legal barrier** — SpaceX requires applicants to be US citizens, lawful permanent residents, refugees, or asylees under ITAR (International Traffic in Arms Regulations). Harry is on F-1 visa — not eligible without a State Dept. export license, which is essentially impossible for F-1 students on standard programs. The application form requires citizenship status disclosure under ITAR.

2. **Comp floor risk** — New grad base $135K–$155K. Harry's minimum is $140K; floor is below minimum. Total comp with stock options may improve but is uncertain at a private company.

Per apply policy: still apply, but enter with full awareness of these barriers.

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| C, C++, Go, Python, or Rust (required) | Chrome: C++ IPC, lock-free trie; TiMoto: Python/Django; Pulumi: Go | ✅ Strong |
| Graduating 2026 or 2027 (required) | Georgia State BS CS, May 2027 | ✅ |
| 1+ year professional SWE experience | TiMoto (Sep 2025-present) + Chrome (May-Aug 2025) ≈ 12 months | ✅ |
| Linux-based software | AWS/EC2/ECS (TiMoto), CI/CD pipelines | ✅ Basic |
| Embedded devices / custom hardware | Not in CV | ❌ Gap |
| Networking protocols (TCP/IP) | Not explicit in CV | ⚠️ Gap |
| Fault-tolerant devices, long-running systems | TiMoto 99.9% uptime + circuit breakers is adjacent | ⚠️ Partial |
| Performance optimization + debugging | Chrome 96% p99 reduction; gRPC deadlock root-cause | ✅ |
| Security for distributed systems | Not explicit | ❌ Gap |
| ITAR eligibility | F-1 student — NOT eligible | ❌ Hard blocker |

**Gaps:**
1. **ITAR** — Legal export control barrier. SpaceX works on export-controlled technology; F-1 students cannot work on ITAR programs without a State Dept. export authorization (virtually never granted for student visas). This will surface on the application form (Citizenship Status).
2. **Embedded / custom hardware** — Starlink devices are custom silicon; Harry has no embedded experience. Significant gap for Starlink team assignments.
3. **Networking protocols** — No explicit TCP/IP, RF, or modem stack work in CV.
4. **Comp floor** — $135K–$155K base; Harry's minimum is $140K.

---

## C) Level and Strategy

**Level:** New Grad (explicitly named in title). Good fit on experience level.

**If Harry applies despite ITAR:**
> "I'm on F-1 status and will be completing OPT from May 2027. I understand SpaceX's ITAR requirements — I'm flagging this proactively and asking whether your Starlink software roles have any positions on projects that are not ITAR-controlled, or if there's a path to an ITAR exception for software roles. If not, I understand."

In practice: SpaceX HR will likely filter F-1 applicants at citizenship status question.

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| SpaceX new grad SWE stated range | $135,000–$155,000 base |
| Plus | Stock options / LTI (private company, illiquid) |
| Harry target | $150K–$200K |
| Harry minimum | $140K |

Base floor ($135K) is below Harry's $140K minimum. SpaceX stock options are in a private company; liquidity event timing unknown. Mission-driven premium may apply if Harry values the SpaceX mission, but comp is below market for the tech profile.

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active on Greenhouse | Positive |
| JD specificity | Detailed responsibilities, specific tech (Linux, C/C++/Go/Rust), ITAR language, comp range disclosed | Positive |
| Comp disclosed | $135K–$155K stated | Positive |
| Company status | SpaceX — Starlink production, millions of users, real scale | Positive |
| ITAR disclosure | Explicit legal requirement stated in JD | Positive (transparent) |
| Prior SpaceX entries | None in scan history | Neutral |

---

## Keywords extracted

C++, C, Go, Python, Rust, embedded, Linux, ARM, RISC-V, microcontrollers, satellite, telemetry, distributed systems, fault-tolerant, networking, TCP/IP, hardware-in-the-loop, CI/CD, performance optimization, ITAR, new graduate, Starlink, SpaceX, Bastrop TX

---

## Machine Summary

```yaml
company: SpaceX
role: New Graduate Engineer, Software (Starlink)
date: 2026-06-06
url: https://job-boards.greenhouse.io/embed/job_app?for=spacex&token=8399140002
score: 2.5
archetype: Systems Software Engineer (embedded + distributed)
location: Bastrop, TX (on-site)
comp_range: "$135,000–$155,000 base + private stock options"
visa_risk: "F-1 — ITAR HARD LEGAL BLOCKER; SpaceX requires US citizen/LPR/refugee/asylee; F-1 not eligible"
legitimacy: High Confidence
recommendation: "SKIP recommended — ITAR legal barrier + comp below minimum; apply only if Harry wants to disclose F-1 status and ask about ITAR exceptions on specific teams"
```
