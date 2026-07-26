# Figures log

Gate rule applied: a generated figure may carry no number, no percentage and no data claim.
Every figure judged by two models acting as senior REI physician-scientists. Any REJECT or REVISE
from either judge triggers regeneration, at most twice; a figure still failing after that is
abandoned as an AI image and rebuilt deterministically, where every label is under direct control.

Generator: `google/gemini-3.1-flash-image-preview` (the script default, left unchanged) via
`~/.claude/skills/generate-image/scripts/generate_image.py`.

Tooling note: the generate_image.py script reads `OPENROUTER_API_KEY` only from a `.env` file in the
current directory or a parent, and never from the process environment, despite its own error message
advising `export`. The key was therefore passed with `--api-key` from a shell variable rather than
writing a secret into the project directory.

---

## fig1 — Two pathways (fresh versus freeze-all)

**Outcome: AI generation ABANDONED after three failed attempts. Rebuilt deterministically as
hand-authored SVG (`gen_fig1.py` -> `fig1.svg` -> `fig1.png`, rendered at 2x through Playwright
Chromium). Final verdict ACCEPT.**

| Attempt | What failed |
|---|---|
| v1 (AI) | Judge A (Opus 4.8) returned REVISE. No warming step and no time break, so the freeze-all arm did not read as a separate later cycle. Worse, the fresh-transfer uterus was a pixel-level clone of the frozen-transfer uterus (mean difference 6.7/255 after 12 px alignment), so the stimulated cycle was drawn with quiescent, normal-sized ovaries. |
| v2 (AI) | Failed on inspection before judging. The generator rendered my prompt's descriptive adjectives into the canvas as literal labels: `ENLARGED`, `ENLARGED, UN/AND MULTIFOLLICULAR`, `QUIESCENT`. It also misspelled `transcervicaly` (one L) in the upper panel while spelling `transcervically` correctly in the lower panel. Garbled text is an automatic fail. |
| v3 (AI) | Failed on inspection. The entire shared-sequence label row was duplicated: `Ovarian stimulation`, `Oocyte retrieval` and `Fertilisation and culture` each appeared twice, once above and once below the sequence. |
| v4 (deterministic) | Judge A returned REVISE with three source-exact defects: the fresh-arm catheter escaped its panel and visually joined the two supposedly separate pathways; the later-cycle uterus right ovary overflowed the panel border by ~5 units; subtitle contrast was 3.11:1, below WCAG AA. |
| v5 (deterministic, final) | **ACCEPT.** Catheter shortened (cy+152 -> cy+112, teal sheath cy+112 -> cy+72); later-cycle uterus moved cx 1392 -> 1378; subtitle grey darkened #7d8f97 -> #5b6b73, measured 5.13:1. Judge A re-verified by pixel measurement: zero ink outside either panel, all 15 labels correctly spelled, no digits. |

Why the deterministic rebuild is stronger than a fourth generation attempt: the build script asserts
the hard rule rather than trusting inspection. It regexes every rendered `<text>` node for digits and
percent signs and reports the result on every build. It also parameterises ovarian appearance
(`follicles`, `ov_rx`, `ov_ry`) so the stimulated and unstimulated uteri cannot silently collapse into
the same drawing, which is precisely the defect the AI version hid.

---

## fig2 — OHSS mechanism

**Outcome: AI generation ACCEPTED on the first attempt. No regeneration needed.**

Judge A (Opus 4.8) returned ACCEPT and explicitly declined to manufacture a criticism: causal chain
and arrow direction correct, both hCG inputs feeding the ovary rather than the endothelium, the
permeability step drawn at a true vessel wall with apposed endothelial monolayers enclosing a lumen
and visible interendothelial gaps rather than generic tissue, fluid collecting intraperitoneally with
a clear fluid level, and `VEGF` and both instances of `hCG` correctly spelled and correctly cased.
Optional polish was noted (a corpus-luteum cue, egress arrows, hyphenation) but not required.

