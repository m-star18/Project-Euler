ans = 11
digit1_9 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
digit10_19 = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
digit20_90 = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
for i in range(1, 1000):
    if i >= 100:
        if i % 100 == 0:
            ans -= 3
        ans += 10 + digit1_9[i // 100]
    i %= 100
    if 11 <= i <= 19:
        ans += digit10_19[i - 10]
    else:
        ans += digit20_90[i // 10] + digit1_9[i % 10]
print(ans)
