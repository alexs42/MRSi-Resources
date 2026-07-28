# MRSi 2026 — resources, and one agent run with its work shown

Companion repository for **"Removing the Thorn From the Rose: How Best to Use LLMs"**
Aleksandar Stanic-Kostic, MD, PhD · MRSi 2026 · Drake Hotel, Chicago · 28 July 2026

**→ [alexs42.github.io/MRSi-Resources](https://alexs42.github.io/MRSi-Resources/)** — reads better on
a phone.

---

> ## ⚠️ This is a demonstration of method, not a clinical document.
>
> Everything under [`run-output/`](run-output/) was produced by a single unedited agentic run on
> 2026-07-22 and is published exactly as the run wrote it. It has **not been reviewed for accuracy by
> a human expert**, and **nothing was corrected, re-worded or re-styled after the run finished**. The
> checks it describes — two models from two vendors retrieving each source independently, and an
> adjudication rule applied in code — are checks the run ran on itself. They are not peer review.
>
> **This is not medical advice**, not a guideline and not a systematic review. Do not use it for
> patient care.

---

## The four rules, if you remember nothing else

1. Match the tool to the risk, and the data to the tool.
2. Ground every factual claim in a source, and verify the citation and the number before you reuse it.
3. Keep PHI inside approved, BAA-covered or on-prem systems.
4. Preserve skill through unaided practice and audit.

### The red line — decide what never gets pasted

| Tier | What it means |
|---|---|
| 🔴 **Consumer** | Free or personal web apps carry no business-associate agreement, so de-identified questions and drafting only. **Never PHI.** |
| 🟠 **Enterprise no-train** | Paid endpoints that contractually do not train on inputs lower the leak risk, but without a signed BAA they are not cleared for identifiable data. |
| 🟢 **BAA-covered or on-prem** | The only tier identifiable data may enter, and only for the approved use. |

**The prompt box is a disclosure.** Under HIPAA, any vendor that handles ePHI needs a BAA even in
"no-view" encrypted setups, and the "don't train on my data" toggle stops training reuse — it does
not create a BAA. IVF data resists de-identification: PGT genetics and partner linkage are
inherently identifying, so the genome is the identifier.

<sub>Khanna S. Responsible use of large language models: privacy and governance. <i>Therap Adv Gastroenterol</i> 2026;19:17562848261441693.</sub>

## Start here

**[`resources.md`](resources.md)** — the agents, the models, where to download open weights and run
them on your own hardware, the two people worth reading, the prompting guides, and the one security
article to read before you point an agent at anything that matters.

**[`system-prompt.md`](system-prompt.md)** — the standing instruction I give a model before anything
else, and why each line is in it.

The rest of this repository is the demonstration.

## The demonstration

The talk shows a recorded run of an agent answering a real clinical question — fresh versus elective
frozen embryo transfer — under a method designed so that a clinician can check it rather than trust
it. A plan committed before any searching. A named primary source behind every number. Two frontier
models from two different vendors retrieving those sources separately and instructed to refute rather
than agree. An arithmetic rule, applied in code, deciding what survives.

The point is not that a language model can write about IVF. It is that one can be made to show its
work in a form you can audit.

### The result

| | |
|---|---|
| Claims extracted and adjudicated | 57 |
| Convergent (both verifiers returned the identical verdict) | 44 of 57 (77%) |
| `[verified x2]` | 42 |
| `[disputed]` (verifiers disagreed, disagreement quoted inline) | 12 |
| `[refuted x2]` (both verifiers rejected it, excluded) | 2 |
| `[unverified — source not retrieved]` (excluded) | 1 |
| Usable in the bottom line and the summary table | 54 of 57 |
| Wall clock | 2 h 13 min |

The two models did not agree on everything. They returned different verdicts on **13 of 57** claims.
Every disagreement is quoted in [`run-output/adjudication.md`](run-output/adjudication.md) rather than
resolved silently, because the disagreements are the part that carries information. Nothing was
staged: no disagreement was manufactured and no convergence was suppressed.

### What is in here

| Path | What it is |
|---|---|
| [`explainer.html`](explainer.html) | The deliverable. One self-contained scrolling page, no external requests, fonts and figures inlined. Opens in any browser including a phone. Carries a disclaimer banner — see [`NOTICE.md`](NOTICE.md) |
| [`run-output/explainer.html`](run-output/explainer.html) | The same page, **byte-identical** to what the run wrote, banner and all changes absent |
| [`run-output/plan.md`](run-output/plan.md) | The plan the model wrote **before** it was allowed to search |
| [`run-output/claims.json`](run-output/claims.json) | Every extracted claim with effect size, CI, absolute numbers, design, n, and provenance |
| [`run-output/claims_adjudicated.json`](run-output/claims_adjudicated.json) | The same claims with both verdicts and the final tag |
| [`run-output/adjudication.md`](run-output/adjudication.md) | Claim-by-claim table, and each disagreement quoted in full |
| [`run-output/verdicts/`](run-output/verdicts/) | The eight raw verdict files — four from each verifier, one per sub-question, with the URL each actually opened |
| [`run-output/CITATIONS.md`](run-output/CITATIONS.md) | Vancouver references with their adjudicated tags |
| [`run-output/figures_log.md`](run-output/figures_log.md) | Every figure attempt, including the failures and why they failed |
| [`prompts/demo_prompt.md`](prompts/demo_prompt.md) | The prompt that produced all of this. This is the whole method |
| [`prompts/chatbot_prompt.md`](prompts/chatbot_prompt.md) | The shorter chat-interface version of the same discipline |
| [`prompts/verify_job_1.txt`](prompts/verify_job_1.txt) … `_4` | What the adversarial verifier was actually told, per sub-question |
| [`prompts/judge_job.txt`](prompts/judge_job.txt) | What the figure referee was told |
| [`figures/`](figures/) | The three figures, plus SVG sources and build scripts for the two drawn deterministically |
| [`media/demo_full.mp4`](media/demo_full.mp4) | 4 min 17 s of the recorded run, sped up (26 MB) |
| [`media/demo_screencast.mp4`](media/demo_screencast.mp4) | The shorter 1 min 35 s cut, the one played during the talk (15 MB) |

### How it works

1. **Plan first.** Sub-questions, eligible designs, inclusion and exclusion rules and the recency
   window are written and printed before any retrieval, so the method cannot be fitted to the answer.
2. **Fan out.** One subagent per sub-question, in parallel, each fetching primary full text rather
   than a secondary summary, each recording DOI, PMID, the exact quoted sentence and the location.
3. **Debate.** Every claim goes to two verifiers with **independent retrieval paths**, both told to
   refute. Verifier A is Claude Opus 4.8. Verifier B is OpenAI GPT-5.6-Sol, run through the codex
   CLI, required to retrieve each source itself rather than trust any excerpt handed to it. Two
   models agreeing about the same excerpt tests only whether they can read. Two models agreeing after
   fetching the paper separately tests something.
4. **Adjudicate.** The rule is applied in code, not by a model: both confirmed keeps the claim tagged
   `[verified x2]`; one confirmed and one disputed keeps it only with the disagreement quoted inline;
   anything unretrievable is tagged and excluded from the bottom line. No model votes on whether its
   own work was good enough.
5. **Draw, then judge.** A generated figure may carry no number, no percentage and no data claim.
   Pictures carry structure and sequence; numbers live in the table where they have a citation and a
   verdict attached. Every figure is then judged by both models acting as senior REI
   physician-scientists, scored on fabricated data, garbled text, anatomical and procedural
   correctness, and legibility when projected.
6. **Build.** One self-contained page carrying the provenance tags where the reader sees them, not in
   a log nobody opens.
7. **Write.** Pitched at a senior physician-scientist, per-transfer and cumulative live birth kept
   strictly distinct, effect sizes with confidence intervals and absolute risk differences.

### What went wrong, kept on the record

[`run-output/figures_log.md`](run-output/figures_log.md) and the closing section of the run record
four things that did not go to plan. They are published rather than tidied away, because a
demonstration of checkable work that hides its own failures is not a demonstration of anything.

- **Two of the three figures were abandoned as AI images.** The generator cloned the fresh-transfer
  uterus from the frozen-transfer one, erasing the stimulated versus quiescent ovarian distinction
  that was the entire point of the panel. It baked prompt adjectives onto the canvas as literal
  labels. It misspelled `transcervicaly`. Figures 1 and 3 were rebuilt as hand-authored SVG where
  every label is under direct control and a build-time assertion rejects any digit in the drawing.
  Figure 2 was generated and passed both judges on the first attempt.
- **The adjudication rule had no case for both verifiers disputing a claim.** That happened twice. It
  was handled as `[refuted x2]` and excluded like the unverified case, and the extension is flagged
  in `adjudication.md` so it is not mistaken for the original rule.
- **One retrieval subagent returned a degenerate answer** with zero tool calls and was re-run.
- **The codex CLI refuses to start in a directory that is not a git repository**, failing fast with a
  zero exit code. It was handled with an explicit flag.

### Reproducing it

Claude Code, plus the codex CLI for the second verifier. Paste the fenced block from
[`prompts/demo_prompt.md`](prompts/demo_prompt.md) into a session in a writable folder. Steps 1 to 3
alone are the useful core and work without a second vendor. Steps 4 to 7 add the adversarial check,
the visual gate on generated figures, and the written output.

Versions used for this run: Claude Opus 4.8, and OpenAI GPT-5.6-Sol via codex-cli 0.145.0 at
reasoning effort max. Search window 2015-01-01 to 2026-07-22.

## Licensing

Code under [MIT](LICENSE). Prose, figures and generated pages under
[CC BY 4.0](LICENSE-CONTENT). Quoted sentences from published papers, the status of the generated
figure, and the single documented difference between the two copies of `explainer.html` are all
addressed in [`NOTICE.md`](NOTICE.md).
