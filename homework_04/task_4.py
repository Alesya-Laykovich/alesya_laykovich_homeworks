#   Пользователь вводит два числа с клавиатуры. Вывести на экран yes,
#   если они отличаются друг от друга на 135, иначе вывести на экран No.

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if num1 - num2 == 135 or num2 - num1 == 135:
    print('Yes')
else:
    print('No')
