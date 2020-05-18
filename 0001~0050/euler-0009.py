from math import sqrt

for a in range(0, 1000):
    for b in range(a + 1, 1000):
        c = sqrt(a ** 2 + b ** 2)
        if a + b + c == 1000 and b < c:
            print(a * b * c)
            exit()
