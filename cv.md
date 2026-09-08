%-------------------------
% Resume: Harry Nguyen, New Grad 2027 | Applied AI Systems (production reliability + inference performance)
%-------------------------

\documentclass[letterpaper,11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}

\pagestyle{fancy}
\fancyhf{}
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.95in}
\addtolength{\textheight}{1.75in}

\urlstyle{same}
\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

\titleformat{\section}{
  \vspace{-6pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-6pt}]

\pdfgentounicode=1

\newcommand{\resumeItem}[1]{
  \item\small{{#1 \vspace{-2pt}}}
}

\newcommand{\resumeSubheadingShortSplit}[3]{%
  \vspace{-2pt}\item
    \begin{tabular*}{0.98\textwidth}[t]{l@{\extracolsep{\fill}}r}
      {\normalsize\textbf{#1}} \textbar{} {\normalsize #2} & {\normalsize #3} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{0.98\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      {\small#3} & {\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{%
  \vspace{-2pt}\item
    \begin{tabular*}{0.98\textwidth}[t]{l@{\extracolsep{\fill}}r}
      {\normalsize #1} & {\normalsize #2} \\
    \end{tabular*}\vspace{-7pt}
}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-9pt}}
\newcommand{\resumeSkillHeading}[2]{%
  \item\small{\textbf{#1}: #2 \vspace{-9pt}}%
}

%-------------------------------------------
\begin{document}

%----------HEADING----------
\begin{center}
    \textbf{\Huge \scshape Harry Nguyen} \\ \vspace{1pt}
    \small +1 470-667-9000 $|$
    \href{mailto:nguyenharry2662@gmail.com}{\underline{nguyenharry2662@gmail.com}} $|$
    \href{https://www.linkedin.com/in/harrynguyen26/}{\underline{linkedin.com/in/harrynguyen26}} $|$
    \href{https://github.com/HarryNguyen2662}{\underline{github.com/HarryNguyen2662}}
\end{center}
\vspace{-18pt}

%-----------EDUCATION-----------
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheadingShortSplit
      {Georgia State University}{Bachelor of Science in Computer Science}{May 2027}
  \resumeSubHeadingListEnd

%-----------EXPERIENCE-----------
\section{Experience}
  \resumeSubHeadingListStart

    \resumeSubheadingShortSplit
      {TiMoto AI}{Software Engineer}{Sep 2025 -- Present}
        \resumeItemListStart
          \resumeItem{Shipped an AI agent that fixes production bugs from PR diffs and logs behind tests and auto-rollback, cutting a small team's debug time from about 45 to \textbf{under 8 min} over 150+ issues in 2 months, 95\% fully automated}
          \resumeItem{Built TiMoto's motorbike-valuation backend from zero on AWS Fargate; since AI valuations can take minutes, split it into a Django REST API, a private gRPC evaluator, and a WebSocket service that notifies the app when done}
          \resumeItem{Redesigned an over-provisioned \$5K/month EKS setup onto multi-AZ ECS Fargate (Terraform) with Grafana monitoring, reducing cost 44\% to under \$3K/month at 99.9\% uptime over 4 months and root cause to under 15 min}
          \resumeItem{Diagnosed out-of-memory failures on 6--8\% of peak-hour LLM requests as 65\% KV cache fragmentation; moving serving to vLLM cut it under 4\%, with none in 4 months, and raised throughput 3.2x (14 to 45 req/sec)}
          \resumeItem{Traced ML evaluation accuracy stuck at 57\% to a production gRPC deadlock that truncated responses into wrong results, then replaced inconsistent lock ordering with one enforced order, raising accuracy to 87\%}
          \resumeItem{Partnered with ops, sales, marketing, product, and the founder to fix the company-wide AI agent, which gave staff wrong answers, reorganizing its knowledge base by team with RAG and a knowledge graph and speeding replies from 30--40s to 5--10s}
      \resumeItemListEnd

    \resumeSubheadingShortSplit
      {Google}{Software Engineer Intern (Chrome Browser)}{May 2025 -- Aug 2025}
      \resumeItemListStart
        \resumeItem{Built a Mojo IPC interface and C++ config reader to rebuild Chrome's Privacy Sandbox internals page, cutting debugging from 2--3 hours of logs and DB dumps to \textbf{under 5 min} for 200+ engineers; shipped to stable in 78 PRs}
        \resumeItem{Wrote the design doc for a lock-free trie in the browser process after settings search took 1,200ms at p99 because it scanned linearly while IPC kept writing new keys, bringing it under 50ms}
        \resumeItem{Root-caused stale tabs and renderer crashes, via bug-tracker repros and call stacks, to sub-teams' panels mutating one shared state object; moved the page to an event-driven observer model, closing 45 related bugs}
        \resumeItem{Fixed about 30 page tests that timed out mid-run because checks fired before UI data loaded; wrote a testing design doc that made tests wait for data before checking the UI, taking the suite from \textbf{2 hours to 10 min}}
      \resumeItemListEnd

    \resumeSubheadingShortSplit
      {Develop for Good}{Software Engineer Intern}{May 2024 -- Aug 2024}
      \resumeItemListStart
        \resumeItem{Sped up the member list for CW3, a global Web3 community, which took 3+ seconds to load over 10,000+ records because of N+1 queries; batched the queries and added PostgreSQL indexes, bringing it \textbf{under 100ms}}
        \resumeItem{Moved CW3 off Airtable, which had become cluttered and hard to use, to Appwrite as primary backend engineer on a 12-person team, with profile-based member matching for meetups, serving 500+ concurrent users}
        \resumeItem{Automated manual weekly deploys with a GitHub Actions CI/CD pipeline, cutting them from 15 to 5 min}
      \resumeItemListEnd

  \resumeSubHeadingListEnd

%-----------PROJECTS-----------
\section{Projects}
  \resumeSubHeadingListStart
    \resumeProjectHeading
      {\textbf{Pulumi} \textbar{} Open Source Contributor}{\href{https://github.com/pulumi/pulumi}{github.com/pulumi}}
      \resumeItemListStart
        \resumeItem{Open-source infrastructure-as-code tool that lets DevOps, platform, and software engineers manage AWS, Azure, GCP, and Kubernetes in Go, Python, or TypeScript}
        \resumeItem{Submitted Go CLI features and fixes for multi-cloud (AWS/Azure/GCP) provisioning, in maintainer review}
        \resumeItem{Wrote Raft/Paxos consensus test cases for Pulumi's distributed state synchronization layer (submitted), checking correctness under concurrent operations and partial failures}
      \resumeItemListEnd
    \resumeProjectHeading
      {\textbf{NextStep} \textbar{} Founder}{\href{https://nexteasystep.com/}{nexteasystep.com}}
      \resumeItemListStart
        \resumeItem{NextStep's AI copilot tracks deadlines and obligations in household documents for 100 users; its first model and harness misread 37\% of extracted fields, so switched both and added deterministic schema validation and multi-pass repair, dropping errors to \textbf{9\%} with 7\% routed to manual review}
        \resumeItem{Provider rate limits and timeouts left the LLM router completing only 92--94\% of requests, with 12--15\% of structured outputs malformed; automatic failover across Gemini, OpenAI, OpenRouter, and NVIDIA NIM plus a retry-and-repair layer raised completion to 99.7\% and cut malformed outputs under 0.3\%}
        \resumeItem{The model needs each document whole, so uploads up to 500 MiB had to survive network drops and client restarts; built a resumable pipeline with 8 MiB chunks on private Supabase Storage (RLS) and Terraform-managed Cloud Run and KMS, within the project's 302-test suite}
      \resumeItemListEnd
  \resumeSubHeadingListEnd

%-----------TECHNICAL SKILLS-----------
\section{Skills}
  \resumeSubHeadingListStart
    \resumeSkillHeading{Languages}{C++, Python, Go, TypeScript, Java, JavaScript, SQL, Bash, Rust}
    \resumeSkillHeading{AI Dev Tools}{Claude Code, GitHub Copilot, Codex, Cursor}
    \resumeSkillHeading{Backend \& Infra}{vLLM, gRPC, AWS, Terraform, Kubernetes, Docker, CI/CD, Prometheus, Grafana}
    \resumeSkillHeading{Frameworks \& Databases}{Django, FastAPI, Node.js, React, REST APIs, PostgreSQL, pgvector, Redis, MongoDB}
    \resumeSkillHeading{Agentic Systems}{LLM Agents, Tool Calling, MCP, Hybrid Retrieval (RAG), Schema-Constrained Generation, Evals}
  \resumeSubHeadingListEnd

\end{document}
