# 6. В строке “Иван Иванов” поменяйте местами слова. Может быть предоставлена
# любая строка с именем и фамилией. Например, “Петр Иванов” => “Иванов Петр”

input_string = input('Введите имя и фамилию через пробел: ')
my_string = input_string.split(' ')
print(f'Фамилия и имя: {my_string[1]} {my_string[0]}')
