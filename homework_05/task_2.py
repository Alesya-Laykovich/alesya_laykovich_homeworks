# 2. Есть список с четными и нечетными элементами. Посчитать количество
# четных и нечетных элементов.

list_new = [3, 43, 4, 15, 18, 2, 7, 35, 6]
list1 = []
list2 = []
for i in list_new:
    if i % 2 == 0:
        list1 += [i]
    else:
        list2 += [i]
print(f'Количество четных элементов: {len(list1)}')
print(f'Количество нечетных элементов: {len(list2)}')
