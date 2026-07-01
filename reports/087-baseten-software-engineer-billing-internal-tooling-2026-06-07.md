# Evaluation: Baseten — Software Engineer, Billing and Internal Tooling

**Date:** 2026-06-07
**URL:** https://jobs.ashbyhq.com/baseten/d073254f-729c-471e-9a33-520358ead183
**Archetype:** Backend Engineer (Payments & High-Throughput) — adjacent to Harry's archetype
**Score:** 3.5/5
**Legitimacy:** High Confidence
**PDF:** output/087-baseten-software-engineer-billing-internal-tooling-harry-nguyen-2026-06-07.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Backend (Billing / Internal Tools) — adjacent; not Harry's primary pitch but Baseten's ML context makes it closer |
| Domain | AI inference platform — usage-based billing, pricing, metering, internal tooling for Finance/Sales/GTM |
| Function | Build + Own — end-to-end billing infrastructure + internal automation for a $300M Series E AI company |
| Seniority | Mid-level SWE (no explicit YOE; comp range $165K–$330K suggests L3–L5 scope) |
| Remote | Hybrid — San Francisco or New York |
| Team size | Not specified; Baseten is ~100–200 employees post-Series E |
| Comp | $165,000–$330,000 + equity ("90th percentile or better" stated policy) |
| TL;DR | Baseten powers inference for Cursor, Notion, OpenEvidence — $300M Series E, top-tier AI infra company. This role owns billing/pricing/metering, which is non-trivial given usage-based AI inference pricing. Harry's gap: no billing/payments work on CV. His fit: "internal tools" OR condition, PostgreSQL/Django/Redis web stack, reliability/observability experience (metering ↔ CloudWatch). Apply if interested in the company; frame around the internal tools + metering angle, not billing expertise. H-1B confirmed. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| Bachelor's CS or related | Georgia State BS CS, Expected May 2027 | ✅ |
| Experience with billing systems OR internal tools | TiMoto: built and owned internal backend tooling, LLM evaluation infrastructure; Develop for Good: BaaS internal tool | ✅ via "internal tools" clause |
| Deep knowledge of web stack & databases | TiMoto: Django/FastAPI/PostgreSQL/Redis; Develop for Good: PostgreSQL indexing, AWS BaaS | ✅ Direct |
| Reliability / monitoring / incident response | TiMoto: circuit breakers, CloudWatch, 99.9% uptime, auto-rollback, on-call; Chrome: 95% test coverage | ✅ Strong |
| End-to-end ownership, shipping iteratively | TiMoto: primary engineer on 3-person team, 0→1 product | ✅ |
| Collaboration with Finance/Sales/GTM | No explicit Finance/GTM partnership in CV | ❌ Gap |
| Experience with Orb (billing platform) | Not in CV | ❌ Gap |
| Billing: pricing, invoicing, metering, revenue reporting | No explicit billing/invoicing work in CV | ❌ Primary gap |
| H-1B sponsorship | F-1 — Baseten confirmed H-1B sponsor: 8 LCAs FY2025, 7 LCAs FY2026 | ✅ Positive |
| SF/NYC hybrid | Harry Atlanta-based; open to relocation | ⚠️ Relocation |

**Gaps:**

1. **Billing systems experience (primary requirement).** Harry has no explicit billing/invoicing/pricing infrastructure work on the CV. Mitigation: the JD says "billing systems OR building internal tools" — Harry qualifies via the internal tools path. The pitch becomes: "I've built production backend tooling from scratch at TiMoto; I haven't specifically done billing but I know how to build reliable data pipelines with exactly-once semantics and high auditability."
2. **Orb integration (specific bonus).** Orb is a usage-based billing platform. Not in Harry's CV. Learnable; mention willingness to ramp.
3. **Finance/Sales/GTM collaboration.** Harry has shipped production backend systems but has not explicitly partnered with non-engineering teams (Finance, Sales). Mitigation: TiMoto 3-person team required cross-functional judgment by default; Chrome worked with Chrome infra and product teams.
4. **Billing is the primary job, not ML inference.** Baseten's billing role exists to support their AI inference business, but the day-to-day work is billing infrastructure, not ML serving. Harry's ML infrastructure depth (vLLM, evaluation pipelines) is context, not the core job function here.

---

## C) Level and Strategy

**Level detected:** Broad range ($165K–$330K) suggests the role could land at L3–L5 depending on experience. Harry would likely enter at L3.

**Framing strategy — lead with the "internal tools" clause, then connect to Baseten's inference metering context:**
> "The requirement that caught my eye was 'billing systems or internal tools' — I've built the latter. At TiMoto I owned the backend, evaluation infrastructure, and observability tooling for a production AI system. What makes Baseten's billing interesting specifically is that it's usage-based inference metering — that's not a traditional billing problem, it's an observability + reliability + data pipeline problem. I've built exactly that stack."

**On the billing gap:**
> "I haven't built invoicing systems before. I've built reliable data pipelines with circuit breakers, CloudWatch metrics, and audit trails at TiMoto. The metering and monitoring foundation for billing is the same engineering problem — I'd ramp on the billing-specific semantics quickly."

**On Baseten company fit:**
> "Baseten powers Cursor and Notion's inference — I use both products daily. The billing infrastructure here directly gates revenue for one of the most important AI infrastructure platforms right now. That's a different problem from billing at a SaaS company — it has real latency, correctness, and scale requirements."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Baseten stated base | $165,000–$330,000 (90th percentile or better policy) |
| Baseten equity | Meaningful; $300M Series E (BOND, IVP, Spark, Greylock, Conviction) |
| Billing/internal tools SWE L3 TC (est.) | ~$250K–$350K at a Series E AI company |
| Harry target | $150K–$200K base |
| Harry minimum | $140K |

