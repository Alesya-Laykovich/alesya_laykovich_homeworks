# 3. Написать функцию, которая определяет количество разрядов введенного целого числа.
def digit_order_num(new):
    i = 0
    while new != 0:
        new //= 10
        i += 1
    return i


num = int(input('Введите число: '))
print(f'Количество разрядов: {digit_order_num(num)}')
