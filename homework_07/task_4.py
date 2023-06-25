# 4. Даны два целых числа m и n. Напишите программу, которая выводит все числа
# от m до n включительно в порядке возрастания, если m<n,
# или в порядке убывания в противном случае.

m = int(input('Введите первое число: '))
n = int(input('Введите второе число: '))

list1 = []
list2 = []
if m < n:
    for i in range(m, n+1):
        list1.append(i)
        list1.sort(reverse=True)
    print(list1)
else:
    for i in range(n, m+1):
        list2.append(i)
        list2.sort()
    print(list2)
