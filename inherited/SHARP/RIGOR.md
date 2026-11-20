# SHARP: the sharp finite-energy multichannel supremum, and why the edge-reserve route cannot reach it

Labels: **PROVED** (complete argument here or in a cited artifact), **CERTIFIED** (outward-rounded Arb or exact rational computation in `replay.py`), **NUMERICAL** (floating-point evidence, no enclosure), **[INFERENCE]** (reasoned, not formalized), **OPEN**.

Status of inputs. FINITE-ENERGY (`../FINITE-ENERGY/`) is being repaired by another agent; every statement below that uses its constants is conditional on that lane's final status. Nothing below depends on FINITE-ENERGY being correct except the upper ends of the brackets and the "consistency" checks. The obstruction (Theorem 1) does not depend on it.

## 0. Verdict

- **OPEN.** The sharp suprema $S_{\rm cent} = \sup_{\mathcal C_{\rm cent}} k_BT_{\rm lin}/\sqrt\rho$ and $S_{\rm caus} = \sup_{\mathcal C_{\rm caus}} k_BT_{\rm lin}/\sqrt\rho$ are not determined. The best brackets are unchanged:
  $S_{\rm cent}\in[C_\infty, C_{\rm cent}] = [0.1827262477723295,\ 0.1860593213945454]$ and $S_{\rm caus}\in[C_\infty, C_{\rm caus}] = [0.1827262477723295,\ 0.1887345453918264]$.
  - The lower end is **PROVED** by inheritance. The single-channel ($d=1$) branches lie in both classes, and the common-soft limit (`../SOFT-LIMIT/`, PASS) approaches $C_\infty$ for $d=1$, so $S\ge C_\infty$. For $d=1$ the value is never attained (scalar finite-band proof, Zenodo 24364879, cited by `../FINITE-ENERGY/RIGOR.md` line 21).
  - The upper ends are FINITE-ENERGY's claimed constants. They are **PROVED there, conditional on the repair** of that lane.
- **PROVED + CERTIFIED (Theorem 1, new): edge-route obstruction.** No argument that passes through the FINITE-ENERGY edge-reserve inequality `eq:edge_reserve` can prove a constant below
  - $0.185411$ on $\mathcal C_{\rm cent}$, and on $\mathcal C_{\rm caus}$, since $\mathcal C_{\rm cent}\subset\mathcal C_{\rm caus}$;
  - $0.188201$ on the four-inequality Harnack relaxation that FINITE-ENERGY uses for $\mathcal C_{\rm caus}$.

  Both floors exceed $C_\infty$, so $S = C_\infty$ (if true) cannot be proved by any sharpening of that route. At least $80.5\%$ of the centered bracket and $91.1\%$ of the causal (Harnack-relaxation) bracket lie below the route's floor.
- **NUMERICAL.** The best constant the edge route can give is about $0.1854129$ (centered) and about $0.188201$ (Harnack relaxation), against FINITE-ENERGY's $0.186059$ and $0.188735$. Their constants are within $0.35\%$ and $0.29\%$ of what the route can give.
- **NUMERICAL.** Adversarial searches over actual multichannel branches found no gain $\ge 1$ at $k_BT = C_\infty\sqrt\rho$. Pointwise DOS monotonicity of $T_{\rm lin}$ fails (§7), so the flat-DOS comparison route is not available by monotone level raising.

## 1. Inherited model (no new assumptions)

We use the model of `../FINITE-ENERGY/RIGOR.md` §1 (lines 34–87) verbatim:

- $w_n = 2n+1$;
- $k_j(t) = (t+j^2)^{-1}$;
- $p_{nm} = k_{|n-m|} - k_{n+m+1} > 0$ and $S_{nm} = k_{|n-m|} + k_{n+m+1} > 0$;
- the edge form
$$I_{xy}(t) = \sum_{n,m\ge0} b_n c_m\big[p_{nm}(X_n^2+Y_m^2) - 2S_{nm}X_nY_m\big];$$
- the bare edge norm $B_r(X,Y) = \sum_n w_n(r^{-1}b_nX_n^2 + r c_nY_n^2)$;
- the edge reserve
$$B_r + \tfrac12 I_{xy}(t) \ge d_* B_r\quad\forall r>0,\ t>0,\ \text{admissible }(b,c),\qquad\text{(eq:edge\_reserve)}$$
- and its consequence: strict stability whenever $(2\pi\tau)^2 > 2(1-d_*)\rho$.

