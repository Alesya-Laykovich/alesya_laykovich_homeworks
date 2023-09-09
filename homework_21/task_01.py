"""Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
успеваемость (список из пяти элементов). Создать класс School:
Добавить возможность для добавления студентов в школу.
Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
Добавить возможность вывода учеников заданной группы.
Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)"""


class Students:
    def __init__(self, surname_initials, group_number, academic_performance):
        self.surname_initials = surname_initials
        self.group_number = group_number
        self.academic_performance = academic_performance


class School:
    students = []

    def add_students(self, student):
        self.students.append(student)

    def get_average_grade(self):
        students_with_grades_five_six = {}
        for student in self.students:
            if (student.academic_performance.count(5) + student.academic_performance.count(6)) == 5:
                students_with_grades_five_six.update({student.surname_initials: student.group_number})
        return f'Студенты, имеющие оценки только 5 или 6: {students_with_grades_five_six}'

    def input_group(self, group_number):
        self.group_number = group_number
        group_students = []
        for student in self.students:
            if student.group_number == group_number:
                group_students.append(student.surname_initials)
        return f'Студенты группы {self.group_number}: {group_students}'
    def high_average_grade(self):
        students_with_high_grades = []
        for student in self.students:
            average_grade = sum(student.academic_performance) / len(student.academic_performance)
            if average_grade >= 7:
                students_with_high_grades.append(student.surname_initials)
        return f'Студенты, претендующие на автомат: {students_with_high_grades}'


student1 = Students('Sanko M.M.', 20, [5, 9, 5, 8, 9])
student2 = Students('Kravets S.K.', 20, [5, 6, 6, 8, 5])
student3 = Students('Svetlova A.O.', 21, [6, 6, 6, 5, 6])
student4 = Students('Kripko V.P.', 20, [6, 7, 5, 8, 9])
student5 = Students('Andreev D.I.', 21, [5, 5, 6, 5, 6])

school = School()
school.add_students(student1)
school.add_students(student2)
school.add_students(student3)
school.add_students(student4)
school.add_students(student5)

print(school.get_average_grade())
print(school.input_group(20))
print(school.high_average_grade())
