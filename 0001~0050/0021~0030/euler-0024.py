from itertools import permutations

num = 10 ** 6
dict = [i for i in permutations(list(range(10)))]
dict.sort()
print(''.join(map(str, dict[num - 1])))
