"""" 2) Создайте новую Базу данных: Поля: id, 2 целочисленных поля, Целочисленные поля
заполняются рандомно от 0 до 9. Выберите случайную запись из БД. Если каждое число данной записи
чётное, то удалите эту запись, если нечётное, то обновите данные в ней на(2,2)"""

import sqlalchemy as db
import random

meta = db.MetaData()
user = db.Table('User', meta,
                db.Column('id', db.Integer, primary_key=True),
                db.Column('num_1', db.Integer, nullable=True),
                db.Column('num_2', db.Integer, nullable=True))

engine = db.create_engine('mysql+mysqlconnector://root:DfbDTuZG1DfbDTuZG1@localhost:3306/hw_23_task_02')
meta.create_all(engine)
connection = engine.connect()

num_1 = random.randint(0, 9)
num_2 = random.randint(0, 9)
add_query = user.insert().values(num_1=num_1, num_2=num_2)
connection.execute(add_query)
connection.commit()

search_ = db.select(user)
con_execute = connection.execute(search_)
result = con_execute.fetchall()

choice = random.choice(result)
print(result)
print(choice)
if choice[0] % 2 == 0 and choice[1] % 2 == 0 and choice[2] % 2 == 0:
    d = user.delete().where(user.c.id == choice[0])
    result = connection.execute(d)
else:
    update_query = user.update().values(num_1=2, num_2=2).where(user.c.id == choice[0])
    connection.execute(update_query)

select_all_query = db.select(user)
result1 = connection.execute(select_all_query)
print(result1.fetchall())
