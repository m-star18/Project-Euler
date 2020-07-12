def check(n):
    n = str(n)
    return all(n[2 * x] == str(x + 1) for x in range(9))


limit = int(19293949596979899 ** 0.5) + 1
for i in range(limit, 0, -2):
    if check(i * i):
        print(i * 10)
        break
