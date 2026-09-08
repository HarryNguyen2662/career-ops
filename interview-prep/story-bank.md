# Story Bank — Master STAR+R Stories

This file accumulates your best interview stories over time. Each evaluation (Block F) adds new stories here. Instead of memorizing 100 answers, maintain 5-10 deep stories that you can bend to answer almost any behavioral question.

## How it works

1. Every time `/career-ops oferta` generates Block F (Interview Plan), new STAR+R stories get appended here
2. Before your next interview, review this file — your stories are already organized by theme
3. The "Big Three" questions can be answered with stories from this bank:
   - "Tell me about yourself" → combine 2-3 stories into a narrative
   - "Tell me about your most impactful project" → pick your highest-impact story
   - "Tell me about a conflict you resolved" → find a story with a Reflection

## Stories

<!-- Stories will be added here as you evaluate offers -->
<!-- Format:
### [Theme] Story Title
**Source:** Report #NNN — Company — Role
**S (Situation):** ...
**T (Task):** ...
**A (Action):** ...
**R (Result):** ...
**Reflection:** What I learned / what I'd do differently
**Best for questions about:** [list of question types this story answers]
-->

> **Rewritten 2026-09-25** to match the locked cv.md. Every number below traces to cv.md, modes/_profile.md ("User-stated context" notes), article-digest.md, or a commit Harry authored. Older stories with unconfirmed numbers ("100% evaluation success rate", "sub-50ms p99 inference", "68% MTTI", "95% test coverage", "25K+ lines", "React" for the Chrome page) were removed. "Reflection" lines are suggested lessons: rewrite them in your own words before an interview. "Watch out" lines are the follow-up questions most likely to come next.

## Big Three quick map

