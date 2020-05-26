def binary_search(list, item):
    if item is None:
        return item
    low = 0
    high = limit - 2

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return item
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    # 見つからなかったとき
    return None


limit = 10 ** 5
p = [n * (3 * n - 1) // 2 for n in range(1, limit)]
h = [n * (2 * n - 1) for n in range(1, limit)]
n = 286

while 1:
    t = n * (n + 1) // 2
    if binary_search(h, binary_search(p, t)):
        print(t)
        break
    n += 1
