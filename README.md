# Hi, I'm Santo

CS @ UT Dallas | Systems, AI/ML, and infrastructure

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat&logo=cplusplus&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat&logo=go&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat&logo=rust&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

> I build production systems from scratch -- vector databases, task queues, research agents, observability platforms. Most of my work sits at the intersection of systems programming and applied ML.

---

## Current Projects

- **[VectorVault](https://github.com/oneKn8/VectorVault)** - HNSW approximate nearest neighbor engine built from scratch in C++20. AVX2 SIMD-accelerated distance computation, memory-mapped persistence with CRC32 validation, thread-safe concurrent reads. Sub-millisecond queries at 100k vectors. REST API + Docker.
  ![C++](https://img.shields.io/badge/-C++20-00599C?style=flat-square&logo=cplusplus&logoColor=white) ![CMake](https://img.shields.io/badge/-CMake-064F8C?style=flat-square&logo=cmake&logoColor=white) ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

- **[RivetQ](https://github.com/oneKn8/RivetQ)** - Durable task queue in Go with write-ahead log (segmented WAL + Pebble KV), Raft consensus for HA, priority queues, visibility timeouts, dead-letter queues, rate limiting. REST + gRPC APIs, Prometheus metrics, Next.js admin UI.
  ![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![gRPC](https://img.shields.io/badge/-gRPC-244c5a?style=flat-square) ![Prometheus](https://img.shields.io/badge/-Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white) ![Next.js](https://img.shields.io/badge/-Next.js-000?style=flat-square&logo=nextdotjs&logoColor=white)

- **[Deep Research Agent](https://github.com/oneKn8/research-agent)** - Autonomous research pipeline using LangGraph with a locally-hosted DeepSeek-R1-14B brain (via vLLM). Plans adaptively, searches web + ArXiv, self-corrects through gap analysis, outputs LaTeX papers with citations. FastAPI backend with SSE streaming, Next.js monitoring UI.
  ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![vLLM](https://img.shields.io/badge/-vLLM-7C3AED?style=flat-square) ![LangGraph](https://img.shields.io/badge/-LangGraph-1C3C3C?style=flat-square)

- **[Pulse](https://github.com/oneKn8/pulse)** - HPC cluster observability platform. Simulated GPU/node telemetry with SLURM-style job scheduling, Prometheus + Alertmanager + Grafana dashboards, VictoriaMetrics for long-term storage, and an LLM-based ops assistant (Ollama + RAG) for incident investigation. Go API, React dashboard.
  ![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![Prometheus](https://img.shields.io/badge/-Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/-Grafana-F46800?style=flat-square&logo=grafana&logoColor=white) ![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black)

- **[OpenLock](https://github.com/oneKn8/Lockdownbrowser.)** - Open-source lockdown exam browser for Linux. Implements the SEB protocol (BEK + Config Key + RNCryptor v3 .seb parsing), kiosk shell (X11/Wayland), process guard with cgroups isolation, input lockdown, VM/debugger detection.
  ![C++](https://img.shields.io/badge/-C++17-00599C?style=flat-square&logo=cplusplus&logoColor=white) ![Qt](https://img.shields.io/badge/-Qt6-41CD52?style=flat-square&logo=qt&logoColor=white) ![Chromium](https://img.shields.io/badge/-Chromium-4285F4?style=flat-square&logo=googlechrome&logoColor=white)

- **[Pulp](https://github.com/oneKn8/pulp)** - Document intelligence CLI. Drop a PDF, ask questions, get answers. Multi-provider LLM backend (OpenAI, Anthropic, Ollama). Terminal-native TUI.
  ![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white) ![CLI](https://img.shields.io/badge/-CLI-4D4D4D?style=flat-square&logo=gnubash&logoColor=white)

- **[Speaksy](https://github.com/oneKn8/jarvis)** - Voice typing daemon for Linux. Hold a key, speak, release -- text appears at your cursor in <1s. Groq Whisper API with local faster-whisper fallback, filler word removal, systemd service. Works everywhere: terminal, browser, IDE.
  ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Whisper](https://img.shields.io/badge/-Whisper-74aa9c?style=flat-square) ![Linux](https://img.shields.io/badge/-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

## Tools & Experiments

- **[LinkBreaker](https://github.com/oneKn8/LinkBreaker)** - Link shortener bypass engine. Puppeteer Stealth with timer acceleration (overrides setTimeout/setInterval/Date.now), DOM overlay removal via MutationObserver, network sniffing for final URLs, modular strategy engine.
  ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![Puppeteer](https://img.shields.io/badge/-Puppeteer-40B5A4?style=flat-square&logo=puppeteer&logoColor=white)

- **[jsonLens](https://github.com/oneKn8/jsonLens)** - Research workbench. Monaco editor, PDF parsing, force-directed graph visualization, KaTeX math rendering, Supabase backend.
  ![Next.js](https://img.shields.io/badge/-Next.js-000?style=flat-square&logo=nextdotjs&logoColor=white) ![Supabase](https://img.shields.io/badge/-Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=white)

- **[tracker](https://github.com/oneKn8/tracker)** - Productivity system. Turborepo monorepo, Drizzle ORM + better-sqlite3, Hono API, Zod validation. Typed end-to-end.
  ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white) ![Hono](https://img.shields.io/badge/-Hono-E36002?style=flat-square&logo=hono&logoColor=white)

- **[Ghost Browser](https://github.com/oneKn8/ghost-browser)** - Privacy-focused desktop browser. Electron + Rust core (napi-rs), React/Vite frontend, SQLite storage.
  ![Electron](https://img.shields.io/badge/-Electron-47848F?style=flat-square&logo=electron&logoColor=white) ![Rust](https://img.shields.io/badge/-Rust-000?style=flat-square&logo=rust&logoColor=white) ![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black)

- **[Nocturne Works](https://github.com/oneKn8/noc)** - 3D portfolio with interactive WebGL chapters. Custom GLSL shaders, particle fields, flow simulations.
  ![Three.js](https://img.shields.io/badge/-Three.js-000?style=flat-square&logo=threedotjs&logoColor=white) ![WebGL](https://img.shields.io/badge/-WebGL-990000?style=flat-square&logo=webgl&logoColor=white) ![Framer](https://img.shields.io/badge/-Framer_Motion-0055FF?style=flat-square&logo=framer&logoColor=white)

- **modeltrain** - Fine-tuning Mistral Small 3.2 24B with Unsloth + QLoRA. Custom dataset generation pipeline.
  ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)

- **functune** - Interactive function visualizer. Plot and manipulate math functions in real-time.
  ![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black) ![Vite](https://img.shields.io/badge/-Vite-646CFF?style=flat-square&logo=vite&logoColor=white)

---

[![LinkedIn](https://img.shields.io/badge/linkedin-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shifatislam-santo/)
[![Email](https://img.shields.io/badge/email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:shifatislamsanto764@gmail.com)
[![Instagram](https://img.shields.io/badge/instagram-E4405F?style=flat&logo=instagram&logoColor=white)](https://www.instagram.com/shifatis.santo/)
