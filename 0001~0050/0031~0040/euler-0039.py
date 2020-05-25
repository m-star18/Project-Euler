from math import sqrt
from collections import defaultdict

limit = 10 ** 3
dict = defaultdict(int)
for a in range(1, limit):
    for b in range(1, limit):
        c = sqrt(a ** 2 + b ** 2)
        p = a + b + c
        if c.is_integer() and p <= 1000:
            dict[int(p)] += 1
print(max(dict.items(), key=lambda x: int(x[1]))[0])
