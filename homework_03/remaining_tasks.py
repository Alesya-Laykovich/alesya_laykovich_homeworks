# Это оставшиеся 2 задачи, которые я не успела выполнить. Если будет время,посмотрите, пожалуйста.

# Задание №5. Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 2-мя способами
name = input('Введите имя: ')
age = input('Введите возраст: ')
city = input('Введите город: ')

my_string = f"Let's get aсquainted! My name is {name}. I'm {age} years old. I'm from {city}."
print(my_string)

new_string = "Let's get aсquainted! My name is {0}. I'm {1} years old. I'm from {2}."
print(new_string.format(name, age, city))

# Задание № 6. Посчитайте, сколько раз определенный символ встречается в строке.
# Символ вводим с клавиатуры.
phrase = input('Введите фразу: ')
symbol = input('Введите символ: ')
print(phrase.count(symbol))
