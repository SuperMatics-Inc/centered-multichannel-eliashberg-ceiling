# SHARPFLAT4 — Collapse of Centered Row-Update Balance and Sharp Supremum

## 0. Verdict, outcome, and claim labels

This work resolves the narrowed open problem posed in `../SHARPFLAT-REVIEW/REVIEW.md:54,195-204` (item P3) and `../SHARPFLAT/RIGOR.md:57-59`: in the two-channel centered case with a common bounded even normalized DOS $\nu$ and a common centered branch $s_{n,1} = s_{n,2} = s_n$, does $S = C_\infty$ hold under operational row-update balance along $b_m(s_m)$ at every Matsubara row $n \ge 0$, without assuming $d\mathfrak m = P\,d\mu$ factorization and without assuming the `../../../G3COMBINE/RIGOR.md:27` transfer-by-transfer hypothesis $(K_j\mathbf 1)_x = \bar K_j$ for every $j \ge 0$?

**Outcome: Theorem (Collapse to `G3COMBINE Q2`, yielding $S = C_\infty$) + Finite-Row Boundary Obstruction.**

Specifically:
1. **PROVED (Collapse Theorem, Theorem 1, §2):** On any finite-channel ($d \ge 2$, in particular $d = 2$) centered model with positive DOS heights $\eta_x > 0$, common bounded even normalized DOS $\nu$ having positive Lebesgue support ($\nu \not\equiv 0$), and finite-zero-lag, finite-moment reciprocal glue measures $d\mathfrak m_{xy} = d\mathfrak m_{yx} \ge 0$ on $(0,\infty)$, operational row-update balance along a common centered branch $b_m(s_m)$ at **every** Matsubara row $n \ge 0$ and at **one** temperature $\tau > 0$ **automatically forces**:
   - $(K_j \mathbf 1)_x = (K_j \mathbf 1)_y$ for every $j \ge 0$ and every channel pair $x, y$, and
   - measure-level row balance $\sum_{z=1}^d \eta_z\, d\mathfrak m_{xz} = \sum_{z=1}^d \eta_z\, d\mathfrak m_{yz}$ as Borel measures on $(0,\infty)$ (hence transfer-by-transfer row balance at all temperatures).
2. **PROVED (Sharp Supremum on the Reduced Conjecture Class, Corollary 1, §2):** Under the hypotheses of the Reduced Conjecture (`../SHARPFLAT/RIGOR.md:57-59`), either $\nu = 0$ a.e. (empty Cooper space, $T_{\rm lin} = 0$) or $\nu \not\equiv 0$, in which case Theorem 1 collapses the model into `../../../G3COMBINE/RIGOR.md:27`. Hence $k_B T_{\rm lin} < C_\infty \sqrt\rho$ (for $\rho > 0$) and the sharp supremum is $S = C_\infty$. **Crucially, this class is NOT strictly larger than `G3COMBINE Q2`**: all-row update balance on a nontrivial centered branch never occurs without measure-level transfer balance.
3. **PROVED and CERTIFIED (Non-factorized `G3COMBINE Q2` witness, §3):** While all-row update balance collapses to `G3COMBINE Q2`, `G3COMBINE Q2` itself is strictly larger than the factorized $d\mathfrak m = P\,d\mu$ tensor-product subclass of `../SHARPFLAT/RIGOR.md:44-50`: an explicit unequal-$\eta$ two-channel witness ($\eta = (1, 3)$, $d\mathfrak m_{11} = 3\delta_{E=1}$, $d\mathfrak m_{12} = \delta_{E=2}$, $d\mathfrak m_{22} = \delta_{E=1} + \frac{2}{3}\delta_{E=2}$) satisfies $(K_j \mathbf 1)_1 = (K_j \mathbf 1)_2$ for all $j \ge 0$ while $d\mathfrak m \ne P\,d\mu$, with $\rho = \|\mathcal M\|_{\ell^2(\eta)\to\ell^2(\eta)} = 6$.
4. **PROVED and CERTIFIED (Finite-row non-implication witness, §4):** Weakening "all Matsubara rows $n \ge 0$" to a finite prefix ($n = 0$) breaks the collapse: an explicit two-channel box-DOS witness ($\eta = (1, 1)$, $r(u) = \mathbf 1_{|u| \le 1}$, $\tau = 1/(2\pi)$, $d\mathfrak m_{11} = \delta_{E=1}$, $d\mathfrak m_{12} = 0$, $d\mathfrak m_{22} = c_2\delta_{E=2}$ with certified $c_2 \in [6.26499 \pm 5\times 10^{-6}]$) satisfies exact row-$0$ update balance along Channel 1's actual centered branch $b_m(s_m)$, while $\Delta_0 < -0.566 < 0$, $\Delta_1 < -0.752 < 0$, and row $n = 1$ fails balance ($< -0.240 < 0$).
5. **OPEN (outside this collapsed class):** `S_cent = C_inf` on general coupled centered non-flat-DOS branches without common centered normal widths or without all-row balance (currently bracketed in $[C_\infty, C_{\rm cent}]$, `../FINITE-ENERGY/RIGOR.md:6-10`, `../SHARP/RESULT.md:15-17`), as well as general rank-one or commuting couplings not satisfying `G3COMBINE Q2`.

