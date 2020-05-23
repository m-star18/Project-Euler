check = list(map(str, list(range(1, 10))))
ans = set()
for i in range(2000):
    for j in range(1000):
        a = list(str(i)) + list(str(j)) + list(str(i * j))
        a.sort()
        if a == check:
            ans.add(i * j)
print(sum(ans))
