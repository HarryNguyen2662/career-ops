# Evaluation: Giga (GigaML) — Software Engineer I / II

**Date:** 2026-07-20
**URL:** https://jobs.ashbyhq.com/gigaml/96f0c2f8-3d97-4763-ab46-b6af6ad8b2e7
**Via:** —
**Archetype:** Backend / Distributed Systems Engineer + AI/ML Engineer (Inference & Serving)
**Score:** 4.3/5
**Legitimacy:** High Confidence
**PDF:** output/184-gigaml-harry-nguyen-2026-07-20.pdf

---

## Machine Summary

```yaml
company: "Giga (GigaML)"
role: "Software Engineer I / II"
score: 4.3
legitimacy_tier: "High Confidence"
archetype: "Backend / Distributed Systems Engineer + AI/ML Engineer (Inference & Serving)"
final_decision: "Apply"
hard_stops: []
soft_gaps:
  - "JD asks for '1-3 years of professional software engineering experience' -- TiMoto (~10 months, non-internship) falls short of the stated floor; more explicit than the 'New Grad' framing on Harry's two prior GigaML applications (#15, #59)"
  - "Onsite San Francisco -- requires relocation from Atlanta"
top_strengths:
  - "'Activity Stream: Log visualization with filters, timestamps, and frequency charts' is a near-direct match to TiMoto's Prometheus/Grafana/CloudWatch observability stack"
  - "AI agent infrastructure (Atlas, agent memory, dynamic knowledge) maps directly onto TiMoto's production vLLM/PagedAttention serving experience"
  - "$61M Series A with a named, verifiable paying customer (DoorDash) -- de-risked vs. a typical pre-revenue Series A"
  - "Third distinct GigaML req evaluated (#15, #59, this one) -- consistently high-scoring company for Harry's profile"
risk_level: "Medium"
confidence: "Medium"
next_action: "Apply -- be ready to address the experience-floor question directly (TiMoto is real production ownership even at under a year); no new company-research needed beyond what #59 already established (same $61M Series A, same DoorDash relationship)"
discard_reasons: []
via: null
company_confidential: false
advertised_comp: "$160K - $250K, Offers Equity"
risk_summary:
  legitimacy: "high_confidence"
  classification: "clear"
  culture: "not_evaluated"
  interview_redflags: "not_evaluated"
  ai_infra: "consistent"
```

## A) Role Summary

| Field | Value |
|---|---|
| Archetype detected | Backend / Distributed Systems Engineer (primary) + AI/ML Engineer, Inference & Serving (secondary) |
| Domain | AI agent infrastructure for enterprise customer support/operations (voice, chat, email) |
| Function | Build (backend, data pipelines, integrations, agent infrastructure) |
| Seniority | SWE I/II — the posting explicitly asks for "1-3 years of professional software engineering experience," a step above pure new-grad framing |
| Remote | Onsite — San Francisco |
| Team size | Not stated — small/early-stage engineering team ("brilliant founders," "real responsibility early") |
| Culture screen | Not evaluated — no `culture_screen.require` configured in `config/profile.yml`; scored qualitatively in Block D instead |
| TL;DR | Third distinct GigaML req evaluated for Harry — same strong technical fit as #15/#59, but this specific posting states an explicit 1-3 year experience floor that the earlier "New Grad" reqs didn't, and pays a wider $160-250K band. |

No geo-mismatch: the JD's structured location (San Francisco, On-site) is consistent throughout the body, with no remote claim to contradict it.

**Duplicate check:** distinct from report #15 (`cb74c445-...`, "Software Engineer (New Grads)") and report #59 (`7314c5c1-...`, "Software Engineer (New Grads)," New York) — this req (`96f0c2f8-...`) is a different URL, a different title ("Software Engineer I/II" vs. "New Grads"), a different location (San Francisco vs. New York), and states a different experience bar (1-3 years vs. new-grad framing). Not a duplicate, but the third data point on the same company for Harry.

## B) Match with CV

