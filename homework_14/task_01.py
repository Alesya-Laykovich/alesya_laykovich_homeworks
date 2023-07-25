# 1. Простейший калькулятор c введёнными двумя числами вещественного типа. Ввод с клавиатуры:
# операции + - * / и два числа. Операции являются функциями. Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).


while True:
    num1 = float(input('Введите первое число: '))
    sign = input('Введите знак (+,-,*,/): ')
    num2 = float(input('Введите второе число: '))

    def new_func(sign):
        if sign == '+':
            return f'Сумма чисел {num1} + {num2} = {num1 + num2}'
        elif sign == '-':
            return f'Разность чисел {num1} - {num2} = {num1 - num2}'
        elif sign == '*':
            return f'Произведение чисел {num1} * {num2} = {num1 * num2}'
        elif sign == '/':
            try:
                division = num1 / num2
                return f'Частное чисел {num1} / {num2} = {division}'

            except ZeroDivisionError:
                return 'Вызвано исключение'
        else:
            return 'Данные введены неверно'


    print(new_func(sign))

    finish = int(input('Для завершения программы введите 0. Чтобы продолжить, введите любую другую цифру: '))
    if finish == 0:
        break
    else:
        continue
