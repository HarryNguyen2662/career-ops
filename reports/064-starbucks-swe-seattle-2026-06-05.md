# Evaluation: Starbucks -- Software Engineer (ST, Seattle WA)

**Date:** 2026-06-05
**URL:** https://apply.starbucks.com/careers/job/481078371803-software-engineer-st-seattle-wa-seattle-washington-united-states
**Archetype:** Site Reliability Engineer / Platform + Cloud Infrastructure Engineer (hybrid)
**Score:** 3.2/5
**Legitimacy:** Proceed with Caution
**PDF:** output/064-starbucks-swe-seattle-harry-nguyen.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| **Archetype** | SRE / Platform & Cloud Infrastructure (hybrid) |
| **Domain** | Enterprise technology reliability & delivery tooling |
| **Function** | Build + operate (release engineering, monitoring, security compliance) |
| **Seniority** | Individual Contributor — 0--4 years experience (new grad eligible) |
| **Remote/Onsite** | In-Office, Seattle WA — 4 days/week |
| **Pay range** | $111,000--$185,000 (stated in posting) |
| **Team size** | Not mentioned |
| **TL;DR** | Enterprise SRE/platform role focused on build-and-release tooling, service monitoring, and security compliance at a F500 consumer company -- not a product-engineering or ML role. |

---

## B) Match with CV

### Requirement-to-CV Mapping

| JD Requirement | Match | CV Evidence |
|----------------|-------|-------------|
| 0--4 yrs professional software development | Strong | TiMoto AI (Sep 2025--Present) + Google Chrome intern (May--Aug 2025) + Develop for Good intern |
| BS CS or related field | Strong | Georgia State CS, GPA 3.75, Expected May 2027 |
| Systems & production operations (monitoring, telemetry, incident response) | Strong | "Maintained distributed production systems... triaged and resolved incidents via root-cause analysis, documented runbooks, participated in on-call rotation" (TiMoto); CloudWatch observability bullet |
| Automation & coding -- Python, Go, Java, C++ | Strong | Languages: C++, Python, Go, TypeScript, Java, Bash (cv.md Skills) |
| Cloud & delivery tooling -- AWS/Azure, CI/CD | Strong | "multi-AZ ECS Fargate with Terraform IaC, CloudWatch observability... auto-rollback on health check failure" (TiMoto); "90% deployment time reduction via CI/CD (GitHub Actions)" (Develop for Good) |
| Distributed systems + TCP/IP networking | Moderate | Distributed systems coursework + gRPC inter-service layer + multi-AZ; no explicit TCP/IP or DNS routing work listed |
| Databases/data stores (SQL/NoSQL) | Strong | PostgreSQL (TiMoto, Develop for Good), Redis (Skills), MongoDB (Skills); N+1 fix bullet |
| High-availability / reliability engineering | Strong | 99.9% uptime, circuit breaker + auto-rollback (TiMoto) |
| Security & compliance baselines | Weak | Not present in CV -- stateless JWT auth is the closest signal |
| Build & release process engineering | Weak | CI/CD GitHub Actions (Develop for Good) mentioned but at a high level; no explicit release tooling ownership |
| Scripting for automation | Moderate | Bash in Skills, Python in Skills; no dedicated automation scripting bullet |

### Gaps

| Gap | Blocker? | Mitigation |
|-----|----------|------------|
| Security / compliance hardening | Soft | Note AWS IAM and security baseline work is common with Terraform IaC; describe in cover letter |
| Build & release tooling depth | Soft | Frame GitHub Actions CI/CD at Develop for Good + TiMoto auto-rollback; not a hard gap |
| TCP/IP / DNS / networking depth | Soft | Distributed systems coursework + gRPC service mesh is adjacent; mention Networks coursework |
| F-1 visa -- sponsorship unconfirmed | Risk flag | See sponsorship note below |

**Sponsorship note:** Starbucks posted $111K--$185K and does NOT mention sponsorship in the JD. Large enterprise companies (F500) vary widely. With the April 2026 tech layoffs (61 roles, mostly non-SWE), sponsorship budget may be tightened. Per apply policy: still apply, ask recruiter early.

