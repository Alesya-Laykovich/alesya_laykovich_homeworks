# 4. Вам предоставляется CSV-файл, содержащий данные о продажах различных товаров.
# Каждая строка файла содержит информацию о конкретной продаже:
# название товара, количество проданных единиц и цена за единицу. Ваша задача - написать программу,
# которая считывает данные из файла и вычисляет общую сумму продаж.
import csv

# data = [
#     ['Название товара', 'Количество проданных единиц', 'Цена за единицу в руб.'],
#     ['Ежедневник', 2, 20],
#     ['Книга', 1, 35],
#     ['Ручка', 2, 2]
# ]
# with open('prices.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerows(data)

with open('prices.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';', )
    reader_list = list(reader)
    # print(reader_list)
    result = 0
    total_per_item = []
    total = []
    total_per_item.extend(reader_list[1:])
    # print(*total_per_item)
    for row in total_per_item:
        print(row)
        result = int(row[1]) * int(row[2])
        # print(f'Сумма продажи по каждому товару: {result}')
        total.append(result)
    print(f'Общая сумма продажи: {sum(total)}')
