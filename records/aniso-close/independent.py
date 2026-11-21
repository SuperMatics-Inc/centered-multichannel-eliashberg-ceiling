"""Independent rational full-domain quadtree for the three-stage reserve.
No imports from replay.py; separate atan, partitions and exact completion evaluator.
"""
import argparse
from fractions import Fraction as R

NAMES = ("budget", "tail", "identity", "denominator", "cone", "coverage", "reserve", "strict", "head-divisor", "ratio-index")
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--mutant", choices=NAMES)
parser.add_argument("--reserve", type=R, default=R(3189, 10000))
options = parser.parse_args()
mutation = options.mutant


def check(condition, reason):
    if not condition:
        print("REJECT:", reason)
        raise SystemExit(1)


SCALE = 10**13
LAST = 20
reserve = options.reserve
reported = reserve if mutation == "strict" else R(159, 500)
check(reported < reserve, "strict onset reporting gap")


def floor(value):
    return value.numerator*SCALE//value.denominator


def ceil(value):
    return -((-value.numerator*SCALE)//value.denominator)


def series(z, count=36):
    check(0 <= z <= R(1, 2), "positive Taylor argument")
    power, total = z, R(0)
    for j in range(count):
        total += power/(2*j+1) if j % 2 == 0 else -power/(2*j+1)
        power *= z*z
    return total, total+power/(2*count+1)


l5, u5 = series(R(1, 5), 32)
l239, u239 = series(R(1, 239), 18)
pil, piu = 16*l5-4*u239, 16*u5-4*l239
lh, uh = series(R(1, 2), 40)
check(R(3141592653589793, 10**15) < pil < piu < R(3141592653589794, 10**15), "independent Machin enclosure")


def arctangent(value):
    if value > 1:
        l, u = arctangent(1/value)
        return pil/2-u, piu/2-l
    if value > R(1, 3):
        z = (2*value-1)/(value+2)
        l, u = series(abs(z))
        return (lh+l, uh+u) if z >= 0 else (lh-u, uh-l)
    return series(value)


# Test an expanded completion rather than the primary's rationalized implementation.
def residual(m, k, r, p, available):
    wm, wk = 2*m+1, 2*k+1
    sign = -1 if mutation == "denominator" else 1
    return p/(2*wm)*(r-(p+R(4, wm*wk))/(2*wk*available+sign*p/r))


for m in (0, 1, 2):
    for k in range(m+1, LAST+1):
        t, r, A = R(2, 17), R(4, 3), R(7, 13)
        p = 1/(t+(k-m)**2)-1/(t+(k+m+1)**2)
        s = 1/(t+(k-m)**2)+1/(t+(k+m+1)**2)
        coefficient = 2 if mutation == "identity" else 4
        check(s*s-p*p == R(coefficient, (2*m+1)*(2*k+1))*p, "new-stage factor four")
        direct = r*p/(2*(2*m+1))-s*s/(4*(2*m+1)*(2*k+1)*(A+p/(2*r*(2*k+1))))
        check(direct == residual(m, k, r, p, A), "expanded Schur complement")

# Independently enumerate remaining rows by testing min/max indices.
row_cost = []
for n in range(1, LAST+1):
    finite = sum(R(1, (2*k+1)*(n+k+1)**2) for k in range(1, LAST+1) if not (min(n, k) in (1, 2) and n != k))
    tail = R(0) if mutation == "tail" else R(1, (2*LAST+3)*(n+LAST+1))
    check(tail >= R(1, 43*(n+21)), "positive infinite remainder")
    row_cost.append(finite+tail)
cap = R(33, 500)
full_row = sum(R(1, (2*k+1)*(k+2)**2) for k in range(1, 17))+R(1, 4*16**2)
check(full_row < cap, "independent full row bound")
ext = 1-reserve-cap
far = sum(R(1, (2*k+1)*k*k*(k+1)**2) for k in range(1, LAST+1))+R(1, 8*LAST**4)
check(far < R(7, 75), "infinite far loss")
check(R(9, 17)-R(7, 75)/ext > reserve, "far r exterior")
check(R(2, 5)+R(3, 4)*(ext/8-R(1, 9))/ext > reserve, "near r exterior")
check(R(1, 3)+R(4, 9)*(ext/6-R(1, 9))/ext > reserve, "large t exterior")
check(ext/8 > R(1, 25) and R(43, 3)*ext > R(2, 43), "discarded completion signs")

# Separate outward tangent construction and all-intersection envelope minimization.
tangents = []
for k in range(1, LAST+1):
    wk = 2*k+1
    lines = [(R(1, wk), R(0)), (R(wk), R(1-wk))]
    for xi in (4, 5, 6, 8, 10, 12, 16, 24):
        ax_l, ax_u = arctangent(R(xi))
        ay_l, ay_u = arctangent(R(xi, wk))
        slope = R(wk*(1+xi*xi), wk*wk+xi*xi)
        lower = 2*ay_l/piu-slope*2*ax_u/pil
        intercept = R(lower.numerator*10**9//lower.denominator, 10**9)
        if mutation == "cone":
            intercept = R(1, 100)
        check(intercept <= lower and intercept <= 0 and slope+intercept <= 1, "outward tangent intercept")
        lines.append((slope, intercept))
    tangents.append(lines)
weight_knots = [R(0), R(1, 2), R(3, 4)]+[R(i, 200) for i in range(160, 201)]
weight_cells = list(zip(weight_knots[:-1], weight_knots[1:]))
check(sum(hi-lo for lo, hi in weight_cells) == 1, "full head domain")
intersections = set()
for lines in tangents:
    for a, b in lines:
        for c, d in lines:
            if a != c:
                intersections.add((d-b)/(a-c))
head_tables = []
for lo, hi in weight_cells:
    if lo == 0:
        check(all(a*hi+b <= hi/R(2*k+1) for k, lines in enumerate(tangents, 1) for a, b in lines[1:]), "zero head endpoint")
        pts = [hi]
    else:
        pts = [lo, hi]+sorted(v for v in intersections if lo < v < hi)
    head_tables.append([(floor(1/v), tuple(floor(max(a*v+b for a, b in lines)/v) for lines in tangents)) for v in pts])


def minimize(base, coeffs, table):
    return min((base*inv+sum(c*ratios[0 if mutation == "ratio-index" else index] for index, c in enumerate(coeffs)))//SCALE for inv, ratios in table)


def head_remainder(base, head):
    return base/(head*head if mutation == "head-divisor" else head)


# The exact inverse-weight objective is expanded separately in the base path.
test_base = floor(R(13, 29))
test_coefficients = [floor(R(k*k+3, 113)) for k in range(1, LAST+1)]
for table in head_tables:
    reference_values = []
    for inv, ratios in table:
        value = R(test_base*inv, SCALE*SCALE)
        for index in range(LAST):
            value += R(test_coefficients[index]*ratios[index], SCALE*SCALE)
        reference_values.append(value)
    check(minimize(test_base, test_coefficients, table) == floor(min(reference_values)), "independent frequency reference")
for left, right in weight_cells:
    endpoints = (right,) if left == 0 else (left, right)
    reference = min(R(test_base, SCALE)/head for head in endpoints)
    check(head_remainder(R(test_base, SCALE), right) == reference, "independent head remainder reference")


def enclosed(rl, ru, tl, tu, d):
    remainder = [1-d-q for q in row_cost]
    if min(remainder) <= 0:
        return False
    allocation = []
    for k, rem in enumerate(remainder, 1):
        fractions = (R(1), R(0), R(0)) if k == 1 else ((R(7, 10), R(3, 10), R(0)) if k == 2 else (R(13, 20), R(1, 4), R(1, 10)))
        if mutation == "budget":
            fractions = (R(1), R(1), R(1))
        check(sum(fractions) == 1, "disjoint stage allocations")
        allocation.append(tuple(rem*f for f in fractions))
    side_coefficients = []
    for r in (rl, 1/ru):
        gains = {1: [0]*LAST, 2: [0]*LAST}
        for m in (1, 2):
            for k in range(m+1, LAST+1):
                wm, wk = 2*m+1, 2*k+1
                A = allocation[k-1][m]
                if r*wk*A <= R(2, wm*wk):
                    return False
                pl = R(wm*wk, 1)/((tu+(k-m)**2)*(tu+(k+m+1)**2))
                gains[m][k-1] = floor(residual(m, k, r, pl, A))
        side_coefficients.append(gains)
    matrices = []
    for side, r in enumerate((rl, 1/ru)):
        matrix = []
        for index, table in enumerate(head_tables):
            A = []
            for k in range(1, LAST+1):
                base = floor(allocation[k-1][0])
                if k <= 2:
                    gain = side_coefficients[1-side][k]
                    A.append(R(minimize(base, gain, table), SCALE))
                else:
                    A.append(head_remainder(allocation[k-1][0], weight_cells[index][1]))
            positive, signed_loss = [], 0
            for k, available in enumerate(A, 1):
                wk = 2*k+1
                if r*wk*available >= R(2, wk):
                    pl = R(wk, 1)/((tu+k*k)*(tu+(k+1)**2))
                    positive.append(floor(residual(0, k, r, pl, available)))
                else:
                    ph = R(wk, 1)/((tl+k*k)*(tl+(k+1)**2))
                    # Drop the positive denominator term and use upper b_k/b_0 <= w_k.
                    signed_loss += floor(wk*ph/(2)*(r-R(2, wk*wk)/available))
                    positive.append(0)
            matrix.append([minimize(floor(1-d), positive, other)+signed_loss for other in head_tables])
        matrices.append(matrix)
    center = (rl+ru)/2
    for a in range(len(head_tables)):
        for b in range(len(head_tables)):
            x = R(matrices[0][a][b], SCALE)
            y = R(matrices[1][b][a], SCALE)
            if x <= 0 or y <= 0:
                return False
            derivative = y-x/(center*center)
            linear = 2*x/center+(rl if derivative >= 0 else ru)*derivative
            if linear+2*tl*(1+tl)*x*y < 2:
                return False
    return True


chosen = R(1, 2) if mutation == "reserve" else reserve
pending = [(R(1, 3), R(2 if mutation == "coverage" else 3), R(0), R(1, 2), 0)]
volume, count, deepest = R(0), 0, 0
while pending:
    left, right, bottom, top, level = pending.pop()
    if enclosed(left, right, bottom, top, chosen):
        volume += (right-left)*(top-bottom)
        count += 1
        deepest = max(deepest, level)
    else:
        if level >= 16:
            rc, tc = (left+right)/2, (bottom+top)/2
            print(f"LIMIT: r={rc}; t={tc}; point_predicate={enclosed(rc, rc, tc, tc, chosen)}; edge_point_predicate={enclosed(R(1), R(1), R(0), R(0), chosen)}")
        check(level < 16, "independent unresolved quadtree cell")
        middle, horizontal = (left+right)/2, (bottom+top)/2
        pending += [(a, b, c, e, level+1) for a, b in ((left, middle), (middle, right)) for c, e in ((bottom, horizontal), (horizontal, top))]
check(volume == R(4, 3), "full residual rectangle volume")
print(f"EXACT independent three-stage cover: d={reserve}; leaves={count}; depth={deepest}; area={volume}; heads={len(head_tables)}")
print(f"C_bound = sqrt({2*(1-reserve)})/(2*pi); C_report = sqrt({2*(1-reported)})/(2*pi)")
