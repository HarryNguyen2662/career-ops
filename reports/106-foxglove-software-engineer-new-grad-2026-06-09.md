# Evaluation: Foxglove — Software Engineer, New Grad

**Date:** 2026-06-09
**URL:** https://jobs.ashbyhq.com/foxglove/def61478-8b86-43e5-b27b-be7b76900449
**Archetype:** Developer Tools / Platform Infrastructure Engineer (robotics data pipeline context)
**Score:** 3.2/5
**Legitimacy:** High Confidence
**PDF:** output/106-foxglove-software-engineer-new-grad-harry-nguyen-2026-06-09.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Developer Tools / Platform Infrastructure Engineer — data ingestion, observability, multi-cloud infrastructure for robotics and autonomous systems |
| Domain | Robotics data infrastructure — tools used by robotics engineers to ingest, store, query, replay, and analyze massive volumes of multimodal sensor data from production fleets |
| Function | Build — on-device software (robots), cloud data pipelines (batch + real-time), low-latency playback systems, search/query features for ML training data |
| Seniority | New Grad (BS/MS, recent or graduating 2026) — explicit new grad label |
| Location | San Francisco, CA — onsite |
| Comp | $150,000–$180,000 base + equity (SWE level); $183K–$210K (Senior level) |
| Company | Foxglove — Series B; builds observability, visualization, and data infrastructure for robotics teams |
| TL;DR | New grad infrastructure role at a Series B robotics dev-tools company. Foxglove builds data tools *for* robotics engineers — not robots themselves. Harry's C++/TypeScript, distributed systems, observability stack (Prometheus/Grafana), multi-cloud, Kubernetes, and Pulumi OSS contribution map directly to the actual work. Primary gap: robotics domain experience (ROS/AV/embedded) is explicitly required. Grad timing (May 2027 vs "graduating in 2026") is a soft mismatch. H-1B unconfirmed at Series B scale. Apply — frame as "I build the data infrastructure your tools are built on." |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| Rust, C++, or TypeScript | C++: Chrome IPC transport layer (3B users, sub-50ms p99); TypeScript: Chrome React/observer system (25K+ lines); Rust in skills | ✅ C++ and TypeScript direct; Rust in skills (no project) |
| Distributed systems, cloud infra, data-intensive applications | TiMoto: gRPC, exactly-once delivery, multi-AZ ECS Fargate, circuit breakers, 99.9% uptime; Pulumi: multi-cloud (AWS/Azure/GCP) | ✅ Direct |
| Multi-cloud (GCP, AWS, Azure) | TiMoto: AWS (ECS Fargate, EKS, EC2, S3, RDS), GCP in skills; Pulumi: AWS/Azure/GCP provisioning | ✅ Direct |
| Kubernetes | Skills section; EKS in AWS stack | ✅ Listed (no standalone K8s project in CV) |
| Observability, monitoring, developer tooling | TiMoto: CloudWatch + Prometheus + Grafana for 99.9% uptime SLO; Pulumi OSS developer tools contribution | ✅ Direct |
| SQL databases, query engines, data-intensive systems | TiMoto: PostgreSQL + Redis data layer; Develop for Good: PostgreSQL N+1 → sub-100ms composite indexing | ✅ Direct |
| REST APIs or user-facing interfaces in React (bonus) | TiMoto: FastAPI/Django REST APIs; Chrome: TypeScript/React event-driven system | ✅ Bonus covered |
| Terraform, Kubernetes, cloud admin (bonus) | TiMoto: Terraform IaC (ECS Fargate with explicit lifecycle management); EKS in stack | ✅ Bonus covered |
| Agentic coding tools (Claude Code / Cursor) | Claude Code listed in AI Dev Tools; used daily in TiMoto workflow | ✅ Direct — explicitly listed in their stack |
| Interesting personal projects solving real problems (bonus) | Pulumi OSS contributor — Go CLI features enabling multi-cloud provisioning under active review | ✅ Bonus |
| **Robotics experience (ROS, AV, embedded systems)** | **Zero robotics exposure in CV, profile, or education** | ❌ Hard gap — required, not nice-to-have |
| On-device/embedded software with resource constraints | Chrome C++ IPC: sub-50ms p99, performance-critical systems programming (adjacent but not embedded) | ⚠️ Adjacent — Chrome is resource-aware, not embedded |
| Sensor data pipelines (lidar, camera, IMU) (bonus) | Zero exposure | ❌ Not expected but relevant context |
| Graduating in 2026 | Harry graduates May 2027 | ⚠️ Timing mismatch — one year off |
| BS/MS CS or related | Georgia State BS CS, GPA 3.75, Expected May 2027 | ✅ Direct |

