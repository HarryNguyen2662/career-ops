# Evaluation: Akuna Capital — Software Engineer (Entry-Level) - C++

**Date:** 2026-07-14
**URL:** https://akunacapital.com/careers/job/8013085/?gh_jid=8013085
**Via:** — (direct; original link shared was the Greenhouse application embed for the same req, `jr_id=6a553593268af95237bea1a0`)
**Archetype:** Systems Software Engineer (primary), hybrid with Backend / Distributed Systems Engineer
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** output/160-akuna-capital-cpp-harry-nguyen-2026-07-14.pdf

---

> ⚠️ **Cross-report conflict with #159 (Akuna Capital — Software Engineer (Entry-Level) - Python, evaluated same day):** Akuna's application requires certifying this role is your **top preference** and that you "will not be considered for other Tech and/or Quant roles at Akuna for this recruiting season." You now have two Akuna entry-level SWE reqs evaluated in the same recruiting season (#159 Python, #160 C++). You can only truthfully mark **one** of them as top preference — submitting both with a "yes" on each risks contradicting your own certification on the form ("I certify that all information I have provided... is true, complete, and accurate"). Pick one before applying to either. Based purely on CV match strength, this C++ req scores higher (see Block B) — but the decision is yours (team, growth, personal interest may weigh differently).

## Machine Summary

```yaml
company: "Akuna Capital"
role: "Software Engineer (Entry-Level) - C++"
score: 4.5
legitimacy_tier: "High Confidence"
archetype: "Systems Software Engineer"
final_decision: "Apply"
hard_stops: []
soft_gaps:
  - "JD asks for modern C++20/C++23 experience specifically; cv.md doesn't state which C++ standard was used at Google Chrome"
  - "Onsite 5 days/week in Chicago, no remote/hybrid option — requires relocation from Atlanta"
  - "Top-preference exclusivity directly conflicts with report #159 (Akuna Python req, evaluated same day) — only one can be truthfully marked top preference"
top_strengths:
  - "Near-exact match to 'lock-free data structures and algorithms' and 'networking or protocol encoding/decoding' via the Google Chrome C++ IPC/Protobuf transport layer and lock-free concurrent trie bullets"
risk_level: "Medium"
confidence: "High"
next_action: "Decide with the candidate which Akuna req (this C++ role or #159's Python role) to mark as top preference before applying to either"
discard_reasons: []
via: null
company_confidential: false
advertised_comp: "$145,000 minimum base (Illinois Equal Pay Act disclosure) + discretionary performance bonus + benefits package"
```

## A) Role Summary

