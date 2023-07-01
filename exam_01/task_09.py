# 9. Дан список [student1, student2, student3], с помощью цикла for добавить
# к каждому элементу списка слово “_good”. Вывести на экран.

list1 = ['student1', 'student2', 'student3']
new = []
for i in list1:
    new.append(i + '_good')
print(f'Список с добавлением "_good" к каждому элементу списка: {new}')
