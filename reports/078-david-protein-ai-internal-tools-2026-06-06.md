# Evaluation: David Protein — Software Engineer, AI & Internal Tools

**Date:** 2026-06-06
**URL:** https://apply.workable.com/david-protein/j/186851CD65
**Archetype:** AI Platform / LLMOps / Agentic Automation
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** output/078-david-protein-ai-internal-tools-harry-nguyen-2026-06-06.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | AI Platform Engineer — LLM workflows, agent orchestration, internal tooling |
| Domain | Consumer food startup (David Protein bar) — Finance/Ops internal tools |
| Function | Build — AI agents, internal productivity tools, data pipelines, full-stack web |
| Seniority | All levels (explicitly stated) |
| Remote | On-site New York City, 5 days/week |
| Comp | $150,000–$250,000 inclusive of cash bonus + equity |
| TL;DR | Peter Rahal's (RXBAR) new protein bar startup at $725M valuation ($85M raised, Greenoaks Series A). Looking for an engineer who can build AI-native internal tools — LLM APIs, agent frameworks, MCP, RAG, evaluation — exactly what Harry built at TiMoto. Stack is Python/TypeScript + Claude/GPT + dbt/BigQuery. Comp floor clears Harry's minimum; H-1B unknown (startup too new). Strong technical match, early-stage upside risk. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| Python and/or TypeScript (required) | TiMoto: Python/Django/FastAPI; Chrome: TypeScript/React | ✅ Strong |
| LLM APIs — Claude, GPT (required) | TiMoto: vLLM inference + LLM-as-a-judge evaluation pipeline | ✅ Direct |
| Agent frameworks, MCP connectors, RAG | TiMoto: LLM serving + evaluation; Claude Code / Pulumi MCP exposure | ✅ Partial |
| Evaluation frameworks, HITL | TiMoto: LLM-as-a-judge evaluation, 100% success rate at sub-50ms p99 | ✅ Direct |
| Production-grade Python/TypeScript | TiMoto: Django/FastAPI production backend; Chrome: 25K+ line TS/React to 3B users | ✅ |
| Full-stack web framework | Chrome: TypeScript/React; TiMoto: Django/FastAPI + React | ✅ |
| dbt + BigQuery + PostgreSQL | Not in CV — PostgreSQL only; no dbt or BigQuery | ⚠️ Gap |
| Next.js / React | Chrome: React (observer pattern, 68% delivery accel); Next.js not explicit | ✅ Partial |
| 2+ years professional SWE/data experience | TiMoto (Sep 2025-present) + Chrome (May-Aug 2025) + Develop for Good (May-Aug 2024) ≈ 14 months | ⚠️ Under minimum |
| Founding / early-stage comfort | Not explicit; TiMoto as primary engineer on 3-person startup team is the closest signal | ✅ Partial |
| H-1B sponsorship | No LCA history — startup too new; $85M raised but small headcount | ⚠️ Unknown |

**Gaps:**
1. **Experience floor** — JD says "minimum 2 years professional SWE/data experience." Harry has ~14 months total (Chrome 3 mo + Develop for Good 3 mo + TiMoto ~9 mo by June 2026). Partial gap — apply per policy; TiMoto primary ownership story compensates on seniority signal.
2. **dbt / BigQuery** — Finance team likely uses dbt + BigQuery heavily for data pipelines. Not in CV.
3. **H-1B unknown** — David Protein is a 2024-founded startup; no LCA filings in public databases. With $85M raised and Greenoaks backing, sponsorship is plausible but not confirmed.
4. **5 days NYC on-site** — Commute/relocation required; Harry would need to be NYC-based or willing to relocate.

---

## C) Level and Strategy

**Level detected:** All levels (explicitly stated). Harry fits junior/mid based on experience. Role scope suggests 1-3 YOE is acceptable given "all levels" framing and early-stage context.

**Sell TiMoto AI product experience as the direct match:**
> "I built the LLM serving layer for an AI product from scratch — vLLM with PagedAttention, LLM-as-a-judge evaluation pipeline, gRPC orchestration. Not infrastructure for its own sake: the system runs production traffic with zero OOM failures at sub-50ms p99. David Protein is building AI-native internal tools — that's exactly the same problem."

**On experience gap (2-year floor):**
> "I'm under 2 years by calendar but I've been the primary engineer responsible for the full backend, infra, and ML serving at TiMoto since September 2025. That's the ownership level of a mid SWE, not an intern."

**On H-1B:**
> "F-1, OPT from May 2027. Will need H-1B. With $85M raised and Greenoaks backing, I'd ask whether David Protein has a path for H-1B — happy to discuss timing at the offer stage."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| David Protein stated range | $150,000–$250,000 inclusive of cash bonus + equity |
| Harry target | $150K–$200K base |
| Harry minimum | $140K |

