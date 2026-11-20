# Independent Review: ANISO-SHARP

**Verdict: ACCEPT**

All mathematical derivations in `ANISO-SHARP/RIGOR.md`, the exact rational coverings in `replay.py` and `independent.py`, the 13 inherited source pins in `source-pins.json`, and all 12 guarded mutants executed by `verify.py` are mathematically sound and independently verified. No blocking defects were found. Three minor non-blocking P3 observations (dead-code remnants from the `FINITE-ENERGY` copy, shared exterior/structural scaffold between the two checkers, and an omitted defensive `rem <= 0` guard / `q_full_row1` recheck in `independent.py`) are recorded below.

Reviewed on 2026-11-20. No files inside `ANISO-SHARP/` were modified. `ANISO-SHARP/RESULT.md` was ignored as instructed (stale initial gap statement).

---

## 1. Mathematical and Algorithmic Audit

### 1.1 Reduction from the centered finite-channel class to the covered 2D domain
- **Model and folded form (`RIGOR.md` §§1-2):** Matches the reviewed `FINITE-ENERGY/RIGOR.md` centered class (finite positive weights $\eta_x > 0$, even normalized DOS $\nu_x \in [0, 1]$, reciprocal nonnegative measures $d\mathfrak{m}_{xy} = d\mathfrak{m}_{yx} \ge 0$ supported on $(0, \infty)$ with finite moment norm $\rho = \|M\|_{\ell^2(\eta)} \in (0, \infty)$ and temperature-dependent normal row bound $R(\tau) < \infty$, centered width cone $w_m^{-1} \le s_{m,x}/s_{0,x} \le w_m$). Positive-semidefiniteness of $M$ is not required; using $h = (I - M/R')^{-1}\mathbf{1} > 0$ for $R' > \rho$ and $r = h_x/h_y$ in $B_r + I_{xy}/2 \ge d_* B_r$ gives $Q(v) \ge [1 - 2(1-d_*)\rho/(2\pi\tau)^2]\sum_x \eta_x \|g_x\|^2$ as $R' \downarrow \rho$. **Verified.**
- **Centered Poisson lower envelope (`RIGOR.md` §3):** Both $\sigma \in [1, w_m]$ and $\sigma \in [w_m^{-1}, 1]$ yield $b_m \ge \phi_{w_m}(b_0) = \frac{2}{\pi}\arctan(\frac{1}{w_m}\tan\frac{\pi b_0}{2})$, which is strictly increasing and strictly convex for $w_m > 1$. Supporting tangent slopes $L_{\xi, m} = w_m(1+\xi^2)/(w_m^2+\xi^2)$ and intercepts $C_{\xi, m}$ at $\xi \in \{4, 5, 6, 8, 10, 12, 16, 24\}$ are enclosed downward to denominator $10^8$ using outward rational Machin $\pi$ and Leibniz $\arctan$ bounds (`bm_lo - lam * b0_hi`, floored toward $-\infty$). **Verified.**
- **Disjoint sector decomposition and infinite tail (`RIGOR.md` §4):** The four sectors $(0,0)$, Stage 0 ($0 \leftrightarrow m \ge 1$), Stage 1 ($1 \leftrightarrow k \in \{2,\dots,20\}$), and remaining tail-tail pairs are disjoint. The reflected-tail weighted AM-GM bound retains the required factor of $2$, producing the exact rational infinite-tail upper bounds $q_n$ (using $w_m \ge 43$ and $\sum_{m \ge 21} (n+m+1)^{-2} \le (n+21)^{-1}$) and $q_{\rm full,n} \le q_{\rm full,1} < 33/500$. Stage-1 and Stage-0 completion identities (6)-(7) hold identically via $S_{1k}^2 - p_{1k}^2 = 4p_{1k}/(3w_k)$ and $S_{0m}^2 - p_{0m}^2 = 4p_{0m}/w_m$. For $m > 20$ on $r \in [1/3, 3]$, $(43/3)\alpha_{\rm ext} = (43/3)(77/125) > 2/43$, so all unretained Stage-0 completions are positive and validly discarded. **Verified.**

### 1.2 Completeness of the covering (edges, limits, and exterior tails)
- **Compact domain $[1/3, 3] \times [0, 1/2]$:** `replay.py` partitions $[1, 3] \times [0, 1/2]$ into 159 closed rectangles (max depth 20, exact rational area $1$) and covers $[1/3, 1] \times [0, 1/2]$ by channel-exchange symmetry $r \leftrightarrow r^{-1}$. `independent.py` partitions the full $[1/3, 3] \times [0, 1/2]$ directly into 466 closed rectangles (max depth 11, exact rational area $4/3$) without symmetry reduction, handling negative Stage-0 completions on both sides. The head determinant criterion $2t(1+t)\Phi_X\Phi_Y + r^{-1}\Phi_X + r\Phi_Y \ge 2$ is continuous at $t = 0$, closing rectangles touching $t = 0$. **Verified.**
- **Head-weight partition $[0, 1]$ (43 intervals):** Knots $0, 1/2, 3/4, 160/200, \dots, 200/200$ partition $[0, 1]$ without gaps. Both scripts verify rationally that adjacent tangent intersections are nondecreasing for every $m \in \{1,\dots,20\}$, which guarantees that enumerating adjacent intersections captures every switch of the convex piecewise-affine upper envelope in $u_0 = 1/b_0$. On the first interval $(0, 1/2]$, both scripts verify that all additional lines lie at or below the basic line $b_0/w_m$ at $b_0 = 1/2$; since their slopes exceed $1/w_m$, they stay below $b_0/w_m$ on all of $(0, 1/2]$, so the envelope ratio is constant $1/w_m$ and $A/b_0 + \sum C_m/w_m$ is minimized at $b_0 = 1/2$ (no $b_0 \to 0^+$ limit is missed). **Verified.**
- **Exterior regions (`RIGOR.md` §6):** With $\alpha_{\rm ext} = 1 - 159/500 - 33/500 = 77/125 = 0.616$:
  - $r \le 1/4$ or $r \ge 4$: $9/17 - (7/75)/\alpha_{\rm ext} = 212/561 \approx 0.377897 > 159/500 = 0.318$, with $\sum_{m=1}^{20} [(2m+1)m^2(m+1)^2]^{-1} + 1/(8\cdot 20^4) \approx 0.090355 < 7/75$.
  - $1/4 \le r \le 1/3$ or $3 \le r \le 4$: $\alpha_{\rm ext}/8 = 77/1000 > 1/25$ (all $m \ge 2$ positive) and $2/5 + (3/4)(\alpha_{\rm ext}/8 - 1/9)/\alpha_{\rm ext} = 13249/36960 \approx 0.358469 > 159/500$.
  - $t \ge 1/2$ and $r \in [1/3, 3]$: $p_{01}(t) \le 4/9$ and $1/3 + (4/9)(\alpha_{\rm ext}/6 - 1/9)/\alpha_{\rm ext} = 2041/6237 \approx 0.327241 > 159/500$.
  Together with $[1/3, 3] \times [0, 1/2]$, these exhaust all $r > 0, t > 0$. **Verified.**

### 1.3 Exactness of arithmetic and rounding directions
- No floating-point arithmetic enters `replay.py` or `independent.py`; all quantities use exact `fractions.Fraction` and Python arbitrary-precision integers scaled by $Q = 10^{12}$ (and $Q_c = 10^8$ for tangent intercepts).
- Every rounding direction in `box_ok_int` and `cell_ok_full` was audited line by line:
  - Reserve `dt` and Hankel costs `q_red` are rounded upward (`ceil`); remaining budgets `one_m_dt`, `rem`, `alp_0`, `bet_1` are rounded downward (`floor`).
  - For positive completion numerators, monotonicity in $r$, $p$, and $A_m$ (or $\beta_k$) holds; lower bounds are used for $r, p, A_m, \beta_k$ and upper bounds for $r^{-1}$ in the denominator, followed by floor division.
  - For negative Stage-0 completion numerators (`num < 0`), dropping the positive $+2r p_{0m}$ denominator term, using `p_0k_hi` (at $t_{\rm lo}$), Python floor division toward $-\infty$, and multiplying by the upper Harnack bound $w_m \ge b_m/b_0$ all round strictly downward (more negative).
  - The supporting tangent inequality for $r^{-1} P_X + r P_Y$ at $r_0 = (r_{\rm lo}+r_{\rm hi})/2$ and the $t_{\rm lo}$ product term are evaluated in exact `Fraction` arithmetic.
- High-precision independent check (60-digit `Decimal` Machin $\pi$):
  - $C_* = \sqrt{341/250}/(2\pi) = 0.185877711471916879909440447679\ldots \in (0.185877711471916, 0.185877711471917)$.
  - $C_{\rm rep} = \sqrt{6821/5000}/(2\pi) = 0.185891338370617195766211508817\ldots \in (0.185891338370617, 0.185891338370618)$.
  **Verified.**

### 1.4 Relationship to previous `C_cent` proof and strict vs non-strict constants
- `FINITE-ENERGY` certified $d_{\rm cent,*} = 317/1000$, yielding closed supremum bound $C_{\rm cent,*} = \sqrt{683/500}/(2\pi) \approx 0.186013935536718$ and strict reported bound $C_{\rm cent} = \sqrt{41/30}/(2\pi) \approx 0.186059321394545$.
- `ANISO-SHARP` certifies $d_* = 159/500 = 0.318 > 317/1000$, yielding closed supremum bound $C_* = \sqrt{341/250}/(2\pi) \approx 0.185877711471917$ and strict reported bound $C_{\rm rep} = \sqrt{6821/5000}/(2\pi) \approx 0.185891338370617$ ($d_{\rm rep} = 3179/10000$, bare gap $1/6821$ at $\tau = C_{\rm rep}\sqrt{\rho}$).
- Both new constants strictly improve both previous constants ($C_* < C_{\rm rep} < C_{\rm cent,*} < C_{\rm cent}$) and remain consistent with the reviewed `SHARP` centered frozen-weight edge-method floor $0.185411$ ($d_* < 0.321407$). The distinction between the closed supremum inequality $S_{\rm cent} \le C_*$ (using finite $R(\tau)$ at every $\tau > C_*\sqrt{\rho}$ without assuming onset monotonicity) and the strict reported bound $k_B T_{\rm lin} < C_{\rm rep}\sqrt{\rho}$ is logically sound. **Verified.**

### 1.5 Independence of the second implementation
- `independent.py` does not import `replay.py`; it uses different Machin/Leibniz series lengths ((12, 8) vs (14, 6) for $\pi$; 14/16 vs 12 for $\arctan$), covers the full unsymmetrized domain $[1/3, 3] \times [0, 1/2]$ via 4-way quadtree subdivision (466 leaves, area $4/3$) with two-sided negative-completion handling instead of binary subdivision on $[1, 3] \times [0, 1/2]$ (159 leaves, area $1$), and explicitly checks the Stage-0 and Stage-1 completion rationalization identities and tangent crossings separately.
- However, both implementations share the same underlying two-stage cascade decomposition ($M=20$, split $7/10$, $Q=10^{12}$, same 8 tangent points and 43 head intervals) and copy the same exterior-check block verbatim (`replay.py:274-301` vs `independent.py:269-297`). This is transparently stated in `RIGOR.md` §0 and `source-pins.json`, and meets the campaign's two-implementation standard.

---

## 2. Numbered Findings (all non-blocking)

1. **P3 (dead code) -- Unused 9-interval `sub_ivs` definitions retained from `FINITE-ENERGY` (`replay.py:109-120`, `independent.py:111-121`):** Both scripts define the legacy 9-interval `sub_ivs` list near the top and then immediately overwrite `sub_ivs` with the new 43-interval partition (`replay.py:277`, `independent.py:271`) before any function reads it. No correctness impact, but deleting the shadowed 9-interval definitions removes dead weight.
2. **P3 (defensive check) -- `independent.py` omits `rem <= 0` guard and `q_full_row1 < 33/500` assertion:** `replay.py:185-186` checks `if any(r_val <= 0 for r_val in rem): return False` inside `box_ok_int` and checks `q_full_row1 < Fraction(33, 500)` at lines 103-105; `independent.py` omits both (relying on `min(rem) > 0.64 Q` for `d_cert = 159/500` and the inherited `33/500` cap). Adding both checks in `independent.py` would make it fully self-contained on the Hankel tail cap.
3. **P3 (transparency) -- Verbatim shared exterior-check block:** Lines 274-301 of `replay.py` and lines 269-297 of `independent.py` are nearly identical copies for the exterior analytic checks and decimal enclosures. No soundness issue since every displayed rational inequality was independently verified in exact arithmetic, but worth noting in the independence boundary.

---

## 3. Verification and Adversarial Search

### 3.1 Replay and mutant verification (`verify.py`)
Executed `python -B replay/verify.py` (wall time 141.21 s, **exit code 0**):

| Command | Exit | Expected | Time (s) | Observed Result |
|---|---:|---:|---:|---|
| `replay.py` | 0 | 0 | 19.859 | `CERTIFIED primary centered cover: reserve=159/500; leaves=159; max_depth=20; area=1; head_intervals=43` |
| `replay.py --mutant pin` | 1 | 1 | 0.078 | `REJECT: inherited proof bytes ../FINITE-ENERGY/RIGOR.md` |
| `replay.py --mutant strict-budget` | 1 | 1 | 0.063 | `REJECT: strict reporting margin` |
| `replay.py --mutant coverage-gap` | 1 | 1 | 19.500 | `REJECT: complete residual area, no coverage gaps` |
| `replay.py --mutant reserve-too-high` | 1 | 1 | 6.890 | `REJECT: compact rectangle subdivision depth` |
| `replay.py --mutant hankel-tail` | 1 | 1 | 0.063 | `REJECT: reduced Hankel row-1 bound` |
| `replay.py --mutant centered-cone` | 1 | 1 | 0.062 | `REJECT: admissible lower tangent line` |
| `independent.py` | 0 | 0 | 40.985 | `CERTIFIED independent centered cover: reserve=159/500; leaves=466; max_depth=11; area=4/3; head_intervals=43` |
| `independent.py --mutant pin` | 1 | 1 | 0.062 | `REJECT: inherited proof bytes ../FINITE-ENERGY/RIGOR.md` |
| `independent.py --mutant strict-budget` | 1 | 1 | 0.047 | `REJECT: strict reporting margin` |
| `independent.py --mutant coverage-gap` | 1 | 1 | 32.188 | `REJECT: independent full residual area` |
| `independent.py --mutant reserve-too-high` | 1 | 1 | 21.031 | `REJECT: independent full-domain quadtree depth` |
| `independent.py --mutant completion-sign` | 1 | 1 | 0.125 | `REJECT: independent stage-0 completion rationalization` |
| `independent.py --mutant tangent-intercept` | 1 | 1 | 0.141 | `REJECT: certified tangent intercept nonpositive` |

Final line: `PASS: two independent exact coverings and all twelve mutants rejected (each mutant exit 1).`

### 3.2 Independent exact-arithmetic and pin checks
- All 13 SHA-256 entries in `source-pins.json` verified against the live inherited files (**exit 0**).
- Exact rational exterior bounds and 60-digit `Decimal` enclosures of $C_*$, $C_{\rm rep}$, $C_{\rm cent,*}$, and $C_{\rm cent}$ verified (**exit 0**).

### 3.3 Adversarial float search (attempt to break the bound)
- Ran an independent `numpy`/`scipy` search (`UV_OFFLINE=1`, **exit 0**) over 700 random 2- and 3-channel centered models (bipartite non-PSD $M$, unequal $\eta \in [10^{-2}, 10^2]$, 1-2 Einstein modes, box, flat+box, notched, outer-ray, and two-shell even DOS profiles) plus 12-start Nelder-Mead optimization at $\tau = C_\infty\sqrt{\rho}$ and $\tau = C_*\sqrt{\rho}$.
- At ultra-soft energies ($E \sim 10^{-3}$), finite-$N$ ($N=35$) truncation produced the expected $1 \pm 10^{-7}$ soft-limit artifact that dropped below $1$ at $N=80$ (`lam(C_inf) = 0.99999995`, `lam(C_star) = 0.99998692`).
- Across 300 finite-energy ($E \in [0.05, 5.0]$) 2- and 3-channel models evaluated at $N=50$ and re-evaluated at $N=100$, the maximum pairing gain was `0.99998242` at $C_\infty$ and `0.99982546` at $C_*$. No counterexample exceeding $C_*$ (or $C_\infty$) was found. (As noted in `RIGOR.md` §8, this float search is exploratory only and does not prove $S_{\rm cent} = C_\infty$.)

### 3.4 Reviewed file hashes (`ANISO-SHARP/`)

| File | Bytes | SHA-256 |
|---|---:|---|
| `RIGOR.md` | 19402 | `c4762485b482beb1a44c95111ab3858f1abca8a5c36f5ffda265b2163afc59df` |
| `CHECKS.txt` | 5031 | `291a17400173a393a8a0571cd29558dbc562115bb57a024e4202a94fa9a4b7bb` |
| `replay.py` | 14881 | `531a068b15989977aa375cf29ca6d52c026a90d1e8d067e3dac4059db9c02a67` |
| `independent.py` | 14899 | `73050fecade9d4016992c5d60ed04055df98eb5fa1fb4aa1c40d0e5ec256b1d8` |
| `verify.py` | 1415 | `6adac179a9918db8fddf61ab40764469c99fa24b1adcf76246ab99f46496e23b` |
| `source-pins.json` | 1453 | `285ae3b56596f476e355368321f28989f937a3d8bc982142e2c913b1a22d9742` |

**Checks intentionally not run:** Re-verification of inherited `FINITE-ENERGY`, `SHARP`, `SHARPFLAT4`, and `SOFT-LIMIT` scripts (already reviewed and pinned by SHA-256); `ANISO-SHARP/RESULT.md` (explicitly excluded as stale).
