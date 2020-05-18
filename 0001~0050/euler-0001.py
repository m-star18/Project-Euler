import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

ans = 0
for i in range(1000):
    ans += i if i % 3 == 0 or i % 5 == 0 else 0
print(ans)
