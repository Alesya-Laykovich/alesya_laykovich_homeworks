# 3. В текстовом файле посчитать количество строк, а также для каждой отдельной строки
# определить количество в ней символов.

with open('task_01_1.txt', 'r') as file:
    new_file2 = file.readlines()
    print(f'Количество строк: {len(new_file2)}')
    for i in new_file2:
        print(f'Количество символов: {len(i)}')
