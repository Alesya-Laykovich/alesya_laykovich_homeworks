"""1) Создайте новую Базу данных. В ней создайте таблицу с тремя полями,
два текстовых, одно – целое число.
Число запрашивается с клавиатуры, а слова задаются статически.
Выведите каждую запись в отдельную строку.( без круглых круглых скобочек)

Пример
Содержимое бд

[(hello, world, 2), (hello2, world2, 3)]
Результат работы нашей программы
hello, world, 2
hello2, world2, 3"""

import mysql.connector as mysql

connection = mysql.connect(
    host='localhost',
    user='root',
    password='DfbDTuZG1DfbDTuZG1',
    database='new_db_people_sql'
)
cursor = connection.cursor()
cursor.execute("""CREATE DATABASE IF NOT EXISTS new_db_people_sql""")
cursor.execute("""SHOW DATABASES""")
print(cursor.fetchall())

age = int(input('Введите возраст: '))

cursor.execute("""CREATE TABLE IF NOT EXISTS table2 (Name VARCHAR(10), Surname VARCHAR(10), Age INT)""")
# cursor.execute("""SHOW TABLES""")
# print(cursor.fetchall())


cursor.execute("""INSERT INTO table2 (Name, Surname, Age) VALUES ('Alesya', 'Laykovich', %s)""", (age,))
connection.commit()
cursor.execute("""SELECT * FROM table2""")
result = cursor.fetchall()
print(result)
for i in result:
    string = ', '.join(str(j) for j in i)
    print(string)
connection.close()

