"""Создайте класс Employee, представляющий сотрудника компании.
Каждый сотрудник имеет имя и должность. Реализуйте магический метод __new__ для класса Employee,
чтобы гарантировать, что только один экземпляр класса может быть создан для каждой должности.
Таким образом, если два сотрудника имеют одну и ту же должность, то они будут
ссылаться на один и тот же экземпляр класса Employee."""


class Employee:
    __instance = None
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, job_title):
        if not self.__initialized:
            self.name = name
            self.job_title = job_title
            self.__initialized = True

    def disclose_inf(self):
        print(f'{self.name} is a {self.job_title}')



# class CEO:
#     def __init__(self, name, job_title):
#         self.name = name
#         self.job_title = job_title
#
#     def disclose_inf(self):
#         print(f'{self.name} is a {self.job_title}')


employee1 = Employee('Masha', 'Manager')
employee2 = Employee('Kate', 'Manager')
employee3 = Employee('Dima', 'Manager')
# ceo1 = CEO('Sergei', 'CEO')
# ceo2 = CEO('Jules', 'CEO')

# print(id(employee1), id(employee2), id(employee3))
# print(id(ceo1), id(ceo2))
employee1.disclose_inf()
employee2.disclose_inf()
employee3.disclose_inf()
# ceo1.disclose_inf()
# ceo2.disclose_inf()
