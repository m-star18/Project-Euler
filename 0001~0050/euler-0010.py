def makePrimeChecker(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    return isPrime


limit = 2 * 10 ** 6
ans = 0
for i, v in enumerate(makePrimeChecker(limit)):
    ans += i if v else 0
print(ans)
