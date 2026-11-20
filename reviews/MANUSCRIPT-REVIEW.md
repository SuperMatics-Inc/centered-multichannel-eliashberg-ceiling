# Independent Preprint Review: ANISO-SHARP-PAPER

**Verdict: ACCEPT-WITH-FIXES**

The underlying mathematics, exact rational certificates (`replay.py` and `independent.py`), Zenodo DOI targets, disclosure/convention requirements, and clean Tectonic build all pass. However, two proof-text defects in `main.tex` (a reversed inequality in the far-imbalance exterior case and a $\tau \ge C_*\sqrt{\rho}$ vs $\tau > C_*\sqrt{\rho}$ positive-definite/semidefinite slip in the proof of Theorem 1) and three factual/citation accuracy issues (Table 1 caption claiming truncation when values are rounded, channel-weight letter swap $b_m/b_0$ vs $c_m/c_0$ in Stage 0, and a missing word in one Zenodo citation title) should be fixed before public release.

No files inside `ANISO-SHARP-PAPER/` or `ANISO-SHARP/` were modified during this review.

---

## Numbered Findings

1. **P1 (blocks release) -- Proof of Theorem 1 uses $\tau \ge C_*\sqrt{\rho}$ and positive semidefiniteness instead of $\tau > C_*\sqrt{\rho}$ and strict positive definiteness (`main.tex:181`):**
   Line 124 defines $T_{\mathrm{lin}}$ as the supremum of temperatures at which $Q$ fails to be *positive definite*, but line 181 supposes $\tau \ge C_*\sqrt{\rho}$, obtains only $Q(v) \ge 0$ (positive *semidefinite*), and concludes $\tau_{\mathrm{lin}} \le C_*\sqrt{\rho}$ (also introducing $\tau_{\mathrm{lin}}$ without defining it). Positive semidefiniteness at $\tau = C_*\sqrt{\rho}$ does not rule out a zero mode. `RIGOR.md` §7 avoids this cleanly by taking strict $\tau > C_*\sqrt{\rho}$, where the bracket in \eqref{eq:gap} is strictly positive so $Q$ is strictly positive definite (bounded below by a positive multiple of the normal norm) at every $\tau > C_*\sqrt{\rho}$, immediately implying $k_{\mathrm B}T_{\mathrm{lin}} \le C_*\sqrt{\rho}$.
   **Fix (`main.tex:181`):** Replace `Now suppose $\tau\ge\Cstar\sqrt\rho$, that is $(2\pi\tau)^2\ge2(1-\dstar)\rho$. Then \eqref{eq:gap} gives $Q(v)\ge0$ for every $v$, and $Q$ is a continuous quadratic form that is nonnegative everywhere, so its symmetrised operator is positive semidefinite. ... A positive semidefinite form therefore cannot carry a negative direction of the actual pairing equation at $\tau$, and $\tau_{\mathrm{lin}}\le\Cstar\sqrt\rho$.` with strict $\tau > \Cstar\sqrt\rho$, giving a strictly positive bare gap $1 - 2(1-\dstar)\rho/(2\pi\tau)^2 > 0$, hence a strictly positive-definite stability operator bounded below by $[1 - 2(1-\dstar)\rho/(2\pi\tau)^2]/(1+R(\tau)) > 0$, which yields $\kB\Tlin \le \Cstar\sqrt\rho$.

2. **P1 (blocks release) -- Reversed inequality in the far-imbalance exterior case (`main.tex:377`):**
   For $r \le 1/4$, line 377 writes `Here the first estimate in \eqref{eq:headest} is at least $9/17$, since $r+r^{-1}\le17/4$`. The inequality is reversed: for $r \in (0, 1/4]$, $r + r^{-1} \ge 17/4$, which gives $1 - 2/(r+r^{-1}) \ge 1 - 8/17 = 9/17$.
   **Fix (`main.tex:377`):** Change `$r+r^{-1}\le17/4$` to `$r+r^{-1}\ge17/4$`.

