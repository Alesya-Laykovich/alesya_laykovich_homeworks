"""4) Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
Заполнить её с помощью INSERT данными (3 записи).
Удалить с помощью DELETE 2 запись. Обновить значения 3-ей записи на:
hello world с помощью UPDATE
*Записать данные с таблицы в файл в три колонки. Первая – id, вторая и третья с данными."""

import csv
import sqlalchemy as db

meta = db.MetaData()
user = db.Table('User', meta,
                db.Column('id', db.Integer, primary_key=True),
                db.Column('name', db.Text, nullable=True),
                db.Column('password', db.Text, nullable=True))

print(user.c)

engine = db.create_engine('mysql+mysqlconnector://root:DfbDTuZG1DfbDTuZG1@localhost:3306/hw_23_task_04')
meta.create_all(engine)
connection = engine.connect()

name = input('Введите имя: ')
password = input('Введите пароль: ')
add_query = user.insert().values(name=name, password=password)
connection.execute(add_query)
connection.commit()

delete_id2 = user.delete().where(user.c.id == 2)
result = connection.execute(delete_id2)
connection.commit()

update_query = user.update().values(name='hello world', password='hello world').where(user.c.id == 3)
connection.execute(update_query)

search_ = db.select(user)
con_execute = connection.execute(search_)
print(con_execute.fetchall())

connection.close()


with open('task_04_0.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=';')

    writer.writerow([id, name, password])
