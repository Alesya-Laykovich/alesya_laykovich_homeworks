# Найти результат выражения. Переменная 'а' вводится с клавиатуры.

a = int(input('Введите значение "a" : '))
num1 = ((1 + a + a ** 2) / (2 * a + a ** 2)) + 2
num2 = (1 - a + a ** 2) / (2 * a - a ** 2)
num3 = 5 - 2 * a ** 2
y = (num1 - num2) ** -1 * num3
print(y)

# Вопросы в целом:
# 1. функция 'print' НЕ подразумевает под собой тип данных 'str', правильно?
# 2. когда нужно указывать тип данных (например, bool, int, float) в функции 'print'?