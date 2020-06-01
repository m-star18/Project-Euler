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
for num in range(56004, limit):
    if not prime_check[num]:
        continue
    num = str(num)
    for check in range(10):
        check = str(check)
        m = ''
        for n in num:
            m += (n if n != check else '?')
        if '?' not in m:
            continue
        cnt = 0
        for i in range(10):
            if i == 0 and m[0] == '?':
                continue
            if prime_check[int(m.replace('?', str(i)))]:
                cnt += 1
        if cnt >= 8:
            print(num)
            exit()
