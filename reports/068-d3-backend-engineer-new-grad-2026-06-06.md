# Evaluation: D3 — Backend Engineer, New Grad

**Date:** 2026-06-06
**URL:** https://job-boards.greenhouse.io/embed/job_app?for=d3&token=4915295008
**Archetype:** Founding / Early-Stage Software Engineer + Backend / Distributed Systems Engineer
**Score:** 3.4/5
**Legitimacy:** Proceed with Caution
**PDF:** output/068-d3-backend-engineer-new-grad-harry-nguyen-2026-07-23.pdf

> **Re-verification (2026-07-23):** same posting resurfaced via jobright under a new Greenhouse `jr_id` (`6a534f9bd007ee02d95faf78`, vs. this report's original job ID) — re-checked via Playwright directly on the new URL, still live ~7 weeks after the original evaluation. Title ("Backend Engineer - New Grad"), location (hybrid LA), and full JD body (DomainFi pitch, $25M Series A led by Paradigm, responsibilities/qualifications) are unchanged. Score stands at 3.4/5 — no new gaps or strengths; Web3/blockchain nice-to-have gap and below-walk-away comp assessment both still hold. CV regenerated with the now-fixed LaTeX template (one-line header, working `**bold**` emphasis, corrected `mailto:` link) against the current `cv.md`, which has grown since this report's original evaluation: `output/068-d3-backend-engineer-new-grad-harry-nguyen-2026-07-23.pdf`, 1 page, verified via `pdfinfo`. **New pipeline bug found and fixed during this regeneration:** `build-cv-latex.mjs`'s `buildEducation()` escaped the Education `degree` field in plain-text mode instead of bullet mode, so `**GPA: 3.75/4.0**` markdown rendered as literal asterisks instead of bold — confirmed present in the already-regenerated 011-warp and 063-koahlabs CVs from earlier this session too (both PDFs currently on disk still show the raw `**...**` text; not fixed retroactively, pending Harry's call). Fixed at `build-cv-latex.mjs:22` (added the `'bullet'` escape mode) and reverified via the script's own `--test` self-test plus a full `pdftotext` read of this CV — no other stray markdown found. **Honors line added:** a concurrent session working the same bug independently added an `education[].honors` field to `buildEducation()` while this CV was being built; the first D3 PDF (13:10) predated it and silently dropped Harry's three real academic honors (Presidential Scholarship, Anita Andrew Fellowship, Roxie Alexander Memorial Award), which `cv.md` does carry. Regenerated with `honors` populated — which pushed the CV to 2 pages, so the vLLM bullet was cut as described above to bring it back to 1. Final PDF verified: 1 page, zero stray `**`, Honors line present. Bullet order re-derived from this JD's own priorities rather than reused verbatim from the original Customization Plan (Section E), since `cv.md`'s TiMoto bullets have since changed — the gRPC-deadlock debugging bullet now leads (matches "debug, fix, and improve existing codebases"), followed by the observability-built-from-zero bullet (matches D3's own "zero-to-one" pitch), then the ECS Fargate/Terraform cloud bullet (matches the cloud-platforms nice-to-have), then the post-mortem-practice bullet. The vLLM/ML-serving bullet was **cut entirely** — it is the least relevant TiMoto bullet to this JD (D3's posting never mentions ML; it is backend services, payment integrations, and blockchain connectors), and the page had to give somewhere once the Honors line was added (see below). vLLM/PagedAttention remains visible in the ML & AI Infrastructure skills row, so the capability is not erased from the CV. Skills reordered to lead with Frameworks & Databases and Languages (Node.js/Python/PostgreSQL match the JD directly) ahead of Distributed Systems and ML & AI Infrastructure. Recommendation unchanged — already Applied; no action needed beyond this refresh.

---

## A) Role Summary

| Field | Detail |
|---|---|
| **Archetype** | Founding / Early-Stage SWE + Backend |
| **Domain** | Web2/Web3 domain registrar + blockchain (DomainFi) |
| **Function** | Build backend services, payment integrations, blockchain connectors |
| **Seniority** | Entry-level / New Grad (0–2 YOE) |
| **Location** | Hybrid — Los Angeles, CA |
| **Team size** | ~40 employees (early-stage) |
| **TL;DR** | Early-stage crypto startup building a blockchain for domain names; solid backend fit but Web3 focus diverges from distributed systems / ML infra trajectory; comp likely below walk-away. |

---

## B) Match with CV

