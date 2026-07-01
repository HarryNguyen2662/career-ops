# Evaluation: Notion — Software Engineer, New Grad

**Date:** 2026-06-04
**URL:** https://jobs.ashbyhq.com/notion/a6311f97-4850-4674-a5f3-d9fe5f6f2555
**Archetype:** Full-Stack / Product Engineer (New Grad) — adjacent to Backend/Systems
**Score:** 3.7/5
**Legitimacy:** High Confidence
**PDF:** pending (LaTeX generated)

---

## A) Role Summary

| Field | Value |
|-------|-------|
| Archetype detected | Full-Stack / Product Engineer (web-leaning), adjacent to Backend/Distributed Systems |
| Domain | Productivity SaaS / collaborative AI workspace |
| Function | Build product features end-to-end (conception → research → implementation → maintenance) |
| Seniority | New Grad (University dept); start full-time before July 27, 2026 |
| Remote | Hybrid — San Francisco, CA (`#LI-Onsite` tag despite "Hybrid" label) |
| Team size | Pooled new-grad req — recruiter places you on a team post-offer |
| Comp | $126,000–$146,000 base (SF/NYC) + equity + benefits |
| TL;DR | Generalist new-grad SWE building core Notion product features in a React/TypeScript/Node.js/Postgres stack, with explicit emphasis on AI-assisted development (Claude Code, Codex). |

This is the **general** new-grad req, distinct from the already-tracked "Software Engineer, New Grad (AI)" (`7e6dc7fe...`). This one is broader and more frontend/product-leaning.

## B) Match with CV

| JD Requirement | CV Evidence | Match |
|----------------|-------------|-------|
| Bachelor's/master's in CS, start before Jul 27 2026 | Georgia State BS CS, **Expected May 2027** | ⚠️ Partial — grad date is AFTER the stated start window |
| Previous internship experience | Google Chrome (May–Aug 2025), Develop for Good (2024) | ✅ Strong |
| Proficiency in TypeScript, Node.js, or Python | cv.md Skills: "TypeScript, Python… Node.js"; Chrome "event-driven TypeScript/React system" | ✅ Strong |
| Passion for web apps; HTML/CSS/JS + React | Chrome "TypeScript/React… observer pattern… 25K+ lines Chromium"; Skills: React, Node.js | ✅ Direct |
| Familiarity with backend systems / data model | TiMoto "gRPC, PostgreSQL, ML serving"; DfG "PostgreSQL indexing, N+1 fix" | ✅ Strong |
| Postgres / MySQL / MongoDB a plus | Skills: "PostgreSQL, Redis, MongoDB"; DfG sub-100ms Postgres | ✅ Direct |
| Stay current with AI dev tools (Codex, Claude Code) | Skills: "AI Dev Tools: Claude Code, GitHub Copilot, Codex, Cursor" | ✅ Direct hit |
| Elasticsearch (nice-to-have) | Not on CV | ❌ Gap (minor) |
| Own the outcome / initiative | TiMoto "primary engineer on 3-person team… end-to-end ownership" | ✅ Strong |

**Gaps:**
1. **Grad date vs start window (July 27, 2026)** — *Hard-ish blocker.* Harry graduates May 2027, ~10 months after the stated full-time start. This req is for candidates who can start by mid-2026. Mitigation: per apply policy, still apply and clarify with recruiter whether a 2027 cohort exists or whether this maps to the intern/return pipeline. Notion also runs a separate Intern (Summer/Fall 2026) and a New Grad (AI) req — the recruiter may redirect. Flag, do not block.
2. **Elasticsearch** — nice-to-have only. Mitigate: name Postgres indexing + search-adjacent work (Chrome trie search, settings index). Not a real blocker.
3. **Frontend depth** — JD leans web UI ("Passion for web applications," React UIs for big audiences). Harry's strength is backend/systems; frontend proof is the Chrome TS/React work. Mitigate: lead with Chromium React + observer-pattern bullet to show UI credibility, then bridge to backend.

## C) Level and Strategy

- **JD level:** New Grad (L3 / entry). **Candidate natural level:** New grad — aligned.
- **Sell without lying:** Position as a **production-minded generalist** — "shipped TypeScript/React to Chrome stable (3B+ users) AND owns backend+infra+ML in production at TiMoto." That breadth (frontend at Google + backend/Postgres at TiMoto/DfG) is exactly the full-stack generalist Notion's pooled req wants. Lead the AI-dev-tools fluency (Claude Code/Codex) hard — the JD calls it out explicitly and it's a literal skill-line match.
- **If downleveled / redirected:** This is already entry-level. The real risk is timing, not level. If recruiter says start date is firm, ask to be routed to the **2027 new-grad cohort** or the **Summer 2026 internship** as a bridge.

## D) Comp and Demand

| Metric | Value | Source |
|--------|-------|--------|
| JD stated range (SF/NYC) | **$126K–$146K base** + equity + benefits | JD posting |
| Notion L3 SWE median TC | ~$346K (skewed by RSU/refresh; first-year new-grad lower) | Levels.fyi |
| Notion SF SWE range | $177K–$855K (L1→L5) | Levels.fyi |
| Target range | $150K–200K total comp | profile.yml |
| Demand | High — Notion actively hiring eng/product, no major 2026 layoffs found | WebSearch |

