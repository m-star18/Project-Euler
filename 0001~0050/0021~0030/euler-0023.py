def make_divisors(n):
    res = -n
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += i
            if i != n // i:
                res += n // i

    # divisors.sort()
    return res


limit = 28123
ans = 0
memo = []
check1 = set(range(1, limit))
check2 = set()
for i in range(1, limit):
    if i < make_divisors(i):
        memo.append(i)
for i, a in enumerate(memo):
    for b in memo[i:]:
        if a + b >= limit:
            break
        check2.add(a + b)
print(sum(check1 - check2))
