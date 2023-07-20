# 2. Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).

with open('article.txt', 'r', encoding='utf-8') as file:
    list1 = file.readlines()
    list_split = [line.rstrip() for line in list1]
    print(list_split)
new_list = []
for word in list_split:
    words = word.split(' ')
    new_list.extend(words)
# print(new_list)
# max_length = max(new_list, key=len)
max_length = len(max(new_list, key=len))
new = []
for i in new_list:
    if len(i) == max_length:
        new.append(i)
print('Слово, имеющее максимальную длину:', *new)
print(f'Максимальное количество символов: {max_length}')


