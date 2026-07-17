# Evaluation: Abridge — Software Engineer, Early Career

**Date:** 2026-07-15
**URL:** https://jobs.ashbyhq.com/abridge/7d6ae2be-cd53-466c-8151-2dae2e87aace
**Via:** — (direct)
**Archetype:** AI/ML Infrastructure Engineer / Agentic — primary hit
**Score:** 4.4/5
**Legitimacy:** High Confidence
**PDF:** output/168-abridge-harry-nguyen-2026-07-15.pdf

---

## Machine Summary

```yaml
company: "Abridge"
role: "Software Engineer, Early Career"
date: 2026-07-15
score: 4.4
status: Evaluated
legitimacy_tier: "High Confidence"
archetype: "AI/ML Infrastructure Engineer / Agentic (primary)"
level: "Early-career, new-grad friendly ('degree or equivalent experience')"
location: "SF Office or NYC Office — onsite 5 days/week (explicit in JD)"
advertised_comp: "$157K - $184K"
comp_note: "Base only; Levels.fyi Abridge SWE median TC ~$251K-$320K across levels — this band reads as the early-career tier of a much higher-paying ladder."
visa_risk: "low-medium — active H-1B sponsor (1 LCA approved FY2025, historically 2 in FY2022-2024), clean DOL compliance record; smaller volume than big tech but real"
final_decision: "Apply — strong priority"
hard_stops: []
soft_gaps:
  - "Onsite 5 days/week in SF or NYC — relocation required from Atlanta, no remote/hybrid option stated"
  - "Healthcare/clinical domain is new; JD explicitly does not require it"
  - "No production RAG/agentic-orchestration shipped yet (TiMoto uses vLLM serving, not agent orchestration) — JD explicitly welcomes coursework/personal-project-level GenAI experience"
top_strengths:
  - "TiMoto vLLM/PagedAttention production serving work is a rare, direct match to 'contribute to monitoring and observability systems that keep LLM workflows healthy in production'"
  - "AI Dev Tools usage (Claude Code, Copilot, Codex, Cursor) directly matches 'AI tooling is already part of how you work'"
  - "Well-funded, real company: $5.3B valuation, $778M raised, Series E extension April 2026"
```

---

## A) Role Summary

| Field | Details |
|-------|---------|
| **Archetype** | AI/ML Infrastructure Engineer / Agentic (primary) |
| **Domain** | Healthcare AI — ambient clinical documentation, LLM-powered structured notes from patient-clinician conversations |
| **Function** | Build (agentic LLM systems, retrieval pipelines, evaluation frameworks, backend/frontend) |
| **Seniority** | Early career — "degree in CS or related field, or equivalent experience" |
| **Remote** | Onsite 5 days/week, SF (Mission District) or NYC (SoHo) — explicitly stated twice in the JD |
| **Team size** | Not specified; cross-functional (researchers, clinicians, engineers) |
| **Culture screen** | Pass (qualitative) — "extreme ownership," "unusual amount of responsibility and autonomy," fast-paced startup with real product-market traction (millions of conversations processed monthly) |
| **TL;DR** | Early-career agentic-LLM engineer role at a $5.3B-valuation healthcare AI startup, $157K-$184K base, onsite SF/NYC, direct match to Harry's ML infra and AI-tooling profile. |

**Geo-mismatch check:** location field lists SF/NYC offices with Location Type "On-site"; JD body confirms "onsite 5 days a week in either our NYC or SF offices." No contradiction — consistent, explicit onsite requirement.

## B) Match with CV

| JD Requirement | Match | Evidence from cv.md |
|----------------|-------|---------------------|
| Degree in CS or equivalent experience | ✅ | BS CS, Georgia State, Expected May 2027, GPA 3.75 |
| Hands-on GenAI experience (LLM API, RAG, agents) | ✅ Strong | TiMoto: production vLLM/PagedAttention LLM serving; LLM-as-a-judge evaluation pipelines (per profile.yml superpowers) |
| LLM orchestration concepts (prompt chaining, tool use, retrieval) | ✅ | LangChain listed in skills; vLLM serving experience is adjacent infra knowledge |
| AI tooling already part of how you work | ✅ Strong | Daily use of Claude Code, GitHub Copilot, Codex, Cursor — exact match to the JD's own framing |
| Monitoring/observability for LLM workflows in production | ✅ Strong | TiMoto: built observability stack from zero (Prometheus, Grafana, CloudWatch) specifically across "the gRPC and ML serving layers" |
| Backend and frontend contribution | ✅ | TiMoto Django backend; Chromium TypeScript/React frontend work |
| Collaborative, low-ego, move-fast mindset | ✅ | Primary engineer on 3-person TiMoto team; Chrome cross-team design doc reviews |
| Curiosity about model evaluation and failure modes | ✅ | TiMoto gRPC deadlock root-cause work; profile.yml lists LLM-as-a-judge evaluation as a superpower |

### Gaps

