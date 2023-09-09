""" 1. метод sum(a,b) принимает 2 числа и возвращает их сумму.
Написать декоратор, который возвращает ошибку
если переданы не числовые параметры(например строка)

    примерно такое:

    `@validate_int_parameters
    def sum(a,b)`

    `sum(3, "1") => ошибка
    sum(4, 2) = > 6`"""

def validate_parameters(func):
    def wrapper(a, b):
        is_valid_a = isinstance(a, (int, float))
        is_valid_b = isinstance(b, (int, float))
        if is_valid_a and is_valid_b:
            return func(a, b)
        else:
            raise TypeError('Not valid')
    return wrapper

@validate_parameters
def sum(a, b):
    return a + b

print(f'Сумма чисел равна {sum(15, 5)}')
