# 3. Имеется текстовый файл prices.txt с информацией о заказе из интернет-магазина.
# В нем каждая строка с помощью символа табуляции \t разделена на три колонки:
# наименование товара; количество товара (целое число); цена (в рублях) товара за 1 шт.
# (целое число). Напишите программу, подсчитывающую общую стоимость заказа.

# data = [
#     'ежедневник\t', '2\t', '20\n',
#     'книга\t', '1\t', '35\n',
#     'ручка\t', '2\t', '2'
# ]
# with open('prices.txt', 'w', encoding='utf-8') as file:
#     file.writelines(data)

with open('prices.txt', 'r', encoding='utf-8') as file:
    a = file.readline().split()
    print(a)
    b = file.readline().split()
    print(b)
    c = file.readline().split()
    print(c)
    new_list1 = int(a[1]) * int(a[2])
    new_list2 = int(b[1]) * int(b[2])
    new_list3 = int(c[1]) * int(c[2])
    new_list = new_list1 + new_list2 + new_list3
    print(f'Общая стоимость заказа: {new_list} руб.')
