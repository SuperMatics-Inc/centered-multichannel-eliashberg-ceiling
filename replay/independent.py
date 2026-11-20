"""Independent exact 4-way full-domain verification of reserve 159/500.
This uses the separate FINITE-ENERGY implementation, not replay.py imports.
It has its own atan enclosure, tail summation and signed cell evaluator.
Run: python -B independent.py [--mutant NAME]
"""
MUTANTS = ("pin", "strict-budget", "coverage-gap", "reserve-too-high", "completion-sign", "tangent-intercept")
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

demand = require

# 1. Independent rational atan and pi bounds (12-pair / 8-pair Leibniz enclosure)
def atan_leibniz(z: Fraction, pairs: int) -> tuple[Fraction, Fraction]:
    demand(0 <= z <= Fraction(1, 2), "atan_leibniz nonneg domain")
    if z == 0:
        return Fraction(0), Fraction(0)
    z2 = z * z
    cur = z
    acc = Fraction(0)
    for k in range(2 * pairs):
        term = cur / (2 * k + 1)
        acc = acc + term if (k % 2 == 0) else acc - term
        cur *= z2
    return acc, acc + cur / (4 * pairs + 1)


a5_l, a5_h = atan_leibniz(Fraction(1, 5), 12)
a239_l, a239_h = atan_leibniz(Fraction(1, 239), 8)
PI_L = 16 * a5_l - 4 * a239_h
PI_H = 16 * a5_h - 4 * a239_l
AH_L, AH_H = atan_leibniz(Fraction(1, 2), 16)


def atan_pos(x: Fraction) -> tuple[Fraction, Fraction]:
    demand(x > 0, "atan_pos argument")
    if x > 1:
        li, hi = atan_pos(Fraction(1) / x)
        return Fraction(1, 2) * PI_L - hi, Fraction(1, 2) * PI_H - li
    if x > Fraction(1, 3):
        u = (2 * x - 1) / (x + 2)
        lu, hu = atan_leibniz(abs(u), 14)
        return (AH_L + lu, AH_H + hu) if u >= 0 else (AH_L - hu, AH_H - lu)
    return atan_leibniz(x, 14)


for m in range(1, 21):
    wm = 2 * m + 1
    r_v = Fraction(7, 10)
    t_v = Fraction(1, 11)
    a_v = Fraction(3, 5)
    p0 = Fraction(wm, (t_v + m * m) * (t_v + (m + 1) ** 2))
    s0 = Fraction(1, t_v + m * m) + Fraction(1, t_v + (m + 1) ** 2)
    sgn = -1 if bad == "completion-sign" else 1
    direct0 = r_v * p0 / 2 - s0 * s0 / (4 * wm * (a_v + p0 / (2 * r_v * wm)))
    rat0 = (2 * p0 * (r_v * wm * a_v - Fraction(2, wm))) / (4 * wm * a_v + sgn * 2 * (1 / r_v) * p0)
    demand(direct0 == rat0, "independent stage-0 completion rationalization")
    if m >= 2:
        p1 = Fraction(3 * wm, (t_v + (m - 1) ** 2) * (t_v + (m + 2) ** 2))
        s1 = Fraction(1, t_v + (m - 1) ** 2) + Fraction(1, t_v + (m + 2) ** 2)
        b1_v = Fraction(1, 7)
        direct1 = r_v * p1 / 6 - s1 * s1 / (12 * wm * (b1_v + p1 / (2 * r_v * wm)))
        rat1 = (2 * p1 * (r_v * wm * b1_v - Fraction(2, 3 * wm))) / (12 * wm * b1_v + sgn * 6 * (1 / r_v) * p1)
        demand(direct1 == rat1, "independent stage-1 completion rationalization")

# 2. Independent 4-way quadtree covering of the FULL [1/3, 3] x [0, 1/2] domain (area = 4/3)
Q = 10**12
M = 20
w = [2 * m + 1 for m in range(1, M + 1)]


def q_floor(x: Fraction) -> int:
    return (x.numerator * Q) // x.denominator


