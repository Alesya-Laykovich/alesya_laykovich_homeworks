# 5. Есть словарь песен группы Depeche Mode violator songsdict = { 'World in My Eyes': 4.76,
# 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
# Выведите общее время звучания всех песен. Создайте список песен, время звучаниях которых
# больше 5 минут Создайте новый словарь тех песен, в название которых состоит из одного слова

violator_songdict = {'World in My Eyes': 4.76,
            'Sweetest Perfection': 5.43,
            'Personal Jesus': 4.56,
            'Halo': 4.30,
            'Waiting for the Night': 6.07,
            'Enjoy the Silence': 4.6,
            'Policy of Truth': 4.88,
            'Blue Dress': 4.18,
            'Clean': 5.68}
songs_length = 0
new_dict = {}
for key, values in violator_songdict.items():
    songs_length += values
    if values > 5:
        new_dict.update({key: values})
print(f'Общее время звучания всех песен: {songs_length}')
print(f'Список песен, время звучаниях которых больше 5 минут: {list(new_dict)}')
new_1 = dict()
for key, values in violator_songdict.items():
    if ' ' not in key:
        new_1.update({key: values})
print(f'Словарь песен, название которых состоит из одного слова: {new_1}')


# songs_length = 316 + 343 + 296 + 270 + 367 + 300 + 328 + 258 + 368
# print(f'Общее время звучания всех песен: {songs_length / 60}')