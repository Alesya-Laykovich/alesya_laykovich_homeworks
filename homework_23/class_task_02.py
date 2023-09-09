"""2) Вы разрабатываете систему управления студентами для университета.
У вас есть база данных, в которой хранятся данные о студентах. Вам необходимо написать программу,
используя SQLAlchemy, которая выберет и выведет список имен всех студентов, учащихся на вашем факультете."""

import sqlalchemy as db

meta = db.MetaData()
user = db.Table('User', meta,
                db.Column('name', db.Text, nullable=True),
                db.Column('surname', db.Text, nullable=True),
                db.Column('faculty', db.Text, nullable=True))

print(user.c)

engine = db.create_engine('mysql+mysqlconnector://root:DfbDTuZG1DfbDTuZG1@localhost:3306/students_db')
meta.create_all(engine)
connection = engine.connect()
name = input('Введите имя студента: ')
surname = input('Введите фамилию студента: ')
faculty = input('Введите факультет: ')
add_query = user.insert().values(name=name, surname=surname, faculty=faculty)
connection.execute(add_query)
connection.commit()

select_all_query = db.select(user)
result = connection.execute(select_all_query)
print(result.fetchall())

search_faculty = db.select(user.c.name, user.c.surname).where(user.c.faculty == 'ФИКИТ')
result = connection.execute(search_faculty)
print(result.fetchall())
