# Evaluation: Akuna Capital — Software Engineer (Entry-Level) - Python

**Date:** 2026-07-14
**URL:** https://akunacapital.com/careers/job/8013230/?gh_jid=8013230
**Via:** — (direct; original link shared was the Greenhouse application embed for the same req, `jr_id=6a552db0ae07d60a8d00f806`)
**Archetype:** Backend / Distributed Systems Engineer (primary)
**Score:** 4.3/5
**Legitimacy:** High Confidence
**PDF:** output/159-akuna-capital-harry-nguyen-2026-07-14.pdf
**Status:** Rejected (2026-07-25)

---

> **Outcome — Rejected 2026-07-25 (failed testing round).** Rejection email received from `no-reply@akunacapital.com`, addressed to "Huu Phuc Toan" and naming this Python req specifically: *"The results of your testing did not meet our requirements to move forward in our process."*
>
> **Funnel read:** this is an assessment-stage rejection, not a resume-screen rejection — the application cleared screening and reached Akuna's online test. The CV and targeting did their job here; the gate that closed was the timed technical assessment. Worth separating from resume-stage rejections when running `patterns`, since the corrective action is different (assessment/interview drilling, not CV or targeting changes).
>
> **Open question on the C++ req (#160).** The email names only the Python role, so #160 is not explicitly rejected and remains `Applied` in the tracker. Two unresolved factors, both flagged at evaluation time and neither verified since: (1) Akuna's application requires certifying a single **top preference** role and states you "will not be considered for other Tech and/or Quant roles at Akuna for this recruiting season" — if Python was certified as top preference, #160 may already have been foreclosed by that clause rather than still pending; (2) many trading firms treat a failed entry-level assessment as season-wide rather than per-req. Neither has been confirmed with Akuna — do not treat #160 as either alive or dead without asking the recruiter.
>
> **Assessment details not captured.** The platform, subject matter, and score/threshold of the testing round were never logged, so `assessment-log.mjs` has no entry for it and `data/assessments.tsv` remains empty. If the details are recoverable from the original test invitation email, logging them retroactively would make this the first data point for assessment-channel analysis.

## Machine Summary

```yaml
company: "Akuna Capital"
role: "Software Engineer (Entry-Level) - Python"
score: 4.3
legitimacy_tier: "High Confidence"
archetype: "Backend / Distributed Systems Engineer"
final_decision: "Apply"
hard_stops: []
soft_gaps:
  - "Python depth not showcased in cv.md bullets — Python only appears in the Languages skill row, primary CV proof points are C++/Go/TypeScript"
  - "Onsite 5 days/week in Chicago, no remote/hybrid option — requires relocation from Atlanta"
top_strengths:
  - "Production distributed-systems ownership: gRPC deadlock fix, exactly-once semantics, event-driven architecture (TiMoto, Google Chrome)"
risk_level: "Medium"
confidence: "High"
next_action: "Apply via https://akunacapital.com/careers/job/8013230/?gh_jid=8013230 — reorder CV to lead with distributed-systems + Python-backend framing first"
discard_reasons: []
via: null
company_confidential: false
advertised_comp: "$145,000 minimum base (Illinois Equal Pay Act disclosure)"
```

## A) Role Summary

| Field | Value |
|---|---|
| Archetype | Backend / Distributed Systems Engineer (primary) |
| Domain | Trading infrastructure / platform |
| Function | Build |
| Seniority | Entry-level / New Grad |
| Remote | Onsite — Chicago office, 5 days/week (confirmed by application-form question, no hybrid/remote option offered) |
| Team size | Not disclosed; candidate joins one of Post Trade Technology, Data Engineering, or Crypto teams working alongside traders |
| Culture screen | No `culture_screen` config set in `config/profile.yml` — scored qualitatively, not structurally capped. Mixed evidence: Glassdoor shows both an "A+ organization, culture and atmosphere" review and a separate report of a ~40-person layoff (undated, department unclear). Team-based trading+engineering integration is explicitly emphasized in the JD. |
| TL;DR | Entry-level Python backend/distributed-systems role at a Chicago options market-making firm; strong disclosed pay floor, onsite-only. |

**Geo-mismatch check:** Structured location field says Chicago (not remote); JD body confirms onsite ("Please note the expectation for this role is to work in our Chicago office"). No contradiction — both signals agree.

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| Pursuing technical degree, GPA 3.5+, graduating by Aug 2027 | Georgia State University, BS CS, GPA 3.75/4.0, Expected May 2027 | Strong — graduates 3 months ahead of the JD's deadline |
| Legal US work authorization on day one (F-1 OPT/STEM OPT accepted) | `config/profile.yml` — F-1 status | Direct match — JD explicitly accepts F-1 OPT/STEM OPT |
| Strong OO Python development | Skills row: "Languages: C++, Python, Go, TypeScript..."; Frameworks row: "Django, FastAPI" | Partial — Python is listed but has no dedicated bullet/project in cv.md |
| Demonstrated distributed-systems experience | TiMoto gRPC deadlock fix ("replaced inconsistent lock-acquisition ordering... inter-service layer"); Skills: "gRPC, Protocol Buffers, Circuit breakers, Exactly-once semantics, Event-driven architecture"; Google Chrome C++ IPC transport layer | Strong — direct hit, JD's headline requirement |
| High-performance systems, large data volumes | Develop for Good: N+1 fix, sub-100ms on 10,000+ records; TiMoto: vLLM/PagedAttention serving at scale | Strong |
| Work with trading team, gather requirements, deliver cleanly in changing conditions | TiMoto: primary engineer on 3-person team, cross-functional ownership | Adjacent — no trading-domain experience, but JD states this isn't required |
| Build systems from the ground up, self-starter | TiMoto: "building TiMoto's observability stack from zero"; Develop for Good: "designing a stateless AWS BaaS" | Strong |

**Gaps:**

1. **Python-specific proof points (soft gap).** cv.md doesn't have a dedicated Python bullet — Python only appears in the Languages list, and Django/FastAPI only in the Frameworks list. Not a blocker (JD only asks for "strong programming skills," not a specific language project), but worth closing. *Mitigation:* in the Professional Summary and cover letter, explicitly name Django/FastAPI as the Python backend work underlying the TiMoto bullets — this reformulates existing, real skills-list entries rather than inventing anything.
2. **Onsite-only, Chicago (logistics, not a CV gap).** No remote/hybrid path; requires relocation from Atlanta. *Mitigation:* profile's location policy is "open to relocation for strong roles" — state this directly in the application/cover letter given the strong comp band below.
3. **No finance/trading domain experience.** Explicitly **not** a real gap — the JD states plainly: "Previous experience in finance or trading is not required... we pride ourselves on our ability to onboard those new to the industry."

## C) Level and Strategy

1. **Level detected:** Entry-level / New Grad — matches the candidate's actual level (May 2027 graduate) exactly. This is a purpose-built new-grad req, not a downlevel risk.
2. **Differentiation plan:** Lead with production ownership rather than "student who took courses" — per `_profile.md`'s default lead story. Cite the gRPC deadlock fix and multi-AZ Terraform uptime work as evidence of already operating above the typical new-grad bar.
3. **If downleveled or team-assignment is narrower than expected:** Accept given the strong stated comp floor ($145K+ base, ~$215K+ total comp per market data below); ask specifically which team (Post Trade Tech / Data Engineering / Crypto) and what the 6-month growth path looks like during the interview process.

## D) Comp and Demand

**Company type:** Private proprietary trading firm / options market maker. Doesn't map cleanly onto the shared taxonomy's standard rows — closest analog is a privately-held finance firm with public-company-grade compensation structure, since Akuna publishes a legally mandated comp floor and multiple independent salary aggregators corroborate it closely.

**Compensation reliability:** High — the JD states a legally disclosed minimum (Illinois Equal Pay Act), and third-party sources (Levels.fyi, Glassdoor) independently converge near the same entry-level range.

| Source | Figure | Origin |
|---|---|---|
| Advertised (JD) | $145,000 minimum base — legally mandated floor per Illinois Equal Pay Act; final offer varies with experience/quals | JD |
| Levels.fyi (Junior Software Engineer, total comp) | ~$215K median (range up to $479K at Senior) | [Levels.fyi](https://www.levels.fyi/companies/akuna-capital/salaries/software-engineer) |
| Glassdoor (Software Engineer, all levels) | $148,641 avg base ($118,611–$188,768, 25th–75th pct), 51 salaries | [Glassdoor](https://www.glassdoor.com/Salary/AKUNA-CAPITAL-Software-Engineer-Salaries-E608116_D_KO14,31.htm) |
| Glassdoor/Indeed (Entry-level, 0–1 yr) | $137,222 avg base | Glassdoor/Indeed aggregate |

- **Likely guaranteed base:** ~$145K–160K — the legal floor plus a modest range for experience/quals.
- **Variable/conditional cash components:** The gap between Glassdoor base (~$137–149K) and Levels.fyi total comp (~$215K median) strongly implies a significant year-end bonus/profit-sharing component typical of options market makers — not itemized in the JD.
- **Expected stable cash:** ~$145–160K base is the reliable floor; total comp likely $200K+ once bonus is included, but the bonus portion is discretionary/performance-based, not guaranteed.
- **Non-cash benefits:** Not detailed in the JD; assume standard finance-firm benefits (health, 401k) — unconfirmed.

**Demand trend:** Akuna runs a named, structured annual new-grad "recruiting season" (explicit JD language) — a planned, recurring hiring cycle rather than an ad hoc opening.

**HR verification questions:**
1. Is the $145,000 minimum base fixed, or does it vary by final team assignment (Post Trade Tech / Data Engineering / Crypto)?
2. What is the structure and typical payout range of year-end bonus/profit-sharing for entry-level engineers?
3. Is relocation assistance provided for candidates moving to Chicago?
4. What is the standard timeline for STEM OPT → H-1B sponsorship for this role?
5. Does the "top preference" exclusivity acknowledgment apply only to this recruiting cycle, or to future cycles too?

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---------|---------------|------------------|---------|
| 1 | Professional Summary | Generic distributed-systems framing | Lead with "Python backend engineer with production distributed-systems ownership" | Mirrors the JD's OO Python + distributed-systems ask; closes the Python-visibility gap using existing Skills-list facts, nothing invented |
| 2 | TiMoto bullet order | Leads with the observability-stack bullet | Reorder to lead with the gRPC deadlock fix bullet | Most directly maps to "distributed systems" and "react quickly to changing conditions" |
| 3 | Skills section | "Django, FastAPI" buried in Frameworks row | Move earlier in that row | Surfaces existing Python-web evidence to match JD's Python-first framing |
| 4 | Summary/bullet phrasing | Implicit reliability framing (p99, circuit breaker) | Add a phrase on operating in fast-changing, high-stakes production environments | Mirrors JD's "react quickly and accurately to rapidly changing market conditions" |
| 5 | LinkedIn headline | Current general headline | "Software Engineer \| Distributed Systems & Python Backend" | Aligns to recruiter search terms for this req |

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|-----------------|-----------------|---|---|---|---|------------|
| 1 | Distributed systems / react quickly to changing conditions | TiMoto gRPC deadlock fix | Production gRPC service intermittently failed under concurrent load | Root-cause and fix without downtime | Diagnosed inconsistent lock-acquisition ordering; enforced one sequencing rule across the inter-service layer | Restored 100% eval success at sub-50ms p99 | Lock ordering should be an explicit invariant, not an implicit convention — now documents it for any new concurrent service |
| 2 | High-performance systems, large data volumes | Google Chrome lock-free trie | Settings search was mutex-contended, visibly sluggish for power users | Cut p99 latency without regressing 3B+ users | Replaced mutex-contended search path with a lock-free concurrent trie | 96% p99 cut (1200ms → sub-50ms), zero regressions | Concurrency bugs are often architectural, not just implementation bugs |
| 3 | Elegant solutions to complex problems, self-starter | TiMoto observability stack from zero | No visibility into incident root cause | Build observability from scratch | Deployed Prometheus/Grafana + CloudWatch across gRPC and ML serving layers | Cut root-cause time from unknown to under 15 minutes | Observability has to be built proactively, not reactively |
| 4 | Large data volumes / DB scale | Develop for Good N+1 fix | API response time 3+ seconds on 10,000+ record datasets | Cut latency without redesigning the whole data layer | Diagnosed N+1 query bottleneck, redesigned with PostgreSQL indexing | Sub-100ms response time | Profile before optimizing — the fix only looked like indexing after ruling out other suspects |
| 5 | Communicate with trading team, gather requirements, implement cleanly | Google Chrome cross-team design docs | Cross-team cascading UI bugs slowing feature delivery in Chromium | Decouple UI state propagation cleanly across teams | Architected event-driven TypeScript/React system via observer pattern; wrote design docs, ran code reviews with senior engineers | 68% faster feature delivery across 25K+ lines, 95% test coverage | A good design doc does as much work as the code — it earns senior engineers' trust in the architecture upfront |
| 6 | Reliability under failure, uptime/cost tradeoffs | TiMoto multi-AZ Terraform | Single-zone failures risked taking production down | Improve reliability while cutting cost | Architected multi-AZ ECS Fargate deployment with Terraform IaC, CloudWatch, auto-rollback circuit breaker | 99.9% uptime, 44% infra cost cut ($40-60/mo) | Uptime and cost aren't a tradeoff if you model the failure mode first |

**Recommended case study:** TiMoto live product demo (timoto.ai) — Akuna's "team-based trading + engineering integration" mirrors TiMoto's small-team, full-ownership model; strong parallel for how Harry would work alongside traders as a Python engineer.

**Red-flag questions and how to answer them:**
- *"Why work at a trading firm with no finance background?"* → JD explicitly states finance background isn't required; pivot to the genuine draw being the distributed-systems/production-engineering overlap, with real interest in learning options market-making.
- *"Are you comfortable being disqualified for AI tool use in interviews/assessments?"* → Confirm understanding; the JD states AI use during interviews/assessments causes disqualification, unlike normal daily workflow with Claude Code/Copilot/Cursor.
- *"This role commits you to Akuna as your top preference this season — are you sure?"* → Only apply if this is genuinely the preferred Akuna role, since the acknowledgment is binding for the season and forecloses other Quant/Tech reqs there (Trading roles are explicitly exempted).

## G) Posting Legitimacy

**Assessment:** High Confidence

| Signal | Finding | Weight |
|---|---|---|
| Posting freshness | Live JD page, active "Apply Now" reaching a working Greenhouse application form | Positive |
| Description quality | Names specific teams (Post Trade Technology, Data Engineering, Crypto), explicit requirements (GPA, grad date, tech skills), realistic entry-level scope, explicitly states finance experience isn't required | Positive |
| Salary transparency | Legally disclosed minimum base ($145,000) per Illinois Equal Pay Act | Positive |
| Company hiring signals | A Glassdoor review references a historical "large layoff (40 employees)" — undated, department unclear; no 2026-specific layoff/freeze news found | Neutral |
| Reposting pattern | `scan-history.tsv` shows 6 other distinct Akuna reqs scanned 2026-07-05 (different `gh_jid` values) — this req (8013230) is not a duplicate/repeat listing | Positive |
| Role market context | Entry-level new-grad req tied to a named, structured "recruiting season" — a typical, expected fill cycle | Positive |

**Context notes:** Akuna runs structured annual new-grad recruiting cycles (explicit "this recruiting season" language in the JD), consistent with a real, planned hiring need rather than an evergreen or ghost posting.

**Employment classification signal (US):** No contractor/1099/services-status language found — standard employment framing with an explicit sponsorship disclaimer. No flag.

**Buzzword/infrastructure mismatch signal:** No AI/transformation buzzword pattern present — straightforward backend/infra JD. No flag.

---

## Cover Letter Draft

> Draft generated at evaluation time. Complete via `/career-ops cover 159-akuna-capital-2026-07-14` to fill in angles, confirm research, and generate the PDF.
> Gaps flagged below — address them during the cover flow.

---

**Opening** *(placeholder — refine with your "why this role" angle)*
Akuna's Entry-Level Python Software Engineer role is where I want to apply distributed-systems engineering to a domain where correctness under concurrent, high-stakes load is the whole job. I build production systems that stay reliable when things move fast — exactly the profile this role calls for.

**Profile introduction**
I'm a Computer Science student at Georgia State University (GPA 3.75, expected May 2027) with production experience shipping distributed systems at Chrome scale and running ML infrastructure as the primary engineer on a 3-person team at TiMoto AI. My work centers on the same problem Akuna's engineers face daily: keeping systems correct and fast under concurrent, changing conditions.

**Key achievements** *(selected from cv.md — exact wording preserved)*
- **Restored 100% evaluation success rate at sub-50ms p99** by resolving a production gRPC deadlock — replaced inconsistent lock-acquisition ordering under concurrent calls with a single enforced sequencing rule across the inter-service layer.
- **Cut mean-time-to-identify 68%** by building a post-mortem practice with runbooks and a shared on-call rotation.
- **96% p99 latency cut** (1,200ms down to sub-50ms), zero production regressions, by replacing a mutex-contended search path with a lock-free concurrent trie serving 3B+ Chrome users.
- **Cut API response time from 3+ seconds to sub-100ms** on 10,000+ record datasets by diagnosing an N+1 query bottleneck and redesigning the data layer with PostgreSQL indexing.

**Problems I will solve** *(placeholder — requires company research + your input)*
> To be completed: which of Post Trade Technology, Data Engineering, or Crypto are you most drawn to, and why? What would you want to fix or build first on that team?

**Closing**
I am happy to discuss further at your convenience.

---

**Gaps flagged:**
- Python isn't backed by a dedicated CV bullet — only appears in the Skills list (Languages, and Django/FastAPI in Frameworks). Reformulate, don't invent: name the existing Django/FastAPI entries as the Python backend work underlying the TiMoto bullets.
- Onsite-only in Chicago — no remote/hybrid option. Address relocation directly and early if applying.
- The application requires acknowledging this is Akuna's "top preference" role for the season, foreclosing other Quant/Tech reqs there (Trading roles excepted) — confirm this is the intended Akuna role before submitting.

**JD keywords to mirror** *(extracted for ATS + human read)*
Python, Object-Oriented Python Development, distributed systems, Post Trade Technology, Data Engineering, Crypto, high-performance systems, market data, options market making, low latency, trading strategies, mathematical models, self-starter, Chicago, entry-level, new grad, STEM OPT, H-1B

---
*Run `/career-ops cover 159-akuna-capital-2026-07-14` to complete angles, confirm company research, and generate the PDF.*

## Keywords extracted

Python, Object-Oriented Programming, distributed systems, Post Trade Technology, Data Engineering, Crypto team, high-performance systems, market data, trading data, options market making, low latency, trading strategies, mathematical models, self-starter, adaptability, testable codebase, Chicago, entry-level, new grad, GPA 3.5+, STEM OPT, H-1B, Illinois Equal Pay Act, top preference acknowledgment
