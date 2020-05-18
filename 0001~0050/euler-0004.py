min_v = 10 ** 2
max_v = 10 ** 3
ans = 0
for i in range(min_v, max_v):
    for j in range(min_v, max_v):
        v = str(i * j)
        for b, f in zip(v, v[::-1]):
            if b != f:
                break
        else:
            ans = max(ans, int(v))
print(ans)
