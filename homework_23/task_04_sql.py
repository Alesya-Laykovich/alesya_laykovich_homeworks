"""4) Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
Заполнить её с помощью INSERT данными (3 записи).
Удалить с помощью DELETE 2 запись. Обновить значения 3-ей записи на:
hello world с помощью UPDATE
*Записать данные с таблицы в файл в три колонки. Первая – id, вторая и третья с данными."""

import mysql.connector as mysql
import csv

connection = mysql.connect(
    host='localhost',
    user='root',
    password='DfbDTuZG1DfbDTuZG1',
    database='hw_23_task_04_sql'
)
cursor = connection.cursor()
cursor.execute("""CREATE DATABASE IF NOT EXISTS hw_23_task_04_sql""")
# cursor.execute("""SHOW DATABASES""")
# print(cursor.fetchall())

name = input('Введите имя: ')
password = input('Введите пароль: ')

cursor.execute("""CREATE TABLE IF NOT EXISTS table1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), 
password VARCHAR(20))""")
# cursor.execute("""SHOW TABLES""")
# print(cursor.fetchall())


cursor.execute("""INSERT INTO table1 (name, password) VALUES (%s, %s)""", (name, password))
connection.commit()
cursor.execute("""SELECT * FROM table1""")
result = cursor.fetchall()
print(result)

delete_id2 = """DELETE FROM table1 WHERE id=2"""
cursor.execute(delete_id2)
connection.commit()

update_id3 = """UPDATE table1 SET name='hello world', password='hello world' WHERE id=3"""
cursor.execute(update_id3)
connection.commit()
cursor.execute("""SELECT * FROM table1""")
print(cursor.fetchall())

with open('task_04_sql.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([id, name, password])
