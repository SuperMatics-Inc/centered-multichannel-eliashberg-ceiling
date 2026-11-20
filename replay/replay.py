"""Exact centered extension of FINITE-ENERGY: new reserve 159/500.
Copied arithmetic bodies retain the original rational floor/ceiling directions.
Source identities and analytic imports are pinned in source-pins.json.
Run: python -B replay.py [--mutant NAME]
"""
MUTANTS = ("pin", "strict-budget", "coverage-gap", "reserve-too-high", "hankel-tail", "centered-cone")
from argparse import ArgumentParser
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

p = ArgumentParser(description=__doc__)
p.add_argument("--mutant", choices=MUTANTS)
bad = p.parse_args().mutant


def require(ok, name):
    if not ok:
        raise SystemExit("REJECT: " + name)


root = Path(__file__).resolve().parent
pins = json.loads((root / "source-pins.json").read_text(encoding="utf-8"))["source_sha256"]
require(len(pins) == 13, "all inherited source pins present")
inherited = root.parent / "inherited"
for rel, expected in pins.items():
    target = root / rel
    if not target.exists():
        target = inherited / rel.split("../")[-1]
    observed = sha256(target.read_bytes()).hexdigest()
    if bad == "pin":
        expected = "0" * 64
    require(observed == expected, "inherited proof bytes " + rel)

# 1. Pure rational enclosing intervals for pi and arctan(x) via alternating Leibniz series
def atan_small_bounds(z: Fraction, n_pairs: int = 12) -> tuple[Fraction, Fraction]:
    require(abs(z) <= Fraction(1, 2), "atan_small_bounds domain")
    if z == 0:
        return Fraction(0), Fraction(0)
    sign = 1 if z > 0 else -1
    az = abs(z)
    z2 = az * az
    pow_z = az
    s = Fraction(0)
    for j in range(2 * n_pairs):
        term = pow_z / (2 * j + 1)
        if j % 2 == 0:
            s += term
        else:
            s -= term
        pow_z *= z2
    lo_pos = s
    hi_pos = s + pow_z / (4 * n_pairs + 1)
    return (lo_pos, hi_pos) if sign > 0 else (-hi_pos, -lo_pos)


a5_lo, a5_hi = atan_small_bounds(Fraction(1, 5), 14)
a239_lo, a239_hi = atan_small_bounds(Fraction(1, 239), 6)
PI_LO = 16 * a5_lo - 4 * a239_hi
PI_HI = 16 * a5_hi - 4 * a239_lo
require(
    Fraction(3141592653589793, 10**15) < PI_LO < PI_HI < Fraction(3141592653589794, 10**15),
    "Machin rational pi enclosure",
)
ATAN_HALF_LO, ATAN_HALF_HI = atan_small_bounds(Fraction(1, 2), 14)


def atan_pos_bounds(x: Fraction) -> tuple[Fraction, Fraction]:
    require(x > 0, "positive atan argument")
    if x > 1:
        lo_inv, hi_inv = atan_pos_bounds(Fraction(1) / x)
        return Fraction(1, 2) * PI_LO - hi_inv, Fraction(1, 2) * PI_HI - lo_inv
    if x > Fraction(1, 3):
        z = (2 * x - 1) / (x + 2)
        z_lo, z_hi = atan_small_bounds(z, 12)
        return ATAN_HALF_LO + z_lo, ATAN_HALF_HI + z_hi
    return atan_small_bounds(x, 12)
# 3. Exact rational bounds on the reduced Hankel tail (after extracting stage-0 and stage-1 cascades)
Q = 10**12
M = 20
w = [2 * m + 1 for m in range(1, M + 1)]


def f_floor(x: Fraction) -> int:
    return (x.numerator * Q) // x.denominator


