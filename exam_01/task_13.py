# 13. Дан список чисел, необходимо удалить все вхождения числа 20 из него.
current_list = [12, 34, 20, 20, 56, 21, 20, 20, 84]
new_list = []
for i in current_list:
    if i != 20:
        new_list.append(i)
print(f'Список без числа 20: {new_list}')

# Еще пробовала удалить число 20 с помощью .remove, но удаляется не все :( Что не так?
# for i in current_list:
#     if i == 20:
#         current_list.remove(i)
# print(current_list)