3. **P2 (should fix) -- Table 1 caption falsely states decimals are truncated (`main.tex:447`):**
   The caption of Table 1 states `The decimals are truncated, not rounded`, but all nine 10-digit decimals in Table 1 (`main.tex:436-444`) are *rounded* to 10 decimal places, not truncated. Six of the nine entries differ from their truncated values: $C_\infty = 0.18272624777\ldots$ (printed `0.1827262478`), $C_* = 0.18587771147\ldots$ (printed `0.1858777115`), $C_{\mathrm{rep}} = 0.18589133837\ldots$ (printed `0.1858913384`), $C_{\mathrm{cent}} = 0.18605932139\ldots$ (printed `0.1860593214`), $C_{\mathrm{caus}} = 0.18873454539\ldots$ (printed `0.1887345454`), and $C_{21} = 0.19544330695\ldots$ (printed `0.1954433070`).
   **Fix (`main.tex:447`):** Replace `The decimals are truncated, not rounded,` with `The decimals are rounded to ten places,` (the exact rational enclosures remain in Theorem 1).

4. **P2 (should fix) -- Swapped channel-weight ratio in Stage-0 negative-numerator bound (`main.tex:311`):**
   Lines 306-310 complete the square in $z_m$ against $a_0$, leaving $c_m D_{0m}$ in $a_0^2$, which enters $\Phi_X$ as $(c_m/c_0) D_{0m}^X$ (line 324). Line 311 then states `multiplying by the upper Harnack ratio $b_m/b_0\le w_m$`, which uses the opposite channel's weights (`b` instead of `c`).
   **Fix (`main.tex:311`):** Change `$b_m/b_0\le w_m$` to `$c_m/c_0\le w_m$` (or note `$c_m/c_0\le w_m$`, and `$b_m/b_0\le w_m$` on the mirror side).

5. **P2 (should fix) -- Citation title for `finite` omits leading word `Sharp` (`refs.bib:3`):**
   The Zenodo API for `10.5281/zenodo.24364879` gives the published title `Sharp Eliashberg pairing bounds for an energy-dependent density of states`, whereas `refs.bib:3` has `title = {{Eliashberg} pairing bounds for an energy-dependent density of states}`.
   **Fix (`refs.bib:3`):** Change to `title = {Sharp {Eliashberg} pairing bounds for an energy-dependent density of states}`.

6. **P3 (nit) -- Imprecise wording for the $C_{21}$ excess-removal percentages (`main.tex:454`):**
   Line 454 writes `the figure moves from $73.79\%$ for the pair of~\cite{finiteenergy} to $75.11\%$ here.` Those two percentages correspond specifically to the *strict* constants ($C_{\mathrm{cent}}$ removes $73.79\%$ and $C_{\mathrm{rep}}$ removes $75.11\%$; the supremum constants remove $74.15\%$ and $75.22\%$, respectively).
   **Fix (`main.tex:454`):** Replace `for the pair of~\cite{finiteenergy} to $75.11\%$ here` with `for the strict constant of~\cite{finiteenergy} to $75.11\%$ for $\Crep$ here`.

7. **P3 (nit) -- Preposition in Stage-1 boost sentence (`main.tex:300`):**
   Line 300 writes `is thereby boosted by $\alpha_{0,1}^{\rm eff}=\alpha_{0,1}+\sum_{k=2}^{M}c_kD_{1k}$`, where the equation gives the boosted total rather than the increment.
   **Fix (`main.tex:300`):** Change `boosted by` to `boosted to`.

8. **P3 (nit) -- Unused BibTeX entry `dolgov` (`refs.bib:29-36`):**
   `@article{dolgov, ...}` is never cited in `main.tex` (so BibTeX omits it from the PDF). Also `NOTES.md:4` states `refs.bib: 6 entries` when there are 5 entries.
   **Fix (`refs.bib:29-36`):** Either cite `\cite{dolgov}` in Section 1 when introducing multiband Eliashberg models or remove the unused entry from `refs.bib`.

---

## Checklist Summary

### 1. Faithfulness to `RIGOR.md` and `FINITE-ENERGY`
- **Class hypotheses:** Exact match to `FINITE-ENERGY` and `ANISO-SHARP/RIGOR.md` (finite channel space with $\eta_x > 0$, even measurable DOS $0 \le N_x(\xi) \le \eta_x$, energy-independent radial vertices, reciprocal nonnegative measures $d\mathfrak m_{xy} = d\mathfrak m_{yx} \ge 0$ on $(0,\infty)$, finite moment norm $\rho = \|\mathcal M\|_{\ell^2(\eta)} \in (0,\infty)$, $\mathcal M$ not required PSD, finite zero-transfer mass and finite normal row bound $R(\tau) < \infty$ at each tested $\tau$, odd-folded nonnegative normal excess, dominated attractive pairing envelope, PSD static pairing subtraction, actual positive reflected normal branch, centered width cone $w_m^{-1} \le s_{m,x}/s_{0,x} \le w_m$).
- **Proof steps:** Every step of `RIGOR.md` §§1-7 is present and accurate apart from Findings 1, 2, and 4 above.
- **No overstatement:** Bound is explicitly on linear Migdal-Eliashberg $T_{\mathrm{lin}}$ and not $T_c$ or a measurement (Abstract, §§1, 2.2, 7.2, Disclosure). Method floor `0.185411` is explicitly stated as a floor of the frozen-weight edge-reserve method and NOT a lower bound on $S_{\mathrm{cent}}$ (Abstract, §§1, 7.1). $S_{\mathrm{cent}} = C_\infty$ vs $S_{\mathrm{cent}} > C_\infty$ is explicitly stated as open (Abstract, §1, Remark 2, §7.3).

