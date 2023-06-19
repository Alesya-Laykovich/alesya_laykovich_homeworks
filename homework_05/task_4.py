# 4. Дан список чисел. Если число встречается более двух раз, то добавить его
# в новый список.

new_list = [1, 3, 4, 1, 6, 3, 14, 23, 23, 5, 4, 6, 11, 1, 3, 23]
repeating_numbers = []
# non_repeating_numbers = []
for i in new_list:
    c = new_list.count(i)
    if c > 2:
        repeating_numbers.append(i)
    # else:
    #     non_repeating_numbers.append(i)
print('Числа, повторяющиеся более 2 раз: ', repeating_numbers)
# print('Числа, повторяющиеся 2 раза или менее 2 раз: ', non_repeating_numbers)
