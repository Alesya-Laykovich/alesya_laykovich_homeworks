# 1. Дан список list = [15,48,'hello',6,19,'world’]. Все числа этого списка
# проверить на чётность. Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить его на 1 в списке. Все слова: посчитать количество гласных
# и согласных. Вывести всё на экран.

list1 = [15, 48, 'hello', 6, 19, 'world']
numbers = []
letters = []
for i in list1:
    if type(i) != str:
        numbers.append(i)
    else:
        letters.append(i)
print(f'Список с типом данных int: {numbers}, список с типом данных str: {letters}')
new_numbers = []
for i in numbers:
    if i % 2 == 0:
        if i >= 10:
            a = i // 10
            b = i % 10
            c = a + b
            new_numbers.append(c)
        else:
            new_numbers.append(i)
    else:
        new_numbers.insert(i, 1)
print(f'Список после замены четных чисел на их сумму, нечетных - на 1: {new_numbers}')

string_letters = ''.join(letters)
vowels = 'AEIOUYaeiouy'
number_of_vowels = []
number_of_consonants = []
for i in string_letters:
    if i in vowels:
        number_of_vowels.append(i)
    else:
        number_of_consonants.append(i)
# print(f'Список согласных: {number_of_consonants}, список гласных: {number_of_vowels}')
print(f'Количество согласных в списке: {len(number_of_consonants)}, количество гласных: {len(number_of_vowels)}')
