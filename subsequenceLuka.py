def luka_cycle(L0, L1, n):
    for _ in range(1, n):
        L0, L1 = L1, L0 + L1
    return L1

def luka(n):
    #последовательность Люка: 2,1,3,4,7,11,18,...
    L0 = 2
    L1 = 1
    return luka_cycle(L0, L1, n)

#начало программы
n = int(input())
print(luka(n))