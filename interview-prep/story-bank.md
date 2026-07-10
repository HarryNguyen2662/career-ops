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

### [Concurrency / Debugging] gRPC Deadlock Fix at TiMoto
**Source:** Report #031 -- Dropbox -- Infrastructure Software Engineer
**S:** Production AI evaluation service receiving concurrent gRPC calls from 3 clients hitting intermittent deadlocks.
**T:** Debug and eliminate the deadlock causing evaluation failures in production.
**A:** Traced shared resource acquisition conflict in gRPC handler sequencing; identified circular dependency in lock acquisition order; redesigned call sequencing to enforce consistent ordering.
**R:** 100% evaluation success rate at sub-50ms p99, zero recurrence.
**Reflection:** Always instrument concurrent call paths before launch -- a lock acquisition order diagram would have caught this before production.
**Best for questions about:** Debugging, production incidents, concurrency, distributed systems, root-cause analysis

### [Performance / OS Internals] Lock-Free Trie at Google Chrome
**Source:** Report #031 -- Dropbox -- Infrastructure Software Engineer
**S:** Chrome settings search hitting 1,200ms p99 for power users -- root cause was mutex contention on trie traversal.
**T:** Reduce p99 to target latency without correctness regression.
**A:** Identified contention hotspot via profiling; replaced mutex-protected trie with lock-free concurrent structure; verified linearizability before shipping.
**R:** 96% latency reduction (1,200ms to ~50ms p99), zero production regressions, shipped to Chrome stable.
**Reflection:** Lock-free structures need proof by construction, not just benchmarks -- verified linearizability as a correctness condition before shipping.
**Best for questions about:** Performance optimization, OS internals, mutex/semaphore, proactive problem-finding

### [Infrastructure / Reliability] Multi-AZ Circuit Breaker at TiMoto
**Source:** Report #031 -- Dropbox -- Infrastructure Software Engineer
**S:** Single-AZ backend with no failover -- zone failure would cause full outage.
**T:** Design and implement multi-AZ failover with auto-rollback on health check failure.
**A:** Designed multi-AZ ECS Fargate topology with Terraform IaC, CloudWatch alarms, circuit breaker pattern, auto-rollback.
**R:** 99.9% uptime, 44% cost reduction ($40--60/month), zero unplanned outages post-launch.
**Reflection:** AZ isolation is cheaper to design in at the start than to retrofit -- treat it as a Day 1 infrastructure requirement.
**Best for questions about:** Reliability, SRE, infrastructure design, cost optimization, Terraform/IaC

### [Full-Stack / AI Feature] vLLM Serving Architecture at TiMoto
**Source:** Report #035 -- Gen Digital -- Software Engineer (Avast)
**S:** TiMoto needed concurrent LLM inference without OOM errors under simultaneous user load; naive batching caused KV cache exhaustion.
**T:** Evaluate serving options and build a production inference layer.
**A:** Compared naive inference vs vLLM/PagedAttention; selected vLLM for dynamic KV cache management; deployed with continuous batching and gRPC front-end.
**R:** Zero OOM failures at production traffic, sub-50ms p99 inference, 100% evaluation success rate.
**Reflection:** Document serving architecture decisions -- future team members need the "why" not just the config file.
**Best for questions about:** AI feature development, architecture decisions, ML infrastructure, tradeoff analysis, full-stack build

### [Front-End / Observer Pattern] React State Decoupling at Google Chrome
**Source:** Report #035 -- Gen Digital -- Software Engineer (Avast)
**S:** Chrome settings feature delivery was slowing as teams coupled UI state to rendering -- changes in one part broke others, requiring cascading fixes.
**T:** Decouple state propagation from rendering across 25K+ lines of Chromium TypeScript/React.
**A:** Designed observer-pattern event system; all UI components subscribe to state events rather than reading shared mutable state directly.
**R:** 68% feature delivery acceleration, 95% test coverage, zero regressions shipped.
**Reflection:** Decouple state model early -- retrofitting at Chromium scale was harder than it needed to be; this should be a design requirement on any React codebase above 5K lines.
**Best for questions about:** Front-end architecture, React, TypeScript, design patterns, OOP, working at scale

