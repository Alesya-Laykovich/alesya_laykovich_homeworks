"""1)	Требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
Для этого создайте класс TriangleChecker, принимающий только положительные числа. С помощью метода is_triangle()
возвращаются следующие значения (в зависимости от ситуации):
●	Ура, можно построить треугольник!
●	С отрицательными числами ничего не выйдет!
●	Жаль, но из этого треугольник не сделать. """


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)) or \
                not isinstance(self.c, (int, float)):
            return 'Значения сторон должны быть числами.'
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 'Значения сторон должны быть только положительными числами.'
        elif self.a > self.b + self.c or self.b > self.a + self.c or self.c > self.a + self.b:
            return 'Жаль, но из этого треугольник не сделать.'
        else:
            return 'Ура, можно построить треугольник!'


triangle1 = TriangleChecker(3, 2, (14,))
print(triangle1.is_triangle())
triangle2 = TriangleChecker(3, 8, 4)
print(triangle2.is_triangle())
triangle3 = TriangleChecker(3, 2, 4)
print(triangle3.is_triangle())
triangle4 = TriangleChecker(-3, 2, 2)
print(triangle4.is_triangle())
