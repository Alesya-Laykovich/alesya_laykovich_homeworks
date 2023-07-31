# 8. Функцию, которая при заданном целом числе n посчитает n + nn + nnn.

def func_n(new):
    n = int(new) + int((new * 2)) + int((new * 3))
    return n

s = input('Введите целое число: ')
print(func_n(s))