Classes:

- $\mathcal C_{\rm cent}$ consists of the centered even-DOS Poisson weights at widths in the two-sided cone $w_m^{-1}\le s_m/s_0\le w_m$ (FINITE-ENERGY line 7 and §4).
- $\mathcal C_{\rm caus}$ is handled in FINITE-ENERGY through the four Harnack inequalities `eq:harnack` (lines 48–53), called the "synthetic causal relaxation" (line 56). Write $\mathcal H$ for the set of sequences $b\in[0,1]^{\mathbb N}$ obeying `eq:harnack`.

## 2. Lemma 1 (route constant). PROVED

Let $\mathcal W$ be an admissible weight set. Define
$$\Lambda(\mathcal W) := \sup\Big\{\frac{-\tfrac12 I_{xy}(t)}{B_r(X,Y)} : b,c\in\mathcal W,\ t>0,\ r>0,\ X,Y \text{ finitely supported},\ B_r>0\Big\}.$$

Then `eq:edge_reserve` holds for $\mathcal W$ with reserve $d_*$ if and only if $d_*\le 1-\Lambda(\mathcal W)$. Consequently the edge route proves at best $k_BT_{\rm lin} < C_{\rm route}\sqrt\rho$ with
$$C_{\rm route}(\mathcal W) = \frac{\sqrt{2\Lambda(\mathcal W)}}{2\pi},$$
and it cannot certify any constant below this value.

*Proof.* Since $B_r\ge0$, the inequality $B_r + \tfrac12 I\ge d_*B_r$ is equivalent to $-\tfrac12 I \le (1-d_*)B_r$.

If $B_r = 0$, then $b_nX_n^2 = 0$ and $c_mY_m^2 = 0$ for all $n,m$. Every term of $I$ carries one of the factors $b_nc_mX_n^2$, $b_nc_mY_m^2$ or $b_nc_mX_nY_m$, so $I = 0$ and the inequality is trivial.

Otherwise, divide by $B_r$ and take the supremum. Inserting the best admissible $d_* = 1-\Lambda$ into FINITE-ENERGY's stability criterion $(2\pi\tau)^2 > 2(1-d_*)\rho$ gives $C_{\rm route}$. Any $d_* > 1-\Lambda$ violates the hypothesis on some admissible instance. $\square$

FINITE-ENERGY's numbers fit this form. With $d = 19/60$ and $d = 19/64$ one gets $2(1-d) = 41/30$ and $45/32$; with $d_* = 317/1000$ and $119/400$ one gets $683/500$ and $281/200$. These are exact identities, **CERTIFIED** in `replay.py` E1.

## 3. Lemma 2 (diagonal reduction; $k_0$ cancels). PROVED

Take $b = c$ with $b_n>0$, $r = 1$, and $X = Y$ with $X_n = v_n/\sqrt{w_nb_n}$. Then $B_1 = 2\|v\|^2$ and $-\tfrac12 I(t) = v^{\mathsf T}\mathcal A_b(t)v$, where
$$\mathcal A_b(t)_{nm} = \frac{\sqrt{b_nb_m}\,S_{nm}}{\sqrt{w_nw_m}}\ (n\ne m),\qquad \mathcal A_b(t)_{nn} = \frac{2b_nk_{2n+1} - \sum_{m\ne n}b_m p_{nm}}{w_n}.$$
Hence $2\Lambda(\mathcal W)\ge \sup_{v} v^{\mathsf T}\mathcal A_b(t)v/\|v\|^2$ for every $b\in\mathcal W$ and every $t>0$.

*Proof.* In $\tfrac12 I$, the $n=m$ term is $b_n^2X_n^2(p_{nn}-S_{nn}) = -2b_n^2k_{2n+1}X_n^2$. The singular $k_0 = 1/t$ cancels exactly.

