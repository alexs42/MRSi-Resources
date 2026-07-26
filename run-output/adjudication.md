# Adjudication

Two independent verifiers, each instructed to refute rather than to agree, each required to
retrieve every source itself and explicitly forbidden from reading the other's cached artefacts.

- **Verifier A** Claude Opus 4.8, one subagent per sub-question, re-opening each source.
- **Verifier B** OpenAI GPT-5.6-Sol via codex-cli 0.145.0 at reasoning effort max, one shell
  invocation per sub-question, retrieving every source itself.

The rule was applied in code, not by a model (`adjudicate.py`):

| Verdict pair | Result |
|---|---|
| both CONFIRMED | keep, tag `[verified x2]` |
| one CONFIRMED, one DISPUTED | keep **only** with the disagreement quoted inline, tag `[disputed]` |
| either UNRETRIEVABLE | tag `[unverified - source not retrieved]`, excluded from the bottom line and summary table |
| both DISPUTED | **not covered by the specification.** Handled as `[refuted x2]` and also excluded. Flagged here so the extension is not mistaken for the original rule. |

## Result

- Claims adjudicated: **57**
- Convergent (both verifiers returned the identical verdict): **44/57** (77%)
- `[verified x2]`: **42**
- `[disputed]`: **12**
- `[refuted x2]`: **2**
- `[unverified - source not retrieved]`: **1**

**The two models did not agree on everything.** They returned different verdicts on
13 of 57 claims. Each disagreement is quoted below rather than resolved silently.

## Claim-by-claim

