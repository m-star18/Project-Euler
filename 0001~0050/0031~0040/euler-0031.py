p = [1, 2, 5, 10, 20, 50, 100, 200]
dp = [0] * (p[-1] + 1)
dp[0] = 1
for pp in p:
    for i in range(p[-1] - pp + 1):
        dp[i + pp] += dp[i]
print(dp[p[-1]])
