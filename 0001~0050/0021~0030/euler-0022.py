data = open('names.txt', 'r').readline().split(sep=',')
for i, d in enumerate(data):
    data[i] = d.replace('"', '')
data.sort()
print(sum((i + 1) * sum(ord(m) - 64 for m in d) for i, d in enumerate(data)))
