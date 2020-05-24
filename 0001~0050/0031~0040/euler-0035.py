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
prime_list = eratosthenes(limit)
cnt = 1
for n in range(1, limit, 2):
    n = str(n)
    for j in range(len(n)):
        if not prime_list[int(n[j:] + n[:j])]:
            break
    else:
        cnt += 1
print(cnt)
