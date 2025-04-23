#функция проверки числа на простоту
def is_prime(n):
    #крайние случаи
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    #оптимизированный перебор
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


n = int(input())
print(is_prime(n))
