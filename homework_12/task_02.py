# 2. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

with open('task_02_1.txt', 'w') as file:
    while True:
        text = input('Введите строку: ')
        file.write(text + '\n')
        if text == '':
            break