| JD Requirement | CV Evidence |
|---|---|
| "Backend, from data pipelines and integrations to agent infrastructure" | TiMoto: gRPC inter-service layer, vLLM/PagedAttention serving infrastructure — direct agent-infrastructure-adjacent production experience |
| "Activity Stream: Log visualization with filters, timestamps, and frequency charts to give visibility into agent behavior" | TiMoto: "deployed Prometheus and Grafana metrics alongside CloudWatch dashboards" — nearly the same problem (observability/visibility into a running AI system), just a different specific feature |
| "Agent memory: Conversation awareness and recent interaction lookups so agents remember context across sessions" | TiMoto: production LLM serving experience (vLLM/PagedAttention, KV cache management) — directly relevant systems-level context for building agent memory/session-state features |
| "1-3 years of professional software engineering experience" | TiMoto (Sep 2025-Present, non-internship, ~10 months) + Google Chrome + Develop for Good internships — below the stated floor if internships don't count, though real production ownership |
| "Are curious and ask good questions... want to understand why things work, not just how" | TiMoto gRPC deadlock fix: root-caused via lock-acquisition-order analysis, not a surface patch |
| "Prefer shipping over perfection but still care about quality" | Google Chrome: 95% test coverage cited twice, shipped to Chrome stable — quality discipline; TiMoto: shipped production fixes under real time pressure |
| "Want to grow at a startup where you'll have real responsibility early" | TiMoto: "primary engineer for backend, cloud infra, and ML serving... 3-person team" — already operating with exactly this kind of ownership |

**Gaps:**

1. **Experience floor (1-3 years stated, Harry has ~10 months non-internship).** This is the main gap, and it's more explicit here than on Harry's two prior GigaML applications, which were framed as "New Grad" roles. Mitigation: be direct if asked — TiMoto is real, non-internship production ownership (primary engineer on a 3-person team, not a junior contributor role), and total engineering exposure across TiMoto + two internships is broader than the raw month-count suggests.
2. No other material gaps identified — the technical overlap (observability, AI serving, backend infrastructure) is unusually direct for this specific company across all three evaluated reqs.

## C) Level and Strategy

1. **Level detected:** SWE I/II, entry-to-early-career — the stated 1-3 year band sits just above Harry's current tenure, but the posting explicitly covers both I and II, giving room for a SWE I landing.
2. **Sell senior without lying:** Lead with the "primary engineer, 3-person team, end-to-end ownership" framing from TiMoto — this directly answers "want to grow at a startup where you'll have real responsibility early" by showing Harry already operates that way, not that he's hoping to.
3. **If the experience-floor question becomes a hard filter:** There's limited room to argue the raw number; the stronger move is reframing the conversation around demonstrated ownership and production judgment (the gRPC deadlock fix, the EKS-to-ECS-Fargate migration decision) rather than contesting the month-count directly.

## D) Comp and Demand

**Company type:** Growth-stage / VC-backed startup with paying enterprise customers — Confidence: High. Same company profile established in report #59: $61M Series A (November 2025), with a named, verifiable paying customer (DoorDash, confirmed via both a Fortune article and a LinkedIn partnership post) — a meaningfully de-risked signal compared to a typical pre-revenue Series A.