def f_ceil(x: Fraction) -> int:
    return -((-x.numerator * Q) // x.denominator)


q_red_exact: list[Fraction] = []
for n in range(1, M + 1):
    s = Fraction(0)
    for m in range(1, 21):
        if (n == 1 and m >= 2) or (m == 1 and n >= 2):
            continue
        s += Fraction(1, (2 * m + 1) * ((n + m + 1) ** 2))
    if bad == "hankel-tail":
        s -= Fraction(1, 20)
    else:
        s += Fraction(1, 43 * (n + 21))
    q_red_exact.append(s)

require(
    q_red_exact[0] > Fraction(38, 1000) and q_red_exact[0] < Fraction(381, 10000),
    "reduced Hankel row-1 bound",
)
q_full_row1 = sum(Fraction(1, (2 * m + 1) * ((m + 2) ** 2)) for m in range(1, 17)) + Fraction(1, 4 * 16 * 16)
q_hankel_cap = Fraction(33, 500)
require(q_full_row1 < q_hankel_cap, "full Hankel Schur bound")
q_red_int = [f_ceil(q) for q in q_red_exact]

# 5. Certified rational tangent envelopes for causal and centered classes
sub_ivs = [
    (Fraction(0), Fraction(2, 3)),
    (Fraction(2, 3), Fraction(4, 5)),
    (Fraction(4, 5), Fraction(17, 20)),
    (Fraction(17, 20), Fraction(88, 100)),
    (Fraction(88, 100), Fraction(90, 100)),
    (Fraction(90, 100), Fraction(92, 100)),
    (Fraction(92, 100), Fraction(94, 100)),
    (Fraction(94, 100), Fraction(96, 100)),
    (Fraction(96, 100), Fraction(1)),
]


def make_certified_rational_tangents(xi_ints: list[int]) -> tuple[list[list[Fraction]], list[list[Fraction]]]:
    slopes = [[Fraction(1, 2 * m + 1) for m in range(1, M + 1)]]
    intercepts = [[Fraction(0) for _ in range(M)]]
    Q_c = 10**8
    for xi in xi_ints:
        ax_lo, ax_hi = atan_pos_bounds(Fraction(xi))
        b0_hi = (2 * ax_hi) / PI_LO
        lam_row: list[Fraction] = []
        c_row: list[Fraction] = []
        for m in range(1, M + 1):
            wm = 2 * m + 1
            lam = Fraction(2 * wm) if bad == "centered-cone" else Fraction(wm * (1 + xi * xi), wm * wm + xi * xi)
            am_lo, _ = atan_pos_bounds(Fraction(xi, wm))
            bm_lo = (2 * am_lo) / PI_HI
            c_exact_lo = bm_lo - lam * b0_hi
            c_rat = Fraction((c_exact_lo.numerator * Q_c) // c_exact_lo.denominator, Q_c)
            require(c_rat <= 0 and lam + c_rat <= 1, "admissible lower tangent line")
            lam_row.append(lam)
            c_row.append(c_rat)
        slopes.append(lam_row)
        intercepts.append(c_row)
    slopes.append([Fraction(2 * m + 1) for m in range(1, M + 1)])
    intercepts.append([Fraction(-(2 * m)) for m in range(1, M + 1)])
    return slopes, intercepts


def build_iv_int_tables(xi_ints: list[int]) -> list[tuple[list[int], list[list[int]]]]:
    slopes, intercepts = make_certified_rational_tangents(xi_ints)
    all_bkpts: set[Fraction] = set()
    L = len(slopes)
    for l in range(L - 1):
        for m in range(M):
            denom = slopes[l + 1][m] - slopes[l][m]
            require(denom > 0, "strictly increasing tangent slopes")
            b_int = -(intercepts[l + 1][m] - intercepts[l][m]) / denom
            all_bkpts.add(b_int)
    sorted_bkpts = sorted(all_bkpts)
    iv_tables: list[tuple[list[int], list[list[int]]]] = []
    for b_lo, b_hi in sub_ivs:
        pts = [b_hi] if b_lo == 0 else ([b_lo] + [pt for pt in sorted_bkpts if b_lo < pt < b_hi] + [b_hi])
        inv_p = [f_floor(Fraction(1) / pt) for pt in pts]
        ratio_cl = []
        for pt in pts:
            row = [f_floor(max(slopes[l][m] * pt + intercepts[l][m] for l in range(L)) / pt) for m in range(M)]
            ratio_cl.append(row)
        iv_tables.append((inv_p, ratio_cl))
    return iv_tables


def box_ok_int(
    r_lo: Fraction,
    r_hi: Fraction,
    t_lo: Fraction,
    t_hi: Fraction,
    dt: Fraction,
    split: Fraction,
    iv_tables: list[tuple[list[int], list[list[int]]]],
) -> bool:
    dt_ceil = f_ceil(dt)
    one_m_dt = Q - dt_ceil
    rem = [one_m_dt - q_red_int[m] for m in range(M)]
    if any(r_val <= 0 for r_val in rem):
        return False
    alp_0 = [(rem[m] * split.numerator) // split.denominator for m in range(M)]
    bet_1 = [(rem[m] * (split.denominator - split.numerator)) // split.denominator for m in range(M)]
    alp_0[0] = rem[0]
    bet_1[0] = 0

    r_lo_int = f_floor(r_lo)
    r_hi_int = f_ceil(r_hi)
    ri_lo_int = f_floor(Fraction(1) / r_hi)
    ri_hi_int = f_ceil(Fraction(1) / r_lo)

    p_0k = [f_floor(Fraction(1) / (t_hi + k * k) - Fraction(1) / (t_hi + (k + 1) ** 2)) for k in range(1, M + 1)]
    p_0k_hi = [f_ceil(Fraction(1) / (t_lo + k * k) - Fraction(1) / (t_lo + (k + 1) ** 2)) for k in range(1, M + 1)]
    p_1k = [f_floor(Fraction(1) / (t_hi + (k - 1) ** 2) - Fraction(1) / (t_hi + (k + 2) ** 2)) for k in range(2, M + 1)]

    D_1k_X: list[int] = []
    D_1k_Y: list[int] = []
    for idx in range(M - 1):
        wm = w[idx + 1]
        b1 = bet_1[idx + 1]
        p1 = p_1k[idx]
        thresh = (2 * Q * Q + 3 * wm - 1) // (3 * wm)
        num_X = r_lo_int * wm * b1 - thresh
        num_Y = ri_lo_int * wm * b1 - thresh
        if num_X <= 0 or num_Y <= 0:
            return False
        den_X = 12 * wm * b1 * Q + 6 * ri_hi_int * p1
        den_Y = 12 * wm * b1 * Q + 6 * r_hi_int * p1
        D_1k_X.append((2 * p1 * num_X) // den_X)
        D_1k_Y.append((2 * p1 * num_Y) // den_Y)

    S = len(sub_ivs)
    tilde_alp_X1_lo: list[int] = []
    tilde_alp_Y1_lo: list[int] = []
    for a in range(S):
        inv_p, ratio_cl = iv_tables[a]
        tilde_alp_X1_lo.append(
            min((alp_0[0] * inv_p[i] + sum(ratio_cl[i][m + 1] * D_1k_X[m] for m in range(M - 1))) // Q for i in range(len(inv_p)))
        )
        tilde_alp_Y1_lo.append(
            min((alp_0[0] * inv_p[i] + sum(ratio_cl[i][m + 1] * D_1k_Y[m] for m in range(M - 1))) // Q for i in range(len(inv_p)))
        )

    Phi_X_min = [[0] * S for _ in range(S)]
    Phi_Y_min = [[0] * S for _ in range(S)]

    for a in range(S):
        b_hi = sub_ivs[a][1]
        D_0k_X: list[int] = []
        for m in range(M):
            wm = w[m]
            ta = tilde_alp_Y1_lo[a] if m == 0 else (alp_0[m] * b_hi.denominator) // b_hi.numerator
            thresh0 = (2 * Q * Q + wm - 1) // wm
            num = r_lo_int * wm * ta - thresh0
            if num <= 0:
                return False
            p0 = p_0k[m]
            den = 4 * wm * ta * Q + 2 * ri_hi_int * p0
            D_0k_X.append((2 * p0 * num) // den)
        for b in range(S):
            inv_p, ratio_cl = iv_tables[b]
            Phi_X_min[a][b] = min(
                (one_m_dt * inv_p[i] + sum(ratio_cl[i][m] * D_0k_X[m] for m in range(M))) // Q for i in range(len(inv_p))
            )

    for b in range(S):
        c_hi = sub_ivs[b][1]
        D_0k_Y: list[int] = []
        neg_loss_Y = 0
        for m in range(M):
            wm = w[m]
            ta = tilde_alp_X1_lo[b] if m == 0 else (alp_0[m] * c_hi.denominator) // c_hi.numerator
            thresh0 = (2 * Q * Q + wm - 1) // wm
            num = ri_lo_int * wm * ta - thresh0
            if num >= 0:
                p0 = p_0k[m]
                den = 4 * wm * ta * Q + 2 * r_hi_int * p0
                D_0k_Y.append((2 * p0 * num) // den)
            else:
                p0_h = p_0k_hi[m]
                neg_loss_Y += wm * ((2 * p0_h * num) // (4 * wm * ta * Q))
                D_0k_Y.append(0)
        for a in range(S):
            inv_p, ratio_cl = iv_tables[a]
            Phi_Y_min[a][b] = min(
                (one_m_dt * inv_p[i] + sum(ratio_cl[i][m] * D_0k_Y[m] for m in range(M))) // Q + neg_loss_Y
                for i in range(len(inv_p))
            )

    r0 = Fraction(1, 2) * (r_lo + r_hi)
    r0_sq = r0 * r0
    two_t = 2 * t_lo * (1 + t_lo)
    for a in range(S):
        for b in range(S):
            px = Fraction(Phi_X_min[a][b], Q)
            py = Fraction(Phi_Y_min[a][b], Q)
            if px <= 0 or py <= 0:
                return False
            slope = py - px / r0_sq
            base = 2 * px / r0
            g_lo = base + (r_lo if slope >= 0 else r_hi) * slope
            if g_lo + two_t * px * py < 2:
                return False
    return True

# New head partition. Below 1/2 only the basic lower tangent is active.
knots = [Fraction(0), Fraction(1, 2), Fraction(3, 4)] + [Fraction(i, 200) for i in range(160, 201)]
sub_ivs = list(zip(knots, knots[1:]))
require(sub_ivs[0][0] == 0 and sub_ivs[-1][1] == 1, "head partition endpoints")
require(all(lo < hi for lo, hi in sub_ivs), "nonempty head subintervals")
require(all(sub_ivs[i][1] == sub_ivs[i + 1][0] for i in range(len(sub_ivs) - 1)), "gapless head partition")
xi_list = [4, 5, 6, 8, 10, 12, 16, 24]
d_cert = Fraction(159, 500)
d_report = d_cert if bad == "strict-budget" else Fraction(3179, 10000)
require(d_report < d_cert, "strict reporting margin")
require(2 * (1 - d_cert) == Fraction(341, 250), "certified squared numerator")
require(2 * (1 - d_report) == Fraction(6821, 5000), "reported squared numerator")
require(1 - (1 - d_cert) / (1 - d_report) == Fraction(1, 6821), "reported bare gap 1/6821")

# Exterior proofs reuse the analytic formulas, but with the NEW reserve.
alpha_ext = 1 - d_cert - Fraction(33, 500)
require(alpha_ext == Fraction(77, 125) and alpha_ext > Fraction(3, 5), "new exterior bare budget")
far_sum = sum(Fraction(1, (2*m + 1)*m*m*(m + 1)**2) for m in range(1, 21)) + Fraction(1, 8*20**4)
require(far_sum < Fraction(7, 75), "far-imbalance infinite tail")
require(Fraction(9, 17) - Fraction(7, 75)/alpha_ext > d_cert, "far-imbalance reserve")
require(Fraction(2, 5) + Fraction(3, 4)*(alpha_ext/8 - Fraction(1, 9))/alpha_ext > d_cert, "intermediate-imbalance reserve")
require(Fraction(1, 3) + Fraction(4, 9)*(alpha_ext/6 - Fraction(1, 9))/alpha_ext > d_cert, "large-energy reserve")
require(alpha_ext/8 > Fraction(1, 25), "exterior higher-tail sign")
require(Fraction(43, 3)*alpha_ext > Fraction(2, 43), "unretained positive stage-0 tails")

# Exact decimal enclosures. No float, Decimal, numpy or external packages.
c_cert_lo = Fraction(185877711471916, 10**15)
c_cert_hi = Fraction(185877711471917, 10**15)
c_report_lo = Fraction(185891338370617, 10**15)
c_report_hi = Fraction(185891338370618, 10**15)
require((2*PI_HI*c_cert_lo)**2 < Fraction(341, 250) < (2*PI_LO*c_cert_hi)**2, "certified endpoint decimal enclosure")
require((2*PI_HI*c_report_lo)**2 < Fraction(6821, 5000) < (2*PI_LO*c_report_hi)**2, "reported endpoint decimal enclosure")
print("Exact endpoint enclosures:", c_cert_lo, c_cert_hi, c_report_lo, c_report_hi)

# Ordered adjacent intersections certify that no omitted line-switch
# breakpoint can minimize the convex envelope in inverse head weight.
slopes, intercepts = make_certified_rational_tangents(xi_list)
for m in range(M):
    breaks = [-(intercepts[j+1][m] - intercepts[j][m])/(slopes[j+1][m] - slopes[j][m]) for j in range(len(slopes)-1)]
    require(all(a <= b for a, b in zip(breaks, breaks[1:])), "ordered tangent intersections")
    require(all(slopes[j][m]/2 + intercepts[j][m] <= Fraction(1, 2*w[m]) for j in range(1, len(slopes))), "basic tangent on first head interval")
iv_tables = build_iv_int_tables(xi_list)
target = Fraction(1, 3) if bad == "reserve-too-high" else d_cert
stack = [(Fraction(1), Fraction(2 if bad == "coverage-gap" else 3), Fraction(0), Fraction(1, 2), 0)]
leaves = 0
max_depth = 0
area = Fraction(0)
while stack:
    r0, r1, tl, th, depth = stack.pop()
    if box_ok_int(r0, r1, tl, th, target, Fraction(7, 10), iv_tables):
        leaves += 1
        max_depth = max(max_depth, depth)
        area += (r1 - r0)*(th - tl)
        continue
    require(depth < 22, "compact rectangle subdivision depth")
    rm = (r0 + r1)/2
    tm = (tl + th)/2
    if r1 - r0 > Fraction(3, 2)*(th - tl):
        stack.extend([(r0, rm, tl, th, depth+1), (rm, r1, tl, th, depth+1)])
    else:
        stack.extend([(r0, r1, tl, tm, depth+1), (r0, r1, tm, th, depth+1)])
require(area == 1, "complete residual area, no coverage gaps")
print(f"CERTIFIED primary centered cover: reserve={d_cert}; leaves={leaves}; max_depth={max_depth}; area={area}; head_intervals={len(sub_ivs)}")