def q_ceil(x: Fraction) -> int:
    return -((-x.numerator * Q) // x.denominator)


q_red: list[int] = []
for n in range(1, M + 1):
    s = Fraction(1, 43 * (n + 21))
    for m in range(1, 21):
        if (n == 1 and m >= 2) or (m == 1 and n >= 2):
            continue
        s += Fraction(1, (2 * m + 1) * ((n + m + 1) ** 2))
    q_red.append(q_ceil(s))

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


def make_tables(xi_list: list[int]) -> list[tuple[list[int], list[list[int]]]]:
    slopes = [[Fraction(1, 2 * m + 1) for m in range(1, M + 1)]]
    intercepts = [[Fraction(0) for _ in range(M)]]
    Q_c = 10**8
    for xi in xi_list:
        _, ax_hi = atan_pos(Fraction(xi))
        b0_hi = (2 * ax_hi) / PI_L
        l_row: list[Fraction] = []
        c_row: list[Fraction] = []
        for m in range(1, M + 1):
            wm = 2 * m + 1
            lam = Fraction(wm * (1 + xi * xi), wm * wm + xi * xi)
            am_lo, _ = atan_pos(Fraction(xi, wm))
            bm_lo = (2 * am_lo) / PI_H
            c_lo = bm_lo - lam * b0_hi
            c_rat = Fraction(1, 10) if bad == "tangent-intercept" else Fraction((c_lo.numerator * Q_c) // c_lo.denominator, Q_c)
            demand(c_rat <= 0 and lam + c_rat <= 1, "certified tangent intercept nonpositive")
            l_row.append(lam)
            c_row.append(c_rat)
        slopes.append(l_row)
        intercepts.append(c_row)
    slopes.append([Fraction(2 * m + 1) for m in range(1, M + 1)])
    intercepts.append([Fraction(-(2 * m)) for m in range(1, M + 1)])

    bkpts: set[Fraction] = set()
    L = len(slopes)
    for l in range(L - 1):
        for m in range(M):
            bkpts.add(-(intercepts[l + 1][m] - intercepts[l][m]) / (slopes[l + 1][m] - slopes[l][m]))
    s_bkpts = sorted(bkpts)
    tables: list[tuple[list[int], list[list[int]]]] = []
    for b_lo, b_hi in sub_ivs:
        pts = [b_hi] if b_lo == 0 else ([b_lo] + [pt for pt in s_bkpts if b_lo < pt < b_hi] + [b_hi])
        inv_p = [q_floor(Fraction(1) / pt) for pt in pts]
        ratio_cl = [[q_floor(max(slopes[l][m] * pt + intercepts[l][m] for l in range(L)) / pt) for m in range(M)] for pt in pts]
        tables.append((inv_p, ratio_cl))
    return tables


def cell_ok_full(
    r_lo: Fraction,
    r_hi: Fraction,
    t_lo: Fraction,
    t_hi: Fraction,
    dt: Fraction,
    split: Fraction,
    tables: list[tuple[list[int], list[list[int]]]],
) -> bool:
    one_m_dt = Q - q_ceil(dt)
    rem = [one_m_dt - q_red[m] for m in range(M)]
    alp_0 = [(rem[m] * split.numerator) // split.denominator for m in range(M)]
    bet_1 = [(rem[m] * (split.denominator - split.numerator)) // split.denominator for m in range(M)]
    alp_0[0] = rem[0]
    bet_1[0] = 0

    r_lo_i = q_floor(r_lo)
    r_hi_i = q_ceil(r_hi)
    ri_lo_i = q_floor(Fraction(1) / r_hi)
    ri_hi_i = q_ceil(Fraction(1) / r_lo)

    p_0k = [q_floor(Fraction(1) / (t_hi + k * k) - Fraction(1) / (t_hi + (k + 1) ** 2)) for k in range(1, M + 1)]
    p_0k_hi = [q_ceil(Fraction(1) / (t_lo + k * k) - Fraction(1) / (t_lo + (k + 1) ** 2)) for k in range(1, M + 1)]
    p_1k = [q_floor(Fraction(1) / (t_hi + (k - 1) ** 2) - Fraction(1) / (t_hi + (k + 2) ** 2)) for k in range(2, M + 1)]

    D_1k_X: list[int] = []
    D_1k_Y: list[int] = []
    for idx in range(M - 1):
        wm = w[idx + 1]
        b1 = bet_1[idx + 1]
        p1 = p_1k[idx]
        thresh = (2 * Q * Q + 3 * wm - 1) // (3 * wm)
        num_X = r_lo_i * wm * b1 - thresh
        num_Y = ri_lo_i * wm * b1 - thresh
        if num_X <= 0 or num_Y <= 0:
            return False
        D_1k_X.append((2 * p1 * num_X) // (12 * wm * b1 * Q + 6 * ri_hi_i * p1))
        D_1k_Y.append((2 * p1 * num_Y) // (12 * wm * b1 * Q + 6 * r_hi_i * p1))

    S = len(sub_ivs)
    t_alp_X1 = [
        min((alp_0[0] * tables[a][0][i] + sum(tables[a][1][i][m + 1] * D_1k_X[m] for m in range(M - 1))) // Q for i in range(len(tables[a][0])))
        for a in range(S)
    ]
    t_alp_Y1 = [
        min((alp_0[0] * tables[a][0][i] + sum(tables[a][1][i][m + 1] * D_1k_Y[m] for m in range(M - 1))) // Q for i in range(len(tables[a][0])))
        for a in range(S)
    ]

    Phi_X = [[0] * S for _ in range(S)]
    Phi_Y = [[0] * S for _ in range(S)]
    sign_den = -1 if bad == "completion-sign" else 1

    for a in range(S):
        b_hi = sub_ivs[a][1]
        D_0k_X: list[int] = []
        neg_X = 0
        for m in range(M):
            wm = w[m]
            ta = t_alp_Y1[a] if m == 0 else (alp_0[m] * b_hi.denominator) // b_hi.numerator
            thresh0 = (2 * Q * Q + wm - 1) // wm
            num = r_lo_i * wm * ta - thresh0
            if num >= 0:
                p0 = p_0k[m]
                den = 4 * wm * ta * Q + sign_den * 2 * ri_hi_i * p0
                demand(den > 0, "positive stage-0 completion denominator")
                D_0k_X.append((2 * p0 * num) // den)
            else:
                p0_h = p_0k_hi[m]
                neg_X += wm * ((2 * p0_h * num) // (4 * wm * ta * Q))
                D_0k_X.append(0)
        for b in range(S):
            inv_p, ratio_cl = tables[b]
            Phi_X[a][b] = min(
                (one_m_dt * inv_p[i] + sum(ratio_cl[i][m] * D_0k_X[m] for m in range(M))) // Q + neg_X for i in range(len(inv_p))
            )

    for b in range(S):
        c_hi = sub_ivs[b][1]
        D_0k_Y: list[int] = []
        neg_Y = 0
        for m in range(M):
            wm = w[m]
            ta = t_alp_X1[b] if m == 0 else (alp_0[m] * c_hi.denominator) // c_hi.numerator
            thresh0 = (2 * Q * Q + wm - 1) // wm
            num = ri_lo_i * wm * ta - thresh0
            if num >= 0:
                p0 = p_0k[m]
                den = 4 * wm * ta * Q + sign_den * 2 * r_hi_i * p0
                demand(den > 0, "positive stage-0 completion denominator")
                D_0k_Y.append((2 * p0 * num) // den)
            else:
                p0_h = p_0k_hi[m]
                neg_Y += wm * ((2 * p0_h * num) // (4 * wm * ta * Q))
                D_0k_Y.append(0)
        for a in range(S):
            inv_p, ratio_cl = tables[a]
            Phi_Y[a][b] = min(
                (one_m_dt * inv_p[i] + sum(ratio_cl[i][m] * D_0k_Y[m] for m in range(M))) // Q + neg_Y for i in range(len(inv_p))
            )

    r0 = Fraction(1, 2) * (r_lo + r_hi)
    r0_sq = r0 * r0
    two_t = 2 * t_lo * (1 + t_lo)
    for a in range(S):
        for b in range(S):
            px = Fraction(Phi_X[a][b], Q)
            py = Fraction(Phi_Y[a][b], Q)
            if px <= 0 or py <= 0:
                return False
            slope = py - px / r0_sq
            g_lo = 2 * px / r0 + (r_lo if slope >= 0 else r_hi) * slope
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
require((2*PI_H*c_cert_lo)**2 < Fraction(341, 250) < (2*PI_L*c_cert_hi)**2, "certified endpoint decimal enclosure")
require((2*PI_H*c_report_lo)**2 < Fraction(6821, 5000) < (2*PI_L*c_report_hi)**2, "reported endpoint decimal enclosure")
print("Exact endpoint enclosures:", c_cert_lo, c_cert_hi, c_report_lo, c_report_hi)

# Ordered adjacent intersections certify that no omitted line-switch
# breakpoint can minimize the convex envelope in inverse head weight.
# Independent tangent-intersection integrity calculation.
for m in range(1, M + 1):
    wm = 2*m + 1
    lines = [(Fraction(1, wm), Fraction(0))]
    for xi in xi_list:
        slope = Fraction(wm*(1 + xi*xi), wm*wm + xi*xi)
        _, ax_hi = atan_pos(Fraction(xi))
        am_lo, _ = atan_pos(Fraction(xi, wm))
        intercept = Fraction(((2*am_lo/PI_H - slope*2*ax_hi/PI_L)*10**8).__floor__(), 10**8)
        lines.append((slope, intercept))
    lines.append((Fraction(wm), Fraction(1 - wm)))
    crossings = [(lines[k][1] - lines[k+1][1])/(lines[k+1][0] - lines[k][0]) for k in range(len(lines)-1)]
    demand(all(x <= y for x, y in zip(crossings, crossings[1:])), "independent ordered tangent intersections")
    demand(all(a/2 + b <= Fraction(1, 2*wm) for a, b in lines[1:]), "independent first-interval basic tangent")
tables = make_tables(xi_list)
target = Fraction(1, 3) if bad == "reserve-too-high" else d_cert
r_end = Fraction(2 if bad == "coverage-gap" else 3)
stack = [(Fraction(1, 3), r_end, Fraction(0), Fraction(1, 2), 0)]
leaves = 0
max_depth = 0
area = Fraction(0)
while stack:
    r0, r1, tl, th, depth = stack.pop()
    if cell_ok_full(r0, r1, tl, th, target, Fraction(7, 10), tables):
        area += (r1 - r0)*(th - tl)
        leaves += 1
        max_depth = max(max_depth, depth)
        continue
    demand(depth < 12, "independent full-domain quadtree depth")
    rm = (r0 + r1)/2
    tm = (tl + th)/2
    stack.extend([(r0, rm, tl, tm, depth+1), (rm, r1, tl, tm, depth+1), (r0, rm, tm, th, depth+1), (rm, r1, tm, th, depth+1)])
demand(area == Fraction(4, 3), "independent full residual area")
print(f"CERTIFIED independent centered cover: reserve={d_cert}; leaves={leaves}; max_depth={max_depth}; area={area}; head_intervals={len(sub_ivs)}")
