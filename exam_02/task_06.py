# 6.Сжать массив, удалив из него все элементы, величина которых находится в интервале
# [а, b]. Освободившиеся в конце массива элементы заполнить нулями.
import random
list1 = [random.randint(1, 100) for i in range(5)]
print(f'Список: {list1}')
min_num = int(input('Введите минимальное число диапазона: '))
max_num = int(input('Введите максимальное число диапазона: '))

new_list = []
for i in list1:
    if i > max_num:
        new_list.append(i)
    elif i < min_num:
        new_list.append(i)
    else:
        new_list.insert(i, 0)
new_list.sort(reverse=True)
print(f'Список элементов, величина которых находится в интервале {min_num, max_num}: {new_list}')
