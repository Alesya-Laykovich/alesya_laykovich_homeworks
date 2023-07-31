"""5. Написать функцию, которая заполняет массив длинной 10 элементов, случайными числами в диапазоне,
указанном пользователем с клавиатуры. Функция должна принимать два аргумента – начало диапазона
и его конец, при этом ничего не возвращать."""
import random


def list_function(min_num, max_num):
    list1 = [random.randint(min_num, max_num) for i in range(10)]
    pass


min_d = int(input('Введите начало диапазона: '))
max_d = int(input('Введите конец диапазона: '))
print(list_function(min_d, max_d))
