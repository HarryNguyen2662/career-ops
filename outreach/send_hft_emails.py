#!/usr/bin/env python3
"""
HFT/Quant cold email sender.
Usage:
  export SENDER_APP_PASSWORD="xxxx xxxx xxxx xxxx"
  python3 outreach/send_hft_emails.py --dry-run
  python3 outreach/send_hft_emails.py
"""

import smtplib, time, argparse, os, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

SENDER = "nguyenharry2662@gmail.com"

EMAILS = [
    {
        "to": ["abaker@janestreet.com", "mchung@janestreet.com", "gmurphy@janestreet.com", "jkim@janestreet.com"],
        "subject": "New Grad SWE (May 2027) — C++/systems, Google Chrome intern",
        "body": """Hi,

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad software engineering roles at Jane Street.

This summer I interned at Google on Chrome, where I shipped a C++ IPC transport layer with Protocol Buffers to the stable channel — 3B+ active users, sub-50ms p99, 10K+ req/sec. I also diagnosed a settings-navigation bottleneck at 1,200ms and eliminated it by implementing a lock-free concurrent trie — 96% latency reduction, zero production regressions across 25K+ lines of Chromium at 95% test coverage. Both projects went through formal design documents and senior engineer review before landing.

Outside of Google, I'm the primary engineer at TiMoto AI — I own a gRPC inter-service layer (resolved a production deadlock by tracing shared resource acquisition conflicts), a vLLM inference engine (zero OOM failures under concurrent load, sub-50ms p99), and AWS/Terraform infrastructure (99.9% uptime). I've also studied Raft/Paxos consensus for distributed state synchronization through open source contributions to Pulumi.

Jane Street's engineering culture — functional correctness, deep systems thinking, and getting things exactly right — is what I've been building toward. I'd love to learn about 2027 new grad or summer 2026 SWE/technology roles.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["ying@hudson-trading.com", "christina@hudson-trading.com"],
        "subject": "New Grad SWE (May 2027) — low-latency systems + C++, Google Chrome intern",
        "body": """Hi,

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad software engineering roles at Hudson River Trading.

My background is in low-latency systems: at Google I shipped a C++ IPC transport layer (Protocol Buffers, sub-50ms p99, 3B+ users) and implemented a lock-free concurrent trie that cut a p99 bottleneck from 1,200ms to under 50ms with zero production regressions. At TiMoto AI I own the gRPC inter-service layer and inference stack end-to-end — I resolved a production deadlock by tracing shared resource acquisition conflicts and redesigning call sequencing, achieving 100% success rate at sub-50ms p99.

The discipline of microsecond-level correctness and performance is something I've built toward through every project — C++, lock-free data structures, and explicit tradeoff decisions (Protocol Buffers vs. custom serialization, mutex vs. lock-free, JWT vs. session state). HRT's systems engineering work is exactly the environment I want to grow in.

I'd love to learn about 2027 new grad or summer 2026 technology roles.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["mvavaroutsos@drwholdings.com", "mschlie@drwholdings.com", "chawk@drwholdings.com"],
        "subject": "New Grad SWE (May 2027) — C++/low-latency systems, Google Chrome intern",
        "body": """Hi,

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad technology roles at DRW.

At Google I designed and shipped a C++ IPC transport layer with Protocol Buffers to Chrome stable — 3B+ users, sub-50ms p99. I diagnosed a 1,200ms p99 bottleneck in settings navigation and eliminated it with a lock-free concurrent trie (96% reduction, zero regressions, 95% test coverage). At TiMoto AI I've built and operated distributed production systems end-to-end: gRPC service layer (resolved production deadlock under concurrent load), vLLM inference engine (sub-50ms p99, zero OOM failures), and AWS/Terraform infrastructure (99.9% uptime).

DRW's technology work — building trading systems where correctness and latency are non-negotiable — is exactly the kind of engineering problem I want to work on. I'd love to learn about 2027 new grad or summer 2026 SWE openings.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["mmolloy@jumptrading.com", "esimonovich@jumptrading.co", "caplume@jumptrading.com"],
        "subject": "New Grad SWE (May 2027) — low-latency C++/systems, Google Chrome intern",
        "body": """Hi,

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad software engineering roles at Jump Trading.

My systems background: at Google I shipped a C++ IPC transport layer (Protocol Buffers) to Chrome stable — 3B+ users, sub-50ms p99, 10K+ req/sec — and fixed a p99 latency bottleneck using a lock-free concurrent trie (1,200ms → 48ms, zero regressions, 95% test coverage). At TiMoto AI I own a gRPC inter-service layer and have directly debugged production deadlocks under concurrent load — tracing shared resource acquisition patterns and redesigning call sequencing until the system behaved correctly under all conditions.

Latency and correctness as hard constraints, not preferences — that's been the common thread in my work. It's also the discipline that makes trading systems engineering distinct. I'd love to connect about 2027 new grad or summer 2026 SWE roles at Jump.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["Sharon.Lin@twosigma.com", "tommy.grassey@twosigma.com", "Liam.Smith@twosigma.com", "priscilla.huh@twosigma.com"],
        "subject": "New Grad SWE (May 2027) — systems + distributed infra, Google Chrome intern",
        "body": """Hi {first_name},

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad software engineering roles at Two Sigma.

At Google I shipped a C++ IPC transport layer (Protocol Buffers) to Chrome's stable channel — 3B+ users, sub-50ms p99 — and implemented a lock-free concurrent trie to eliminate a 1,200ms latency bottleneck (96% reduction, zero regressions, 95% test coverage across 25K+ lines of Chromium). At TiMoto AI I've built distributed production systems end-to-end: gRPC inter-service layer (debugged and fixed a production deadlock under concurrent calls), vLLM inference engine with PagedAttention (zero OOM failures), and AWS/Terraform infrastructure (99.9% uptime, multi-AZ). I've also studied Raft/Paxos consensus through contributions to Pulumi's distributed state synchronization layer.

Two Sigma's combination of rigorous engineering and quantitative thinking is exactly the environment I want to be in. I'd love to learn about 2027 new grad SWE openings and whether there are roles that fit my background.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["Max.Ma@deshaw.com", "mama@deshaw.com", "Sumya.Rashid@deshaw.com"],
        "subject": "New Grad SWE (May 2027) — C++/systems, Google Chrome intern",
        "body": """Hi {first_name},

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad software engineering roles at D.E. Shaw.

At Google I designed and shipped a C++ IPC transport layer with Protocol Buffers to Chrome stable (3B+ users, sub-50ms p99) and fixed a p99 settings-navigation bottleneck via a lock-free concurrent trie — 96% latency reduction, zero production regressions at 95% test coverage. At TiMoto AI I'm the primary engineer on a 3-person team, owning gRPC inter-service layer (resolved a production deadlock through resource acquisition analysis), vLLM inference engine (sub-50ms p99, zero OOM), and AWS/Terraform infrastructure (99.9% uptime).

D.E. Shaw's engineering culture — technical depth, rigor, and working at the intersection of systems and quantitative thinking — is exactly what I'm looking for in a new grad role. I'd love to learn about 2027 openings.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["MMancuso@us.flowtraders.com", "athieu@flowtraders.jobs"],
        "subject": "New Grad SWE (May 2027) — low-latency systems + C++, Google Chrome intern",
        "body": """Hi,

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad technology roles at Flow Traders.

My background: Google Chrome SWE intern (C++ IPC transport layer, Protocol Buffers, 3B+ users, sub-50ms p99; lock-free concurrent trie cutting a 1,200ms p99 bottleneck by 96%, zero regressions). Currently primary engineer at TiMoto AI — gRPC layer, vLLM inference (sub-50ms p99, zero OOM), AWS/Terraform (99.9% uptime). I've debugged production deadlocks under concurrent load and care deeply about both correctness and latency as hard engineering constraints.

Flow Traders' focus on technology-driven market making and low-latency infrastructure is exactly the kind of work I want to be doing. I'd love to learn about 2027 new grad openings.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["Meg.mcleish@oldmissioncapital.com"],
        "subject": "New Grad SWE (May 2027) — C++/systems, Google Chrome intern",
        "body": """Hi Meg,

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad software engineering or technology roles at Old Mission Capital.

At Google this summer I shipped a C++ IPC transport layer (Protocol Buffers) to Chrome stable — 3B+ users, sub-50ms p99 — and eliminated a p99 latency bottleneck with a lock-free concurrent trie (96% reduction, zero regressions, 95% test coverage). At TiMoto AI I own a production gRPC inter-service layer, vLLM inference engine, and AWS/Terraform infrastructure end-to-end. I've resolved a production deadlock under concurrent load by tracing shared resource acquisition conflicts — the kind of systematic debugging that matters in trading systems.

I'd love to learn about 2027 new grad or summer 2026 roles at Old Mission.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["cparkwinebrake@fiveringscapital.com"],
        "subject": "New Grad SWE (May 2027) — C++/low-latency, Google Chrome intern",
        "body": """Hi,

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad roles at Five Rings.

My background is in low-latency systems and C++: at Google I shipped a C++ IPC transport layer (Protocol Buffers, 3B+ users, sub-50ms p99) and implemented a lock-free concurrent trie that cut a p99 bottleneck by 96% with zero production regressions. At TiMoto AI I've built and operated distributed production systems including a gRPC layer (debugged a production deadlock under concurrent load) and an inference engine at sub-50ms p99.

Five Rings' culture of deep technical work and quantitative rigor is exactly what I'm looking for. I'd love to connect about new grad or summer 2026 software engineering roles.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["anja.kitzmiller@akunacapital.com"],
        "subject": "New Grad SWE (May 2027) — C++/systems, Google Chrome intern",
        "body": """Hi Anja,

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad software engineering roles at Akuna Capital.

At Google I designed and shipped a C++ IPC transport layer (Protocol Buffers) to Chrome stable — 3B+ users, sub-50ms p99 — and fixed a 1,200ms p99 bottleneck with a lock-free concurrent trie (96% latency reduction, zero regressions, 95% test coverage). At TiMoto AI I own a production gRPC service layer, vLLM inference engine, and AWS/Terraform infrastructure. I've debugged production deadlocks under concurrent load and care about both performance and correctness as first-class constraints.

Akuna's engineering-forward culture and the technical depth required in options market making is exactly the environment I want to grow in as a new grad. I'd love to learn about 2027 or summer 2026 openings.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["anne.olmstead@imc.com", "lauren.bachman@imc.com", "karlie.okeefe@imc.com"],
        "subject": "New Grad SWE (May 2027) — low-latency systems + C++, Google Chrome intern",
        "body": """Hi {first_name},

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad software engineering roles at IMC.

At Google I shipped a C++ IPC transport layer with Protocol Buffers to Chrome's stable channel — 3B+ users, sub-50ms p99, 10K+ req/sec — and eliminated a p99 latency bottleneck using a lock-free concurrent trie (96% reduction, zero production regressions, 95% test coverage across 25K+ lines of Chromium). At TiMoto AI I'm the primary engineer on a 3-person team: I own a gRPC inter-service layer (resolved a production deadlock by tracing shared resource acquisition conflicts), a vLLM inference engine (zero OOM failures, sub-50ms p99), and AWS/Terraform infrastructure (99.9% uptime, multi-AZ).

IMC's technology team — building low-latency trading infrastructure where correctness and performance are both non-negotiable — is exactly the kind of engineering challenge I want to take on as a new grad. I'd love to learn about 2027 new grad or summer 2026 SWE openings.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
]

# ── helpers ────────────────────────────────────────────────────────────────────

def first_name(email: str) -> str:
    local = email.split("@")[0]
    for sep in [".", "_", "-"]:
        if sep in local:
            return local.split(sep)[0].capitalize()
    return local.capitalize()

def build_body(body: str, addr: str) -> str:
    return body.replace("{first_name}", first_name(addr))

def log(path, to, subject):
    with open(path, "a") as f:
        f.write(f"{datetime.now().isoformat()}\t{to}\t{subject}\n")

# ── main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--delay", type=float, default=4.0)
    parser.add_argument("--only", type=str, help="Filter by email substring")
    args = parser.parse_args()

    password = os.environ.get("SENDER_APP_PASSWORD", "")
    if not args.dry_run and not password:
        print("ERROR: export SENDER_APP_PASSWORD='xxxx xxxx xxxx xxxx'")
        sys.exit(1)

    log_file = os.path.join(os.path.dirname(__file__), "sent_log.tsv")

    # flatten to individual sends
    queue = []
    for entry in EMAILS:
        for addr in entry["to"]:
            if args.only and args.only.lower() not in addr.lower():
                continue
            queue.append((addr, entry["subject"], build_body(entry["body"], addr)))

    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Sending {len(queue)} emails from {SENDER}")
    print("=" * 60)

    if args.dry_run:
        for to, subject, body in queue:
            print(f"  → {to}")
            print(f"    Subject : {subject}")
            print(f"    Opening : {body.splitlines()[0]}")
            print()
        print(f"Total: {len(queue)} emails would be sent.")
        return

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER, password)
        sent = failed = 0
        for i, (to, subject, body) in enumerate(queue, 1):
            try:
                msg = MIMEMultipart("alternative")
                msg["From"] = SENDER
                msg["To"] = to
                msg["Subject"] = subject
                msg.attach(MIMEText(body, "plain"))
                smtp.sendmail(SENDER, to, msg.as_string())
                log(log_file, to, subject)
                sent += 1
                print(f"[{i}/{len(queue)}] ✓ {to}")
                if i < len(queue):
                    time.sleep(args.delay)
            except Exception as e:
                failed += 1
                print(f"[{i}/{len(queue)}] ✗ {to} — {e}")

    print(f"\nDone. Sent: {sent} | Failed: {failed}")
    print(f"Log: {log_file}")

if __name__ == "__main__":
    main()
