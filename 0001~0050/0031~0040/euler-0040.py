import numpy as np

memo = ''
limit = 10 ** 6
for d in range(limit):
    memo += str(d)

print(np.prod([int(memo[10 ** i]) for i in range(7)]))
