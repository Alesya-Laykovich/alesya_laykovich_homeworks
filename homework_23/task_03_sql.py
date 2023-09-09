"""3) Создайте метод класса для работы с БД. В БД: Если передан 1 аргумент, вставить в таблицу
запись с числом 3. Если переданы 2 аргумента: проверить, что второй аргумент является числом.
Если условие верно, то удалить первую запись с БД. Если переданы 2 аргумента, их значения не
известны, а 3 является числом, то обновить на число 77 запись 3."""

import mysql.connector as mysql


class DataBaseManager:
    def __init__(self):
        self.connection = mysql.connect(
            host='localhost',
            user='root',
            password='DfbDTuZG1DfbDTuZG1',
            database='hw_23_task_03_sql'
        )
        self.cursor = self.connection.cursor()

    def create_database(self):
        self.cursor.execute("""CREATE DATABASE IF NOT EXISTS hw_23_task_03_sql""")

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user (id INT AUTO_INCREMENT PRIMARY KEY, value INT(9))""")

    def insert_one_arg(self, value):
        self.cursor.execute('INSERT INTO user (value) VALUES (%s)', (value,))
        self.connection.commit()
        self.cursor.execute('SELECT * FROM user')
        print(self.cursor.fetchall())

    def insert_two_args(self, value1, value2):
        if type(value2) == int:
            self.cursor.execute('DELETE FROM user WHERE id=1')
            self.connection.commit()
            self.cursor.execute('SELECT * FROM user')
            print(self.cursor.fetchall())
        else:
            self.connection.close()

    def update(self, old_value, new_value=77):
        self.cursor.execute('UPDATE user SET value=%s WHERE value=%s', (new_value, old_value))
        self.connection.commit()
        self.cursor.execute('SELECT * FROM user')
        print(self.cursor.fetchall())


db = DataBaseManager()
db.create_database()
db.create_table()
db.insert_one_arg(3)
db.insert_two_args(2, 2)