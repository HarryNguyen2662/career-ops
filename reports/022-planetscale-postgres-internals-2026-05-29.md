# 022 — PlanetScale — Software Engineer, Postgres Internals

**Date:** 2026-05-29
**Score:** 2.2/5
**URL:** https://job-boards.greenhouse.io/embed/job_app?for=planetscale&token=4257174009
**PDF:** ❌
**Legitimacy:** High Confidence

---

## Machine Summary

```yaml
company: PlanetScale
role: Software Engineer, Postgres Internals
date: 2026-05-29
score: 2.2
status: SKIP
level: Mid-level specialist — implied 3-7 years PostgreSQL contribution history
location: SF Bay Area or Remote (NA/EMEA)
comp_base: "$120,000–$290,000 USD"
comp_equity: "Equity offered — private company; no liquidity timeline"
archetype: "Database Internals / PostgreSQL Core Contributor"
graduation_timing_risk: low — remote role, no graduation restriction
visa_risk: high — PlanetScale filed 1 LCA (FY2021), 0 filings FY2022-2024; very low H-1B sponsor history
apply_rec: "SKIP — 2.2/5 well below 4.0 threshold; all three core requirements are hard blockers: no Postgres internals, no C DB work, no Postgres open-source contributions; comp floor below walk-away ($120K < $140K)"
```

---

## Block A — Role Summary

| Dimension | Detail |
|---|---|
| **Archetype** | Database Internals Engineer — PostgreSQL core contributor |
| **Domain** | Database engine development; open-source PostgreSQL ecosystem |
| **Function** | Contribute patches to Postgres upstream; maintain extensions; engage Commitfest |
| **Seniority** | Mid-level (no explicit floor, but "demonstrated contributions" = 3+ years Postgres-specific) |
| **Location** | SF Bay Area or Remote (NA/EMEA) |
| **Stack** | C (PostgreSQL codebase), Linux/BSD, Git patch workflow |
| **TL;DR** | PlanetScale needs an existing PostgreSQL contributor for MVCC, WAL, query planner, vacuum internals — kernel-level work, not application-layer backend |

---

## Block B — Match with CV

**Score: 1.5/5**

| JD Requirement | Harry's Evidence | Fit |
|---|---|---|
| **C in large codebases** | Google Chrome: C++ IPC + lock-free trie in Chromium | ⚠️ C++ ≠ C; large-codebase experience but not C or DB-specific |
| **PostgreSQL internals (MVCC, WAL, vacuum, query planner, replication, memory contexts)** | None — Harry uses PostgreSQL at application level | ❌ Hard blocker |
| **Demonstrated open-source Postgres contributions** | Pulumi (Go/TypeScript IaC) — unrelated to databases | ❌ Hard blocker |
| **Postgres patch workflow + Commitfest** | No Postgres upstream contributions | ❌ Missing |
| **Linux/BSD + DB profiling** | Linux development yes; DB profiling at application level only | ⚠️ Adjacent |
| **Distributed systems background (nice-to-have)** | gRPC, Raft/Paxos, exactly-once semantics | ✅ Adjacent signal; not sufficient |

**Key gap:** The role requires someone already contributing to the PostgreSQL open-source project. Harry uses PostgreSQL as an application developer (N+1 fix, indexing); that is not the same as contributing to the database engine itself. All three hard requirements are unmet and unmitigatable without a multi-year investment.

---

## Block C — Level and Strategy

"Demonstrated open-source contributions to PostgreSQL" means an existing presence in the Commitfest review process — typically 3–7 years of Postgres-specific work. No viable framing strategy exists. The gap is domain specialization, not seniority.

**Recommendation: SKIP. Do not apply.**

---

## Block D — Comp and Demand

**Score: 3.0/5**

| Component | Value | vs Target |
|---|---|---|
| Base | $120,000–$290,000 | **Floor $120K is $20K BELOW Harry's walk-away ($140K)** ❌ |
| Variable | Included | Unspecified |
| Equity | Yes — private company | No liquidity timeline |
| Remote | Yes (NA/EMEA) | Positive |

Floor below walk-away. Even if the match existed, the comp floor is a secondary disqualifier.

---

## Block E — Customization Plan

Not applicable — SKIP-level role.

---

## Block F — Interview Plan

Not applicable — SKIP-level role. Would not clear initial skills screen without Postgres contribution history.

---

## Block G — Posting Legitimacy

**Tier: High Confidence** (posting is real; role is simply not a match)

| Signal | Finding | Weight |
|---|---|---|
| Posting active | Live Greenhouse form; full JD with comp range | Positive |
| Salary transparency | $120K–$290K base explicitly stated | Positive |
| Company verification | PlanetScale — $105M raised (Series C 2021); 81 employees; profitable | Positive |
| JD specificity | Named internals (MVCC, WAL, vacuum, query planner); Commitfest named; patch workflow | Positive |
| H-1B sponsorship | 1 LCA filed FY2021; 0 filings FY2022–2024 — very low sponsorship history | Concerning |
| Company size | 81 employees — small team | Neutral |

Real posting at a legitimate company. The H-1B concern is additional context if the skills match had existed.

---

## Global Score

**2.2/5 — SKIP**

| Dimension | Score | Driver |
|---|---|---|
| CV Match | 1.5 | No Postgres internals; no C DB work; no Postgres open-source contributions — all hard requirements |
| North Star | 2.5 | Database engineering adjacent to distributed systems; Postgres kernel far from primary archetypes |
| Compensation | 3.0 | $120K floor below $140K walk-away; ceiling inaccessible without matching profile |
| Culture | 3.5 | Remote-friendly; small team; high standards culture |
| Red flag adj. | -2.3 | Postgres contributions gap (-1.0); C DB internals gap (-0.7); H-1B unconfirmed (-0.3); comp below walk-away (-0.3) |
| **Global** | **2.2** | |

**Recommendation: SKIP.** All three core requirements are hard blockers. Time is better spent on active 4.0+ pipeline roles (IMC 4.4/5, Giga 4.1/5, Glean 4.2/5).
