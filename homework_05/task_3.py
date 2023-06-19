# 3. Вывести на экран все чётные значения в диапазоне от 1 до 497.
even_numbers = []
for i in range(1, 497):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)
