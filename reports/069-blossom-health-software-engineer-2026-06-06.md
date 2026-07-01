# Evaluation: Blossom Health — Software Engineer (All Levels)

**Date:** 2026-06-06
**URL:** https://jobs.ashbyhq.com/Blossom-Health/94a6b3b4-01ee-4b2d-ad2b-0c7cda197604
**Archetype:** Founding/Early-Stage SWE + AI Product Engineering
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** output/069-blossom-health-software-engineer-harry-nguyen-2026-06-06.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Founding/Early-Stage SWE + AI/ML Engineer (product-facing) |
| Domain | AI-native mental health / psychiatry platform |
| Function | Build — product + infra, full-stack ownership |
| Seniority | All levels (2+ years minimum) |
| Remote | On-site NYC 5 days/week |
| Team size | Small Series A team (~20-30 est.) |
| TL;DR | Early-stage startup needs a generalist SWE fluent in TypeScript/Python who can ship AI-powered clinician and patient product features end-to-end. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| TypeScript (strong pref) | Chrome: 25K+ lines React/TypeScript, observer pattern, 68% delivery acceleration | ✅ Strong |
| Python (strong pref) | TiMoto: Django/FastAPI serving layer; Develop for Good: AWS BaaS | ✅ Strong |
| LLM-powered apps experience | TiMoto: vLLM inference engine, PagedAttention, continuous batching — zero OOM in production | ✅ Direct |
| Production systems end-to-end | TiMoto: primary engineer for backend + infra + ML serving, 99.9% uptime | ✅ Strong |
| Reliability / observability / uptime | TiMoto: CloudWatch + Prometheus + circuit breaker + auto-rollback | ✅ Strong |
| High-quality code / code reviews | Chrome: 95% test coverage, design docs reviewed by senior Chrome engineers | ✅ Strong |
| Autonomy / ownership | TiMoto: primary engineer on 3-person team, owns full stack | ✅ Direct |
| CS degree or equivalent | Georgia State BS CS, GPA 3.75, May 2027 | ✅ |
| 2+ years professional experience | ~1.5 years calendar (Google May–Aug 2025 + TiMoto Sep 2025–present) | ⚠️ Soft gap |
| Authorized to work in US | F-1 (OPT eligible May 2027) — technically authorized, long-term H-1B needed | ⚠️ Risk |
| Healthcare domain | No experience — not required for SWE role | ➖ Neutral |

**Gaps:**

1. **2+ years vs ~1.5 years calendar** — Production depth at Chrome (3B+ users) + TiMoto end-to-end exceeds what most 2-year engineers have done. Frame impact, not calendar time.
2. **F-1 / H-1B sponsorship unconfirmed** — "Authorized to work" language is ambiguous. F-1 OPT is authorized. Series A startup with $20M may lack bandwidth for H-1B. Clarify early.
3. **NYC relocation from Atlanta** — Harry is open; not a blocker.
4. **Healthcare domain** — Not required; SWE role is product + infra, not clinical.

---

## C) Level and Strategy

**Level detected:** "All Levels" — calibrated by interview. Harry maps to L3/junior-mid.

**Sell senior without lying:**
- Lead with production impact, not years: "I shipped C++ to 3B Chrome users and own a production AI serving stack — the timeline is compressed but the depth isn't."
- TiMoto primary engineer = founding SWE archetype. Perfect for a 30-person startup.
- Google brand carries weight at startups — positions Harry as top-percentile new grad.

**If they downlevel:**
- $150K at L2/junior band still above $140K minimum. Accept if equity meaningful (0.1–0.3% at Series A).
- Negotiate 6-month review clause to level up.

---

## D) Comp and Demand

| Metric | Data | Source |
|--------|------|--------|
| Blossom stated range | $150K–$220K + equity | Ashby JD |
| NYC SWE avg total comp | ~$193K median | Levels.fyi |
| Series A startup SWE (NYC) | $150K–$200K base + 0.1–0.5% equity | Levels.fyi |
| Harry target range | $150K–$200K | profile.yml |
| Harry minimum | $140K | profile.yml |

Comp is a direct match to Harry's targets. $150K floor above $140K walk-away. Series A equity is real upside — Headline-backed, 10K+ patients with insurance coverage, credible path to scale.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet 1 | "Led backend, cloud infra, and ML serving" | "Built end-to-end AI-native product stack — LLM serving, backend services, and cloud infra — for a production AI platform serving real users" | Mirrors Blossom "AI-native" language |
| 2 | TiMoto bullet order | vLLM mid-list | Move vLLM/LLM serving to lead | "LLM-powered apps preferred" = top differentiator |
| 3 | Chrome bullet order | C++ IPC leads | Lead with TypeScript/React observer pattern | Role is TypeScript/Python first; Chrome TS proves product credibility |
| 4 | Skills section | Distributed Systems leads | Promote Frameworks & Databases (Django, FastAPI, TypeScript, React) row up | JD is Python/TypeScript product role, not systems-first |
| 5 | CV headline comment | Distributed systems framing | "AI-native product engineering" framing | Blossom is AI-native care platform — mirror the language |

