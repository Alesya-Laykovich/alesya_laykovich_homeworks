"""2. Создайте программу, которая, принимая массив имён, возвращает строку описывающая
количество лайков (как в Facebook). Примеры:
likes() -> "no one likes this"
likes("Ann") -> "Ann likes this"
likes("Ann", "Alex") -> "Ann and Alex like this"
likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this"
likes("Ann", "Alex", "Mark", "Max") -> "Ann, Alex and 2 others like this" """


def likes_function(new_list):
    if len(new_list) == 0:
        return 'no one likes this'
    elif len(new_list) == 1:
        likes = ' '.join(new_list)
        return likes + ' likes this'
    elif len(new_list) == 2:
        likes = ' and '.join(new_list)
        return likes + ' like this'
    elif len(new_list) == 3:
        likes = ', '.join(new_list[0:2]) + ' and ' + new_list[-1]
        return likes + ' like this'
    else:
        likes1 = new_list[0:2]
        likes = ', '.join(likes1)
        return likes + ' and ' + str(len(new_list) - 2) + ' others like this'


input_inf = ['Alena', 'Vlad', 'Darya', 'Karina', 'Nikita']
print(likes_function(input_inf))
