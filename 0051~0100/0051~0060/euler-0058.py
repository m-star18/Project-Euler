def prime_check(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


tmp = 1
limit = 10 ** 6
cnt = 0
memo = 2
for n in range(limit):
    for i in range(4):
        tmp += memo
        if prime_check(tmp):
            cnt += 1
    memo += 2
    if cnt * 10 < (n + 1) * 4 + 1:
        print(memo - 1)
        break
