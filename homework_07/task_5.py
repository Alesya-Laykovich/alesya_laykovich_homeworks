# 5. Заполнить список ста нулями, кроме первого и последнего элементов,
# которые должны быть равны единице.

# Вариант 1.
list1 = [0] * 100
# print(list1)
list1[0] = 1
list1[-1] = 1
print(list1)

# Вариант 2.
list1 = [0] * 99
# print(list1)
list1.append(1)
list1[0] = 1
print(list1)
