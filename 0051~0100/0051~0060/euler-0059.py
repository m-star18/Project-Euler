from itertools import product


def moji_list(a, b):
    # アルファベット小文字 → (97, 123)
    # アルファベット大文字 → (65, 91)
    # 半角数字 → (48, 58)
    # ひらがな → (12353, 12436)
    # カタカナ → (12449, 12532+1)
    # 全角数字 → (65296, 65306)
    return [chr(i) for i in range(a, b)]


cipher = [int(x) for x in open('cipher.txt').read().split(',')]
moji = moji_list(97, 123)
v = len(cipher) // 3 + 1
ans = 0
for bit in product(moji, repeat=3):
    memo = [a ^ b for a, b in zip(cipher, [ord(x) for x in bit] * v)]
    text = ''.join(chr(x) for x in memo)
    if ' the ' in text or ' The ' in text:
        ans += sum(memo)
print(ans)
