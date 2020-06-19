import sympy as sym


def is_prime_pairs(num1, num2):
    a = int(str(num1) + str(num2))
    if not (sym.isprime(a)):
        return False
    b = int(str(num2) + str(num1))
    return sym.isprime(b)


def sum_clique(memo, p, clique):
    global ans
    next_clique = clique | {p}
    next = edge[p]
    if len(next_clique) != 1:
        next &= memo

    if len(next) < 5 - len(next_clique):
        return

    if len(next_clique) == 4:
        v = sum(next_clique) + min(next)
        if ans == 0 or v < ans:
            ans = v
            return
    sort_next = sorted([x for x in next if x > max(next_clique)])
    for q in sort_next:
        sum_clique(next, q, next_clique)
    return


num_max = 3 * 10 ** 4
primes = {i for i in sym.primerange(3, num_max)}
primes.remove(5)
edge = {i: set() for i in primes}

for p in primes:
    for q in (q for q in primes if q > p):
        if is_prime_pairs(p, q):
            edge[p].add(q)
            edge[q].add(p)

dict = {prime: prime_set for prime, prime_set in edge.items() if len(prime_set) > 3}
edge = {prime: {q for q in prime_set if q in dict.keys()} for prime, prime_set in dict.items()}
keys = sorted(edge.keys())
ans = 0
for k in keys:
    if 0 < ans < k:
        break
    sum_clique(set(), k, set())

print(ans)