**LinkedIn:** Add "AI-native product engineering" + "LLM application development"; pin timoto.ai as Featured — live AI product mirrors Blossom's stack.

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Build scalable, reliable systems | TiMoto multi-AZ + circuit breaker | Single-AZ prod with no failover | Fault-tolerant infra on startup budget | ECS Fargate, Terraform, circuit breaker, health check auto-rollback | 99.9% uptime, 44% cost cut, $40–60/mo | Design for failure Day 1 — retrofit is expensive |
| 2 | LLM-powered experiences | TiMoto vLLM inference | OOM crashes under concurrent production load | Zero OOM, sub-50ms p99 | vLLM + PagedAttention; tuned batching | Zero OOM at production traffic | KV cache fragmentation is a latency multiplier — instrument early |
| 3 | Ship quality code fast | Chrome TypeScript/React system | 25K+ lines Chromium, state coupling causing cascading failures | Decouple + accelerate feature delivery | Observer pattern event system; 95% test coverage | 68% delivery acceleration, 3B users | Decouple state model early — retrofitting at scale is expensive |
| 4 | Reliability / observability | gRPC deadlock fix at TiMoto | Production deadlock under concurrent calls | Debug root cause alone; fix without regression | Traced shared resource acquisition; redesigned call sequencing | 100% success rate, sub-50ms p99 | Concurrent paths need explicit ownership models |
| 5 | Autonomy, ambiguity, ownership | TiMoto primary engineer | 3-person team, no senior engineers, full stack | Own everything from scratch | Designed, deployed, operated all layers | Production SLOs met consistently | Owning all layers forces you to understand tradeoffs — startup superpower |
| 6 | Leverage AI for user experiences | TiMoto AI product + eval pipeline | Users needed reliable AI-powered workflows | Zero hallucination failures, real-time responses | Evaluation pipeline + vLLM + session context | Sub-50ms p99, trusted in production | Eval pipeline is as critical as the model — trust requires measurement |

**Recommended case study:** TiMoto AI (timoto.ai) — walk through the live AI-native product: backend, LLM serving layer, infra. This is exactly what Blossom builds. Demo it.

**Red-flag questions:**
- *"You're still in school?"* → "Targeting May 2027 graduation. Happy to discuss timing — for the right role I have flexibility."
- *"Work authorization / sponsorship?"* → "F-1 OPT authorized from May 2027. Long-term I'll need H-1B sponsorship. Can you confirm Blossom's policy? I want to be transparent early."
- *"Only 1.5 years experience?"* → "Google Chrome shipped C++ + TypeScript to 3B users; TiMoto I own the full production AI stack. The depth is above average for the timeline — let the work speak."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active — full Ashby application form visible | Positive |
| JD specificity | Named stack (TypeScript, Python, LLM), team context, realistic requirements | Positive |
| Company funding | $20M Series A confirmed via Fortune + PRNewswire (March 26, 2026) | Positive |
| Salary transparency | $150K–$220K + equity explicitly stated | Positive |
| Hiring volume | 71 open roles on Glassdoor — actively scaling post-Series A | Positive |
| Layoff signals | None found — early growth phase | Positive |
| Reposting | Not seen in scan-history.tsv | Positive |

---

## Keywords extracted

ai-native, LLM-powered apps, TypeScript, Python, production systems, reliability, observability, uptime, performance, scalable systems, end-to-end ownership, autonomy, code reviews, technical mentorship, mental health, psychiatry platform, Series A, AI copilot, full-stack, high-quality code

---

## Machine Summary

```yaml
company: Blossom Health
role: Software Engineer (All Levels)
date: 2026-06-06
url: https://jobs.ashbyhq.com/Blossom-Health/94a6b3b4-01ee-4b2d-ad2b-0c7cda197604
score: 3.8
archetype: Founding/Early-Stage SWE + AI Product Engineering
location: New York City (on-site 5d/wk)
comp_range: "$150K–$220K + equity"
visa_risk: "F-1 — H-1B sponsorship unconfirmed at Series A"
legitimacy: High Confidence
recommendation: "Conditional apply — strong LLM/TypeScript/Python fit; clarify H-1B sponsorship before investing time; relocation to NYC required"
```
