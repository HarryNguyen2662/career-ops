# User Profile Context -- career-ops

---

## HARD RULES (never override)

### Profile Rules

| Rule | Value |
|------|-------|
| **Email** | `nguyenharry2662@gmail.com` — NEVER use `harry.nguyen@timoto.ai` or `harrynguyenswe@gmail.com` |
| **TiMoto framing** | "primary engineer on 3-person team" — NEVER "sole engineer" |
| **Graduation** | May 2027, Georgia State CS, GPA 3.75 |
| **Visa** | F-1, OPT eligible May 2027, H-1B sponsorship needed long-term |

### LaTeX Resume Rules

| Rule | Detail |
|------|--------|
| **En-dash** | Use `--` not `---` or `—` |
| **Abbreviate** | `K8s` not `Kubernetes`; `IaC` not `Infrastructure-as-Code` |
| **Tech tags** | Max 6 tags per `\resumeProjectHeading` line |
| **AI Dev Tools** | ALWAYS include `\resumeSkillHeading{AI Dev Tools}{Claude Code, GitHub Copilot, Codex, Cursor}` as last skills row |
| **Compiler compat** | Do NOT include `\input{glyphtounicode}` or `\pdfgentounicode=1` — breaks tectonic |

### Pipeline Rules

| Rule | Detail |
|------|--------|
| **CV threshold** | Generate LaTeX CV for any score ≥ 3.0 |
| **Apply policy** | Apply to everything; warn red flags but never block application |
| **Visa warnings** | Note sponsorship risk, never skip solely for that reason |

### Red Flags (warn, never block)

- "No sponsorship" language → note, still apply, ask recruiter early
- Graduation year mismatch (JD wants 2025/2026, Harry is 2027) → disclose proactively in cover/form
- YOE requirement exceeded → note, frame production ownership as substitute
- Comp below $140K floor → note, suggest raising in negotiation

### Contacts Already Reached Out

| Person | Company | Status |
|--------|---------|--------|
| Ana Echeverria | CloudKitchens | Sent March (generic); follow-up drafted |
| Ren Young | Cursor/Anysphere | Sent (recruiter) |
| Alexey Kozy | Cursor/Anysphere | Drafted (peer/infra) |
| Albert Slepak | Cursor | Sent (referral request) |
| Less Wright | Cursor | Drafted (referral, ex-Meta PyTorch) |

---



## Your Target Roles

**North Star (from profile.yml):** New grad / intern SWE, backend & distributed systems, systems software, platform & cloud infra, ML infra, AI/ML serving, SRE, performance engineering.


| Archetype                                           | Thematic axes                                                                       | What they buy                                                              |
| --------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Backend / Distributed Systems Engineer**          | gRPC, Protobuf, exactly-once, event-driven APIs, PostgreSQL/Redis/DynamoDB at scale | Someone who ships reliable, fast backends under concurrency                |
| **Systems Software Engineer**                       | C++, IPC, lock-free structures, Chromium-scale performance, 95%+ test coverage      | Someone who optimizes core paths for billions of users                     |
| **ML / AI Infrastructure Engineer**                 | vLLM, PagedAttention, continuous batching, inference SLOs, GPU/memory efficiency    | Someone who runs LLM workloads in production without OOM/latency surprises |
| **Site Reliability Engineer**                       | Multi-AZ, circuit breakers, health checks, auto-rollback, uptime/cost tradeoffs     | Someone who keeps prod healthy and cheap                                   |
| **Performance Engineer**                            | p99 latency, profiling, hot partitions, N+1 elimination, mutex contention           | Someone who finds bottlenecks and proves impact with numbers               |
| **Platform / Cloud Infrastructure Engineer**        | Terraform IaC, ECS Fargate, CI/CD, JWT/stateless scale, AWS primitives              | Someone who owns cloud topology and deploy pipelines                       |
| **Cloud / DevOps Engineer**                         | GitHub Actions, auto-scaling, observability-minded ops                              | Someone who automates deploy and scale                                     |
| **AI/ML Engineer (Inference & Serving)**            | LoRA/QLoRA, quantization, evaluation pipelines, Django/FastAPI serving layer        | Someone who connects models to product APIs                                |
| **Backend Engineer (Payments & High-Throughput)**   | Idempotent APIs, Redis cache, exponential backoff, partition keys                   | Someone who builds money paths safely under partitions                     |
| **Open Source / Developer Tools Engineer**          | Go CLI, multi-cloud IaC, Raft/Paxos literacy                                        | Someone who contributes upstream with rigor                                |
| **Founding / Early-Stage Software Engineer**        | End-to-end ownership, cost-conscious infra, solo delivery                           | Someone who builds 0→1 with production discipline                          |
| **Full-Stack Engineer** *(adjacent)*                | React/TypeScript UI, Django REST, observer-pattern state                            | Breadth when role is product-facing, not primary pitch                     |
| **Browser / Client Platform Engineer** *(adjacent)* | Chromium, TypeScript/React in browser stack                                         | Chrome internship proof when JD is client/platform                         |


