# 10. Дан список lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20].
# Необходимо вывести элементы, которые одновременно 1) меньше 30 и 2) делятся на 3 без остатка.
# Все остальные элементы списка необходимо просуммировать и вывести конечный результат.

lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
new_lst = []
n = 0
for i in lst:
    if i < 30 and i % 3 == 0:
        new_lst.append(i)
    else:
        n += i
print(f'Элементы, которые одновременно меньше 30 и делятся на 3 без остатка: {new_lst}')
print(f'Сумма остальных элементов списка: {n}')
