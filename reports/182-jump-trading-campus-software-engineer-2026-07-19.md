# Evaluation: Jump Trading — Campus Software Engineer (Full-Time)

**Date:** 2026-07-19
**URL:** https://www.jumptrading.com/hr/job?gh_jid=8000835
**Via:** —
**Archetype:** Systems Software Engineer + Backend / Distributed Systems Engineer
**Score:** 4.5/5
**Legitimacy:** High Confidence
**PDF:** output/182-jump-trading-harry-nguyen-2026-07-19.pdf

---

## Machine Summary

```yaml
company: "Jump Trading"
role: "Campus Software Engineer (Full-Time)"
score: 4.5
legitimacy_tier: "High Confidence"
archetype: "Systems Software Engineer + Backend / Distributed Systems Engineer"
final_decision: "Apply"
hard_stops: []
soft_gaps:
  - "Expected-graduation-date field is a dropdown, not yet confirmed May 2027 is a selectable option (unconfirmed at browse time)"
  - "'Reliable and predictable availability' phrasing plus $250K flat comp signal a high-intensity HFT culture -- worth going in with eyes open"
  - "Onsite Chicago -- requires relocation from Atlanta"
top_strengths:
  - "Lock-free concurrent trie at Google Chrome is a near-verbatim match to 'data structures and threading models' plus the 'build from scratch, not assemble from libraries' ethos this JD explicitly asks for"
  - "C++ and Python on Linux are both named requirements and both are on Harry's CV"
  - "Explicit visa sponsorship for full-time roles, CPT/OPT-eligible, 'no finance or economics required' -- removes the two most common blockers for this candidate profile"
  - "$250,000 flat base is the highest single-figure comp seen in the pipeline to date, well above target range"
risk_level: "Low"
confidence: "High"
next_action: "Apply -- confirm the expected-graduation-date dropdown accepts May 2027 during the application; be ready to discuss availability/hours expectations if raised"
discard_reasons: []
via: null
company_confidential: false
advertised_comp: "$250,000 per year (estimated base salary)"
risk_summary:
  legitimacy: "high_confidence"
  classification: "clear"
  culture: "not_evaluated"
  interview_redflags: "not_evaluated"
  ai_infra: "not_evaluated"
```

## A) Role Summary

| Field | Value |
|---|---|
| Archetype detected | Systems Software Engineer (primary) + Backend / Distributed Systems Engineer (primary) |
| Domain | Proprietary trading technology — core trading engine, custom hardware, distributed trading systems |
| Function | Build (design, code, test, maintain the distributed trading system and supporting infrastructure) |
| Seniority | Campus / new grad — "new graduate hires work alongside experienced engineers"; page metadata tags this "Intern" but the title and body both describe a full-time new-grad role, and the application form's sponsorship/graduation-date questions confirm it's a post-graduation hire |
| Remote | Onsite — Chicago; no remote/hybrid language anywhere in the JD |
| Team size | Not stated — "Core Development is a global team," specific team assignment happens across market data / order entry / risk management / simulation / UI development groups |
| Culture screen | Not evaluated — no `culture_screen.require` configured in `config/profile.yml`; scored qualitatively in Block D instead |
| TL;DR | Elite systems-engineering new-grad role at a major HFT firm — near-perfect C++/Linux/lock-free-structures fit, explicit visa sponsorship, and the highest flat comp figure seen in the pipeline so far. |

No geo-mismatch: the JD names no remote option anywhere in the body to contradict the Chicago onsite location field.

**Note on the "Intern" job-type tag:** the page's structured metadata labels this posting "Intern" while the title says "(Full-Time)" and the body explicitly describes "new graduate hires" learning "advanced skills" alongside experienced engineers, plus a $250,000 base salary figure that would be unusual for a true internship. This reads as a Greenhouse job-family mislabeling (campus/new-grad roles sometimes share a job-family taxonomy with internships), not a substantive signal about the role itself — the JD content is unambiguous that this is a full-time new-grad hire.

