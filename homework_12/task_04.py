# 3. Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из них
# не является числом, то должна выполняться конкатенация, то есть соединение, строк.
# В остальных случаях введенные числа суммируются.

# a = input('Введите первое значение: ')
# b = input('Введите второе значение: ')
# if a.isdigit() and b.isdigit():
#     print(f'Сумма чисел равна {int(a) + int(b)}')
# elif a.isdigit() or b.isdigit():
#     print(f'Одно из значений не является числом: {a + b}')
# else:
#     print(f'Значения не являются числами: {a + b}')

a = input('Введите первое значение: ')
b = input('Введите второе значение: ')
try:
    new_a = int(a)
    new_b = int(b)
    print(f'Сумма чисел равна {int(a) + int(b)}')
except ValueError:
    print(f'Значение(-я) не является числом: {a + b}')
finally:
    print('Программа выполнена')


