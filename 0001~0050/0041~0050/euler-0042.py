from itertools import accumulate

cumsum = list(accumulate(list(range(100))))
al = {chr(m): i + 1 for i, m in enumerate(range(65, 91))}
data = open('words.txt', 'r').readline().split(sep=',')
print(sum(1 if sum(al[w] for w in d.replace('"', '')) in cumsum else 0 for d in data))
