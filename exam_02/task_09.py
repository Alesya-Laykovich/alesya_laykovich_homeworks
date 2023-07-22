# 9. Ваша задача состоит в том, чтобы преобразовать строки в то, как они были бы написаны
# Джейденом Смитом. Строки является настоящими цитатами Джейдена Смита, но они не написаны
# с заглавной буквы так, как он их изначально напечатал.

# example = "How can mirrors be real if your eyes aren't real"
inf = input('Введите цитату: ')
new_inf = inf.replace(',', '')
new_inf_2 = new_inf.replace('.', '')
# print(new)
list1 = new_inf_2.split(' ')
# print(list1)
titled_letters = []
for i in list1:
    # if type(i) == str:
    titled_letters.append(i[0].upper() + i[1:].lower())
result = ' '.join(titled_letters)
print(f'Цитата в стиле Джейдена Смита: {result}')
