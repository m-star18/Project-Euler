def binary_search(item):
    low = 0
    high = limit * 2 - 2

    while low <= high:
        mid = (low + high) // 2
        if p[mid] == item:
            return True
        if p[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    # 見つからなかったとき
    return False


limit = 10 ** 4
p = [n * (3 * n - 1) // 2 for n in range(1, limit * 2)]
for j, pj in enumerate(p[:limit + 1]):
    for pk in p[j + 1:limit + 1]:
        if binary_search(pk + pj) and binary_search(pk - pj):
            print(pk - pj)
            exit()
