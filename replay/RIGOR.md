# ANISO-SHARP: a refined centered certificate and the remaining coupled question

## 0. Statement and trust boundary

**PROVED (pending independent review), with a computational part eligible for CERTIFIED only after the recorded two-implementation replay succeeds.** In the inherited centered finite-channel class,

\[
 S_{\rm cent}\le C_*:=\frac{\sqrt{341/250}}{2\pi},\qquad
 k_BT_{\rm lin}<C_{\rm rep}\sqrt\rho,\qquad
 C_{\rm rep}:=\frac{\sqrt{6821/5000}}{2\pi}.
\]

The certificate target is the edge reserve \(d_*=159/500=0.318\). The reported reserve is \(d_{\rm rep}=3179/10000=0.3179\), leaving a bare gap \(1/6821\) at the reported temperature. Exact rational decimal enclosures are

\[
 0.185877711471916<C_*<0.185877711471917,\quad
 0.185891338370617<C_{\rm rep}<0.185891338370618.
\]

Neither constant is claimed sharp. **OPEN:** \(S_{\rm cent}=C_\infty\) versus \(S_{\rm cent}>C_\infty\). The causal upper constant is not improved here. All temperatures are energy-valued linear ME onset temperatures, not thermodynamic exact-Hamiltonian Tc or measurements.

The model, centered width cone and folded stability reduction are the same as in `../FINITE-ENERGY/RIGOR.md`. The new arithmetic uses separate copied bodies from its primary and independent implementations. There is no import of the new primary checker by the independent checker. `source-pins.json` pins thirteen read-only inherited proofs and arithmetic sources. Infinite normal-branch existence, the centered width cone and the scalar sharp lower construction are analytic inputs, not outputs of the finite computation. This text derives the reserve argument, its infinite-tail reduction and its conversion to an onset bound. Independent mathematical review of this continuation remains required.

## 1. Actual model and the precise unsolved comparison

Let channels x have finite positive DOS-height weights eta_x. In the inherited normalization, a reciprocal nonnegative measure d m_xy(E) has moment mass M_xy = integral d m_xy(E) and acts as

\[
 (Mf)_x=\sum_y\eta_y M_{xy} f_y,\qquad \rho=\|M\|_{\ell^2(\eta)}\in(0,\infty).
\]

Here rho has energy-squared units. Reciprocity is M_xy=M_yx. Entrywise nonnegativity is required; positive semidefiniteness of M is NOT required. Each measure is supported on positive energies, has finite moment and finite zero-transfer mass at a tested positive temperature. Normal rows have a bound R(tau)<infinity at each tested tau, without requiring a temperature-independent bound. The normalized fixed DOS profiles nu_x=N_x/N_max,x lie in [0,1] and are even. Radial vertices are energy independent within a channel. Pairing and normal equations have the same nonnegative retarded transfer. The comparison permits a dominated attractive pairing envelope, an odd-folded nonnegative additional normal mass, and a PSD static pairing subtraction.

Put tau=k_B T, omega_n=pi tau w_n, w_n=2n+1, t=(E/(2 pi tau))^2 and

\[
 k_j(t)=(t+j^2)^{-1},\quad
 p_{nm}=k_{|n-m|}-k_{n+m+1}>0,\quad
 S_{nm}=k_{|n-m|}+k_{n+m+1}.
\]

Thus the energy-squared factor removed from the physical transfer is (2 pi tau)^2, not (pi tau)^2. On the centered branch,

\[
 b_{n,x}=\int_{\mathbb R}\nu_x(\xi)
 \frac{\pi\tau s_{n,x}}{(\pi\tau s_{n,x})^2+\xi^2}\frac{d\xi}{\pi},\quad
 s_{n,x}=w_n+\frac1{(2\pi\tau)^2}\sum_y\eta_y\int\sum_m p_{nm}(t)b_{m,y}\,d m_{xy}(E).
\]

Extra allowed normal mass only increases the displayed width lower bound. The inherited centered width cone is w_m^{-1} <= s_m,x/s_0,x <= w_m. It implies four Harnack inequalities for b and its complement, including

\[
 b_0/w_m\le b_m\le w_m b_0,\quad
 w_m b_0-(w_m-1)\le b_m\le (b_0+w_m-1)/w_m.
\]

