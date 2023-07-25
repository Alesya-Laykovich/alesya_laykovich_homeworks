# 3. Функция для вывода таблицы умножения для указанного числа.

num_2 = range(0, 11)
def newfunc(num_1, num_2):
    for x in num_2:
        print(f'{num_1} * {x} = {num_1 * x}\n', end='')
    return num_1 * x


num_1 = int(input('Введите число: '))
newfunc(num_1, num_2)
