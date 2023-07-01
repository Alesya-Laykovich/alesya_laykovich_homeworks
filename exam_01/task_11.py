# 11. Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
# В новый список добавить элементы, которые содержат пробел.

list1 = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
new_list = []
for i in list1:
    if ' ' in i:
        new_list.append(i)
print(f'Список элементов, содержащих пробел: {new_list}')