| Field | Value |
|---|---|
| Archetype | Systems Software Engineer (primary) — C++, lock-free structures, concurrency, performance profiling; hybrid overlap with Backend / Distributed Systems Engineer (distributed systems, async architectures) |
| Domain | Trading infrastructure / platform (core systems) |
| Function | Build |
| Seniority | Entry-level / New Grad |
| Remote | Onsite — Chicago office (same structural location field and onsite expectation as the Python req, #159) |
| Team size | Small-to-medium teams, frequently interfacing with Quant and Trading |
| Culture screen | No `culture_screen` config set in `config/profile.yml` — scored qualitatively (same evidence base as #159: mixed Glassdoor signals, team-based trading+engineering integration explicitly emphasized) |
| TL;DR | Entry-level C++ systems-engineering role at the same Chicago options market maker as #159, with a JD that maps almost one-to-one onto the candidate's strongest CV bullets. |

**Geo-mismatch check:** Structured location field says Chicago (not remote); no contradiction with JD body (no remote/hybrid language present).

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|---|---|---|
| Pursuing technical degree, graduating by Aug 2027 | Georgia State University, BS CS, GPA 3.75/4.0, Expected May 2027 | Strong |
| Legal US work authorization day one (F-1 OPT/STEM OPT accepted) | `config/profile.yml` — F-1 status | Direct match |
| Modern C++ experience (C++20+, C++23 preferred) | cv.md lists C++ as a primary language (Skills row, Chrome bullets); no C++ standard version stated | Partial — likely true given Chrome-scale production C++, but not explicitly dated/versioned in cv.md |
| Distributed systems | TiMoto gRPC deadlock fix, exactly-once semantics, event-driven architecture | Strong — same evidence as #159 |
| Lock-free data structures and algorithms | Google Chrome: "replacing a mutex-contended search path with a lock-free concurrent trie" | Direct, near-exact match — this is the JD's own phrase |
| Networking or protocol encoding/decoding | Google Chrome: "C++ IPC transport layer... choosing Protocol Buffers over custom serialization" | Direct, near-exact match |
| Parallel processing / asynchronous architectures | TiMoto vLLM/PagedAttention concurrent inference serving; Chrome IPC transport at 10K+ req/sec | Strong |
| Performance profiling | Chrome: 96% p99 latency cut (1,200ms → sub-50ms) — implies profiling to find and verify the bottleneck | Adjacent — outcome is proven, but cv.md doesn't name specific tools (perf/gprof/vtune) |
| Scripting (Python or shell) | cv.md Languages: Python, Bash | Direct match |
| Debugging tools (GDB, Valgrind, ASan) | Not mentioned in cv.md | Gap — no evidence either way |
| Communicate with non-technical stakeholders (Quant/Trading) to gather requirements | TiMoto: primary engineer on 3-person team, cross-functional ownership | Adjacent — no trading-domain stakeholders specifically, but demonstrated cross-functional delivery |
| Build complex systems from the ground up | TiMoto: "building TiMoto's observability stack from zero"; Develop for Good: "designing a stateless AWS BaaS" | Strong |

**Gaps:**

1. **C++ standard version unstated (soft gap).** JD wants C++20/23 specifically. cv.md's Chrome bullets don't date the C++ standard used. *Mitigation:* if this comes up in a screen, confirm directly — Chromium's codebase has used C++17/20 features extensively in recent years, so this is very likely true, but shouldn't be asserted in writing without the candidate confirming it firsthand.
2. **Debugging tools (GDB, Valgrind, ASan) — no CV evidence either way.** *Mitigation:* not a blocker (JD lists this among "familiarity with," not a hard requirement); if relevant, candidate should confirm familiarity before the interview rather than have it asserted in the CV/cover letter.
3. **Onsite-only, Chicago (logistics, not a CV gap)** — identical to #159; profile's relocation openness applies the same way here.
4. **No finance/trading domain experience** — explicitly **not required** per JD, identical framing to #159.

## C) Level and Strategy

1. **Level detected:** Entry-level / New Grad — matches candidate's actual level exactly, same as #159.
2. **Differentiation plan:** This req's JD vocabulary ("lock-free data structures," "protocol encoding/decoding") lines up almost verbatim with the Chrome bullets — lead with those two bullets specifically rather than TiMoto, since they're the closest literal match to the JD's own phrasing.
3. **If downleveled or team-assignment narrower than expected:** Same as #159 — accept given the strong disclosed comp floor; ask which systems area (algorithms/data structures, concurrency, networking, performance, or hardware) during interviews.

## D) Comp and Demand

*Company-type classification and market research reused from report #159 (same company, evaluated same day) — no new queries run, per the bounded research budget.*

**Company type:** Private proprietary trading firm / options market maker — see #159 for full classification rationale. Compensation reliability: High.

| Source | Figure | Origin |
|---|---|---|
| Advertised (JD) | $145,000 minimum base (Illinois Equal Pay Act) + discretionary performance bonus + benefits package (medical, dental, vision, retirement, PTO) — more explicit about bonus/benefits than the Python req's disclosure | JD |
| Levels.fyi (Junior Software Engineer, total comp) | ~$215K median (range up to $479K at Senior) | [Levels.fyi](https://www.levels.fyi/companies/akuna-capital/salaries/software-engineer) |
| Glassdoor (Software Engineer, all levels) | $148,641 avg base ($118,611–$188,768, 25th–75th pct), 51 salaries | [Glassdoor](https://www.glassdoor.com/Salary/AKUNA-CAPITAL-Software-Engineer-Salaries-E608116_D_KO14,31.htm) |

- **Likely guaranteed base:** ~$145K–160K (same floor logic as #159).
- **Variable/conditional cash components:** This JD explicitly names a "discretionary performance bonus" as part of total comp — more transparent than the Python req, which didn't mention bonus structure at all. Still not quantified.
- **Expected stable cash:** ~$145–160K base reliable; total comp likely $200K+ with bonus, which remains discretionary/performance-based.
- **Non-cash benefits:** This JD explicitly lists "employer-paid medical, dental, vision, retirement contributions, paid time off" — more detail than the Python req provided.

**Demand trend:** Same named annual "recruiting season" cycle as #159 — planned, recurring hiring need. C++ systems roles at market-making firms are core-business-critical (unlike more peripheral engineering functions), typically a stable, ongoing hiring category.

**HR verification questions:** Same five questions as #159 apply here (base fixed vs. team-dependent, bonus structure/payout range, relocation assistance, STEM OPT → H-1B timeline) — add: does the "top preference" acknowledgment apply per-req or per-candidate-per-season (relevant given the #159/#160 conflict flagged above)?

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---------|---------------|------------------|---------|
| 1 | Professional Summary | Currently distributed-systems-first framing (as tailored for #159) | Lead with "Systems engineer with production C++ and lock-free concurrency experience" | Mirrors this JD's specific vocabulary — "lock-free data structures," "protocol encoding/decoding" — more precisely than a Python-first framing would |
| 2 | Google Chrome bullet order | Currently 3rd in queue behind TiMoto (per #159's tailoring) | Move Google Chrome experience to lead position, with the lock-free trie and C++ IPC bullets first | Most direct literal match to this JD's own requirement phrases |
| 3 | Skills section | "Distributed Systems" row leads | Add or surface a "Systems & Concurrency" row (C++, lock-free structures, IPC, UNIX/Linux) similar to what was used for the HRT (#158) CV | This JD is a near-identical systems/concurrency profile to HRT's — reuse that framing rather than the Python-tailored skills ordering |
| 4 | Bullet phrasing | No explicit debugging-tool or C++ standard mention | Do not add either — no CV evidence to draw from (see gaps 1–2). Address verbally if asked. | Avoids inventing detail not backed by cv.md |
| 5 | LinkedIn headline | Currently drafted as "Distributed Systems & Python Backend" (for #159) | If pursuing this req instead, use "Software Engineer \| Systems, Concurrency & C++" | Matches this req's specific recruiter search terms |

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|-----------------|-----------------|---|---|---|---|------------|
| 1 | Lock-free data structures and algorithms | Google Chrome lock-free trie | Settings search was mutex-contended, visibly sluggish for power users | Cut p99 latency without regressing 3B+ users | Replaced mutex-contended search path with a lock-free concurrent trie | 96% p99 cut (1200ms → sub-50ms), zero regressions | Concurrency bugs are often architectural, not just implementation bugs |
| 2 | Networking / protocol encoding-decoding | Google Chrome C++ IPC transport layer | Chrome needed a new IPC transport layer for its stable channel | Choose a serialization approach that scales across languages and schema versions | Chose Protocol Buffers over custom serialization for schema evolution and cross-language compatibility | Shipped to 3B+ users at sub-50ms p99, 10K+ req/sec | Standardized serialization formats pay for themselves the moment more than one team touches the wire format |
| 3 | Distributed systems / async architectures | TiMoto gRPC deadlock fix | Production gRPC service intermittently failed under concurrent load | Root-cause and fix without downtime | Diagnosed inconsistent lock-acquisition ordering; enforced one sequencing rule across the inter-service layer | Restored 100% eval success at sub-50ms p99 | Lock ordering should be an explicit invariant, documented for any new concurrent service |
| 4 | Building complex systems from the ground up | TiMoto observability stack from zero | No visibility into incident root cause | Build observability from scratch | Deployed Prometheus/Grafana + CloudWatch across gRPC and ML serving layers | Cut root-cause time from unknown to under 15 minutes | Observability has to be built proactively, not reactively |
| 5 | Communicate with non-technical stakeholders (Quant/Trading analog) | Google Chrome cross-team design docs | Cross-team cascading UI bugs slowing feature delivery in Chromium | Decouple UI state propagation cleanly across teams | Architected event-driven TypeScript/React system via observer pattern; wrote design docs, ran code reviews with senior engineers | 68% faster feature delivery across 25K+ lines, 95% test coverage | A good design doc earns stakeholder trust in the architecture before a line of code ships |
| 6 | Ownership / fixing bugs when they arise | TiMoto multi-AZ Terraform + post-mortem practice | Single-zone failures risked taking production down; no structured incident learning process | Improve reliability while building a repeatable ownership habit | Architected multi-AZ ECS Fargate with auto-rollback circuit breaker; built post-mortem practice with runbooks and on-call rotation | 99.9% uptime, 44% infra cost cut; 68% faster mean-time-to-identify | Ownership means building the process that catches the next bug, not just fixing this one |

**Recommended case study:** Google Chrome C++ IPC + lock-free trie work — closer literal match than the TiMoto demo for this specific req, since the JD's own vocabulary (lock-free, protocol encoding, networking) maps directly onto that experience.

**Red-flag questions and how to answer them:**
- *"Why work at a trading firm with no finance background?"* → Same answer as #159 — JD explicitly doesn't require it; pivot to genuine interest in the systems/concurrency problem space.
- *"You applied to two Akuna reqs this season — which is your actual top preference?"* → **This will likely come up if both are submitted.** Have an honest, decided answer ready before any recruiter contact — do not let the firm discover the conflict before the candidate has resolved it.
- *"Are you comfortable being disqualified for AI tool use in interviews/assessments?"* → Same as #159.

## G) Posting Legitimacy

**Assessment:** High Confidence

| Signal | Finding | Weight |
|---|---|---|
| Posting freshness | Live JD page, active "Apply Now" reaching a working Greenhouse form | Positive |
| Description quality | Specific technical detail (C++20/23, lock-free structures, profiling tools named), explicit requirements, explicitly states finance experience isn't required | Positive |
| Salary transparency | Legally disclosed minimum base ($145,000) + explicit bonus/benefits mention — more detailed than #159's disclosure | Positive |
| Company hiring signals | Same as #159 — historical Glassdoor layoff review (undated, department unclear), no 2026-specific layoff/freeze news found | Neutral |
| Reposting pattern | `scan-history.tsv` shows a generically-titled "Software Engineer - C++" req at Akuna (`gh_jid=7496397`) scanned 2026-07-05 — likely the same evergreen entry-level C++ opening reissued under this new req ID (`8013085`) nine days later, or a closely related opening | Neutral — mild repost signal, not concerning on its own for an entry-level "recruiting season" pipeline role |
| Role market context | Entry-level new-grad req tied to the same named "recruiting season" as #159 | Positive |

**Context notes:** Same recruiting cycle and company context as #159. The repost/reissue signal is consistent with an evergreen entry-level pipeline role rather than a ghost posting — Akuna is actively running several parallel entry-level SWE reqs (Python, C++, Data Engineering, Crypto, Platform, Systems) from the same 2026-07-05 scan batch.

**Employment classification signal (US):** No contractor/1099/services-status language found. No flag.

**Buzzword/infrastructure mismatch signal:** No AI/transformation buzzword pattern present. No flag.

---

## Cover Letter Draft

> Draft generated at evaluation time. Complete via `/career-ops cover 160-akuna-capital-2026-07-14` to fill in angles, confirm research, and generate the PDF.
> **Before completing this draft, resolve the #159/#160 top-preference conflict flagged above — only draft and send a cover letter for the req you actually decide to pursue.**

---

**Opening** *(placeholder — refine with your "why this role" angle)*
Akuna's Entry-Level C++ Software Engineer role is squarely the kind of systems problem I look for: multithreaded, asynchronous, distributed systems where correctness under concurrency is the whole job. I've shipped exactly this class of problem to production at Chrome scale.

**Profile introduction**
I'm a Computer Science student at Georgia State University (GPA 3.75, expected May 2027) with production C++ experience at Chrome scale and distributed-systems ownership as the primary engineer on a 3-person team at TiMoto AI. My work centers on the same problem Akuna's C++ engineers face daily: keeping concurrent, high-throughput systems correct and fast.

**Key achievements** *(selected from cv.md — exact wording preserved)*
- **Shipped a C++ IPC transport layer** to Chrome's stable channel — serving 3B+ active users at sub-50ms p99 and 10K+ req/sec — by choosing Protocol Buffers over custom serialization for schema evolution and cross-language compatibility.
- **96% p99 latency cut** (1,200ms down to sub-50ms), zero production regressions, by replacing a mutex-contended search path with a lock-free concurrent trie.
- **Restored 100% evaluation success rate at sub-50ms p99** by resolving a production gRPC deadlock — replaced inconsistent lock-acquisition ordering under concurrent calls with a single enforced sequencing rule.
- **Prevented single-zone failures from taking production down**, sustaining 99.9% uptime and cutting infrastructure cost 44%, by architecting a multi-AZ ECS Fargate deployment with an auto-rollback circuit breaker pattern.

**Problems I will solve** *(placeholder — requires company research + your input)*
> To be completed: which systems area draws you most — algorithms/data structures, concurrency, networking, performance tuning, or hardware? What would you want to fix or build first?

**Closing**
I am happy to discuss further at your convenience.

---

**Gaps flagged:**
- C++ standard version (C++20/23) isn't stated in cv.md — don't assert it in writing; confirm directly if asked.
- Debugging tools (GDB, Valgrind, ASan) have no CV evidence either way — same rule, don't invent.
- Onsite-only in Chicago — no remote/hybrid option.
- **Top-preference conflict with report #159** — resolve which Akuna req to actually pursue before sending anything.

**JD keywords to mirror** *(extracted for ATS + human read)*
C++20, C++23, distributed systems, parallel processing, asynchronous architectures, networking, protocol encoding, decoding, lock-free data structures, performance profiling, GDB, Valgrind, address sanitizer, Quant, Trading, Chicago, entry-level, new grad, STEM OPT, H-1B, Illinois Equal Pay Act

---
*Run `/career-ops cover 160-akuna-capital-2026-07-14` to complete angles, confirm company research, and generate the PDF.*

## H) Draft Application Answers

**Form structure note:** Akuna's Greenhouse form for this req is almost entirely structured fields (dropdowns for university, GPA band, graduation month/year, work-authorization status, yes/no acknowledgments) rather than open-ended "why this role" essay prompts. There is no free-text motivation/cover-letter field on the form itself — the cover letter draft above is for a separate attachment or the recruiter-facing email, not a form field.

Draftable free-text fields found on the form, with guidance (not fabricated specifics — factual fields like phone, GPA, and graduation date must come from the candidate directly):

| Field | Draft guidance |
|---|---|
| "What is your legal first name?" | Candidate's own legal first name — direct input, not drafted |
| "Do you have a preferred name...?" | Candidate's own answer — direct input |
| "Please confirm the Chicago office expectation works for you." (dropdown) | Answer honestly based on the candidate's actual relocation decision — see the onsite/Chicago gap noted in Block B |
| "How did you hear about this job?" | "Job board / aggregator" (per the `utm_source=jobright` origin of the shared link) — confirm with candidate |
| "If you have prior options market making firm experience, please list the firm and position held" | N/A — no such experience per cv.md |
| "Please provide additional detail about your sponsorship needs..." | Suggested honest text: "F-1 student on OPT/STEM OPT; will require H-1B sponsorship for long-term employment following OPT/STEM OPT authorization." — candidate should confirm before submitting |
| Phonetic name pronunciation | Candidate's own input — not drafted |

No essay-style "why this role" / "why Akuna" field exists on this form to draft further; the cover-letter content above covers that angle for use elsewhere (recruiter email, LinkedIn message, or an optional attachment).

## Keywords extracted

C++20, C++23, distributed systems, parallel processing, asynchronous architectures, networking, protocol encoding/decoding, lock-free data structures and algorithms, performance profiling, perf, gprof, vtune, GDB, Valgrind, address sanitizer, Quant, Trading stakeholders, Chicago, entry-level, new grad, STEM OPT, H-1B, Illinois Equal Pay Act, discretionary performance bonus, top preference acknowledgment
