# 3. Даны несколько списков: [-8, 1, 2, -2, 0], [1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 34].
# Для каждого из списков найти второе наименьшее значение в нем (правильные ответы выделены
# жирным шрифтом).

list1 = [-8, 1, 2, -2, 0]
list2 = [1, -1, 0, -9, 4, -5]
list3 = [1, 4, 0, 23, 6, 34]
list1.sort(reverse=True)
list2.sort(reverse=True)
list3.sort(reverse=True)
print(f'Список в порядке убывания - {list1}\nВторое наименьшее значение: {list1[-2]}')
print(f'Список в порядке убывания - {list2}\nВторое наименьшее значение: {list2[-2]}')
print(f'Список в порядке убывания - {list3}\nВторое наименьшее значение: {list3[-2]}')