### 2. Numbers, Constants, and Certificate Replay
- Recomputed all constants, exact rational identities, enclosures, exterior bounds, and percentages in Python using exact `Fraction` and 60-digit `Decimal` Machin $\pi$:
  - $2(1 - 159/500) = 341/250$, $2(1 - 3179/10000) = 6821/5000$, bare gap $1 - (1-d_*)/(1-d_{\mathrm{rep}}) = 1/6821$.
  - $C_* = 0.185877711471916880\ldots \in (0.185877711471916, 0.185877711471917)$ ($1.7247\%$ above $C_\infty$, printed $1.725\%$).
  - $C_{\mathrm{rep}} = 0.185891338370617196\ldots \in (0.185891338370617, 0.185891338370618)$ ($1.7321\%$ above $C_\infty$, printed $1.732\%$).
  - All comparison constants ($\sqrt{683/500}/(2\pi)$, $C_{\mathrm{cent}}$, $C_{\mathrm{caus}}$, $C_{21}$, $C_1$, $U$), their 10-digit rounded values (see Finding 3), and their relative excesses over $C_\infty$ match.
  - $q_1 = 973/25542$, $\mathrm{rem}_1 = 4111661/6385500 \approx 0.643906$, $\min_{2\le k\le 20}\beta_{1,k} = 0.198451 > 0.1984$, $q_{\mathrm{full},16} \approx 0.065514 < 33/500$, $\alpha_{\mathrm{ext}} = 77/125 = 0.616$, $(43/3)\alpha_{\mathrm{ext}} > 2/43$.
  - Exterior tail sum $0.090355028\ldots < 7/75$; exterior reserves $212/561 \approx 0.377897$, $13249/36960 \approx 0.358469$, $2041/6237 \approx 0.327241$, all $> 159/500$.
  - Floor metrics: $\sqrt{1.357186}/(2\pi) \approx 0.18541284 > 0.185411$, $1 - 1.357186/2 = 0.321407$, $C_*$ above floor by $0.2517\%$ (printed $0.25\%$), floor fraction of $[C_\infty, C_*]$ is $0.8519$ (printed $0.852$).
- Reran `replay.py` (exit 0, 159 leaves, max_depth 20, area 1, 43 head intervals) and `independent.py` (exit 0, 466 leaves, max_depth 11, area 4/3, 43 head intervals) once each; both printed the exact rational enclosures matching Theorem 1.

### 3. Citations and DOIs (Zenodo API)
All 8 Zenodo DOIs in `refs.bib` returned HTTP 200 from `https://zenodo.org/api/records/<id>` with creator `Rens, Davis`:
- `10.5281/zenodo.24364879`: *Sharp Eliashberg pairing bounds for an energy-dependent density of states* (publication; see Finding 5)
- `10.5281/zenodo.24364881`: *Supplement to Sharp Eliashberg pairing bounds for an energy-dependent density of states* (software)
- `10.5281/zenodo.24372930`: *What a glue moment bounds in linear Eliashberg theory* (publication)
- `10.5281/zenodo.24372929`: *Replay supplement for What a glue moment bounds in linear Eliashberg theory* (software)
- `10.5281/zenodo.24374032`: *A √(377/250)/(2π) moment-norm ceiling for causal multichannel Eliashberg branches* (publication)
- `10.5281/zenodo.24374034`: *Replay supplement for A √(377/250)/(2π) moment-norm ceiling for causal multichannel Eliashberg branches* (software)
- `10.5281/zenodo.24380829`: *Moment-norm ceilings √(41/30)/(2π) and √(45/32)/(2π) for multichannel Eliashberg branches* (publication)
- `10.5281/zenodo.24380827`: *Replay supplement for Moment-norm ceilings √(41/30)/(2π) and √(45/32)/(2π) for multichannel Eliashberg branches* (software)

