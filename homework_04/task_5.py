#   Вам необходимо написать программу, которая проверяет здоровье персонажа в игре.
#   Если оно равно или меньше нуля, то результат возвращает False, в противном случае True.

health = int(input('Введите состояние здоровья героя в виде численного выражения: '))
if health <= 0:
    print('False')
else:
    print('True')