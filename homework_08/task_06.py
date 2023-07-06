# 6. Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} ->
# {‘key3’: ‘value’}). Чтобы получить список ключей - использовать метод .keys()

dictionary_1 = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}

for key in list(dictionary_1.keys()):
    new_key = key + str(len(key))
    dictionary_1[new_key] = dictionary_1.pop(key)
print(f'Новый словарь: {dictionary_1}')
