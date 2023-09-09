"""Вы разрабатываете систему для учета инвентаря в магазине электроники. Вам необходимо создать
абстрактный класс Product, который будет представлять общие свойства всех товаров в магазине,
а также создать конкретные классы для различных типов продуктов.

Создайте абстрактный класс Product с методами и атрибутами:

Атрибут name (название продукта).
Атрибут price (цена продукта).
Абстрактный метод display_info(), который должен быть реализован в дочерних классах.
Создайте два конкретных класса, наследующихся от Product:

Класс Laptop:
Атрибут processor (процессор ноутбука).
Реализуйте метод display_info(), который выводит на экран информацию о ноутбуке.
Класс Phone:
Атрибут camera (разрешение камеры телефона).
Реализуйте метод display_info(), который выводит на экран информацию о телефоне."""

from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def display_info(self):
        pass


class Laptop(Product):
    def __init__(self, name, price, processor):
        super().__init__(name, price)
        self.processor = processor

    def display_info(self):
        return f'Информация о продукте: название - {self.name}, стоимость - {self.price}, процессор - {self.processor}'


class Phone(Product):
    def __init__(self, name, price, camera):
        super().__init__(name, price)
        self.camera = camera

    def display_info(self):
        return f'Информация о продукте: название - {self.name}, стоимость - {self.price}, разрешение камеры - {self.camera}'

laptop = Laptop('Lenovo', 1000, 'Core i5')
print(laptop.display_info())

phone = Phone('Apple', 1000, '48 Мп')
print(phone.display_info())

