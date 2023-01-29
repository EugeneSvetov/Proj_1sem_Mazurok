# 2.Составить генератор (yield), который выводит из строки только буквы.
def stringer(st: str):
    yield "".join(c for c in st if c.isalpha())


print(f'Ваши буквы : {next(stringer(input("Введите строку : ")))}')
