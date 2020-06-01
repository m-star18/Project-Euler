limit = 10 ** 6
for num in range(1, limit):
    check = list(str(num))
    check.sort()
    for i in range(2, 7):
        memo = list(str(num * i))
        if check != sorted(memo):
            break
    else:
        print(num)
        break
