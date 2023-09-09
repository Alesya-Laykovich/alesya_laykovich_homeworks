"""1) Создайте новую Базу данных. Поля: id, 2 целочисленных поля.
Целочисленные поля заполняются рандомно от 0 до 9.
Посчитайте среднее арифметическое всех элементов без учёта id.
Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД"""

import sqlalchemy as db
import random

meta = db.MetaData()
user = db.Table('User', meta,
                db.Column('id', db.Integer, primary_key=True),
                db.Column('num_1', db.Integer, nullable=True),
                db.Column('num_2', db.Integer, nullable=True))

# print(user.c)

engine = db.create_engine('mysql+mysqlconnector://root:DfbDTuZG1DfbDTuZG1@localhost:3306/hw_23_task_01')
meta.create_all(engine)
connection = engine.connect()

num_1 = random.randint(0, 9)
num_2 = random.randint(0, 9)
add_query = user.insert().values(num_1=num_1, num_2=num_2)
connection.execute(add_query)
connection.commit()

search_ = db.select(user)
result = connection.execute(search_)
final_result = result.fetchall()
total_sum = 0
for i in final_result:
    total_sum += sum(i)
arith_mean = total_sum / (len(final_result) * 2)
print(f'Среднее арифметическое равно {arith_mean}, {total_sum}')
print(f'Длина БД: {len(final_result)}')

if arith_mean > len(final_result):
    delete_query_for_id = user.delete().where(user.c.id == 4)
    result = connection.execute(delete_query_for_id)
    # connection.commit()

search_ = db.select(user)
result = connection.execute(search_)
print(result.fetchall())

connection.close()
