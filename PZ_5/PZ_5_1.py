def make_pretty(n, symb):
    try:
        int(n)
        str(symb)
        i = 0
        result = ''
        while i != n:
            i += 1
            result += symb
        return print(f'СИМВОЛЫ: {result}')
    except:
        print('Неверный формат ввода')


make_pretty(input('Введите количество '), input('Введите символ '))
