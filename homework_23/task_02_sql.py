"""" 2) Создайте новую Базу данных: Поля: id, 2 целочисленных поля, Целочисленные поля
заполняются рандомно от 0 до 9. Выберите случайную запись из БД. Если каждое число данной записи
чётное, то удалите эту запись, если нечётное, то обновите данные в ней на(2,2)"""

import mysql.connector as mysql
import random

connection = mysql.connect(
    host='localhost',
    user='root',
    password='DfbDTuZG1DfbDTuZG1',
    database='hw_23_task_02_sql'
)
cursor = connection.cursor()
cursor.execute("""CREATE DATABASE IF NOT EXISTS hw_23_task_02_sql""")
# cursor.execute("""SHOW DATABASES""")
# print(cursor.fetchall())

num_1 = random.randint(0, 9)
num_2 = random.randint(0, 9)
cursor.execute("""CREATE TABLE IF NOT EXISTS table1 (id INT AUTO_INCREMENT PRIMARY KEY, num_1 INT, num_2 INT)""")
# cursor.execute("""SHOW TABLES""")
# print(cursor.fetchall())


cursor.execute("""INSERT INTO table1 (num_1, num_2) VALUES (%s, %s)""", (num_1, num_2))
connection.commit()
cursor.execute("""SELECT * FROM table1""")
result = cursor.fetchall()
print(result)
choice = random.choice(result)
print(choice)

if choice[0] % 2 == 0 and choice[1] % 2 == 0 and choice[2] % 2 == 0:
    index = choice[0]
    sqlformula_for_delete = """DELETE FROM table1 WHERE id=%s"""
    cursor.execute(sqlformula_for_delete, (index,))
#     # connection.commit()
else:
    index = choice[0]
    sqlformula_for_update = """UPDATE table1 SET num_1=2, num_2=2 WHERE id=%s"""
    cursor.execute(sqlformula_for_update, (index,))
    # connection.commit()
#
cursor.execute("""SELECT * FROM table1""")
print(cursor.fetchall())

cursor.close()
connection.close()
