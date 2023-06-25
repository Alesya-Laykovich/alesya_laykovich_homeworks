# # 1. Дан произвольный список. Представить его в обратном порядке.

# import random
# list1 = [random.randint(1, 20) for i in range(5)]
# print(f'Произвольный список: {list1}')
# list1.reverse()
# print(f'Список в обратном порядке: {list1}')


# # 2. Дан список с числами и в нем есть цифра 20. Поменять 20 на 200.
# list2 = [1, 2, 3, 43, 20, 8, 17]
# x = list2.index(20)
# list2[x] = 200
# print(f'Список при замене числа 20 на 200: {list2}')

# # 3.  Список из 7 цифр. Если чётных цифр в нём больше, то найти сумму всех цифр,
# если нечётных больше, то найти произведение 1, 3 и 6 элемента.

# import random
# numbers = [random.randint(1, 20) for i in range(7)]
# print(numbers)
# even = 0
# not_even = 0
# for i in numbers:
#     if i % 2 == 0:
#         even += 1
#     else:
#         not_even += 1
# print(f'количество четных {even}\nколичество нечетных {not_even}')
# sum_of_list = 0
# mult = 0
# if even > not_even:
#     for i in numbers:
#         sum_of_list += i
#     print(f'сумма элементов = {sum_of_list}')
# else:
#     mult = numbers[0] * numbers[2] * numbers[5]
#     print(f'Произведение 1, 3 и 6 элементов = {mult}')


# # 4. Найти совпадающие элементы двух списков. a = [5,[1,2],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]] Эти значения записать в новый список

# a = [5, [1, 2], 2, 'r', 4, 'ee']
# b = [4, 'we', 'ee', 3, [1, 2]]
# new_list1 = a + b
# repeat = []
# for i in new_list1:
#     if new_list1.count(i) >= 2 and i not in repeat:
#         repeat.append(i)
# print(f'Повторяющиеся значения: {repeat}')


# # 5. Даны 2 списка: a = [4,6,'pу','tell',78], b = [44,'hello’,56,'exept’,3]
# Выполнить следующие операции:
# 1)Сложить два списка
# 2) Добавьте элемент 6 на 3 позицию.
# 3)Удалите все текстовые переменные
# 4) Посчитайте количество элементов списка

a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]
new_list = a + b
print(f'1) В результате сложения получился список: {new_list}')
new_list.insert(2, 6)
print(f'2) Добавление элемента 6 на 3 позицию: {new_list}')

new_list1 = []
for i in new_list:
    if type(i) != str:
        new_list1.append(i)
print(f'3) Список после удаления текстовых переменных: {new_list1}')


# Пробовала удалить текстовые элементы с помощью remove, но удалились не все. Что не так?
# for i in new_list:
#     if type(i) == str:
#         new_list.remove(i)
# print(f'Список после удаления текстовых переменных: {new_list}')

print(f'4) Количество всех элементов списка: {len(new_list)}')
