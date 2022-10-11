def squares(a, b):
    return (1 if a == b else
            1 + squares((a - b), b) if a > b else
            1 + squares(a, b - a))


print(squares(int(input()), int(input())))