### [Onboarding / Codebase Mastery] Joining Chromium at 25K+ Lines
**Source:** Report #039 -- Meta -- Software Engineer
**S:** Joined Google Chrome team as intern facing a 25,000+ line TypeScript/React Chromium codebase with no prior Chromium context.
**T:** Ramp quickly enough to ship a meaningful feature within the internship window.
**A:** Prioritized reading design docs and existing code reviews over writing code in week 1; followed Chrome's internal code review culture rigorously; got changes reviewed and adopted by senior Chrome engineers.
**R:** 68% feature delivery acceleration; changes merged into production branch; 95% test coverage.
**Reflection:** Reading code is 70% of the job on large codebases -- invest in understanding existing patterns before writing new ones.
**Best for questions about:** Onboarding, ramp-up, large codebases, code review culture, learning quickly

### [Database / Debugging] N+1 Fix at Develop for Good
**Source:** Report #039 -- Meta -- Software Engineer
**S:** Production API degrading to 3s+ response time on large datasets; users abandoning the page.
**T:** Diagnose root cause and fix without breaking existing API contracts.
**A:** Enabled query logging; identified N+1 pattern (one query per record, not per page); redesigned with PostgreSQL indexing and batch queries.
**R:** Sub-100ms response time on 10,000+ records, zero API contract changes.
**Reflection:** Query planning review should be part of any PR that touches data access -- this should have been caught in code review, not production.
**Best for questions about:** Debugging, SQL, performance, backend, production problem-solving

### [Incident Management / Culture] Post-Mortem Culture at TiMoto
**Source:** Report #042 -- Plaid -- Software Engineer, Backend
**S:** After resolving the gRPC deadlock incident, no documented process existed for future incidents on the 3-person team.
**T:** Build repeatable incident response culture from scratch.
**A:** Wrote runbooks for top 5 failure modes; conducted post-mortems with structured learning; introduced on-call rotation shared across the team.
**R:** 68% reduction in MTTI (mean time to identify) on subsequent incidents, verified with TiMoto leadership; team now has playbook for all recurring failure modes.
**Reflection:** The real output of an incident isn't the fix -- it's the runbook. A fix you can't repeat at 2am isn't a real fix.
**Best for questions about:** Incident management, SRE culture, team building, leadership, reliability, post-mortems

### [Collaboration / Cross-Functional] Design Doc Review at Google Chrome
**Source:** Report #042 -- Plaid -- Software Engineer, Backend
**S:** Chrome settings IPC transport layer design needed sign-off from Chrome infrastructure team before shipping to stable.
**T:** Write design document and get technical alignment from senior Chrome engineers in the review process.
**A:** Documented design tradeoffs (Protobuf vs custom serialization, schema evolution rationale); incorporated feedback from senior engineers into final implementation.
**R:** Changes adopted into production branch; 95% test coverage validated; shipped to Chrome stable.
**Reflection:** Design docs force you to articulate tradeoffs you haven't fully thought through -- writing "why not X" is often more valuable than writing "why Y".
**Best for questions about:** Collaboration, design docs, cross-functional alignment, code review culture, technical communication

### [Observability / SRE] Building Observability Stack from Zero at TiMoto
**Source:** Report #048 -- EliseAI -- Software Engineer (New Grads 2025-2026)
**S:** TiMoto's ML serving and gRPC layers had no observability -- when incidents happened, root-cause analysis started from scratch with no signal.
**T:** Build an observability stack that makes production incidents tractable on a 3-person team.
**A:** Deployed CloudWatch dashboards for AWS-layer health, Prometheus scraping for gRPC and ML serving metrics, Grafana panels for latency/throughput/error visualization; documented runbooks for top failure modes; established on-call rotation.
**R:** Triage time from unknown -- root-cause reduced to under 15 minutes on subsequent incidents; team has playbook for all recurring failure modes.
**Reflection:** Observability is not a nice-to-have -- it's what makes on-call survivable and prevents the same bug from recurring. Instrument before you need it.
**Best for questions about:** SRE, observability, Prometheus, Grafana, CloudWatch, production systems, incident response, engineering best practices
