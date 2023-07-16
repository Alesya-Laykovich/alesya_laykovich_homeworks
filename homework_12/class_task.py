# В файле, в одну строку записаны слова и числа через пробел или _ найти сумму всех чисел
elements = []
with open('new_task1.txt', 'r') as file:
    list1 = file.readlines()
for i in list1:
    i = i.replace('_', ' ')
    print(i)
    elements = i.split(' ')
print(elements)
result = sum([int(i) for i in elements if i.isdigit()])
print(f'Сумма чисел: {result}')