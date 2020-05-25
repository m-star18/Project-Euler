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
ans = 0
cnt = 0
for i in range(11, limit, 2):
    i = str(i)
    for j in range(len(i)):
        if not (prime_list[int(i[:j + 1])] and prime_list[int(i[j:])]):
            break
    else:
        cnt += 1
        ans += int(i)
        if cnt == 11:
            break
print(ans)
