# 16. Напишите программу, которая вычисляет процентное содержание символов G (гуанин)
# и C (цитозин) во введенной строке (программа не должна зависеть от регистра вводимых символов).
# Например, в строке "acggtgttat" процентное содержание символов G и C равно 4/10 ⋅ 100 = 40.0,
# где 4 - это количество символов G и C, а 10 -- это длина строки.

input_string = input('Введите строку: ')
string_lower = input_string.lower()     # переводим все символы в один регистр (нижний)
letter_g = string_lower.count('g')
letter_c = string_lower.count('c')
letters_cg = letter_g + letter_c
print(f"Количество символов 'G'/'g' и 'C'/'c': {letters_cg}")
percentage = letters_cg / len(input_string) * 100
print(f"Процентное содержание символов 'G'/'g' и 'C'/'c', %: {percentage}")
