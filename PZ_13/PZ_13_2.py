# В матрице найти минимальный элемент в предпоследней строке.

import random

n = int(input('Введите размерность матрицы: '))

matrix = [[random.randint(-50, 50) for _ in range(n)] for _ in range(n)]
print('Ваша матрица: ')
for i in matrix:
    print(*i, sep='\t'*2)

print(f'Минимальный элемент в предпоследней строке матрицы: {min(matrix[-2])}')