**Gaps:**

1. **Robotics domain experience** (hard): "Hands-on experience with robotics systems — through internships, research, or significant academic projects (e.g., ROS, autonomous vehicles, embedded systems, robot perception/planning)." This is the primary required qualification Harry lacks entirely. Foxglove is a developer tools company — they build tooling *for* robotics engineers — but they still expect their engineers to understand the domain deeply enough to build the right tools. Mitigation is thin: Harry can frame observability + data pipeline experience as structurally similar to the telemetry and playback systems Foxglove builds. But without any ROS/AV/embedded contact points, the interview story is weak in the robotics context sections.

2. **Rust projects** (medium): Rust is the first language in the stack and appears throughout their backend. Harry has Rust in skills but no Rust project in CV. Mitigation: C++ at Chrome scale demonstrates low-level systems programming proficiency. Rust is learnable from C++. Can note "learning Rust" in cover letter.

3. **On-device/embedded software** (medium): "Building reliable, low-resource software to run on a wide range of devices." Chrome C++ is performance-critical (sub-50ms p99, lock-free structures) but runs on full-featured desktop OSes, not resource-constrained embedded systems. Adjacent framing available.

4. **Graduation timing** (soft): JD says "recent graduates or graduating in 2026." Harry graduates May 2027. One year past the stated window. Per policy: still apply and clarify timing in application — many companies interpret this loosely for early-career hires.

5. **H-1B at Series B** (risk): Foxglove is a ~$25M Series B startup (~20-50 employees based on company stage). Small companies have lower H-1B approval rates and capacity. Must ask in first recruiter contact. Not a hard blocker per policy.

---

## C) Level and Strategy

**Level detected:** New Grad (explicit label). $150K–$180K SWE band confirms entry-level. This is genuinely a new grad role — one of the cleaner fits from a seniority perspective.

**Core pitch:**
> "Foxglove builds the data infrastructure for robots. I build data infrastructure too — distributed pipelines, real-time observability, multi-cloud systems. The difference is I haven't shipped it for robots yet. The Rust/C++/TypeScript stack, Kubernetes, Terraform, PostgreSQL — that's my stack. I've used Claude Code to ship production systems faster. I don't have ROS internship experience, but I can build the data layer you need and I'll learn the robotics domain faster than anyone coming from the other direction."

**On robotics gap:**
> "I don't have a robotics internship. What I have is a production distributed data system (gRPC, multi-AZ, PostgreSQL, observability), C++ at 3B-user scale, and Pulumi OSS contributions in developer tooling — which is exactly what Foxglove builds. My learning curve is on the robotics domain, not on the infrastructure. For a company that builds the tools rather than the robots, that's the right gap to have."

**On Rust:**
> "Rust is in my skills — I understand the ownership model and borrow checker. My production C++ work at Chrome (lock-free trie, IPC transport) required the same low-level reasoning Rust enforces. I'm actively ramping up on Rust for systems work."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Foxglove stated range (SWE) | $150,000–$180,000 + equity |
| Foxglove stated range (Senior) | $183,000–$210,000 + equity |
| Harry target | $150K–$200K |
| Harry minimum | $140K |
| Assessment | Floor ($150K) hits minimum exactly; ceiling ($180K) within target; equity at Series B adds upside risk/reward |
| Foxglove equity | Series B company — unpriced equity value; illiquid until IPO/acquisition; meaningful if company scales |
| H-1B sponsorship | Unconfirmed — Series B, ~20-50 employees; must verify in first recruiter contact |
| Robotics dev-tools market | Growing rapidly — autonomous vehicles, factory automation, warehouse robotics all scaling; Foxglove positioned as infrastructure layer |