The scalar case, arbitrary flat-DOS coupled channels, and a common branch with transfer-by-transfer balanced rows have the sharp constant C_inf. All-row operational balance on a common nonzero DOS branch collapses to transfer-measure balance by SHARPFLAT4, so it is not a solution for unequal channel profiles. A common-soft lower sequence proves S_cent>=C_inf. These are inherited theorems. The missing theorem is a simultaneous channel-frequency comparison of the actual coupled normal equation and pairing form. Separate per-edge admissibility constraints discard part of that coupling.

The reviewed SHARP obstruction puts the centered frozen-weight edge-method floor at at least 0.185411, and the four-Harnack relaxation floor at at least 0.188201. Neither is an actual-branch instability or a lower bound on S_cent or S_caus.

## 2. The edge reduction and the factor of two

For a finite-support real gap profile v, write g_n,x=sqrt(w_n b_n,x) v_n,x. The folded form is

\[
 Q(v)=\sum_x\eta_x\|g_x\|^2+
 \frac1{2(2\pi\tau)^2}\sum_{x,y}\eta_x\eta_y\int I_{xy}(t)\,d m_{xy}(E),
\]

where, for X_n=v_n,x, Y_m=v_m,y, b_n=b_n,x and c_m=b_m,y,

\[
 I_{xy}=\sum_{n,m}b_n c_m\{p_{nm}(X_n^2+Y_m^2)-2S_{nm}X_nY_m\}.
\]

It suffices to prove, for all r>0, t>0 and admissible weights,

\[
 B_r+I_{xy}/2\ge d_*B_r,\qquad
 B_r=\sum_n w_n(r^{-1}b_nX_n^2+r c_nY_n^2).                 \tag{1}
\]

Set a_n=r^{-1/2}sqrt(w_n b_n)X_n, z_n=r^{1/2}sqrt(w_n c_n)Y_n, so B_r=sum(a_n^2+z_n^2). Zero-weight coordinates contribute no pairing term and are removed by continuity. For R'>rho, h=(I-M/R')^{-1}1 is positive, and Mh<R'h. Take r=h_x/h_y in (1). The two parts of the summed B_r each contribute at most R' sum eta_x ||g_x||^2, using reciprocity for the second. Consequently

\[
 Q(v)\ge\left[1-\frac{2(1-d_*)\rho}{(2\pi\tau)^2}\right]\sum_x\eta_x\|g_x\|^2.       \tag{2}
\]

This also explains why a nonnegative reciprocal M need not be PSD: the positive resolvent and its norm bound are enough. A nonnegative excess normal form or a PSD static subtraction increases Q. For a dominated pairing envelope the absolute-value trial profile bounds the attractive gain, so it cannot worsen the onset.

## 3. Centered Poisson lower envelope

Rescale channel energy by pi tau s_0 and put sigma=s_m/s_0. The two averages are integrals against the densities 2/[pi(1+xi^2)] and 2 sigma/[pi(sigma^2+xi^2)] on xi>=0. Their density ratio is sigma(1+xi^2)/(sigma^2+xi^2).

For sigma>=1 this ratio increases with xi, so minimizing the second average with the first fixed and 0<=nu<=1 fills an interval adjacent to zero. This gives (2/pi)atan(sigma^{-1} tan(pi b_0/2)). For sigma<=1 the ratio decreases, so the minimizing profile fills a tail interval. Integrating that tail gives (2/pi)atan(sigma tan(pi b_0/2)). Since sigma lies in [1/w,w], both cases give

\[
 b_m\ge\phi_w(b_0):=\frac2\pi\arctan\left(\frac1w\tan\frac{\pi b_0}2\right).           \tag{3}
\]

The profile minimizations follow directly by exchanging mass between points ordered by the density ratio; arbitrary measurable profiles follow by integration. Endpoint cases follow by continuity. For w>1, differentiating (3) shows that phi_w is increasing and convex. At b_0(xi)=(2/pi)atan(xi), its tangent has slope

\[
 L_{\xi,m}=\frac{w_m(1+\xi^2)}{w_m^2+\xi^2},\quad
 C_{\xi,m}=\frac2\pi\arctan(\xi/w_m)-L_{\xi,m}\frac2\pi\arctan\xi.
\]

The intercept is rounded downward to a rational of denominator 10^8 using independent rational atan and pi enclosures. The basic line b_0/w_m and the complementary line w_m b_0-(w_m-1) are retained. The new reference points are xi=4,5,6,8,10,12,16,24. Every resulting line is a valid lower bound, including when its intercept is negative. Only coefficients with nonnegative sign may multiply these lower bounds.

## 4. Disjoint sector decomposition and infinite tail

