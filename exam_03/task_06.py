"""6) Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять методов: getName, getAge,
getGroupNumber, setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени конкретного студента,
метод getAge нужен для получения данных о возрасте конкретного студента, метод setGroupNumber нужен для получения
данных о номере группы конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов установленных
по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. В программе необходимо
создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы."""


class Student:
    def __init__(self, name='Ivan', group_number='10A', age=18):
        self.name = name
        self.group_number = group_number
        self.age = age

    def info(self):
        return f"Данные о студенте:\nИмя - {self.name}\nНомер группы - {self.group_number}\nВозраст - {self.age}"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_group_number(self, name):
        self.name = name
        return f'{self.group_number}'

    def set_age(self, age):
        self.age = age
        return self.age

    def set_group_number(self, group_number):
        self.group_number = group_number
        return self.group_number


student1 = Student('Irina', '6A', 12)
student2 = Student('Pavel', '11A', 17)
student3 = Student('Diana', '10B', 16)
student4 = Student('Alex', '11A', 18)
student5 = Student('Anna', '6A', 12)
new_list = [student1, student2, student3, student4, student5]

print(new_list[1].get_name())
new_list[3].set_group_number('7t')
new_list[3].set_age(13)
print(new_list[3].info())
