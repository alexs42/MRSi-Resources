# Claude Code CLI demo prompt: "fresh vs frozen embryo transfer" evidence review

*Shown on the talk's Part-3 slide and shared here so you can reproduce the demo.
Paste the fenced block into a Claude Code session, in a folder where you can write files.

It is written to make the **agentic** behaviour visible. It plans before it searches, fans out parallel
subagents, and then puts every number through **two independent verifiers from two different vendors**
(Claude Opus 4.8 and OpenAI GPT-5.6-Sol) before any of it is allowed into the answer. Speed is not the
point. Disciplined, checkable evidence is.*

**Two versions of the discipline.** Steps 1, 2 and 3 alone are the loop that traced every number in this
talk back to its page, and they are enough on their own. Steps 4 through 7 are what the live demo adds:
a second vendor's model as an adversarial check, a visual gate on AI-generated figures, and a written
output at the level of a senior physician-scientist. Take whichever depth fits your work.

---

```
You are running a focused evidence review on FRESH versus FROZEN (elective frozen, "freeze-all")
single embryo transfer in IVF, and then publishing it as a self-contained HTML explainer.
Audience: practising REI physicians and reproductive scientists. Three outcomes matter:
(1) live birth, (2) OHSS and safety, (3) any signal in subgroups (PGT-A, ovulatory vs PCOS).

Work in this order and SHOW me each step. Print a banner line before each phase so I can see
where you are.

1. PLAN FIRST. Before searching, write a short plan: the exact sub-questions, the study designs
   that would answer them (prioritise RCTs and meta-analyses of RCTs), inclusion and exclusion
   rules, and the recency window. Print the plan as a checklist. Do not search until the plan is
   on screen.

2. FAN OUT. Spawn one subagent per sub-question (no more than four at once) and run them in
   parallel. Each subagent must:
      a. find candidate papers (use the paper-lookup and parallel-web skills; prefer PubMed,
         Cochrane, and the primary journal),
      b. fetch the PRIMARY source, full text or PDF, not a blog and not a secondary summary,
      c. extract only the load-bearing numbers: effect size, 95% CI, absolute numbers, n, design,
      d. record provenance: DOI and PMID, the exact quoted sentence, and the page or section.
   Write the pooled result to claims.json, one record per claim.

3. DEBATE. Every claim now goes to TWO independent adversarial verifiers, and they must not share
   a retrieval path. Both are instructed to REFUTE, not to agree.

      Verifier A - Claude Opus 4.8. Spawn a subagent per sub-question. It re-opens the source and
      tries to show the number is wrong, or right only in a different population than claimed.

      Verifier B - OpenAI GPT-5.6-Sol. Run it yourself, from the shell, one call per sub-question,
      and WAIT for each to finish:

          codex exec -s workspace-write -c approval_policy=never - < verify_job_N.txt

      Do NOT pass --effort; the flag is rejected and the correct setting is already the default.
      Verifier B must retrieve the source ITSELF rather than trusting any excerpt you hand it.
      That independence is the whole point: two models agreeing after retrieving separately means
      something, two models agreeing about the same excerpt means nothing.

   Each verifier returns, per claim, one of:
      CONFIRMED     - the number appears as stated, in the stated population. Quote the sentence.
      DISPUTED      - it does not. Say precisely what is wrong and quote what the source says.
      UNRETRIEVABLE - full text could not be obtained. Say what was tried.

4. ADJUDICATE. Tally the two verdicts mechanically. Do not let a model decide this; apply the rule:
      both CONFIRMED           -> keep, tag [verified x2]
      one CONFIRMED one DISPUTED -> keep ONLY with the disagreement quoted inline, tag [disputed]
      either UNRETRIEVABLE     -> tag [unverified - source not retrieved], and DO NOT USE IT in the
                                  bottom line or the summary table
   Write adjudication.md with a table: Claim | Opus 4.8 | GPT-5.6-Sol | Final | Convergent.
   Then de-duplicate papers by DOI to PMID, and where studies disagree say so and prefer the
   stronger design. Note ASRM and ESHRE positions with their year if you find them.
   If the two models agreed on everything, say so plainly. Convergence is a result, not a failure,
   and you must never manufacture a disagreement.

5. DRAW, THEN JUDGE. Generate the explanatory figures, then gate them.
      a. Generate each figure:
            python3 ~/.claude/skills/generate-image/scripts/generate_image.py "<prompt>" -o figN.png
         Leave the model at its default. Express size and aspect in the prompt itself; there are
         no flags for them.
      b. HARD RULE: a generated figure may carry NO number, NO percentage, and NO data claim.
         Pictures are for structure and sequence. Every number lives in the table, where it is
         traceable. If a figure needs a value on it, that is a table, not a picture.
      c. Judge every figure with BOTH models, each acting as a senior REI physician-scientist, and
         score it on: no fabricated data; no garbled or misspelled text; anatomical and procedural
         correctness a practising REI physician or embryologist would accept; legibility when
         projected. Opus 4.8 reads the file directly. For GPT-5.6-Sol:

            codex exec -s workspace-write -c approval_policy=never -i figN.png - < judge_job.txt

      d. Any REJECT or REVISE from either judge means regenerate, at most twice. If it still fails,
         abandon the AI image and build that figure deterministically instead, in Graphviz or plain
         HTML and CSS, where you control every label. Log what failed and why in figures_log.md.

6. BUILD. Produce explainer.html: ONE self-contained scrolling page, no external network requests,
   fonts and images inlined as base64, readable on a phone. It must contain, in order:
      the bottom line - the outcome table (effect sizes, 95% CIs, absolute differences, design, n)
      - the judged figures - the adjudication table from step 4 - Vancouver-numbered references each
      tagged [verified x2] or [disputed] or [unverified] - an explicit "what is still uncertain"
      list - and a short method note naming both models and their versions.

7. WRITE. The prose, and especially the closing summary, is pitched at a SENIOR MD/PhD REI
   PHYSICIAN-SCIENTIST, not at a general clinician. That means:
      - Assume fluency in agonist and antagonist protocols, segmentation, VEGF-mediated OHSS
        pathophysiology, endometrial and embryo synchrony, PGT-A, and cumulative versus
        per-transfer outcomes. Do not explain what these are.
      - Give effect sizes with 95% CIs AND absolute risk differences. A relative risk alone is
        not an answer.
      - Name the design explicitly - multicentre RCT, meta-analysis of RCTs, registry - report
        heterogeneity, and where trials disagree, say which population drives the disagreement.
      - Keep per-transfer and cumulative live birth strictly distinct. Conflating them is the
        standard error in this literature.
      - Close on what would change practice, and what evidence would be needed to change it.
      - Write in long, information-dense sentences that carry their qualifications inside them.
        Assert directly where the evidence supports it. No em dashes. No "it is worth noting",
        "importantly", "notably", "delve", "landscape", "robust", "holistic". No throat-clearing,
        no hedging cascades, and do not set up a gap in the literature just to fill it.

Rules that override everything above: no fabricated citations, numbers, or quotations, ever. If you
are unsure, say so in the chat rather than inventing a plausible value. A claim that failed
retrieval is reported as unverified and left out, not softened into the text. And do not stage any
of this for effect: if nothing was disputed and nothing was rejected, report that honestly.
```

---

**Why this prompt is built the way it is**

- **Plan-then-act** makes the model commit to a method before it can see any results, which is what
  stops it from cherry-picking the studies that agree with the answer it drifted toward.
- **Subagent fan-out** parallelises the search and keeps each thread small enough to audit.
- **Two vendors, two retrieval paths.** One model checking its own work measures its consistency, not
  its accuracy. A second model from a different lab, fetching the paper itself and told to refute,
  is the first check that can actually fail. The disagreements are printed rather than resolved
  silently, because the disagreements are the useful part.
- **Mechanical adjudication.** The rule for what survives is arithmetic, applied to the two verdicts.
  No model gets to decide whether its own claim was good enough.
- **A picture may carry no number.** The model that draws is not the model that verifies, and an image
  generator has no notion of whether a value is real. Structure goes in the figure; every number goes
  in the table, where it has a citation and a verdict attached to it.
- **Provenance tags survive into the output.** `[verified x2]`, `[disputed]`, `[unverified]` are on the
  page the reader sees, not in a log the reader never opens. If a number could not be checked, the
  reader learns that at the same moment they learn the number.
