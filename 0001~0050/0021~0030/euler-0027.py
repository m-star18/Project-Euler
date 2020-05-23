def miller_rabin(n):
    # 確率的素数判定（ミラーラビン素数判定法）
    # 素数なら確実に True を返す、合成数なら確率的に False を返す
    # True が返ったなら恐らく素数で、False が返ったなら確実に合成数である
    # 参考: http://tjkendev.github.io/procon-library/python/prime/probabilistic.html
    # 検証: https://yukicoder.me/submissions/381948
    primes = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]  # 32bit: [2, 7, 61]
    if n == 2:
        return True
    if n <= 1 or n & 1 == 0:
        return False
    d = m1 = n - 1
    d //= d & -d
    for a in primes:
        if a >= n:
            return True
        t, y = d, pow(a, d, n)
        while t != m1 and y != 1 and y != m1:
            y = y * y % n
            t <<= 1
        if y != m1 and t & 1 == 0:
            return False
    return True


memo = 0
ans = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while miller_rabin(n ** 2 + a * n + b):
            n += 1
        if memo < n:
            memo = n
            ans = a * b
print(ans)
