# Evaluation: Cleric — Software Engineer, Backend

**Date:** 2026-06-07
**URL:** https://jobs.ashbyhq.com/cleric/2f5fa7c7-f065-4b29-b5e9-73177a95aee0
**Archetype:** Agentic / Automation + AI Platform / LLMOps
**Score:** 4.0/5
**Legitimacy:** High Confidence
**PDF:** output/086-cleric-software-engineer-backend-harry-nguyen-2026-06-07.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Agentic / Automation (primary) + AI Platform / LLMOps (secondary) |
| Domain | AI-powered SRE — autonomous incident investigation and resolution agent |
| Function | Build — agent capabilities, tool execution workflows, integrations, evaluation/observability tooling |
| Seniority | Junior (1–2 years) — close match for Harry's ~9 months |
| Remote | In-person, San Francisco |
| Team size | ~17 employees (Series A, Dec 2025) |
| Comp | $140,000–$170,000 base + equity (undisclosed) |
| TL;DR | Cleric builds an autonomous AI agent that resolves production incidents — combining LLMs with tool use, reasoning, and corrective actions. Harry's TiMoto profile (vLLM serving, LLM-as-a-judge evaluation, gRPC production systems) is a near-perfect match for this archetype. 1–2 years experience requirement fits Harry's ~9 months. Comp floor ($140K) exactly meets Harry's minimum. Main risks: H-1B sponsorship unconfirmed at a 17-person startup; equity illiquid at $20M valuation. Strong apply. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| 1–2 years professional SWE experience | TiMoto (~9 months) + Google Chrome intern + Develop for Good intern | ✅ Within range |
| Python experience (primary language) | Skills: Python; TiMoto: FastAPI, Django, LangChain; Develop for Good: AWS BaaS | ✅ Direct |
| Software engineering fundamentals + system design | TiMoto: gRPC inter-service, circuit breakers, multi-AZ ECS; Chrome: IPC transport, lock-free trie | ✅ Strong |
| Interest in AI/ML/agentic systems | TiMoto: vLLM serving, LLM APIs (Claude, GPT), LLM-as-a-judge evaluation pipeline; LangChain in Skills | ✅ Direct |
| Agent evaluation + observability tooling | TiMoto: LLM-as-a-judge evaluation pipeline, 100% evaluation success rate at sub-50ms p99 | ✅ Direct |
| Autonomous agent capabilities + tool execution | TiMoto: LLM API integration, agentic workflow; LangChain | ✅ |
| Distributed systems / cloud infra (nice-to-have) | TiMoto: gRPC, multi-AZ ECS Fargate, Terraform, circuit breakers; 99.9% uptime | ✅ Direct |
| Startup / fast-paced team (nice-to-have) | TiMoto: primary engineer on 3-person team, 0→1 product | ✅ Direct |
| Integrations with production systems | TiMoto: gRPC inter-service; Chrome: C++ IPC with Protocol Buffers; Develop for Good: AWS BaaS | ✅ |
| H-1B / sponsorship | F-1 — Cleric is 17-person startup; no confirmed LCA filings found | ⚠️ Unconfirmed |
| SF in-person | Harry Atlanta-based; open to relocation | ⚠️ Relocation |

**Gaps:**

1. **H-1B sponsorship unconfirmed.** Cleric has ~17 employees and raised $9.8M total (Series A Dec 2025). At this stage they may not have filed H-1B LCAs yet. Mitigation: ask the recruiter directly in the intro call. Early-stage startups often haven't filed yet but are willing to sponsor strong hires. This is a question, not a blocker.
2. **Comp floor ($140K) is Harry's walk-away minimum.** High end ($170K) is in-range. Equity upside exists at ~$20M valuation but is illiquid and early-stage. Negotiate toward the top of the range.
3. **Experience: ~9 months vs 1–2 years.** Not a hard gap — Cleric is hiring for learning velocity ("desire to learn quickly"), not tenure. TiMoto primary engineer experience signals exactly the "startup fast-paced" context they value.
4. **SF in-person.** Relocation needed from Atlanta. Not a blocker given Harry's openness to relocate.

