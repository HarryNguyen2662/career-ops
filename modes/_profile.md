# User Profile Context -- career-ops



## Your Target Roles

**North Star (from profile.yml):** New grad / intern SWE, applied AI systems (production reliability for AI outputs + AI inference performance), backend & distributed systems, systems software, platform & cloud infra, SRE, performance engineering.

**Positioning note (2026-09-11, mentor-informed pivot):** "Backend / Distributed Systems" alone is no longer a differentiated lead — it's the default framing on most new-grad resumes and the hiring bar for it is shrinking. "I built an agent" is not a signal either, since agent creation is now roughly one prompt away for anyone. The durable, differentiated story is **proof of work for AI reliability in production** — not "I called an LLM," but "I built the evaluation/confidence/review layer that makes an LLM's output trustworthy at scale" — paired with **AI inference performance** (the actual optimization work, not just "I used vLLM"). Backend/distributed-systems/SRE content still matters as supporting evidence of production rigor, but should not be the headline framing when the target role is AI-native. Lead with **Applied AI Systems Engineer** first; use the other archetypes below as the secondary/supporting frame per JD.

| Archetype                                           | Thematic axes                                                                       | What they buy                                                              |
| --------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **Applied AI Systems Engineer** *(primary lead)*    | Agentic tool calling with pre-deploy test gates and post-deploy auto-rollback; hybrid BM25/vector retrieval + MCP; vLLM/PagedAttention inference performance under concurrent load; multi-provider LLM routing with schema-constrained output validation | Someone who makes AI output trustworthy and fast in production, not just functional in a demo |
| **ML / AI Infrastructure Engineer**                 | vLLM, PagedAttention, continuous batching, inference SLOs, GPU/memory efficiency    | Someone who runs LLM workloads in production without OOM/latency surprises |
| **Backend / Distributed Systems Engineer**          | gRPC, Protocol Buffers, concurrency debugging, read-replica routing, PostgreSQL/pgvector/Redis    | Someone who ships reliable, fast backends under concurrency                |
| **Systems Software Engineer**                       | C++, Mojo IPC, lock-free structures, Chromium-scale performance, large-scale refactors | Someone who optimizes core paths in a browser-scale codebase                     |
| **Site Reliability Engineer**                       | Multi-AZ ECS, Prometheus/Grafana, pre-deploy tests + auto-rollback, uptime/cost tradeoffs | Someone who keeps prod healthy and cheap                                   |
| **Performance Engineer**                            | p99 latency, profiling, hot partitions, N+1 elimination, mutex contention           | Someone who finds bottlenecks and proves impact with numbers               |
| **Platform / Cloud Infrastructure Engineer**        | Terraform IaC, ECS Fargate, CI/CD deploy speed (15→5 min), AWS platform migrations  | Someone who owns cloud topology and deploy pipelines                       |
| **Cloud / DevOps Engineer**                         | GitHub Actions, auto-scaling, observability-minded ops                              | Someone who automates deploy and scale                                     |
| **AI/ML Engineer (Inference & Serving)**            | vLLM/PagedAttention serving, evals, multi-provider routing, Django/FastAPI serving layer | Someone who connects models to product APIs                                |
| **Backend Engineer (Payments & High-Throughput)**   | Idempotent APIs, Redis cache, exponential backoff, partition keys                   | Someone who builds money paths safely under partitions                     |
| **Open Source / Developer Tools Engineer**          | Go CLI, multi-cloud IaC, Raft/Paxos literacy                                        | Someone who contributes upstream with rigor                                |
| **Founding / Early-Stage Software Engineer**        | End-to-end ownership, cost-conscious infra, solo delivery                           | Someone who builds 0→1 with production discipline                          |
| **Full-Stack Engineer** *(adjacent)*                | React/TypeScript UI (NextStep), event-driven state refactor (Chromium)                                | Breadth when role is product-facing, not primary pitch                     |
| **Browser / Client Platform Engineer** *(adjacent)* | Chromium, Mojo IPC + state-management refactor (closed 45 bugs) in browser stack                    | Chrome internship proof when JD is client/platform                         |


## Your Adaptive Framing


