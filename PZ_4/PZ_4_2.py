# Дано целое число N (>0), являющееся некоторой степенью числа 2: N = 2^К.
# Найти целое число К. — показатель этой степени.
try:
    n = int(input('Введите N '))  # проверка является ли ввод числом
    i = 1
    while 2 ** i != n: # начало цикла
        i += 1
    print(i) # вывод результата
except ValueError:
    print('Неверный формат ввода') # вывод исключения

