import csv
with open('new_file.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        ('Имя', 'Фамилия', 'Возраст')
    )
    while True:
        name = input('Введите имя: ')
        if name == 'stop' or name == 'стоп':
            print('Данные сохранены успешно')
            break
        surname = input('Введите фамилию: ')
        age = int(input('Введите возраст: '))
        writer.writerow([name, surname, age])

