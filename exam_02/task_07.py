# 7. Ввести строку. Вывести на экран букву, которая находится в середине этой строки.
# Также, если эта центральная буква равна первой букве в строке, то создать и вывести
# часть строки между первым и последним символами исходной строки. (подсказка: для получения
# центральной буквы, найдите длину строки и разделите ее пополам. Для создания результирующий
# строки используйте срез)

input_inf = input('Введите строку: ')
centeral_letter = int(len(input_inf) / 2)
print(f'Центральная буква: {input_inf[centeral_letter]}')
if input_inf[centeral_letter] == input_inf[0]:
    print(f'Часть строки между первым и последним символами: {input_inf[1:-1]}')
else:
    print('Центральная буква и первая буква не совпадают')