Comp floor ($165K) is above Harry's $150K target and well above the $140K minimum. The stated policy of "90th percentile or better" is credible given the investor list and $300M raise. Baseten is pre-IPO — equity is illiquid but meaningful at this valuation stage. Very strong comp picture.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet order | vLLM varies | Lead with reliability/observability bullet (99.9% uptime, circuit breakers, CloudWatch) | Billing role values reliability, monitoring, incident response over ML serving |
| 2 | Develop for Good | AWS BaaS | Emphasize PostgreSQL indexing + JWT stateless scale | "Deep knowledge of web stack & databases" is the primary technical requirement |
| 3 | Skills row order | Distributed Systems or ML leads | Frameworks & Databases leads (Django/FastAPI/PostgreSQL/Redis), then Languages | Web stack + databases = core requirement; billing is backend CRUD at scale |
| 4 | Languages row | C++ or Python first | Python, Go, TypeScript first | Django/FastAPI are Python; billing backend is typically Python |
| 5 | TiMoto bullet 3 | vLLM/PagedAttention | Keep but de-emphasize; move to last TiMoto bullet | ML inference is context (Baseten company), not the job requirement |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Reliability + observability for revenue-critical workflows | TiMoto circuit breakers + CloudWatch | Distributed production system with cascading failure risk across gRPC + DB + ML serving | 99.9% uptime with auto-rollback on health check failure | Circuit breaker pattern, CloudWatch alerts, multi-AZ ECS, Terraform IaC | 44% cost reduction, zero unplanned downtime | Revenue-critical systems need failure budgets written down before incidents happen, not after |
| 2 | Internal tooling + automation | TiMoto evaluation pipeline | Needed a reliable automated evaluation system for LLM output quality in production | 100% evaluation success at sub-50ms p99 | LLM-as-a-judge evaluation pipeline with structured output; deployed as internal tooling | Zero evaluation failures at production traffic | Good internal tooling has the same SLO discipline as customer-facing systems |
| 3 | End-to-end ownership from requirements to shipping | TiMoto 0→1 | Primary engineer on 3-person startup, build entire backend + infra | Ship a production AI system with no senior safety net | Owned every layer: gRPC, Django, vLLM, ECS, Terraform | 99.9% uptime, $40–60/month infra spend | End-to-end ownership means you cannot defer the hard decisions — you own the consequences |
| 4 | Web stack + database depth | Develop for Good N+1 fix | 3s+ response degradation on large datasets from N+1 queries | sub-100ms for 10,000+ records | Diagnosed ORM-generated N+1 pattern; redesigned with PostgreSQL indexing strategy | Consistent sub-100ms | Database performance is architecture — the fix is in the schema and query design, not in caching |
| 5 | Debugging production issues with urgency | TiMoto gRPC deadlock | Production deadlock under concurrent gRPC calls | Restore 100% evaluation success rate | Traced resource acquisition conflicts across two services; redesigned call sequencing | Resolved, zero recurrence | Debugging with urgency doesn't mean debugging fast — it means forming a falsifiable hypothesis first, then testing it |

**Red-flag questions:**
- *"No billing experience?"* → "Correct — I've built production reliability infrastructure, not invoicing systems specifically. But the JD says 'billing systems or internal tools' — I've built the latter, and the metering + monitoring foundation for billing is the same engineering problem I've been solving. I'd ramp on the billing semantics fast."
- *"This role requires working with Finance and GTM — is that something you're comfortable with?"* → "At TiMoto I was the only backend engineer, so every cross-functional requirement landed on me by default. I've learned to translate ambiguous stakeholder requests into technical specs. Finance needs for billing correctness, auditability, and reconciliation are the same type of problem — just different stakeholder vocabulary."
- *"Work authorization?"* → "F-1, OPT from May 2027. Baseten filed 8 H-1B petitions in FY2025 — I confirmed that before applying. Happy to discuss timing."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active on Ashby | Positive |
| Comp disclosed | $165K–$330K + equity explicitly stated; "90th percentile" compensation policy named | Positive |
| Company status | Baseten — $300M Series E (BOND, IVP, Spark Capital, Greylock, Conviction); powers Cursor, Notion, OpenEvidence inference | Positive |
| H-1B sponsorship | 8 LCAs FY2025, 7 LCAs FY2026 — active sponsor | Positive |
| JD specificity | Named billing platform (Orb), named internal workflows (quoting, approvals, renewals, usage reconciliation), named department (Dedicated Inference) | Positive |
| Role-company fit | Usage-based billing for an AI inference platform is a real, critical function at this company stage | Positive |
| Company momentum | $300M Series E announced; named customers (Cursor, Notion) are verifiable | Positive |

---

## Keywords extracted

billing, internal tools, pricing, invoicing, metering, revenue infrastructure, Orb, PostgreSQL, Django, FastAPI, Redis, Python, web stack, reliability, observability, incident response, Finance, GTM, automation, San Francisco, New York, hybrid, Series E, AI inference, usage-based billing

---

## Machine Summary

```yaml
company: Baseten
role: Software Engineer, Billing and Internal Tooling
date: 2026-06-07
url: https://jobs.ashbyhq.com/baseten/d073254f-729c-471e-9a33-520358ead183
score: 3.5
archetype: Backend Engineer (Billing / Internal Tools)
location: San Francisco or New York (hybrid)
comp_range: "$165,000–$330,000 base + equity (90th percentile policy, $300M Series E)"
visa_risk: "F-1 — H-1B positive (8 LCAs FY2025, 7 FY2026 — active sponsor)"
legitimacy: High Confidence
recommendation: "Apply cautiously — excellent company and comp; billing experience gap is real but 'internal tools OR billing' clause opens the door; frame around metering/reliability/internal tooling angle; H-1B confirmed"
```
