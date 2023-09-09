"""1.	Создайте класс House
2.	Создайте метод __init__() и определите внутри него два атрибута: _area и _price. Свои начальные значения они
получают из параметров метода __init__()
3.	Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учетом
данной скидки.
1.	Создайте класс SmallHouse, унаследовав его функционал от класса House
2.	Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2"""
from human import Human


class House:
    @classmethod
    def __init__(cls, area, price):
        cls._area = area
        cls._price = price

    def final_price(self, discount):
        price_with_discount = self._price - discount
        return price_with_discount


house = House(50, 20000)
# print(house.final_price(199))


class SmallHouse(House):
    def __init__(self):
        super().__init__(40, house._price)


print(Human.default_info(Human))
human = Human('Ann', 43)
print(human.info())

house1 = SmallHouse()
print(human.buy_house(900))
human.earn_money(300)
print(human.buy_house(900))
