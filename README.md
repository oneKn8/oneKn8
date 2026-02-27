# Hi, I'm Santo

**Dallas, TX** | **CS @ UT Dallas** | **Systems, AI/ML, and infrastructure**

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![C++](https://img.shields.io/badge/-C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Rust](https://img.shields.io/badge/-Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Java](https://img.shields.io/badge/-Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![Linux](https://img.shields.io/badge/-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Codex](https://img.shields.io/badge/-Codex-121212?style=flat-square&logo=openai&logoColor=white)
![Claude Code](https://img.shields.io/badge/-Claude_Code-000000?style=flat-square&logo=anthropic&logoColor=white)

> I build production systems from scratch -- vector databases, task queues, research agents, observability platforms. Most of my work sits at the intersection of systems programming and applied ML.

## Projects

- **[VectorVault](https://github.com/oneKn8/VectorVault)** - HNSW approximate nearest neighbor engine from scratch in C++20. AVX2 SIMD-accelerated distance computation, memory-mapped persistence, sub-millisecond queries at 100k vectors.
  ![C++](https://img.shields.io/badge/-C++20-00599C?style=flat-square&logo=cplusplus&logoColor=white) ![CMake](https://img.shields.io/badge/-CMake-064F8C?style=flat-square&logo=cmake&logoColor=white) ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

- **[OpenLock](https://github.com/oneKn8/openlock_browser)** - Open-source lockdown exam browser for Linux. Implements the SEB protocol (BEK + Config Key + RNCryptor v3), kiosk shell, process guard with cgroups, VM/debugger detection.
  ![C++](https://img.shields.io/badge/-C++17-00599C?style=flat-square&logo=cplusplus&logoColor=white) ![Qt](https://img.shields.io/badge/-Qt6-41CD52?style=flat-square&logo=qt&logoColor=white) ![Chromium](https://img.shields.io/badge/-Chromium-4285F4?style=flat-square&logo=googlechrome&logoColor=white)

- **[QUASAR](https://github.com/oneKn8/QUASAR)** - Quantum circuit discovery agent. Physics-augmented LLM proposes candidates, surrogate model filters 10k+ in milliseconds, top 10% go through full VQE optimization.
  ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white) ![Qiskit](https://img.shields.io/badge/-Qiskit-6929C4?style=flat-square&logo=ibm&logoColor=white)

- **[Socratic](https://github.com/oneKn8/socratic)** - Private, multi-model alternative to NotebookLM. 16+ providers, podcast generation, vector search, multi-modal content ingestion. Runs entirely local.
  ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![Next.js](https://img.shields.io/badge/-Next.js-000?style=flat-square&logo=nextdotjs&logoColor=white) ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![LangChain](https://img.shields.io/badge/-LangChain-1C3C3C?style=flat-square)

- **[Syzygy](https://github.com/oneKn8/Syzygy)** - Document engineering IDE. Rust + Tauri 2.0 + Typst backend, visual pipelines, AI-assisted document creation.
  ![Rust](https://img.shields.io/badge/-Rust-000?style=flat-square&logo=rust&logoColor=white) ![Tauri](https://img.shields.io/badge/-Tauri-FFC131?style=flat-square&logo=tauri&logoColor=black) ![Typst](https://img.shields.io/badge/-Typst-239DAD?style=flat-square)

- **[SearchLight](https://github.com/oneKn8/searchLight)** - Hybrid search API combining BM25 keyword matching and HNSW vector similarity via Lucene 9. Hexagonal architecture, Spring Boot 3.3, Prometheus + OpenTelemetry.
  ![Java](https://img.shields.io/badge/-Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![Spring](https://img.shields.io/badge/-Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white) ![Lucene](https://img.shields.io/badge/-Lucene-EE5A24?style=flat-square) ![Prometheus](https://img.shields.io/badge/-Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)

- **[RivetQ](https://github.com/oneKn8/RivetQ)** - Durable task queue with write-ahead log, Raft consensus for HA, priority queues, dead-letter queues, rate limiting. REST + gRPC, Prometheus metrics, Next.js admin UI.
  ![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![gRPC](https://img.shields.io/badge/-gRPC-244c5a?style=flat-square) ![Prometheus](https://img.shields.io/badge/-Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white) ![Next.js](https://img.shields.io/badge/-Next.js-000?style=flat-square&logo=nextdotjs&logoColor=white)

- **[Research Agent](https://github.com/oneKn8/Research-Agent)** - Autonomous research pipeline using LangGraph with locally-hosted DeepSeek-R1-14B via vLLM. Adaptive planning, web + ArXiv search, gap analysis, LaTeX output with citations.
  ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![vLLM](https://img.shields.io/badge/-vLLM-7C3AED?style=flat-square) ![LangGraph](https://img.shields.io/badge/-LangGraph-1C3C3C?style=flat-square)

- **[Pulse](https://github.com/oneKn8/Pulse)** - HPC cluster observability platform. GPU/node telemetry, SLURM-style scheduling, Prometheus + Alertmanager + Grafana, VictoriaMetrics, LLM-based ops assistant via Ollama + RAG.
  ![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![Prometheus](https://img.shields.io/badge/-Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/-Grafana-F46800?style=flat-square&logo=grafana&logoColor=white) ![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black)

- **[SysVitals](https://github.com/oneKn8/SysVitals)** - Real-time system health monitoring dashboard. CPU, memory, network, storage, services, security -- all over WebSocket, zero polling. Runs 100% locally.
  ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black) ![WebSocket](https://img.shields.io/badge/-WebSocket-010101?style=flat-square)

- **[undertone](https://github.com/oneKn8/undertone)** - Voice typing daemon for Linux. Hold a key, speak, release -- text appears at your cursor in <1s. Groq Whisper with local faster-whisper fallback.
  ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Whisper](https://img.shields.io/badge/-Whisper-74aa9c?style=flat-square) ![Linux](https://img.shields.io/badge/-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

- **[mcp-memory](https://github.com/oneKn8/mcp-memory)** - MCP server for persistent agent memory with semantic search. ChromaDB embeddings, per-project scoping, importance scoring. Fully local.
  ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![ChromaDB](https://img.shields.io/badge/-ChromaDB-FF6F61?style=flat-square) ![MCP](https://img.shields.io/badge/-MCP-000?style=flat-square)

- **[Pulp](https://github.com/oneKn8/Pulp)** - Document intelligence CLI. Drop a PDF, ask questions, get answers. Multi-provider LLM backend (OpenAI, Anthropic, Ollama). Terminal-native TUI.
  ![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![CLI](https://img.shields.io/badge/-CLI-4D4D4D?style=flat-square&logo=gnubash&logoColor=white)

- **[Ghost Browser](https://github.com/oneKn8/Ghost-Browser)** - Privacy-focused desktop browser. Electron + Rust core via napi-rs, React/Vite frontend, SQLite storage.
  ![Electron](https://img.shields.io/badge/-Electron-47848F?style=flat-square&logo=electron&logoColor=white) ![Rust](https://img.shields.io/badge/-Rust-000?style=flat-square&logo=rust&logoColor=white) ![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black)

- **[scaffold](https://github.com/oneKn8/scaffold)** - Project bootstrapper CLI for Go, Rust, Python, and TypeScript.
  ![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![CLI](https://img.shields.io/badge/-CLI-4D4D4D?style=flat-square&logo=gnubash&logoColor=white)

- **[gitpulse](https://github.com/oneKn8/gitpulse)** - GitHub stats CLI dashboard -- track contributions, streaks, and achievement progress from the terminal.
  ![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![CLI](https://img.shields.io/badge/-CLI-4D4D4D?style=flat-square&logo=gnubash&logoColor=white)

- **[llm-cost](https://github.com/oneKn8/llm-cost)** - Multi-provider LLM API cost tracker across OpenAI, Anthropic, Groq, Google, DeepSeek.
  ![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![CLI](https://img.shields.io/badge/-CLI-4D4D4D?style=flat-square&logo=gnubash&logoColor=white)

## GitHub Activity

<p align="center">
  <img src="https://github-readme-stats-eight-theta.vercel.app/api?username=oneKn8&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true" alt="GitHub Stats" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=oneKn8&theme=tokyonight&hide_border=true" alt="GitHub Streak" />
</p>

<p align="center">
  <img src="https://ghchart.rshah.org/oneKn8" alt="Contribution Graph" />
</p>

---

[![X](https://img.shields.io/badge/-@shifat__santo-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/shifat_santo)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shifatislam-santo/)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:shifatislamsanto764@gmail.com)
[![Instagram](https://img.shields.io/badge/-Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/shifatis.santo/)
[![Discord](https://img.shields.io/badge/-onekn8-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.com/users/onekn8)
[![GitHub](https://img.shields.io/badge/-Follow-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/oneKn8)
