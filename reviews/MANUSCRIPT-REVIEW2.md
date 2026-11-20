# Delta Review: ANISO-SHARP-PAPER (Post-Fix)

**Verdict: PASS**

All eight findings from `REVIEW.md` and the two self-identified strictness-logic issues (`E1`, `E2` in `FIXES.md`) are cleanly fixed in `main.tex` and `refs.bib`, with no new defects introduced into the manuscript or PDF. `REVIEW.md` and all files in `ANISO-SHARP-PAPER/` were left untouched.

---

## 1. Diff Audit (`prefix1/` vs current)

- **Finding 1 (P1, `main.tex:181-185`) -- Verified:** The proof of Theorem 1 now fixes strict $\tau > C_*\sqrt{\rho}$, defines $\beta(\tau) = 1 - 2(1-d_*)\rho/(2\pi\tau)^2 > 0$, lets $R' \downarrow \rho$ in (8) to obtain $Q(v) \ge \beta(\tau)\sum_x \eta_x\|g_x\|^2$, and uses $s_{n,x} \le w_n + R(\tau) \le (1+R(\tau))w_n$ (valid since $w_n = 2n+1 \ge 1$ and every normal-kernel frequency row is bounded by $R(\tau) < \infty$) to conclude
  $$Q(v) \ge \frac{\beta(\tau)}{1+R(\tau)} \sum_x \eta_x \|(s_x b_x)^{1/2} v_x\|^2.$$
  Because $\beta(\tau) > 0$ and $1 + R(\tau) \in [1, \infty)$, strict positive definiteness (coercivity in the pairing Hilbert norm) genuinely follows at every $\tau > C_*\sqrt{\rho}$. Thus no $\tau > C_*\sqrt{\rho}$ is a failure temperature, giving $k_{\mathrm B}T_{\mathrm{lin}} \le C_*\sqrt{\rho}$ (including disconnected instability sets). The undefined symbol $\tau_{\mathrm{lin}}$ is gone.
- **Extra fixes E1 & E2 (strictness paragraph `main.tex:187-192`, remark `main.tex:144-148`, Section 7.2 `main.tex:478`) -- Verified:** The strictness paragraph computes the bare gap $1/6821 > 0$ and positive operator lower bound $[6821(1+R(\tau))]^{-1} > 0$ at $\tau \ge C_{\mathrm{rep}}\sqrt{\rho}$, showing that temperature is itself stable, and derives $k_{\mathrm B}T_{\mathrm{lin}} < C_{\mathrm{rep}}\sqrt{\rho}$ directly from $k_{\mathrm B}T_{\mathrm{lin}} \le C_*\sqrt{\rho}$ together with $C_* < C_{\mathrm{rep}}$. The post-theorem remark and Section 7.2 fourth point were reworded consistently so all three places agree with `RIGOR.md` §7.
- **Theorem 1 display (`main.tex:130-131`) -- Verified:** Reads $S_{\mathrm{cent}} := \sup \frac{k_{\mathrm B}T_{\mathrm{lin}}}{\sqrt{\rho}} \le C_* = \frac{\sqrt{341/250}}{2\pi}$ (explicitly a ratio).
- **Finding 2 (P1, `main.tex:381`) -- Verified:** Reversed inequality fixed from `$r+r^{-1}\le17/4$` to `$r+r^{-1}\ge17/4$`.
- **Finding 3 (P2, `main.tex:451`) -- Verified:** Table 1 caption changed from `The decimals are truncated, not rounded` to `The decimals are rounded to ten places`.
- **Finding 4 (P2, `main.tex:315`) -- Verified:** Channel-weight ratio fixed to `$c_m/c_0\le w_m$, with $b_m/b_0\le w_m$ on the mirror side`.
- **Finding 5 (P2, `refs.bib:3`) -- Verified:** Restored leading word `Sharp`: `title = {Sharp {Eliashberg} pairing bounds for an energy-dependent density of states}` (matches Zenodo record `10.5281/zenodo.24364879`).
- **Finding 6 (P3, `main.tex:458`) -- Verified:** Clarified to `from $73.79\%$ for the strict constant of~\cite{finiteenergy} to $75.11\%$ for $\Crep$ here`.
- **Finding 7 (P3, `main.tex:304`) -- Verified:** `boosted by` changed to `boosted to`.
- **Finding 8 (P3, `refs.bib`) -- Verified:** Unused `dolgov` entry removed; all 4 entries in `refs.bib` are cited in `main.tex` (0 uncited, 0 missing).
- **Non-PDF metadata note (harmless):** `NOTES.md:4` (and `FIXES.md` row 8) says `refs.bib: 5 entries`, whereas `refs.bib` now has 4 entries after removing `dolgov`. Does not affect `main.tex`, `refs.bib`, or `main.pdf`.

---

## 2. Clean Rebuild and Purity Scans

- **Clean Tectonic rebuild in `<build>`:** Copied `main.tex` and `refs.bib` only; compiled with `tectonic -X compile --keep-logs --outdir out main.tex`. Exit 0, 12 pages, 168,611 bytes (matching `ANISO-SHARP-PAPER/main.pdf`), 0 `Overfull`/`Underfull`/warning/error/undefined messages in `out/main.log`, clean `out/main.blg`. Deleted `<build>` via `cmd /c rmdir /s /q <build>` and verified absence (`CLEANUP2_OK`).
- **Purity scans (`main.tex`, `refs.bib`, 12-page `main.pdf` via PyMuPDF):**
  - Em dashes (`U+2014` and `---`): 0 in source, 0 in PDF.
  - Byline/ORCID (`Davis Rens`, `SuperMatics Inc.`, `0000-0001-5839-5197`), `This preprint has not been peer reviewed`, and AI disclosure: all present.
  - Internal lane names, machine names, workspace paths, and review/fix filenames (`prefix1`, `FIXES.md`, `REVIEW.md`): 0 in PDF (the single `\bSHARP\b` match is the legitimate published paper title `[2] Davis Rens. Sharp Eliashberg pairing bounds...`).
  - DOI placeholders (`DOI-PAPER`, `DOI-SUPP`): appear only in preamble macros `\PAPERDOI` (`main.tex:23`) and `\SUPPLEMENTDOI` (`main.tex:24`), invoked at `main.tex:496`.

---

## 3. Commands and Exit Codes

| Command | Exit Code | Notes |
|---|---:|---|
| `diff -u prefix1/main.tex main.tex` & `diff -u prefix1/refs.bib refs.bib` | 0 | Verified all 8 findings + E1/E2; no unintended edits |
| `mkdir -p <build>/out && tectonic -X compile --keep-logs --outdir out main.tex` | 0 | 12 pages, 168,611 bytes, 0 log warnings/errors |
| `powershell -NoProfile -Command "cmd /c rmdir /s /q <build>" && test ! -e <build>` | 0 | `CLEANUP2_OK` |
| Python + PyMuPDF purity & citation scan (`main.tex`, `refs.bib`, `main.pdf`) | 0 | 0 em dashes, 4/4 citations matched, 0 internal leaks |
