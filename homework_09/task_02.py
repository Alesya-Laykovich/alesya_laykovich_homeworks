# 2. Имеется список с произвольными данными. Поставлена задача преобразовать его
# в множество. Если какие-то элементы нельзя хешировать, то пропускаем их.
# ( загуглить про то, какие данные не поддерживает множество)
list1 = ['hi', 'madam', (11, 56), {12, 3, 4}, 'opinion', 17, {'city': 'Minsk'}, [1, 2, 3]]
set1 = set()
for i in list1:
    if type(i) != list and type(i) != set and type(i) != dict:
        set1.add(i)
print(f'Преобразование списка в множество: {set1}')