**Compensation reliability:** High — the JD states an explicit, structured range directly on the posting (Ashby's built-in compensation field, not just prose), consistent with the range already seen on report #59's NYC req.

| Component | Value | Source |
|---|---|---|
| Advertised (JD) | $160,000 - $250,000, Offers Equity | JD |
| Likely guaranteed base | $160K-$250K, as stated | JD |
| Variable / conditional cash | Bonus mentioned in Perks & Benefits ("Competitive base + bonus + equity") but not quantified | JD |
| Non-cash benefits | Equity, catered lunch, dinner stipend, $500/month wellness & commuter benefit, 401(k), medical/dental/vision | JD |
| Prior GigaML comp research (report #59) | Year-1 TC estimate ~$195K-$215K for a comparable NYC new-grad req | Report #59 |

This range sits comfortably above Harry's $150-200K target and well above the $140K walk-away floor at every point in the band — the strongest advertised comp seen across all three GigaML evaluations to date.

**Demand trend:** No 2026 layoff or hiring-freeze signal found for GigaML/Giga specifically (broad 2026 tech-layoff searches surfaced only industry-wide AI-driven layoff coverage at large incumbents — Meta, Amazon, Oracle — not this company). Combined with the confirmed, recent $61M Series A and an active, real customer relationship (DoorDash), this reads as an actively growing company rather than one under funding or headcount pressure.

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---|---|---|---|
| 1 | TiMoto observability bullet | Present, second or third position depending on recent tailoring | Lead with the observability/Prometheus-Grafana-CloudWatch bullet | Near-direct match to the JD's "Activity Stream" log-visualization feature |
| 2 | TiMoto vLLM bullet | Present | Keep in top 3 | Directly relevant to "agent memory" and general AI-agent-infrastructure framing |
| 3 | Skills section | AI Dev Tools / ML & AI Infrastructure rows already list vLLM, PagedAttention, LangChain | No change needed | Already covers the AI-agent-adjacent stack |
| 4 | Summary/headline | Backend/systems generalist framing | Emphasize "backend + AI agent infrastructure" framing for this application | Matches the JD's specific domain more precisely than a generic backend pitch |
| 5 | Cover letter | N/A | Address the experience-floor gap briefly and confidently, framed around ownership rather than tenure | Better to control the narrative on the one real gap than let it surface unaddressed |

## F) Interview Plan

| # | JD Requirement | STAR+R Story | Best for |
|---|---|---|---|
| 1 | "Activity Stream: Log visualization... to give visibility into agent behavior" | Building Observability Stack from Zero at TiMoto (story bank) | Observability, monitoring, visibility tooling |
| 2 | "Agent memory: Conversation awareness and recent interaction lookups" | vLLM Serving Architecture at TiMoto (story bank) | AI/ML infrastructure, session-state/context management |
| 3 | "Curious... want to understand why things work, not just how" | gRPC Deadlock Fix at TiMoto (story bank) | Root-cause analysis, debugging, systems curiosity |
| 4 | "Backend, from data pipelines and integrations to agent infrastructure" | Multi-AZ Circuit Breaker at TiMoto (story bank) | Backend infrastructure, reliability |
| 5 | "Want to grow at a startup where you'll have real responsibility early" | Post-Mortem Culture at TiMoto (story bank) | Ownership, process-building, startup readiness |
| 6 | "Paired with senior engineers on larger initiatives" | Design Doc Review at Google Chrome (story bank) | Collaboration, working with senior engineers |

All six stories already exist in `interview-prep/story-bank.md` — no new stories needed for this evaluation.

**Recommended case study:** The observability-stack build at TiMoto paired with the vLLM serving story — together they map almost directly onto "Activity Stream" (visibility into agent behavior) and "Agent memory" (session-aware AI serving), the two most concretely described project examples in the JD.

**Red-flag questions and how to answer them:**
- *"This role asks for 1-3 years of experience — you have less than that. Why should we move forward?"* → Be direct: TiMoto is real, non-internship production ownership as the primary engineer on a 3-person team, not a junior support role; total engineering exposure across TiMoto plus two internships (Google, Develop for Good) is broader than the raw tenure number suggests.
- *"Why Giga specifically, over other AI infra companies you've looked at?"* → Anchor on the DoorDash relationship and the "Activity Stream"/"Agent memory" project examples — genuine, specific reasons rather than generic enthusiasm.
- *"You've applied to two other GigaML roles before — why this one?"* → Be honest: this is a different req (SF, broader I/II band, higher comp ceiling) than the New York new-grad roles previously evaluated; genuine, continued interest in the company across multiple open positions is a reasonable thing to say plainly if asked.

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Posting freshness | "Apply for this Job" resolves to a live, functional Ashby application flow | Positive |
| Description quality | Names specific, concrete in-flight projects (Atlas, Activity Stream, Dynamic knowledge, Agent memory), a specific named customer (DoorDash), and a structured compensation field — well above boilerplate | Positive |
| Requirements realism | 1-3 years is a realistic, moderate bar for a SWE I/II posting with no internal contradictions | Positive |
| Salary transparency | Explicit, structured compensation range disclosed via Ashby's compensation field | Positive |
| Company hiring signals | No 2026 layoffs or freeze found; $61M Series A (Nov 2025) and a confirmed, named paying customer (DoorDash) both point to active growth | Positive |
| Reposting pattern | This exact req (`96f0c2f8-...`) not found in `data/scan-history.tsv`; distinct from the two other GigaML reqs already evaluated (#15, #59) — this is the company's third open req seen by this pipeline, consistent with active, multi-track hiring rather than a single recycled listing | Neutral |
| Role market context | Early-career SWE reqs at funded, revenue-generating startups commonly fill within a normal window; nothing here suggests an outlier | Neutral |

**Context notes:** This is the third distinct GigaML/Giga req evaluated for Harry (#15, #59, and this one), each with a different URL, title, or location — consistent with a company running multiple genuine, concurrent hiring tracks rather than reposting the same listing.

**6. Employment Classification:** Not flagged — standard full-time employment posting with comprehensive benefits (401(k), medical/dental/vision), no contractor-status language.

**7. AI-Buzzword vs. Infrastructure Mismatch:** Not flagged — the JD names concrete, specific projects (Atlas, Activity Stream, Agent memory) rather than vague transformation language, and the company has a real, named paying customer; not applicable.

**8. Benefits/Employment Terminology Country Mismatch:** Not flagged — location is San Francisco, US, and benefits terms (401(k)) are consistent with a US posting.

## Re-verification Addendum (2026-09-28, Work at a Startup listing)

The same role surfaced on YC's Work at a Startup ("Software Engineer I / II - San Francisco", Giga S23). Same title, location, and body (Atlas, Activity Stream, Dynamic knowledge, Agent memory examples; "1-3 years of professional software engineering experience") as the Ashby posting `96f0c2f8-3d97-4763-ab46-b6af6ad8b2e7` evaluated here, so this is a duplicate, not a new requisition. No new row. Status stays **Applied** (applied earlier via #019 and #184, both pointing to this Ashby ID). Do not re-apply through Work at a Startup without checking with the recruiter first; a second submission to the same req can look like noise.

Updated facts from the WaaS listing: $150K-$250K (WaaS range; the Ashby band recorded above was $160K-$250K plus equity), "Will sponsor" (visa sponsorship stated), Series A of $61M with DoorDash as a named customer, stack Django, React, GCP, fine-tuned open-source LLMs. Interview process: 20-minute recruiter screen, 1.5-hour live coding round, 15-minute hiring-manager intro, full-day in-office interview. WaaS tags the role "3+ years" while the body says 1-3 years; the body is the more specific signal. Score stays 4.3/5.

Fresh CV from the locked `cv.md`: `output/184-harry-nguyen-resume-2026-09-28.pdf` (1 page, no em dash), for use if the recruiter asks for an updated resume.

## Risk Summary

| Signal | Status |
|--------|--------|
| Posting legitimacy | ✅ High Confidence — live application flow, concrete named projects and customer, structured comp disclosure |
| Employment classification | ✅ clear — standard full-time employment posting |
| Culture screen | — not evaluated (no `culture_screen.require` configured in `config/profile.yml`) |
| Interview red flags | — no interview sessions yet |
| AI claims vs. infrastructure | ✅ consistent — concrete, specific project examples and a verifiable paying customer, not oversold transformation framing |

---

## Cover Letter Draft

> Draft generated at evaluation time. Complete via `/career-ops cover 184-gigaml` to fill in angles, confirm research, and generate the PDF.
> Gaps flagged below — address them during the cover flow.

---

**Opening** *(placeholder — refine with your "why this role" angle)*
Giga's Activity Stream feature — giving visibility into agent behavior through log filters, timestamps, and frequency charts — is the exact problem I solved at TiMoto by building an observability stack from zero, just for a different kind of production AI system.

**Profile introduction**
I'm a Computer Science student at Georgia State (May 2027) currently the primary engineer for backend, cloud infrastructure, and ML serving at TiMoto AI, where I own a production system end-to-end on a 3-person team: a vLLM-based inference layer, a full observability stack, and gRPC backend services. Before that, I shipped production infrastructure at Google as a Chrome engineering intern.

**Key achievements** *(selected from cv.md — exact wording preserved)*
- **Observability stack built from zero at TiMoto,** cutting incident root-cause time to under 15 minutes via Prometheus, Grafana, and CloudWatch across the gRPC and ML serving layers.
- **vLLM/PagedAttention inference engine,** eliminating OOM failures under concurrent production load by solving KV cache memory fragmentation for LLM serving.
- **gRPC deadlock fix,** restoring 100% evaluation success rate at sub-50ms p99 by redesigning lock-acquisition ordering under concurrent calls.
- **Migrated off EKS to a multi-AZ ECS Fargate deployment,** cutting infrastructure cost 44% while sustaining 99.9% uptime.

**Problems I will solve** *(placeholder — requires company research + your input)*
> To be completed: which of the four example projects (Atlas, Activity Stream, Dynamic knowledge, Agent memory) are you most drawn to, and why? Any specific detail about the DoorDash partnership or Giga's voice AI approach worth referencing?

**Closing**
I am happy to discuss further at your convenience.

---

**Gaps flagged:**
- Experience floor (1-3 years stated, Harry has ~10 months non-internship) — address directly and briefly if raised, don't over-explain.
- This is the third GigaML/Giga req evaluated for Harry — if applying to multiple GigaML roles, be prepared to explain genuine interest across positions if asked.

**JD keywords to mirror** *(extracted for ATS + human read)*
Software Engineer I/II, AI agents, backend, data pipelines, integrations, agent infrastructure, Atlas, Activity Stream, log visualization, Dynamic knowledge, Agent memory, conversation awareness, voice AI, real-time, enterprise automation, ownership, early-career

---
*Run `/career-ops cover 184-gigaml` to complete angles, confirm research, and generate the PDF.*

---

## Keywords extracted

Software Engineer I/II, AI agents, backend, data pipelines, integrations, agent infrastructure, Atlas, Activity Stream, log visualization, Dynamic knowledge, Agent memory, conversation awareness, voice AI, real-time, enterprise automation, DoorDash, customer support, ownership, early-career, Series A

## Addendum 2026-10-19: same Ashby posting sent again

**URL:** https://jobs.ashbyhq.com/gigaml/96f0c2f8-3d97-4763-ab46-b6af6ad8b2e7 (application path and jr_id ignored). Same Ashby job id as this report and as #19; still listed on Giga's board (first published 2025-05-14), San Francisco onsite, $160K to $250K plus equity, 1 to 3 years of professional experience. **Why no new row and no new CV:** exact duplicate, and the tracker records an application followed by a rejection on 2026-09-30 for this requisition (#19 is also Applied). A resubmission of the same requisition is likely blocked or ignored, so no fresh CV was built.

**Not yet evaluated on Giga's board:** Software Engineer I / II in New York (Ashby `ba9b543d-e85c-4bd1-978b-f838d7a4062f`, published 2026-02-20), which no report mentions. It is the closest alternative if you want another Giga attempt.

**Same day, second send (2026-10-19):** the same Ashby posting arrived again with a Jobright checker result of 7.0 (Fair), keywords 0/0 (the checker listed no keywords for this posting). Still a duplicate of #184, already applied and rejected on 2026-09-30; nothing else changed.

**Fresh CV on request (2026-10-19):** `output/184-harry-nguyen-resume-2026-10-19.pdf` (1 page), built because you asked for one even though this requisition was already applied to and rejected. Languages lead with Python, TypeScript and Go; Agentic Systems adds Agentic AI Systems beside LLM Agents, Tool Calling, MCP, Hybrid Retrieval (RAG) and Evals; Practices adds Customer-Facing and Monitoring (Grafana and Prometheus are stated). TiMoto order leads with the AI bug-fix agent, then the cross-team agent fix (knowledge base and RAG), then the backend and vLLM; NextStep above Pulumi. Numbers match the master CV exactly. Not added: agent memory and Slack integrations as named skills.
