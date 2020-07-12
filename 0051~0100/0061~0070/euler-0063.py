cnt = 0
check = 100
for i in range(check):
    for j in range(check):
        if len(str(pow(i, j))) == j:
            cnt += 1
print(cnt)