### 4. Conventions
- **Em dashes:** 0 in `main.tex`, 0 in `refs.bib`, 0 in extracted 12-page `main.pdf` text (both U+2014 and `---`).
- **Byline:** `Davis Rens`, `SuperMatics Inc.`, `ORCID 0000-0001-5839-5197` present in source and PDF.
- **Disclosures:** `This preprint has not been peer reviewed.` and the AI generation/review disclosure are present in Section `Supporting material and disclosure`.
- **Internal names / paths:** None appear in the PDF text (no `ANISO-SHARP`, `FINITE-ENERGY`, `OPTIMUM`, `SHARP`, `G3COMBINE`, `UNIV-GLUE`, `SOFT-LIMIT`, `SHARPFLAT`, machine names, or workspace paths).
- **DOI placeholders:** `DOI-PAPER` and `DOI-SUPP` appear only in the preamble macros `\PAPERDOI` (`main.tex:23`) and `\SUPPLEMENTDOI` (`main.tex:24`), invoked via `\DOI{\SUPPLEMENTDOI}` and `\DOI{\PAPERDOI}` at `main.tex:492`.

### 5. Clean Tectonic Rebuild
- Copied `main.tex` and `refs.bib` to `<build>`, built with `tectonic -X compile --keep-logs --outdir out main.tex`: **exit 0**, 12 pages, 168,043 bytes (matching `ANISO-SHARP-PAPER/main.pdf`), 0 Overfull/Underfull warnings, 0 undefined references/citations, 0 BibTeX errors/warnings.
- Deleted `<build>` via `cmd /c rmdir /s /q <build>` and verified absence.

### 6. Readability and Journal-Worthiness
- **Readability:** Very good for a mathematical-physics audience. The exposition is clear, disciplined, and self-contained, with clean separation between analytic proofs and the finite rational certificate, explicit discussion of limitations, and an honest statement of the open problem.
- **Journal-worthiness:** **Preprint-only** as a standalone paper (not ready on its own for *Lett. Math. Phys.* or *J. Math. Phys.*). The improvement over the immediately preceding preprint \cite{finiteenergy} is an incremental tightening of a single constant ($1.824\% \to 1.732\%$ above $C_\infty$, a $0.09\%$ gain) obtained by raising the reserve from $317/1000$ to $159/500$ and refining the head-weight partition and tangent-envelope minimization within the same two-stage edge-reserve framework, while leaving the causal constant unchanged and the central question ($S_{\mathrm{cent}} = C_\infty$ vs $S_{\mathrm{cent}} > C_\infty$) open. For journal publication in *LMP* or *JMP*, this result should either be folded into a unified manuscript presenting the full multichannel moment-norm framework or await a resolution of $S_{\mathrm{cent}} = C_\infty$. As a Zenodo preprint documenting the near-exhaustion of the edge-reserve method ($0.25\%$ above its $0.185411$ floor), it is well-scoped and appropriate once Findings 1-5 are fixed.

---

## Commands Run and Exit Codes

| Command | Exit Code | Notes |
|---|---:|---|
| `python -B replay.py` (in `ANISO-SHARP`) | 0 | 51.39 s; `CERTIFIED primary centered cover: reserve=159/500; leaves=159; max_depth=20; area=1; head_intervals=43` |
| `python -B independent.py` (in `ANISO-SHARP`) | 0 | 100.33 s; `CERTIFIED independent centered cover: reserve=159/500; leaves=466; max_depth=11; area=4/3; head_intervals=43` |
| `curl -sS https://zenodo.org/api/records/<id>` (8 DOIs) | 0 | All 8 returned HTTP 200; title mismatch on `24364879` (Finding 5) |
| `mkdir -p <build>/out && tectonic -X compile --keep-logs --outdir out main.tex` | 0 | 12 pages, 168,043 bytes, 0 warnings/errors (initial call without `out/` dir exited 1) |
| `powershell -NoProfile -Command "cmd /c rmdir /s /q <build>" && test ! -e <build>` | 0 | `CLEANUP_OK` |
| Python audit of `main.tex`, `refs.bib`, `main.pdf` (PyMuPDF) | 0 | 12 pages, 0 em dashes, all conventions checked |
| Python exact `Fraction` + 60-digit `Decimal` recomputation | 0 | All numbers verified; Table 1 rounding vs truncation mismatch found (Finding 3) |
