# 2. Создайте класс Soda (для определения типа газированной воды),
# принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}»
# в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».
class Soda:
    default_ingredient = None

    def __init__(self, ingredient=default_ingredient):
        self.ingredient = ingredient

    def show_my_drink(self):
        if self.ingredient:
            return f'Газировка и {self.ingredient}'
        else:
            return 'Обычная газировка'


soda1 = Soda()
soda2 = Soda('Lemon')
print(soda1.show_my_drink())
print(soda2.show_my_drink())
