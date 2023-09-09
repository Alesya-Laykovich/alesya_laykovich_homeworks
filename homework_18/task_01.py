# 1. Напишите класс Pet (Домашнее животное), который должен иметь приведенные ниже атрибуты данных:
# __name (Для клички домашнего животного)
# __animal_type (Для типа домашнего животного, например, это может быть ‘собака’)
# __age (Для возраста домашнего животного)
#
# Класс Pet должен иметь метод __init__(), который создает эти атрибуты. Он также
# должен иметь приведенные ниже методы:
#
# - метод set_ name() присваивает значение полю __name;
# - метод set_animal_type() присваивает значение полю __animal_ type;
# - метод set_age() присваивает значение полю __age
# - метод get_name() возвращает значение поля __name;
# - метод get_animal_type() возвращает значение поля __animal_ type
# - метод get_age() возвращает значение поля __age
#
# После написания данного класса напишите программу, которая создает объект класса и
# предлагает пользователю ввести кличку, тип и возраст своего домашнего животного. Эти
# данные должны храниться в качестве атрибутов объекта. Примените методы,
# чтобы извлечь имя, тип и возраст домашнего животного и показать эти данные на экране.

class Pet:

    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


input_name = input('Введите кличку животного: ')
input_type = input('Введите тип животного: ')
input_age = input('Введите возраст животного: ')

pet = Pet(input_name, input_type, input_age)
print(f'{pet.get_name()} is a {pet.get_animal_type()}, {pet.get_age()} years old')
