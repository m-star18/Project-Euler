cnt = 0
check = 100
for i in range(1, check):
    for j in range(1, check):
        if len(str(pow(i, j))) == j:
            cnt += 1
print(cnt)
