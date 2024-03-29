# Из предложенного текстового файла (text18-15.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы нижнего регистра на верхний.

file = open('text18-15.txt', 'r', encoding='utf-8')  # открываем файл
a = file.read()  # считываем информацию
file.close()  # закрываем файл
print(f'Ваш файл : \n{a}')  # вывод файла
print(f'Количество букв в нижнем регистре : {sum(map(str.islower, a))}')  # вывод
b = open('new_text.txt', 'w')  # создаем файл
print(a.swapcase(), file=b)  # добавляем в него данные
b.close()  # закрываем файл
b = open('new_text.txt', 'r')  # читаем файл
print(f'\nНовый файл : \n{b.read()}')  # вывод результата