---

## fig3 — Two denominators (per-transfer versus cumulative)

**Outcome: AI generation ABANDONED after three failed attempts. Rebuilt deterministically as
hand-authored SVG (`gen_fig3.py` -> `fig3.svg` -> `fig3.png`). Final verdict ACCEPT.**

| Attempt | What failed |
|---|---|
| v1 (AI) | Judge A returned REVISE: the third panel was missing the free-standing embryo icon the other two carried, inviting the reading that no embryo remained; the cumulative bracket's tan stroke was identical to the third panel's border colour and to nothing else, so it colour-keyed to one panel while spanning three; and the figure mixed two typefaces. |
| v2 (AI) | Judge A returned REVISE. The three v1 defects were fixed, but at 5x magnification the "embryo" was an unmistakable fetus — large cranium, curled trunk, facial and otic markings, limb bud, umbilical cord, roughly 8-10 week morphology — in **twelve** locations: six cohort icons, three free-standing icons, and inside the cavity of all three uteri. Disqualifying for this audience, and self-defeating in a figure about denominators, since showing a fetus already in the cavity at the moment of transfer presupposes the numerator. |
| v3 (AI) | Failed on inspection. Blastocyst morphology was finally correct, but the generator drew the cumulative bracket spanning only the second and third transfer panels, excluding the first. That inverts the meaning of the only thing the figure exists to convey. |
| v4 (deterministic, final) | **ACCEPT.** Same blastocyst primitive as fig1 (zona pellucida, dashed trophectoderm rim, eccentric inner cell mass); no fetal features at 8x. Bracket spans asserted in code: per-transfer y 35-245 (first panel only), cumulative y 35-765 (all three panels, first included). Judge A confirmed both visually. A subsequent one-line fix reversed the bracket arms to open leftward toward the panels they group, following the usual convention. |

---

## Second judge: GPT-5.6-Sol (codex-cli 0.145.0, reasoning effort max)

Run as `codex exec -s workspace-write --skip-git-repo-check -c approval_policy=never -i figN.png -
< judge_job.txt`, one call per figure, against the final version of each figure.

| Figure | Verdict | Notes |
|---|---|---|
| fig1 | **ACCEPT** | All twelve labels read back correctly. Confirmed the freeze-all arm reads as a separate later cycle, the catheter is transcervical with the embryo deposited near the fundal cavity "rather than in the cervix, myometrium, or tube", and stimulated ovaries contain multiple follicles. No required changes. |
| fig2 | **ACCEPT** | Confirmed both hCG inputs act upstream of the ovary, that permeability is drawn at an endothelial vessel wall, and that fluid sits in the abdominopelvic compartment. Suggested "third-space" and "pregnancy-derived" hyphenation as style, explicitly "not required for accuracy". No required changes. |
| fig3 | **ACCEPT** | Independently accepted the ordinal labels as structural rather than quantitative, and confirmed "the short and long brackets correctly distinguish per-transfer from cumulative outcomes". No required changes. |

**Both judges returned ACCEPT on all three final figures, with no required changes from either.**
The two models were not shown each other's reviews.

---

## Summary

Three figures. One survived AI generation (fig2). Two required deterministic rebuilds after
exhausting the permitted regenerations (fig1, fig3). Six AI generation attempts produced three
distinct classes of failure that no amount of prompt engineering removed: prompt text leaking onto the
canvas as labels, duplicated or misspelled labels, and semantically inverted structure. The two
failures that mattered most, a cloned uterus that erased the stimulated versus unstimulated
distinction and a cumulative bracket that excluded the first transfer, were both invisible to a casual
glance and would have propagated a false claim into a document read by specialists.

Judge agreement is worth stating plainly rather than dramatising: on the final figure set the two
models agreed completely, and neither asked for a change. The disagreements that mattered occurred
earlier, on the intermediate versions, and every one of them was a defect that a reader would
otherwise have inherited.
