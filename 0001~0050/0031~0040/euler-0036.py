limit = 10 ** 6
ans = 0
for i in range(limit):
    for bf, af in zip(str(i), str(i)[::-1]):
        if bf != af:
            break
    else:
        j = bin(i)[2:]
        for bf, af in zip(j, j[::-1]):
            if bf != af:
                break
        else:
            ans += i
print(ans)
