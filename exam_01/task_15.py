# 15. Необходимо удалить пустые строки из списка строк.

list1 = ['need', 'list', '', '', 'hello', '', 'way', '', 'number', 'key']

# # Вариант 1.
# new_list = []
# for i in list1:
#     if i != '':
#         new_list.append(i)
# print(new_list)

# Вариант 2.
string = ' '.join(list1)
# print(string)
list2 = string.split()
print(f'Список после удаления пустых строк: {list2}')

# Тоже пробовала удалить с помощью метода .remove, но удаляются не все пустые строки.
# list1 = ['need', 'list', '', '', 'hello', '', 'way', '', 'number', 'key']
# for i in list1:
#     if i == '':
#         list1.remove(i)
# print(f'Список после удаления пустых строк: {list1}')