---

## C) Level and Strategy

**Level detected:** Junior SWE (1–2 years). Harry is slightly below on paper (~9 months) but above on demonstrated production AI/systems work.

**Sell production AI engineering depth, not time:**
> "I've been building autonomous AI systems in production since September 2025 — vLLM serving, LLM-as-a-judge evaluation pipelines, gRPC inter-service layers under concurrent load. Cleric's problem — agents reasoning through production incidents with tools — is the same architecture I've been working in: LLMs + tool execution + evaluation loops. I want to work on the hardest version of this problem."

**On the startup fit:**
> "At TiMoto I was the primary engineer responsible for backend, infra, and ML serving on a 3-person team. I've never had a senior engineer to punt problems to — that's the environment I do my best work in."

**On the agentic systems angle:**
> "The evaluation and observability layer is what separates reliable agents from unreliable ones. I built a LLM-as-a-judge evaluation pipeline at TiMoto that runs at 100% success rate at sub-50ms p99. That's the kind of work I want to keep doing — and Cleric's incident resolution domain is the right production environment to push it further."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Cleric stated base | $140,000–$170,000 |
| Cleric equity | Undisclosed; ~$20M est. valuation (Seed + Series A = $9.8M total raised) |
| AI agent SWE new grad TC (market est.) | $180K–$280K at well-funded AI startups; Cleric below market on base but early equity |
| Harry target | $150K–$200K base |
| Harry minimum | $140K |

Base floor ($140K) exactly meets Harry's walk-away minimum; target is $150K–$170K for this role. Equity at ~$20M valuation has meaningful upside if the company grows (typical early-stage SWE grant = 0.1–0.5%). Negotiate to top of range ($170K) — cite TiMoto production AI serving depth and Google Chrome internship.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet order | gRPC/deadlock varies | Lead with vLLM/LLM serving + evaluation bullet | Cleric is an AI agent company; LLM infrastructure and evaluation is the core signal |
| 2 | TiMoto bullet 1 | "Led backend..." | Add explicit mention of LLM API integration (Claude, GPT) | Cleric uses LLMs for agent reasoning — show Harry built with LLM APIs in production |
| 3 | Skills row order | Distributed Systems leads | ML & AI Infrastructure leads, then Languages (Python first) | Python is the primary language; LLM/agent infrastructure is the core archetype |
| 4 | Languages row | C++ first | Python, Go, TypeScript, C++ first | Python = Cleric's primary language |
| 5 | Pulumi project | Raft/Paxos study | Keep — distributed systems depth shows the "strong fundamentals" Cleric values | Supports system design interview preparation |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Agent evaluation + observability | TiMoto LLM-as-a-judge | AI product needed reliable evaluation of LLM output quality in production | 100% evaluation success rate at sub-50ms p99 | Designed LLM-as-a-judge evaluation pipeline; continuous evaluation under load | Zero evaluation failures at production traffic | Evaluation is not testing — it's a production system that tells you when the model drifts; treat it with the same SLO discipline as your serving layer |
| 2 | Autonomous agent + tool execution | TiMoto LLM API serving | Needed to serve LLM-powered agent calls with reliability and low latency | Zero OOM failures at production traffic | vLLM with PagedAttention; continuous batching; gRPC tool invocation layer | 100% success rate, sub-50ms p99 | An AI agent is only as reliable as its inference layer — you have to understand the memory model of the LLM to prevent cascading failures under concurrent load |
| 3 | Production distributed systems | TiMoto gRPC deadlock | Production deadlock under concurrent gRPC calls from agent workflows | 100% evaluation success restored | Traced shared resource acquisition conflicts; redesigned call sequencing | Resolved, zero recurrence | Production AI systems fail in two ways: the model and the infra — the gRPC layer was the infra failure mode, not the model |
| 4 | Startup ownership | TiMoto 0→1 | Primary engineer on 3-person startup building AI product | Ship backend + infra + ML serving end-to-end | Owned every layer: gRPC, Django, vLLM, ECS Fargate, Terraform | 99.9% uptime, 44% cost reduction | The defining constraint of a small team isn't skill, it's judgment — you have to know what NOT to build as much as what to build |
| 5 | Learning quickly / production AI | Chrome + TiMoto combined | New to both Chrome-scale C++ and production LLM serving | Ship to 3B+ users in one case; build serving infra from scratch in the other | C++ IPC/lock-free trie at Google; vLLM/LLM-as-a-judge at TiMoto | Both in production, both with SLOs | Fast learning in production is different from fast learning in a sandbox — the cost of being wrong is the feedback signal that actually sticks |

