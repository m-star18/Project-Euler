from itertools import accumulate


def eratosthenes(n):
    prime_list = [True] * (n + 1)
    prime_list[0] = False
    prime_list[1] = False
    for i, prime in enumerate(prime_list[2:int(n ** 0.5) + 1]):
        if prime:
            for j in range(pow(i + 2, 2), n + 1, i + 2):
                prime_list[j] = False
    return prime_list


limit = 10 ** 6
prime_check = eratosthenes(limit)
prime_list = []
for i, prime in enumerate(prime_check):
    if prime:
        prime_list.append(i)
cumsum = list(accumulate(prime_list))
ans = 0
check = -1
for i, bf in enumerate(cumsum):
    memo = 0
    idx = 0
    for j, af in enumerate(cumsum[i + 1:]):
        tmp = af - bf
        if tmp >= limit:
            break
        if prime_check[tmp]:
            memo = tmp
            idx = j
    if idx > check:
        check = idx
        ans = memo
print(ans)