**Archetype fit score (this role vs Harry's target):** The role is an SRE/platform match (secondary archetype, not primary). It is NOT ML infra, systems software, or high-frequency backend -- Harry's strongest proof points are partially adjacent but not dead-on.

---

## C) Level and Strategy

### Level Analysis

| Dimension | JD signal | Harry's level |
|-----------|-----------|---------------|
| Experience | 0--4 years | ~1.5 years effective (1 internship + TiMoto part-time) |
| Seniority | IC, entry | Good fit |
| Scope | Production ops + release engineering | TiMoto covers ops; release engineering is lighter |
| Company complexity | F500, 35K+ tech partners globally | Harry's scale is startup (3-person team) + big-tech (Chrome intern) |

### Sell Strategy

Frame Harry as: **"Production-ready new grad who already operates distributed systems and runs on-call -- not a student learning prod for the first time."**

Key phrases:
- "I've maintained distributed production systems with 99.9% uptime at TiMoto -- on-call rotation, runbooks, root-cause analysis. I understand what it means when a service goes down at 2am."
- "At Google I shipped infrastructure (IPC transport + lock-free search) into a product serving 3B users -- code review bar was high and test coverage non-negotiable."
- "I use Terraform for IaC and GitHub Actions for CI/CD today -- not theoretical, in production."

### If Downleveled

Starbucks has L24--L28 bands. This role likely maps to L24/L25. Accept if $130K+ base (bottom of posted range is $111K which is below Harry's $140K minimum). Negotiate toward middle of range ($148K). Request 6-month review with promotion criteria to L26.

---

## D) Comp and Demand

| Source | Data | Notes |
|--------|------|-------|
| JD (stated) | $111,000--$185,000 base | Wide band -- entry vs senior overlap |
| Levels.fyi (L26 median, Seattle) | $167,172 TC | Includes base + bonus; no public equity data |
| Levels.fyi (range, Seattle) | $120K--$237K | L24--L28 band |
| Glassdoor (SWE Seattle) | $162K base / $230K TC est. | Bonus-heavy; includes senior data |

**Assessment:**
- Bottom of range ($111K) is **below Harry's $140K minimum** -- flag. At market band ($140K--$160K base) this is acceptable for a new grad at a F500.
- Starbucks is **not a top-quartile tech payer** (no pre-IPO equity, no RSU at Google/Meta scale). Total comp likely $130K--$165K base + 10--15% annual bonus for entry level.
- If offered below $140K base, push back or decline.

**Sponsorship & demand trend:**
- Enterprise SRE/platform roles at consumer companies are stable but slow-growth vs. pure-tech employers.
- April 2026 layoffs (61 tech jobs, SoDo HQ) were roles like TPMs, cybersecurity analysts, scrum masters -- **NOT SWE platform roles**. New CTO Varadarajan (ex-Amazon) appears to be reorienting spend toward hiring SWEs on platform/reliability.
- This posting was live as of 05/22/2026 and active as of evaluation date.

---

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---------|---------------|-----------------|-----|
| 1 | Summary | Distributed systems / ML serving focus | Add "production reliability and service observability" framing alongside ML infra | JD calls out monitoring, telemetry, high-availability explicitly |
| 2 | TiMoto bullet 4 | "99.9% uptime, 44% cost reduction" | Move this bullet higher; add explicit mention of CloudWatch alerting and incident runbooks | Matches "service monitoring, deep telemetry, high-availability" requirement verbatim |
| 3 | TiMoto bullet 5 | "participated in on-call rotation" | Expand to: "documented runbooks and post-mortem learnings; on-call rotation for gRPC + ML serving layer" | On-call and runbooks are directly called out in JD preferred quals |
| 4 | Develop for Good bullet | High-level CI/CD mention | Add: "configured GitHub Actions pipeline with deployment gates, rollback triggers, and environment promotion" | "CI/CD or build/release tooling and automation" is a preferred qualification |
| 5 | Skills: Cloud & Infrastructure | Current line sufficient | Add "incident response, runbooks" under Cloud & Infrastructure or new Reliability line | Matches JD language directly |

**Top 5 LinkedIn changes:**
1. Headline: Add "reliability" or "platform" alongside distributed systems
2. TiMoto description: surface on-call and runbook work more prominently
3. Skills section: add "Service Monitoring," "Incident Response," "Observability"
4. Featured: link timoto.ai as production uptime case study
5. About section: one sentence on 99.9% uptime + CloudWatch telemetry ownership

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|----------------|-------------|---|---|---|---|------------|
| 1 | Production ops, incident response | TiMoto gRPC deadlock | Production deadlock under concurrent calls | Fix the bug under time pressure | Traced shared resource acquisition, redesigned call sequencing | 100% eval success, sub-50ms p99 restored | Would add formal runbook entry same day; learned to add instrumentation before the incident, not after |
| 2 | Service monitoring, telemetry | TiMoto CloudWatch/circuit breaker | Need 99.9% uptime on 3-person team with no ops staff | Set up multi-AZ + auto-rollback | Terraform IaC, CloudWatch alarms, circuit breaker pattern | 99.9% uptime, 44% cost cut | Learned that cost and reliability are complementary when you right-size compute |
| 3 | Automation & coding | Develop for Good CI/CD | 90% manual deployment process | Automate deploy for nonprofit engineering team | GitHub Actions pipeline with environment gates | 90% deployment time reduction | Would add staging environment promotion gates earlier; manual gate created bottleneck |
| 4 | Fast, reliable delivery / build processes | Google Chrome IPC | Ship IPC transport for Chrome stable to 3B users | Zero regressions on release to stable | Protocol Buffers over custom serialization; 95% test coverage | Shipped to stable channel | Protobuf schema evolution pays off long-term; initial overhead worth it at Chrome's release cadence |
| 5 | Distributed systems + core technical foundations | TiMoto vLLM/PagedAttention | OOM failures under concurrent inference | Serve LLMs reliably in production | PagedAttention to eliminate KV cache fragmentation | Zero OOM failures at production traffic | Learned to design for worst-case memory pressure, not average-case load |
| 6 | Debugging & troubleshooting | Develop for Good N+1 | 3s+ response time on large dataset queries | Fix performance in production-like load | Diagnosed N+1 via query logging; redesigned with PostgreSQL indexing | Sub-100ms on 10K+ records | Always profile before optimizing; the bottleneck was 3 layers deeper than I thought |

**Recommended case study:** TiMoto AI -- walk through the reliability architecture (multi-AZ ECS, circuit breaker, CloudWatch, auto-rollback). Frame it as: "Here is how a 3-person team ran 99.9% uptime on a production ML serving stack." This maps directly to what Starbucks Technology is hiring for.

**Red flag questions:**
- *"You're still in school -- how will you balance work and studies?"* → "I've been working at TiMoto as a primary engineer since September 2025 while carrying a full courseload. My GPA is 3.75 and the system is in production. The discipline required to operate both is something I've already demonstrated."
- *"Do you have experience with enterprise-scale systems vs startup scale?"* → "TiMoto gave me full ownership of distributed systems design. Google gave me the opposite -- code reviewed by senior Chrome engineers, shipped to 3B users, zero tolerance for regressions. I've operated at both ends of the scale spectrum."
- *"Starbucks is a coffee company -- why tech here vs a pure tech firm?"* → "The technology team at Starbucks operates at massive scale -- 35K+ stores globally, millions of daily transactions. The reliability and platform work here is real. I'm interested in Varadarajan's new roadmap and what he's building after coming from Amazon."

**Story bank check:** Stories 1, 2, 3, 5, 6 are likely already in story-bank.md from prior evaluations. Story 4 (Chrome CI/CD) is new framing -- append.

---

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting date | Posted 05/22/2026 -- 14 days ago | Positive |
| Apply button | Active -- "Apply Now" live and functional | Positive |
| Expiration date | 06/22/2026 -- still 17 days remaining | Positive |
| JD specificity | Mentions technologies (Python, Go, Java, C++, AWS, Azure, CI/CD), specific responsibilities (build & release, monitoring, security baselines) | Positive |
| Pay range stated | $111,000--$185,000 -- explicit range listed | Positive |
| April 2026 layoffs | 61 tech jobs cut (TPM, cybersecurity, scrum masters, architects) -- WARN filed, separations June--August 2026 | Concerning |
| Reposting history | No Starbucks entries in scan-history.tsv -- no prior repost detected | Neutral |
| Layoff department overlap | Layoffs affected non-SWE roles (PM, cybersecurity analysts, admins); SWE platform roles appear to be the *target hire* under new CTO | Mitigating |
| Similar roles on site | "software engineer sr - ST, Seattle" also posted same date -- suggests active hiring push | Positive |
| Role-company fit | Platform/reliability SWE fits enterprise tech transformation under new Amazon-origin CTO | Positive |

**Context notes:**
- The April 2026 layoffs are real (61 WARN-filed) but were concentrated in non-engineering management and specialist roles. The new CTO appears to be restructuring toward engineering-heavy platform teams -- this SWE posting is likely part of that hire wave.
- 4 days/week in-office (Seattle) is aggressive vs tech market norm but explicit -- no bait-and-switch risk.
- Wide salary band ($111K--$185K) is standard Starbucks practice for IC bands -- not a ghost posting signal.
- **Bottom line:** Active posting from a company in active restructuring. The layoffs are concerning but directionally they are *making room* for SWE hires, not eliminating them. Worth applying with awareness.

---

## Keywords Extracted

```
service monitoring, telemetry, high-availability, build and release, CI/CD, incident response,
automation, Python, Go, Java, C++, AWS, Azure, distributed systems, TCP/IP, DNS, SQL, NoSQL,
security baseline, compliance, configuration management, production support, on-call, scripting,
observability, cloud infrastructure, reliability engineering, software development lifecycle
```

---

## Machine Summary

```yaml
report: "064"
company: Starbucks
role: "Software Engineer (ST, Seattle WA)"
date: "2026-06-05"
score: 3.2
archetype: "SRE / Platform & Cloud Infrastructure"
location: "Seattle, WA"
remote: "In-Office (4 days/week)"
comp_range: "$111K--$185K base"
comp_at_target: false
legitimacy: "Proceed with Caution"
sponsorship: "unconfirmed"
apply_recommendation: "apply -- warn about comp floor and layoff context"
key_gaps:
  - "Security/compliance hardening (soft)"
  - "Build & release tooling depth (soft)"
  - "F-1 sponsorship unconfirmed"
key_strengths:
  - "Production ops, on-call, incident response (TiMoto)"
  - "99.9% uptime, circuit breaker, multi-AZ IaC"
  - "CI/CD GitHub Actions (Develop for Good)"
  - "0--4yr experience range: Harry is a direct fit"
```
