ans = 0
for i in range(2, 5 * 10 ** 5):
    v = 0
    for n in list(str(i)):
        v += pow(int(n), 5)
    ans += i if i == v else 0
print(ans)
