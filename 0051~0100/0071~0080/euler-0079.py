data = open('keylog.txt', 'r').read().split()
start = 10 ** 7
end = 10 ** 18
for check in range(start, end):
    check = str(check)
    for d in data:
        idx = 0
        for c in check:
            if c == d[idx]:
                idx += 1
                if len(d) == idx:
                    break
        else:
            break
    else:
        print(check)
        break
