from math import gcd

ans = 1
for next in range(1, 21):
    ans *= next // gcd(ans, next)
print(ans)