- **Tell me about yourself:** TiMoto backend from zero (#2) + AI bug-fix agent (#1) + Chrome Privacy Sandbox internals page (#10).
- **Most impactful project:** AI bug-fix agent (#1) for AI roles; Chrome internals page (#10) for big tech generalist roles; valuation backend (#2) for backend roles.
- **Hardest bug / conflict / cross-team:** gRPC deadlock (#7) or Chrome state refactor (#12) for debugging; company-wide agent (#9) or Chrome team interviews (#10) for working with others.

---

## TiMoto AI (Software Engineer, Sep 2025 -- Present)

Context: TiMoto AI (timoto.ai) is a Vietnamese app that prices used motorbikes from photos with AI and trades gas bikes in for electric ones. Harry is the primary engineer for backend, cloud infra, and AI systems on a small team.

### 1. [AI Reliability / Automation] AI agent that fixes production bugs
**Source:** cv.md; modes/_profile.md (user-stated 2026-09-11/12 and 2026-09-25)
**S:** A small team running a large product spent about 45 minutes debugging each production bug.
**T:** Cut the time from bug to fix without letting bad fixes reach users.
**A:** Built an AI agent that reads PR diffs and logs and proposes a fix. Every fix runs behind tests, and auto-rollback undoes a bad deploy. The agent approves fixes it is confident about and sends only uncertain ones to a human for review.
**R:** Debug time dropped from about 45 to under 8 minutes over 150+ issues in 2 months; 95% of fixes fully automated.
**Provenance:** source: cv.md | user-stated 2026-09-25 (95% replaced the earlier 30-35%).
**Watch out:** "How does the agent decide it is confident?" and "Why did an earlier CV say 30-35%?" (CVs #603-#620 carry the old figure). Have a one-sentence answer for both. The 2026-09-24 repo review found a draft-PR flow waiting for approval on staging, so be precise about what "fully automated" covers.
**Reflection:** The hard part of an AI agent is not generating a fix, it is knowing when not to trust it.
**Best for:** AI engineering, automation, reliability, "most impactful project", judgment about AI output.

### 2. [System Design / Backend] Motorbike-valuation backend from zero
**Source:** cv.md; modes/_profile.md (architecture verified against code and AWS)
**S:** TiMoto needed a production backend for its valuation app, and an AI valuation can take minutes, too long to hold one HTTP request open.
**T:** Build the backend and infra from zero to production so the app stays responsive while AI runs.
**A:** Built it on AWS ECS Fargate as separate services: a Django REST API for the app, a private gRPC evaluator (appearance, engine, emissions, price) reached over Cloud Map, and a WebSocket service that tells the app when a valuation is ready or rejected, with FCM push as a fallback when the app is offline. Route 53 and a public NLB front only the REST API and WebSocket service. Aurora PostgreSQL holds app data; photos upload straight to S3 through presigned URLs. The first version (Jan 2026) called the AI synchronously with a 300-second Gunicorn timeout; in May 2026 it moved to async: POST returns 202, the app fetches the result later.
**R:** The app no longer blocks on long AI jobs; users get notified the moment results are ready.
**Provenance:** source: cv.md | user-stated 2026-09-24 | architecture verified in code and AWS by Harry's repo review.
**Watch out:** Do NOT claim a microservice count, user counts, valuations per day, a 30-second valuation time, gRPC streaming, or an NLB in front of the gRPC evaluator. Be ready for "why gRPC between services" (typed protobuf contract, generated stubs) and "why move from sync to async".
**Reflection:** Starting synchronous was fine for launch; the timeout was the signal to redesign.
**Best for:** System design, backend architecture, async processing, real-time notifications, "walk me through something you built".

### 3. [Concurrency / Backend] Duplicate OpenAI calls for the same bike
**Source:** modes/_profile.md; commit 8cc1984 (2026-03-22, authored by Harry)
**S:** Two requests arriving at the same time for the same bike could each call OpenAI, doubling cost and work.
**T:** Make repeat requests for one bike safe.
**A:** Added a lock keyed on bike_id (660-second TTL) and pending/running states in the database, so a repeat request gets a 202 instead of running the model again.
**R:** Concurrent requests for one bike no longer trigger duplicate model calls.
**Provenance:** source: commit 8cc1984 | user-confirmed 2026-09-24.
**Watch out:** Do not call it guaranteed system-wide idempotency: the cache falls back to per-process memory if Redis is absent, and the async worker is a thread in the web process. Saying this yourself shows you know the limits.
**Best for:** Concurrency, race conditions, idempotency, backend correctness.

### 4. [Incident / DevOps] Deploy said "success" but users saw the old UI
**Source:** modes/_profile.md; commit b18817f5 (2026-07-13, authored by Harry)
**S:** A Dealer Portal deploy reported success, but users still saw the old UI.
**T:** Find why a "successful" deploy never reached users and stop it from happening again.
**A:** Found the deploy script updated one ECS service while the public NLB was routing traffic to a different one. Fixed the rollout target and added post-deploy checks that compare the live JavaScript bundle with the build and verify DNS, targets, and image.
**R:** Deploys now update the service that actually serves traffic; the follow-up verification passed all 11 checks.
**Provenance:** source: commit b18817f5 | user-confirmed 2026-09-24. The Dealer frontend has since moved to Vercel, so tell it as a past incident.
**Watch out:** Add from memory: who noticed first, how long users were affected, and which step of the investigation was yours.
**Best for:** Production incidents, debugging deploys, "tell me about a time something broke".

### 5. [Infrastructure / Cost] Over-provisioned EKS to multi-AZ ECS Fargate
**Source:** cv.md; story-bank 2026-09-12 provenance; modes/_profile.md
**S:** The EKS setup was over-provisioned at about $5K/month and the system design was not cost-efficient.
**T:** Cut cost without hurting reliability.
**A:** Redesigned onto multi-AZ ECS Fargate managed with Terraform, with Grafana monitoring. (Commit 8c36adb, 2025-10-19, moved the Dealer staging deploy to Fargate after node-group failures and Kubernetes complexity.)
**R:** Cost down 44% to under $3K/month at 99.9% uptime over 4 months; root cause found in under 15 minutes.
**Provenance:** source: cv.md | user-stated 2026-09-12 | user re-confirmed 2026-09-24 (numbers were not found in the audited repos).
**Watch out:** Know where each number comes from (AWS bill, dashboard) before the interview.
**Best for:** Cost optimization, infrastructure, Terraform, reliability, SRE.

### 6. [ML Infrastructure] Out-of-memory failures in LLM serving
**Source:** cv.md; modes/_profile.md
**S:** 6-8% of peak-hour LLM requests failed out of memory.
**T:** Stop the failures and serve more traffic on the same setup.
**A:** Diagnosed the cause as 65% KV cache fragmentation and moved serving to vLLM, whose PagedAttention allocates KV cache in pages.
**R:** Fragmentation under 4%, no out-of-memory failures in the 4 months after the fix, throughput up 3.2x (14 to 45 req/sec).
**Provenance:** source: cv.md | user-confirmed 2026-09-24 ("4 months" = no OOM in the 4 months after the fix).
**Watch out:** Know which model vLLM serves and on what GPU; the repo review did not find the vLLM config, so answer from memory.
**Best for:** ML infrastructure, performance, inference, "tell me about a tradeoff".

### 7. [Debugging / Concurrency] gRPC deadlock behind wrong ML results
**Source:** cv.md; modes/_profile.md
**S:** ML evaluation accuracy was stuck at 57%.
**T:** Find why results were wrong.
**A:** Traced it to a production gRPC deadlock that truncated responses, which then scored as wrong results. The cause was inconsistent lock ordering; replaced it with one enforced order.
**R:** Accuracy rose to 87%.
**Provenance:** source: cv.md | user-confirmed 2026-09-24.
**Watch out:** "How did you notice accuracy was wrong?" and "How is accuracy measured?" Answer from memory; the repo review found no write-up of this.
**Reflection:** A correctness bug can hide inside a concurrency bug; check whether "wrong" results are really incomplete ones.
**Best for:** Debugging, root-cause analysis, concurrency, "hardest bug".

### 8. [Retrieval / AI Reliability] Hybrid search so the agent reads the right specs
**Source:** modes/_profile.md (user-stated and confirmed real 2026-09-24)
**S:** One retrieval system, reached over MCP, feeds both the bug-fix agent and an internal dev assistant with API specs, runbooks, post-mortems, and ADRs. It was vector-only (PostgreSQL + pgvector) and missed exact identifiers such as error codes, function names, and endpoint paths, so the agent inferred wrong API schemas and its patches failed integration tests, costing 2-3 extra retry rounds (estimate).
**T:** Get the right documents into the agent's top results.
**A:** Added BM25 keyword search fused with vector search using Reciprocal Rank Fusion. Separately, the MCP server routes AI tool reads to read replicas plus a cache instead of the primary database.
**R:** Precision@5 from 68% to 91%; data-access latency down 70% (about 1,200ms to about 350ms, approximate).
**Provenance:** user-stated 2026-09-24, confirmed real. Not on the master CV (kept for AI-focused tailoring).
**Best for:** RAG, search, AI reliability, "a technical decision you made".

### 9. [Cross-Functional / Collaboration] Company-wide AI agent for all staff
**Source:** cv.md; modes/_profile.md (user-stated 2026-09-24)
**S:** A company-wide internal AI agent (separate from the bug-fix agent), loaded with company context, gave staff wrong, messy answers and was slow.
**T:** Make it useful for non-engineering teams.
**A:** Worked with ops, sales, marketing, product, and the founder to learn how each team works, reorganized the knowledge base by team, and used RAG plus a knowledge graph (graphify) to speed up retrieval.
**R:** Replies went from 30-40 seconds to 5-10 seconds per request.
**Provenance:** source: cv.md | user-stated 2026-09-24.
**Watch out:** Have one concrete example of a question a sales or ops person asked that now works.
**Best for:** Working with non-engineers, stakeholder management, cross-functional collaboration.

---

## Google (Software Engineer Intern, Chrome Browser, May -- Aug 2025)

### 10. [Impact / Developer Tools] Chrome Privacy Sandbox internals page
**Source:** cv.md; modes/_profile.md (user-confirmed 2026-09-24)
**S:** Talking with other teams showed that debugging a user's Privacy Sandbox settings took 2-3 hours per case of raw logs and database dumps.
**T:** Give engineers one place to see that state.
**A:** Rebuilt the Chrome Privacy Sandbox internals page: defined the .mojom interface and wrote the C++ browser-process handler that reads config and sends it over IPC to a TypeScript UI. Worked on Topics (epoch and taxonomy state) and part of Attribution Reporting (pending reports and sources).
**R:** Shipped to Chrome stable in 78 merged changes; debugging dropped to under 5 minutes for 200+ engineers, and the Chrome team uses the page.
**Provenance:** source: cv.md | user-confirmed 2026-09-24.
**Watch out:** Chromium CLs are public on chromium-review.googlesource.com. Never say they are confidential; keep 1-2 CL links ready. Do not guess the milestone. Do not claim Protected Audience or Private Aggregation. The old "10K+ req/sec" figure was dropped.
**Best for:** Impact, developer tooling, "most impactful project", talking to users before building.

### 11. [Performance / Concurrency] Lock-free trie for settings search
**Source:** cv.md; modes/_profile.md
**S:** Searching thousands of config keys and feature flags took 1,200ms at p99, because it scanned linearly while an IPC thread kept writing new keys.
**T:** Make search fast without readers waiting on writers.
**A:** Wrote the design doc and built a lock-free trie in C++ in the browser process, so search reads never wait on IPC writes.
**R:** p99 under 50ms, with no test regressions.
**Provenance:** source: cv.md | user-confirmed 2026-09-24.
**Watch out:** Chromium usually prefers posting tasks between sequences over locks and lock-free code. Expect "why not just post a task?" and "how did you prove it correct?"
**Best for:** Performance, data structures, concurrency, design docs.

### 12. [Debugging / Architecture] Shared state behind stale tabs and crashes
**Source:** cv.md; modes/_profile.md
**S:** Panels written by different sub-teams (Topics, Attribution Reporting, and others) all changed one shared state object directly. Tabs showed stale data, and the renderer crashed when two components wrote at once.
**T:** Find the root cause behind a stream of bug reports.
**A:** Reproduced the bug-tracker reports and traced call stacks to the shared mutable state, then moved the page to an event-driven observer model where panels subscribe instead of writing shared state.
**R:** Closed 45 related bugs; they stopped recurring.
**Provenance:** source: cv.md | user-confirmed 2026-09-24 (no duration or recurrence count, so never add one; "25K+ lines" dropped).
**Best for:** Debugging, architecture, working across teams, "hardest bug".

### 13. [Testing / Productivity] Flaky page tests: 2 hours to 10 minutes
**Source:** cv.md; modes/_profile.md
**S:** About 30 page tests timed out or crashed mid-run, because checks fired before the UI finished loading data.
**T:** Make the suite reliable and fast.
**A:** Wrote a testing design doc and changed the tests to wait for their data before checking UI changes.
**R:** The team's suite went from 2 hours to 10 minutes, with no more mid-run timeouts.
**Provenance:** source: cv.md | user-stated 2026-09-24 ("about 30" is approximate).
**Best for:** Testing, developer productivity, flaky tests, design docs.

---

## Develop for Good (Software Engineer Intern, May -- Aug 2024)

### 14. [Database / Performance] N+1 queries on CW3's member list
**Source:** cv.md
**S:** The member list for CW3, a global Web3 community, took 3+ seconds to load over 10,000+ records.
**T:** Make the page load fast.
**A:** Found N+1 queries, replaced them with batched queries, and added PostgreSQL indexes.
**R:** Load time under 100ms.
**Provenance:** source: cv.md.
**Best for:** SQL, performance, backend debugging.

### 15. [Migration / Ownership] Moving CW3 off Airtable
**Source:** cv.md; modes/_profile.md (user-stated 2026-09-24)
**S:** CW3 had outgrown Airtable, which had become cluttered and hard to use.
**T:** Move the community onto a real backend as the primary backend engineer on a 12-person team.
**A:** Moved it to Appwrite with profile-based member matching for meetups, and automated weekly deploys with a GitHub Actions CI/CD pipeline.
**R:** 500+ real concurrent users (measured in the system, not a load test); deploys from 15 to 5 minutes.
**Provenance:** source: cv.md | user-stated 2026-09-24.
**Best for:** Ownership, migrations, working on a team.

---

## NextStep (Founder)

Context: NextStep's AI copilot tracks deadlines and obligations in household documents for 100 real users (confirmed 2026-09-24).

### 16. [AI Reliability] Extraction errors from 37% to 9%
**Source:** cv.md; modes/_profile.md
**S:** The first model and harness misread 37% of the fields they extracted.
**T:** Make extraction trustworthy enough for real users.
**A:** Switched both the model and the harness, and added deterministic schema validation with multi-pass repair; fields still uncertain go to manual review.
**R:** Errors down to 9%, with 7% routed to manual review.
**Provenance:** source: cv.md | user-stated 2026-09-24.
**Best for:** AI reliability, iteration, "a time your first approach failed".

### 17. [LLM Infrastructure] Multi-provider router
**Source:** cv.md; article-digest.md
**S:** Provider rate limits and timeouts left the LLM router completing only 92-94% of requests, and 12-15% of structured outputs reached the client malformed.
**T:** Keep the AI working when a provider fails.
**A:** Added automatic failover across Gemini, OpenAI, OpenRouter, and NVIDIA NIM plus a retry-and-repair validation layer, all server-side so credentials never reach the client.
**R:** Completion 99.7%; malformed outputs under 0.3%.
**Provenance:** source: cv.md | article-digest.md | user-stated 2026-09-24.
**Best for:** Reliability, vendor risk, LLM infrastructure.

### 18. [Systems / Reliability] Resumable uploads up to 500 MiB
**Source:** cv.md
**S:** The model needs each document whole, so uploads up to 500 MiB had to survive network drops and client restarts.
**T:** Never hand the model a partial document.
**A:** Built a resumable pipeline with 8 MiB chunks on private Supabase Storage (row-level security) and Terraform-managed Cloud Run and KMS.
**R:** Uploads resume after drops and restarts, covered by the project's 302-test suite.
**Provenance:** source: cv.md | user-stated 2026-09-24.
**Best for:** Systems design, reliability, file handling.

---

## Pulumi (Open Source Contributor) -- PENDING

### 19. [Open Source] Pulumi contributions
**Source:** cv.md
**What is on the CV:** Go CLI features and fixes for multi-cloud provisioning (in maintainer review); Raft/Paxos consensus test cases for the distributed state synchronization layer (submitted).
**Status:** Harry says the tests target real Pulumi code, but the package path or PR link is not on file yet.
**Watch out:** Pulumi's public docs describe state as checkpoints plus lock files, with no Raft or Paxos. Before any interview, know exactly which package the tests target and what the Go CLI changes fix, or be ready to be asked "where is Raft in Pulumi?"

---

## Jobright / auto-apply "Anything else we should know?" answer

Use this verbatim in Jobright's profile field ("Add any details you want Jobright to consider when filling out applications") and in any other platform's open-ended "anything else" field. It is written to be pasted once and reused, so it stays generic across companies, unlike a per-job cover letter.

> I'm a CS senior at Georgia State (May 2027 grad) and the primary engineer for backend, cloud infrastructure, and AI systems at TiMoto AI, where I built a production AI agent that fixes bugs from PR diffs and logs (95% of fixes fully automated, the rest routed to human review) and the app's backend and infra from zero on AWS. I also interned on Chrome's Privacy Sandbox team at Google, where my C++/TypeScript work shipped to Chrome stable across 78 changes.
>
> I'm on an F-1 visa (OPT/CPT eligible now; will need H-1B sponsorship in the future). Please only submit me to roles that are open to sponsoring international candidates, now or later, rather than roles that explicitly exclude new sponsorship.
>
> I'm targeting Software Engineer, Backend/Distributed Systems, ML/AI Infrastructure, Systems Software, Platform/Cloud Infrastructure, or SRE roles at the new-grad or intern level, total comp $150K-$200K (walk-away minimum $140K). I'm open to onsite, hybrid, or remote, and open to relocating for the right role.
>
> When answering free-text questions on my behalf, only use facts from my resume; never invent metrics, employers, or projects I haven't listed.

**Provenance:** compensation and location from config/profile.yml (`compensation`, `location`); role targets from config/profile.yml `target_roles.primary`; work history facts from cv.md, confirmed 2026-09-24/25.

**Keep this updated when:** the compensation target, visa status, or grad date in config/profile.yml changes, or a new employer/role is added to cv.md.
