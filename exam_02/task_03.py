# 3. Создайте словарь из строки 'An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.
string = 'An apple a day keeps the doctor away'.lower()
lst_keys = []
lst_keys.extend(string)
# print(lst_keys)
new_dict = dict()
for i in lst_keys:
    new_dict[i] = lst_keys.count(i)
    # print(lst.count(i))
print(f'Словарь, где ключи - символы строки, а значения - количество вхождения данного символа:'
      f'\n{new_dict}')