For $n\ne m$, symmetry of $p$ gives $\tfrac12\sum_{n\ne m}b_nb_mp_{nm}(X_n^2+X_m^2) = \sum_n b_nX_n^2\sum_{m\ne n}b_mp_{nm}$. The cross term is $-\sum_{n\ne m}b_nb_mS_{nm}X_nX_m$.

Substituting $b_nX_n^2 = v_n^2/w_n$ and $b_nb_mX_nX_m = \sqrt{b_nb_m}\,v_nv_m/\sqrt{w_nw_m}$ gives $\tfrac12 I = -v^{\mathsf T}\mathcal A_bv$. Finally, $B_1 = \sum_n w_n(b_nX_n^2 + b_nX_n^2) = 2\|v\|^2$. $\square$

When $b\equiv1$ and $t\to0$, $\mathcal A_b$ is the flat soft operator, whose top eigenvalue is $\kappa = (2\pi C_\infty)^2 = 1.3181402121\ldots$ (**NUMERICAL**: `numerics/opt0.py` gives $1.318140213729$ at $N=160$). Lemma 2 shows the frozen-weight edge problem is a weighted version of the $d=1$ soft operator in which the weights enter the pair-breaking diagonal and the pairing off-diagonal differently. Choosing $b_n$ decreasing in $n$ suppresses pair-breaking from high Matsubara rows more than it suppresses low-index pairing, and that pushes the top eigenvalue above $\kappa$.

## 4. Theorem 1 (edge-route obstruction). PROVED + CERTIFIED

Fix $t = 10^{-6}$. Let $L = 4000$ and $N_0 = 160$.

**(a) Centered instance.** Let $b^{\rm cent}_n = \frac2\pi\arctan(W/w_n)$ with $W = 33/4$.

- *Membership (PROVED).* $b^{\rm cent}$ is the Poisson average of the even box DOS $\mathbf 1_{[-W,W]}$ at widths $\sigma_n = s_n/s_0 = w_n$, which lie on the closed upper boundary of the width cone, with $s_n = w_n\ge w_n$. Equivalently, $b^{\rm cent}_n = \phi_{w_n}(b_0)$, the lower envelope of FINITE-ENERGY Proposition 1 (line 313). So $b^{\rm cent}\in\mathcal C_{\rm cent}$ as that lane defines the class. It is also the zero-normal-self-energy weight of an actual box-DOS branch; see (e).
  - The four Harnack bounds and monotone decrease are checked in Arb for $m\le L$.
  - Beyond $L$, monotonicity holds because $\arctan$ is increasing.
- *Certificate (CERTIFIED).* For the stored trial vector $v^{\rm cent}\in\mathbb R^{160}$ (exact dyadic floats, `cert_vectors.json`), the Rayleigh quotient satisfies
$$\frac{v^{\mathsf T}\mathcal A_{b^{\rm cent}}(10^{-6})v}{\|v\|^2}\in[1.357186931006264952760059\pm3.7\times10^{-26}] > R_{\rm cent} := 1.357186.$$

**(b) Harnack-relaxation instance.** Let $b^{\rm H}_n = \max(b_0/w_n,\ w_nb_0-(w_n-1))$ with $b_0 = 7/8$. The sequence is exactly $(7/8, 5/8, 3/8, 1/8, 7/72, 7/88, \dots)$, with $b_n = b_0/w_n$ for $n\ge3$.

- *Membership (PROVED).* $b^{\rm H}$ is the pointwise maximum of the two lower Harnack bounds, so the lower bounds hold. The upper bounds hold because $b_0/w\le wb_0$, $b_0/w\le(b_0+w-1)/w$, $wb_0-(w-1)\le wb_0$ and $wb_0-(w-1)\le(b_0+w-1)/w$; the last is equivalent to $(w-1)(w+1)(b_0-1)\le0$. So $b^{\rm H}\in\mathcal H$. This is also checked in exact rationals for $m\le L$, together with the closed form for $m\ge3$.
- *Certificate (CERTIFIED).*
$$\frac{v^{\mathsf T}\mathcal A_{b^{\rm H}}(10^{-6})v}{\|v\|^2}\in[1.398311736412096733120856\pm1.3\times10^{-25}] > R_{\rm H} := 1.398311.$$

