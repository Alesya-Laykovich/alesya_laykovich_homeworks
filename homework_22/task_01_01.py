import sqlalchemy as db

meta = db.MetaData()
user = db.Table('db_people', meta,
                db.Column('Name', db.Text, nullable=True),
                db.Column('Surname', db.Text, nullable=True),
                db.Column('age', db.Integer, nullable=True))

print(user.c)

engine = db.create_engine('mysql+mysqlconnector://root:DfbDTuZG1DfbDTuZG1@localhost:3306/new_db_people')
meta.create_all(engine)
connection = engine.connect()

age = int(input('Введите возраст: '))
add_query = user.insert().values(Name='Alesya', Surname='Laykovich', age=age)
connection.execute(add_query)
connection.commit()

select_all_query = db.select(user)
result = connection.execute(select_all_query)
for i in result:
    string = ', '.join(str(j) for j in i)
    print(string)
connection.close()
