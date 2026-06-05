#!/usr/bin/env python3
"""
Cold email sender for career-ops outreach.

Setup:
  1. Enable Gmail App Password: myaccount.google.com/apppasswords
  2. Set environment variables:
       export SENDER_EMAIL="nguyenharry2662@gmail.com"
       export SENDER_APP_PASSWORD="xxxx xxxx xxxx xxxx"
  3. Run dry-run first:  python3 send_emails.py --dry-run
  4. Send for real:      python3 send_emails.py
"""

import smtplib
import time
import argparse
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# ─── EMAILS ────────────────────────────────────────────────────────────────────

EMAILS = [
    # ── BIG TECH ──────────────────────────────────────────────────────────────
    {
        "to": ["robert_graham@apple.com", "sze@apple.com", "orin_rottman@apple.com", "Lance_Perry@apple.com"],
        "individual": True,  # send one per address
        "subject": "New Grad SWE (May 2027) — C++/systems, Google Chrome intern",
        "body": """Hi {first_name},

I'm Harry, a Computer Science student at Georgia State University graduating May 2027. I interned at Google on Chrome this past summer and wanted to reach out about new grad engineering roles at Apple.

At Google, I designed and shipped a C++ IPC transport layer with Protocol Buffers to Chrome's stable channel — 3B+ active users, sub-50ms p99, 10K+ req/sec. I also identified and fixed a p99 settings-navigation bottleneck (1,200ms) by implementing a lock-free concurrent trie, achieving 96% latency reduction with zero production regressions across 25K+ lines of Chromium. All work went through design documents, code review, and 95% test coverage before landing — the bar Chrome holds is one I want to keep working at.

Outside of Google, I'm the primary engineer at TiMoto AI (3-person team), running distributed production systems end-to-end: vLLM inference, gRPC service layer, AWS/Terraform infrastructure, 99.9% uptime.

I'm particularly interested in Apple's systems, platform, or performance engineering teams — the kind of work that demands correctness and reliability at scale. I'd love to learn if there are 2027 new grad openings in that space, and I'm happy to share my resume.

Thank you for your time.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["oduhon@google.com", "oduhon@xwf.google.com", "brennaman@xwf.google.com"],
        "individual": True,
        "subject": "Following up on Chrome internship — New Grad 2027 (Harry Nguyen)",
        "body": """Hi {first_name},

I'm Harry — I interned on the Chrome team at Google this past summer (May–Aug 2025). I wanted to reach out directly about full-time new grad opportunities for May 2027.

During my internship I shipped a C++ IPC transport layer with Protocol Buffers to Chrome stable (3B+ users, sub-50ms p99), and eliminated a p99 settings-navigation bottleneck via a lock-free concurrent trie (96% latency reduction, zero regressions). My changes were reviewed and adopted into the production branch by senior Chrome engineers at 95% test coverage.

I genuinely loved working at Google — the engineering bar, the scale, and the team. I'd love to come back as a new grad and would really appreciate any guidance on the 2027 new grad process or teams that might be a good fit given my background in systems and performance engineering.

Happy to chat whenever convenient.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["berniceau@meta.com", "Cantonsen@meta.com", "togorman@meta.com"],
        "individual": True,
        "subject": "New Grad SWE (May 2027) — distributed systems + ML infra, Google intern",
        "body": """Hi {first_name},

I'm Harry, a CS student at Georgia State graduating May 2027. I wanted to reach out about new grad software engineering roles at Meta.

This summer I interned at Google on Chrome — shipped C++ IPC (Protocol Buffers) to the stable channel serving 3B+ users at sub-50ms p99, and fixed a settings-nav bottleneck via lock-free concurrent trie (96% latency reduction, zero regressions, 95% test coverage). Currently I'm the primary engineer at TiMoto AI, a 3-person team where I built and operate our distributed ML serving stack (vLLM, gRPC, AWS/Terraform), maintaining 99.9% uptime.

I'm particularly interested in Meta's infrastructure, distributed systems, or ML platform engineering teams — the kind of work where scale is a first-class constraint. I'd love to learn about 2027 new grad openings and whether there are roles that might be a good fit.

Happy to share my resume or connect over a quick call.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["letiagt@amazon.com", "jackdavp@amazon.com"],
        "individual": True,
        "subject": "New Grad SWE (May 2027) — AWS infra background, Google Chrome intern",
        "body": """Hi {first_name},

I'm Harry, a CS student at Georgia State graduating May 2027. I wanted to reach out about new grad software engineering opportunities at Amazon.

My background has a strong AWS/infrastructure thread: at TiMoto AI I'm the primary engineer on a 3-person team, running multi-AZ ECS Fargate, Terraform IaC, CloudWatch observability, and CI/CD pipelines in production (99.9% uptime, 44% infrastructure cost reduction). Before that, I interned at Google on Chrome — shipped a C++ IPC transport layer to 3B+ users at sub-50ms p99, reviewed at 95% test coverage.

I'm particularly interested in teams at Amazon working on distributed systems, cloud infrastructure, or developer tooling — areas where I have direct production experience. I'd love to learn about the 2027 new grad process and whether there are roles that might fit.

Thank you for your time.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["v-snunna@microsoft.com"],
        "individual": False,
        "subject": "New Grad SWE (May 2027) — systems + distributed infra, Google intern",
        "body": """Hi,

I'm Harry, a CS student at Georgia State graduating May 2027, reaching out about new grad SWE opportunities at Microsoft.

I interned at Google on Chrome this summer, shipping C++ IPC (Protocol Buffers) to Chrome stable (3B+ users, sub-50ms p99, 95% test coverage). I'm currently the primary engineer at TiMoto AI, running distributed production systems end-to-end — gRPC, vLLM inference, AWS/Terraform, 99.9% uptime on a 3-person team.

I'm drawn to Microsoft's infrastructure and distributed systems work — Azure, Windows, and developer tooling are areas where deep systems knowledge matters, which is the kind of engineering I've been building toward. I'd love to connect about 2027 new grad SWE openings.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662""",
    },
    {
        "to": ["nprichodko@salesforce.com"],
        "individual": False,
        "subject": "New Grad SWE (May 2027) — backend + cloud infra, Google intern",
        "body": """Hi,

I'm Harry, a CS student at Georgia State graduating May 2027. I interned at Google on Chrome this summer (C++ IPC to 3B+ users, sub-50ms p99) and currently run backend and cloud infrastructure at TiMoto AI — AWS/Terraform, gRPC, CI/CD, 99.9% uptime on a 3-person team.

I'm interested in new grad SWE roles at Salesforce for 2027, particularly on platform or backend infrastructure teams. Happy to share my resume.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662""",
    },
    # ── GROWTH / SCALE ────────────────────────────────────────────────────────
    {
        "to": ["bcorrell@tesla.com"],
        "individual": False,
        "subject": "New Grad SWE (May 2027) — C++/systems, Google Chrome intern",
        "body": """Hi,

I'm Harry, a CS student at Georgia State graduating May 2027. I wanted to reach out about new grad software engineering opportunities at Tesla.

This summer I interned at Google on Chrome, shipping a C++ IPC transport layer to the stable channel (3B+ users, sub-50ms p99). I also fixed a latency bottleneck in settings navigation using a lock-free concurrent trie — 96% latency reduction, zero production regressions. Currently I'm the primary engineer at TiMoto AI, owning distributed backend systems and AWS/Terraform infrastructure end-to-end.

Tesla's software engineering work — from vehicle software to energy systems to manufacturing automation — involves the kind of reliability and correctness constraints I've been building for. I'd love to learn about 2027 new grad SWE openings, especially on systems or platform teams.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["Alaina.Williams@spacex.com", "christina.knighton@spacex.com"],
        "individual": True,
        "subject": "New Grad SWE (May 2027) — C++/systems/infra, Google Chrome intern",
        "body": """Hi {first_name},

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad software engineering roles at SpaceX.

At Google this summer I shipped a C++ IPC transport layer (Protocol Buffers) to Chrome's stable channel — 3B+ users, sub-50ms p99, zero regressions at 95% test coverage — and fixed a p99 latency bottleneck via a lock-free concurrent trie (96% reduction). I hold myself to a high bar for correctness; I know what it means to ship software where a regression is unacceptable.

Outside of Google, I'm the primary engineer at TiMoto AI: distributed production systems, gRPC inter-service layer (resolved a production deadlock under concurrent load), vLLM inference engine, AWS/Terraform infrastructure (99.9% uptime). I own the full stack on a 3-person team.

SpaceX's software — flight systems, ground control, vehicle software — demands the same discipline: correctness first, performance second, no shortcuts. That's the culture I want to work in. I'd love to learn about 2027 new grad or summer 2026 SWE roles, especially on flight software, ground systems, or infra.

Thank you for your time.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["alexandratorre@stripe.com"],
        "individual": False,
        "subject": "New Grad SWE (May 2027) — distributed systems + reliability, Google intern",
        "body": """Hi Alexandra,

I'm Harry, a CS student at Georgia State graduating May 2027. I wanted to reach out about new grad software engineering opportunities at Stripe.

Stripe's engineering reputation is something I've followed closely — the API design discipline, the reliability standards, and the attention to developer experience are things I genuinely respect. My own background sits at a similar intersection: I interned at Google shipping C++ to Chrome stable (3B+ users, sub-50ms p99, 95% test coverage, zero regressions), and I currently run distributed production systems at TiMoto AI — gRPC layer, vLLM inference, AWS/Terraform, 99.9% uptime. I've also resolved a production deadlock by tracing shared resource acquisition conflicts, and rebuilt a PostgreSQL-backed API from N+1 bottleneck to sub-100ms for 10,000+ records.

I'm particularly interested in Stripe's infrastructure, backend platform, or developer experience teams — roles where correctness and reliability aren't just goals but constraints. I'd love to learn about 2027 new grad openings and whether my background is a fit.

Happy to share my resume or chat briefly.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["morgan.shalom@databricks.com", "katie.tenboer@databricks.com", "sabiha.khan@databricks.com"],
        "individual": True,
        "subject": "New Grad SWE (May 2027) — ML infra + distributed systems, Google intern",
        "body": """Hi {first_name},

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad SWE roles at Databricks.

My background maps closely to what Databricks works on: at TiMoto AI I built and operate our entire ML serving stack — vLLM with PagedAttention (zero OOM failures at production traffic, sub-50ms p99 inference), gRPC inter-service layer (resolved a production deadlock under concurrent calls), and AWS/Terraform infrastructure (99.9% uptime, multi-AZ, 44% cost reduction). I've also contributed to Pulumi, a 24K-star open source IaC project, specifically around distributed state synchronization and Raft/Paxos correctness.

Before TiMoto, I interned at Google on Chrome — shipped C++ IPC (Protocol Buffers) to 3B+ users at sub-50ms p99, 95% test coverage.

The problem of making large-scale data and ML infrastructure reliable and efficient is exactly what I want to work on as a new grad. I'd love to learn about 2027 openings on infrastructure, ML platform, or distributed systems teams.

Happy to share my resume whenever.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["jessica.woo@doordash.com", "enny.tran@doordash.com", "cianna.contestabile@doordash.com"],
        "individual": True,
        "subject": "New Grad SWE (May 2027) — backend + distributed systems, Google intern",
        "body": """Hi {first_name},

I'm Harry, a CS student at Georgia State graduating May 2027. I wanted to reach out about new grad SWE roles at DoorDash.

My background is primarily backend and distributed systems: I interned at Google on Chrome (shipped C++ IPC to 3B+ users, sub-50ms p99, 95% test coverage), and I'm currently the primary engineer at TiMoto AI — owning gRPC service layer, vLLM ML serving, and AWS/Terraform infrastructure on a 3-person team (99.9% uptime). I've also fixed a PostgreSQL N+1 bottleneck that was degrading response times to 3s+ — redesigned indexing to hit sub-100ms for 10,000+ records.

DoorDash's backend infrastructure — real-time logistics, high-throughput order systems, distributed coordination — is the kind of engineering problem I've been building toward. I'd love to learn about new grad SWE openings for 2027, especially on backend or platform teams.

Thank you for your time.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["simone.assaley@capitalone.com", "jazmin.ramirez@capitalone.com", "shaelyn.dowd@capitalone.com"],
        "individual": True,
        "subject": "New Grad SWE (May 2027) — cloud infra + backend, Google intern",
        "body": """Hi {first_name},

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad software engineering opportunities at Capital One.

My background: Google Chrome SWE intern (C++ IPC to 3B+ users, sub-50ms p99, 95% test coverage) and primary engineer at TiMoto AI, where I run distributed production systems end-to-end on AWS — ECS Fargate, Terraform IaC, CloudWatch observability, multi-AZ (99.9% uptime, 44% infrastructure cost reduction). I've also built and scaled a BaaS on AWS supporting 500+ concurrent users with a 90% deployment time reduction via GitHub Actions CI/CD.

I'm interested in new grad SWE roles at Capital One for 2027, particularly on cloud platform, backend infrastructure, or distributed systems teams. Happy to share my resume or connect briefly.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
    {
        "to": ["jaiwebb@linkedin.com"],
        "individual": False,
        "subject": "New Grad SWE (May 2027) — distributed systems + backend infra, Google intern",
        "body": """Hi Jaime,

I'm Harry, a CS student at Georgia State graduating May 2027. I'm reaching out about new grad software engineering opportunities at LinkedIn.

I interned at Google on Chrome this summer — shipped a C++ IPC transport layer (Protocol Buffers) to Chrome stable (3B+ active users, sub-50ms p99, 95% test coverage) and fixed a latency bottleneck via lock-free concurrent trie (96% reduction, zero regressions). Currently I'm the primary engineer at TiMoto AI: gRPC inter-service layer, vLLM inference stack, and AWS/Terraform infrastructure (99.9% uptime on a 3-person team).

LinkedIn's infrastructure work — at the scale of hundreds of millions of users and one of the most complex professional data graphs in the world — is exactly the kind of environment I want to grow in as a new grad. I'd love to learn about 2027 openings, especially on backend or distributed systems teams.

Thank you for your time.

Harry Nguyen
nguyenharry2662@gmail.com · +1 470-667-9000
github.com/HarryNguyen2662 · linkedin.com/in/harrynguyen26""",
    },
]

# ─── HELPERS ───────────────────────────────────────────────────────────────────

def first_name_from_email(email: str) -> str:
    """Extract first name from email address, capitalized."""
    local = email.split("@")[0]
    # Handle formats: robert_graham, Sharon.Lin, letiagt, v-snunna
    for sep in [".", "_", "-"]:
        if sep in local:
            part = local.split(sep)[0]
            return part.capitalize()
    return local.capitalize()


def send_email(smtp, sender: str, to: str, subject: str, body: str, dry_run: bool):
    msg = MIMEMultipart("alternative")
    msg["From"] = sender
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    if dry_run:
        print(f"  [DRY RUN] Would send to: {to}")
        print(f"            Subject: {subject}")
        print(f"            First line: {body.splitlines()[0]}")
        return True

    smtp.sendmail(sender, to, msg.as_string())
    return True


def log_sent(to: str, subject: str, log_file: str):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now().isoformat()}\t{to}\t{subject}\n")