**Rigour of the infinite sums (PROVED).** Only the diagonal contains infinite sums, and they enter with a minus sign, so an upper bound suffices. For $L>n$, $m\ge L$:

- $0\le b_m\le b_L$ (monotone decrease);
- $p_{nm}>0$;
- $\sum_{m\ge L}p_{nm} = \sum_{m\ge L}(k_{m-n}-k_{m+n+1}) = \sum_{j=L-n}^{L+n}k_j$, which telescopes because $k_j\to0$.

`replay.py` adds $b_L\sum_{j=L-n}^{L+n}k_j$ to the explicit sum over $m<L$. All arithmetic uses 192-bit Arb balls with outward rounding, and the reported value is the lower endpoint of the final ball.

**(c) Consequences (PROVED from Lemma 1, 2 and the certificates).**

- On $\mathcal C_{\rm cent}$, every edge reserve has $d_* < 1 - R_{\rm cent}/2 = 0.321407$, and every edge-route constant satisfies
$$C_{\rm route}(\mathcal C_{\rm cent}) \ge \sqrt{R_{\rm cent}}/(2\pi) > 0.185411.$$
- Since $\mathcal C_{\rm cent}\subset\mathcal C_{\rm caus}$, the same floor $0.185411$ holds for any edge-reserve proof on the actual causal class.
- On the Harnack relaxation $\mathcal H$, $d_* < 1 - R_{\rm H}/2 = 0.3008445$ and
$$C_{\rm route}(\mathcal H) > 0.188201.$$
- Both floors exceed $C_\infty$. **CERTIFIED:** $R_{\rm cent}, R_{\rm H} > \kappa_{\rm hi} = (2\pi\cdot0.1827262477723295176168720)^2 = 1.31814021213242038\ldots$, using the certified upper endpoint of `../../../GAMMA/RESULT.md` (row $\gamma=2$). That endpoint is CERTIFIED there, conditional on the analytic tail estimates in its RIGOR.md.

**(d) Comparison with FINITE-ENERGY.** This is conditional on that lane's certificates, which are under repair.

- FINITE-ENERGY certifies $\Lambda\le 683/1000$ on its centered relaxation and $\Lambda\le 281/400$ on $\mathcal H$ (reserves $317/1000$ and $119/400$). Together with (c), the best edge-route constant lies in
  - $[0.185411,\ 0.186014]$ (centered), against the stated $C_{\rm cent} = 0.186059$;
  - $[0.188201,\ 0.188651]$ (Harnack), against the stated $C_{\rm caus} = 0.188735$.
- **CERTIFIED** in `replay.py`: $(0.185411 - C_\infty)/(C_{\rm cent}-C_\infty) > 0.805$ and $(0.188201 - C_\infty)/(C_{\rm caus}-C_\infty) > 0.911$. So at least $80.5\%$ and $91.1\%$ of the respective open brackets are unreachable by any edge-reserve argument.
- No contradiction with FINITE-ENERGY was found: $R_{\rm cent}<683/500<41/30$ and $R_{\rm H}<281/200<45/32$ (**CERTIFIED** as exact rational comparisons).

**(e) Actual-branch version. [INFERENCE]** (continuity sketch, not formalized). Take two channels with the same box DOS of half-width $W\pi\tau$ and one reciprocal edge of strength $\varepsilon$ at dimensionless energy $t$.

- As $\varepsilon\to0$ at fixed $\tau$, the actual widths converge to the bare $s_n = w_n$ and the weights converge to $b^{\rm cent}$, with $0\le b\le1$.
- For a fixed finite-support $v$, the Rayleigh quotient of Lemma 2 is continuous under this convergence (dominated convergence in $\sum_m b_mp_{nm}$, since $\sum_{m\ne n}p_{nm}<\infty$).
- The reserve inequality is homogeneous in the edge strength.

So the floor $0.185411$ applies even when the reserve is required only on actual centered branches. For the Harnack instance there is no such realization:

- **OPEN** whether $\Lambda(\mathcal C_{\rm caus})$ on actual causal branches exceeds the centered value.
- **[INFERENCE]** $b^{\rm H}$ is not exactly realizable. Equality in the lower bound for $1-B$ (at $m\le3$) and for $B$ (at $m\ge3$) would make both $B$ and $1-B$ extremal positive harmonic functions, whose sum cannot be the constant $1$.

**(f) Interpretation. [INFERENCE]** The frozen-weight edge inequality must hold for every edge with weights that are frozen independently of that edge. The instances above use $X = Y$ on a soft edge ($t\to0$), where $k_0$ cancels in pairing. In an actual branch, the same soft edge also feeds the normal widths through $k_0$, which suppresses those weights. That suppression is exactly what the per-edge reserve cannot see. This agrees with FINITE-ENERGY's own OPEN item (line 455): closing the gap needs multi-frequency self-consistency or a global cross-channel argument, not a better edge reserve.

**(g) Two Matsubara rows suffice. CERTIFIED.** The obstruction already appears on trial vectors supported on rows $n\in\{0,1\}$. With the same weights and $t = 10^{-6}$, `replay.py` (E6) certifies:
- $v = (0.94548797, 0.32565701)$ (box) gives Rayleigh quotient $\in[1.332987909590540403264320\pm3.9\times10^{-25}] > 1.3329 > \kappa_{\rm hi}$;
- $v = (0.95361671, 0.30102355)$ (Harnack) gives $\in[1.387055335070180423825369\pm3.1\times10^{-25}] > 1.3870 > \kappa_{\rm hi}$.

For the Harnack instance the leading block is explicit as $t\to0$, with $b = (7/8, 5/8, 3/8, 1/8, 7/(8w_m),\dots)$. **NUMERICAL** values at $t = 10^{-6}$ are in brackets:
$$\mathcal A_{00} = \tfrac74 - \sum_{m\ge1}b_m\Big(\tfrac1{m^2}-\tfrac1{(m+1)^2}\Big)\ [1.21859],\qquad \mathcal A_{01} = \frac{\sqrt{35/64}\,(1+\tfrac14)}{\sqrt3}\ [0.53369],\qquad \mathcal A_{11}\ [-0.30364].$$
For the flat weight $b\equiv1$ (**NUMERICAL**, $t = 10^{-6}$, $N = 160$), the leading $k\times k$ blocks have top eigenvalues $0.999999$, $1.273649$, $1.308233$, $1.316940$, $1.318074$ and $1.318139$ for $k = 1, 2, 3, 5, 10, 160$. The flat soft top $\kappa$ is approached only through many rows. The box and Harnack weights exceed $\kappa$ already at $k = 2$ (box: $1.122327$ at $k = 1$, $1.332988$ at $k = 2$; Harnack: $1.218586$, $1.387055$).

So the excess over $\kappa$ is a low-frequency effect. Weights that drop between rows 0 and 1 and decay beyond them cut the pair-breaking diagonal $\sum_{m\ne n}b_mp_{nm}$ more than they cut the pairing couplings $\sqrt{b_nb_m}\,S_{nm}$ among the low rows. This locates where a non-edge-wise argument must act: on the $n\le1$ block of a soft edge, where the actual normal widths $s_0, s_1$ respond to the same soft glue (**[INFERENCE]**).

## 5. Route-optimum estimates. NUMERICAL

These use `numerics/opt0.py`, `opt0h.py`, `opt0p.py`, `opt0c.py`, `edgeopt.py` and `escan.py`, with $N = 160$ trial rows and 20000 explicit normal-row terms in the soft limit $t\to0$, unless stated otherwise.

**Centered, $b = c$, box family $b_n = \frac2\pi\arctan(W/w_n)$.**

| $W$ | 4 | 6 | 8 | 10 | 12 | 16 | flat ($W\to\infty$) |
|---|---|---|---|---|---|---|---|
| $\lambda_{\max}$, $t=0$ | 1.32766 | 1.35295 | 1.3571516 | 1.35620 | 1.35392 | 1.34899 | 1.3181402 $(=\kappa)$ |