**Comp note:** The $150K floor is bare minimum for Harry. Negotiate to $165K–$175K target citing market data for new grad distributed systems engineers (Levels.fyi: infra new grads at Series B typically $160K–$180K base). Equity is the upside lever.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet 1 | Distributed systems framing | Reframe: "Led backend, cloud infrastructure, and ML serving for a 3-person engineering team — designed and operated batch and real-time data pipelines, ingesting and serving production ML workloads at sub-50ms p99" | Batch + real-time data ingestion is exactly what Foxglove does for sensor data |
| 2 | TiMoto bullet 4 | Circuit breaker + uptime SLO | Keep but add observability: "CloudWatch + Prometheus + Grafana observability layer for production fleet monitoring — 99.9% uptime SLO; telemetry across gRPC, PostgreSQL, and ML serving layers" | Fleet monitoring + telemetry = Foxglove's core product category |
| 3 | Chrome bullet 1 | C++ IPC with Protobuf | Emphasize systems: "Designed C++ IPC transport layer with Protocol Buffers for low-latency inter-process communication — selected Protocol Buffers for schema evolution; shipped to Chrome stable channel at sub-50ms p99, 10K+ req/sec across 3B+ users" | Low-latency, high-throughput data transport = direct analog to robotics telemetry |
| 4 | Pulumi project | OSS CLI framing | Lead with: "Submitted Go CLI features enabling multi-cloud (AWS/Azure/GCP) provisioning — developer tooling contribution under active review by core maintainers" | Foxglove is a developer tools company; OSS developer tools contribution is directly on-brand |
| 5 | Skills section | AI/ML infra first | Reorder: Languages (C++, Rust, TypeScript first), then Distributed Systems, then Cloud & Infra (Kubernetes prominent), then Frameworks & Databases, then ML last | Role is infrastructure/systems first; Rust and C++ should be visible immediately |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Data-intensive distributed systems | TiMoto gRPC + data pipeline | Production ML evaluation pipeline with concurrent gRPC inter-service calls dropping data under load | 100% exactly-once delivery at sub-50ms p99 | Traced happens-before graph; identified lock ordering violation; redesigned call sequencing with explicit lock hierarchy | Zero data loss at production traffic | Data loss in async pipelines is silent. The only way to find it is to instrument every handoff point. That's exactly the observability problem Foxglove helps robotics teams solve — you need to know which data was collected, which was transmitted, and which was dropped |
| 2 | Real-time observability and telemetry | TiMoto CloudWatch + Prometheus | Production distributed system needed multi-layer visibility: infra health + ML pipeline correctness | Two-layer observability across infra and data pipeline | CloudWatch for infra SLOs; Prometheus + Grafana for pipeline correctness; LLM-as-a-judge eval for output quality | 99.9% uptime SLO; zero pipeline errors | The hardest observability problem is knowing what you don't know. Foxglove lets robotics teams answer "what actually happened?" — that's the same question I was answering for our ML pipeline |
| 3 | Multi-cloud infrastructure | TiMoto AWS + Pulumi multi-cloud | TiMoto needed reliable infra at minimal cost; Pulumi needed multi-cloud provisioning | 99.9% uptime, 44% cost cut; AWS/Azure/GCP provisioning in OSS | Terraform IaC for ECS Fargate; circuit breaker + auto-rollback; Pulumi Go CLI for multi-cloud | 44% cost reduction; Pulumi PR under active review | Cloud infrastructure is a tradeoff problem between reliability, cost, and operability. The same tradeoff applies to Foxglove's multi-cloud architecture — you need to run in customer cloud accounts, which means reproducible IaC that works across providers |
| 4 | Low-latency data transport | Chrome C++ IPC | Chrome extensions needed cross-process data transport with schema evolution | Sub-50ms p99 at 10K+ req/sec to 3B+ users | Protocol Buffers over custom serialization for schema evolution + cross-language compatibility; IPC transport layer in C++ | Shipped to Chrome stable; zero post-ship regressions | Schema evolution is the long-term problem that bites distributed systems. Choose serialization formats for what happens after v1, not for how fast you can write v1. Robotics data formats (ROS bags, MCAP) have the same versioning challenge |
| 5 | Developer tooling for engineers | Pulumi OSS contribution | Pulumi needed multi-cloud CLI features | Enable AWS/Azure/GCP provisioning from the CLI | Submitted Go CLI features and bug fixes; studied Raft/Paxos consensus for distributed state model | Active review by core maintainers | The best developer tools reduce cognitive load. Pulumi's CLI design choice — same code for all clouds — reduces the mental model engineers carry. Foxglove's design principle is the same: one tool for all robot data sources |
| 6 | PostgreSQL + data-intensive queries | Develop for Good N+1 | Production API degrading to 3s+ on 10K+ records | Sub-100ms for 10,000+ records | Diagnosed N+1 ORM pattern; redesigned with composite PostgreSQL indexing and eager loading | 30× latency improvement | N+1 is the database equivalent of O(n) in a hot loop — invisible at small scale, catastrophic at production scale. For Foxglove's query layer over robotics data, the same query planning discipline applies |

