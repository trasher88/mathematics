#число капрекара
def kaprekar(n):
    x = n ** 2
    s = str(x)

    for i in range(1, len(s)):
        a = int(s[:i])
        b = int(s[i:])

        # Игнорирование случаев, где b пусто (кроме тривиального n=1)
        if not b and n != 1:
            continue

        a_num = int(a) if a else 0
        b_num = int(b) if b else 0

        if a_num + b_num == n:
            return True

    return False

n = int(input())
print(kaprekar(n))