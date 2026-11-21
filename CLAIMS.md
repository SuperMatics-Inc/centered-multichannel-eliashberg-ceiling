# Claims of version 2, with labels and sources

Revision state: the reviewed manuscript source has sha256 `94e095d1649d283a3ee093b9dc3d5d6d1107f3c7c32fb8e00ac943c5e1bc9d94` and 14 pages. The release copy `paper/main.tex` has sha256 `76e6e35f1cd98901f02a9001048c8c7e8636c8e4f18c74f41d3cdf4a5bc7129a`; it differs from the reviewed source in exactly two places, the two reserved version 2 DOIs substituted for the two placeholders, and in no other byte. `paper/main.pdf` is built from that release source. The reviewed predecessor source has sha256 `55fb5f12a41a195db241bae618ceaff93962d4c7ff86ddda71ab50b4fe326fec`. This version states claims 1 and 4 with the correct denominator, keeps the direction of the two superscripts in claim 1, and carries the sharpness sentence, the provenance of the decimal enclosures, the table status cell, the title, the percentage pair and the covering-mechanics phrase in the form the independent reviews approved.

Sources are the shipped close-out record of the new result in `records/aniso-close/`: `RIGOR.md` (proof record), `CHECKS.txt` (executed commands, observed exit codes and receipts) and `replay.py` and `independent.py` (the two exact covering programs). Line anchors below are lines of the shipped files. Evidence that is reported only in the working close-out record is marked as such; this map cites what the repository carries.

Label vocabulary used in the paper: Proved (human-reviewed analysis plus machine-certified exact arithmetic, not formalised), Certified (the finite exact-arithmetic statement on its own), Numerical (floating point, no enclosure), Open (undecided). Version 1 used the same vocabulary; this version changes which statements carry which label, not the vocabulary.

## 1. Supremum bound with the certified three-stage reserve

- Claim: the edge reserve is `d_3 = 3189/10000 > 159/500`, so `S_cent <= C_3 = sqrt(6811/5000)/(2 pi)` over the whole centered class, with `(1-d_3)` and `2(1-d_3) = 6811/5000`.
- Label: **CERTIFIED** for the continuum reserve including all three exterior regions; **PROVED** for the analytic application that turns it into the onset bound.
- Sources: `records/aniso-close/RIGOR.md:60` (edge inequality target `B_r + I/2 >= d B_r` at `d = 3189/10000`), `RIGOR.md:162` (consequence `S_cent <= C_3`), `CHECKS.txt:554` and `CHECKS.txt:671` (primary cover exits 0, both bases), `CHECKS.txt:559` and `CHECKS.txt:717` (independent cover exits 0, both bases).
- Paper locations: abstract (`paper/main.tex:51`), Theorem 1 (`paper/main.tex:131-145`), Proposition 3 (`paper/main.tex:166-170`), reserve share table (`paper/main.tex:297-306`), certificate section (`paper/main.tex:425-446`).

## 2. Strict bound at the first-version constant, with exact bare gap

- Claim: for every model of the class `k_B T_lin < C_* sqrt(rho)`, `C_* = sqrt(341/250)/(2 pi)`, because `C_3 < C_*`; at `tau = C_* sqrt(rho)` the bare gap of the form equals the rational `9/6820 > 0`.
- Label: **PROVED** for the bound; the bare gap number is **CERTIFIED**.
- Sources: `records/aniso-close/RIGOR.md:167` (strict report at `d_report = 159/500 < d`, exact bare gap `9/6820`), `CHECKS.txt:620-621` (exact rational enclosures of both constants, from which `C_3 < C_*` follows).
- Paper locations: Theorem 1 and the gap identity (`paper/main.tex:131-152`), its use in the proof of Theorem 1 (`paper/main.tex:190-196`), limits paragraph (`paper/main.tex:491`, `paper/main.tex:499`).

## 3. Exact rational enclosures of both constants

- Claim: `0.1857550243987982 < C_3 < 0.1857550243987983` and `0.1858777114719168 < C_* < 0.1858777114719169`; `C_3` is about `0.066%` below `C_*` and about `1.66%` above `C_inf = 0.18272624777232952`.
- Label: **CERTIFIED**.
- Sources: `records/aniso-close/CHECKS.txt:620` (enclosure of `C_3`), `CHECKS.txt:621` (enclosure of `C_*`), `CHECKS.txt:623` (improvement interval), `CHECKS.txt:136` and `CHECKS.txt:140` (same enclosure of `C_*` in rational and decimal form).
- Paper locations: Theorem 1 enclosures (`paper/main.tex:141-145`), abstract (`paper/main.tex:51`), table row for `C_3` (`paper/main.tex:459`), excess sentences after the table (`paper/main.tex:477`).

## 4. Certificate description: both exact checkers, heads and guarded runs

