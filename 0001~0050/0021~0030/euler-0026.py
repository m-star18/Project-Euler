ans = 0
check = 1000
for d in range(1, check):
    v = 10 ** len(str(d))
    s = ''
    for i in range(check * 2):
        u, v = divmod(v, d)
        if v % d == 0:
            break
        s += str(u)
        v *= 10
    else:
        for i in range(1, check):
            if s[:i] == s[i:i * 2]:
                if ans < i:
                    ans = i + 1
                break
print(ans)
