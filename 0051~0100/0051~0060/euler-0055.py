import functools


@functools.lru_cache()
def lychrel(n, cnt):
    global ans
    if cnt >= 50:
        ans += 1
    else:
        n += int(str(n)[::-1])
        nn = str(n)[::-1]
        if str(n) != nn:
            lychrel(n, cnt + 1)


ans = 0
limit = 10 ** 4
for i in range(limit):
    lychrel(i, 0)
print(ans)
