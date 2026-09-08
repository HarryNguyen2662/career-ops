# Evaluation: Netic — Software Engineer (Agent Platform), New Grad 2026-2027

**Date:** 2026-07-17
**URL:** https://jobs.ashbyhq.com/netic/d9bcb6a2-0e54-4cb3-baec-43f2d74db18f/application?utm_source=jobright&jr_id=6a5853ca68d16a30e241281d
**Via:** — (direct, sourced via jobright aggregator; same company as report #173, distinct role/team)
**Archetype:** ML / AI Infrastructure Engineer (primary) + Backend / Distributed Systems Engineer (primary) — JD-level archetype: Agentic / Automation
**Score:** 4.2/5
**Legitimacy:** High Confidence
**PDF:** output/174-netic-agent-platform-harry-nguyen-2026-07-17.pdf

---

## Machine Summary

```yaml
company: Netic
role: "Software Engineer (Agent Platform) - New Grad - 2026-2027"
url: "https://jobs.ashbyhq.com/netic/d9bcb6a2-0e54-4cb3-baec-43f2d74db18f/application?utm_source=jobright&jr_id=6a5853ca68d16a30e241281d"
date: "2026-07-17"
archetype: "ML / AI Infrastructure Engineer + Backend / Distributed Systems Engineer (both primary fits)"
score: 4.2
legitimacy: "High Confidence"
advertised_comp: "not stated in JD; independently researched job-board listing for Netic New Grad SF shows $141,400 - $203,800"
via: null
risk_summary:
  posting_legitimacy: "clear"
  employment_classification: "not_evaluated"
  culture_screen: "caution"
  culture_screen_note: "Same company as report #173 -- explicit high-intensity culture language (\"run through walls\", \"lose sleep over the almost perfect\"); not negative, but a real fit consideration"
  interview_red_flags: "not_evaluated"
  ai_infra_mismatch: "not_evaluated"
```

## A) Role Summary

| Field | Value |
|---|---|
| Archetype | ML / AI Infrastructure Engineer (primary) + Backend / Distributed Systems Engineer (primary) — this is the strongest archetype match seen in this pipeline, since both are Harry's *primary* fits, not adjacent |
| Domain | Agent Platform — the internal system ("Agent Manager") that lets Netic's AI agents author, evaluate, and roll out improvements to other agents autonomously |
| Function | Build (orchestration layer, execution harnesses, guardrails/rollback for agent-improving-agent systems) |
| Seniority | Explicit "New Grad - 2026-2027," same flexible start window as #173 (winter 2026 – summer 2027, earlier welcomed) |
| Remote | On-site, San Francisco — same as #173, no remote/hybrid option |
| Team size | Same company as #173 (~22 employees), this specific team's size not separately stated |
| Culture screen | Same company-level assessment as report #173: well-funded ($43M, Series B led by Founders Fund with Greylock and notable angels), no layoff signals, but explicit high-intensity culture commitments ("run through walls," "lose sleep over the almost perfect") — caution, not a red flag. See #173 for the full writeup; not re-litigated here. |
| TL;DR | A second, distinct Netic req (Agent Platform team, not Full-Stack Product) — and a substantially better technical fit than #173, since this role is fundamentally about applying production-reliability engineering (guardrails, rollback, failure recovery) to multi-agent orchestration, which is close to exactly what Harry already does at TiMoto. |

**Geo-mismatch check:** No contradiction — same as #173, "On-site" field matches JD body.

## B) Match with CV

This is an unusually tight conceptual match — the JD's core problem (agents that must safely modify other agents, with guardrails and rollback when something goes wrong) maps almost line-for-line onto Harry's actual production reliability work, just applied to a different substrate (agent behavior instead of infrastructure).

| JD Requirement | Harry's CV Evidence |
|---|---|
| "Agent Manager": agents propose, test, and roll out improvements to other agents, including guardrails, rollback paths | TiMoto AI: architected an auto-rollback circuit breaker pattern for a multi-AZ deployment — the same "detect failure, roll back safely" pattern, applied to infrastructure rather than agent behavior. Directly transferable mental model. |
| Orchestration layer: route, sequence, and supervise multi-agent workflows in real time | TiMoto AI: resolved a production gRPC deadlock by enforcing a single lock-acquisition sequencing rule across the inter-service layer — direct experience with coordinating concurrent, multi-component systems correctly |
| Agent harnesses: tooling, sandboxes, and eval loops for agents to validate their own outputs | Skills: LLM-as-a-judge evaluation (LangChain) — directly relevant to building eval loops; TiMoto's observability stack is the same "validate before/after change" instinct applied to infra metrics |
| Python (asyncio, FastAPI) and TypeScript (Node, React) | Develop for Good: Python backend work; Chrome: TypeScript/React event-driven system; Skills list both explicitly |
| Distributed systems fundamentals | Coursework (Distributed Systems, OS, Networks) + direct production experience (gRPC, multi-AZ, circuit breakers, Kafka) |
| LLM APIs, eval frameworks, RAG, agent frameworks (LangChain, MCP) — "production experience not required, curiosity is" | Exceeds the bar: TiMoto's vLLM/PagedAttention is genuine production LLM-serving experience, well beyond the "curiosity" threshold explicitly said to be sufficient |
| Orchestration mindset: multi-step, multi-agent systems coordinating state, tool calls, failure recovery | This is, almost verbatim, a description of the TiMoto gRPC deadlock fix and the multi-AZ circuit-breaker work — just for agents instead of services |
| Founder-level ownership, comfortable with ambiguity | TiMoto AI: primary engineer, 3-person team, no existing playbook for the observability stack or the vLLM adoption |
| Co-create with customers: surface where agent-improvement can/can't be trusted, turn edge cases into safeguards | TiMoto AI: built a post-mortem practice with runbooks from real incidents — the same "turn real failures into codified safeguards" pattern, though not customer-facing in the direct-contact sense |

**Gaps:**

1. **No direct multi-agent orchestration experience** (the JD explicitly says this is fine — "you don't need to have built this before, but you should be excited to"). Not a real gap given the JD's own framing; mention genuine excitement about the problem space rather than overselling unearned experience.
2. **Customer co-creation is scoped differently here than in #173** — this JD's version is about surfacing technical edge cases from customer workflows, not sales-style relationship-building, which is a better fit for Harry's actual strengths (turning incidents into safeguards) than #173's more general "customer empathy" framing. Minor residual gap: still no direct customer-contact experience, but the technical framing narrows it meaningfully.

## C) Level and Strategy

1. **Level detected:** Explicit New Grad, same flexible window as #173.
2. **Sell senior without lying:** This is the strongest "sell senior" case in the pipeline — the JD's central technical problem (safe, guarded, reversible modification of a running system) is one Harry has solved in production, just for a different kind of system. Lead with the circuit-breaker/auto-rollback story directly, not as an analogy but as the closest real precedent available.
3. **On "no prior agent-orchestration experience":** The JD explicitly removes this as a bar — don't manufacture false depth here; instead pair genuine curiosity with the adjacent, real expertise (concurrency correctness, failure recovery) that transfers directly.

## D) Comp and Demand

Same company-level research as report #173 — not repeated here in full. Key figures:

| Source | Range | Notes |
|---|---|---|
| Advertised (JD) | Not stated | JD contains no compensation section, same as #173 |
| Independently researched (job-board listing, San Francisco, New Grad) | $141,400 – $203,800 | Same source as #173 — this is a company/level-wide figure, not role-specific to Agent Platform vs. Full-Stack Product, so treat with the same Medium-High confidence |
| Target range (candidate) | $150K – $200K | `config/profile.yml` |

**Company type and demand trend:** See report #173 — same $43M Series B-backed, 22-person, actively-hiring company. Hiring multiple new grads specifically for the Agent Platform team signals this is a real, resourced initiative, not a single speculative headcount.

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---------|---------------|------------------|---------|
| 1 | Summary | Generic backend/ML-infra framing | Lead explicitly with the circuit-breaker/auto-rollback story as the closest real-world precedent to "agents that guard and roll back other agents" | This is the single strongest, most specific hook available in this entire pipeline |
| 2 | TiMoto bullets | Present | Lead with the gRPC deadlock fix and the auto-rollback circuit breaker bullets, in that order | Both map almost directly onto "orchestration" and "guardrails/rollback" JD language |
| 3 | Skills | Full list | Surface LangChain/LLM-as-a-judge evaluation prominently, alongside Python/TypeScript | Matches "eval loops" and "agent frameworks" JD language directly |
| 4 | Cover note | N/A | Name the "no prior multi-agent orchestration experience" point directly, paired with the circuit-breaker precedent | The JD itself says this is acceptable — proactively bridging it with a real precedent is stronger than staying silent |

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|-----------------|-----------------|---|---|---|---|------------|
| 1 | Agent Manager: guardrails and rollback paths for self-modifying agents | Multi-AZ auto-rollback circuit breaker at TiMoto | Single-zone failures risked taking production down silently | Guarantee safe recovery without manual intervention | Architected a circuit breaker pattern with auto-rollback across multi-AZ ECS Fargate | 99.9% uptime maintained | Would formalize the pattern into a reusable module — directly relevant to building a general-purpose Agent Manager guardrail system |
| 2 | Orchestration layer: sequencing and supervising concurrent multi-agent workflows | gRPC deadlock fix at TiMoto | Inconsistent lock-acquisition ordering caused deadlocks under concurrent calls | Restore correct sequencing across the inter-service layer | Enforced a single lock-acquisition sequencing rule | 100% eval success rate at sub-50ms p99 | Should have added a lock-ordering lint/test earlier — directly informs how to design guardrails proactively rather than reactively |
| 3 | Agent harnesses: eval loops for agents to validate their own outputs | Building TiMoto's observability stack from zero | No visibility into whether changes improved or degraded the system | Build a system that surfaces regressions before they cause harm | Deployed Prometheus/Grafana metrics for continuous validation | Cut incident root-cause time to under 15 minutes | Would prioritize automated regression detection over manual dashboard review next time |
| 4 | Comfortable with ambiguity, no established playbook | vLLM/PagedAttention adoption with no prior production LLM-serving background | No existing team knowledge or playbook for production LLM serving | Ship reliable inference despite the unfamiliar territory | Researched, chose, and deployed vLLM/PagedAttention solo | Eliminated OOM failures entirely | Direct, honest evidence of operating without a playbook — the closest match to "there isn't much of a playbook for agents building agents" |
| 5 | Turn customer edge cases into platform safeguards | Post-mortem practice with runbooks at TiMoto | Incidents were being fixed but not systematically prevented | Convert real failures into institutional knowledge | Built a shared on-call rotation and runbook practice | Cut mean-time-to-identify 68% | Would formalize this into automated regression tests earlier rather than relying on runbooks alone |

**Recommended case study to present:** The TiMoto circuit-breaker/auto-rollback story specifically — it is the single most directly transferable piece of evidence in Harry's entire background for this exact role.

**Red-flag questions and how to answer them:**
- *"You've never built multi-agent orchestration — why should we trust you here?"* → The JD itself says this isn't required; pivot immediately to the circuit-breaker/gRPC-deadlock precedent as evidence of solving the same underlying problem class (safe coordination and recovery of concurrent, interacting components) in a different domain.
- *"This role has no established best practices — how do you operate without a playbook?"* → The vLLM/PagedAttention adoption story is direct, honest evidence, not a hypothetical answer.

## G) Posting Legitimacy

**Assessment: High Confidence**

Same company-level assessment as report #173 (not re-derived): live page, active application form, detailed and specific JD, Department "University" (dedicated new-grad pipeline), fresh Series B funding, no layoff signals, actively hiring multiple new grads. This is a genuinely distinct req (different `jr_id`, different team, different responsibilities) from #173, not a duplicate or repost of the same listing.

**Employment classification signal:** Not evaluated — same as #173, no contractor language present.

**AI-buzzword vs. infrastructure mismatch:** Not evaluated — if anything, this JD is unusually technically specific and un-buzzword-y for an "agentic AI" posting (it names concrete systems — Agent Manager, execution harnesses, orchestration layer — rather than vague transformation language), so this check clearly doesn't apply.

**Benefits/employment terminology mismatch:** Not evaluated — no benefits section in this posting to check.

## Risk Summary

| Signal | Status |
|--------|--------|
| Posting legitimacy | ✅ High Confidence |
| Employment classification | — not evaluated |
| Culture screen | ⚠️ caution — same company-level signal as #173 (high-intensity culture language, otherwise well-funded and growing) |
| Interview red flags | — no interview sessions yet |
| AI claims vs. infrastructure | — not evaluated |

---

## Cover Letter Draft

> Draft generated at evaluation time. Complete via `/career-ops cover 174-netic-agent-platform-swe-new-grad-2026-07-17` to fill in angles, confirm research, and generate the PDF.
> Gaps flagged below — address them during the cover flow.

---

**Opening** *(placeholder — refine with your "why this role" angle)*
Netic's Agent Manager problem — building the guardrails and rollback paths that let agents safely improve other agents — is the same class of problem I've already solved in production, just for infrastructure instead of agent behavior.

**Profile introduction**
I'm the primary engineer for backend, cloud infrastructure, and ML serving at TiMoto AI, where I built an auto-rollback circuit breaker pattern that keeps a multi-AZ production system at 99.9% uptime, and resolved a concurrency bug by enforcing correct sequencing across a distributed inter-service layer. I want to bring that same "detect failure, recover safely, prevent recurrence" discipline to Netic's Agent Platform team.

**Key achievements** *(selected from cv.md — exact wording preserved)*
- **Prevented single-zone failures from taking production down, sustaining 99.9% uptime,** by architecting a multi-AZ ECS Fargate deployment with Terraform IaC and an auto-rollback circuit breaker pattern.
- **Restored 100% evaluation success rate at sub-50ms p99,** by resolving a production gRPC deadlock — replaced inconsistent lock-acquisition ordering with a single enforced sequencing rule.
- **Eliminated OOM failures under concurrent production load,** by replacing naive batching with a vLLM/PagedAttention inference engine, solving KV cache memory fragmentation for LLM serving.
- **Cut incident root-cause time from unknown to under 15 minutes,** by building TiMoto's observability stack from zero — Prometheus and Grafana metrics alongside CloudWatch dashboards.

**Problems I will solve** *(placeholder — requires company research + your input)*
> To be completed: worth asking in interviews what's currently the hardest unsolved problem in the Agent Manager system's guardrail design — the report's research didn't turn up Netic-specific technical detail beyond the JD itself.

**Closing**
I am happy to discuss further at your convenience.

---

**Gaps flagged:**
- No direct multi-agent orchestration experience — the JD explicitly says this isn't required; addressed via the circuit-breaker precedent rather than left unaddressed.
- Same comp-not-stated-in-JD and high-intensity-culture flags as report #173 — not repeated in depth here.

**JD keywords to mirror** *(extracted from the JD)*
Agent Manager, orchestration layer, execution harnesses, guardrails, rollback paths, human-in-the-loop, multi-agent workflows, agentic products, eval loops, asyncio, FastAPI, distributed systems, New Grad

---

*Run `/career-ops cover 174-netic-agent-platform-swe-new-grad-2026-07-17` to complete angles, confirm company research, and generate the PDF.*

---

## Keywords extracted

Agent Manager, orchestration layer, execution harnesses, sandboxes, eval loops, guardrails, rollback paths, human-in-the-loop, multi-agent workflows, agentic products, asyncio, FastAPI, Node, React, distributed systems, LLM APIs, RAG, LangChain, MCP, founder-level ownership, New Grad, San Francisco, on-site

---

## Addendum 2026-09-19: CV correction warning

The CV originally built for this report (`output/173-...` or `output/174-...`, dated 2026-07-17) was made under an older cv.md. It contains content that is not on the current cv.md, including "Expected May 2027", a Coursework line, "3B+ active users", JWT auth, Kafka, LangChain, LoRA/QLoRA and PyTorch. Report body text in this file that cites those items should not be reused. If an application was submitted with that CV, be ready for interview questions on those claims, and answer only from what the current cv.md supports. A fresh CV built from the current cv.md can be generated on request.

## Addendum 2026-11-02 (same requisition re-sent from Jobright; no new tracker row)

**Duplicate:** Ashby id `d9bcb6a2` and the same Jobright `jr_id` as the July application link. Tracker status is already **Applied** (from 2026-07-17). The posting is still listed on Netic's Ashby board (published 2026-07-16). Netic also has #173 (Applied) and #573 (FDE, Evaluated, not applied).

**New fact since July:** pay is now stated on the board: base $138,000 to $160,000 per year (San Francisco). The bottom is $2K under your $140K floor; the top is inside your $150K to $200K target.

**Fresh CV:** `output/174-harry-nguyen-resume-2026-11-02.pdf` replaces the 2026-07-17 build, which was made from an older cv.md (see the 2026-09-19 correction above). One page, eight one-line Skills rows, no blank gap. TiMoto order: production agent, backend owned end to end, gRPC deadlock, company-wide agent, vLLM, Fargate migration. Google order: Mojo IPC, test fix, shared-state refactor, lock-free trie. NextStep before Pulumi. Skills: LLM APIs, LLM Agents, Tool Calling, MCP, LangChain (stated by Harry, Skills only), RAG, Evals; Distributed Systems, Concurrency, Algorithms, Data Structures; Guardrails, Rollback, Reliability, Monitoring, Scalability (backed by the agent's tests and auto-rollback); Full-Stack Development (stated), Customer-Facing (stated). Checks: 1 page, 0 em dashes, 0 asterisks, numeric parity with the master CV, ATS coverage 19 of 26 JD terms (73%).

**Why it matches the JD:** "Agent Manager" with guardrails, rollback paths and human-in-the-loop checkpoints maps to the TiMoto production agent (tests, auto-rollback, 95% automated). Real gaps, not added: multi-agent orchestration, asyncio, data modeling.

**Status guidance:** if the July CV was the one submitted, expect questions on claims that are not on the current cv.md (listed above), and answer only from what cv.md supports. Send the fresh CV to a Netic recruiter if you are in contact, or use it for a follow-up. Status stays Applied.
