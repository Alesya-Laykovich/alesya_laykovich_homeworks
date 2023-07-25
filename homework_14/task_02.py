#  2. Если в функцию передается кортеж, то посчитать длину всех его слов. Если список,
#  то посчитать кол-во букв и чисел в нем. Число - количество нечетных цифр.
#  Строка - количество букв.

# new = input('Введите данные через пробел: ')
# new_1_split = new.split(' ')
# print(new_1_split)

# new_2 = input('Введите данные через пробел: ')
# new_2_split = new_2.split(' ')
# n_t = tuple(new_2_split)
# print(n_t)

# n = int(input('Введите число: '))


num_letters = []

def function(new_1):
    if type(new_1) == tuple:
        return f'Длина всех слов кортежа = {sum([len(i) for i in new_1])}'
    elif type(new_1) == list:
        # w.append(len([i for i in new_1 if str(i).isalpha()]))
        num_letters.append(sum([len(i) for i in new_1 if str(i).isalpha()]))
        num_letters.append(len([i for i in new_1 if str(i).isdigit()]))
        return f'Количество букв и чисел в списке: {num_letters}'
    elif type(new_1) == int:
        return f"Количество нечетных цифр: {len([i for i in str(new_1) if i in '13579'])}"
    elif type(new_1) == str:
        a = new_1.replace(' ', '')
        return f"Количество букв в строке: {len(a)}"


print(function(('gjg', 'ff')))
print(function(['hhgf', 'ji', 6, 'h', 8]))
print(function(6785))
print(function('hgfddrr jgt lj'))