- The optimum at $t = 10^{-6}$ is $W^* = 8.2727$ with $\lambda = 1.3571871725$, giving a route constant of $0.18541292$. At $N = 320$, $W = 8$ the value changes by less than $10^{-11}$.
- **Full centered relaxation** ($t = 0$; lower envelope $\phi_{w_m}(b_0)$, Harnack upper bounds; L-BFGS-B, 6 starts per $b_0$): the optimizer returned the lower envelope (the box) at every $b_0\in\{0.80, 0.85, 0.88, 0.90, 0.92, 0.93, 0.94, 0.96\}$. The values were 1.29161, 1.33163, 1.34768, 1.35430, 1.35712, 1.35694, 1.35561 and 1.34911.
- **Poisson pair, $b\ne c$** ($t = 0$; 46 geometric DOS bins per channel with edges $0.05\cdot1.3^k$ and a tail bin; 6 starts for each of seeds 1 and 2): the best was $1.3567150$, at box/box with neighbouring bin edges. That is no improvement over $b = c$.
- **Finite $t$, $X\ne Y$, free $r$.** `escan.py` solves the full edge eigenproblem for box pairs $W_b, W_c\in\{1,2,4,8,16,32\}$. The maximum is at $W_b = W_c = 8$ for every $t$: $\alpha = 1.34501$, $1.35105$, $1.35348$, $1.35470$, $1.35593$, $1.35654$, $1.35678$ and $1.35703$ at $t = 0.01$, $0.005$, $0.003$, $0.002$, $10^{-3}$, $5\cdot10^{-4}$, $3\cdot10^{-4}$ and $10^{-4}$. $\alpha$ increases as $t\downarrow0$ towards the soft-limit value $1.3571516$ ($W = 8$), so the supremum is in the soft limit.
- `edgeopt.py` (free DOS levels, L-BFGS-B) found nothing above these box values at $t\ge10^{-3}$: $1.32114$, $1.34473$, $1.35320$ and $1.35564$ at $t = 0.03$, $0.01$, $0.003$ and $10^{-3}$. Its runs at $t\le3\cdot10^{-4}$ did not converge.

**Harnack relaxation, $b = c$.** The optimizer returned the lower Harnack envelope at every $b_0$ tested. Along the envelope, $\lambda(b_0)$ is piecewise smooth with local maxima at the kinks $b_0 = w_m/(w_m+1)$:

| $b_0$ | 0.80 | 5/6 | 0.86 | 0.875 = 7/8 | 0.88 | 0.89 | 0.90 = 9/10 | 0.91 |
|---|---|---|---|---|---|---|---|---|
| $\lambda$ ($t = 10^{-6}$) | 1.37601 | 1.39640 | 1.39739 | **1.3983117** | 1.39706 | 1.39465 | 1.39234 | 1.38818 |

Pair runs at equal heads reproduce the $b = c$ value (1.392342 at $(0.9, 0.9)$). Unequal heads are lower (1.383769 at $(0.85, 0.95)$).

So, **NUMERICAL**, $C_{\rm route}(\mathcal C_{\rm cent})\approx0.1854129$ and $C_{\rm route}(\mathcal H)\approx0.188201$. The certified floors in Theorem 1 coincide with these optima to six digits.

## 6. Lower-side search over actual branches. NUMERICAL

`numerics/engine.py` is the self-consistent multichannel normal solver (centered, or anchored-shifted) plus the folded Perron gain at $\tau = C_\infty\sqrt\rho$.

- *Validation:* flat single channel, $t = 0.02$: $0.9994916127320115$, against FINITE-ENERGY's $0.999491612731$ (`numerics/val.py`).
- *Search* (`numerics/search.py`): $d\in\{2,3\}$, couplings $J$, DOS heights, two Lorentzian spectral modes with $t\ge t_0$, and 12-bin piecewise-constant DOS levels (even for centered; independent signs for shifted).
- All 25 finished starts have gain $< 1$ and below the flat single-channel gain at the same $t_0$. See RESULT.md for the rows and seeds. Two shifted searches converged to the gain of a centered optimum: seed 12 ($t_0 = 0.01$, $d = 2$) matches the seed-11 optimum $0.99984405824013$ to 13 digits, and seed 28 ($t_0 = 1$, $d = 2$) matches the seed-27 optimum $0.731445035217375$ to 15 digits. **[INFERENCE]** The optimizer removed the asymmetry; the search found no benefit from shifting.
- A centered 15-level DOS scan (`numerics/opt1.py`, $d = 1$, L-BFGS-B, 3 starts plus a bipartite start, $t = 0.01$) converges to the flat DOS: $g = 0.9997012185$, the flat value, with every level at 1.
- **[INFERENCE]** This is weak evidence for $S = C_\infty$. It is not a bound.

