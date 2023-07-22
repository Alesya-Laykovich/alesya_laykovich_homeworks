# 4. Ввести 10 чисел с клавиатуры, данные числа добавить во множество.
input_inf = input('Введите 10 чисел через пробел: ')
new_list = input_inf.split(' ')
# print(new_list)
new_set = []
for i in new_list:
    if i.isdigit():
        new_set.append(int(i))
print(f'Множество: {set(new_set)}')