| Claim | Opus 4.8 | GPT-5.6-Sol | Final | Convergent |
|---|---|---|---|---|
| **SQ1-C1** In unselected women undergoing IVF/ICSI, a freeze-all strategy produced no detecta... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ1-C2** In the same Cochrane review, live birth after the FIRST embryo transfer per random... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ1-C3** In 1508 infertile women with polycystic ovary syndrome undergoing their first IVF ... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ1-C4** In the same PCOS trial (Chen 2016), the CUMULATIVE live-birth rate including all f... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ1-C5** In 2157 OVULATORY infertile women undergoing a first IVF cycle in China, live birt... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ1-C6** In 782 infertile women WITHOUT polycystic ovary syndrome at a single centre in Vie... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ1-C7** In the same Vietnamese trial, the CUMULATIVE 12-month live-birth rate among women ... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ1-C8** In 1650 OVULATORY women with good prognosis undergoing a first IVF cycle at 21 Chi... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ1-C9** In 460 women aged 18-39 with regular menstrual cycles at eight public hospitals in... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ1-C10** In the same Danish/Swedish/Spanish trial followed for a minimum of two years, the ... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ1-C11** In the E-Freeze pragmatic multicentre UK trial of 619 couples across 18 clinics - ... | Confirmed | Disputed | `disputed` | **no** |
| **SQ1-C12** As of this search there is NO published individual-participant-data meta-analysis ... | Disputed | Disputed | `refuted x2` | yes |
| **SQ2-C1** In a Cochrane meta-analysis of 6 RCTs (4478 women) comparing a 'freeze all' strate... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ2-C2** In Chen 2016 (multicentre RCT, 1508 infertile women with PCOS undergoing a first I... | Disputed | Confirmed | `disputed` | **no** |
| **SQ2-C3** In Shi 2018 (multicentre RCT, 2157 ovulatory infertile women, day-3 double embryo ... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ2-C4** In Santos-Ribeiro 2020 (single-centre RCT, 209 high responders with >=18 follicles... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ2-C5** In E-Freeze 2022 (pragmatic multicentre RCT, 18 UK clinics, 619 couples randomised... | Disputed | Confirmed | `disputed` | **no** |
| **SQ2-C6** In Stormlund 2020 (multicentre RCT, 460 women with regular menstrual cycles, singl... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ2-C7** In a Cochrane meta-analysis of 3 RCTs (3940 women; Chen 2016, Vuong 2018, Wei 2019... | Disputed | Confirmed | `disputed` | **no** |
| **SQ2-C8** In Chen 2016 (1508 women with PCOS), preeclampsia was more frequent after frozen-e... | Disputed | Confirmed | `disputed` | **no** |
| **SQ2-C9** In Wei 2019 (multicentre RCT, 1650 ovulatory women with good prognosis, SINGLE bla... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ2-C10** In Shi 2018 (2157 ovulatory women, the largest single freeze-all versus fresh RCT)... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ2-C11** In a Cochrane meta-analysis of 3 RCTs (3940 women; Vuong 2018, Wei 2019, Zhang 201... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ2-C12** In the Cochrane review, the cumulative risk of a small-for-gestational-age baby wa... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ2-C13** In a Cochrane meta-analysis of 5 RCTs (1607 singletons), singleton birth weight wa... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ2-C14** In the Cochrane review, cumulative preterm delivery (<37 weeks) was lower after fr... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ2-C15** In Stormlund 2020 (460 women, single blastocyst transfer, freeze-all arm using a M... | Disputed | Confirmed | `disputed` | **no** |
| **SQ2-C16** In a Nordic population-based registry cohort with within-sibship analysis (Medical... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ3-C1** In 1508 infertile women with PCOS undergoing a first IVF cycle (Chen 2016), electi... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ3-C2** In the same PCOS trial (Chen 2016), the CUMULATIVE live-birth rate including all f... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ3-C3** In 2157 OVULATORY infertile women undergoing a first IVF cycle (Shi 2018), freeze-... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ3-C4** Shi et al. themselves attribute the discrepancy with the PCOS trial to the trial p... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ3-C5** In 782 infertile women explicitly WITHOUT PCOS (Vuong 2018, Vietnam), freeze-all d... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ3-C6** Vuong et al. explicitly state that their null result in women without PCOS is not ... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ3-C7** In 1650 OVULATORY women with regular menstrual cycles and good prognosis (Wei 2019... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ3-C8** The cumulative live-birth advantage in Wei 2019's ovulatory population disappears:... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ3-C9** In 460 women with regular menstrual cycles in Denmark, Sweden and Spain (Stormlund... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ3-C10** The Cochrane review of fresh versus frozen embryo transfer (Zaat 2021) performs NO... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ3-C11** The only source that formally models interactions using data from both the PCOS an... | Confirmed | Disputed | `disputed` | **no** |
| **SQ3-C12** The only meta-analysis that stratifies freeze-all versus fresh transfer by a physi... | Disputed | Disputed | `refuted x2` | yes |
| **SQ3-C13** A meta-analysis restricted specifically to ovulatory / non-PCOS women (Jin 2021) p... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ3-C14** A prospectively registered individual participant data meta-analysis of freeze-all... | Confirmed | Disputed | `disputed` | **no** |
| **SQ4-C1** In the STAR multicentre RCT, ongoing pregnancy at 20 weeks (which equalled live bi... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ4-C2** In the STAR trial, ongoing pregnancy/live birth analysed per intention to treat at... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ4-C3** In a POST HOC subgroup analysis of the STAR trial, PGT-A raised ongoing pregnancy/... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ4-C4** In the Yan 2021 multicentre RCT, the cumulative live birth rate after up to three ... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ4-C5** Yan 2021 found no significant difference between PGT-A and conventional IVF in ong... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ4-C6** The 2020 Cochrane review of PGT-A found that NO randomised trial reported cumulati... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ4-C7** In a 2022 systematic review and meta-analysis of nine RCTs of comprehensive-chromo... | Confirmed | Unretrievable | `unverified` | **no** |
| **SQ4-C8** The Coates 2017 RCT randomised 179 patients who were ALL undergoing PGT-A/NGS to f... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ4-C9** In the Bosdou 2019 meta-analysis of eight RCTs (5,265 patients) comparing the firs... | Confirmed | Disputed | `disputed` | **no** |
| **SQ4-C10** The high-responder freeze-all signal in Bosdou 2019 is driven almost entirely by C... | Confirmed | Disputed | `disputed` | **no** |
| **SQ4-C11** In a randomised trial confined to predicted high responders defined by an explicit... | Confirmed | Disputed | `disputed` | **no** |
| **SQ4-C12** The 2024 ASRM/SART Practice Committee opinion on PGT-A states that routine use of ... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ4-C13** The same 2024 ASRM/SART Practice Committee opinion records that potential risks of... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ4-C14** The 2023 ESHRE good practice recommendations on add-ons in reproductive medicine s... | Confirmed | Confirmed | `verified x2` | yes |
| **SQ4-C15** The same 2023 ESHRE good practice recommendations state that preimplantation genet... | Confirmed | Disputed | `disputed` | **no** |

## Every disagreement, quoted

### SQ1-C11 &mdash; `disputed`
> In the E-Freeze pragmatic multicentre UK trial of 619 couples across 18 clinics - an unselected IVF/ICSI population and the only major trial published after the Cochrane search date - elective freeze did not improve live birth after the first embryo transfer and the point estimate favoured fresh: 87/307 (28.3%) versus 106/309 (34.3%), adjusted risk ratio 0.83 (99% CI 0.65 to 1.06).

**GPT-5.6-Sol disputes:** The live-birth counts and adjusted RR are present, but this was not an unselected IVF/ICSI population: randomisation occurred only after at least three good-quality Day-3 embryos were available. Of 1578 consented couples, 959 were not randomised, including 476 because three good-quality embryos were unavailable. The effect metadata also mislabels 0.65 to 1.06 as a 95% CI; Table II specifies a 99% CI for this secondary outcome. Finally, the 'only major trial published after the Cochrane search date' assertion is no longer true: a 2025 BMJ multicentre freeze-all-versus-fresh RCT randomised 838 women with low IVF prognosis (https://www.bmj.com/content/388/bmj-2024-081474).

**Claude Opus 4.8 confirms, quoting:** "The live birth rate {28.3% versus 34.3%; RR, 99% CI: 0.83 (0.65 to 1.06)} and clinical pregnancy rates {33.9% versus 40.1%; RR, 99% CI: 0.85 (0.65 to 1.11)} were lower in the elective freeze arm, but there is no statistically significant difference ( Table  II )."

### SQ1-C12 &mdash; `refuted x2`
> As of this search there is NO published individual-participant-data meta-analysis of freeze-all versus fresh transfer: the INFORM IPD meta-analysis exists only as a protocol (BMJ Open 2022, PROSPERO CRD42021296566), with live birth resulting from the first embryo transfer as its planned primary outcome.

**Claude Opus 4.8 disputes:** The claim's central assertion is refuted. It states 'As of this search there is NO published individual-participant-data meta-analysis of freeze-all versus fresh transfer: the INFORM IPD meta-analysis exists only as a protocol'. INFORM results are published, in three places, and the most SQ1-relevant one reports precisely the outcome this sub-question is about. (1) Fertility and Sterility, October 2024, DOI 10.1016/j.fertnstert.2024.07.251, 'WHO BENEFITS MOST FROM A FREEZE-ALL EMBRYO TRANSFER STRATEGY? AN INDIVIDUAL PARTICIPANT DATA META-ANALYSIS OF RANDOMISED CONTROLLED TRIALS (INFORM)', Wang R, Au LS, Wei D, ... Legro RS, Wang Z, Sun Y, Wu K, Vuong LN et al: 'The primary outcome was live birth following the first transfer', results as quoted above, and 'CONCLUSIONS The freeze-all and fresh embryo transfer strategies did not differ significantly in overall live birth rate following the first transfer, although a freeze-only strategy benefitted patients with elevated progesterone levels on trigger day.' (2) Human Reproduction 40(Supplement_1), June 2025, DOI 10.1093/humrep/deaf097.1086, 'P-782 Obstetric and Neonatal Outcomes following Freeze-all vs Fresh Embryo Transfer Strategies: An Individual Participant Data Meta-Analysis of Randomised Trials (INFORM)' (Au N, Wang R, Wei D, Vuong LN, Pinborg AB et al), 12 RCTs, 8222 participants, hypertensive disorders 2.9% vs 1.8% aRR 1.66, LGA 17.8% vs 13.1% aRR 1.38, SGA 5.7% vs 8.1% aRR 0.71, and it states in terms 'Our earlier work on this IPD-MA found no significant live birth rate differences between the two groups'. (3) A full results manuscript is posted as a 2026 preprint, DOI 10.2139/ssrn.7001926, 'Frozen Versus Fresh Embryo Transfer in IVF - An Individual Participant Data Meta-Analysis of Randomised Controlled Trials (INFORM)', with the full INFORM author list and the same PROSPERO registration CRD42021296566: search 'up until 24 September 2025', 'Among 16 eligible trials, IPD from 13 trials involving 9060 randomised participants (96% of eligible participants) were obtained', primary outcome 'live birth following the first embryo transfer', result 'no evidence that a freeze-all embryo transfer strategy differed from a fresh embryo transfer on live birth rate following the first transfer (adjusted risk ratio (aRR) 1.00, 95% confidence interval (CI) 0.86 to 1.17, moderate-certainty evidence)', plus OHSS aRR 0.28 (0.18 to 0.43, high certainty) and major congenital anomaly aRR 0.73 (0.63 to 0.85), and the interpretation 'In unselected IVF population, the freeze-all and fresh embryo transfer strategies are comparable in terms of live birth rate following the first transfer'. WHY THE CLAIM MISSED IT: its stated search used PubMed and OpenAlex only, and neither indexes ASRM/ESHRE abstracts published in Fertility and Sterility or Human Reproduction supplements, nor SSRN preprints; the Europe PMC citation list for the protocol has just one entry. WHY THIS MATTERS FOR SQ1, beyond the bibliographic point: the claim's own note argues 'the IPD will therefore not by itself resolve the cumulative question'. That framing now needs revising, because the IPD result on the per-first-transfer outcome is NULL (aRR 1.00, 0.86-1.17 in the full analysis; 1.04, 0.92-1.18 in the earlier 12-trial version) and therefore directly contradicts Cochrane's pooled per-first-transfer OR 1.17 (1.06-1.28) with I2=74% - the IPD analysis, adjusted for age and BMI and using 96% of eligible participants, brings the per-transfer estimate into line with the cumulative null rather than leaving the two timings in conflict. WHAT SURVIVES: the protocol itself is real and correctly described - I verified via Europe PMC that BMJ Open 2022 PMID 35851030 states 'The primary outcome will be live birth resulting from the first embryo transfer', that PROSPERO registration is CRD42021296566, and that 'The search was performed on 23 September 2020 and will be updated'. The quote the claim attributes to the protocol is verbatim.

**GPT-5.6-Sol disputes:** The 2022 protocol and its planned first-transfer primary outcome are real, but the categorical statement that INFORM exists only as a protocol and has published no results is false. Fertility and Sterility published this INFORM primary-results abstract in October 2024. Human Reproduction also published an INFORM obstetric/neonatal IPD-results abstract in June 2025 (https://academic.oup.com/humrep/article/40/Supplement_1/deaf097.1086/8170259). I did not need to infer that a full-length results article exists: these published results abstracts alone refute 'no results have been published.'

### SQ2-C2 &mdash; `disputed`
> In Chen 2016 (multicentre RCT, 1508 infertile women with PCOS undergoing a first IVF cycle with up to two day-3 cleavage-stage embryos transferred), elective freeze-all reduced moderate or severe OHSS compared with fresh transfer (1.3% vs 7.1%; rate ratio 0.19, 95% CI 0.10 to 0.37; P<0.001).

**Claude Opus 4.8 disputes:** The effect estimate, the outcome definition and the quote are all EXACT - 'moderate or severe ovarian hyperstimulation syndrome' is genuinely the trial's wording, it is genuinely a prespecified secondary outcome, and 'Moderate and severe ovarian hyperstimulation syndromes were defined according to accepted criteria' with reference 25 = Golan et al. 1989 is genuinely in the Methods. What is WRONG is the claim's field high_risk_excluded: 'no - this trial deliberately enrolled PCOS women, the archetypal high-OHSS-risk population, which is why the fresh-arm OHSS rate is high (7.1%)'. Chen 2016 DID exclude high-OHSS-risk women, at exactly the same point and by exactly the same mechanism as Shi 2018: randomisation happened on the day of oocyte retrieval and only patients 'at low risk for the ovarian hyperstimulation syndrome (as determined by local investigators)' (and with >3 and <30 oocytes) were randomised. The claim's causal gloss is therefore unsupported: the 7.1% fresh-arm rate arose DESPITE screening out high-risk women, not because they were included. This also silently undermines the contrast the claim set drew in SQ2-C3's notes, which presents Shi 2018 as the trial that uniquely 'screened out' high-risk women.

**GPT-5.6-Sol confirms, quoting:** "The incidence of moderate or severe ovarian hyperstimulation syndrome was significantly lower in the frozen-embryo group than in the fresh-embryo group (1.3% vs. 7.1%), for a rate ratio of 0.19 (95% CI, 0.10 to 0.37; P<0.001) (Table 4)."

### SQ2-C5 &mdash; `disputed`
> In E-Freeze 2022 (pragmatic multicentre RCT, 18 UK clinics, 619 couples randomised, over 80% single embryo transfer, hCG trigger in both arms because randomisation occurred on day 3 after fertilisation), OHSS was 11/307 (3.6%) after elective freeze versus 25/309 (8.1%) after fresh transfer (RR 0.44, 99% CI 0.15 to 1.30; p=0.051), a non-significant difference, with 6 cases (1.9%) of severe OHSS occurring only in the fresh arm.

**Claude Opus 4.8 disputes:** The headline is exact - 'The risk of OHSS was 3.6% (11/307) in the elective freeze arm compared to 8.1% (25/309) in the fresh embryo transfer arm (RR 0.44, 99% CI: 0.15 to 1.30) (Table II). The severity of ovarian hyperstimulation was only mild to moderate in the elective freeze group, whereas there were 6 cases (1.9%) of severe OHSS in the fresh embryo transfer group' is verbatim, 619 couples across 18 UK clinics 2016-2019 is verbatim, single embryo transfer 249/298 (83.6%) and 247/303 (81.5%) confirms 'over 80%', the exclusion 'a clinical indication for an elective freeze such as OHSS or fertility preservation' is verbatim, and 'The risk of OHSS was not reduced by an elective freeze policy' is verbatim. WHAT IS WRONG is the claim's statistical annotation: 'the corresponding 95% CI given in the outcome table is 0.18 to 1.10'. It is not a 95% CI. Table II's own footnote states 'CIs are 95% for the primary outcome and 99% for all secondary outcomes', and OHSS is a secondary outcome, so 0.44 (0.18 to 1.10) is the UNADJUSTED RR with a 99% CI while 0.44 (0.15 to 1.30) is the ADJUSTED RR with a 99% CI - the claim has both mislabelled the interval level and conflated unadjusted with adjusted. I verified this arithmetically: for 11/307 vs 25/309, log-RR SE = 0.353, giving a 99% CI of 0.18 to 1.10 (matching the table exactly) and a 95% CI of 0.22 to 0.88. This is material, not cosmetic: the true 95% interval EXCLUDES 1, so the trial's 'non-significant' verdict rests entirely on its prespecified 99% intervals, and a reader relying on the claim's annotation would report a non-significant 95% CI that does not exist. The claim set is internally inconsistent on this point - SQ2-C14's notes correctly label the same column's preterm-delivery entry (0.91, 0.31 to 2.65) as a 99% CI.

**GPT-5.6-Sol confirms, quoting:** "The risk of OHSS was 3.6% (11/307) in the elective freeze arm compared to 8.1% (25/309) in the fresh embryo transfer arm (RR 0.44, 99% CI: 0.15 to 1.30) (Table II). The severity of ovarian hyperstimulation was only mild to moderate in the elective freeze group, whereas there were 6 cases (1.9%) of severe OHSS in the fresh embryo transfer group."

### SQ2-C7 &mdash; `disputed`
> In a Cochrane meta-analysis of 3 RCTs (3940 women; Chen 2016, Vuong 2018, Wei 2019), hypertensive disorders of pregnancy after the first embryo transfer were more frequent following a freeze-all strategy than conventional fresh transfer (63/1962 vs 29/1978; Peto OR 2.15, 95% CI 1.42 to 3.25; I2 = 29%), an absolute increase of 1.74 percentage points.

**Claude Opus 4.8 disputes:** OUTCOME DEFINITION MISQUOTED. The claim's outcome_definition field states the review prespecified HDP as 'Hypertensive disorders of pregnancy, comprising pregnancy-induced hypertension (PIH), pre-eclampsia (PE) and [eclampsia]'. The review's Methods actually read '...pregnancy-induced hypertension (PIH), pre-eclampsia (PE) and haemolysis, elevated liver enzymes, and low platelets in the blood (HELLP syndrome)'. The bracketed '[eclampsia]' is a reconstruction presented inside quotation marks as the review's own wording, and it is wrong: the third component of the composite is HELLP syndrome, not eclampsia. Everything else in this claim survived attack and is EXACT: 63/1962 vs 29/1978, Peto OR 2.15 [1.42, 3.25], Chi2 = 2.84, df = 2 (P = 0.24), I2 = 29%, Z = 3.63 (P = 0.0003); the denominators really are per randomised woman (746/762, 391/391, 825/825); the overall-across-subgroups figures the claim reports (1.80 [1.23, 2.64], I2 = 59%, subgroup difference Chi2 = 4.46, df = 1, P = 0.03, I2 = 77.6%) are exact; the Summary of Findings row '15 per 1000 ... 31 per 1000 (21 to 46)' is exact; and Vuong 2018 does sit left of the null in both subgroups. Also correctly flagged: Shi 2018, Stormlund 2020 and E-Freeze 2022 are genuinely absent from this pooled estimate.

**GPT-5.6-Sol confirms, quoting:** "The risk of hypertensive disorders might be increased following the 'freeze all' strategy (Peto OR 2.15, 95% CI 1.42 to 3.25; I2 = 29%; 3 RCTs, 3940 women; low-quality evidence; Analysis 1.9; Figure 6)."

### SQ2-C8 &mdash; `disputed`
> In Chen 2016 (1508 women with PCOS), preeclampsia was more frequent after frozen-embryo transfer than fresh-embryo transfer (4.4% vs 1.4%; rate ratio 3.12, 95% CI 1.26 to 7.73; P=0.009), although no patient in either group had severe preeclampsia.

**Claude Opus 4.8 disputes:** The quoted sentence, the percentages, the rate ratio, the CI, the P value and the 'no patient in either group had severe preeclampsia' rider are all EXACT. The defect is the same false eligibility statement as SQ2-C2: the field high_risk_excluded is set to 'no', but Chen 2016 randomised only women 'at low risk for the ovarian hyperstimulation syndrome (as determined by local investigators)' on the day of oocyte retrieval. SECOND, WEAKER POINT, recorded for the caller's benefit rather than as a refutation: the claim assigns timing 'per-pregnancy' but no openly retrievable source states the Table 4 denominator - NEJM Table 4 does not render through any route I could reach (curl 403, the Unpaywall-listed PDF endpoint 403, and two parallel-cli extracts returned the body text but not the table). I can prove only that it is NOT per randomised woman: Cochrane Analysis 1.9, which I read directly, enters this trial's hypertensive disorders of pregnancy as 29/746 vs 11/762, and since pre-eclampsia is a subset of HDP a 4.4% pre-eclampsia rate cannot sit on a denominator of 746 (that would require about 33 events, more than the 29 HDP events). So the denominator is restricted to pregnancies or deliveries, consistent with but not proof of the claim's label. By analogy the sister trial Shi 2018, same investigators and journal, labels its equivalent row 'Preeclampsia among clinical pregnancies'.

**GPT-5.6-Sol confirms, quoting:** "However, the incidence of preeclampsia was significantly higher with frozen-embryo transfer (4.4% vs. 1.4%), for a rate ratio of 3.12 (95% CI, 1.26 to 7.73; P=0.009), although no patient in either group had severe preeclampsia."

### SQ2-C15 &mdash; `disputed`
> In Stormlund 2020 (460 women, single blastocyst transfer, freeze-all arm using a MODIFIED NATURAL endometrial preparation cycle in all but two women), there was no difference in pre-eclampsia (4/57 [7.0%] vs 4/55 [7.3%]; P=1.00) or pregnancy-induced hypertension (2/57 [3.5%] vs 2/55 [3.6%]; P=1.00) between the freeze-all and fresh transfer arms.

**Claude Opus 4.8 disputes:** PROVENANCE AND DENOMINATOR BOTH MISSTATED. (1) The claim cites 'Table 3 (maternal complications)'. Table 3 is the INTENTION-TO-TREAT reproductive-outcomes table and contains no maternal complications; the pre-eclampsia and PIH rows are in Table 4, which is explicitly labelled '(as-treated analysis)'. (2) The claim sets timing to 'per-pregnancy' and describes the population as 'pregnancies continuing beyond 22 weeks'. The table's own footnote defines the denominator as the number of DELIVERIES (stillbirths plus live births) and restricts it to 'pregnancies and births after frozen embryo transfers in freeze-all group and fresh transfers in fresh transfer group'. That is a per-delivery, as-treated denominator, not a per-pregnancy randomised comparison. This is material rather than pedantic in THIS trial specifically, because Table 2 shows 37/230 (16.1%) of the fresh arm were converted to elective frozen transfer, 24/230 (10.4%) of them for OHSS risk - those women's pregnancies came after a frozen transfer and are therefore excluded from the 55-delivery fresh-arm denominator, so the comparison labelled 'multicentre RCT' is not the randomised contrast. THE FOUR NUMBERS THEMSELVES ARE EXACT (4/57 [7.0%] vs 4/55 [7.3%], P=1.00; 2/57 [3.5%] vs 2/55 [3.6%], P=1.00), the post-hoc status of PIH is correctly stated ('Post hoc analysis was performed for selected obstetric outcomes (pregnancy induced hypertension, gestational diabetes, chorioamnionitis, postpartum haemorrhage, induction of birth, mode of birth ..., twin rates, and duration of hospital stay)' is verbatim), the pointer to 'Supplementary table S1 provides definitions of secondary outcomes' is verbatim, the Discussion passage about the corpus luteum is verbatim, and Table 2 does confirm the modified natural cycle in 160/162 (98.8%) with programmed cycle in only 2/162 (1.2%), i.e. 'all but two'.

**GPT-5.6-Sol confirms, quoting:** "In this trial, all but two women randomised to the freeze-all group had frozen-thawed blastocyst transfer in a modified natural endometrial preparation cycle.
Pregnancy induced hypertension 2/57 (3.5) 2/55 (3.6) 1.00
Pre-eclampsia 4/57 (7.0) 4/55 (7.3) 1.00"

### SQ3-C11 &mdash; `disputed`
> The only source that formally models interactions using data from both the PCOS and the ovulatory trial (Wei 2018, JCEM) fitted SEPARATE logistic models within each population and tested treatment-by-ovarian-response interactions inside each; it reports P<0.001 for the treatment-by-oocyte-number and treatment-by-peak-estradiol interactions on live birth in PCOS women and non-significant interactions in ovulatory women, but it does NOT report a pooled treatment-by-ovulatory-status interaction p-value.

**GPT-5.6-Sol disputes:** The detailed characterization of Wei 2018 is accurate: it fitted separate PCOS and ovulatory models, reported P<0.001 for the two PCOS treatment-by-response interactions, found no significant corresponding interactions in ovulatory women, and did not report a pooled treatment-by-PCOS-status test. The word “only” is now false, however. A completed INFORM IPD meta-analysis preprint was posted on SSRN on 29 June 2026 under the same prospective registration, CRD42021296566. It formally investigated prespecified treatment-covariate interactions across 13 trials (9060 participants); its protocol explicitly prespecified PCOS/WHO group II anovulation as a participant-level treatment-covariate interaction. Thus Wei 2018 is no longer the only source formally modeling interactions with data spanning these trial populations.

**Claude Opus 4.8 confirms, quoting:** "To evaluate the effect of ovarian response on pregnancy outcomes after frozen and fresh embryo transfer, two series of multivariable logistic regression models were built in women with PCOS and in ovulatory women, respectively, with backward process for variable selection."

### SQ3-C12 &mdash; `refuted x2`
> The only meta-analysis that stratifies freeze-all versus fresh transfer by a physiological proxy for the PCOS/ovulatory axis (Bosdou 2019, by ovarian responder type) reports live-birth relative risks that are nearly identical in the two strata - 1.18 (95% CI 1.06-1.31) in high responders and 1.13 (95% CI 0.90-1.41) in normal responders - so the apparent subgroup difference is a difference in precision, not in effect size, and no interaction test is reported.

**Claude Opus 4.8 disputes:** The claim opens with a false uniqueness assertion: 'The ONLY meta-analysis that stratifies freeze-all versus fresh transfer by a physiological proxy for the PCOS/ovulatory axis (Bosdou 2019, by ovarian responder type)'. It is not the only one, and the other one predates it. Roque M, Haahr T, Geber S, Esteves SC, Humaidan P. 'Fresh versus elective frozen embryo transfer in IVF/ICSI cycles: a systematic review and meta-analysis of reproductive outcomes.' Hum Reprod Update 2019;25(1):2-14, PMID 30388233, doi 10.1093/humupd/dmy033, stratifies on exactly the same axis. Its abstract states verbatim: 'Subgroup analyses included normal and hyper-responder patients, embryo developmental stage on the day of embryo transfer, freezing method and the route of progesterone administration for luteal phase support in eFET cycles' and 'Subgroup analyses indicated higher LBRs by eFET than by fresh embryo transfer in hyper-responders (RR = 1.16; 95% CI: 1.05-1.28) and in PGT-A cycles (RR = 1.55; 95% CI: 1.14-2.10). However, no differences were observed for LBR in normo-responders (RR = 1.03; 95% CI: 0.91-1.17)'. On WebFetch of the Roque full text the strata are labelled explicitly as 'PCOS/hyper-responder patients' versus 'non-PCOS/normo-responders' with 4 studies/2035 patients and 3 studies/3076 patients respectively - i.e. Roque stratifies on the PCOS/ovulatory axis MORE directly than Bosdou does, not merely by proxy. The Cochrane review names both in the same breath, verbatim: 'Two recently published systematic reviews and meta-analyses, Roque 2019 and Bosdou 2019 reported a higher live birth rate after the first transfer in the freeze all strategy compared to conventional IVF/ICSI... In Roque 2019 this increased live birth rate was only found in hyper-responders and in cycles with PGT-A.' This omission is material rather than pedantic, because the claim's substantive argument is that the apparent subgroup difference is 'a difference in precision, not in effect size'. That argument is weaker once Roque is included: Roque's strata differ by 0.13 on the RR scale (1.16 versus 1.03), nearly three times Bosdou's 0.05 gap, and Roque's normo-responder interval (0.91-1.17) is tight rather than wide, so the null result there cannot be dismissed as imprecision. Everything else in the claim checks out: both relative risks and both confidence intervals are verbatim correct, the population description is correct, the timing (live birth after the FIRST frozen transfer in a freeze-only strategy) is correct, and the limitation sentence is verbatim correct - 'the analysis did not apply a standard for determining high or normal responders since the type of ovarian response followed the characterisation of populations as reported by the authors of the eligible studies'. I also independently confirm the claim's two flagged caveats: (i) WebFetch of the Bosdou full text reports that no formal test for subgroup differences, interaction test or meta-regression is present, so 'no interaction test is reported' stands; (ii) the published abstract really is internally inconsistent on stratum sizes - it states four RCTs with n=3255 in normal responders and four RCTs with n=2010 in high responders, yet the live-birth analysis reports n=3398 in high responders, which exceeds the stated high-responder total. The fix is to delete the word 'only' and add Roque 2019 as a second, concordant, earlier subgroup meta-analysis.

**GPT-5.6-Sol disputes:** The two pooled RR estimates and confidence intervals do appear in the source, but the live-birth sample sizes printed beside them are internally impossible and assigned to the wrong populations. Table II identifies the three high-responder live-birth trials as Absalan (100), Chen (1508), and Aflatoonian (280), totaling 1888—not 3398. It identifies the three normal-responder live-birth trials as Coates (179), Shi (2157), and Vuong (782), totaling 3118—not 1608. The article separately states that all four high-responder RCTs total only 2010 participants and all four normal-responder RCTs total 3255. In addition, no cross-stratum interaction test was performed, so “a difference in precision, not in effect size” is an interpretation of similar point estimates, not a tested source result.

### SQ3-C14 &mdash; `disputed`
> A prospectively registered individual participant data meta-analysis of freeze-all versus fresh transfer trials (INFORM, PROSPERO CRD42021296566) was designed specifically to examine treatment-covariate interactions across trials, but as of this search only the protocol has been published and no results paper could be located, so no IPD-based interaction test by ovulatory status is yet available.

**GPT-5.6-Sol disputes:** The protocol quotation is accurate, but the time-sensitive assertion that only the protocol has been published is obsolete. A 29-page INFORM results preprint, “Frozen Versus Fresh Embryo Transfer in IVF – An Individual Participant Data Meta-Analysis of Randomised Controlled Trials (INFORM),” was posted on SSRN on 29 June 2026 and cites PROSPERO CRD42021296566. It reports 13 trials and 9060 randomized participants, an adjusted RR for live birth after first transfer of 1.00 (95% CI 0.86 to 1.17), formal prespecified treatment-covariate analyses, a nonlinear progesterone interaction, and no strong evidence of subgroup effects for the other baseline covariates. The abstract does not print a standalone PCOS/ovulatory-status interaction P value, but the categorical claim that there is still no INFORM results report or IPD interaction analysis is false.

**Claude Opus 4.8 confirms, quoting:** "We will invite the lead investigators of eligible trials to join the Individual participant data meta-analysis of trials comparing frozen versus fresh embryo transfer strategy (INFORM) collaboration and share the deidentified individual participant data (IPD) of their trials. We will harmonise the IPD and perform a two-stage meta-analysis and examine treatment-covariate interactions for important baseline characteris"

### SQ4-C9 &mdash; `disputed`
> In the Bosdou 2019 meta-analysis of eight RCTs (5,265 patients) comparing the first frozen transfer in a freeze-only strategy with fresh transfer, live birth was significantly more likely with the frozen strategy in HIGH responders (RR 1.18, 95% CI 1.06-1.31, I2=0%, three studies) but not in NORMAL responders (RR 1.13, 95% CI 0.90-1.41, I2=77%, three studies), with responder status assigned according to each individual trial's own definition rather than a single oocyte-yield threshold.

**GPT-5.6-Sol disputes:** The pooled RR, CI, heterogeneity, trial counts, and author-defined responder classification are reported, but the claim's per-transfer timing is wrong. The endpoint was live birth per randomized participant under ITT, not live birth conditional on an embryo transfer. Separately, the paper is internally inconsistent: it reports n=3,398 for the three high-responder live-birth studies despite stating that all four high-responder RCTs together contained only 2,010 patients; the claim does not resolve that source inconsistency.

**Claude Opus 4.8 confirms, quoting:** "The study was categorised as having been performed in normal, high or poor responders based on the definition given by the authors of each eligible RCT."

### SQ4-C10 &mdash; `disputed`
> The high-responder freeze-all signal in Bosdou 2019 is driven almost entirely by Chen 2016, an RCT restricted to 1,508 women with polycystic ovary syndrome in which frozen transfer gave live birth after the first transfer in 49.3% versus 42.0% with fresh transfer (rate ratio 1.17, 95% CI 1.05-1.31, P=0.004) - a rate ratio essentially identical to the pooled high-responder estimate.

**GPT-5.6-Sol disputes:** The 49.3% versus 42.0%, RR 1.17 (95% CI 1.05–1.31), P=0.004 result and the PCOS population are correct, but the claim labels the result per-transfer. It was an ITT comparison among 1,508 randomized women of live birth during/after the first transfer, not a rate conditional on actually receiving a transfer. The article reports 170 women dropped out or deviated from protocol, yet retained the randomized-group ITT comparison.

**Claude Opus 4.8 confirms, quoting:** "Frozen-embryo transfer resulted in a higher frequency of live birth after the first transfer than did fresh-embryo transfer (49.3% vs. 42.0%), for a rate ratio of 1.17 (95% confidence interval [CI], 1.05 to 1.31; P=0.004)."

### SQ4-C11 &mdash; `disputed`
> In a randomised trial confined to predicted high responders defined by an explicit threshold of at least 18 follicles measuring at least 11 mm, freeze-all did not significantly improve pregnancy outcomes compared with fresh transfer supported by low-dose hCG (live birth 42/101, 41.6% versus 41/104, 39.4%), while moderate-to-severe ovarian hyperstimulation syndrome occurred only in the fresh-transfer arm (9/105, 8.6% versus 0/104).

**GPT-5.6-Sol disputes:** The follicle threshold, live-birth counts, lack of a significant pregnancy difference, and OHSS counts are correct, but the stated per-transfer timing is not. These were randomized-group outcomes after the first transfer. The live-birth denominators were available-case modified-ITT denominators after excluding four patients lost to follow-up (one fresh, three freeze-all), not numbers of embryo transfers; three post-randomization consent withdrawals were also excluded.

**Claude Opus 4.8 confirms, quoting:** "The intention to treat clinical pregnancy and live birth rates (with the latter excluding four cases lost to follow-up: one in the fresh transfer and three in the freeze-all arms, respectively) after the first embryo transfer did not vary significantly among the fresh embryo transfer and freeze-all study arms: 51/105 (48.6%) versus 57/104 (54.8%) and 41/104 (39.4%) versus 42/101 (41.6%), respectively (relative risk f"

### SQ4-C15 &mdash; `disputed`
> The same 2023 ESHRE good practice recommendations state that preimplantation genetic testing for aneuploidy is currently not recommended for routine clinical use, and separately record that because blastocyst biopsy is combined with shallow sequencing, freeze-all of biopsied embryos is mostly applied in these cycles - explicitly linking PGT-A to obligatory cryopreservation and its attendant risks.

**GPT-5.6-Sol disputes:** The recommendation against routine PGT-A use is present, and the document links these cycles to freeze-all and its risks. However, the claim's characterization of cryopreservation as obligatory is not supported: the source says it is “mostly applied,” not required in every PGT-A cycle.

**Claude Opus 4.8 confirms, quoting:** "Pre-implantation genetic testing for aneuploidy is currently not recommended for routine clinical use."

## De-duplication by DOI to PMID

57 claims resolve to **21 unique sources**. Every source carried exactly one DOI
and one PMID; no source appeared under two identifiers and no cohort was published twice in this set.

| PMID | DOI | Claims | Design |
|---|---|---|---|
| 33539543 | 10.1002/14651858.cd011184.pub3 | 10 | meta-analysis of RCTs |
| 27509101 | 10.1056/nejmoa1513873 | 7 | multicentre RCT |
| 29320646 | 10.1056/nejmoa1705334 | 5 | multicentre RCT |
| 29320655 | 10.1056/nejmoa1703768 | 4 | single-centre RCT |
| 30827784 | 10.1016/s0140-6736(18)32843-5 | 3 | multicentre RCT |
| 32759285 | 10.1136/bmj.m2519 | 4 | multicentre RCT |
| 40350355 | 10.1016/j.rbmo.2024.104449 | 1 | multicentre RCT (prespecified secondary outcom |
| 34999830 | 10.1093/humrep/deab279 | 2 | multicentre RCT |
| 35851030 | 10.1136/bmjopen-2022-062578 | 2 | IPD meta-analysis (protocol only - no results  |
| 32964939 | 10.1093/humrep/deaa226 | 2 | single-centre RCT |
| 36154568 | 10.1161/hypertensionaha.122.19689 | 1 | registry |
| 29718297 | 10.1210/jc.2018-00613 | 1 | subgroup analysis (post hoc secondary analysis |
| 30689865 | 10.1093/humrep/dey388 | 2 | meta-analysis of RCTs |
| 33006114 | 10.1007/s43032-020-00323-2 | 1 | meta-analysis of RCTs |
| 31551155 | 10.1016/j.fertnstert.2019.07.1346 | 3 | multicentre RCT |
| 34818479 | 10.1056/nejmoa2103613 | 2 | multicentre RCT (noninferiority) |
| 32898291 | 10.1002/14651858.cd005291.pub3 | 1 | meta-analysis of RCTs (Cochrane systematic rev |
| 36201787 | 10.1097/aog.0000000000004962 | 1 | meta-analysis of RCTs |
| 28139240 | 10.1016/j.fertnstert.2016.12.022 | 1 | single-centre RCT |
| 38762806 | 10.1016/j.fertnstert.2024.04.013 | 2 | committee opinion |
| 37747409 | 10.1093/humrep/dead184 | 2 | society guideline (good practice recommendatio |

## Where studies disagree, and which design is preferred

**Live birth, per transfer against cumulative.** Chen 2016 (multicentre RCT, PCOS, n=1508, double
cleavage-stage transfer) and Wei 2019 (multicentre RCT, ovulatory, n=1650, single blastocyst transfer)
both report a per-transfer advantage for segmentation; Shi 2018 (multicentre RCT, ovulatory, n=2157),
Vuong 2018 (single-centre RCT, non-PCOS, n=782), Stormlund 2020 (multicentre RCT, n=460) and E-Freeze
(Maheshwari 2022, multicentre RCT, n=619) report none. The disagreement is not resolved by choosing
between trials. It is resolved by the denominator: in both Chen and Wei the advantage disappears when
the same trial is counted cumulatively. The stronger design for this question is the meta-analysis of
RCTs reporting cumulative live birth per woman randomised, which is null at OR 1.08 (0.95 to 1.22) with
I-squared of 0%, and which the Cochrane authors themselves nominate as the outcome relevant to women.
The per-first-transfer pooled estimate is preferred by no one, including the review that reports it.

**Ovulatory status.** The apparent conflict between Chen (positive, PCOS) and Shi (null, ovulatory) is
routinely read as a population effect. Wei 2019 breaks that reading, because it is an ovulatory
population with a large per-transfer advantage, and Stormlund breaks it further, because it is
ovulatory, single blastocyst, and null. No design in this evidence base tests the interaction, so the
population claim is not supported at any level of design strength. Preferring the stronger design here
means preferring the one that exists: none of them tested it.

**Hyperstimulation.** Stormlund 2020 is excluded from interpretation on this outcome despite being a
multicentre RCT, because it used a GnRH agonist trigger in the freeze-all arm against hCG in the fresh
arm and converted 24 of 230 fresh-arm women to freezing for hyperstimulation risk under protocol. Design
label alone does not make a trial informative for a given outcome. Santos-Ribeiro 2020 is a
single-centre RCT and therefore lower in the conventional hierarchy, but it triggered both arms with an
agonist and is the cleanest available test of the fresh transfer itself.

**Hypertensive disorders.** The pooled Peto OR of 2.15 (1.42 to 3.25) rests on 92 events in three
trials and excludes Shi 2018, the largest trial in the field, which reported a null pre-eclampsia
result. Registry evidence is stronger on this outcome than the trial pool in one specific respect, which
is precision, and weaker in the respect that matters more, which is confounding. The within-sibship
Nordic analysis is the strongest observational design available because it conditions on the mother.
It is still labelled registry throughout and is never used to overturn a randomised result.

## Society positions

**ASRM 2024** &mdash; `verified x2` &mdash; committee opinion  
> "At present, however, the routine use of blastocyst biopsy with aneuploidy testing in all infertile patients undergoing IVF treatment cannot be recommended."  
PMID 38762806; DOI 10.1016/j.fertnstert.2024.04.013

**ASRM 2024** &mdash; `verified x2` &mdash; committee opinion  
> "Potential risks of a ‘‘freeze-all’’ strategy include increased risk of maternal hypertensive disorders of pregnancy and having a large-for-gestational-age infant (47)."  
PMID 38762806; DOI 10.1016/j.fertnstert.2024.04.013

**ESHRE 2023** &mdash; `verified x2` &mdash; society guideline (good practice recommendations)  
> "Elective freeze-all is currently not recommended for routine clinical use."  
PMID 37747409; DOI 10.1093/humrep/dead184

**ESHRE 2023** &mdash; `disputed` &mdash; society guideline (good practice recommendations)  
> "Pre-implantation genetic testing for aneuploidy is currently not recommended for routine clinical use."  
PMID 37747409; DOI 10.1093/humrep/dead184

ASRM has no standalone practice document on elective freeze-all. Its only position on the strategy
appears inside the 2024 PGT-A committee opinion.
