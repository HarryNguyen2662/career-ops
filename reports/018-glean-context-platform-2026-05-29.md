# 018 — Glean — Software Engineer, Context Platform

**Date:** 2026-05-29
**Score:** 4.2/5
**URL:** https://job-boards.greenhouse.io/embed/job_app?for=gleanwork&token=4638008005
**PDF:** ✅
**Legitimacy:** High Confidence

---

## Machine Summary

```yaml
company: Glean
role: Software Engineer, Context Platform
date: 2026-05-29
score: 4.2
status: Evaluated
level: New Grad / Entry-level (1+ year experience; explicit new-grad adjacent)
location: Mountain View, CA — Hybrid (Mon/Wed/Fri onsite, 3-4 days/week)
comp_base: "$140,000–$265,000 USD"
comp_equity: "Equity mentioned — Series D startup ($4.6B valuation 2024)"
archetype: "Platform / Developer Tools Engineer (SDK, REST API, MCP, OAuth2)"
graduation_timing_risk: none — entry-level, no graduation date restriction
visa_risk: medium — Glean Series D; no ITAR; sponsorship unconfirmed but likely given active new-grad hiring
apply_rec: "Apply — strong Go + TypeScript + Python + REST API stack match; $140K–$265K comp floor meets minimum; SDK/API/platform work aligns with Harry's Open Source/Developer Tools archetype; confirm H-1B sponsorship and relocation plan before submitting"
```

---

## Block A — Match with CV

**Score: 3.8/5**

| JD Requirement | Harry's Evidence |
|---|---|
| **Go (Golang)** — primary language | Pulumi open source: Go CLI features and bug fixes for multi-cloud provisioning; 24.4K★ repo under active maintainer review |
| **TypeScript** — secondary | Google Chrome: TypeScript/React observer system across 25K+ lines of Chromium at 95% test coverage; 68% feature delivery acceleration |
| **Python** — secondary | TiMoto: Python/Django REST backend, FastAPI; vLLM inference stack |
| **REST APIs** | TiMoto: Django REST backend; Develop for Good: BaaS with JWT-based stateless auth on AWS |
| **gRPC / inter-service communication** | TiMoto: gRPC inter-service layer; production deadlock diagnosed and fixed at sub-50ms p99 |
| **Client libraries / SDK development** | Pulumi: CLI = developer-facing SDK; Go CLI feature development directly analogous to client library engineering |
| **Cloud-native (GCP/AWS/Azure)** | TiMoto: multi-AZ ECS Fargate + Terraform + Terraform IaC; Develop for Good: AWS BaaS (EC2, S3, RDS, auto-scaling) |
| **MCP server integration** | Not explicitly in CV — Glean integrates with MCP ecosystem; indirect signal via career-ops tooling, but no direct project evidence |
| **OAuth2/OIDC** | Not explicit in CV — Develop for Good BaaS uses JWT (OAuth2 stateless token pattern) but not full OAuth2/OIDC implementation. This is the clearest gap. |
| **Agent integrations / AI context** | TiMoto vLLM inference with PagedAttention; LLM-as-a-judge evaluation patterns; context serving directly relevant to Glean's context engine |
| **1+ year industry experience** | 3 internships (~11 months combined): Google (3mo), D4G (4mo), CoderPush (4mo) + ongoing TiMoto; borderline on literal count but Google quality more than compensates |

**Strengths:** Go (Pulumi) + TypeScript (Chrome) + Python (TiMoto) + REST APIs + gRPC = exact preferred stack. Pulumi CLI contributions directly map to SDK/developer tool work. TiMoto as a context/inference serving platform is thematically aligned.

**Gaps:** No explicit OAuth2/OIDC implementation (JWT is adjacent). No MCP server build experience. SDK development inferred from CLI work rather than explicit client library shipping.

---

## Block B — North Star Alignment

**Score: 4.5/5**

Glean's Context Platform team builds the core developer-facing layer: SDKs, REST APIs, MCP servers, and OAuth2/OIDC integrations that connect Glean's context engine to enterprise apps (Salesforce, Workday, Confluence, Jira) and AI agents.

**Where it aligns:**
- **Open Source / Developer Tools archetype** — Glean Context Platform is exactly "developer tools engineer": SDKs, client libraries, API contracts. Harry's Pulumi open source contributor track record is direct evidence of this archetype.
- **Platform primitives** — Harry's background (gRPC IPC at Google Chrome, TiMoto multi-service architecture) shows systems credibility for building infrastructure others build on — the exact skill profile for a platform team.
- **AI context engine** — TiMoto is a context-serving platform (vLLM inference + session persistence). Framing it as a context API platform maps directly to Glean's mission.
- **Golang primary** — Glean's Go preference matched by Pulumi contributions; Go is Harry's strongest open source language.
- **Series D, AI-first** — Glean ($4.6B, 2024) is post-product-market-fit with clear revenue (enterprise search + AI context); career trajectory here is systems depth at an AI platform company — Harry's North Star.

