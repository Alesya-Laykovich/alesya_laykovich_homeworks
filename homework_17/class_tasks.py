# 1. Создайте класс Example. В нём пропишите 3 метода. Две переменные задайте как атрибут класса, две как атрибут
# объекта(в init). Первый метод: создайте переменную и выведите. Второй метод: верните сумму 2-ух атрибутов класса
# Третий метод: верните результат возведения первого атрибута объекта во второй атрибут объекта. Создайте объект класса.
# Напечатайте результат двух методов. Напечатайте переменную a.

# class Example:
#     var1 = 49
#     var2 = 101
#
#     def __init__(self, var3, var4):
#         self.var3 = var3
#         self.var4 = var4
#
#     def method_1(self):
#         a = 'hello'
#         return a
#
#     def method_2(self):
#         return self.var1 + self.var2
#
#     def method_3(self):
#         return self.var3 ** self.var4
#
# example = Example(12, 1)
# print(example.method_1())
# print(example.method_2())
# print(example.method_3())


# 2. Калькулятор. Создайте класс, где реализованы методы математических операций. Каждый метод принимает 2 параметра,
# первое число и второе число.

# class Calculator:
#
#     def addition(self, num1, num2):
#         return f'Сумма чисел {num1} + {num2} = {num1 + num2}'
#
#     def subtraction(self, num1, num2):
#         return f'Разность чисел {num1} - {num2} = {num1 - num2}'
#
#     def multiplication(self, num1, num2):
#         return f'Произведение чисел {num1} * {num2} = {num1 * num2}'
#
#     def division(self, num1, num2):
#         try:
#             division = num1 / num2
#             return f'Частное чисел {num1} / {num2} = {division}'
#         except ZeroDivisionError:
#             return 'Вызвано исключение'
#
#
#
# calculator = Calculator()
# print(calculator.addition(10, 7))
# print(calculator.subtraction(50, 9))
# print(calculator.multiplication(34, 7))
# print(calculator.division(88, 2))

# 3. Создайте класс Dog, представляющий собаку. Класс должен иметь атрибуты name (имя собаки) и age (возраст собаки).
# Реализуйте метод bark(), который выводит на экран сообщение "Гав!".

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print('Гав')

dog = Dog('Elly', 3)
print(f'Имя собаки: {dog.name}, возраст: {dog.age}')
dog.bark()
