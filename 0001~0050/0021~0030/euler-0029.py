ab = set()
for a in range(2, 101):
    for b in range(2, 101):
        ab.add(pow(a, b))
print(len(ab))