| JD Requirement | Harry's Match | CV Source |
|---|---|---|
| Backend development (0–2 YOE) | ✅ Strong — TiMoto (SWE, Sep 2025–Present), Google Chrome intern, Develop for Good | cv.md — all experience |
| Python / Node.js / JS backend | ✅ Django, FastAPI, Node.js | cv.md Skills |
| PostgreSQL / MySQL | ✅ N+1 fix → sub-100ms on 10K+ records | cv.md — Develop for Good |
| Git / collaborative dev | ✅ Chromium 25K+ lines, upstream Pulumi contributions | cv.md — Google + Pulumi |
| CS degree | ✅ Georgia State CS, GPA 3.75, May 2027 | cv.md Education |
| AWS / GCP exposure (nice-to-have) | ✅ AWS ECS Fargate, Terraform, multi-AZ | cv.md — TiMoto |
| Distributed systems coursework / projects (nice-to-have) | ✅ Distributed Systems coursework + TiMoto production + Pulumi Raft/Paxos | cv.md |
| Web3 / blockchain interest (nice-to-have) | ⚠️ No direct blockchain work; Pulumi distributed state is adjacent | cv.md — Pulumi |
| NestJS / GraphQL (nice-to-have) | ❌ Gap — not listed | — |
| Payment integrations | ⚠️ Partial — Develop for Good AWS BaaS; no explicit payments work | — |

**Gaps:**
1. **No blockchain / Web3 experience** — Nice-to-have only ("not required — you'll learn here"). Mitigate with Pulumi distributed state + willingness-to-learn framing.
2. **NestJS / GraphQL** — Minor. Skip in application.
3. **Payment integrations** — Lean into AWS BaaS stateless design; don't over-claim.

**F-1 note:** JD silent on sponsorship. Clarify early — do not skip application for this reason.

---

## C) Level and Strategy

**Level:** Entry-level New Grad — matches Harry's 2027 timeline perfectly.

**Sell strong without lying:**
- Lead with TiMoto "primary engineer, 3-person team" — maps to D3's zero-to-one framing.
- Google Chrome production scale (3B+ users) establishes quality bar.
- gRPC + Terraform + AWS SLOs signals no hand-holding needed.

**If downleveled:** Already entry-level. Accept if comp is fair. Negotiate 6-month review with explicit ownership of a backend service.

---

## D) Comp and Demand

No published salary band. D3 is ~40 people, Series A ($25M, Jan 2025, Paradigm + Coinbase Ventures).

| Source | Data |
|---|---|
| Glassdoor — Backend Engineer US avg | $175K TC (25th–75th: $136K–$230K) |
| Levels.fyi — SWE Los Angeles avg | $175K TC (range $126K–$240K) |
| D3 Principal Blockchain Engineer (web3.career) | $122K–$150K base (senior) |
| Early-stage crypto startup new grad estimate | $110K–$140K base + equity |

**Assessment:** Likely at or below Harry's $140K walk-away. Equity is speculative (crypto/Web3 category, no Series B visibility 17 months post-Series A). Ask for total package on first recruiter call.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---|---|---|---|
| 1 | Summary | Distributed systems / ML infra | Add "full-stack backend ownership and 0→1 delivery" | D3 values breadth + early-stage ownership |
| 2 | TiMoto bullet 1 | "distributed production systems" | Add "shipped from zero to production" | Aligns to D3 zero-to-one framing |
| 3 | Develop for Good | AWS BaaS + N+1 fix | Emphasize stateless JWT scale — payment-adjacent | Bridges to D3 payment integration ask |
| 4 | Pulumi | IaC + Raft/Paxos | Highlight "distributed state synchronization" | Covers Web3/blockchain nice-to-have softly |
| 5 | Skills | Current order | Move Node.js, Python, PostgreSQL higher | ATS match for D3 stack |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Backend services design | TiMoto gRPC layer | Needed inter-service RPC with strict SLOs | Owned design on 3-person team | Designed gRPC protocol + traced deadlock, redesigned call sequencing | sub-50ms p99, 100% eval success rate | Deadlocks come from circular resource acquisition — trace call graphs early |
| 2 | Payment / transaction systems | Develop for Good AWS BaaS | Stateless auth for 500+ concurrent users | Solo backend intern | JWT over session auth, AWS auto-scaling | 500+ concurrent, 90% deploy time cut | JWT simplicity makes horizontal scale trivial |
| 3 | Clean, testable code | Google Chrome IPC | Chrome stable requires 95% coverage | Shipping C++ IPC to 3B users | Wrote IPC with Protobuf, collaborated with senior infra team | Zero regressions to stable | 95% coverage at Chrome scale prevents billions of broken users |
| 4 | Debug existing codebases | Develop for Good N+1 | 3s+ response on large datasets | Fix under time pressure | Diagnosed N+1, redesigned with PostgreSQL indexing | sub-100ms for 10K+ records | Profile before optimizing — N+1 was invisible without query logs |
| 5 | Cross-team collaboration | Google Chrome React | UI state propagation bottleneck | Deliver across 25K+ lines of Chromium | Event-driven observer pattern decoupling UI state | 68% faster feature delivery, 95% coverage | Decoupling state makes the entire codebase move faster |
| 6 | Web3 / blockchain learning | Pulumi open source | Understand distributed consensus in production | Study Raft/Paxos in Pulumi state sync | Analyzed linearizability under concurrent ops and partial failures | Go CLI contributions accepted | Production code teaches consensus better than papers alone |