---

## 1. Model, notation, and row-update balance

Let $X = \{1, \dots, d\}$ ($d \ge 2$; the two-channel case is $d = 2$) be a finite channel set with positive DOS-height weights $\eta_x > 0$, endowed with the $\ell^2(\eta)$ inner product $\langle u, v \rangle_\eta = \sum_{x=1}^d \eta_x \overline{u_x} v_x$ and operator action $(A h)_x = \sum_{y=1}^d A_{xy} \eta_y h_y$, as in `../../../G3COMBINE/RIGOR.md:21` and `../../PHYS-Q2/RIGOR.md:7`. Assume:
- **Reciprocal glue measures:** for each $x, y \in X$, $d\mathfrak m_{xy} = d\mathfrak m_{yx} \ge 0$ is a finite nonnegative Borel measure on $(0,\infty)$ with finite zero-lag and moment integrals
  $$K_0(x,y) = \int_{(0,\infty)} E^{-2}\,d\mathfrak m_{xy}(E) < \infty, \qquad \mathcal M_{xy} = \int_{(0,\infty)} d\mathfrak m_{xy}(E) < \infty.$$
  At temperature $\tau = k_B T > 0$, the dimensionless Matsubara transfers are
  $$K_j(x,y) := \int_{(0,\infty)} \frac{d\mathfrak m_{xy}(E)}{E^2 + (2\pi\tau j)^2} \qquad (j \in \mathbb Z),$$
  and $\rho := \|\mathcal M\|_{\ell^2(\eta)\to\ell^2(\eta)}$ (`../../../G3COMBINE/RIGOR.md:21`, `../SHARP/PLAN.md:4`).
- **Common bounded even normalized DOS:** every channel shares the same measurable even profile $\nu \in L^\infty(\mathbb R)$ with $0 \le \nu(\xi) \le 1$ and $\nu(-\xi) = \nu(\xi)$ (so $N_x(\xi) = \eta_x \nu(\xi)$). Writing $u = \xi/(\pi\tau)$ and $r(u) := \nu(\pi\tau u)$, the common centered Poisson transform at dimensionless half-Matsubara width $s > 0$ is
  $$b(s) := \frac{1}{\pi}\int_{-\infty}^\infty \frac{s}{s^2 + u^2}\,r(u)\,du = \frac{1}{\pi}\int_{-\infty}^\infty \frac{\pi\tau s}{(\pi\tau s)^2 + \xi^2}\,\nu(\xi)\,d\xi \in [0, 1].$$
- **Centered normal equations:** write $w_n := 2n + 1$ ($n \ge 0$) and $P_{nm}(x,y) := K_{|n-m|}(x,y) - K_{n+m+1}(x,y) \ge 0$. On a centered normal branch, the self-consistent widths satisfy
  $$s_{n,x} = w_n + \sum_{y=1}^d \eta_y \sum_{m=0}^\infty P_{nm}(x,y)\, b(s_{m,y}) \qquad (n \ge 0,\ x \in X).$$
  Note that row telescoping gives $\sum_{m=0}^\infty P_{nm}(x,y) = K_0(x,y) + 2\sum_{j=1}^n K_j(x,y) \le D_*$, where
  $$D_* := \max_{x \in X} \sum_{y=1}^d \eta_y \left(K_0(x,y) + \frac{\pi^2}{3(2\pi\tau)^2}\mathcal M_{xy}\right) < \infty$$
  (`../../../G3COMBINE/RIGOR.md:25`, `../FINITE-ENERGY-PAPER/replay/CENTERED-GAP/RIGOR.md:19`). Since $0 \le b(s_{m,y}) \le 1$, any positive solution satisfies $w_n \le s_{n,x} \le w_n + D_*$.

**Definition (Operational row-update balance along a common centered branch).** Fix $\tau > 0$ and suppose $s_n$ ($n \ge 0$) is a common centered branch ($s_{n,x} = s_n$ for all $x \in X$), with $b_m := b(s_m)$. For any pair $(x, y) \in X^2$, define the signed Borel measure on $(0,\infty)$
$$d\delta_{xy}(E) := \sum_{z=1}^d \eta_z \bigl(d\mathfrak m_{xz}(E) - d\mathfrak m_{yz}(E)\bigr)$$
and the transfer-row differences
$$\Delta_j^{(xy)} := (K_{|j|}\mathbf 1)_x - (K_{|j|}\mathbf 1)_y = \int_{(0,\infty)} \frac{d\delta_{xy}(E)}{E^2 + (2\pi\tau j)^2} \qquad (j \in \mathbb Z).$$
In the two-channel case $X = \{1, 2\}$, $d\delta := d\delta_{12} = \eta_1 d\mathfrak m_{11} + (\eta_2 - \eta_1)d\mathfrak m_{12} - \eta_2 d\mathfrak m_{22}$ by reciprocity $d\mathfrak m_{21} = d\mathfrak m_{12}$. Operational row-update balance between $x$ and $y$ along $b_m$ at row $n \ge 0$ is the condition
$$\sum_{m=0}^\infty \bigl(\Delta_{|n-m|}^{(xy)} - \Delta_{n+m+1}^{(xy)}\bigr) b_m = 0.$$
Notice that this condition is *weaker a priori* than $(K_j \mathbf 1)_x = (K_j \mathbf 1)_y$ for all $j \ge 0$, because it tests only the weighted combination against the single sequence $b_m = b(s_m)$.

