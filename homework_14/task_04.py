# 4. Чтобы лучше разобраться в типах параметров функций Инна создала inspect_function(),
# которая в качестве аргумента принимает другую функцию (главное, не встроенную, built-in).
# В результате работы она выводит следующие данные: название анализируемой функции, наименование
# всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.). Попробуйте повторить
# результат девушки.

# Решение смотрела в интернете. Прочитала про модуль 'inspect', но пока остались вопросы,
# в том числе по применению методов. Например, в 'inspect.signature(some_func).parameters.values()'
# запись про ".parameters.values()" она всегда нужна, да? (без нее выдает ошибку)

import inspect
import random

def inspect_function(some_func):
    print(f'Анализируем функцию {some_func.__name__}')
    for parameter in inspect.signature(some_func).parameters.values():
        print(parameter.name, parameter.kind, sep=': ')


inspect_function(random.randint)



