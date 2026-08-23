# Santo

Systems and AI engineering. Dallas, TX.

Two threads run through most of what I build. **Bengali NLP**, because the tooling everyone else takes for granted still handles the script badly. And **tools I actually run**, because the ones I use every day are the ones that get finished.

A repo is easy to describe and hard to verify, so the list below is ordered by how little you have to take my word for.

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Rust](https://img.shields.io/badge/-Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![C++](https://img.shields.io/badge/-C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Postgres](https://img.shields.io/badge/-Postgres-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Linux](https://img.shields.io/badge/-Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

## Rerun it yourself

*The claim, the data behind it, and the script that produced it are all in the repo.*

- **[bengali-tokenizer-eval](https://github.com/oneKn8/bengali-tokenizer-eval)** - tokenizer choice changes what Bengali costs you by 5 to 9x. Thirteen SentencePiece tokenizers measured against nine public ones, with the worst failures traced to one character: leave U+09BC out of normalization and byte-fallback climbs from 2% to 20%. Ships the tokenizers, the 3,000-document benchmark, a per-document SHA-256 manifest, a datasheet, frozen results, and the paper
- **[bangla-llm](https://github.com/oneKn8/bangla-llm)** - the pipeline behind Kotha-1: corpus collection, MinHash-LSH near-dedup, language ID, a 32k BPE tokenizer, and a bf16 pre-training loop for a 306M LLaMA-style Bengali model

## Install it and see

*Published, deployed, or running on my machine right now.*

- **[undertone](https://github.com/oneKn8/undertone)** - hold a key, speak, release, and the words land in whatever window has focus. Groq Whisper with a local faster-whisper fallback, cleanup guarded against rewriting your slang into corporate English, and clipboard-plus-evdev injection for apps that refuse synthetic keystrokes. `pipx install undertone`, runs as a systemd service, and is how I dictate most of my own text
- **[glyphlab](https://glyphlab-rose.vercel.app)** - any image into character art without uploading it. ASCII, Braille, halftone, sextants, contour tracing, exported as selectable text, ANSI, GIF, or a playable terminal movie. Also emits buildable LEGO and cross-stitch charts using real BrickLink part numbers and DMC floss codes
- **[machine-memory](https://github.com/oneKn8/machine-memory)** - local-first file and repo search daemon, exposed to agents over MCP
- **[lifeagent](https://github.com/oneKn8/lifeagent)** - accountability bot that checks what you claim against GitHub, Strava, and Wakatime before it believes you

## Read the mechanism

*The interesting part is a specific mechanism, and it is in the source rather than in a dependency.*

- **[granum](https://github.com/oneKn8/granum)** - insurance appeals optimized the way an immune system optimizes antibodies. Populations of appeal strategies mutate, compete on an LLM judge, then promote or apoptose: negative selection, tournament, elitist retention, feedback-directed mutation, with lineage tracked through Arize Phoenix over MCP
- **[vitals](https://github.com/oneKn8/vitals)** - see your own pulse on a webcam. Eulerian video magnification and FFT-based rPPG, with the bandpass and peak-picking math in the source rather than a DSP crate
- **[agentgov](https://github.com/oneKn8/agentgov)** - policy engine gating agent trust and release. Signed, idempotent decisions, with homoglyph-aware prompt-injection scanning on agent cards
- **[Research-Agent](https://github.com/oneKn8/Research-Agent)** - plan, search, analyze, refine, synthesize, write, review as a LangGraph state machine, with LaTeX and BibTeX output hardened against shell-escape injection
- **[soniq](https://github.com/oneKn8/soniq)** - AI phone agent for small businesses. LiveKit voice pipeline with tenant isolation enforced by Postgres row-level security rather than a WHERE clause
- **[drift](https://github.com/oneKn8/drift)** - audio post-production for generated music, with its own beat-synced chroma loop detection and Camelot-wheel arrangement
- **[slopguard](https://github.com/oneKn8/slopguard)** - Reddit moderation triage that asks what a mod should do about a suspicious post rather than only whether it is AI, with an explicit guard against penalizing non-native English
- **[profgraph](https://github.com/oneKn8/profgraph)** - professor intelligence for any LLM: ratings, a teaching-style classifier, and real UT Dallas grade distributions

---

## Currently green

<p align="center">
  <a href="https://pypi.org/project/undertone/"><img alt="undertone on PyPI" src="https://img.shields.io/pypi/v/undertone?style=flat-square&amp;color=e8a34c&amp;label=undertone%20on%20pypi"></a>
  <a href="https://github.com/oneKn8/undertone/actions"><img alt="undertone CI" src="https://img.shields.io/github/actions/workflow/status/oneKn8/undertone/ci.yml?style=flat-square&amp;label=undertone%20CI"></a>
  <a href="https://github.com/oneKn8/granum/actions"><img alt="granum CI" src="https://img.shields.io/github/actions/workflow/status/oneKn8/granum/ci.yml?style=flat-square&amp;label=granum%20CI"></a>
  <a href="https://github.com/oneKn8/agentgov/actions"><img alt="agentgov CI" src="https://img.shields.io/github/actions/workflow/status/oneKn8/agentgov/ci.yml?style=flat-square&amp;label=agentgov%20CI"></a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/oneKn8/oneKn8/main/assets/streak-dark.svg?v=20260823">
    <img alt="Contribution streak and activity" src="https://raw.githubusercontent.com/oneKn8/oneKn8/main/assets/streak-light.svg?v=20260823">
  </picture>
</p>

---

[![X](https://img.shields.io/badge/-@shifat__santo-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/shifat_santo)
[![LinkedIn](https://img.shields.io/badge/-Shifat_Islam_Santo-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shifatislam-santo/)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:shifatislamsanto764@gmail.com)
[![Discord](https://img.shields.io/badge/-onekn8-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.com/users/onekn8)
[![GitHub](https://img.shields.io/badge/-Follow-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/oneKn8)
