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
