def eratosthenes(n):
    prime_list = [True] * (n + 1)
    prime_list[0] = False
    prime_list[1] = False
    for i, prime in enumerate(prime_list[2:int(n ** 0.5) + 1]):
        if prime:
            for j in range(pow(i + 2, 2), n + 1, i + 2):
                prime_list[j] = False
    return prime_list


limit = 10 ** 5
prime_list = []
check = [True] * (limit + 1)
for i, prime in enumerate(eratosthenes(limit)):
    if i % 2 == 0 or prime:
        check[i] = False
    if prime:
        prime_list.append(i)
check[1] = False
for prime in prime_list:
    for i in range(1, int(pow(limit, 0.5)) + 1):
        v = prime + 2 * i ** 2
        if v > limit:
            break
        check[v] = False
print(check.index(True))
