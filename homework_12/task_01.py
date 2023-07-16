# 1. Файл содержит числа и буквы. Каждый записан в отдельной строке. Нужно считать содержимое
# в список так, чтобы сначала шли числа по возрастанию, а потом слова по возрастанию их длины.

with open('task_01_1.txt', 'r') as file:
    lines = file.readlines()
    # print(lines)
    list_split = [line.rstrip() for line in lines]
    # print(list_split)

new_list_num = []
new_list_str = []
for i in list_split:
    if i.isdigit():
        new_list_num.append(int(i))
        new_list_num.sort()
    else:
        new_list_str.append(i)
        new_list_str.sort(key=len)
# print(new_list_num, new_list_str)
result = new_list_num + new_list_str
print(f'Новый список: {result}')
