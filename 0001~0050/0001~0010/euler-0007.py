def eratosthenes(limit):
    from math import sqrt
    if limit == 1:
        limit -= 1
    numbers = [i for i in range(2, limit + 1)]
    prime_list = []
    for i in range(limit):
        prime = min(numbers)
        if prime > sqrt(limit):
            break
        prime_list.append(prime)
        for j in range(limit):
            if j >= len(numbers):
                break
            if numbers[j] % prime == 0:
                numbers.pop(j)
                continue
    for num in numbers:
        prime_list.append(num)

    return prime_list


prime_list = eratosthenes(2 * 10 ** 5)
print(prime_list[10 ** 4])
