# 2. Написать программу для вычисления значения выражений. Проверить правильность
# выполнения задания с помощью тестовых значений.

import math
alpha = float(input("Введете значение 'alpha': "))
beta = float(input("Введете значение 'beta': "))
gamma = float(input("Введете значение 'gamma': "))

a = math.sin(alpha + beta - gamma)
b = math.sin(beta + gamma - alpha)
c = math.sin(gamma + alpha - beta)
d = math.sin(alpha + beta + gamma)

y = 1 / 4 * (a + b + c - d)
print(f'Значение выражения равно: {y}')


# test
# import math
# alpha = 1
# beta = 1
# gamma = 0.5
#
# a = math.sin(alpha + beta - gamma)
# b = math.sin(beta + gamma - alpha)
# c = math.sin(gamma + alpha - beta)
# d = math.sin(alpha + beta + gamma)
#
# y = 1 / 4 * (a + b + c - d)
# print(f'Значение выражения равно: {y}')