## B) Match with CV

| JD Requirement | CV Evidence |
|---|---|
| "C++ development on Linux platform" | CV Skills: "C++" listed first under Languages; Google Chrome: production C++ IPC transport layer shipped to Chrome's stable channel |
| "Python development on Linux platform" | CV Skills: Python; TiMoto: Python-based vLLM/PagedAttention serving layer |
| "Strong understanding of data structures and threading models" | Google Chrome: "replacing a mutex-contended search path with a lock-free concurrent trie" — a direct, near-verbatim match to both data structures and threading/concurrency |
| "Passion for solving complex problems... building optimal solutions from scratch, instead of simply assembling things from existing libraries" | Google Chrome lock-free trie (built, not assembled) and TiMoto's gRPC deadlock fix (root-caused a concurrency bug, not patched around it) both demonstrate this directly |
| "Interest in using knowledge from several areas -- hardware, networking, OS design -- to produce extremely high-performance software" | Coursework: Operating Systems, Computer Networks; Google Chrome sub-50ms p99 IPC work and 96% latency-cut trie both demonstrate applied OS/networking-adjacent performance work |
| "Ability to work with a team in a fast-paced environment, deploying new software daily" | TiMoto: primary engineer on a 3-person team shipping to production; Google Chrome: changes reviewed and adopted by senior engineers into Chrome's live codebase |
| "Distributed trading system" (implicit: distributed systems fluency) | TiMoto: gRPC inter-service deadlock fix, multi-AZ ECS Fargate deployment — direct distributed-systems production experience |
| "No finance or economics study or work experience required" | Not applicable — explicitly removes a gap that would otherwise apply |
| "INTERNATIONAL STUDENTS encouraged... sponsor work visas for full-time positions" | Directly resolves Harry's F-1 visa consideration — one of the strongest sponsorship statements seen in the pipeline |

**Gaps:**

1. **No prior HFT/trading-specific domain exposure.** The JD explicitly says this isn't required ("No finance or economics study or work experience required"), so this is a non-issue by the posting's own terms — no mitigation needed beyond noting genuine interest in the domain if asked.
2. **Linux-specific tooling depth is implicit, not explicit, on the CV.** TiMoto and Chrome are both almost certainly Linux-based (AWS ECS Fargate, Chromium build systems), but "Linux platform" isn't spelled out as a named skill. Mitigation: safe to state directly in a cover letter or interview — the underlying infrastructure (AWS, Docker, ECS Fargate) is Linux-based by default, this is not a stretch claim.
3. **"Reliable and predictable availability"** — a phrase worth taking at face value as signaling on-call or demanding-hours expectations typical of HFT technology teams. Not a CV gap, but worth going into the process aware of, and asking about directly during interviews.

## C) Level and Strategy

1. **Level detected:** Entry / campus new-grad — matches Harry's actual level directly, with "new graduate hires work alongside experienced engineers" confirming a mentorship structure rather than an expectation of senior-level autonomy.
2. **Sell senior without lying:** Lead with the lock-free trie story — it is the single strongest available proof point for "building optimal solutions from scratch," which is the JD's own stated hiring bar, and it demonstrates production-grade concurrency work at a scale (3B+ users) most new-grad candidates cannot show.
3. **If downleveled:** N/A — this is already the entry tier, no lower level exists to negotiate into. Given the advertised base is flat ($250,000, not a range), there's limited room to negotiate base itself; any negotiation would likely focus on sign-on or start date instead.

## D) Comp and Demand

**Company type:** Mature, established proprietary trading firm (privately held) — Confidence: High. Jump Trading is a decades-old, large-scale HFT/quant firm, not an early-stage or growth-stage company; despite being privately held (not stock-market public), it has a long, consistent track record of flat, transparent new-grad compensation figures, consistent with peer firms already evaluated in this pipeline.

