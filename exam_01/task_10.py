# 10. Вывести на экран числа от 0 до 50, кроме 35.

# Вариант 1.
# i = -1
# while i <= 49:
#     i += 1
#     if i == 35:
#         continue
#     print(i)

# Вариант 2.
for i in range(51):
    if i == 35:
        continue
    print(i)