**Recommended case study:** TiMoto end-to-end — "I built the backend, the serving layer, and the evaluation pipeline for an AI product from scratch. The hardest part wasn't the LLM — it was making the evaluation layer reliable enough to trust in production. That's exactly what Cleric needs: someone who cares about whether the agent is actually working, not just whether it's running."

**Red-flag questions:**
- *"Less than 1 year of experience?"* → "9 months as primary engineer for backend, infra, and ML serving on a 3-person team — no senior engineer above me. That maps to more production surface area than most 2-year experiences at larger companies."
- *"Work authorization?"* → "F-1, OPT from May 2027. I'd need H-1B sponsorship for long-term. Can you confirm Cleric's sponsorship posture? I want to surface it early so it doesn't become a surprise."
- *"Why Cleric over a larger AI company?"* → "Larger AI companies have infrastructure teams that build the serving layer for the agents — the interesting problem is abstracted away. At Cleric I'd own the full stack of a production agent that investigates real incidents. That's the harder problem."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active on Ashby | Positive |
| Comp disclosed | $140K–$170K explicitly stated | Positive |
| Company status | Cleric — $9.8M raised (Seed + Series A Dec 2025), 17 employees, running in production at fintech/ride-sharing/AV companies | Positive |
| JD specificity | Named responsibilities (agent capabilities, tool execution, evaluation/observability, integrations), named interview process (4 rounds), stated culture ("radical candor") | Positive |
| Production claims verifiable | "Already running in production at high-scale companies across fintech, ride-sharing, and autonomous vehicles" — specific enough to be real | Positive |
| Blog / press coverage | $4.3M seed announced (TechFunding News, LinkedIn, Pulse2); Series A Dec 2025 confirmed via Tracxn/Crunchbase | Positive |
| Founders named | Shahram Anver (CEO) + Willem Pienaar (CTO) — searchable | Positive |
| H-1B | No confirmed LCA filings (small startup); sponsorship willingness unconfirmed | Neutral |

---

## Keywords extracted

Python, autonomous agent, LLM, AI agent, agentic systems, incident resolution, SRE, observability, evaluation, tool execution, distributed systems, cloud infrastructure, backend, production, San Francisco, startup, early-stage, FastAPI, LangChain, agent reasoning, integration

---

## Machine Summary

```yaml
company: Cleric
role: Software Engineer, Backend
date: 2026-06-07
url: https://jobs.ashbyhq.com/cleric/2f5fa7c7-f065-4b29-b5e9-73177a95aee0
score: 4.0
archetype: Agentic / Automation + AI Platform / LLMOps
location: San Francisco, CA (in-person)
comp_range: "$140,000–$170,000 base + equity (~$20M est. valuation)"
visa_risk: "F-1 — H-1B unconfirmed (17-person startup, no LCA filings found); ask recruiter early"
legitimacy: High Confidence
recommendation: "Apply — perfect archetype match (AI agent + evaluation + production systems); Python primary; TiMoto vLLM/evaluation is direct proof; ask about H-1B in intro call; negotiate to $170K top of range"
```
