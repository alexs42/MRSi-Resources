# Evidence Review Plan: Fresh vs Elective Frozen (freeze-all) Embryo Transfer

Written BEFORE any retrieval. Audience: practising REI physicians and reproductive scientists.

## Sub-questions (one subagent each, 4 in parallel)

### SQ1 — Live birth, whole population
Does elective cryopreservation of all embryos with subsequent FET change live birth versus fresh
transfer in unselected autologous IVF/ICSI? **Per-transfer LBR (first transfer) and cumulative LBR
(per woman randomised, all transfers from one retrieval) must be extracted and reported separately.**
Conflating these is the standard error in this literature and is a pre-specified extraction field.

- Designs that answer it: Cochrane / systematic review and meta-analysis of RCTs (highest weight);
  multicentre RCTs; individual-participant-data meta-analysis.
- Designs that do not: single-centre cohorts, registry analyses, before-after series.

### SQ2 — OHSS and safety
Ovarian hyperstimulation syndrome (any, and moderate/severe) plus obstetric and perinatal safety:
hypertensive disorders of pregnancy / pre-eclampsia, large-for-gestational-age and macrosomia,
small-for-gestational-age and low birthweight, preterm birth.

- Designs: RCTs and meta-analyses of RCTs first. Registry/cohort admitted ONLY for outcomes RCTs
  cannot power (rare obstetric events), and labelled as such — never used to overturn RCT evidence.

### SQ3 — PCOS versus ovulatory
Does the live-birth effect differ by ovulatory status? This is the axis on which the field turns.
Extract per-trial population definition, and whether the trial excluded women at OHSS risk.

- Designs: the pivotal multicentre RCTs, plus subgroup/meta-regression analyses within meta-analyses
  of RCTs. Subgroup claims graded lower than main effects unless pre-specified and tested for
  interaction.

### SQ4 — PGT-A, segmentation subgroups, and practice positions
Does PGT-A change the fresh-versus-frozen calculus? Signal in high responders. Also capture ASRM and
ESHRE committee opinions / guidelines **with year**.

- Designs: RCTs of PGT-A where transfer policy is documented; meta-analyses of RCTs; named society
  documents cited as positions, not as evidence.

## Pre-specified extraction fields (every claim)

1. Effect measure (RR / OR / risk difference) with 95% CI
2. Absolute numbers: events / n in BOTH arms
3. Absolute risk difference (computed from the absolute numbers if not reported)
4. Design and n randomised
5. **Per-transfer or cumulative** — mandatory, no claim accepted without it
6. **Number of embryos transferred (SET vs DET)** — see caveat below
7. Heterogeneity (I-squared, tau-squared) for meta-analyses
8. Population descriptors: ovulatory status, age, responder status, stage, freezing method,
   endometrial preparation, trigger
9. Provenance: DOI, PMID, exact quoted sentence, section or page

## Pre-specified caveat to test, not assume

The question is posed as **single** embryo transfer. Several pivotal freeze-all RCTs transferred
**two** embryos. Every subagent must record embryos transferred per trial. If the pivotal evidence is
DET-based, that is reported as a transferability limitation, not silently mapped onto SET practice.

## Inclusion rules

1. Population: autologous IVF/ICSI with ovarian stimulation
2. Intervention: elective freeze-all / segmentation, subsequent FET
3. Comparator: fresh transfer in the stimulated cycle
4. Outcomes: live birth (per-transfer AND cumulative), OHSS, obstetric/perinatal safety, subgroups
5. Design: RCT or SR/MA of RCTs preferred; observational only where flagged and only for rare outcomes
6. Window: **2015-01-01 to 2026-07-22** primary. Older RCTs admitted only via inclusion in an
   in-window meta-analysis. Explicitly check for any post-2021 Cochrane update and any 2022-2026 RCT.
7. Source: PRIMARY full text or PDF (publisher or PMC). DOI + PMID mandatory.

## Exclusion rules

1. Donor-oocyte, recipient, and gestational-carrier cycles, unless reported as a separate stratum
2. Non-elective freezing as the sole comparison (freezing forced by OHSS risk or endometrial factors)
   — contaminates the elective question. PGT-A-driven freezing is handled separately as SQ4.
3. FET protocol-versus-protocol comparisons (natural vs programmed vs modified natural) — different
   question, out of scope
4. Conference abstracts without full text, narrative reviews, editorials, blogs, news, secondary
   summaries. Non-peer-reviewed preprints flagged if used at all.
5. Duplicate publications of one cohort — de-duplicate by DOI to PMID and by trial registration number

## Verification and adjudication

- Every claim goes to two verifiers with independent retrieval paths: Claude Opus 4.8 (subagent,
  re-opens source) and OpenAI GPT-5.6-Sol (codex exec, retrieves the source itself).
- Verdicts: CONFIRMED / DISPUTED / UNRETRIEVABLE.
- Mechanical rule: both CONFIRMED -> keep [verified x2]; one CONFIRMED one DISPUTED -> keep only with
  the disagreement quoted inline [disputed]; either UNRETRIEVABLE -> [unverified], excluded from the
  bottom line and the summary table.
- No fabricated citation, number, or quotation. Failed retrieval is reported as failed, not softened.
