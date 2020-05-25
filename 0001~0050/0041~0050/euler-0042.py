from itertools import accumulate

cumsum = list(accumulate(list(range(100))))
al = {chr(m): i + 1 for i, m in enumerate(range(65, 91))}
data = open('words.txt', 'r').readline().split(sep=',')
cnt = 0
for i, d in enumerate(data):
    if sum(al[w] for w in d.replace('"', '')) in cumsum:
        cnt += 1
print(cnt)
