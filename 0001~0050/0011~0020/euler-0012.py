def make_divisors(n):
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 1
            if i != n // i:
                res += 1
    return res


v = 1
cnt = 1
while make_divisors(v) < 500:
    cnt += 1
    v += cnt
print(v)