# ─── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Send cold outreach emails")
    parser.add_argument("--dry-run", action="store_true", help="Print emails without sending")
    parser.add_argument("--delay", type=float, default=3.0, help="Seconds between emails (default: 3)")
    parser.add_argument("--only", type=str, help="Only send to emails containing this substring")
    args = parser.parse_args()

    sender = os.environ.get("SENDER_EMAIL", "nguyenharry2662@gmail.com")
    password = os.environ.get("SENDER_APP_PASSWORD", "")

    if not args.dry_run and not password:
        print("ERROR: Set SENDER_APP_PASSWORD environment variable.")
        print("  Get one at: myaccount.google.com/apppasswords")
        sys.exit(1)

    log_file = os.path.join(os.path.dirname(__file__), "sent_log.tsv")

    # Build flat list of (to, subject, body)
    queue = []
    for entry in EMAILS:
        if entry["individual"]:
            for addr in entry["to"]:
                fname = first_name_from_email(addr)
                body = entry["body"].format(first_name=fname)
                queue.append((addr, entry["subject"], body))
        else:
            # Send one email to first address (others are CC alternatives — send individually anyway)
            for addr in entry["to"]:
                body = entry["body"].replace("{first_name}", first_name_from_email(addr))
                queue.append((addr, entry["subject"], body))

    # Filter if --only flag
    if args.only:
        queue = [(to, subj, body) for to, subj, body in queue if args.only.lower() in to.lower()]

    print(f"\n{'DRY RUN — ' if args.dry_run else ''}Sending {len(queue)} emails from {sender}")
    print("=" * 60)

    if args.dry_run:
        for to, subject, body in queue:
            send_email(None, sender, to, subject, body, dry_run=True)
            print()
        print(f"\nTotal: {len(queue)} emails would be sent.")
        return

    # Real send via Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        sent = 0
        failed = 0

        for i, (to, subject, body) in enumerate(queue, 1):
            try:
                print(f"[{i}/{len(queue)}] Sending to {to}...")
                send_email(smtp, sender, to, subject, body, dry_run=False)
                log_sent(to, subject, log_file)
                sent += 1
                print(f"  ✓ Sent")
                if i < len(queue):
                    time.sleep(args.delay)
            except Exception as e:
                print(f"  ✗ Failed: {e}")
                failed += 1

    print(f"\n{'=' * 60}")
    print(f"Done. Sent: {sent} | Failed: {failed}")
    print(f"Log: {log_file}")


if __name__ == "__main__":
    main()
