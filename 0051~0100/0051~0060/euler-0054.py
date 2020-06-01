from collections import Counter


def pop_and_return_key(d, k):
    d.pop(k)
    return k


def check(p):
    n = Counter([rank[x[0]] for x in p])
    n_key = n.keys()
    n_value = n.values()
    set_p = len(set([x[1] for x in p])) == 1
    sort_n_key = sorted(n_key)
    sort_n_value = sorted(n_value)
    n_key_check = sort_n_key == list(range(min(n_key), min(n_key) + 5))
    f = lambda d, x: max([k for k, v in d.items() if v == x])

    # Royal Flush
    if sort_n_key == list(range(10, 15)) and set_p:
        yield 10 ** 10
    # Straight flush
    if n_key_check and set_p:
        yield 10 ** 9 + max(n_key)
    # Flush
    if set_p:
        yield 10 ** 6 + max(n_key)
    # Straight
    if n_key_check:
        yield 10 ** 5 + max(n_key)

    while n:
        # Four of a kind
        if 4 in n_value:
            yield 10 ** 8 + pop_and_return_key(n, f(n, 4))
        # Full house
        if sort_n_value == [2, 3]:
            yield 10 ** 7 + pop_and_return_key(n, f(n, 3))
        # Three of a kind
        if 3 in n_value:
            yield 10 ** 4 + pop_and_return_key(n, f(n, 3))
        # Two pair
        if sort_n_value == [1, 2, 2]:
            yield 10 ** 3 + pop_and_return_key(n, f(n, 2))
        # One pair
        if 2 in n_value:
            yield 10 ** 2 + pop_and_return_key(n, f(n, 2))
        # High card
        yield pop_and_return_key(n, f(n, 1))


rank = {x: i for i, x in enumerate(list('23456789TJQKA'), 2)}
cnt = 0
for data in open('poker.txt', 'r'):
    data = data.split()
    p1_memo = check(data[:5])
    p2_memo = check(data[5:])
    p1 = next(p1_memo)
    p2 = next(p2_memo)
    while p1 == p2:
        p1 = next(p1_memo)
        p2 = next(p2_memo)
    if p1 > p2:
        cnt += 1
print(cnt)
