# Дано трехзначное число. Вывести вначале его последнюю цифру (единицы), а затем — его среднюю цифру (десятки).
x = input('Введите трехзначное число ') # Ввод данных
try:
  x = int(x) # Обработка исключения
  print(' Единицы:', x%10, '\n', 'Десятки:', x%100//10) # Вывод результата
except ValueError:
  print('Неверный формат данных') # Вывод исключения
