fibonacci = [1, 2]
ans = 2
while fibonacci[-1] + fibonacci[-2] < 4 * 10 ** 6:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    ans += fibonacci[-1] if fibonacci[-1] % 2 == 0 else 0
print(ans)