- Claim: the primary exact cover has 367 leaves at maximum depth 24 with exact leaf area 1 on the symmetric domain, aborting at depth 30; the independent cover has 1036 leaves at maximum depth 13 with exact leaf area 4/3 on the full domain, aborting at depth 16; both cover 43 head intervals, that is 1849 head pairs, exactly once; each program carries ten deliberately corrupted runs, and all twenty exit 1 at documented mathematical guards.
- Label: **CERTIFIED**.
- Sources: `records/aniso-close/CHECKS.txt:554` (`EXACT primary three-stage cover: d=3189/10000; leaves=367; depth=24; area=1; heads=43`), `CHECKS.txt:559` (`EXACT independent three-stage cover: d=3189/10000; leaves=1036; depth=13; area=4/3; heads=43`), `CHECKS.txt:501` (depth caps 30 and 16; both `d = 3189/10000` commands exit 0), `CHECKS.txt:376` (the historical depth caps 22 and 12 of the superseded search, recorded as superseded), `CHECKS.txt:346-347` (`UNEXPECTED: []`, runner exit 0), `CHECKS.txt:5` and `CHECKS.txt:761` (final verifier runner exit 0).
- Paper locations: certificate section (`paper/main.tex:425-444`), replay paragraph (`paper/main.tex:513`), abstract (`paper/main.tex:51`).

## 5. Next grid point of the reserve left unresolved

- Claim: the reserve `d = 3190/10000` is unresolved, neither rejected nor shown impossible; the next certification attempt exhausted its budget, and the second program was never started for that value.
- Label: **UNRESOLVED** in the source record; the paper states it in words as "unresolved" and draws no conclusion from it, so nothing in the paper is labelled Open on that basis.
- Sources: `records/aniso-close/CHECKS.txt:501` (depth caps, search budget, both `d = 3189/10000` commands exit 0, the next primary command timed out and the next independent command was not started), `CHECKS.txt:565-566` (`UNRESOLVED_TIME_BUDGET: 3190/10000` and `NEXT_GRID_NOT_CERTIFIED: 3190/10000`), `CHECKS.txt:456-461` (the two commands issued for that reserve), `CHECKS.txt:7`.
- Paper locations: abstract (`paper/main.tex:51`), version 2 note (`paper/main.tex:76`), reserve search paragraph (`paper/main.tex:446`).

## 6. Floor of the edge-reserve method and its scope

- Claim: the frozen-sequence edge-reserve argument cannot give a constant below 0.185411, which is a statement about the method and not a lower bound for `S_cent`; `C_3` lies 0.19% above that floor, so the floor sits at the fraction 0.886 of the interval `[C_inf, C_3]`.
- Label: **PROVED** in the predecessor preprint (the floor is a reviewed result there, quoted with its explicit witness `Lambda > 1.357186`); the version 2 sentence only applies it to the new constant and is not itself a new claim.
- Sources: the predecessor preprint, cited by DOI in `paper/refs.bib`, as quoted in `paper/main.tex:479-487`; the version 2 close-out record restates its scope in `records/aniso-close/RIGOR.md:5` (a numerical screen is not a stability enclosure) and in `RIGOR.md:40` (the historical decomposition is numerical and not recomputed).
- Paper locations: abstract (`paper/main.tex:51`), method floor paragraph (`paper/main.tex:72-74`), floor subsection (`paper/main.tex:479-487`), limits paragraph (`paper/main.tex:491`, `paper/main.tex:499`).

## 7. Numerical evidence: the edge-ratio sweep and the generated-model screen

- Claim: a direct sweep over six hundred admissible centered Poisson weight sequences observed the smallest reserve `0.32147971`; a finite-resolution screen of twenty-four generated two- and three-channel models found the largest gain `0.99993728` and a fixed-angular trial understating the gain by up to `0.51`. Neither is an enclosure, neither is an instability of a coupled branch, and neither is evidence about a supremum.
- Label: **NUMERICAL**.
- Sources: `records/aniso-close/RIGOR.md:32` (executed bounded screen: seed 20261120, 24 two- and three-channel generated models, `N=48`, pairing cutoff 32, maximum gain `0.9999372823416597`, largest trial underestimation `0.5102134749644756`), `CHECKS.txt:347-356` (the observed screen output), `RIGOR.md:40` (the historical reserve decomposition, including the numerical minimum, is not recomputed or certified).
- Paper locations: floor subsection (`paper/main.tex:487`), open question section (`paper/main.tex:507`).

## 8. The open question

- Claim: `C_inf <= S_cent <= C_3`; whether `S_cent = C_inf` and whether `S_cent > C_inf` is open, and the paper decides neither; it also does not decide whether `S_cent = C_3`, since `C_3` is an upper bound and no model attaining it is exhibited or excluded.
- Label: **OPEN** (unchanged from version 1 in substance).
- Sources: `records/aniso-close/RIGOR.md:5` (open: the full coupled centered supremum equality, including the two-channel unequal-DOS case), `RIGOR.md:173` (open: full coupled equality, a genuinely larger sharp subclass, and a coupled variational comparison).
- Paper locations: abstract (`paper/main.tex:51`), Remark 2 (`paper/main.tex:153-155`), open question section (`paper/main.tex:503-507`).

## Statements that version 2 deliberately does not make

No claim that `S_cent = C_inf`, no claim that `S_cent` is strictly above `C_inf`, no claim that `S_cent = C_3`, no claim of attainment, no claim that `d = 3190/10000` is impossible, no claim that the numerical sweep or the screen is a stability enclosure, no claim that the edge-reserve floor bounds `S_cent` from below, and no claim about any material, compound or measured transition temperature. `C_3` and `C_*` bound a linear model onset temperature `T_lin` only.
