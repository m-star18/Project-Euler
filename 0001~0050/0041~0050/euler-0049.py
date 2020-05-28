def eratosthenes(n):
    prime_list = [True] * (n + 1)
    prime_list[0] = False
    prime_list[1] = False
    for i, prime in enumerate(prime_list[2:int(n ** 0.5) + 1]):
        if prime:
            for j in range(pow(i + 2, 2), n + 1, i + 2):
                prime_list[j] = False
    return prime_list


limit = 10 ** 4
prime_list = eratosthenes(limit)
for i, prime in enumerate(prime_list[limit // 10:limit]):
    i += limit // 10
    if prime:
        prime1 = sorted(list(str(i)))
        for j in range(limit // 10, limit):
            prime3 = i + j * 2
            prime2 = prime3 - j
            if prime3 >= limit:
                break
            if prime_list[prime2] and prime_list[prime3]:
                if prime1 == sorted(list(str(prime2))) == sorted(list(str(prime3))):
                    print(f'{i}{prime2}{prime3}')
