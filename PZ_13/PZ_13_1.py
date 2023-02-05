# В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
# Выполнить замену элементов второй строки исходной матрицы на полученные
# суммы.

import random

n = int(input('Введите размерность матрицы: '))

matrix = [[random.randint(-50, 50) for _ in range(n)] for _ in range(n)]
print('Ваша матрица: ')
for i in matrix:
    print(*i, sep='\t'*2)

matrix[1] = [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]
print('Новая матрица: ')
for i in matrix:
    print(*i, sep='\t'*2)