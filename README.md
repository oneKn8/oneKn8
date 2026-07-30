# Santo

**Most of what I build, I build from the algorithm up.**

Bandpass filters and FFTs written by hand in Rust. Tokenizers trained, then measured against a benchmark I released so anyone can check the numbers. Retrieval indexes, agent runtimes, voice pipelines.

Two threads run through most of it. **Bengali NLP**, because tooling everyone else takes for granted still handles the script badly. And **tools I actually run**, because the ones I use every day are the ones that get finished.

![Rust](https://img.shields.io/badge/-Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![C++](https://img.shields.io/badge/-C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?style=flat-square&logo=go&logoColor=white)

---

### [bengali-tokenizer-eval](https://github.com/oneKn8/bengali-tokenizer-eval)

**Tokenizer choice changes what Bengali costs you by 5 to 9x. Here is the measurement, the data, and the cause.**

I trained 13 SentencePiece tokenizers, evaluated them alongside 9 public ones across a 3,000-document Bengali corpus, and traced the worst failures to a single character. Leaving U+09BC (Bengali Nukta) out of normalization pushes byte-fallback from roughly 2% to 20%, and accounts for 89.8% of every byte-level token produced.

All 13 tokenizers ship in the repo, along with the benchmark set, a per-document SHA-256 manifest, a datasheet, the frozen evaluation results, and the paper. The table is meant to be rerun, not taken on faith.

Python, SentencePiece, ACL-format paper

---

### [undertone](https://github.com/oneKn8/undertone)

**Push-to-talk voice typing for Linux. Hold a key, speak, release, and the words land in whatever window has focus.**

Groq Whisper with a local faster-whisper fallback, LLM cleanup guarded against quietly rewriting your slang into corporate English, and clipboard-plus-evdev injection for the apps that refuse synthetic keystrokes. Runs as a systemd user service.

`pipx install undertone`. Tested against Python 3.10, 3.11, and 3.12 in CI. I dictate with it daily, which is why the rough edges keep getting filed down.

Python, PyPI, systemd

---

### [granum](https://github.com/oneKn8/granum)

**Insurance denial appeals, optimized the way an immune system optimizes antibodies.**

Populations of appeal strategies mutate, compete on an LLM judge's score, then promote or apoptose. The loop is a real germinal center: negative selection, tournament, elitist retention, feedback-directed mutation. Strategy lineage is tracked through Arize Phoenix over MCP.

The web demo replays frozen artifacts from real runs instead of calling the model live, and the code says so out loud rather than passing it off as live inference. [Demo video](https://youtu.be/483aJsQ9c6Y).

Python, Gemini on Vertex, Phoenix MCP

---

### Also worth your time

| Project | What it is | Built with |
|---------|------------|-----------|
| **[glyphlab](https://github.com/oneKn8/glyphlab)** | Image to glyph art in the browser: ASCII, Braille, halftone, sextants, plus buildable LEGO and cross-stitch charts with real part codes. [Live](https://glyphlab-rose.vercel.app) | TypeScript, Canvas |
| **[vitals](https://github.com/oneKn8/vitals)** | See your own pulse on a webcam. Eulerian video magnification and FFT-based rPPG, signal processing written from scratch | Rust, rustfft |
| **[soniq](https://github.com/oneKn8/soniq)** | AI phone agent for small businesses. LiveKit voice pipeline, tenant isolation enforced by Postgres row-level security rather than a WHERE clause | TypeScript, Python |
| **[lifeagent](https://github.com/oneKn8/lifeagent)** | Accountability bot that checks what you claim against GitHub, Strava, and Wakatime before it believes you | TypeScript, Postgres |
| **[agentgov](https://github.com/oneKn8/agentgov)** | Policy engine gating agent trust and release. Signed, idempotent decisions, with homoglyph-aware prompt-injection scanning | TypeScript, MCP |
| **[drift](https://github.com/oneKn8/drift)** | Audio post-production for generated music. Beat-synced chroma loop detection and Camelot-wheel arrangement, both written by hand | Python, React |
| **[machine-memory](https://github.com/oneKn8/machine-memory)** | Local-first file and repo search daemon, exposed to agents over MCP | TypeScript, SQLite |
| **[profgraph](https://github.com/oneKn8/profgraph)** | Professor intelligence for any LLM: ratings, teaching style, and real UTD grade distributions | Python, MCP |

---

<p align="center">
  <img src="https://ghchart.rshah.org/oneKn8" alt="Contribution Graph" />
</p>

---

[![X](https://img.shields.io/badge/-@shifat__santo-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/shifat_santo)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shifatislam-santo/)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:shifatislamsanto764@gmail.com)
[![Discord](https://img.shields.io/badge/-onekn8-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.com/users/onekn8)
[![GitHub](https://img.shields.io/badge/-Follow-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/oneKn8)
