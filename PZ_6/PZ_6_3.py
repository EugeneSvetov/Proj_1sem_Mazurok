from random import randint
n = input('Введите длину списка')

try:
  n = int(n)
  nums = [randint(0, 11) for i in range(n)]
except ValueError:
  print('Неверно введённые данные')


def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())

print('Ваш список ', nums)

print('Список со здвигом ', shift(nums, -1))
