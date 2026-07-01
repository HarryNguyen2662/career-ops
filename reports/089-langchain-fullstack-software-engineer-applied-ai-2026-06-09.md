# Evaluation: LangChain — Fullstack Software Engineer, Applied AI

**Date:** 2026-06-09
**URL:** https://jobs.ashbyhq.com/langchain/c75915ba-a32b-4e17-873d-19b47564170d
**Archetype:** Agentic/Applied AI + Full-Stack
**Score:** 3.9/5
**Legitimacy:** High Confidence
**PDF:** output/089-langchain-fullstack-software-engineer-applied-ai-harry-nguyen-2026-06-09.pdf

---

## Block A — Role Summary

LangChain is hiring Fullstack Applied AI Engineers to build production-grade agents powering internal operations (GTM, recruiting, support, product) and open-source reference agents (Open SWE, Open Canvas, Deep Research). The team is small and fast-moving, operating at the frontier of agent engineering and feeding learnings directly back into the LangSmith platform. This is an applied role — not pure ML research, not pure infra — requiring someone who can design end-to-end agentic workflows, implement evaluation pipelines, and ship production systems.

**Key requirements:**
- 3+ years total, including 1+ year building LLM systems in production
- Python and/or TypeScript (ideally both)
- Hands-on evaluation and monitoring for agents/workflows
- Deep understanding of prompting, retrieval, orchestration, inference APIs, model selection
- Full-stack delivery capability (agents + UI + deployment)
- Open-source contribution experience (nice-to-have)
- LangChain/LangGraph expertise (nice-to-have)
- Based in SF or NYC on-site 5 days/week

**Compensation:** $165K–$190K base + equity + benefits

---

## Block B — Match with CV + Gaps

### Strong Matches

| JD Requirement | Harry's Evidence |
|---|---|
| LLM systems in production | TiMoto: vLLM/PagedAttention inference engine, LLM-as-a-judge evaluation pipeline, 100% success rate, sub-50ms p99 |
| Evaluation and monitoring systems | TiMoto: Built and deployed LLM-as-a-judge evaluation pipeline; CloudWatch observability stack |
| Python + TypeScript | Python (Django, FastAPI, vLLM at TiMoto); TypeScript/React event-driven system at Google Chrome (25K+ lines, 95% test coverage) |
| Prompting, orchestration, inference APIs | TiMoto: LLM API integration (Claude/GPT), vLLM serving, continuous batching — direct production experience |
| Full-stack delivery | Google Chrome: TypeScript/React event-driven system; TiMoto: Django REST API backend + full-stack infra ownership |
| Open source contribution | Pulumi contributor (Go, TypeScript) — multi-cloud CLI features under review by core maintainers |
| Fast-moving startup environment | TiMoto: primary engineer on 3-person team owning backend + infra + ML serving simultaneously |

### Gaps / Risks

| Gap | Severity | Mitigation |
|---|---|---|
| Explicit LangChain/LangGraph experience not mentioned | Medium | LangChain listed under ML & AI Infrastructure skills; JD lists it as nice-to-have, not required |
| 3+ year experience threshold — Harry is ~1.5 years total (TiMoto + Google + DFG) | Medium-High | Quality of production LLM work at TiMoto is strong; Google intern at scale (3B users) compensates for quantity |
| On-site SF or NYC 5 days/week | Medium | Harry is in Atlanta on F-1. Relocation is possible but significant commitment |
| "Agent architectures" as distinct discipline | Low | TiMoto LLM pipeline + vLLM work demonstrates the underlying components; can frame as agentic workflow patterns |
| F-1 visa — sponsorship not mentioned | Low-Medium | LangChain Series B ($125M), likely can sponsor; apply, flag it |

### Overall Match Assessment

Harry has the most critical signals: production LLM systems with real evals, Python + TypeScript fluency, full-stack delivery, and open-source contribution. The experience years gap (1.5 vs 3+) is the primary risk — but TiMoto's scope (owns backend + ML serving + infra on a production AI startup) reads senior relative to Harry's graduation year. LangChain is clearly building fast and may value trajectory + demonstrated AI depth over raw years.

---

## Block C — Level & Strategy

**Level:** IC2/IC3 (junior-mid). JD says "3+ years" but the team is small and the work is frontier — there's openness to non-traditional paths given the pace.

**Application strategy:**
1. Lead with the applied AI angle — LLM-as-a-judge eval pipeline at TiMoto is exactly what LangChain cares about (they built LangSmith for this)
2. Emphasize full-stack: TypeScript/React at Google Chrome + Django/FastAPI backend at TiMoto = end-to-end delivery
3. Name-drop LangChain skills section explicitly — it's there, make it prominent
4. Frame TiMoto role as "building an applied AI product" not just infra work
5. Open source (Pulumi) addresses the nice-to-have directly — mention it explicitly
6. Acknowledge the years gap proactively in cover note if asked: "I've compressed more production LLM work into 12 months than most 3-year engineers — here's the receipts"

**Visa note:** LangChain is Series B, SF-based, well-funded. H-1B sponsorship likely feasible. Apply without hesitation, disclose F-1 status when asked.

---

## Block D — Comp & Demand

**Posted range:** $165K–$190K base + equity + 401(k) + health/dental/vision + meals on in-office days

**Harry's target:** $150K–$200K target, $140K minimum

