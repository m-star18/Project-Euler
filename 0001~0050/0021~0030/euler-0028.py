ans = 1
v = 1
for i in range(2, 1001, 2):
    for j in range(4):
        v += i
        ans += v
print(ans)
