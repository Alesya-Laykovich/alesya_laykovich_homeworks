"""1.	Создайте класс Gardener
2.	Создайте метод __init__(), внутри которого будут определены два атрибута: 1) name - передается параметром,
является публичным и 2) _plant - принимает объект класса TomatoBush, является приватным
3.	Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
4.	Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
Если нет - метод печатает предупреждение.
5.	Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству."""
from exam_03.task_02.tomato_bush import TomatoBush


class Gardener:
    def __init__(self, name):
        self.name = name
        self.__plant = tomato_bush

    def work(self):
        self.__plant.grow_all()

    def harvest(self):
        if self.__plant.all_are_ripe():
            return 'Урожай собран!'
        else:
            return 'Томаты еще не дозрели'

    @staticmethod
    def knowledge_base():
        return 'Советы, как ухаживать за помидорами:' \
               '\nПомидоры нуждаются в хорошем освещении, не менее 12 часов в сутки. ' \
               '\nНеобходимо регулярное проветривание и своевременный полив.'


# print(Gardener.knowledge_base())
tomato_bush = TomatoBush(3)

gardener = Gardener('Anna')

print(gardener.knowledge_base())
gardener.work()
print(gardener.harvest())
gardener.work()
print(gardener.harvest())
gardener.work()
print(gardener.harvest())
