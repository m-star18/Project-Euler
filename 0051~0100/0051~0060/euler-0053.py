from operator import mul
from functools import reduce


def comb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


cnt = 0
limit = 101
for n in range(23, limit):
    for r in range(1, n):
        if comb(n, r) >= 10 ** 6:
            cnt += 1
print(cnt)
