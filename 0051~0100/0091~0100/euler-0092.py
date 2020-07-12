from functools import lru_cache


@lru_cache()
def check(n):
    if n == 1:
        return False
    if n == 89:
        return True
    return check(sum(int(x) ** 2 for x in str(n)))


limit = 10 ** 7
print(sum(1 for i in range(1, limit) if check(i)))
