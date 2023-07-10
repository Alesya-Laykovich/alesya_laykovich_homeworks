# 3. Есть список натуральных чисел. Требуется сформировать из них множество.
# Если какое-либо число повторяется, то преобразовать его в строку по образцу:
# например, если число 4 повторяется 3 раза, то в множестве будет следующая запись:
# само число 4, строка «44» (второе повторение, т.е. число дублируется в строке),
# строка «444» (третье повторение, т.е. строка множится на 3).


# У меня не получилось решить эту задачу (то, как я пробовала не подходит).
# Вы не могли бы ее потом объяснить?



# import random
# numbers = [random.randint(1, 10) for i in range(10)]
# set1 = set(numbers)
# print(numbers)
# print(set1)
# new_list = []
# for i in numbers:
#     if numbers.count(i) > 1:
#         new_list.append(str(i) * numbers.count(i))
#     else:
#         new_list.append(i)
# new_set = set(new_list)
# print('l', new_set)



# numbers = [random.randint(1, 10) for i in range(10)]
# set1 = set(numbers)
# print(set1)
# print(numbers)
#
# list1 = []
# list2 = []
# for i in numbers:
#     if i not in list1:
#         list1.append(i)
# for i in numbers:
#     list2.append(numbers.count(i))
# # print(list1)
# # print(list2)
# new_dict = dict(zip(list1, list2))
# li = []
# i = 0
# for key, value in new_dict.items():
#     if value > 1:
#         li.append((str(key) * value))
#     while i <= value:
#         li.append(str(key) * i)
#         i += 1
# print(li)



