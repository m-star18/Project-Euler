from itertools import product
from math import gcd

ans = [1, 1]
for i in range(10, 100):
    x = str(i)
    for j in range(i + 1, 100):
        if i % 10 == 0 or j % 10 == 0:
            continue
        y = str(j)
        for bit in product([0, 1], repeat=2):
            ii = i // 10 if bit[0] == 1 else i % 10
            jj = j // 10 if bit[1] == 1 else j % 10
            if x[bit[0]] == y[bit[1]] and i / j == ii / jj:
                ans[0] *= i
                ans[1] *= j
print(ans[1] // gcd(ans[0], ans[1]))
