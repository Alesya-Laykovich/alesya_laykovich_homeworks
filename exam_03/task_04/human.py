"""1.	Создайте класс Human.
2.	Определите для него два статических атрибута: default_name и default_age.
3.	Создайте метод __init__(), который помимо self принимает еще два параметра: name и age. Для этих параметров
задайте значения по умолчанию, используя атрибута default_name и default_age. В методе __init__()
определите четыре атрибута: Публичные - name и age. Приватные - money и house.
4.	Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
5.	Реализуйте справочный статический метод default_info(), который будет выводить статические атрибуты default_name
и default_age.
6.	Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома:
уменьшать количество денег на счету и присваивать ссылку на только что купленный дом. В качестве аргументов данный
метод принимает объект дома и его цену.
7.	Реализуйте метод earn_money(), увеличивающий значение свойства money.
8.	Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и совершать
сделку. Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка на дом и
размер скидки"""


class Human:
    default_name = 'Name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 800
        self.__house = 'House'

    def info(self):
        return f'Информация о покупателе:\nИмя - {self.name}\nВозраст - {self.age}\n' \
               f'Наличие денег - {self.__money}\nНаличие собственного жилья - {self.__house}'

    def default_info(self):
        return self.default_name, self.default_age

    def __make_deal(self, price):
        house = 'Small house'
        self.__money -= price
        return f"'{house}' куплен, на вашем счету осталось {self.__money}"

    def earn_money(self, salary):
        self.__money += salary

    def buy_house(self, house_fee):
        house = 'Small House'
        if house_fee < self.__money:
            return f'Поздравляем, Вы совершили покупку {house}! Остаток на балансе: {self.__money - house_fee}'
        else:
            return 'На Вашем балансе недостаточно средств для совершения покупки'


# human = Human('Ann', 13)
# print(human.info())
# print(human._Human__make_deal('penthouse', 200))
# human.earn_money(1100)
# print(human.buy_house(900))
