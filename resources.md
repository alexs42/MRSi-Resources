# Agents, models and where to learn this properly

Companion list for **"Removing the Thorn From the Rose: How Best to Use LLMs"** — MRSi 2026,
Drake Hotel, Chicago, 28 July 2026.

Every link here was rechecked on 2026-07-28. Model versions move fast; the vendor and the family are
the durable part of each row, so those are what to remember. The flagship column is a snapshot, not
a recommendation.

---

## 1. Coding agents you run in a terminal or editor

These are the tools that do the work in the demo. An agent differs from a chat window in one
respect that matters: it can run commands, read and write files, and loop on the result. That is
also why the security reading in section 6 is not optional.

### Commercial

| Tool | Where |
|---|---|
| Claude Code | https://code.claude.com/docs/en/setup |
| Codex CLI (OpenAI) | https://developers.openai.com/codex/cli/ |
| Antigravity CLI (Google) | https://antigravity.google/product/antigravity-cli |
| Cursor | https://cursor.com/ |
| GitHub Copilot | https://github.com/features/copilot |
| VS Code | https://code.visualstudio.com/ |

### Open source

| Tool | Where |
|---|---|
| OpenCode | https://opencode.ai/ |
| Kilo Code | https://kilo.ai/ |
| Pi | https://pi.dev/ |

### Broader than code

| Tool | Where |
|---|---|
| Hermes Agent (Nous Research) | https://github.com/NousResearch/hermes-agent |
| OpenClaw | https://github.com/openclaw/openclaw |
| NVIDIA NemoClaw | https://github.com/NVIDIA/NemoClaw |

---

## 2. Models behind them

### Closed weights, API only

| Vendor | Family | Flagship as of 2026-07-26 |
|---|---|---|
| OpenAI · https://openai.com | GPT-5.6 | Sol, Terra, Luna |
| Anthropic · https://www.anthropic.com | Claude 5 | Opus 5, Fable 5 |
| Google · https://deepmind.google/models/gemini/ | Gemini 3 | 3.1 Pro, 3.6 Flash |

### Open weights or open source

You can download these, inspect them, and run them on your own hardware. That matters for anything
touching patient data, and it is the reason the "can I even use this at work" conversation has an
answer other than no.

| Origin | Vendor | Model | Weights on Hugging Face |
|---|---|---|---|
| US | Thinking Machines Lab · https://thinkingmachines.ai | Inkling | `thinkingmachines/Inkling` |
| US | NVIDIA | Nemotron 3 Ultra | `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16` |
| US | OpenAI | GPT-OSS 120B | `openai/gpt-oss-120b` |
| US | Meta · https://developer.meta.com/ai/models/llama-4/ | Llama 4 | `meta-llama/Llama-4-Maverick-17B-128E-Instruct` |
| France | Mistral · https://mistral.ai | Mistral Large 3 | `mistralai/Mistral-Large-3-675B-Instruct-2512` |
| China | Moonshot AI · https://moonshot.ai | **Kimi K3** | publication pending · `moonshotai/Kimi-K2.7-Code` available now |
| China | DeepSeek · https://www.deepseek.com | DeepSeek V4 Flash | `deepseek-ai/DeepSeek-V4-Flash` |
| China | Z.ai · https://z.ai | **GLM-5.3** | publication pending · `zai-org/GLM-5.2` available now |
| China | Alibaba | Qwen 3.5 | `Qwen/Qwen3.5-35B-A3B` |

The right-hand column is what you can actually download as of 2026-07-26, checked against the Hugging
Face registry rather than quoted from memory. Kimi K3 and GLM-5.3 are announced with weights not yet
published, so the last released version of each is given alongside. Qwen 3.5 is Alibaba's last open
release.

---

## 3. Getting and running open models

**Download** — https://huggingface.co — roughly 2.9 million models, plus datasets and demos.

**Run locally**

| Tool | Where | Suits |
|---|---|---|
| LM Studio | https://lmstudio.ai | Desktop app, no terminal, easiest first try |
| AnythingLLM | https://anythingllm.com | Desktop app with document chat built in |
| Ollama | https://ollama.com | One command per model, good default for a laptop |
| vLLM | https://docs.vllm.ai | Serving to several users at once, GPU |
| llama.cpp | https://github.com/ggml-org/llama.cpp | The engine underneath much of the above |

---

## 4. Learning how these actually work

**Grant Sanderson (3Blue1Brown)** — https://www.3blue1brown.com — the best visual explanations of
this material anywhere, and the reason a lot of people finally understood attention.

- How transformers work — https://youtu.be/wjZofJX0v4M
- Neural networks, videos 1–10 — https://youtu.be/aircAruvnKk?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi

---

## 5. Context engineering

Getting the right material in front of the model, in the right order, at the right moment. This is
most of the difference between a useful answer and a plausible one.

- Simon Willison, context engineering — https://simonwillison.net/tags/context-engineering/
- Phil Schmid (Google DeepMind), context engineering — https://www.philschmid.de/context-engineering

---

## 6. Read this before you point an agent at anything that matters

**Simon Willison, "The Lethal Trifecta"** — https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/

Access to private data, exposure to untrusted content, and the ability to communicate outward. Any
two are usually fine. All three together, and a document you did not write can instruct your agent
to send your data somewhere you did not choose. Everything in this repository was built by an agent
holding all three, which is exactly why it was run in a scratch directory with no patient data
anywhere near it.

Willison's site generally is worth following: https://simonwillison.net

---

## 7. Prompting guides from the people who built the models

| Vendor | Guide |
|---|---|
| Anthropic | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices |
| Anthropic cookbooks | https://github.com/anthropics/claude-cookbooks |
| OpenAI | https://developers.openai.com/cookbook/examples/chatgpt/chatgpt_prompt_guide/chatgpt_prompt_guide |
| Google | https://github.com/google-gemini/cookbook |

Two consoles that need an account before they will load anything:

- OpenAI prompt optimiser — https://platform.openai.com/chat/edit
- Anthropic dashboard — https://platform.claude.com/dashboard

---

## 8. A system prompt worth stealing

The standing instruction I give a model before anything else. It is in
[`system-prompt.md`](system-prompt.md), and the parts that earn their place are the ones that give
the model permission to say no: *tell me if the request is illogical, wrong, or there is no data
after tool calls*, and *if there is no answer or the resource is not available, say so, do not
invent plausible answers.*

A model with no licence to fail will produce something rather than nothing, and something rather
than nothing is how a fabricated citation ends up in your manuscript.