| If the role is...               | Emphasize about you...                                                                                              | Proof point sources                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Applied AI Systems *(lead when JD is AI-native)* | TiMoto's agentic tool-calling system that investigates and fixes bugs from PR diffs and log traces, guarded by pre-deploy tests and post-deploy auto-rollback; hybrid BM25/vector retrieval plus an MCP server; vLLM/PagedAttention fix eliminating OOM under concurrent load; NextStep's deterministic schema validation and multi-pass repair — production reliability + inference performance, not "I used an LLM API" | cv.md — TiMoto agent/RAG/vLLM bullets; NextStep extraction + router bullets |
| Backend / Distributed Systems   | gRPC + Protobuf IPC; gRPC deadlock/lock-ordering fix; exactly-once payment APIs; DynamoDB partition redesign; PostgreSQL indexing | cv.md — Google IPC, TiMoto gRPC, Develop for Good DB; CoderPush payments (user-confirmed, not currently on the 1-page cv.md) |
| Systems Software                | C++ at scale; lock-free trie (design doc, under 50ms p99); 78 changes shipped to Chrome stable          | cv.md — Google Chrome bullets                               |
| ML / AI Infrastructure          | Primary engineer on TiMoto serving stack; vLLM/PagedAttention (3.2x throughput); deadlock fix under concurrent gRPC; KV cache fragmentation 65%→<4% | cv.md — TiMoto experience; profile.yml proof_points            |
| SRE / Platform                  | 99.9% uptime over 4 months; Prometheus/Grafana from zero; root-cause under 15 min; multi-AZ ECS; Terraform; 44% cost cut | cv.md — TiMoto infra bullet                                 |
| Performance                     | Quantified latency wins (96% settings search p99, sub-100ms queries, 70% data-access latency cut, 3.2x serving throughput, 30% DynamoDB throughput) | cv.md — Google, Develop for Good, TiMoto; CoderPush (user-confirmed) |
| Cloud / DevOps                  | Appwrite/AWS platform migration, GitHub Actions CI/CD (deploys 15 to 5 min), ECS/Terraform                            | cv.md — Develop for Good + TiMoto                           |
| AI/ML (product-facing)          | End-to-end AI evaluation product; agentic bug-fix loop and hybrid RAG in production; model serving tradeoffs        | cv.md — TiMoto; timoto.ai                                   |
| Payments / fintech backend      | Idempotency, Redis 85% hit rate, hot-partition diagnosis                                                            | CoderPush (user-confirmed 2026-09-12; cut from the 1-page cv.md for space, still fair game to use) |
| Open Source / DevTools          | Pulumi Go CLI contributions; Raft/Paxos study for distributed state                                                 | cv.md — Pulumi project                                      |
| Founding / early-stage          | Primary engineer for backend + infra + ML on 3-person team; ships with SLOs and a real cost target (44% infra cut)  | cv.md — TiMoto; profile.yml                                 |
| Full-Stack *(adjacent)*         | Event-driven state refactor in Chromium; React in NextStep                                                                 | cv.md — Google + TiMoto                                     |
| Browser / platform *(adjacent)* | Chromium state-management refactor (45 bugs closed); C++ IPC config reader shipped to stable; Chrome Privacy Sandbox internals page; test suite 2 h to 10 min | cv.md — Google Chrome                                       |


