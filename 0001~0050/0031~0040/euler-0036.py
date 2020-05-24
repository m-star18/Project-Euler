def check(n):
    for bf, af in zip(n, n[::-1]):
        if bf != af:
            return False
    return True


limit = 10 ** 6
print(sum(i if check(str(i)) and check(bin(i)[2:]) else 0 for i in range(limit)))
