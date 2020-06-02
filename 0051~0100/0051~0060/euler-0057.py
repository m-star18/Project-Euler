ans = 0
limit = 10 ** 3
n, d = 1, 1
for _ in range(limit):
    n, d = n + d * 2, n + d
    if len(str(n)) > len(str(d)):
        ans += 1
print(ans)