Use M=20. Split all frequency pairs into (0,0); (0,m)/(m,0) for m>=1; (1,k)/(k,1) for 2<=k<=20; and all remaining n,m>=1. There is no overlap. For a remaining pair,

\[
 p(X^2+Y^2)-2SX Y=p(X-Y)^2-4k_{n+m+1}XY.
\]

The half-edge form therefore contains a nonnegative square and the reflected term -2 b_n c_m k_{n+m+1}X_nY_m. Weighted AM-GM in the a,z coordinates bounds that term below by

\[
 -\frac{a_n^2}{w_m(n+m+1)^2}-\frac{z_m^2}{w_n(n+m+1)^2}.
\]

The factor 2 in this reflected term is essential. The exact upper row cost, for 1<=n<=20, is

\[
 q_n=\sum_{\substack{1\le m\le20\\(n,m)\notin\{(1,k),(k,1):2\le k\le20\}}}
 \frac1{w_m(n+m+1)^2}+\frac1{43(n+21)}.                 \tag{4}
\]

For m>=21 use w_m>=43 and the decreasing integral bound sum_(m>=21)(n+m+1)^(-2)<=1/(n+21). For n>20 no stage-1 pair is removed. The full row cost decreases in n and is bounded by its n=1 row, whose first sixteen terms plus an integral tail obey

\[
 q_{\rm full,n}\le\sum_{m=1}^{16}\frac1{w_m(m+2)^2}+\frac1{4\cdot16^2}<\frac{33}{500}.      \tag{5}
\]

Both are rational infinite-tail bounds, not a truncation of the physical normal equation.

Reserve d_* of every bare coordinate and subtract q_n. Put rem_n=1-d_*-q_n. Allocate alpha_1=rem_1, beta_1=0; alpha_k=(7/10)rem_k, beta_k=(3/10)rem_k for 2<=k<=20. For n>20 allocate alpha_ext=1-d_*-33/500=77/125 entirely to stage 0. All remainders are positive.

For stage 1 define p_1k=k_(k-1)-k_(k+2), S_1k=k_(k-1)+k_(k+2). Completing the square in z_k, with beta_k z_k^2, gives at least c_k D_1k(r,t) a_1^2, where

\[
 D_{1k}=\frac{r p_{1k}}6-\frac{S_{1k}^2}{12w_k(\beta_k+r^{-1}p_{1k}/(2w_k))}
 =\frac{2p_{1k}(r w_k\beta_k-2/(3w_k))}{12w_k\beta_k+6r^{-1}p_{1k}}.             \tag{6}
\]

Here S_1k^2-p_1k^2=4p_1k/(3w_k). The own weight b_1 cancels by b_1/(beta_k+C b_1)<=1/(beta_k+C). Swap r with 1/r and b with c for the other side. These terms enhance the stage-0 coefficient of the first tail. Their numerators are positive on r in [1/3,3], k>=2; the replay checks outward bounds before using monotonicity.

For stage 0 define p_0m=k_m-k_(m+1), S_0m=k_m+k_(m+1). If A_m is a positive lower bound for the available opposite-side coefficient divided by the own head weight, completing its square gives

\[
 D_{0m}(r,t;A_m)=\frac{r p_{0m}}2-\frac{S_{0m}^2}{4w_m(A_m+r^{-1}p_{0m}/(2w_m))}
 =\frac{2p_{0m}(r w_m A_m-2/w_m)}{4w_m A_m+2r^{-1}p_{0m}}.                    \tag{7}
\]

This follows from S_0m^2-p_0m^2=4p_0m/w_m. Positive numerator terms increase in r, p_0m and A_m. A negative numerator is bounded below by dropping the positive denominator contribution 2r^{-1}p_0m, using p_0m at the smaller t endpoint, and then using the UPPER Harnack ratio b_m/b_0<=w_m. Using a lower ratio on such a negative term would have the wrong sign. For m>20, w_m>=43 and (43/3)alpha_ext>2/43, so the unretained stage-0 completions are positive and may be discarded. Thus no finite-frequency remainder of unknown sign is left.

## 5. Head determinant and the new covering

After the two stages, denote the normalized head reserves by

\[
 \Phi_X=\frac{1-d_*}{c_0}+\sum_{m=1}^{20}\frac{c_m}{c_0}D_{0m}^{(X)},\quad
 \Phi_Y=\frac{1-d_*}{b_0}+\sum_{m=1}^{20}\frac{b_m}{b_0}D_{0m}^{(Y)}.
\]

In coordinates sqrt(c_0)a_0, sqrt(b_0)z_0 the remaining head matrix is

