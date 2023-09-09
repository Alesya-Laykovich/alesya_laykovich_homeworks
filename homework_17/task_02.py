# 2) Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента.
# Класс студен описан следующим образом:
#     class Student:
#         def __init__(self, name, money):
#            self.name = name
#            self.money = money
# Необходимо понять у кого больше всего денег и вернуть его имя.
# Если у студентов денег поровну вернуть: “all”.

class Student:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def student_name(self):
        return self.name

    def student_money(self):
        return self.money

student1 = Student('Misha', 34)
student2 = Student('Masha', 34)
student3 = Student('Anna', 34)

lst_name = []
for i in (student1, student2, student3):
    lst_name.append(i.student_name())
# print(lst_name)

lst_money = []
for i in (student1, student2, student3):
    lst_money.append(i.student_money())
# print(lst)_money

dct = dict(zip(lst_name, lst_money))
# print(dct)

def student_max_money():
    for key, value in dct.items():
        print(f'{key} has {value} rubles.')
        if dct['Misha'] == dct['Masha'] == dct['Anna']:
            return 'All students have the same  amount of money.'
        else:
            if max(lst_money) == value:
                return f'{key} has most of the money.'


print(student_max_money())
