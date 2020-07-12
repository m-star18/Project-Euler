cnt = 0
limit = 10 ** 7
for i in range(1, limit):
    while i != 1 and i != 89:
        i = sum(int(x) ** 2 for x in str(i))
    if i == 89:
        cnt += 1
print(cnt)
