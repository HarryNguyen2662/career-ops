%-------------------------
% Resume: Harry Nguyen — New Grad 2027 | Distributed Systems / Backend Infrastructure
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
\addtolength{\topmargin}{-.5in}
\addtolength{\textheight}{1.3in}

\urlstyle{same}
\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

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
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}
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

%-----------EDUCATION-----------
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {Georgia State University}{Expected May 2027}
      {Bachelor of Science in Computer Science \textbf{· GPA: 3.75/4.0}}{}
      \resumeItemListStart
        \resumeItem{Coursework: Distributed Systems, Operating Systems, Database Systems, Computer Networks, Data Structures}
        \resumeItem{Honors: Presidential Scholarship, Anita Andrew Fellowship, Roxie Alexander Memorial Award}
      \resumeItemListEnd
  \resumeSubHeadingListEnd

%-----------EXPERIENCE-----------
\section{Experience}
  \resumeSubHeadingListStart

    \resumeSubheadingShortSplit
      {TiMoto AI}{Software Engineer}{Sep 2025 -- Present}
        \resumeItemListStart
          \resumeItem{Cut incident root-cause time from unknown to \textbf{under 15 minutes} by building TiMoto's observability stack from zero — deployed \textbf{Prometheus} and \textbf{Grafana} metrics alongside CloudWatch
      dashboards across the gRPC and ML serving layers}
          \resumeItem{Restored \textbf{100\% evaluation success rate} at \textbf{sub-50ms p99} by resolving a production \textbf{gRPC} deadlock — replaced inconsistent lock-acquisition ordering under concurrent calls with a
      single enforced sequencing rule across the inter-service layer}
          \resumeItem{Eliminated \textbf{OOM failures} under concurrent production load by replacing naive batching with a \textbf{vLLM/PagedAttention} inference engine, solving KV cache memory fragmentation for LLM serving}
          \resumeItem{Prevented single-zone failures from taking production down, sustaining \textbf{99.9\% uptime} and cutting infrastructure cost \textbf{44\%} (\$40--60/month), by architecting a multi-AZ ECS Fargate
      deployment with \textbf{Terraform IaC}, CloudWatch observability, and an auto-rollback circuit breaker pattern}
          \resumeItem{Cut mean-time-to-identify on repeat incidents \textbf{68\%} across gRPC, PostgreSQL, and ML serving layers by building a from-scratch post-mortem practice — documented runbooks for the top failure modes
      and ran a shared on-call rotation}
      \resumeItemListEnd

    \resumeSubheadingShortSplit
      {Google}{Software Engineer Intern — Chrome Browser}{May 2025 -- Aug 2025}
      \resumeItemListStart
        \resumeItem{Shipped a \textbf{C++ IPC transport layer} to Chrome's stable channel — serving \textbf{3B+ active users} at \textbf{sub-50ms p99} and \textbf{10K+ req/sec} — by choosing Protocol Buffers over custom serialization for schema evolution and cross-language compatibility}
        \resumeItem{Turned a visibly sluggish settings search into an instant one for power users — \textbf{96\%} p99 latency cut (1,200ms down to sub-50ms), zero production regressions — by replacing a mutex-contended search path with a \textbf{lock-free concurrent trie}}
        \resumeItem{Ended cross-team cascading UI bugs and accelerated feature delivery \textbf{68\%} across \textbf{25K+ lines} of Chromium, at \textbf{95\% test coverage}, by architecting an event-driven TypeScript/React system that decoupled UI state propagation via the observer pattern}
        \resumeItem{Landed production-ready changes into Chrome's codebase — reviewed and adopted by senior engineers — by delivering design docs and code reviews at \textbf{95\% test coverage} alongside the Chrome infrastructure team}
      \resumeItemListEnd

    \resumeSubheadingShortSplit
      {Develop for Good}{Software Engineer Intern}{May 2024 -- Aug 2024}
      \resumeItemListStart
        \resumeItem{Scaled a backend to support \textbf{500+ concurrent users} and cut deployment time \textbf{90\%} by designing a stateless AWS BaaS with JWT auth and a GitHub Actions CI/CD auto-scaling policy}
        \resumeItem{Cut API response time from 3+ seconds to \textbf{sub-100ms} on \textbf{10,000+ record} datasets by diagnosing an N+1 query bottleneck and redesigning the data layer with PostgreSQL indexing}
      \resumeItemListEnd

  \resumeSubHeadingListEnd

%-----------PROJECTS-----------
\section{Projects}
  \resumeSubHeadingListStart
    \resumeProjectHeading
      {\textbf{Pulumi — Contributor} $|$ \emph{Go, TypeScript, Infrastructure-as-Code (IaC)}}{\href{https://github.com/pulumi/pulumi}{\underline{github.com/pulumi}}}
      \resumeItemListStart
        \resumeItem{Submitted Go CLI features and bug fixes enabling multi-cloud (AWS/Azure/GCP) provisioning — under active review by core maintainers}
        \resumeItem{Analyzed \textbf{Raft/Paxos consensus} in distributed state synchronization layer — studied linearizability guarantees and correctness under concurrent operations and partial failures}
      \resumeItemListEnd
  \resumeSubHeadingListEnd

%-----------TECHNICAL SKILLS-----------
\section{Skills}
  \resumeSubHeadingListStart
    \resumeSkillHeading{Distributed Systems}{gRPC, Protocol Buffers, Circuit breakers, Exactly-once semantics, Fault tolerance, Kafka, Multi-AZ, Event-driven architecture}
    \resumeSkillHeading{ML \& AI Infrastructure}{vLLM, PagedAttention, Continuous Batching, LoRA/QLoRA, PyTorch, LangChain, LLM-as-a-judge evaluation}
    \resumeSkillHeading{Languages}{C++, Python, Go, TypeScript, Java, JavaScript, SQL, Bash, Rust}
    \resumeSkillHeading{Cloud \& Infrastructure}{AWS (ECS Fargate, EKS, EC2, S3, RDS), Terraform, Kubernetes, Docker, CI/CD, CloudWatch, Prometheus, Grafana, GCP}
    \resumeSkillHeading{Frameworks \& Databases}{Django, FastAPI, Node.js, React, REST APIs, PostgreSQL, Redis, MongoDB}
    \resumeSkillHeading{AI Dev Tools}{Claude Code, GitHub Copilot, Codex, Cursor}
  \resumeSubHeadingListEnd

\end{document}
