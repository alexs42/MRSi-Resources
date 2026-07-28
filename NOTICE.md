# Notice: third-party material, and what was changed after the run

## Quoted material from published papers

`run-output/claims.json`, `run-output/claims_adjudicated.json`, `run-output/adjudication.md` and the
eight files in `run-output/verdicts/` contain **short verbatim sentences quoted from published
papers** — from the *New England Journal of Medicine*, *The Lancet*, the *BMJ*, *Human
Reproduction*, *Reproductive BioMedicine Online* and the Cochrane Database of Systematic Reviews,
among others.

Those sentences are quoted for scholarly commentary and verification. Quoting them is the entire
point: a claim that cannot be checked against the sentence it came from is not a checkable claim.
Each quotation is short, is attributed by DOI and PMID, and sits beside the verdict that two
independent verifiers returned on it.

**The papers themselves are not redistributed here.** The run downloaded full-text PDFs and XML from
publishers into a working directory in order to read them. None of that is in this repository. The
`local_path` and `retrieval_path` fields in the claims files still name which cached artifact each
claim was read from, so the audit trail is intact, but the artifacts are not included. Follow the
DOI to reach the paper.

The reported effect sizes, confidence intervals, event counts and sample sizes are **facts about**
those papers rather than expressive content of them.

If you hold rights in any quoted work and want a specific quotation shortened or removed, open an
issue on this repository.

## Figures

`figures/fig1` and `figures/fig3` are hand-authored SVG, drawn by the run and reproducible from
`gen_fig1.py` and `gen_fig3.py`. `figures/fig2.png` was produced by a generative image model
(`google/gemini-3.1-flash-image-preview`). Copyright in machine-generated images is unsettled in
several jurisdictions; the CC BY 4.0 grant in `LICENSE-CONTENT` is offered to the extent any rights
subsist, and no warranty of title is given for that one file.

None of the three figures contains a number, a percentage, a rate, a sample size or an axis with
values. That was a build-time rule, asserted in code and checked by two model judges. Numbers live
in the tables, where each one carries a citation and a verdict.

## Third-party images in the presentation

Two slides of `presentation.html` carry images that are **not** mine and are **not** covered by the
CC BY 4.0 grant in `LICENSE-CONTENT`:

- **"LLMs have anterograde amnesia"** — the theatrical poster for *Memento*, a still frame from the
  same film, and a stock photograph of a tattooed forearm.
- **"Amplify, don't replace"** — a three-panel meme built from press photographs of two identifiable
  people, watermarked `imgflip.com` and `CausalPython.io`.

They are reproduced here as they appeared in the talk, for commentary. Each of those slides carries a
visible credit line saying so. All rights in them remain with their respective holders. If you hold
rights in any of them and want one removed, open an issue on this repository.

Every other figure in the deck is the author's own, most of them generated or hand-built for this
talk.

## The one thing changed after the run finished

`run-output/explainer.html` is **byte-identical** to what the run wrote on 2026-07-22
(MD5 `3cbd5bdc8f7dd47f7f7aa6874cf43610`). Nothing in it was corrected, re-worded or re-styled.

The copy served at the root of this repository — `explainer.html`, the one the landing page links to
— is that same file with **exactly one addition**: a disclaimer banner at the top of the `<body>`,
stating that the page is unreviewed demonstration output and not medical advice. No other byte
differs. You can confirm this yourself:

```bash
diff <(sed '/id="mrsi-disclaimer"/,/<\/aside>/d' explainer.html) run-output/explainer.html
```

The disclaimer needed to be on the page people actually open, and the unedited original needed to
stay unedited. Publishing both is the only way to have both.

## Scrubbing

Before the first commit, two strings were rewritten throughout: an author's home directory path
(`/home/…/mrsi-demo/` → `./`) and the path to a local environment file holding API keys
(→ `<your .env file>`). 64 occurrences across 7 files. No credential value appeared anywhere in the
run's output — the models withheld them — and none is present here. The rewrites were applied before
`git init`, so nothing removed exists in the repository history either.
