KAPREKAR1 = 495
KAPREKAR2 = 6174
KAPREKAR3 = 549945
KAPREKAR4 = 631764


#проверка входных данных
def kaprekar_check(n):
    control = 0
    l = len(str(n))
    if (l != 3) and (l != 4) and (l != 6):
        control = -1

    digits = str(n)
    all_same = len(set(digits)) == 1 and len(digits) == l
    if all_same:
        control = -1

    if (n == 100) or (n == 1000) or (n == 100000):
        control = -1

    return control != -1


#разделение числа (преобразование в список)
def numerics(n):
    return list(map(int, str(n)))


#взятие max, min и получение числа
def kaprekar_step(L):
    L.sort(reverse=True)
    max = int(''.join(map(str, L)))
    L.sort()
    min = int(''.join(map(str, L)))
    return max - min


#процесс Капрекара, пока не получим числа 495, 6174, 549945, 631764
def kaprekar_loop(n):
    check = kaprekar_check(n)
    if not check:
        print(f"Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара")
        return -1

    repeat_numbers = {n}
    cnt = 1
    while (n != KAPREKAR1) and (n != KAPREKAR2) and (n != KAPREKAR3) and (n != KAPREKAR4):

        cnt += 1
        L = numerics(n)
        digit = kaprekar_step(L)
        n = digit

        #бывают числа, при которых происходит зацикливание, в этом случае надо выходить из цикла
        repeat_numbers.add(digit)
        l = len(repeat_numbers)
        if l != cnt:
            print(f"Следующее число - {n}, кажется процесс зациклился...")
            return -1

        print(digit)


#ввод числа: XXX или XXXX или XXXXXX
n = int(input())
kaprekar_loop(n)