---

## 2. Proof of the Collapse Theorem and $S = C_\infty$

Fix a pair $(x, y) \in X^2$ and suppress the superscript $(xy)$ in $\Delta_j := \Delta_j^{(xy)}$ and $d\delta := d\delta_{xy}$. By hypothesis,
$$\int_{(0,\infty)} (1 + E^{-2})\,d|\delta|(E) < \infty,$$
where $|\delta|$ is the total variation measure of $\delta$. In particular $\|\delta\|_{\rm TV} := |\delta|((0,\infty)) < \infty$, $\Delta_{-j} = \Delta_j$,
$$|\Delta_0| \le \int_{(0,\infty)} E^{-2}\,d|\delta|(E) < \infty, \qquad |\Delta_j| \le \frac{\|\delta\|_{\rm TV}}{(2\pi\tau j)^2} \quad (j \ne 0),$$
and therefore $\Delta = (\Delta_j)_{j\in\mathbb Z} \in \ell^1(\mathbb Z)$.

### Lemma 1 (PROVED: Dichotomy on $\nu$)
*Either $\nu = 0$ Lebesgue-a.e. on $\mathbb R$ (in which case $b_m = 0$ for all $m \ge 0$, $s_n = w_n$, the Cooper space is empty, and $T_{\rm lin} = 0$), or $\nu > 0$ on a set of positive Lebesgue measure, in which case $0 < b_m \le 1$ for every $m \ge 0$.*

*Proof.* Since $s_m \ge w_m \ge 1$, the Poisson kernel $\frac{1}{\pi}\frac{s_m}{s_m^2 + u^2}$ is strictly positive everywhere on $\mathbb R$ and integrates to $1$. If $\nu = 0$ a.e., then $r = 0$ a.e., so $b_m = 0$ for all $m$, the normal update gives $s_n = w_n$, the pairing form reduces to $\|g\|^2 \ge 0$ (`../../PHYS-Q2/RIGOR.md:17`), and $T_{\rm lin} = 0$. Conversely, if $\{\xi \in \mathbb R : \nu(\xi) > 0\}$ has positive Lebesgue measure, the integral of a strictly positive kernel against a nonnegative function that is positive on a set of positive measure is strictly positive, so $b_m > 0$ for every $m \ge 0$; $b_m \le 1$ since $\nu \le 1$. $\square$

### Lemma 2 (PROVED: Odd reflection to full-line convolution)
*Assume row-update balance holds at every $n \ge 0$: $\sum_{m=0}^\infty (\Delta_{|n-m|} - \Delta_{n+m+1}) b_m = 0$ for all $n \ge 0$. Define the odd reflection $\tilde b \in \ell^\infty(\mathbb Z)$ by*
$$\tilde b_m := \begin{cases} b_m, & m \ge 0, \\ -b_{-m-1}, & m \le -1. \end{cases}$$
*Then $(\Delta * \tilde b)_n := \sum_{m \in \mathbb Z} \Delta_{n-m} \tilde b_m = 0$ for every $n \in \mathbb Z$.*