Comp floor ($150K) clears Harry's $140K minimum and meets his target range. The range spans new grad to mid — Harry at junior end (~$150–$170K) is consistent. Equity at $725M valuation (post-Series A, Greenoaks) has real upside if Rahal executes a second consumer brand exit (RXBAR sold to Kellogg's for $600M in 2017).

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet order | gRPC/deadlock leads | Lead with vLLM inference engine + LLM-as-a-judge evaluation | AI workflows + evaluation = direct JD requirement |
| 2 | Chrome bullet order | C++ IPC or React varies | Lead with TypeScript/React observer pattern | Full-stack role; Chrome TS/React is the relevant proof |
| 3 | Skills: Languages | C++ or TypeScript varies | Python, TypeScript first | JD says Python and/or TypeScript; ML/AI role |
| 4 | Skills row order | Varies by archetype | ML & AI Infrastructure leads, then Languages | AI/LLMOps role — ML infra is primary pitch |
| 5 | Skills: ML row | vLLM, evaluation | Include "LLM APIs (Claude, GPT), agent frameworks, RAG, MCP" explicitly if space | JD names these technologies verbatim |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | LLM APIs + evaluation frameworks | TiMoto LLM-as-a-judge | Production LLM serving with quality regression risk | Evaluate LLM output quality at scale without human review bottleneck | LLM-as-a-judge evaluation pipeline; automated scoring; sub-50ms p99 | 100% evaluation success rate | Automated evaluation is the unlock for production LLM — without it you can't ship |
| 2 | Agent orchestration / gRPC | TiMoto gRPC deadlock | Production deadlock under concurrent LLM calls | Diagnose and fix without senior help | Traced shared resource acquisition; redesigned call sequencing | 100% success rate restored at sub-50ms | Agent systems fail at concurrency — instrument from day one |
| 3 | Full-stack AI tool | TiMoto 0→1 | Primary engineer, 3-person team, build AI product from scratch | Ship backend + infra + ML serving | gRPC + Django + vLLM + ECS Fargate as cohesive production system | 99.9% uptime, zero OOM, 44% cost reduction | You can't build AI tooling without owning both the model layer and the API layer |
| 4 | TypeScript/React frontend | Chrome observer pattern | Chrome settings UI state across 25K+ Chromium lines | Decouple state without breaking existing functionality | Observer pattern; 95% test coverage; Chrome infra review | 68% feature delivery acceleration | Component architecture compounds — the right pattern makes every future feature cheaper |
| 5 | Production Python / data | Develop for Good | N+1 query degrading response to 3s+ on large datasets | Sub-100ms for 10,000+ records | PostgreSQL indexing redesign | Sub-100ms, 10K+ records | Read your query plans; N+1 is invisible until it isn't |

**Recommended case study:** TiMoto LLM serving — "I built an LLM inference engine with PagedAttention, then built the evaluation layer to know if it was working. Zero OOM failures and automated quality scoring at sub-50ms. David Protein wants AI-native internal tools — that's the same architecture, just pointed at internal use cases instead of consumer product."

**Red-flag questions:**
- *"Only 14 months experience?"* → "By calendar, yes. By ownership — I've been the primary engineer on the full stack at TiMoto since September 2025. I designed the architecture, debugged production deadlocks, and owned uptime. That's not junior-track work."
- *"Work authorization?"* → "F-1, OPT from May 2027. Will need H-1B. Happy to discuss sponsorship — with Greenoaks backing I'd expect David Protein to have a path."
- *"Why a food company?"* → "Peter Rahal built RXBAR as an engineering problem — ingredients as code, no compromises. David Protein has the same ethos. The AI tooling problem is real regardless of the industry, and early-stage is where you build things that matter."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active on Workable | Positive |
| Comp disclosed | $150K–$250K inclusive of bonus + equity explicitly stated | Positive |
| Company status | David Protein — $725M valuation, $85M raised (Greenoaks Series A May 2025), Peter Rahal (RXBAR $600M exit) | Positive |
| JD specificity | Detailed stack: Python/TypeScript, Claude/GPT LLM APIs, MCP, RAG, dbt, BigQuery, Next.js — specific enough to be real | Positive |
| Founder signal | Peter Rahal track record (RXBAR → Kellogg's $600M) gives credibility to funding and execution | Positive |
| H-1B track record | No LCA filings found — company founded Aug 2024, too young for public record | Neutral/Unknown |
| Finance dept context | Role sits in Finance team — AI tools for finance ops (forecasting, reporting, spend analysis) | Positive (specific) |

---

## Keywords extracted

Python, TypeScript, LLM APIs, Claude, GPT, agent frameworks, MCP connectors, RAG, evaluation frameworks, HITL, LLM-as-a-judge, dbt, BigQuery, PostgreSQL, Next.js, React, AI workflows, internal tools, full-stack, production, vLLM, inference, New York City, Series A, early-stage

---

## Machine Summary

```yaml
company: David Protein
role: Software Engineer, AI & Internal Tools
date: 2026-06-06
url: https://apply.workable.com/david-protein/j/186851CD65
score: 3.8
archetype: AI Platform / LLMOps / Agentic Automation
location: New York City (on-site, 5 days/week)
comp_range: "$150,000–$250,000 inclusive of cash bonus + equity"
visa_risk: "F-1 — H-1B unknown (no LCA history; startup founded Aug 2024); sponsorship plausible with $85M raised"
legitimacy: High Confidence
recommendation: "Apply — TiMoto vLLM + LLM-as-a-judge is a direct match for AI workflows + evaluation requirements; comp floor clears minimum; Rahal RXBAR pedigree + Greenoaks backing = credible upside; H-1B unknown is main risk"
```