**Where it misses:**
- **OAuth2/OIDC depth** — Glean's integrations with enterprise apps involve complex auth flows (SSO, SCIM, OAuth2 delegated access). Harry has JWT but not full OAuth2/OIDC server-side implementation.
- **Enterprise integration domain** — connecting to Salesforce/Workday/Confluence APIs is enterprise software engineering. Harry's background is consumer-scale systems, not enterprise integration patterns.
- **Mountain View hybrid** — onsite 3-4 days/week requires Bay Area relocation from Atlanta. Harry is open to relocation but it adds friction.

**Career trajectory:** Joining Glean Context Platform builds: (1) SDK engineering credibility, (2) AI platform systems depth, (3) enterprise Go experience. All three are premium career assets in the ML/AI infrastructure space. This role is a strong North Star move.

---

## Block C — Compensation

**Score: 4.5/5**

| Component | Value | vs Target |
|---|---|---|
| Base | $140,000–$265,000 | **Floor exactly at walk-away minimum ($140K). Mid-band $200K+ exceeds target.** |
| Equity | Mentioned; Series D ($4.6B val, 2024) | Meaningful but illiquid until IPO/acquisition |
| Benefits | Standard startup-scale (medical/dental/vision, 401k) | Adequate |

**Year-1 TC estimate (mid-band):**
- Base: ~$175K + equity: Series D grants for SWE new grad typically $50K–$120K/4yr (~$12K–$30K/yr vested)
- Year-1 TC: ~$185K–$205K (depending on equity tranche)

**Comp ceiling ($265K) is the highest posted for any full-time role in Harry's tracker.** Even the floor ($140K) matches the walk-away. Negotiate toward $170K+ base — frame with Google Chrome FAANG benchmark.

**Equity risk:** Series D with $4.6B valuation is past the "moonshot" range; an IPO is plausible within 3–5 years. Not liquid like Amazon RSUs, but not startup lottery either.

---

## Block D — Cultural Signals

**Score: 3.8/5**

**Positive signals:**
- **AI-first culture** — Glean explicitly uses AI throughout their engineering process; they require AI tools assessment in interviews. Harry's vLLM/AI infrastructure background is culturally native.
- **Technical rigor** — Glean is known for a high hiring bar and systems-thinking culture; aligns with Harry's distributed systems depth.
- **Series D stability** — $4.6B valuation, enterprise revenue base; not pre-product-market-fit risk.
- **Platform team** — SDK and API platform work tends to attract strong engineers; peer quality is a career accelerant.
- **No ITAR/defense** — Clean sponsorship path (no citizenship restrictions).

**Friction signals:**
- **Mountain View hybrid (3-4 days/week)** — Harry is in Atlanta. Relocation to Bay Area is required. This is the biggest cultural friction point — it's a significant life change for a 2027 grad who may have coursework obligations until May 2027.
- **Start date vs graduation** — Harry graduates May 2027. Full-time start before that is not possible unless role allows deferred start. Need to confirm Glean accepts May 2027 start or can accommodate part-time/deferred.
- **H-1B sponsorship** — Glean Series D; no ITAR. Past record of sponsoring not confirmed in tracker. Likely at this funding stage but must verify.

---

## Block E — Red Flags

| Flag | Severity | Action |
|---|---|---|
| **Mountain View hybrid onsite** — 3-4 days/week (Mon/Wed/Fri) requires full Bay Area relocation | HIGH | Harry confirmed open to relocation. Key question: can he start May 2027 after graduation, or does Glean need a 2026 start? Confirm this before submitting. If they need 2026 start, this is disqualifying for a full-time role. |
| **H-1B sponsorship unconfirmed** — Glean is Series D but record unclear | MEDIUM | Check Glean's LCA filings on DoL OFLC database. Series D with enterprise revenue base = likely to sponsor; flag to recruiter in first screen. Do not mark as blocking — verify. |
| **OAuth2/OIDC gap** — not implemented end-to-end in Harry's projects | MEDIUM | Mitigable: Develop for Good JWT auth demonstrates the pattern; Glean onboarding will teach enterprise-specific flows. Frame as "familiar with stateless auth patterns; ready to go deep on enterprise OAuth2/OIDC." Do not overclaim. |
| **Experience floor (1+ year)** — Harry has ~11 months internship total | LOW | Google Chrome internship quality is graduate-level; 3 internships including FAANG more than compensates for literal month count. Not a blocking concern. |
| **MCP server experience** — no direct evidence in CV | LOW | Do not fabricate. Omit from resume. In application: mention TiMoto as context serving platform and AI agent infrastructure as directional evidence. Frame Pulumi CLI contributions as SDK/API discipline. |