## Your Adaptive Framing


| If the role is...               | Emphasize about you...                                                                                              | Proof point sources                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Backend / Distributed Systems   | gRPC + Protobuf IPC; exactly-once payment APIs; DynamoDB partition redesign; PostgreSQL indexing                    | cv.md — Google IPC, CoderPush payments, Develop for Good DB |
| Systems Software                | C++ at scale; lock-free trie; sub-50ms p99; design docs + senior review in Chrome stable                            | cv.md — Google Chrome bullets                               |
| ML / AI Infrastructure          | Primary engineer on TiMoto serving stack; vLLM/PagedAttention; deadlock fix under concurrent gRPC; sub-50ms p99 inference | cv.md — TiMoto experience; profile.yml proof_points            |
| SRE / Platform                  | 99.9% uptime; circuit breaker + auto-rollback; multi-AZ ECS; Terraform; 44% cost cut                                | cv.md — TiMoto infra bullet                                 |
| Performance                     | Quantified latency wins (96% settings nav, sub-100ms queries, 30% DynamoDB throughput)                              | cv.md — Google, Develop for Good, CoderPush                 |
| Cloud / DevOps                  | AWS BaaS, JWT horizontal scale, GitHub Actions 90% deploy time reduction, ECS/Terraform                             | cv.md — Develop for Good + TiMoto                           |
| AI/ML (product-facing)          | End-to-end AI evaluation product; model serving choices with tradeoff narrative                                     | cv.md — TiMoto; timoto.ai                                   |
| Payments / fintech backend      | Idempotency, Redis 85% hit rate, hot-partition diagnosis                                                            | cv.md — CoderPush                                           |
| Open Source / DevTools          | Pulumi Go CLI contributions; Raft/Paxos study for distributed state                                                 | cv.md — Pulumi project                                      |
| Founding / early-stage          | Primary engineer for backend + infra + ML on 3-person team; ships with SLOs and cost targets ($40–60/mo)            | cv.md — TiMoto; profile.yml                                 |
| Full-Stack *(adjacent)*         | React/observer pattern in Chromium; Django REST backend                                                             | cv.md — Google + TiMoto                                     |
| Browser / platform *(adjacent)* | 25K+ lines Chromium, 68% feature delivery acceleration, 95% coverage                                                | cv.md — Google Chrome                                       |


**Default lead story:** CS @ Georgia State (GPA 3.75, May 2027) + **Google Chrome intern** (production C++/TS) + **TiMoto AI Software Engineer** (primary engineer, distributed production ML serving). Not "student who took courses" — **engineer who ships to stable and owns production**.

## Your Exit Narrative

Use **config/profile.yml → narrative.exit_story** to frame ALL content:

> Primary engineer for backend, cloud infra, and ML serving at TiMoto AI (3-person team) — owns distributed production systems: vLLM, gRPC, Django, AWS/Terraform, 99.9% uptime. Google internship shipped C++ IPC and settings perf work to billions of Chrome users. Prior internship at Develop for Good on AWS, PostgreSQL, and DynamoDB at scale.

**In PDF summaries:** Bridge **coursework foundation** (Distributed Systems, OS, DB, Networks) → **internship production impact** → **target role** (backend/systems/ML infra).

**In STAR stories:** Prefer quantified bullets from cv.md — never invent metrics. Anchor stories:

1. **Google Chrome** — IPC/Protobuf choice, lock-free trie, or Chromium React delivery
2. **TiMoto** — gRPC deadlock fix, vLLM selection, or Terraform/circuit breaker uptime
3. **Develop for Good** — N+1 → sub-100ms or AWS scale-out

**In draft answers:** First paragraph = headline from profile.yml + one proof point matched to company/product.

## Your Cross-cutting Advantage

Frame as **"Production-minded new grad: ships at Chrome scale and leads distributed ML infra in production."**

Signature moves:

- **Measure then fix** — always cite p99, throughput, % reduction, or cost
- **Explicit tradeoffs** — Protobuf vs custom serialization, JWT vs sessions, vLLM vs naive inference, PagedAttention vs OOM
- **Correctness under failure** — exactly-once, circuit breakers, linearizability/Raft literacy
- **High bar for quality** — 95% test coverage norm from Chrome team

## Your Portfolio / Demo


