data = open('triangle.txt', 'r').read()
size = 100
dp = [[0] * (size + 1) for _ in range(size + 1)]
idx = 0
for i in range(size):
    for j in range(i + 1):
        v = int(data[idx: idx + 2]) + dp[i][j]
        idx += 3
        dp[i + 1][j] = max(dp[i + 1][j], v)
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], v)
print(max(dp[-1]))
