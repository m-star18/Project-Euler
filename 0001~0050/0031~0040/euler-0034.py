from math import factorial

print(sum(v if v == sum(factorial(int(i)) for i in list(str(v))) else 0 for v in range(3, 10 ** 5)))
