# Разделить строку “Apples, Oranges, Pears, Bananas, Berries” по запятым
# и вывести на экран. Затем объединить элементы с использованием пробела,
#чтобы программа вывела “Apples Oranges Pears Bananas Berries”.

fruit = 'Apples, Oranges, Pears, Bananas, Berries'
fruit_1 = fruit.split(',')
print(fruit_1)
fruit_2 = ' '.join(fruit_1)
print(fruit_2)


