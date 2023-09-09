"""1.	Создайте класс TomatoBush
2.	Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе
будет создавать список объектов класса Tomato. Данный список будет храниться внутри атрибута tomatoes.
3.	Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
4.	Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
5.	Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая."""
from exam_03.task_02.tomato import Tomato


class TomatoBush:
    def __init__(self, tomato_num):
        self.tomatoes = []
        for i in range(1, tomato_num + 1):
            self.tomatoes.append(Tomato(i))

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        for i in self.tomatoes:
            i.is_ripe()
            if i.is_ripe():
                return True
            else:
                return False

    def give_away_all(self):
        return self.tomatoes.clear()


# tomato_bush = TomatoBush(2)
# tomato_bush.grow_all()
# tomato_bush.grow_all()
# tomato_bush.grow_all()
#
# print(tomato_bush.all_are_ripe())