| Asset                    | URL                                    | When to share                                          |
| ------------------------ | -------------------------------------- | ------------------------------------------------------ |
| TiMoto AI (live product) | [https://timoto.ai](https://timoto.ai) | ML infra, full-stack, founding/early-stage, AI product |
| GitHub                   | github.com/HarryNguyen2662             | All technical roles                                    |
| Pulumi upstream          | github.com/pulumi/pulumi               | Open source, platform, IaC roles                       |


Offer TiMoto demo walkthrough in applications for ML serving, platform, or founder-track roles.

## Your Comp Targets

From **config/profile.yml** (verify with Levels.fyi / Glassdoor per company tier):


| Field               | Value                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| Target range        | **$150K–200K** total comp (USD)                                                                   |
| Minimum / walk-away | **$140K**                                                                                         |
| Level               | New grad / intern (2027) — calibrate expectations: top-tier new grad vs startup may differ widely |


**Evaluation guidance:**

- Frame comp by **role title + level + location**, not skill list
- For **intern** roles: use intern bands, not new-grad TC
- For **F-1**: note sponsorship status in Block B, but **do not skip applications** solely because sponsorship is unclear or absent — candidate still applies and asks during process
- Contractor rates N/A unless JD is contract

## Your Negotiation Scripts

**Salary expectations (new grad):**

> "For this role and level I'm targeting **$150K–200K** total compensation based on market data for [backend / systems / ML infra] new grads. I'm flexible on base vs equity/bonus — what matters is the full package and growth path."

**When offered below minimum ($140K):**

> "I'm comparing offers in a higher band for similar scope. I'm very interested in [company] because of [specific team/product]. Is there room to move toward **$150K+** total comp, or strengthen the equity/bonus component?"

**Sponsorship (F-1 — always clarify early):**

> "I'm on F-1 status and will need **work authorization support** (CPT/OPT now; H-1B sponsorship for long-term). Can you confirm the company's sponsorship policy for this role?"

**Geographic / remote (profile: open to onsite, remote, hybrid, relocation):**

> "I'm based in Atlanta (ET) and open to **onsite, hybrid, or remote** for the right team. For hybrid roles I can align to the team's in-office cadence."

**Do not use** "output-based not location-based" pushback unless employer is clearly underpaying remote vs onsite for identical scope — as a new grad, flexibility on location can be a strength.

## Your Location Policy

From **config/profile.yml**:


| Field               | Value                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| Base                | Atlanta, GA — **America/New_York**                                                                 |
| Country             | United States                                                                                      |
| Visa                | **F-1** — prefer sponsorship long-term; **still apply** even when JD silent or says no sponsorship |
| Flexibility         | Onsite, remote, or hybrid; **open to relocation** for strong roles                                 |
| Onsite availability | Up to **5 days/week** in any city                                                                  |


**In application forms:**

- Work authorization: *F-1 (OPT/CPT eligible; will require H-1B sponsorship)*
- Relocation: *Yes, for the right opportunity*
- Start date: *May 2027* (or earlier for internships — note cycle in free text)

**In evaluations (scoring):**

- **Remote/hybrid outside US:** score **2.0–3.0** unless role explicitly hires US-based remote
- **No sponsorship / sponsorship unclear:** score practicality **2.5–3.5** (risk flag only) — **NOT a deal-breaker; still recommend apply** when skills fit; note F-1 risk in Block B and suggest asking recruiter early
- **Sponsorship confirmed:** small boost to practicality — **3.5–4.0**; do not require for apply decision
- **Must be on-site 5 days in non-target city** without relocation support: score location **2.5–3.0**, not automatic discard if comp/role strong
- **Fully remote US** (sponsorship a plus, not required): favorable — score remote dimension **4.0+**

## Deal-breakers & Scoring Nudges


| Signal                                             | Action                                                                                                                |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| No visa sponsorship (F-1)                          | **Still apply** if role fit is good; flag risk in Block B + negotiation script; never auto-SKIP for sponsorship alone |
| Pure frontend / mobile with no systems overlap     | Lower archetype fit unless adjacent stretch                                                                           |
| ML role with no production/serving (notebook-only) | Prefer infra/serving framing; flag if mismatch                                                                        |
| Below 4.0/5 fit                                    | Recommend skip per system ethics unless user overrides                                                                |
| Legitimacy concerns (Block G)                      | Do not recommend apply until verified                                                                                 |


## Superpowers (quick reference)

From profile.yml — use in Blocks B/E:

- Distributed systems & performance (gRPC, Protobuf, lock-free, exactly-once)
- Production ML serving (vLLM, PagedAttention, AWS)
- Cloud & IaC (ECS Fargate, Terraform, circuit breakers, CI/CD)
- Low-latency backend (C++, Go, TypeScript) + strong testing discipline
