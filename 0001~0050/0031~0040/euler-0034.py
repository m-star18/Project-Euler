fac = list(range(10))
fac[0] = 1
for i in range(9):
    fac[i + 1] *= fac[i]
ans = 0
for i in range(3, 10 ** 5):
    memo = 0
    for v in list(str(i)):
        memo += fac[int(v)]
    if i == memo:
        ans += i
print(ans)
