# 2) Создайте класс Робот. Создайте 2 типа оружия: меч, автомат. Создайте 2 типа амуниции: броня,
# шлем. Добавьте оружию и амуниции свои характеристики(например урон, прочность). Создайте своего робота
# с каким либо оружием (может быть несколько и брони может быть несколько. Так же может быть ничего).
# Выведите весь арсенал робота на экран


class Robot:
    def __init__(self, name, arm=None, ammunition=None):
        self.name = name
        self.arm = arm
        self.ammunition = ammunition

    def arm_type(self, arm):
        self.arm = arm

    def ammunition_type(self, ammunition):
        self.ammunition = ammunition

    def robot_info(self):
        return f"Робот '{self.name}': оружие - {self.arm}; амуниция - {self.ammunition}"


class Arm:
    def __init__(self, name, durability, attack_damage, price):
        self.name = name
        self.durability = durability
        self.attack_damage = attack_damage
        self.price = price

    def __str__(self):
        return f'{self.name}: прочность ({self.durability}), урон ({self.attack_damage}), стоимость ({self.price})'


class Ammunition:
    def __init__(self, name, quality, price):
        self.name = name
        self.quality = quality
        self.price = price

    def __str__(self):
        return f'{self.name}: качество ({self.quality}), стоимость ({self.price})'


robot1 = Robot('HUM-4')
rifle = Arm('Rifle', 20, 5, 300)
robot1.arm_type(rifle)
armor = Ammunition('Armor', 4, 200)
robot1.ammunition_type(armor)

print(robot1.robot_info())


robot2 = Robot('St-17')
sword = Arm('Sword', 60, 5, 700)
robot2.arm_type(sword)
helmet = Ammunition('Helmet', 3, 100)
robot2.ammunition_type(helmet)

print(robot2.robot_info())
