from copy import deepcopy
from collections import defaultdict

ans = 0
maxi = 0
memo = defaultdict(int)
for i in range(10 ** 6 + 1, 0, -2):
    cnt = 0
    j = deepcopy(i)
    root = []
    while i != 1:
        if memo[i] != 0:
            cnt += memo[i]
            break
        root.append(i)
        cnt += 1
        if i % 2 == 0:
            i //= 2
        else:
            i *= 3
            i += 1
    if maxi < cnt:
        maxi = cnt
        ans = j
    for i, v in enumerate(root):
        memo[v] = cnt - i
print(ans)
