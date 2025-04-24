#перевод числа из одной системы счисления в другую (системы: от 2 до 36)
def convert(num, to_base=10, from_base=10):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #проверка на допустимость оснований систем счисления
    if to_base < 2 or to_base > 36:
        return print(f"Значение to_base должно быть от 2 до 36! Ваше число {to_base}")
    if from_base < 2 or from_base > 36:
        return print(f"Значение from_base должно быть от 2 до 36! Ваше число {from_base}")

    #если число записано как строка, перевод в верхний регистр (для сравнения с alphabet)
    if isinstance(num, str):
        num = num.upper()
    else:
        num = str(num)

    #проверка на корректность числа в исходной системе счисления
    for char in num:
        if char not in alphabet[:from_base]:
            return print(f"Недопустимое значение '{char}' для системы счисления from_base: {from_base}")

    #перевод числа в десятичную систему
    decimal_value = 0
    for i, char in enumerate(num[::-1]):
        decimal_value += alphabet.index(char) * (from_base ** i)

    #если целевая система - десятичная, возврат строки
    if to_base == 10:
        return f"{num} в системе с основанием {from_base} => {decimal_value} в системе с основанием {to_base}"

    #перевод десятичного числа в целевую систему счисления
    if decimal_value == 0:
        return f"{num} в системе с основанием {from_base} => {decimal_value} в системе с основанием {to_base}"

    result = []
    while decimal_value > 0:
        decimal_value, remainder = divmod(decimal_value, to_base)
        result.append(alphabet[remainder])

    string = ''.join(reversed(result))
    return f"{num} в системе с основанием {from_base} => {string} в системе с основанием {to_base}"


#начало программы
#примеры ввода
print(convert('1111111', 10, 2))
#print(convert('120120', 10, 3))
#print(convert('3120', 10, 4))
#print(convert('A', 10, 16))
#print(convert(255, 16, 10))
#print(convert(128, 2, 10))
#print(convert('255', 10, 31))
#print(convert('B13', 2, 36))
#print(convert(0, 2, 10))
