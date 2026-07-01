# Cover Letter — Everpure (Pure Storage) | Software Engineer Grad

---

Harry Nguyen
harrynguyenswe@gmail.com | +1 470-667-9000
linkedin.com/in/harrynguyen26 | timoto.ai

2026-05-28

Hiring Team — Engineering
Everpure / Pure Storage

---

Dear Pure Storage Engineering Team,

Data storage sits at the bottom of every computing stack — everything above it depends on it being fast, correct, and reliable. That constraint is what makes storage engineering some of the most demanding systems work in the industry, and it's why I want to build here. My background is in exactly the kind of C++ systems engineering your team does: process-boundary communication, concurrency primitives, memory layout, and performance measurement under production load.

At Google, I designed the C++ IPC transport layer that carries messages between Chrome's processes, serving over 3 billion active users at 10,000+ req/sec with sub-50ms p99 latency. I selected Protocol Buffers for schema evolution and zero-copy semantics — the same tradeoffs that matter in a high-throughput storage system where serialization overhead compounds at scale. I also profiled Chrome's settings navigation to isolate a mutex-contention bottleneck and replaced it with a lock-free concurrent trie, cutting p99 latency by 96%. Every optimization started with measurement: flamegraphs, latency percentiles, regression tests before any change landed in stable.

On the distributed systems side: I traced a production deadlock in TiMoto AI to a circular resource acquisition pattern between concurrent gRPC calls, redesigned the call sequencing, and restored 100% evaluation success rate at sub-50ms p99. At CoderPush I diagnosed a DynamoDB hot-partition failure at 9,000+ req/sec and redesigned the key strategy to recover 30% read throughput. These are the debugging workflows — trace, hypothesize, reproduce, fix, verify — that matter for storage systems where silent corruption or degraded replication can't be tolerated.

Pure Storage's engineering scope — from low-level flash hardware to wide-area replication — is the range I want to work in. Data deduplication and reclamation are fundamentally resource management problems under concurrent access; WAN replication is a consistency and fault-tolerance problem under partial failure. These are distributed systems problems with a storage-domain vocabulary, and my foundation covers the vocabulary of the underlying systems. I'm open to relocating to Santa Clara for the right team, and this is one.

Harry Nguyen
