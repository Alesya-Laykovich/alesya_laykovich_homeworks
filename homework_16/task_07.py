# 7. Написать функцию, которая считает сколько гласных и согласных в строке. Строку вводить
# с клавиатуры.

def string1(new_string):
    vowels = 'AEIOUYaeiouy'
    space = ' ,.-/()'
    vowel_list = len([i for i in new_string if i in vowels])
    consonant_list = len([i for i in new_string if i not in vowels and i not in space])
    return f'Количество гласных в строке: {vowel_list}', f'\nКоличество согласных в строке: {consonant_list}'


string11 = input('Введите строку: ')
print(*string1(string11))

