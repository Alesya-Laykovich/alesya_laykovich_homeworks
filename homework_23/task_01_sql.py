import mysql.connector as mysql
import random

connection = mysql.connect(
    host='localhost',
    user='root',
    password='DfbDTuZG1DfbDTuZG1',
    database='hw_23_task_01_sql'
)
cursor = connection.cursor()
cursor.execute("""CREATE DATABASE IF NOT EXISTS hw_23_task_01_sql""")
# cursor.execute("""SHOW DATABASES""")
# print(cursor.fetchall())

num_1 = random.randint(0, 9)
num_2 = random.randint(0, 9)

cursor.execute("""CREATE TABLE IF NOT EXISTS table1 (id INT AUTO_INCREMENT PRIMARY KEY, num_1 INT, num_2 INT)""")
# cursor.execute("""SHOW TABLES""")
# print(cursor.fetchall())


cursor.execute("""INSERT INTO table1 (num_1, num_2) VALUES (%s, %s)""", (num_1, num_2))
connection.commit()
cursor.execute("""SELECT num_1, num_2 FROM table1""")
result = cursor.fetchall()
print(result)
total_sum = 0
for i in result:
    total_sum += sum(i)
arith_mean = total_sum / (len(result) * 2)

print(f'Среднее арифметическое равно {arith_mean}')
print(f'Длина БД: {len(result)}')

if arith_mean > len(result):
    sqlformula_for_delete = """DELETE FROM table1 WHERE id=4"""
    cursor.execute(sqlformula_for_delete)
    connection.commit()
cursor.execute("""SELECT * FROM table1""")
print(cursor.fetchall())

cursor.close()
connection.close()
