# 3. Создать пустую переменную. Проверить ее на истинность и ложность.
# Объясните полученный результат.

empty_var = None
print(f'Пустая переменная соответствует: {bool(empty_var)}')

# Пустой переменной соответствует булевое значение False, т.к. истинными не являются пустые
# значения переменных (None), 0, пустые строки, списки, кортежи, False.