| Gap | Severity | Mitigation |
|-----|----------|-----------|
| Onsite 5 days/week, SF or NYC | Real constraint | Profile states open to relocation for strong roles; this qualifies. No remote fallback exists — must relocate if hired |
| Healthcare/clinical domain | None (JD explicitly doesn't require it) | Do not overclaim domain knowledge; frame as eager to learn, consistent with JD's own "curiosity" framing |
| Agentic orchestration in production (vs. LLM serving) | Soft | TiMoto's vLLM work is serving infrastructure, not agent orchestration specifically — be honest about this distinction in interviews; JD explicitly accepts coursework/project-level GenAI experience, which lowers the bar |

### Visa Note (F-1)

Abridge is confirmed active H-1B sponsor with a clean DOL compliance record (not a willful violator) — 1 LCA approved FY2025, 2 filed FY2022-2024 ([MyVisaJobs](https://www.myvisajobs.com/employer/abridge-ai/), [H1BGrader](https://h1bgrader.com/h1b-sponsors/abridge-ai-inc-g101xj9vk7)). Volume is modest (small company, not a high-volume filer like big tech), but the sponsorship pathway is real and demonstrated. Standard early clarification with the recruiter is still worthwhile.

## C) Level and Strategy

- **Level:** Early-career — JD explicitly says "degree or equivalent experience," "coursework, personal projects, internships, or hackathons" count as qualifying GenAI experience. Harry's actual production LLM-serving experience (TiMoto) significantly exceeds the stated bar.
- **Sell without lying:** Lead with the observability/monitoring bullet — it is a near-verbatim match to "contribute to monitoring and observability systems that keep our LLM workflows healthy in production." Second: vLLM/PagedAttention production serving (most early-career applicants will only have API-calling experience, not memory-management-level LLM infra work). Third: daily AI-tool fluency, which the JD treats as a first-class qualification, not a footnote.
- **Differentiator:** most early-career GenAI applicants have built a RAG demo; Harry has run production LLM serving infrastructure with real uptime and cost constraints. That is a materially deeper level of "dependable clinical systems" thinking than the typical applicant pool.

## D) Comp and Demand

**Company type:** Growth-stage VC-backed startup — confidence high ($5.3B valuation, $778M raised, a16z-led Series E). **Comp reliability: High** — explicit tiered base band stated directly in the posting.

| Source | Figure | Notes |
|--------|--------|-------|
| Advertised (JD) | $157,000 - $184,000 | JD — base only, geographic-tier structure |
| Levels.fyi Abridge SWE (all levels) | Median TC ~$251K-$320K | [levels.fyi](https://www.levels.fyi/companies/abridge/salaries/software-engineer) — this posting's band is consistent with the early-career rung of that ladder |
| Funding | $778M raised; $5.3B valuation (Series E, Jun 2025) + $316M extension (Apr 2026) | [Sacra](https://sacra.com/c/abridge/) |

- **Likely guaranteed base:** $157K-$184K — $17K-$44K above the $140K walk-away, within the $150-200K target range.
- **Variable:** equity grants explicitly mentioned ("Compensation and Equity" benefit line) — meaningful upside potential given the fast-rising valuation trajectory, though speculative like all startup equity.
- **Expected stable cash:** base as stated; equity value highly dependent on future outcome.
- **Non-cash:** comprehensive medical/dental/vision, HSA contributions, 401(k) match, lifestyle wallet, personal device allowance, paid sabbatical after 5 years, mental health support.

**HR verification questions:**
1. What is the current 409A valuation used for equity grants, and what is the standard vesting schedule?
2. Does the company offer any relocation assistance for candidates moving to SF or NYC?
3. Is there flexibility on 5-day onsite after an initial ramp period, or is this a firm long-term policy?
4. Which office (SF vs NYC) has open headcount for this specific req?

**Demand trend:** Healthcare AI is one of the hottest-funded verticals right now; Abridge's rapid valuation growth ($2.75B → $5.3B in months) signals strong revenue growth and likely continued hiring. Early-career GenAI-specific roles (vs. generic SWE) remain relatively scarce — most GenAI postings target senior/staff levels.

## E) Customization Plan

| # | Section | Change | Why |
|---|---------|--------|-----|
| 1 | TiMoto bullets | vLLM/PagedAttention bullet promoted to #1 or #2 | Direct match to "GenAI experience" + "LLM workflows in production" |
| 2 | TiMoto bullets | Observability stack bullet stays prominent | Near-verbatim match to "monitoring and observability systems... LLM workflows healthy in production" |
| 3 | Skills | AI Dev Tools row — consider noting it's daily-workflow, not just listed tools | JD explicitly values "AI tooling is already part of how you work" |
| 4 | Skills | LangChain, PyTorch stay visible in ML & AI Infrastructure row | JD mentions LangChain/LlamaIndex-style orchestration tools by name |
| 5 | Summary/positioning | Frame TiMoto as "production ML serving," not just "backend" | Aligns with "dependable clinical systems" language |

## F) Interview Plan

| # | JD Requirement | STAR+R Story | Reflection |
|---|----------------|--------------|------------|
| 1 | LLM workflows in production, monitoring/observability | TiMoto: built observability stack from zero (Prometheus/Grafana/CloudWatch) across gRPC + ML serving layers, <15min RCA | Production LLM systems fail silently until you build the tooling to see them fail |
| 2 | GenAI experience (RAG, agents, LLM APIs) | TiMoto vLLM/PagedAttention: solved KV cache memory fragmentation, eliminated OOM under concurrent load | Serving infra is where GenAI theory meets real constraints — memory, concurrency, cost |
| 3 | Evaluation frameworks, model failure modes | TiMoto gRPC deadlock root-cause: circular lock acquisition under concurrent calls | Reliability work is detective work before it's engineering work |
| 4 | Backend + frontend contribution | TiMoto Django backend; Chromium TypeScript/React (25K+ lines, 95% coverage) | Full-stack fluency means you can trace a bug from UI to database without a handoff |
| 5 | AI tooling fluency | Daily Claude Code/Copilot/Codex/Cursor workflow used to build and ship TiMoto and this very application | Knowing when to trust AI output vs. verify is itself a skill, not a given |
| 6 | Collaborative, low-ego, move-fast | Primary engineer role on 3-person TiMoto team; Chrome cross-team design doc reviews | Small teams only move fast when everyone can review everyone's work without ego |
| 7 | Curiosity about failure modes | Lock-free trie: root-caused mutex contention via profiling before touching code | Always profile before you optimize — the fix falls out of the diagnosis |

**Case study:** TiMoto walkthrough (timoto.ai) — the LLM-serving-in-production story is the strongest possible match for this specific role.
**Red-flag question prep:** "Why healthcare?" → honest: drawn to AI systems where reliability has real stakes, not primarily domain expertise; TiMoto's production discipline (SLOs, cost targets, uptime) is the transferable skill, and the mission (deeper understanding, patient care) genuinely resonates.

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting freshness | Full Ashby posting, Apply button active, detailed content | Positive |
| Description quality | Specific responsibilities, specific tech (LangChain, LlamaIndex), specific onsite policy stated twice, benefits detailed | Positive |
| Salary transparency | $157K-$184K explicit tiered band | Positive |
| Company hiring signals | No layoff signals found; actively raising capital (Series E extension April 2026) — strong growth signal | Positive |
| Reposting pattern | Not previously in scan-history.tsv | Neutral |
| Fraud warning present | JD includes an explicit "Staying safe - Protect yourself from recruitment fraud" section — a maturity signal, not a concern about this posting itself | Positive |
| Employment classification | Standard full-time employee posting with full benefits | Positive |

Real posting at a well-funded, fast-growing healthcare AI company. No ghost signals.

---

## Cover Letter Draft

> Draft generated at evaluation time. Complete via `/career-ops cover abridge-early-career`.

---

**Opening** *(placeholder — refine with your "why this role" angle)*
Abridge is shipping agentic LLM systems into real clinical workflows where reliability isn't optional. That is exactly the discipline I have been building at TiMoto: production LLM serving with real uptime and cost constraints, not a demo.

**Profile introduction**
I am a CS student at Georgia State University (GPA 3.75, May 2027) working as a Software Engineer at TiMoto AI, where I am the primary engineer for backend, cloud infrastructure, and ML serving on a three-person team. I interned on Google Chrome, shipping production C++ and TypeScript/React to the stable channel.

**Key achievements** *(from cv.md — exact wording preserved)*
- **Eliminated OOM failures** under concurrent production load by replacing naive batching with a vLLM/PagedAttention inference engine, solving KV cache memory fragmentation for LLM serving.
- **Cut incident root-cause time to under 15 minutes** by building TiMoto's observability stack from zero across the gRPC and ML serving layers (Prometheus, Grafana, CloudWatch).
- **Restored 100% evaluation success rate** at sub-50ms p99 by resolving a production gRPC deadlock under concurrent calls.
- **Built an event-driven TypeScript/React system** across 25K+ lines of Chromium at 95% test coverage.

**Problems I will solve** *(placeholder — requires company research + your input)*
> To be completed: which part of Abridge's clinical documentation pipeline interests you most (evaluation frameworks, agentic retrieval, EMR integration).

**Closing**
I am happy to discuss further at your convenience.

---

**Gaps flagged:** Onsite 5 days/week in SF or NYC requires relocation from Atlanta (profile states open to relocation for strong roles — this qualifies); healthcare domain is new but explicitly not required by the JD.

**JD keywords to mirror:** agentic LLM systems; retrieval pipelines; structured tool use; chained LLM workflows; evaluation frameworks; clinical reliability; human-in-the-loop; monitoring and observability; LLM orchestration; GenAI experience; AI tooling.

---

## Keywords extracted

agentic LLM systems, retrieval pipelines, RAG, structured tool use, chained LLM workflows, evaluation frameworks, human-in-the-loop, LLM orchestration, prompt chaining, tool use, LangChain, LlamaIndex, monitoring, observability, GenAI, production code, backend, frontend, healthcare AI, clinical systems
