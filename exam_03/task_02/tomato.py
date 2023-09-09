"""1.	Создайте класс Tomato
2.	Создайте статический атрибут states, который будет содержать все стадии созревания помидора
3.	Создайте метод __init__(), внутри которого будут определены два приватных атрибута: 1) _index -
передается параметром и 2) _state - принимает первое значение из словаря states
4.	Создайте метод grow(), который будет переводить томат на следующую стадию созревания
5.	Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)."""


class Tomato:
    states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}

    def __init__(self, index):
        self.__index = index
        self.__state = self.states['Отсутствует']

    def grow(self):
        if self.__state < 3:
            self.__state += 1

    def is_ripe(self):
        if self.__state == 3:
            return True
        else:
            return False


# tomato = Tomato(2)
# tomato.grow()
# tomato.grow()
# tomato.grow()
#
# print(tomato.is_ripe())
