def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    # divisors.sort()
    return divisors


ans = 0
for a in range(1, 10 ** 4):
    b = sum(make_divisors(a)) - a
    if a + b == sum(make_divisors(b)) and a != b:
        ans += a
print(ans)
