from itertools import permutations

check = (2, 3, 5, 7, 11, 13, 17)
ans = 0
for comb in permutations((str(i) for i in range(10))):
    if comb[0] == '0':
        continue
    num = ''.join(comb)
    for i, prime in enumerate(check):
        if int(num[i + 1:i + 4]) % prime != 0:
            break
    else:
        ans += int(num)
print(ans)