**Compensation reliability:** High — the JD states a specific, single base figure directly ("The estimated base salary for this role is $250,000 per year"), and this figure is strongly corroborated by comparable flat-rate new-grad offers at peer HFT firms already evaluated: Five Rings ($300,000 flat, report #167), Optiver ($200,000 flat, report #176), Old Mission ($175-200,000, report #164).

| Component | Value | Source |
|---|---|---|
| Advertised (JD) | $250,000 per year (estimated base salary) | JD |
| Likely guaranteed base | $250,000, stated directly and specifically (not a range) | JD |
| Variable / conditional cash | Not stated — HFT firms in this pipeline typically add discretionary bonus on top of base (see Old Mission #164), but none is named here | — |
| Non-cash benefits | Private medical/vision/dental, travel medical insurance, group pension scheme, group life assurance and income protection, paid parental leave, parking/commuter benefits | JD "Benefits include" |
| Peer comparable — HFT new-grad flat base, this pipeline | Five Rings $300K, Optiver $200K, Old Mission $175-200K | Reports #167, #176, #164 |

This is the second-highest flat new-grad base figure seen across all evaluated HFT firms in this pipeline (only Five Rings' $300K is higher), and it sits well above Harry's $150-200K target range on its own, before any bonus.

**Demand trend:** Positive. Jump Trading currently has more open Information Technology roles than at any point in the past 12 months, with no confirmed 2026 layoffs or hiring-freeze signals found. One Glassdoor review title references "downsizing" as a caveat to an otherwise positive review, but this is a single, dated, unverified data point against a much stronger active-hiring signal — treated as a minor, unconfirmed caution rather than a material risk.

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---|---|---|---|
| 1 | Google Chrome bullet order | Lock-free trie bullet is second | Lead with the lock-free concurrent trie bullet | This is the single most directly relevant proof point — "data structures and threading models," built from scratch, not assembled |
| 2 | TiMoto bullet order | Observability-first (from recent tailoring) | Lead with the gRPC deadlock fix bullet | Directly demonstrates distributed-systems concurrency debugging, the JD's core domain |
| 3 | Skills section | Languages row already lists C++ first | No change needed | JD's top two named languages (C++, Python) are already the CV's lead languages |
| 4 | Summary/headline | Backend/systems generalist framing | Emphasize "systems performance + concurrency" framing for this application | JD rewards raw systems/performance depth over breadth |
| 5 | Cover letter | N/A | Note genuine interest in high-performance computing / low-latency systems, without overclaiming finance-domain knowledge | JD explicitly removes the finance-background requirement — no need to manufacture domain interest that isn't genuine |

## F) Interview Plan

| # | JD Requirement | STAR+R Story | Best for |
|---|---|---|---|
| 1 | "Strong understanding of data structures and threading models" | Lock-Free Trie at Google Chrome (story bank) | Concurrency, data structures, performance optimization |
| 2 | "Distributed trading system" / concurrency at scale | gRPC Deadlock Fix at TiMoto (story bank) | Distributed systems, concurrency debugging, root-cause analysis |
| 3 | "Building optimal solutions from scratch, instead of simply assembling things from existing libraries" | vLLM Serving Architecture at TiMoto (story bank) | Build-vs-buy tradeoff reasoning, architecture decisions |
| 4 | "Ability to work with a team... deploying new software daily" | Design Doc Review at Google Chrome (story bank) | Collaboration, code review culture, working with senior engineers |
| 5 | "Using knowledge from several areas -- hardware, networking, OS design" | Multi-AZ Circuit Breaker at TiMoto (story bank) | Infrastructure, systems design, cross-domain reasoning |
| 6 | "Passion for solving complex problems" | N+1 Fix at Develop for Good (story bank) | Debugging, systematic problem-solving |

All six stories already exist in `interview-prep/story-bank.md` — no new stories needed for this evaluation.

**Recommended case study:** The lock-free concurrent trie at Google Chrome — it's the closest possible match to this JD's specific technical bar (data structures, threading, "build from scratch"), demonstrated at a scale (3B+ users, 96% latency cut) that's rare for a new-grad candidate.

**Red-flag questions and how to answer them:**
- *"Do you have any trading or finance background?"* → The JD itself says this isn't required — answer honestly ("no direct finance background, and I understand it's not required"), then pivot immediately to the systems/performance work that is directly relevant.
- *"This role expects reliable, predictable availability — how do you think about work-life balance in a fast-paced trading environment?"* → Be honest and direct rather than over-promising; ask a clarifying question back about what "predictable availability" concretely means day-to-day (on-call rotation? market-hours coverage? no explicit statement in the JD to assume from).
- *"Why systems/infrastructure work at a trading firm specifically, rather than at a general tech company?"* → Anchor on the genuine technical draw: extremely high-performance, correctness-critical software at massive scale, which is exactly the throughline across the Chrome and TiMoto stories.

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Posting freshness | "Apply" button resolves to a live, fully functional application form (Greenhouse-embedded); real reCAPTCHA, real form fields | Positive |
| Description quality | Names a specific team ("Core Development"), specific technologies (C++, Python, Linux), specific sub-teams (market data, order entry, risk management, simulation, UI development), and a specific, single-figure salary — well above boilerplate | Positive |
| Requirements realism | Entry-level, realistic bar ("hands-on experience... in one or more of" C++ or Python, no finance background required) with no internal contradictions | Positive |
| Salary transparency | Explicit, specific base salary figure disclosed ($250,000/year) — more precise than most postings, which give a range | Positive |
| Company hiring signals | Jump Trading currently has more open IT roles than at any point in the past 12 months; no confirmed 2026 layoffs found. One dated, unverified Glassdoor review title mentions "downsizing" as a caveat — noted but not corroborated elsewhere. | Positive |
| Reposting pattern | `data/scan-history.tsv` shows only the general Jump Trading students/new-grads landing page scanned previously (2026-07-05), not this specific req — no reposting history to evaluate for this exact posting | Neutral |
| Role market context | Elite HFT firms commonly run standing, rolling campus pipelines rather than single fixed openings; nothing here suggests an outlier | Neutral |

**Context notes:** The "Intern" job-type tag in the page's structured metadata is a Greenhouse job-family classification quirk, not a legitimacy concern — the JD body text is unambiguous that this is a full-time new-grad hire with a $250,000 base salary.

**6. Employment Classification:** Not flagged — standard full-time employment posting with comprehensive benefits language (medical/dental/vision, pension, parental leave), no contractor-status wording.

**7. AI-Buzzword vs. Infrastructure Mismatch:** Not flagged — the JD is a concrete systems/infrastructure role with no AI/transformation buzzword framing at all; not applicable.

**8. Benefits/Employment Terminology Country Mismatch:** Not flagged — role is listed in Chicago, US, and while some benefit terms ("Group Pension Scheme," "Group Life Assurance") read as UK-influenced phrasing (Jump Trading has a London hub), no US-exclusive marker ("401(k)," "W-2") appears alongside a conflicting jurisdiction claim, so the corroborating-marker threshold for this signal is not met. This likely reflects a firm-wide benefits template shared across Jump's global offices rather than a location error.

## Risk Summary

| Signal | Status |
|--------|--------|
| Posting legitimacy | ✅ High Confidence — live application flow, specific team/tech/salary, active expansion hiring signal |
| Employment classification | ✅ clear — standard full-time employment posting with comprehensive benefits |
| Culture screen | — not evaluated (no `culture_screen.require` configured in `config/profile.yml`) |
| Interview red flags | — no interview sessions yet |
| AI claims vs. infrastructure | — not evaluated (role has no AI-related claims to check) |

---

## H) Draft Application Answers

Score is 4.5/5 (≥4.5 threshold) — draft answers generated for the application form fields observed during the live snapshot.

**Why are you interested in this role? / Why Jump Trading?**
> I want to work on software where correctness under concurrency isn't optional — it's the whole job. At Google Chrome, I replaced a mutex-contended settings-search path with a lock-free concurrent trie and had to prove linearizability before it shipped to 3 billion users. Jump's Core Development team is solving that same class of problem at a scale and speed I haven't gotten to work at yet, and I want to build the discipline to do it well.

**Tell us about a relevant project or achievement**
> I resolved a production deadlock in TiMoto's gRPC inter-service layer by tracing a circular lock-acquisition dependency under concurrent calls and redesigning the sequencing to enforce a single consistent order — restoring 100% evaluation success at sub-50ms p99 with zero recurrence. Before that, at Google, I replaced a mutex-contended trie with a lock-free structure that cut Chrome settings-search latency 96% with zero production regressions.

**What makes you a good fit for this position?**
> The JD's own bar — building optimal solutions from scratch instead of assembling from libraries — is exactly how I've approached both of my hardest technical problems: I didn't patch around the gRPC deadlock, I redesigned the locking model; I didn't reach for an existing concurrent-data-structure library at Chrome, I built and proved correctness on a lock-free trie myself.

**Non-compete/Notice period comments**
> No active non-compete agreements. Available to start per Jump's standard new-grad timeline (targeting May 2027 graduation) — happy to confirm exact availability during the process.

**How did you hear about us?**
> Sourced directly from Jump Trading's careers site.

---

## Cover Letter Draft

> Draft generated at evaluation time. Complete via `/career-ops cover 182-jump-trading` to fill in angles, confirm research, and generate the PDF.
> Gaps flagged below — address them during the cover flow.

---

**Opening** *(placeholder — refine with your "why this role" angle)*
Jump's Core Development team builds software where correctness under concurrency isn't a nice-to-have — it's the entire job. That's the exact problem space I want to work in, and the one I've already spent the last year solving in production.

**Profile introduction**
I'm a Computer Science student at Georgia State (May 2027) currently the primary engineer for backend, cloud infrastructure, and ML serving at TiMoto AI, where I own a distributed production system end-to-end on a 3-person team. Before that, I shipped a lock-free concurrent data structure into Chrome's stable channel as a Google engineering intern, serving 3 billion users.

**Key achievements** *(selected from cv.md — exact wording preserved)*
- **Lock-free concurrent trie at Google Chrome,** cutting settings-search p99 latency 96% for power users, zero production regressions, shipped to Chrome stable.
- **gRPC deadlock fix at TiMoto,** restoring 100% evaluation success rate at sub-50ms p99 by redesigning lock-acquisition ordering under concurrent calls.
- **C++ IPC transport layer at Google Chrome,** serving 3B+ active users at sub-50ms p99 and 10K+ req/sec.
- **Multi-AZ ECS Fargate deployment at TiMoto,** sustaining 99.9% uptime and cutting infrastructure cost 44% via Terraform IaC.

**Problems I will solve** *(placeholder — requires company research + your input)*
> To be completed: which of the technology groups (market data, order entry, risk management, simulation, UI development) are you most drawn to, and why? Any specific Jump Trading engineering blog posts, talks, or open-source work worth referencing?

**Closing**
I am happy to discuss further at your convenience.

---

**Gaps flagged:**
- No prior finance/trading domain exposure — explicitly not required by the JD, no need to over-address.
- "Reliable and predictable availability" phrasing suggests demanding hours typical of HFT — go in with eyes open, ask directly during interviews if concerned.
- Expected-graduation-date dropdown not yet confirmed to include May 2027 — verify during the actual application submission.

**JD keywords to mirror** *(extracted for ATS + human read)*
Campus Software Engineer, C++, Python, Linux, distributed trading system, data structures, threading models, high-performance software, market data, order entry, risk management, simulation, UI development, SDLC, test automation, hardware, networking, OS design

---
*Run `/career-ops cover 182-jump-trading` to complete angles, confirm research, and generate the PDF.*

---

## Keywords extracted

Campus Software Engineer, C++, Python, Linux, distributed trading system, supercomputer, data structures, threading models, concurrency, high-performance software, market data, order entry, risk management, simulation, UI development, SDLC, test automation, hardware, networking, OS design, from-scratch problem solving
