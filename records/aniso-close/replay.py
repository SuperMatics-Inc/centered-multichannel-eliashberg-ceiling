"""Exact three-stage frozen-weight reserve; no floating-point arithmetic.
Run python -B replay.py [--reserve P/Q] [--mutant NAME]. Reviewed analytic reduction.
"""
from argparse import ArgumentParser
from fractions import Fraction as F

MUTANTS = ("budget", "tail", "identity", "denominator", "cone", "coverage", "reserve", "strict", "head-divisor", "ratio-index")
p = ArgumentParser(description=__doc__)
p.add_argument("--mutant", choices=MUTANTS)
p.add_argument("--reserve", type=F, default=F(3189, 10000))
args = p.parse_args()
bad = args.mutant


def need(ok, label):
    if not ok:
        print("REJECT:", label)
        raise SystemExit(1)


Q = 10**12
M = 20
D = args.reserve
REPORT = D if bad == "strict" else F(318, 1000)
need(REPORT < D, "strict reporting margin")


def down(x):
    return x.numerator * Q // x.denominator


def up(x):
    return -((-x.numerator * Q) // x.denominator)


def small(z: F, pairs: int = 16) -> tuple[F, F]:
    need(abs(z) <= F(1, 2), "atan reduction domain")
    a = abs(z)
    terms = sum(((-1 if j % 2 else 1) * a**(2*j+1) / (2*j+1) for j in range(2*pairs)), F(0))
    lo, hi = terms, terms + a**(4*pairs+1)/(4*pairs+1)
    return (lo, hi) if z >= 0 else (-hi, -lo)


a, b = small(F(1, 5))
c, e = small(F(1, 239), 8)
PI_L, PI_H = 16*a-4*e, 16*b-4*c
HALF_L, HALF_H = small(F(1, 2))
need(F(3141592653589793, 10**15) < PI_L < PI_H < F(3141592653589794, 10**15), "pi enclosure")


def atan(x: F) -> tuple[F, F]:
    if x > 1:
        lo, hi = atan(1/x)
        return PI_L/2-hi, PI_H/2-lo
    if x > F(1, 3):
        lo, hi = small((2*x-1)/(x+2))
        return HALF_L+lo, HALF_H+hi
    return small(x)


# Every extracted pair is counted once, independently of completion budgets.
extracted = {(m, k) for m in (1, 2) for k in range(m+1, M+1)}
extracted |= {(k, m) for m, k in tuple(extracted)}
rows = []
for n in range(1, M+1):
    row = sum(F(1, (2*k+1)*(n+k+1)**2) for k in range(1, M+1) if (n, k) not in extracted)
    row += F(0) if bad == "tail" else F(1, (2*M+3)*(n+M+1))
    reference = sum(F(1, (2*k+1)*(n+k+1)**2) for k in range(1, M+1) if (n, k) not in extracted) + F(1, 43*(n+21))
    need(row >= reference, "infinite reflected tail enclosure")
    rows.append(up(row))
full = sum(F(1, (2*k+1)*(k+2)**2) for k in range(1, 17)) + F(1, 1024)
need(full < F(33, 500), "full Schur tail")
alpha_ext = 1-D-F(33, 500)
far = sum(F(1, (2*k+1)*k*k*(k+1)**2) for k in range(1, 21)) + F(1, 8*20**4)
need(far < F(7, 75), "far tail integral")
need(F(9, 17)-F(7, 75)/alpha_ext > D, "far allocation reserve")
need(F(2, 5)+F(3, 4)*(alpha_ext/8-F(1, 9))/alpha_ext > D, "intermediate allocation reserve")
need(F(1, 3)+F(4, 9)*(alpha_ext/6-F(1, 9))/alpha_ext > D, "high energy reserve")
need(alpha_ext/8 > F(1, 25) and F(43, 3)*alpha_ext > F(2, 43), "exterior completion signs")

# Generic direct square-completion identity, including the new m=2 stage.
for m in range(3):
    for k in range(m+1, M+1):
        wm, wk = 2*m+1, 2*k+1
        t, r, A = F(1, 11), F(7, 10), F(3, 5)
        p0 = 1/(t+(k-m)**2)-1/(t+(k+m+1)**2)
        s0 = 1/(t+(k-m)**2)+1/(t+(k+m+1)**2)
        factor = 2 if bad == "identity" else 4
        need(s0*s0-p0*p0 == factor*p0/(wm*wk), "difference-of-squares identity")
        direct = r*p0/(2*wm)-s0*s0/(4*wm*wk*(A+p0/(2*r*wk)))
        den_sign = -1 if bad == "denominator" else 1
        rational = 2*p0*(r*wk*A-F(2, wm*wk))/(4*wm*wk*A+den_sign*2*wm*p0/r)
        need(direct == rational, "generic completion denominator")

# Construct tangent lines and enumerate ALL pairwise intersections, not just adjacent ones.
lines = {}
for k in range(1, M+1):
    wk = 2*k+1
    ls = [(F(1, wk), F(0)), (F(wk), F(1-wk))]
    for x in (4, 5, 6, 8, 10, 12, 16, 24):
        _, axh = atan(F(x))
        ayl, _ = atan(F(x, wk))
        slope = F(wk*(1+x*x), wk*wk+x*x)
        intercept_lo = 2*ayl/PI_H-slope*2*axh/PI_L
        intercept = F(intercept_lo.numerator*10**8//intercept_lo.denominator, 10**8)
        if bad == "cone":
            intercept = F(1, 10)
        need(intercept <= intercept_lo and intercept <= 0 and slope+intercept <= 1, "valid Poisson tangent")
        ls.append((slope, intercept))
    lines[k] = ls
knots = [F(0), F(1, 2), F(3, 4)] + [F(i, 200) for i in range(160, 201)]
intervals = list(zip(knots, knots[1:]))
need(sum(hi-lo for lo, hi in intervals) == 1, "full head domain")
breaks = set()
for ls in lines.values():
    for i, (a, b) in enumerate(ls):
        for c, e in ls[i+1:]:
            if a != c:
                breaks.add((e-b)/(a-c))
tables = []
for lo, hi in intervals:
    points = [hi] if lo == 0 else [lo, hi]+sorted(x for x in breaks if lo < x < hi)
    if lo == 0:
        need(all(a*hi+b <= hi/F(2*k+1) for k, ls in lines.items() for a, b in ls[1:]), "first interval endpoint suffices")
    tables.append([(down(1/x), [down(max(a*x+b for a, b in lines[k])/x) for k in range(1, M+1)]) for x in points])


def lower_head(base, gains, table):
    return min((base*iv + sum(gains[k-1]*rat[0 if bad == "ratio-index" else k-1] for k in range(1, M+1)))//Q for iv, rat in table)


def unassisted_head(base, upper):
    divisor = upper*upper if bad == "head-divisor" else upper
    return base*divisor.denominator//divisor.numerator


# Base-path contracts: independently expand rational objectives on every real table.
probe_base = down(F(7, 11))
probe_gains = [down(F(k*k+1, 97)) for k in range(1, M+1)]
for table in tables:
    reference = min(F(probe_base, Q)*F(iv, Q)+sum((F(g, Q)*F(ratio, Q) for g, ratio in zip(probe_gains, ratios)), F(0)) for iv, ratios in table)
    need(lower_head(probe_base, probe_gains, table) == down(reference), "per-frequency head reference")
for lo, hi in intervals:
    endpoints = [hi] if lo == 0 else [lo, hi]
    reference = min(F(probe_base, Q)/head for head in endpoints)
    need(unassisted_head(probe_base, hi) == down(reference), "unassisted head reference")


def cell(rl, rh, tl, th, target):
    rem = [Q-up(target)-q for q in rows]
    if min(rem) <= 0:
        return False
    budget = [[0]*(M+1) for _ in range(3)]
    for k in range(1, M+1):
        shares = (F(1), F(0), F(0)) if k == 1 else ((F(7, 10), F(3, 10), F(0)) if k == 2 else (F(13, 20), F(1, 4), F(1, 10)))
        if bad == "budget":
            shares = (F(1), F(1), F(1))
        need(sum(shares) == 1, "disjoint bare budget")
        for m in range(3):
            budget[m][k] = rem[k-1]*shares[m].numerator//shares[m].denominator
        need(sum(budget[m][k] for m in range(3)) <= rem[k-1], "rounded budget not overspent")
    rlo = [down(rl), down(1/rh)]
    rinvhi = [up(1/rl), up(rh)]
    enhancement = [[[0]*M for _ in range(3)] for _ in range(2)]
    for direction in range(2):
        for m in (1, 2):
            wm = 2*m+1
            for k in range(m+1, M+1):
                wk = 2*k+1
                pl = down(F(wm*wk, 1)/((th+(k-m)**2)*(th+(k+m+1)**2)))
                A = budget[m][k]  # Own b_m <= 1: conservative, correct at every stage.
                num = rlo[direction]*wk*A-up(F(2, wm*wk))*Q
                if num <= 0:
                    return False
                den = 4*wm*wk*A*Q+2*wm*rinvhi[direction]*pl
                enhancement[direction][m][k-1] = 2*pl*num//den
    phi = [[[0]*len(tables) for _ in tables] for _ in range(2)]
    for direction in range(2):
        for own, table in enumerate(tables):
            A = [0]*(M+1)
            for m in range(1, M+1):
                if m <= 2:
                    gains = enhancement[1-direction][m]
                    A[m] = lower_head(budget[0][m], gains, table)
                else:
                    A[m] = unassisted_head(budget[0][m], intervals[own][1])
            terms, negative = [0]*M, 0
            for k in range(1, M+1):
                wk = 2*k+1
                num = rlo[direction]*wk*A[k]-up(F(2, wk))*Q
                if num >= 0:
                    pl = down(F(wk, 1)/((th+k*k)*(th+(k+1)**2)))
                    den = 4*wk*A[k]*Q+2*rinvhi[direction]*pl
                    terms[k-1] = 2*pl*num//den
                else:
                    ph = up(F(wk, 1)/((tl+k*k)*(tl+(k+1)**2)))
                    negative += wk*(2*ph*num//(4*wk*A[k]*Q))
            for opposite, ot in enumerate(tables):
                value = lower_head(Q-up(target), terms, ot)+negative
                if direction == 0:
                    phi[0][own][opposite] = value
                else:
                    phi[1][opposite][own] = value
    mid = (rl+rh)/2
    for a in range(len(tables)):
        for b in range(len(tables)):
            x, y = F(phi[0][a][b], Q), F(phi[1][a][b], Q)
            if min(x, y) <= 0:
                return False
            slope = y-x/mid**2
            affine = 2*x/mid+(rl if slope >= 0 else rh)*slope
            if affine+2*tl*(1+tl)*x*y < 2:
                return False
    return True


target = F(1, 2) if bad == "reserve" else D
stack = [(F(1), F(2 if bad == "coverage" else 3), F(0), F(1, 2), 0)]
leaves, depth_max, area = 0, 0, F(0)
while stack:
    rl, rh, tl, th, depth = stack.pop()
    if cell(rl, rh, tl, th, target):
        area += (rh-rl)*(th-tl)
        leaves += 1
        depth_max = max(depth_max, depth)
        continue
    if depth >= 30:
        rc, tc = (rl+rh)/2, (tl+th)/2
        print(f"LIMIT: r={rc}; t={tc}; point_predicate={cell(rc, rc, tc, tc, target)}; edge_point_predicate={cell(F(1), F(1), F(0), F(0), target)}")
    need(depth < 30, "unresolved compact box")
    rm, tm = (rl+rh)/2, (tl+th)/2
    if rh-rl > F(3, 2)*(th-tl):
        stack.extend([(rl, rm, tl, th, depth+1), (rm, rh, tl, th, depth+1)])
    else:
        stack.extend([(rl, rh, tl, tm, depth+1), (rl, rh, tm, th, depth+1)])
need(area == 1, "complete closed-rectangle cover")
print(f"EXACT primary three-stage cover: d={D}; leaves={leaves}; depth={depth_max}; area={area}; heads={len(tables)}")
print(f"C_bound = sqrt({2*(1-D)})/(2*pi); C_report = sqrt({2*(1-REPORT)})/(2*pi)")
