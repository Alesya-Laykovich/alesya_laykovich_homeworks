"""4. В зависимости от выбора пользователя вычислить площадь круга, прямоугольника или
треугольника. Для вычисления площади каждой фигуры должна быть написана отдельная функция."""

import math
input_inf = int(input('Введите "1", если Вы хотите найти площадь круга, "2" - если прямоугольника, '
                      '3 - если площадь треугольника: '))
if input_inf == 1:
    def circle(number):
        r = int(input('Введите чему равен радиус круга: '))
        S = math.pi * (r**2)
        return f'Площадь круга: {S}'
    print(circle(input_inf))
elif input_inf == 2:
    def rectangle(number):
        a = int(input('Введите длину прямоугольника: '))
        b = int(input('Введите ширину прямоугольника: '))
        S = a * b
        return f'Площадь прямоугольника: {S}'
    print(rectangle(input_inf))
elif input_inf == 3:
    def triangle(number):
        a = int(input('Введите длину первой стороны треугольника: '))
        b = int(input('Введите длину второй стороны треугольника: '))
        alpha = int(input('Введите угол между сторонами "a" и "b": '))
        S = 0.5 * a * b * math.sin(alpha)
        return f'Площадь прямоугольника: {S}'
    print(triangle(input_inf))

