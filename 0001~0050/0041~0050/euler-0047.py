class Prime_Decomposition:
    def __init__(self, n_max):
        self.min_factor = min_factor = list(range(n_max + 1))
        for i in range(2, int(n_max ** 0.5) + 1):
            if min_factor[i] == i:
                for j in range(i * i, n_max + 1, i):
                    if min_factor[j] == j:
                        min_factor[j] = i

    def __call__(self, n):
        min_factor = self.min_factor
        n_twoes = (n & -n).bit_length() - 1  # 最悪ケースでは速くなる
        res = [2] * n_twoes
        n >>= n_twoes
        while n > 1:
            p = min_factor[n]
            res.append(p)
            n //= p
        return res


limit = 10 ** 6
prime_check = Prime_Decomposition(limit)
cnt = 0
for i in range(1, limit):
    if len(set(prime_check(i))) == 4:
        cnt += 1
        if cnt == 4:
            print(i - 3)
            break
    else:
        cnt = 0
