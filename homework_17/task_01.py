# 1. Реализовать калькулятор с 4 методами: Сумма, вычитание, умножение, деление. Метод принимает 2 аргумента и
# возвращает результат. Невалидные данные должны быть обработаны.

class Calculator:

    def addition(self, num1, num2):
        try:
            return f'Сумма чисел {num1} + {num2} = {num1 + num2}'
        except TypeError:
            return 'Ошибка: переданы нечисловые данные'

    def subtraction(self, num1, num2):
        try:
            return f'Разность чисел {num1} - {num2} = {num1 - num2}'
        except TypeError:
            return 'Ошибка: переданы нечисловые данные'
    def multiplication(self, num1, num2):
        try:
            return f'Произведение чисел {num1} * {num2} = {num1 * num2}'
        except TypeError:
            return 'Ошибка: переданы нечисловые данные'

    def division(self, num1, num2):
        try:
            division = num1 / num2
            return f'Частное чисел {num1} / {num2} = {division}'
        except ZeroDivisionError:
            return 'Деление на ноль'
        except TypeError:
            return 'Ошибка: переданы нечисловые данные'


calculator = Calculator()
print(calculator.addition(10, 'l'))
print(calculator.subtraction(50, 9))
print(calculator.multiplication(34, 7))
print(calculator.division(88, 0))





