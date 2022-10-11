# Вариант 15.
# 1. Дано вещественное число А и целое число N (>0). Используя один цикл, найти сумму 1+А+А^2 + А^З... + А^Х.
i = 0
ans = 0
try:
    a = float(input())
    n = int(input())
    while i != n:
        i += 1
        ans += a ** i
    print(ans + 1)
except ValueError:
    print('Неверный формат')