\[
 \begin{pmatrix}\Phi_X+\beta r&-(\beta+u)\\-(\beta+u)&\Phi_Y+\beta/r\end{pmatrix},\quad
 \beta=[2t(1+t)]^{-1},\quad u=(1+t)^{-1}.
\]

Its diagonals are positive. Clearing positive denominators in its determinant gives exactly

\[
 2t(1+t)\Phi_X\Phi_Y+r^{-1}\Phi_X+r\Phi_Y\ge2.             \tag{8}
\]

The same condition has a finite t=0 limit even though the uncancelled head matrix diverges. It is used only to close rectangles touching t=0; physical spectral atoms still have t>0.

Partition head weights at knots 0,1/2,3/4 and every i/200 for i=160,...,200. There are 43 consecutive intervals. In each head interval, a reserve of the form A/b_0+sum C_m b_m/b_0, with C_m>=0, is minimized over the exact rational lower tangent envelope in u_0=1/b_0. That envelope is convex piecewise affine in u_0. Its minimum occurs at an interval endpoint or a line-switch breakpoint. Both scripts verify that adjacent tangent intersections are ordered, so enumerating adjacent intersections omits no upper-envelope switch. On the first interval, all additional lines lie below b_0/w_m, which is verified rationally. Hence A/b_0 plus the constant basic ratios decreases to its minimum at b_0=1/2; no infinite-u endpoint is lost.

The arithmetic uses Q=10^12 integer-scaled lower and upper enclosures. All positive lower bounds are rounded downward and all subtracted costs or denominator upper bounds upward. The arrays in each checker implement (4), (6), (7), the head interval minima and (8). For a rectangle r in [r_l,r_h], t in [t_l,t_h], obtain positive uniform lower values P_X,P_Y for the two Phi quantities. Put r_0=(r_l+r_h)/2. Convexity of 1/r gives

\[
 r^{-1}P_X+rP_Y\ge\frac{2P_X}{r_0}+r_*\left(P_Y-\frac{P_X}{r_0^2}\right),
\]

where r_* is r_l for nonnegative slope and r_h otherwise. Use t_l in the positive product term of (8). Acceptance requires this unconditional lower bound to be at least 2 for ALL 43^2 head interval pairs, not sampled head weights.

The primary binary covering starts on [1,3]x[0,1/2], reflecting r<1 by exchange of channels. The independent four-way covering starts on the FULL [1/3,3]x[0,1/2] and treats negative completions on both sides separately. No primary cell decisions or tables are read by the second checker. Each tree partitions its parent exactly, counts rational leaf area, and fails if an unresolved rectangle exceeds its depth cap. The area totals must be exactly 1 and 4/3, respectively. All acceptance predicates are inequalities for closed rectangles, so the result covers the continuum, not a grid of parameter points.

Pi is bounded by Machin's formula 16 atan(1/5)-4 atan(1/239), using alternating rational Leibniz remainders. The two implementations use different series lengths and separate atan implementations. All C enclosures compare squared rational endpoints against the exact squared numerator with the appropriate pi bound. No floating point enters the reserve certificate.

## 6. Exterior regions with the NEW reserve

The exterior formulas remain analytic but their budget must be recomputed: alpha_ext=77/125. The unassisted head estimate is at least 1-2/(r+r^{-1}), and at least t/(1+t) after dropping a positive square.

For r<=1/4 or r>=4, the head estimate is >=9/17. The sum of possible negative stage-0 losses is less than (7/75)/alpha_ext, since

\[
 \sum_{m\ge1}\frac1{w_m m^2(m+1)^2}
 \le\sum_{m=1}^{20}\frac1{w_m m^2(m+1)^2}+\frac1{8\cdot20^4}<\frac7{75}.
\]

Thus the reserve is >9/17-(7/75)/alpha_ext>d_*.

For 1/4<=r<=1/3 or the reciprocal interval, the head estimate is >=2/5. All m>=2 completions are nonnegative because alpha_ext/8>1/25. The sole possible negative m=1 contribution is bounded below by (3/4)(alpha_ext/8-1/9)/alpha_ext. The resulting reserve is >d_*.

For t>=1/2 and r in [1/3,3], the head estimate is >=1/3, p_01<=4/9, and again only m=1 can be negative. The reserve is at least 1/3+(4/9)(alpha_ext/6-1/9)/alpha_ext>d_*.

Every displayed exterior comparison is verified exactly in BOTH new scripts. The compact covering and these three cases exhaust r>0,t>0. They establish (1).

## 7. From certified reserve to supremum and strict reported bound

