def make_divisors(n):
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += i
            if i != n // i:
                res += n // i

    return res


ans = 0
for a in range(1, 10 ** 4):
    b = make_divisors(a) - a
    if a + b == make_divisors(b) and a != b:
        ans += a
print(ans)