**Assessment:** The posted range ($165–190K) sits right in Harry's target band and above his minimum. This is a good comp match. At the junior-mid level, Harry would likely land in the $165–175K range depending on leveling conversation. Equity at a Series B with $125M raised (IVP, Sequoia, Benchmark, CapitalG, Sapphire) could be meaningful — this is not a pre-product startup.

**Market signal:** LangChain is the leading open-source LLM framework with 100M+ monthly downloads, 6K+ paying customers, Fortune 500 traction. The equity has real upside potential. This is a brand-name employer in the AI infrastructure space — strong resume signal regardless of tenure.

---

## Block E — Customization Plan

### CV Tailoring
- **Skills section lead:** ML & AI Infrastructure first (vLLM, PagedAttention, LLM-as-a-judge evaluation, LangChain), then Languages with Python + TypeScript prominent
- **TiMoto bullets reorder:** Lead with LLM API integration + evaluation pipeline (the "applied AI" angle), then infra/backend
- **Google Chrome bullets:** Lead with TypeScript/React event-driven system (full-stack signal), then C++ IPC
- **Projects:** Pulumi open-source contribution is a direct nice-to-have match — keep prominent

### Cover / Application Angle
- Open with: "I built a production LLM-as-a-judge evaluation pipeline at TiMoto — which is basically what LangSmith is for the world. I want to work on the team that builds the platform everyone else uses."
- Reference the Applied AI team's open-source reference agents (Open SWE, Open Canvas) — signal you know what the team actually does
- Mention LangChain is in your skills stack and you understand the ecosystem

### Keywords to include
- LangChain, LangGraph, LLM orchestration, evaluation pipelines, agentic workflows, applied AI, Python, TypeScript, production agents, observability, retrieval

---

## Block F — Interview Plan

**Expected interview loop:** Technical screen (coding) → System design (agent architecture) → Applied AI deep-dive → Culture/cross-functional fit

### Coding
- Python + TypeScript fluency expected; LeetCode medium/hard on graphs (agent traversal patterns)
- Expect LangChain/LangGraph API design questions — study LangGraph state machines and edges

### System Design: Agent Architecture
- Key scenario: "Design an agent that automates recruiting outreach at LangChain"
  - Components: LLM orchestration layer, retrieval (LinkedIn/job data), evaluation loop, human-in-the-loop review, monitoring
  - Use LangGraph as the orchestration framework — demonstrate you know the ecosystem
- Harry's TiMoto eval pipeline is the anchor story — real production eval system, real latency constraints

### Applied AI Deep-Dive
- Prompting strategies: chain-of-thought, few-shot, structured output, system prompt design
- Evaluation: what metrics matter for agent quality (task completion rate, hallucination rate, latency)
- Harry's LLM-as-a-judge work is exact match here — own this story

### STAR Stories to Prepare
1. **TiMoto LLM eval pipeline** — designed and deployed evaluation system, 100% success rate, sub-50ms (STAR: Situation=prod reliability needed, Task=build eval infra, Action=LLM-as-a-judge + vLLM, Result=100% success + sub-50ms)
2. **Google Chrome TypeScript/React event-driven system** — 68% feature delivery acceleration, 25K+ lines, 95% test coverage (full-stack delivery signal)
3. **TiMoto infra + ML serving end-to-end** — primary engineer owning full stack from Django APIs to vLLM serving (demonstrates scope + startup autonomy)

### Questions to Ask
- "What does the evaluation framework for agents on the Applied AI team look like today? How does it differ from what LangSmith offers customers?"
- "How do learnings from internal agent work feed back into the platform? Is that a formal process or ad hoc?"
- "What does 'open source' mean for this role specifically — is it contributions to LangGraph, or building reference agents?"

---

## Block G — Posting Legitimacy

**Verification:** Active — posting loaded with full JD, title, description, Apply button visible. Ashby-hosted, direct LangChain careers URL.

**Legitimacy signals:**
- Real company: LangChain is a well-known Series B startup ($125M raised, IVP/Sequoia/Benchmark)
- Specific team context: Applied AI team named, reference agents named (Open SWE, Open Canvas, Deep Research)
- Real compensation range disclosed: $165K–$190K
- Specific location requirements: SF or NYC, on-site 5 days/week
- No red flags (no crypto wallet requests, no suspicious external links, no vague company description)

**Verdict: High Confidence** — legitimate posting from a real, well-funded company with specific role context.

---

## Machine Summary

```yaml
company: LangChain
role: Fullstack Software Engineer, Applied AI
date: 2026-06-09
url: https://jobs.ashbyhq.com/langchain/c75915ba-a32b-4e17-873d-19b47564170d
score: 3.9
archetype: Agentic/Applied AI + Full-Stack
legitimacy: High Confidence
comp_range: "$165K-$190K"
location: "San Francisco, CA; New York, NY"
location_type: On-site
visa_risk: medium
years_gap_risk: medium-high
top_matches:
  - Production LLM inference + evaluation pipeline (TiMoto)
  - Python + TypeScript full-stack (TiMoto + Google Chrome)
  - Open-source contribution (Pulumi)
top_gaps:
  - Years of experience (1.5 vs 3+ required)
  - On-site SF/NYC requirement (Harry in Atlanta)
  - Explicit LangChain/LangGraph production usage
recommendation: Apply — comp match, strong applied AI evidence, LangChain is brand-name. Lead with eval pipeline + full-stack signal. Acknowledge experience gap proactively.
pdf: output/089-langchain-fullstack-software-engineer-applied-ai-harry-nguyen-2026-06-09.pdf
```
