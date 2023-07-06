# 5. Выведите статистику частности букв в кортеже
# long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и’,'и', 'и', 'т', 'т', 'а', 'и', 'и','и', 'и', 'и', 'т', 'и')
# Примечание: Статистика частности - число повторений каждой из букв.

long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
new_list1 = []

for i in long_word:
    if i in long_word and i not in new_list1:
        new_list1.append(i)

new_list2 = []
for i in new_list1:
    new_list2.append(long_word.count(i))
print(new_list2)

dictionary = dict(zip(new_list1, new_list2))
print(dictionary)
