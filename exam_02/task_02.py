# 2. Найти в списке те элементы, значение которых меньше среднего арифметического,
# взятого от всех элементов списка.
import random
list1 = [random.randint(1, 100) for i in range(5)]
print(f'Список: {list1}')

sum_of_num = 0
for i in list1:
    sum_of_num += i
arith_mean = sum_of_num / (len(list1))
print(f'Среднее арифметическое = {arith_mean}')

new_list = []
for i in list1:
    if i < arith_mean:
        new_list.append(i)
print(f'Список элементов, значения которых меньше среднего арифметического: {new_list}')
