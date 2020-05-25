ans = 0
check = list(map(str, list(range(1, 10))))
for i in range(10 ** 6):
    memo = ''
    for j in range(1, 10):
        memo += str(i * j)
        if len(memo) >= 9:
            if sorted(memo) == check and j > 1:
                ans = max(ans, int(memo))
            break
print(ans)