---

## Block F — Global Score

**4.2/5**

| Dimension | Score | Driver |
|---|---|---|
| CV Match | 3.8 | Go + TypeScript + Python + REST/gRPC strong; OAuth2/OIDC gap; SDK inferred via Pulumi |
| North Star | 4.5 | Platform + SDK + AI context engine = primary archetype match; Go-first shop |
| Compensation | 4.5 | $140K–$265K floor meets minimum; mid-band exceeds target; Series D equity |
| Culture | 3.8 | AI-first; Mountain View relocation required; H-1B unconfirmed; stable Series D |
| Red flag adj. | -0.4 | Relocation friction (-0.2), OAuth2 gap (-0.1), sponsorship unconfirmed (-0.1) |
| **Global** | **4.2** | |

**Recommendation: Apply.**

Score 4.2/5 — above the 4.0 threshold. This is Harry's second-strongest full-time role in the tracker after Giga (#15, 4.3/5).

**Why apply:**
1. **$140K–$265K base** — floor meets walk-away exactly; ceiling is highest in tracker
2. **Platform/SDK/Go** — direct archetype match for Open Source / Developer Tools Engineer
3. **AI-first company** — TiMoto + vLLM experience is culturally native to Glean's context engine
4. **Pulumi → SDK credibility** — Go CLI contribution to a 24.4K★ project is strong SDK signal
5. **Series D stability** — not pre-revenue lottery; real enterprise customers, real equity value

**Before submitting:**
1. Confirm Glean accepts May 2027 start date (do not apply if they need 2026 start)
2. Ask recruiter about H-1B sponsorship in first screen
3. Anchor comp at $170K+ base (Google Chrome FAANG benchmark)
4. Prepare "AI tools" answer — this is their signal question

---

## Block G — Posting Legitimacy

**Tier: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Posting live | Active Greenhouse form (`gleanwork` slug) with full JD and fields | Positive |
| Salary transparency | $140,000–$265,000 — explicit range | Positive |
| Company verification | Glean — Series D enterprise AI company, $4.6B valuation (2024) | Positive |
| Company health | Series D with enterprise revenue base (Google Workspace-style search) | Positive |
| JD specificity | Named platform primitives: SDKs, REST APIs, MCP servers, OAuth2/OIDC, agent integrations | Positive |
| ATS | Greenhouse `gleanwork` board — verified employer slug | Positive |

Real posting at a known, well-funded company. No ghost signals.

---

## Application Form Answers

### Standard Fields
- **First Name**: Harry
- **Last Name**: Nguyen
- **Email**: harrynguyenswe@gmail.com
- **Phone**: +1 470-667-9000
- **LinkedIn**: https://www.linkedin.com/in/harrynguyen26/
- **Website**: https://timoto.ai

### Custom Fields

**"Are you willing and able to commit to the hybrid policy?" (3-4 days/week Mountain View)**
> Yes — I am open to relocating to the Bay Area. I am currently finishing my junior year at Georgia State (Expected May 2027) and am prepared to make the move for the right role. I understand the Mon/Wed/Fri schedule and am fully committed to the hybrid policy.

**"Do you know anyone currently at Glean?"**
> No.

**"How did you hear about Glean?"**
> Jobright.ai

**"Total years of relevant experience"**
> 1

*(3 internships totaling ~11 months + ongoing TiMoto: Google Chrome SWE intern, Develop for Good, CoderPush. Rounds to 1 year.)*

**"What AI tools are you currently using today and how are you using them?"**
> Daily workflow: Claude (Anthropic) for architecture review, system design reasoning, and code review at design-doc level. GitHub Copilot for Go, TypeScript, and Python code completion. Cursor for AI-assisted refactoring in my TiMoto codebase.

> Beyond the tools themselves: I build AI infrastructure. TiMoto runs a vLLM inference stack with PagedAttention to serve contextual AI responses under concurrent load — I've debugged KV cache memory pressure, tuned continuous batching, and traced a production gRPC deadlock to circular resource acquisition. I use LLM-as-a-judge evaluation pipelines to benchmark model outputs systematically. AI tools aren't just in my workflow — they're what I ship.