**Default lead story:** CS @ Georgia State (GPA 3.75, May 2027) + **TiMoto AI Software Engineer** (primary engineer: agentic bug-fix system, hybrid RAG + MCP, vLLM/PagedAttention inference performance) + **NextStep founder** (schema-constrained extraction and multi-pass repair, multi-provider LLM router failover). Not "student who took courses," and not "built an agent" — **engineer who makes AI output trustworthy and fast in production**. Google Chrome intern (production C++/Lit merged into Chrome's codebase) stays a strong secondary proof point for systems rigor when the JD is not AI-native.

## Your Exit Narrative

Use **config/profile.yml → narrative.exit_story** to frame ALL content:

> Primary engineer for backend, cloud infra, and AI systems at TiMoto AI (3-person team). Built an agentic tool-calling system that autonomously fixes production bugs (MTTR 45 to under 8 minutes), a hybrid BM25/vector retrieval layer plus MCP server (Precision@5 68% to 91%), and production LLM serving on vLLM/PagedAttention (3.2x throughput). Google internship merged a C++ Mojo IPC interface into Chrome's codebase and cut settings search p99 latency 96% with a self-implemented lock-free trie. Prior internship at Develop for Good on AWS, PostgreSQL, and application scaling.

**In PDF summaries:** Bridge **coursework foundation** (Distributed Systems, OS, DB, Networks) → **internship production impact** → **target role** (backend/systems/ML infra).

**In STAR stories:** Prefer quantified bullets from cv.md — never invent metrics. Anchor stories:

1. **Google Chrome** — Mojo IPC/Protobuf choice, self-implemented lock-free trie, or Privacy Sandbox internals page
2. **TiMoto** — agentic bug-fix system design, gRPC deadlock fix, vLLM selection, or Terraform/multi-AZ uptime
3. **Develop for Good** — CW3's Airtable-to-Appwrite migration, N+1 → sub-100ms, or CI/CD deploys 15→5 min

**In draft answers:** First paragraph = headline from profile.yml + one proof point matched to company/product.

## Your Cross-cutting Advantage

Frame as **"Applied AI systems engineer: builds the reliability layer that makes AI output trustworthy in production, and optimizes the inference performance underneath it — not a demo-agent builder."**

Signature moves:

- **Proof of work over "I built an agent"** — the differentiator is the guardrail layer around AI output (TiMoto's pre-deploy tests and post-deploy auto-rollback on agent-authored fixes; NextStep's schema validation, multi-pass repair, and manual-review routing), not the existence of an LLM call
- **Measure then fix** — always cite p99, throughput, % reduction, or cost
- **Explicit tradeoffs** — Protobuf vs custom serialization, linear scan vs lock-free trie, vLLM vs naive inference, PagedAttention vs OOM
- **Correctness under failure** — pre-deploy gates and auto-rollback, lock-ordering discipline, linearizability/Raft literacy
- **High bar for quality** — no-regression bar on Chrome's existing test suite; 302-test project-wide suite on NextStep

**User-stated metrics (confirmed 2026-09-11/12, treat as facts from cv.md):** TiMoto agentic bug-fix system (MTTR 45 → under 8 min across 150+ issues in 2 months, [superseded 2026-09-25: now 95% fully automated, see Bug-fix agent approval rate note] 30-35% of bugs auto-resolved end to end); TiMoto retrieval (Precision@5 68% → 91%, data-access latency -70% via MCP server to read-replicas); TiMoto vLLM/PagedAttention (3.2x throughput 14 → 45 req/sec, KV cache fragmentation 65% → under 4%, OOM 6-8% of peak-hour requests → none in 4 months); TiMoto gRPC deadlock fix (ML evaluation accuracy 57% → 87%); NextStep extraction (per-field error 37% → 9% for 100 active users, 7% of documents routed to manual review); NextStep LLM router (request completion 92-94% → 99.7% across Gemini/OpenAI/OpenRouter/NVIDIA NIM, malformed structured output 12-15% → under 0.3%). Figures came directly from Harry, not estimated.

**User-stated context (confirmed 2026-09-24):** TiMoto AI (timoto.ai) is a Vietnamese app that prices used motorbikes from photos with AI and trades gas bikes in for electric ones. Before the agentic bug-fix system, production bugs took 45-50 minutes to debug because a 3-person team ran a large product. The EKS setup was over-provisioned and the system design was not cost-efficient; Harry redesigned it to save cost. vLLM: "for 4 months" means zero out-of-memory failures in the 4 months after the fix. Retrieval (user-stated and confirmed as real 2026-09-24): one retrieval subsystem, reached over MCP, serves both the autonomous debug/fix agent and an internal dev assistant; docs = API specs/service contracts, runbooks and post-mortems, ADRs. It was vector-only (PostgreSQL + pgvector), which missed exact identifiers (error codes, function names, endpoint paths), so the agent inferred wrong API schemas and produced patches that failed integration tests, needing 2-3 extra retry rounds (user estimate). The fix added BM25 fused with vectors via RRF (Precision@5 68% to 91%). The MCP server routes AI tool reads to read replicas plus an in-memory/Redis cache instead of the primary DB (data-access latency about 1200ms to about 350ms, the 70% cut; approximate). Google Mojo IPC (user-confirmed 2026-09-24): Harry defined the .mojom interface (browser process to WebUI renderer) and wrote the C++ browser-process handler that queries state, serializes it, and sends it to chrome://privacy-sandbox-internals. He worked on Topics (epoch/taxonomy state) and part of Attribution Reporting (pending reports/sources) only, not Protected Audience or Private Aggregation. This interface is the core of the 2-3 hours to under 5 min result, so the IPC and page-rebuild bullets are one story. DROP "10K+ req/sec": it was a local max-load benchmark, not real traffic. Keep "under 50ms p99". CLs are public on chromium-review.googlesource.com and Harry has found them; never claim they are confidential. Google refactor + search + tests (user-confirmed 2026-09-24): panels written by different sub-teams (Topics, Attribution Reporting, etc.) mutated one shared state object directly, causing stale/desynced data between tabs and light renderer crashes when two components wrote at once; Harry found the cause by reproducing bug-tracker reports and tracing call stacks, moved state to an event-driven observer model, and tracked that the bugs did not recur (no specific duration or count, so never claim one). Drop "25K+ line" (mostly diffs across call sites plus tests). Settings search: thousands of config keys/feature flags; the trie lives in C++ in the browser process; another thread writes new keys from IPC while search reads, hence lock-free. Tests: page tests timed out/crashed mid-run because assertions ran before UI data loaded; Harry made tests wait for data before asserting, which sped up the suite and removed mid-run timeouts. TiMoto app backend (user-stated 2026-09-24; architecture verified against code and AWS by Harry's own repo review): Harry built TiMoto's backend and infra from zero to production. Vercel hosts only web frontends (landing site, Dealer Portal SPA). ECS Fargate production mobile cluster runs 3 services: timoto-backend (Django REST API, port 8000), timoto-ai-service (gRPC evaluator: appearance, engine, emissions, price; reached via private Cloud Map ai-service.timoto.local:50051, unary RPC, 300s deadline, no load balancer), timoto-realtime-ws (WebSocket, port 8001; events valuation_ready/valuation_rejected, FCM fallback when the client is offline). Route 53 points the API domain to a public NLB in front of the REST API and the WebSocket service only. Evaluation is async (POST, then GET result). DB: Aurora PostgreSQL (primary), optional Redis cache, S3 for media; DynamoDB only in the Chotot ingestion pipeline (Lambda/SQS/S3) and control tooling. OPS uses PostgreSQL LISTEN/NOTIFY. Dealer Portal and Internal/OPS have separate Django backends. DO NOT claim: a total microservice count, user counts or valuations/day (telemetry unreconciled; ~2.7-3.05K API requests/day is total traffic only), a 30-second valuation time, gRPC streaming, NLB in front of the gRPC evaluator, or the reason NLB was chosen. REPO AUDIT 2026-09-24 (Harry's own code/Git/AWS review; claims (1)-(7) below were not found in the audited repos; Harry RE-CONFIRMED all of them as accurate on 2026-09-24, saying the repo material is older and the resume numbers are correct. Treat them as user-confirmed facts, but be ready to name each number's source in interviews): (1) 44% cost cut: the only 44% found is EC2's share of one bill snapshot, not a reduction (contradicted). (2) 99.9% uptime: no measurement found. (3) Grafana built from zero: docs list Grafana as a next phase; not confirmed running (CloudWatch logs, ECS events, health checks confirmed). (4) EKS to Fargate: commit 8c36adb (2025-10-19) moved Dealer staging deploy to Fargate citing node-group failures and Kubernetes complexity; mobile EKS path cleaned up Apr 2026; not one company-wide migration. (5) Agent: creates draft PRs; humans merge and deploy; best-documented run reached AWAITING_APPROVAL on mobile staging; no basis found for '30-35% fully automated' or MTTR 45 to under 8 min. (6) vLLM (3.2x, OOM 6-8%, KV cache 65% to under 4%): no vLLM config found in 7 codebases. (7) gRPC deadlock 57% to 87%: no evidence or metric definition found. VERIFIED STORIES (commits authored by Harry; he must confirm he did the investigation): Dealer Portal 2026-07-13 deploy reported success but users saw old UI because the script updated a different ECS service than the one behind the public NLB; commit b18817f5 fixed rollout target and added post-deploy checks (live JS bundle vs build, DNS, targets, image; 11 checks passed). Duplicate OpenAI calls: commit 8cc1984 (2026-03-22) two concurrent requests for one bike could call OpenAI twice; fix = per-bike_id cache lock (660s TTL); async flow returns 202 for repeat requests via pending/running DB state (not guaranteed system-wide idempotency; cache falls back to per-process LocMem if Redis is absent; async worker is a thread in the web process). Sync to async: 2026-01-09 AI evaluation integrated synchronously with Gunicorn timeout raised to 300s; 2026-05-13 POST returns 202 then GET result. Presigned S3 direct upload with client retry. Harry has commits in Dealer backend (1cd4b53), Internal app (33b2187), Chotot AWS pipeline (b22e2fa). Redis in production unconfirmed. Google extra facts (user-stated 2026-09-24): Harry's Privacy Sandbox internals work shipped to Chrome stable (milestone not known, never guess one); 78 merged CLs (countable on chromium-review); he wrote design docs for the settings search and for making page tests efficient; the Chrome team uses the page; stack = TypeScript frontend, Mojo, C++ middle layer. Return offer: unknown. Bug-fix agent approval rate (user-stated 2026-09-25, replaces "30-35% fully automated" on the master CV): the agent proposes a fix and self-approves 95% of them; only fixes it is not confident about go to human review. Earlier CVs already sent (e.g. #603-#620, incl. the Amazon referral) say 30-35%; Harry has not explained the difference, so be ready to explain it if a recruiter sees both. The 2026-09-24 repo audit found a draft-PR flow awaiting approval on staging. More Google numbers (user-stated 2026-09-24): the state refactor closed 45 related bugs; many teams use the page, which made gathering data and logs faster; about 30 page tests used to time out or fail mid-run before Harry's fix (approximate, say "about 30"); tests now wait for data to load before checking UI changes; the team's suite went from 2 hours to 10 minutes. Collaboration (user-stated 2026-09-24): at Google Harry talked with other teams to learn how long they spent debugging with the Privacy Sandbox internals page (source of the 2-3 hours baseline). At TiMoto he worked with operators, sales, the founder, the product manager, and marketing to improve the company's internal agents and knowledge base Details (user-stated 2026-09-24): a separate company-wide internal AI agent (not the bug-fix agent) loaded with company context and knowledge base, used by all staff to answer questions and do tasks; before, it gave wrong, messy answers and retrieval was slow; Harry reorganized the knowledge base by team and used RAG plus a knowledge graph (graphify); response time went from 30-40s to 5-10s per request. Develop for Good (user-stated 2026-09-24): CW3 left Airtable because it had become inconvenient and messy to use at their scale; "500+" is 500+ real concurrent users measured in the system (not a load test). NextStep (user-stated 2026-09-24): the 100 users are real (confirmed, overrides the article-digest verify note). Extraction errors came from the first model/harness not being good enough; the fix was switching model and harness plus the new approach (schema validation, multi-pass repair). Router failures came from provider rate limits and timeouts. Resumable upload exists because the model needs the complete document, so uploads must not be interrupted.

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

- Agentic AI systems (tool calling, MCP, autonomous bug-fix loops with pre-deploy tests and auto-rollback)
- Production ML serving (vLLM, PagedAttention, concurrent inference on AWS)
- Retrieval & AI reliability (hybrid BM25/vector search, schema-constrained generation, multi-pass repair, evals)
- Distributed systems & performance (gRPC, Protocol Buffers, lock-free structures, concurrency debugging)
- Cloud & IaC (ECS Fargate, Terraform, multi-AZ, CI/CD, Prometheus/Grafana observability)

## User-stated skills not on cv.md (Harry, 2026-10-04; Skills lines only)

Harry confirmed he has: full-stack and frontend work, code review, mentoring, on-call experience, customer-facing work, prompt engineering, Jest/Playwright, C#, LangChain, Hugging Face, Kafka, Spark and TensorFlow (plus PyTorch, NVIDIA Triton, Ray, GPU and performance profiling from 2026-09-30/10-03). Use these only as terms in the Skills lines, and only when the JD names them. Never write a bullet that claims a specific project, scale or result with them, and never put them in cv.md unless Harry asks. Be ready for interview questions on each one.

Added 2026-10-09 (Harry, in chat): he has Linux, operating systems, computer networking and TCP/IP, and C (used alongside C++), all learned and used through projects. Skills lines only, like the rest of this list; never write bullet claims, project names or metrics for them.

Added 2026-10-09 (Harry, in chat): he first learned to code through competitive programming in middle school. Usable as narrative and as a "Competitive Programming" Skills term; no contest names, ranks or awards are known, so never state any.

Added 2026-11-04 (Harry, in chat): he has Kotlin, DynamoDB, microservices architecture, API lifecycle management (versioning, documentation, deprecation) and payments work, and he asked for them on his CVs. Skills lines only, and only when the JD names them, like the rest of this list; never write bullet claims, project names, scale or metrics for them. Be ready for interview questions on each one.


