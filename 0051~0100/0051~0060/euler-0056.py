ans = 0
limit = 100
for a in range(1, limit):
    for b in range(limit):
        ab = list(map(int, list(str(pow(a, b)))))
        ans = max(ans, sum(ab))
print(ans)
