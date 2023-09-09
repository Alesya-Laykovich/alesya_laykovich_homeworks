# 1. Создать 4 фрукта. Апельсин, яблоко, мандарин, банан. У всех фруктов есть сорт,
# список витаминов, цена, имя. У апельсина, мандарина, банана есть метод очистить. У яблока -
# метод порезать. У банана есть характеристика: кол-во калия. Создать 4 объекта фрукта и использовать
# все доступные методы и характеристики. При вызове метода очистить, должно писаться имя фрукта
# Например: `apple = Apple("sort", [a,b,c], 120, "apple")`
# `apple.clear()`
# `>>"apple очищен"`

from abc import ABC, abstractmethod


class Fruit(ABC):

    def __init__(self, name, sort, vitamins_list, price):
        self.name = name
        self.sort = sort
        self.vitamins_list = vitamins_list
        self.price = price

    @abstractmethod
    def clear(self):
        pass


class Orange(Fruit):

    def __init__(self, name, sort, vitamins_list, price):
        super().__init__(name, sort, vitamins_list, price)

    def clear(self):
        return f'{self.name} очищен'


class Apple(Fruit):

    def __init__(self, name, sort, vitamins_list, price):
        super().__init__(name, sort, vitamins_list, price)

    def cut(self):
        return f'{self.name} нарезано'

    def clear(self):
        return f'{self.name} очищен'

class Tangerine(Fruit):

    def __init__(self, name, sort, vitamins_list, price):
        super().__init__(name, sort, vitamins_list, price)

    def clear(self):
        return f'{self.name} очищен'


class Banana(Fruit):

    def __init__(self, name, sort, vitamins_list, price, potassium_amount):
        super().__init__(name, sort, vitamins_list, price)
        self.potassium_amount = potassium_amount

    def clear(self):
        return f'{self.name} очищен'


apple = Apple("Яблоко", "Голден", ['C', 'B1', 'B2', 'P', 'E'], 5)
orange = Orange('Апельсин', 'Валенсия', ['A', 'B1', 'B2', 'PP', 'C'], 6)
tangerine = Tangerine('Мандарин', 'Клементин', ['A', 'D', 'E', 'K', 'P', 'C'], 8)
banana = Banana('Банан', 'Плантайн', ['B1', 'B2', 'B6', 'C', 'PP', 'K', 'MG'], 4, 360)

print(f'{apple.name}: сорт - {apple.sort}, список витаминов - {apple.vitamins_list}, цена за кг - '
      f' {apple.price}')
print(apple.cut(), apple.clear())

print(f'{orange.name}: сорт - {orange.sort}, список витаминов - {orange.vitamins_list}, цена за кг - '
      f' {orange.price}')
print(orange.clear())

print(f'{tangerine.name}: сорт - {tangerine.sort}, список витаминов - {tangerine.vitamins_list}, '
      f'цена за кг - {tangerine.price}')
print(tangerine.clear())

print(f'{banana.name}: сорт - {banana.sort}, список витаминов - {banana.vitamins_list}, цена за кг - '
      f'{banana.price},количество калия  в одном банане - {banana.potassium_amount}')
print(banana.clear())