## 7. Failure of DOS monotonicity. NUMERICAL

`numerics/monoc.py` uses random 1- and 2-channel systems with a 13-bin DOS and checks central-difference derivatives of the gain at $(N, P_c) = (128, 64)$, $(256, 128)$ and $(512, 256)$ with $h = 10^{-3}$ and $10^{-4}$.

- Centered, seed 31: $d = 2$, $t = 0.005075$. Raising channel 0's level on the bin $|\xi|\in[8,16]\pi\tau$ lowers the gain: $\partial g = -3.53329\times10^{-3}$, stable to 8 digits across all resolutions.
- Centered, seed 32: $\partial g = -4.1255\times10^{-6}$.
- Shifted, seed 33: $\partial g = -3.67217\times10^{-3}$.

`numerics/tl.py` holds the physical system fixed and computes $T_{\rm lin}$ itself by root-finding in $\tau$, rescaling $t$ and the DOS coordinates. At the seed-31 instance, $T_{\rm lin}/(C_\infty\sqrt\rho) = 0.5760882$ with $d(T_{\rm lin}/C_\infty\sqrt\rho)/d(\text{level}) = -0.043572$. Seeds 32 and 33 give $-3.1185\times10^{-4}$ and $-6.1431\times10^{-3}$. Each derivative agrees to at least 5 digits for $h = 10^{-2}$ and $10^{-3}$ and for $(N, P_c) = (128, 64)$ and $(256, 128)$.

So $T_{\rm lin}$ is not monotone in the DOS levels. One cannot raise the DOS pointwise to the energy-independent (flat) case, where `../../PHYS-Q2/RIGOR.md` PROVES the $C_\infty$ ceiling at arbitrary boson energies, and conclude a bound. **OPEN** whether $T_{\rm lin}(N)\le T_{\rm lin}(N_{\rm flat})$ nonetheless holds globally, with matched normalization. **[INFERENCE]** A constant DOS is invariant under energy shifts, so its normal branch has no odd (asymmetric) part. The flat causal case is then the flat centered case and is covered by PHYS-Q2. This lane did not formalize that reduction.

## 8. Open items

1. **OPEN:** $S_{\rm cent}$ and $S_{\rm caus}$. Is either equal to $C_\infty$?
2. **OPEN:** a non-edge-wise upper argument. Such an argument must keep the normal-width feedback of soft edges (Theorem 1(f)).
3. **OPEN:** the route constant on actual causal (non-centered) branches. It lies in $[0.185411, 0.188651]$. The lower end is CERTIFIED here, through $\mathcal C_{\rm cent}\subset\mathcal C_{\rm caus}$. The upper end is FINITE-ENERGY's certified Harnack reserve, because actual causal branches lie in $\mathcal H$. Whether it reaches the Harnack floor $0.188201$ depends on whether the Harnack instance of Theorem 1(b) can be approached by actual causal branches.
4. **OPEN:** global flat comparison $T_{\rm lin}(N)\le T_{\rm lin}(N_{\max})$, despite the pointwise non-monotonicity in §7.

## 9. Replay

`replay.py` (python-flint, 192-bit Arb) re-verifies every CERTIFIED number above. Its docstring lists E1–E7: identities, membership, Rayleigh bounds, comparison with $\kappa_{\rm hi}$, the two-row witnesses, the consistency comparisons and the bracket shares. It exits 0. Each guarded mutant (`--mutant identity|cent_claim_up|caus_claim_up|floor_up|kappa_up|harnack_violate|vector_tamper|frac_up|two_row_up`) exits 1 with `REJECT:`. Exit codes are recorded in RESULT.md. `gen_vectors.py` (NUMERICAL helper) regenerates the 160-row trial vectors. The certificate does not depend on how the vectors were obtained.
