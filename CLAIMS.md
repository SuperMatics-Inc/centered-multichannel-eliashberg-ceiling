# Claims map for the preprint "Centered multichannel Eliashberg branches: a sqrt(341/250)/(2 pi) moment-norm ceiling"

RIGOR.md is `replay/RIGOR.md` (reviewed, ACCEPT in `reviews/PROOF-REVIEW.md`).
Checker line numbers are in `replay/replay.py` (primary) and `replay/independent.py`
(independent). Predicate names are the strings passed to `require(...)`, which abort the run with `REJECT:`
when they fail. Analytic claims are marked as such and are not machine-checked.

Status legend: C = checked by both checkers; A = analytic, proved in prose; I = inherited input, pinned by
SHA-256 in `replay/source-pins.json` and not re-derived here.

| # | Claim in the paper | RIGOR.md | Checker evidence | Status |
|---|---|---|---|---|
| 1 | Theorem 1, supremum constant `C_* = sqrt(341/250)/(2 pi)` from reserve `d_* = 159/500` and `2(1-d_*)=341/250` | sections 0, 7 (lines 6-22, 216-225) | replay.py:300 (`d_cert`), replay.py:308 (`alpha_ext = 1 - d_cert - 33/500`), independent.py:286, independent.py:289 (`certified squared numerator`) | C |
| 2 | Theorem 1, strict constant `C_rep = sqrt(6821/5000)/(2 pi)` from `d_rep = 3179/10000`, `2(1-d_rep)=6821/5000` | section 7 (line 223) | independent.py:287 (`d_report`), independent.py:288 (`strict reporting margin`), independent.py:290 (`reported squared numerator`); mutant `strict-budget` in both programs (verify.py cases dict) | C |
| 3 | Bare gap `1 - (1-d_*)/(1-d_rep) = 1/6821 > 0` at the reported temperature | section 7 (lines 216-225) | independent.py:291 (`reported bare gap 1/6821`); replay mutant `strict-budget` | C |
| 4 | Decimal enclosures `0.185877711471916 < C_* < 0.185877711471917` and `0.185891338370617 < C_rep < 0.185891338370618` | section 0 (line 13) | replay.py:323-325 (`certified endpoint decimal enclosure`, `reported endpoint decimal enclosure`); independent.py:309-311, same two predicates; printed identically by both runs (`Exact endpoint enclosures:`) | C |
| 5 | Edge inequality: one reserve `d_*` works for every `r>0`, every `t>0` and every weight sequence of the centered class | sections 2, 5-6 (lines 61-214) | replay.py:335-355 (cover loop, `CERTIFIED primary centered cover: reserve=159/500; leaves=159; max_depth=20; area=1; head_intervals=43`); independent.py:348 (`CERTIFIED independent centered cover: ... leaves=466; max_depth=11; area=4/3; head_intervals=43`) | C |
| 6 | Acceptance predicates are inequalities on closed rational rectangles, hence cover the continuum and not a grid | section 5 (line 193) | replay.py:175-230 (`box_ok_int` with outward-rounded `f_floor`/`f_ceil` on every quantity); independent.py:163 (`cell_ok_full`, four-way subdivision, no symmetry) | C |
| 7 | Centered Poisson lower envelope: the two tangent lines bound `phi_w` below, with checked rational intercepts | section 3 (lines 91-109) | replay.py:126-142 (`make_certified_rational_tangents`, `admissible lower tangent line`: `c_rat <= 0 and lam + c_rat <= 1`); independent.py:315 (independent tangent-intersection integrity calculation), mutant `tangent-intercept` | C |
| 8 | Adjacent tangent intersections are ordered, so enumerating them misses no envelope switch | section 5 (line 159-196) | replay.py:332 (`ordered tangent intersections`); independent.py:313-320; mutant `centered-cone` / `tangent-intercept` | C |
| 9 | On `(0,1/2]` the basic line is the envelope, so the reserve is minimised at `b_0 = 1/2` and `b_0 -> 0` loses nothing | section 5 (line 159-196) | replay.py:333 (`basic tangent on first head interval`) | C |
| 10 | Head partition `0, 1/2, 3/4, 160/200, ..., 1`: gapless, correct endpoints, 43 intervals | section 5 (line 193) | replay.py:293-299 (`head partition endpoints`, `nonempty head subintervals`, `gapless head partition`); independent.py:279-284, same three | C |
| 11 | Primary cover: 159 leaves, maximum depth 20, leaf area exactly 1, `r >= 1` with the channel-exchange symmetry | section 5 (line 193) | replay.py:355 printed receipt; depth cap abort in the cover loop | C |
| 12 | Independent cover: 466 leaves, maximum depth 11, leaf area exactly 4/3, full domain `[1/3,3] x [0,1/2]`, no symmetry, separate completion rationalisation | section 5 (line 193) | independent.py:88-92 and 348 printed receipt; mutant `completion-sign` | C |
| 13 | Sector decomposition `M = 20`, pairs `(0,0)`, `(0,m)`, `(1,k)`, rest, disjoint and exhaustive; split `7/10`; `alpha_ext = 77/125 > 3/5` | section 4 (lines 110-139) | replay.py:78 (`M = 20`), replay.py:308-309 (`new exterior bare budget`); independent.py:294-295, same | C |
| 14 | Infinite tail: the truncated normal tail is bounded by `sum 1/((2m+1)m^2(m+1)^2) + 1/(8*20^4) < 7/75` (value 0.0903550) | section 4 (line 157) | replay.py:310-311 (`far-imbalance infinite tail`); independent.py:296-297, same; mutant `hankel-tail` | C |
| 15 | Tail row costs and the cap, and unretained positive stage-0 completions for `m > 20` via `(43/3) alpha_ext > 2/43` | section 4 (lines 110-158) | replay.py:316 (`unretained positive stage-0 tails`) | C |
| 16 | Three exterior regions give reserves `9/17 - (7/75)/alpha_ext`, `2/5 + (3/4)(alpha_ext/8 - 1/9)/alpha_ext`, `1/3 + (4/9)(alpha_ext/6 - 1/9)/alpha_ext`, each above `d_*`; sign `alpha_ext/8 > 1/25` | section 6 (lines 197-214) | replay.py:311-316 (three reserve predicates plus `exterior higher-tail sign`); independent.py:296-301, same five | C |
| 17 | Cascade: first tail mode is stabilised by higher tail modes, so the reserve exceeds the first-mode turning value | section 4 (lines 140-158) | covered by the same rectangle predicates as claim 5 | C |
| 18 | Twelve guarded mutants, six per program, each exit 1 with a `REJECT:` line, driver aborts on mismatch | section 9 | `verify.py` cases dict; receipt `CHECKS.txt` (13 runs, all exit codes as expected, final line `PASS:`) | C |
| 19 | Thirteen inherited proof and arithmetic files pinned by SHA-256 | section 9 | replay.py:24-26 (`all inherited source pins present`, `inherited proof bytes`); independent.py:25-31, same; mutant `pin` in both | C |
| 20 | Reduction from the folded stability form to the edge inequality (positive resolvent, bounded normal rows, no monotone onset), and strict positive definiteness of `Q` at every `tau > C_* sqrt(rho)` with the bound `beta(tau)/(1 + R(tau)) > 0`, which gives `T_lin <= C_* sqrt(rho)`; the strict statement then follows from `C_* < C_rep` | sections 1-2 and 7 (lines 24-90, 216-225) | none; proved in prose | A |
| 21 | Width cone and the four Harnack inequalities on the centered class; the causal class is not treated | sections 1, 3 (lines 24-60, 91-109) | none; inherited and proved in prose, pinned by hash | A/I |
| 22 | Derivation of the exterior formulas (head estimate `>= 1 - 2/(r + 1/r)`, `>= 9/17` from `r + r^-1 >= 17/4` on `r <= 1/4`, `>= 2/5` from the positive completions, `>= 1/3`, `p_01 <= 4/9`) | section 6 (lines 197-214) | none; only the resulting rational comparisons are checked (claim 16) | A |
| 23 | Method floor `sqrt(Lambda)/(2 pi) > 0.185411` from `Lambda > 1.357186`, i.e. `d < 0.321407`, with the reserve `d_* = 0.318` below it and `C_*` above the floor by `0.25%` | section 8 (lines 59, 236-249) | none here; taken from the earlier reviewed work on the same edge method (hashed in source-pins.json via `../SHARP/RIGOR.md` and the `../FINITE-ENERGY` files). It is a statement about the frozen-weight method, not a lower bound on `S_cent`. | I |
| 24 | `C_inf = 0.18272624777232952` and `S_cent >= C_inf` (scalar case belongs to the class) | section 0-1 (lines 3-60) | none here; exact value from the published universal-glue paper | I |
| 25 | Comparison constants `sqrt(683/500)`, `sqrt(41/30)`, `sqrt(45/32)`, `sqrt(377/250)`, `sqrt(413/250)`, `sqrt(6466219/3576050)` and their decimals and percentages | sections 0, 8 (lines 3-22, 228-249) | none in the checkers; each decimal recomputed from the exact surds during manuscript preparation (see NOTES.md) | I |
| 26 | `S_cent = C_inf` versus `S_cent > C_inf` is open; no sharp claim is made | sections 0, 8, 9 | none; statement of an open problem | A |

Not claimed anywhere in the paper: that either constant is sharp, that `T_lin` equals a transition temperature or a
measurement, that any material is superconducting, or that the frozen-weight floor is a lower bound on `S_cent`.

## Status of this map

The map was built against the reviewed proof; the manuscript review of 20 November 2026
(`reviews/MANUSCRIPT-REVIEW.md`, ACCEPT-WITH-FIXES) found errors in the manuscript and none in the
proof, the checkers or the pins. Row 20 was widened and row 22 annotated to follow the corrected wording of
the paper. No claim in this table changed status: every row marked C still rests on the same unmodified
checker, every row marked A on the same section of the reviewed proof, and no row was added or removed. The
item by item repair of the manuscript is recorded in `FIXES.md`.