**Case study:** TiMoto AI — "I owned backend, infra, and ML serving for a live product. Here's what I built, tradeoffs I made, and what's running in production today." Demo timoto.ai.

**Red-flag Qs:**
- *"Web3 experience?"* → "No production blockchain yet, but studied distributed consensus in Pulumi's state layer (Raft/Paxos). I learn fast in production — TiMoto went from zero to live serving stack quickly."
- *"Work authorization?"* → "F-1, OPT eligible. Will need H-1B long-term — happy to discuss sponsorship policy."
- *"Open to hybrid in LA?"* → "Yes, open to hybrid or onsite in LA. Available to relocate."

---

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|---|---|---|
| Apply button | Active ✅ | Positive |
| JD freshness | No date visible; embed is live and responsive | Neutral |
| Description specificity | Names NestJS, GraphQL, blockchain connectors, payments — reasonably specific | Positive |
| Layoffs / freeze | None found; actively hiring ~40 roles | Positive |
| Reposting | Not in scan-history.tsv | Positive |
| Comp transparency | No salary band | Neutral |
| Role-company fit | New grad backend consistent with early-stage growth | Positive |
| Startup risk | Crypto/Web3 niche; Series A Jan 2025 (17 months); no Series B announced | Concerning |

**Context:** Posting appears legitimate. Caution is about startup risk (crypto market volatility, runway visibility) — not ghost job signals.

---

## Keywords Extracted

backend, Node.js, Python, PostgreSQL, MySQL, distributed systems, blockchain, Web3, DeFi, payment integrations, NestJS, GraphQL, cloud, AWS, REST API, Git, code review, domain registrar, marketplace, crypto payments, entry-level, new grad

---

## Machine Summary

```yaml
company: D3
role: Backend Engineer - New Grad
score: 3.4
archetype: Founding/Early-Stage SWE + Backend
location: Los Angeles, CA (Hybrid)
seniority: New Grad
sponsorship: unconfirmed
recommendation: skip
legitimacy: Proceed with Caution
date: 2026-06-06
```

---

> **Re-application CV refresh (2026-08-05):** Harry wants to re-apply to this posting (resurfaced again via jobright, same underlying job — see the 2026-08-05 dedup check against token `4915295008`, still the identical D3 req). Regenerated the CV against `templates/cv-template.tex` now that its spacing bug is fixed (see [modes/_custom.md](../modes/_custom.md) house rule, 2026-08-05): **all content restored, nothing cut.** The 2026-07-23 regeneration had dropped the vLLM/PagedAttention bullet entirely to fit 1 page under the old, space-wasting template — that bullet is back now, last in the TiMoto AI block (still the least D3-relevant bullet, since this JD is backend/payments/blockchain, not ML, but per the new house rule content no longer gets cut to solve a formatting problem). Bullet order otherwise unchanged from the 2026-07-23 tailoring (gRPC deadlock leads, then observability, then ECS Fargate/Terraform), and Skills still lead with Frameworks & Databases and Languages ahead of Distributed Systems/ML infra to match D3's Node.js/Python/PostgreSQL stack. Both Personal Projects (Pulumi and NextStep) present. New PDF: `output/068-d3-backend-engineer-new-grad-harry-nguyen-2026-08-05.pdf` — 1 page, verified (18/18 items, 0 stray asterisks, correct links). Score and recommendation unchanged (3.4/5 — Web3/blockchain nice-to-have gap and below-walk-away comp both still hold); this is a CV refresh for a re-application, not a re-evaluation.

## Addendum 2026-10-09 (checker re-run, fresh CV)

Re-pasted with a checker result (7.5, 7/7 shown keywords). Greenhouse job 4915295008 is still live on the API, but it was first published 2025-09-09 and last updated 2025-12-20, so it is a year old; the row is already Applied. New CV `output/068-harry-nguyen-resume-2026-10-09.pdf` carries Backend Development, JavaScript, Node.js, Python and PostgreSQL. Real gap, not added: MySQL (you have PostgreSQL); GraphQL also not on the CV.

