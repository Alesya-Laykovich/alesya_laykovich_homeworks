# 14. С клавиатуры вводится десятизначное число. Вывести на экран четные числа,
# входящие в данное число. Например, 1234567892  2 4 6 7 8 2

input_number = input('Введите десятизначное число: ')
even_numbers = []
list1 = [int(i) for i in input_number]  # с помощью генератора списков отделяем каждый элемент
for i in list1:
    if i % 2 == 0:
        print(i)
        even_numbers.append(i)
print(f'Список четных чисел, входящих в число: {even_numbers}')