Base alone ($126K–146K) sits below the $150K min on base, but **base + Notion equity** realistically clears the $150K+ TC target — Levels.fyi entry data supports a strong new-grad package. Comp is competitive for new grad. Score this dimension ~4.0.

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | Distributed-systems lead | Add "ships full-stack: TypeScript/React at Chrome scale + backend/Postgres in prod" | JD wants web-app generalist |
| 2 | Skills order | DistSys first | Surface TypeScript, React, Node.js, Postgres earlier | Direct JD keyword match |
| 3 | AI Dev Tools | Last row | Keep but lean on it in cover/answers | JD names Codex + Claude Code explicitly |
| 4 | Chrome bullet | IPC-first | Lead with TS/React/observer + 25K LOC Chromium | Proves UI credibility for big audiences |
| 5 | TiMoto | Infra-heavy | Add Django/Postgres "data model" framing | JD wants "UI → data model" understanding |

**LinkedIn:** (1) headline add "full-stack"; (2) feature Postgres/React; (3) pin TiMoto product; (4) AI-tools fluency in About; (5) GSU + Google + TiMoto banner.

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|----------------|--------------|---|---|---|---|------------|
| 1 | Build web features for big audiences | Chrome TS/React observer system | Slow feature delivery in Chromium UI | Decouple UI state propagation | Event-driven observer pattern, 25K+ LOC | 68% faster delivery, 95% coverage | Decoupling state early pays off at scale |
| 2 | UI → data model understanding | TiMoto Django + Postgres + gRPC | Needed reliable data path under concurrency | End-to-end service layer | gRPC + Postgres, deadlock fix | sub-50ms p99, 100% eval success | Trace shared-resource acquisition before optimizing |
| 3 | Performance/reliability polish | Chrome lock-free trie | Settings nav p99 at 1,200ms | Cut latency without regressions | Lock-free concurrent trie, removed mutex | 96% latency cut, zero regressions | Measure the hot path before touching it |
| 4 | Backend/db familiarity (Postgres) | DfG N+1 fix | 3s+ response on large datasets | Sub-100ms target | Postgres indexing redesign | sub-100ms on 10K+ records | N+1 hides until data grows |
| 5 | Own the outcome / initiative | TiMoto primary engineer | 3-person team, no infra owner | Own backend+infra+ML | Terraform, circuit breakers, on-call | 99.9% uptime, 44% cost cut | Ownership means runbooks + post-mortems, not just code |
| 6 | AI as a collaborator | AI dev-tools fluency | Ship faster as small team | Use Claude Code/Codex in real workflow | AI-assisted dev across backend/infra | Faster delivery on 3-person team | AI is a force-multiplier, not a novelty |
| 7 | Internal tooling / scripts | DfG CI/CD automation | Manual deploys slow | Automate pipeline | GitHub Actions CI/CD | 90% deploy-time reduction | Automate the repetitive path early |

**Recommended case study:** TiMoto (timoto.ai) — live product showing end-to-end ownership and the "humans + AI building together" theme Notion cares about.

**Red-flag Qs:** "You graduate May 2027 — can you start by July 2026?" → "Not for a mid-2026 start; I'm targeting the 2027 new-grad cycle, and I'd love to be routed there or to the Summer 2026 internship as a bridge." "Visa?" → F-1 OPT/CPT eligible; H-1B sponsorship long-term.

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active, links to `/application` | Positive |
| JD specificity | Names React, TypeScript, Node.js, Postgres, Elasticsearch, Codex, Claude Code; concrete example tasks | Positive |
| Salary transparency | $126K–146K disclosed (CA/NY law) | Positive |
| Company hiring | Notion actively hiring eng/new-grad; no major 2026 layoffs found | Positive |
| Reposting | Distinct URL from other Notion reqs; not a repost | Neutral |
| Start-date constraint | "Before July 27, 2026" — narrows eligibility but legitimate cohort signal | Neutral |
| Pooled req | Generic "join across several teams" — normal for new-grad pipeline | Neutral |

**Context:** University/new-grad pooled reqs are intentionally broad — not a ghost-job signal. Real, active opening.

---

## Keywords extracted

Software Engineer, New Grad, TypeScript, Node.js, Python, React, HTML, CSS, JavaScript, Postgres, MySQL, MongoDB, Elasticsearch, web applications, backend systems, data model, Claude Code, Codex, AI-assisted development, product features, performance, reliability, internal tools, San Francisco, hybrid

---

## Notes / Red Flags

- **Start-date mismatch (primary flag):** JD requires start before **July 27, 2026**; Harry graduates **May 2027**. This req targets earlier-start candidates. Per apply policy, still apply and ask the recruiter to route to the 2027 cohort or Summer 2026 internship. Do not treat as a hard block.
- **`#LI-Onsite` tag** despite "Hybrid" label — confirm in-office cadence with recruiter.
- **F-1 sponsorship** — clarify early; not a blocker.
- Score **3.7/5** — decent fit (strong skills + AI-tools match) held back by the timing mismatch and frontend-lean vs Harry's backend/systems core. Below 4.0: apply with eyes open, leading the timing clarification.
