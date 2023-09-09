# 3. Класс NumberList. Напишите программу, в которой описан класс. У объектов класса должно быть поле,
# представляющее собой числовой список. Этот список формируется на основе списка,
# переданного конструктору в качестве аргумента. При этом из списка-аргумента в
# список-поле включаются только числовые элементы (элементы других типов игнорируются).
# Необходимо также описать метод, отображающий содержимое поля списка, а также метод,
# вычисляющий среднее значение элементов поля списка (сумма значений элементов, деленная
# на их количество).

class NumberList:
    lst = []

    def __init__(self, list1=lst):
        self.list1 = list1

    def show_list(self):
        new_list = [i for i in self.list1 if type(i) == int]
        return new_list

    def output_data(self):
        sum_of_num = 0
        new_list1 = [i for i in self.list1 if type(i) == int]
        for i in new_list1:
            sum_of_num += i
            arith_mean = sum_of_num / len(new_list1)
            return arith_mean


number_list1 = NumberList([9, 8, {12: 4}, 12, 'k', 67, 'k', 'l'])
number_list2 = NumberList([110, 'hello', [60, 13, 76], 67, (25, 8)])

for i in (number_list1, number_list2):
    print(i.show_list())
    print(i.output_data())