*Proof.* Since $\Delta \in \ell^1(\mathbb Z)$ and $\tilde b \in \ell^\infty(\mathbb Z)$, the convolution sum converges absolutely for every $n \in \mathbb Z$. For $n \ge 0$, reindexing $m \le -1$ via $m' = -m - 1 \ge 0$ gives $n - m = n + m' + 1$ and $\tilde b_m = -b_{m'}$, while for $m \ge 0$, $\Delta_{n-m} = \Delta_{|n-m|}$ because $\Delta$ is even. Thus
$$(\Delta * \tilde b)_n = \sum_{m=0}^\infty \Delta_{|n-m|} b_m - \sum_{m'=0}^\infty \Delta_{n+m'+1} b_{m'} = \sum_{m=0}^\infty (\Delta_{|n-m|} - \Delta_{n+m+1}) b_m = 0.$$
For $n < 0$, write $n = -1 - k$ with $k \ge 0$. Substituting $m = -1 - m'$ and using $\Delta_{-j} = \Delta_j$ and $\tilde b_{-1-m'} = -\tilde b_{m'}$ yields
$$(\Delta * \tilde b)_{-1-k} = \sum_{m' \in \mathbb Z} \Delta_{-1-k - (-1-m')} \tilde b_{-1-m'} = -\sum_{m' \in \mathbb Z} \Delta_{k - m'} \tilde b_{m'} = -(\Delta * \tilde b)_k = 0. \quad \square$$

### Lemma 3 (PROVED: Centered slope bound and $\ell^2$ difference annihilation)
*Define $d_m := \tilde b_m - \tilde b_{m-1}$ for $m \in \mathbb Z$. Then $d_{-m} = d_m$, $d_0 = 2 b_0$, $d \in \ell^2(\mathbb Z)$, $(\Delta * d)_n = 0$ for all $n \in \mathbb Z$, and on $\mathbb T = \mathbb R/(2\pi\mathbb Z)$ the continuous function $\hat\Delta(\theta) := \sum_{j \in \mathbb Z} \Delta_j e^{-ij\theta}$ and $\hat d \in L^2(\mathbb T)$ satisfy*
$$\hat\Delta(\theta)\,\hat d(\theta) = 0 \qquad \text{for Lebesgue-a.e. } \theta \in (0, 2\pi).$$

*Proof.* For $m = 0$, $d_0 = \tilde b_0 - \tilde b_{-1} = b_0 - (-b_0) = 2b_0$. For $m \ge 1$, $d_{-m} = \tilde b_{-m} - \tilde b_{-m-1} = (-b_{m-1}) - (-b_m) = b_m - b_{m-1} = d_m$, so $d$ is even.

To see $d \in \ell^2(\mathbb Z)$, differentiate $b(s) = \frac{1}{\pi}\int_{-\infty}^\infty \frac{s}{s^2+u^2} r(u)\,du$ under the integral (justified for $s > 0$ because $\left|\frac{\partial}{\partial s}\frac{s}{s^2+u^2}\right| = \frac{|u^2 - s^2|}{(s^2+u^2)^2} \le \frac{1}{s^2+u^2}$):
$$|s\,b'(s)| \le \frac{1}{\pi}\int_{-\infty}^\infty \frac{s|u^2 - s^2|}{(s^2+u^2)^2} r(u)\,du \le \frac{1}{\pi}\int_{-\infty}^\infty \frac{s}{s^2+u^2} r(u)\,du = b(s) \le 1$$
(`G3X/RIGOR.md:42`, `../FINITE-ENERGY-PAPER/replay/CENTERED-GAP/RIGOR.md:27`). Hence $|\frac{d}{ds}b(s)| \le \frac{1}{s}$ for all $s > 0$. By the mean value theorem and $w_m \le s_m \le w_m + D_*$, for every $m \ge 1$:
$$|d_m| = |b(s_m) - b(s_{m-1})| \le \frac{|s_m - s_{m-1}|}{\min(s_m, s_{m-1})} \le \frac{w_m + D_* - w_{m-1}}{w_{m-1}} = \frac{2 + D_*}{2m - 1}.$$
(On the unique centered fixed-point branch of `../FINITE-ENERGY-PAPER/replay/CENTERED-GAP/RIGOR.md:27`, one even has $\frac{w_{m-1}}{w_m} b_{m-1} \le b_m \le \frac{w_m}{w_{m-1}} b_{m-1}$, giving the sharper bound $|d_m| \le \frac{2}{2m-1} b_m$.) Because $\sum_{m=1}^\infty (2m-1)^{-2} < \infty$ and $d_{-m} = d_m$, we obtain $d \in \ell^2(\mathbb Z)$.

Since $\Delta \in \ell^1(\mathbb Z)$ and $\tilde b \in \ell^\infty(\mathbb Z)$, absolute convergence justifies splitting the backward difference:
$$(\Delta * d)_n = \sum_{m \in \mathbb Z} \Delta_{n-m} \tilde b_m - \sum_{m \in \mathbb Z} \Delta_{n-m} \tilde b_{m-1} = (\Delta * \tilde b)_n - (\Delta * \tilde b)_{n-1} = 0 \qquad (\forall\, n \in \mathbb Z).$$
Because $\Delta \in \ell^1(\mathbb Z)$ and $d \in \ell^2(\mathbb Z)$, Young's convolution inequality places $\Delta * d \in \ell^2(\mathbb Z)$ with $L^2(\mathbb T)$ Fourier transform $\hat\Delta(\theta)\hat d(\theta)$ (where $\hat\Delta \in C(\mathbb T)$ by Weierstrass M-test). Plancherel's theorem yields $\hat\Delta(\theta)\hat d(\theta) = 0$ for a.e. $\theta \in (0, 2\pi)$. $\square$

### Lemma 4 (PROVED: Holomorphic extension of $\hat\Delta$ and vanishing of all $\Delta_j$)
*Suppose $\nu \not\equiv 0$ (positive Lebesgue measure support). Then $\hat\Delta(\theta) = 0$ for all $\theta \in [0, 2\pi]$, and consequently $\Delta_j = 0$ for every $j \in \mathbb Z$.*

*Proof.* For any $E > 0$ and $\alpha_E := E / (2\pi\tau) > 0$, Poisson summation (`../../PHYS-Q2/RIGOR.md:94` with $t = \alpha_E^2$, noting $\pi - |\theta_{\bmod [-\pi,\pi]}| = \pm(\pi - \theta)$ on $[0, 2\pi]$ and $\cosh$ is even) gives the uniformly convergent series on $[0, 2\pi]$:
$$\sum_{j \in \mathbb Z} \frac{e^{-ij\theta}}{E^2 + (2\pi\tau j)^2} = \frac{1}{(2\pi\tau)^2}\sum_{j \in \mathbb Z} \frac{e^{-ij\theta}}{\alpha_E^2 + j^2} = \frac{1}{2\tau E}\frac{\cosh\bigl(\alpha_E(\pi - \theta)\bigr)}{\sinh(\alpha_E \pi)} \qquad (\theta \in [0, 2\pi]).$$
(Equivalently, computing the Fourier coefficients $\frac{1}{2\pi}\int_0^{2\pi} \frac{1}{2\tau E}\frac{\cosh(\alpha_E(\pi-\theta))}{\sinh(\alpha_E\pi)} e^{ij\theta}\,d\theta$ by two integrations by parts reproduces $(E^2 + (2\pi\tau j)^2)^{-1}$ for all $j \in \mathbb Z$.)

For any $z = \theta + i\eta$ in the open vertical strip $S := \{z \in \mathbb C : 0 < \Re z < 2\pi\}$, we have $|\pi - \theta| < \pi$ and $|\cosh(a + ib)|^2 = \cosh^2 a - \sin^2 b \le \cosh^2 a$, whence
$$\left|\frac{1}{2\tau E}\frac{\cosh\bigl(\alpha_E(\pi - z)\bigr)}{\sinh(\alpha_E \pi)}\right| \le \frac{1}{2\tau E}\frac{\cosh(\alpha_E \pi)}{\sinh(\alpha_E \pi)} = \frac{1}{2\tau E}\coth(\alpha_E \pi).$$
Since $(1 + x)\sinh x - x\cosh x = \sinh x - x e^{-x} = \frac{1}{2}e^{-x}(e^{2x} - 1 - 2x) \ge 0$ for all $x > 0$, we have $\coth x \le 1 + x^{-1}$, and therefore uniformly for all $z \in S$ and all $E > 0$:
$$\left|\frac{1}{2\tau E}\frac{\cosh\bigl(\alpha_E(\pi - z)\bigr)}{\sinh(\alpha_E \pi)}\right| \le \frac{1}{E^2} + \frac{1}{2\tau E} \le \frac{3}{2 E^2} + \frac{1}{8\tau^2}.$$
Because $\int_{(0,\infty)} (1 + E^{-2})\,d|\delta|(E) < \infty$, Fubini's theorem applies to both the series sum for $\theta \in [0, 2\pi]$ and to any closed triangle $\Gamma \subset S$. Thus
$$F(z) := \int_{(0,\infty)} \frac{1}{2\tau E}\frac{\cosh\bigl(\alpha_E(\pi - z)\bigr)}{\sinh(\alpha_E \pi)}\,d\delta(E)$$
is holomorphic on the connected open strip $S$ (by Morera's theorem) and satisfies $F(\theta) = \hat\Delta(\theta)$ for all $\theta \in (0, 2\pi)$.

Now suppose for contradiction that $F \not\equiv 0$ on $S$. By the identity theorem for holomorphic functions on the connected open set $S$, $F$ can have only finitely many zeros in each compact interval $[1/k, 2\pi - 1/k] \subset S$ ($k \ge 2$). Taking the union over $k \ge 2$, the zero set $Z := (0, 2\pi) \cap F^{-1}(\{0\})$ is at most countable and therefore has Lebesgue measure zero. By Lemma 3, $\hat\Delta(\theta)\hat d(\theta) = F(\theta)\hat d(\theta) = 0$ for a.e. $\theta \in (0, 2\pi)$; since $F(\theta) \ne 0$ for a.e. $\theta \in (0, 2\pi)$, we are forced to have $\hat d(\theta) = 0$ for a.e. $\theta \in (0, 2\pi)$. By uniqueness of $L^2(\mathbb T)$ Fourier coefficients, $d_m = 0$ for all $m \in \mathbb Z$. In particular $2 b_0 = d_0 = 0$, contradicting Lemma 1 ($b_0 > 0$ for $\nu \not\equiv 0$).

Hence $F \equiv 0$ on $S$, so $\hat\Delta(\theta) = 0$ for all $\theta \in (0, 2\pi)$ (and by continuity on $[0, 2\pi]$). Inverting the Fourier series gives $\Delta_j = \frac{1}{2\pi}\int_0^{2\pi} \hat\Delta(\theta)e^{ij\theta}\,d\theta = 0$ for every $j \in \mathbb Z$. $\square$

### Lemma 5 (PROVED: Measure-level collapse $d\delta = 0$)
*If $\Delta_j = 0$ for all $j \ge 1$ (or all $j \ge 0$), then $d\delta = 0$ as a Borel measure on $(0,\infty)$, and consequently $(K_j \mathbf 1)_x = (K_j \mathbf 1)_y$ at every temperature $\tau' > 0$ and every $j \ge 0$.*

*Proof.* Define for $\Re w > 0$
$$g(w) := \int_{(0,\infty)} \frac{d\delta(E)}{E^2 + (2\pi\tau w)^2}.$$
Write $E^2 + (2\pi\tau w)^2 = (E + i2\pi\tau w)(E - i2\pi\tau w)$. For $w = u + iv$ with $u = \Re w > 0$ and $E > 0$, the imaginary parts of the two factors are $\pm 2\pi\tau u$, so both factors have modulus at least $2\pi\tau u$, giving
$$|E^2 + (2\pi\tau w)^2| \ge (2\pi\tau \Re w)^2 \qquad (\forall\, E > 0,\ \Re w > 0).$$
In particular, on $\{\Re w \ge 1/2\}$, setting $w = \frac{1}{2} + \zeta$ with $\Re \zeta \ge 0$, we have $|E^2 + (2\pi\tau(\frac{1}{2} + \zeta))^2| \ge (\pi\tau)^2 > 0$ uniformly in $E > 0$. By Fubini + Morera, $h(\zeta) := g(\frac{1}{2} + \zeta)$ is holomorphic on $\{\Re \zeta > 0\}$ and uniformly bounded: $|h(\zeta)| \le \|\delta\|_{\rm TV}/(\pi\tau)^2$.

Under the Cayley biholomorphism $\zeta = \frac{1+z}{1-z}$ ($z = \frac{\zeta-1}{\zeta+1}$) from $\mathbb D = \{|z| < 1\}$ onto $\{\Re \zeta > 0\}$, the function $H(z) := h(\frac{1+z}{1-z})$ belongs to $H^\infty(\mathbb D)$. Since $g(j) = \Delta_j = 0$ for every integer $j \ge 1$, $h(j - \frac{1}{2}) = 0$ for all $j \ge 1$, so $H(z_j) = 0$ at
$$z_j = \frac{j - 3/2}{j + 1/2} = 1 - \frac{2}{j + 1/2} \in \mathbb D \qquad (j \ge 1).$$
Because $\sum_{j=2}^\infty (1 - |z_j|) = \sum_{j=2}^\infty \frac{2}{j + 1/2} = +\infty$, the Blaschke condition for nonzero $H^\infty(\mathbb D)$ functions is violated, forcing $H \equiv 0$ on $\mathbb D$, hence $g(w) \equiv 0$ for $\Re w > 1/2$, and by analytic continuation for all $\Re w > 0$.

Restricting to $w > 0$ and setting $s = (2\pi\tau w)^2 > 0$, push forward $d\delta$ along $E \mapsto x = E^2$ to the finite signed Borel measure $\tilde\delta := (E \mapsto E^2)_* \delta$ on $(0,\infty)$, so that
$$\int_{(0,\infty)} \frac{d\tilde\delta(x)}{x + s} = 0 \qquad (\forall\, s > 0).$$
Since $\frac{k!}{(x+1)^{k+1}} \le k!$ for $x > 0$ and $\|\tilde\delta\|_{\rm TV} = \|\delta\|_{\rm TV} < \infty$, dominated convergence allows differentiating $k$ times with respect to $s$ at $s = 1$, giving
$$\int_{(0,\infty)} \frac{d\tilde\delta(x)}{(x + 1)^{k+1}} = 0 \qquad (\forall\, k \ge 0).$$
Under the homeomorphism $u = (x+1)^{-1} : (0,\infty) \xrightarrow{\sim} (0, 1)$, let $\sigma := u_* \tilde\delta$ be the pushforward finite signed Borel measure on $[0, 1]$ (with $\sigma(\{0\}) = \sigma(\{1\}) = 0$). Then $\int_{[0,1]} u^{k+1}\,d\sigma(u) = 0$ for all $k \ge 0$, so $\int_{[0,1]} u\,P(u)\,d\sigma(u) = 0$ for every polynomial $P$. By Weierstrass approximation, $\int_{[0,1]} f(u)\,d\sigma(u) = 0$ for every $f \in C([0,1])$ with $f(0) = 0$; since $\sigma(\{0\}) = 0$, inner/outer regularity of finite Borel measures on $[0, 1]$ forces $\sigma = 0$, hence $\tilde\delta = 0$, hence $d\delta = 0$ on $(0,\infty)$. $\square$

### Theorem 1 and Corollary 1 (PROVED: Collapse & $S = C_\infty$)
*In the finite-channel ($d \ge 2$, in particular $d = 2$) centered model of §1 with common bounded even normalized DOS $\nu$ and a common centered branch $s_{n,x} = s_n$ at some temperature $\tau > 0$:*
1. *(Collapse Theorem.) If $\nu \not\equiv 0$ and operational row-update balance holds between every pair $(x, y)$ at every Matsubara row $n \ge 0$, then $(K_j \mathbf 1)_x = \bar K_j$ independent of $x$ for every $j \ge 0$, and $\sum_z \eta_z\, d\mathfrak m_{xz} = \sum_z \eta_z\, d\mathfrak m_{yz}$ on $(0,\infty)$.*
2. *(Sharpness on the Reduced Conjecture class.) On the full Reduced Conjecture class of `../SHARPFLAT/RIGOR.md:57-59` (common bounded even normalized DOS $\nu$, common centered branch $s_{n,1} = s_{n,2} = s_n$, and all-row update balance), $k_B T_{\rm lin} < C_\infty \sqrt{\rho}$ whenever $\rho > 0$ (and $T_{\rm lin} = 0$ if $\rho = 0$ or $\nu = 0$ a.e.), and the sharp supremum is $S = C_\infty$ (non-attained).*

*Proof.* Part 1 is immediate by applying Lemmas 1–5 to every pair $(x, y) \in X^2$. For Part 2, if $\nu = 0$ a.e., Lemma 1 gives $T_{\rm lin} = 0$. If $\nu \not\equiv 0$, Part 1 yields $(K_j \mathbf 1)_x = \bar K_j$ for every $j \ge 0$, placing the system directly inside the hypotheses of `../../../G3COMBINE/RIGOR.md:27` (with finite positive total weight $0 < \sum_x \eta_x < \infty$, common normalized even DOS $\nu$, and common centered branch $s_n$). Hence $k_B T_{\rm lin} < C_\infty\sqrt\rho$ for every $\rho > 0$. The lower endpoint $S \ge C_\infty$ holds on the same class via the inherited single-channel or equal-channel wide-box soft limit (`../SHARP/RESULT.md:20`, `G3X/RIGOR.md:95`). $\square$

**Remark (Non-centered / unequal-DOS observation and limits of the argument).** Notice that the proof of Lemmas 2–5 used the centered normal equation only to guarantee $b_m > 0$ and $b_m - b_{m-1} \in \ell^2(\mathbb Z_{\ge 1})$: any pair of channels sharing a common $b_{m,x} = b_{m,y} = b_m$ with $b_0 \ne 0$ and $b_m - b_{m-1} \in \ell^2(\mathbb Z_{\ge 1})$ likewise collapses. By contrast, if $b_m$ did not have $\ell^2$ differences (for example, a hypothetical non-decaying oscillatory sequence $b_m = \cos((m+1/2)\theta_0)$—which cannot arise on a centered branch), $\hat d$ would concentrate at $\pm\theta_0$ and could vanish on the remaining zeros of $\hat\Delta$.

---

## 3. Non-factorized `G3COMBINE Q2` witness (PROVED and CERTIFIED)

Although Theorem 1 shows that all-row update balance collapses to `../../../G3COMBINE/RIGOR.md:27` (and thus yields **no** class strictly larger than `G3COMBINE Q2`), `G3COMBINE Q2` itself is strictly larger than the factorized $d\mathfrak m = P\,d\mu$ class of `../SHARPFLAT/RIGOR.md:44-50`.

Take $d = 2$ with unequal DOS heights $\eta = (1, 3)$, $\tau = 1/(2\pi)$ (so $(2\pi\tau)^2 = 1$), and reciprocal positive glue measures on $(0,\infty)$:
$$d\mathfrak m_{11} = 3\,\delta_{E=1}, \qquad d\mathfrak m_{12} = d\mathfrak m_{21} = \delta_{E=2}, \qquad d\mathfrak m_{22} = \delta_{E=1} + \frac{2}{3}\,\delta_{E=2}.$$
1. **Exact transfer-by-transfer row balance for all $j \ge 0$ (`G3COMBINE Q2` satisfied):**
   $$\eta_1 d\mathfrak m_{11} + \eta_2 d\mathfrak m_{12} = 3\,\delta_{E=1} + 3\,\delta_{E=2} = \eta_1 d\mathfrak m_{21} + \eta_2 d\mathfrak m_{22},$$
   so for every $j \ge 0$, $(K_j\mathbf 1)_1 = (K_j\mathbf 1)_2 = \frac{3}{1+j^2} + \frac{3}{4+j^2}$.
2. **Non-factorization ($d\mathfrak m \ne P\,d\mu$):**
   The $2\times 2$ kernel entries of $K_0$ and $K_1$ are not proportional:
   $$K^{\rm ker}_0 = \begin{pmatrix} 3 & 1/4 \\ 1/4 & 7/6 \end{pmatrix}, \qquad K^{\rm ker}_1 = \begin{pmatrix} 3/2 & 1/5 \\ 1/5 & 19/30 \end{pmatrix},$$
   with $\det \begin{pmatrix} 3 & 1/4 \\ 3/2 & 1/5 \end{pmatrix} = \frac{3}{5} - \frac{3}{8} = \frac{9}{40} \ne 0$. Hence no $P\,d\mu$ factorization exists.
3. **Moment operator norm in $\ell^2(\eta)$:**
   The moment kernel matrix is $\mathcal M^{\rm ker} = \begin{pmatrix} 3 & 1 \\ 1 & 5/3 \end{pmatrix}$, acting via $(\mathcal M h)_x = \sum_y \mathcal M^{\rm ker}_{xy} \eta_y h_y$. On $\ell^2(\eta)$, $\mathcal M$ is self-adjoint, positivity-preserving, and satisfies $\mathcal M \mathbf 1 = (6, 6)^{\mathsf T} = 6\mathbf 1$, so by the Schur test $\rho = \|\mathcal M\|_{\ell^2(\eta)\to\ell^2(\eta)} = 6$.

---

## 4. Finite-row ($n = 0$) non-implication witness (PROVED and CERTIFIED)

To show that balancing **all** Matsubara rows $n \ge 0$ in Theorem 1 cannot be weakened to balancing finitely many rows (even at $n = 0$), take $d = 2$, $\eta = (1, 1)$, $\tau = 1/(2\pi)$ ($(2\pi\tau)^2 = 1$), and common box DOS $r(u) = \mathbf 1_{|u| \le 1}$ ($\nu(\xi) = \mathbf 1_{|\xi| \le 1/2}$), so
$$b(s) = \frac{2}{\pi}\arctan\!\left(\frac{1}{s}\right).$$
Let $d\mathfrak m_{11} = \delta_{E=1}$, $d\mathfrak m_{12} = d\mathfrak m_{21} = 0$, and $d\mathfrak m_{22} = c_2\,\delta_{E=2}$ with $c_2 > 0$ chosen below. Because $d\mathfrak m_{12} = 0$, Channel 1 decouples in the normal equation and admits a unique centered branch $s_n = w_n + \sum_{m=0}^\infty P_{nm}(1) b(s_m)$ satisfying $w_n \le s_n \le w_n + R_1$, where $P_{nm}(t) := \frac{1}{t + (n-m)^2} - \frac{1}{t + (n+m+1)^2}$ and $R_1 = \sum_{j \in \mathbb Z} \frac{1}{1+j^2} = \pi\coth\pi$.

For each $n \ge 0$ and $t \in \{1, 4\}$, put $F_n(t) := \sum_{m=0}^\infty P_{nm}(t)\, b(s_m) > 0$, and set
$$c_2 := \frac{F_0(1)}{F_0(4)} > 0.$$
Then:
- **Exact row-$0$ balance holds along $b_m = b(s_m)$:** $\sum_{m=0}^\infty \bigl(\Delta_{|0-m|} - \Delta_{m+1}\bigr) b_m = F_0(1) - c_2 F_0(4) = 0$.
- **Transfer balance and row-$1$ balance both fail (CERTIFIED in `replay.py` via 192-bit `python-flint` Arb antitone fixed-point bounds + exact infinite-tail remainder $\sum_{m=M}^\infty P_{nm}(t) = \sum_{j=M-n}^{M+n} (t+j^2)^{-1}$):**
  - $c_2 \in [6.26499 \pm 5\times 10^{-6}]$,
  - $\Delta_0 = 1 - c_2/4 \in [-0.56625 \pm 5\times 10^{-6}] < 0$,
  - $\Delta_1 = 1/2 - c_2/5 \in [-0.75300 \pm 5\times 10^{-6}] < 0$,
  - Row-$1$ mismatch $F_1(1) - c_2 F_1(4) \in [-0.24018 \pm 6\times 10^{-6}] < 0$.

Thus $s'_{0,1} = s'_{0,2} = s_0$ holds on Channel 1's actual centered branch, while both transfer balance ($\Delta_0, \Delta_1 \ne 0$) and row-$1$ update balance fail. (In this decoupled witness $s_{1,2} \ne s_{1,1}$, illustrating why all-row equality $s'_{n,1} = s'_{n,2}$ for all $n \ge 0$ is needed to collapse $d\delta$.)

---

## 5. Replay verification and mutant guards

`replay.py` verifies all finite rational constants, the exact `SHARPFLAT-REVIEW/REVIEW.md` Finding 1–3 numerical/algebraic relations ($C_\infty < C_{\rm route,cent} < C_{\rm cent} < C_{\rm caus}$, $w_0/w_1 = 1/3$, $w_1/w_0 = 3$), the non-factorized `G3COMBINE Q2` witness (§3), and, via 192-bit `python-flint` Arb interval arithmetic, the Poisson summation kernel identity of Lemma 4, the $\coth x \le 1 + x^{-1}$ bound, the Blaschke divergence lower bound, and the certified $n = 0$ finite-row witness (§4) with exact tail enclosures.

Base invocation exits `0`. `--all-mutants` tests 12 genuine mathematical mutants (each corrupting a real constant, matrix entry, Arb sign/enclosure, or witness balance identity — never scope booleans) and exits `0` if and only if every mutant is rejected.
