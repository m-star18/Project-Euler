fib = [1, 2]
ans = 2
while fib[-1] + fib[-2] < 4 * 10 ** 6:
    fib.append(fib[-1] + fib[-2])
    ans += fib[-1] if fib[-1] % 2 == 0 else 0
print(ans)