**Recommended case study:** TiMoto observability stack + Pulumi multi-cloud. Frame as: "I built a multi-layer observability system from scratch for a production distributed application. Your platform does the same for robotics fleets — my stack is the same (PostgreSQL, K8s, multi-cloud), my gap is the robotics domain knowledge, and I learn domains by building production systems in them."

**Red-flag questions:**
- *"You don't have robotics experience."* → "I build the infrastructure that robotics tools like yours are built on. I've shipped data pipelines, multi-cloud infra, observability systems, and developer tooling — those are the actual systems your engineering team works on. The robotics domain is my learning curve, not the infrastructure. I'll get up to speed on ROS and sensor data formats in the first month; rebuilding the infrastructure knowledge would take much longer."
- *"We prefer engineers graduating in 2026."* → "I graduate May 2027 — one year out from your stated window. I'm applying because the technical scope fits exactly, and I'm already operating at production SWE scope with TiMoto and Google Chrome. Would the team consider a May 2027 start or an earlier start if I can arrange a leave of absence?"
- *"Do you know Rust?"* → "It's in my skills — I understand ownership and the borrow checker from C++ background. My Chrome C++ work (lock-free trie, IPC transport) required the same reasoning Rust enforces by default. I'm actively ramping up Rust for systems work and it's the first language I want to grow in."
- *"Work authorization?"* → "F-1 status — OPT eligible after graduation. Can you confirm Foxglove's H-1B sponsorship policy? I want to make sure we're aligned on the long-term path."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active ("Apply for this Job") on Ashby | Positive |
| Comp disclosed | $150K–$180K (SWE), $183K–$210K (Senior) explicitly stated with two-level breakdown | Positive |
| JD specificity | Named stack (Rust, TypeScript, PostgreSQL, Kubernetes), named products (MCAP files, sensor data), org context | Positive |
| Company status | Foxglove — Series B; active developer tools company; real product used by robotics teams (ROS, MCAP format) | Positive |
| New grad label | "Software Engineer, New Grad" — targeted hire, not evergreen | Positive |
| Claude Code in stack | "Agentic coding tools (Claude Code / Cursor)" explicitly listed — team actively uses these tools; genuine modern tech culture signal | Positive |
| H-1B | Series B startup (~20-50 employees) — sponsorship unconfirmed; small companies have lower H-1B bandwidth | ⚠️ Ask early |

---

## Keywords extracted

New grad, software engineer, robotics, autonomous systems, Rust, TypeScript, C++, PostgreSQL, Kubernetes, GCP, AWS, Azure, multi-cloud, data infrastructure, observability, telemetry, real-time data, batch pipelines, low-latency, ROS, sensor data, MCAP, developer tools, Terraform, Claude Code, Series B, San Francisco, on-site

---

## Machine Summary

```yaml
company: Foxglove
role: Software Engineer, New Grad
date: 2026-06-09
url: https://jobs.ashbyhq.com/foxglove/def61478-8b86-43e5-b27b-be7b76900449
score: 3.2
archetype: Developer Tools / Platform Infrastructure Engineer (robotics data pipeline context)
location: "San Francisco, CA — onsite; relocation from Atlanta required"
comp_range: "$150K–$180K base + equity (Series B); floor at Harry's $140K minimum; negotiate toward $165K–$175K"
visa_risk: "F-1 — H-1B UNCONFIRMED at Series B scale (~20-50 employees); ask in first recruiter contact"
legitimacy: High Confidence
recommendation: "Apply (3.2/5) — new grad label is an exact fit; C++/TypeScript/distributed systems/observability/multi-cloud maps directly to actual work. Primary risk: robotics domain gap (ROS/AV/embedded explicitly required). Frame as 'I build the infrastructure your tools are built on.' H-1B unconfirmed — must ask early. Grad timing (May 2027 vs 2026) is soft risk."
```
