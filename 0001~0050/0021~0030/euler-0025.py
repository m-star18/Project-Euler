fib = [1, 2]
cnt = 4
while len(str(fib[-1] + fib[-2])) < 1000:
    fib.append(fib[-1] + fib[-2])
    cnt += 1
print(cnt)