In (2), 2(1-d_*)=341/250. Every tau>C_*sqrt(rho) has a strictly positive bare gap. Since normal rows are bounded separately at that tau, s_n,x<=w_n+R(tau)<=(1+R(tau))w_n. The bare gap controls the normal-coordinate norm by a positive factor 1/(1+R(tau)). Thus the positive linear pairing operator has gain strictly less than one at every such temperature. Therefore tau_lin<=C_*sqrt(rho), including disconnected instability sets. No unproved monotonicity of onset with temperature is used.

Since C_*<C_rep, this already implies tau_lin<C_rep sqrt(rho). At the reported temperature the bare gap equals

\[
 1-\frac{1-d_*}{1-d_{\rm rep}}=\frac1{6821}>0.
\]

This strict reported inequality does not require asserting that stability at one endpoint alone forces the supremum to be strictly below that endpoint. Endpoint stability without a neighborhood theorem would not justify that assertion. In particular, the predecessor reserve 317/1000 already IMPLIED the closed supremum bound sqrt(683/500)/(2 pi), approximately 0.186013935536718, even though the released strict reporting constant was 0.186059321394545. The improvement here is over both numbers, not merely reuse of the predecessor's slack.

## 8. Why the attempted sharp routes remain incomplete

**PROVED (pending independent review), elementary necessary condition.** For a single atom of physical moment mass j_xy>0 at squared energy t, put a_xy=j_xy/(2 pi tau)^2. The actual positive normal equation gives, for any n,

\[
 s_{n,x}\ge w_n+\eta_y a_{xy}p_{nn}b_{n,y},\quad
 s_{n,y}\ge w_n+\eta_x a_{xy}p_{nn}b_{n,x},\quad
 p_{nn}=\frac{w_n^2}{t(t+w_n^2)}.
\]

For positive b values their product is strictly larger than eta_x eta_y a_xy^2 p_nn^2 b_n,x b_n,y. Thus the same-frequency ORDINARY-transfer factor

\[
 \frac{\sqrt{\eta_x\eta_y}\,a_{xy}p_{nn}\sqrt{b_{n,x}b_{n,y}}}{\sqrt{s_{n,x}s_{n,y}}}<1.
\]

This does not bound the full pairing operator: the reflected term 2k_(2n+1), other frequencies and other edges remain. For fixed integrable DOS profiles, fixed positive eta and a soft atom whose a_xy stays bounded below, holding both b_n,x and b_n,y bounded below as t->0 is impossible. The widths would diverge by these inequalities, while each integrable DOS Poisson average is at most ||nu_x||_1/(pi^2 tau s_n,x) and tends to zero at tau bounded below. This excludes that particular frozen-head realization. It does NOT exclude a counterexample with spectra, DOS bands and channel weights scaled together, as permitted when taking a supremum over models.

The Perron-resolvent reduction in section 2 is valid for unequal channels but produces the edge-reserve method floor, not C_inf. Treating M as PSD would incorrectly discard admissible bipartite matrices. A scalar comparison applied separately to each edge loses the common actual normal equation. Operational balance on a common branch cannot bypass this by SHARPFLAT4's collapse theorem. These routes were not promoted to a sharp theorem.

Exploratory retained-runtime float searches considered two and three channels, multiple Einstein modes, unequal eta, boxes and nonmonotone binned DOS. They produced no witness above C_inf. They are NOT certification: finite pairing blocks, truncated normal tails and stopping residuals were not enclosed. Near-unity soft gains are especially unsuitable as exclusion evidence. No claim of exhaustive search, global DOS monotonicity or proof of S_cent=C_inf follows.

## 9. Replay boundary and open items

`python -B verify.py` launches `python -B replay.py` and `python -B independent.py`, then their six mutants each. The base scripts must exit 0. Every mutant must exit 1 with a REJECT message, rather than crashing from a missing dependency. Mutants corrupt source identity, strict reserve margin, continuum coverage, reserve feasibility, and each implementation's arithmetic-specific tangent/tail/completion guard. `CHECKS.txt` is the execution receipt. Only those observed outcomes support the CERTIFIED label.

Remaining: independent mathematical review of this continuation; the sharp actual centered coupled supremum; a certified actual-branch excess witness, if one exists; a sharper universal causal bound; and a literature/priority assessment if a manuscript is pursued. No new third-party paper content, cloud compute, commit, publication, build, lint, formatter or unrelated suite is involved. The inherited scalar spectral endpoint and analytic infinite-tail inputs were not reverified here.
