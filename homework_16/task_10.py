"""10. Функция sum(a, b) принимает 2 числа и возвращает их сумму. Написать декоратор, который
возвращает ошибку если переданы не числовые параметры(например строка)"""


def decorator(func):
    def wrapper(num1, num2):
        try:
            return func(num1, num2)
        except TypeError:
            return 'Ошибка: переданы нечисловые параметры'
    return wrapper


@decorator
def sum_of_num(a, b):
    return a + b


print(sum_of_num(100, "9"))
