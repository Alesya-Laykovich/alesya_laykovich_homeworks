"""3) Создайте метод класса для работы с БД. В БД: Если передан 1 аргумент, вставить в таблицу
запись с числом 3. Если переданы 2 аргумента: проверить, что второй аргумент является числом.
Если условие верно, то удалить первую запись с БД. Если переданы 2 аргумента, их значения не
известны, а 3 является числом, то обновить на число 77 запись 3."""

import sqlalchemy as db


class DataBaseManager:
    def __init__(self):
        self.meta = db.MetaData()
        self.user = db.Table('User', self.meta,
                             db.Column('id', db.Integer, primary_key=True),
                             db.Column('value', db.Integer, nullable=True)
                             )

        engine = db.create_engine('mysql+mysqlconnector://root:DfbDTuZG1DfbDTuZG1@localhost:3306/hw_23_task_03')
        self.meta.create_all(engine)
        self.connection = engine.connect()

    def insert_one_arg(self, value):
        add_query = self.user.insert().values(value=value)
        self.connection.execute(add_query)
        self.connection.commit()

        search_ = db.select(self.user)
        con_execute = self.connection.execute(search_)
        print(con_execute.fetchall())

    def insert_two_args(self, value1, value2):
        if type(value2) == int:
            delete_id1= self.user.delete().where(self.user.c.id == 1)
            result = self.connection.execute(delete_id1)
            self.connection.commit()

            search_ = db.select(self.user)
            con_execute = self.connection.execute(search_)
            print(con_execute.fetchall())
        else:
            self.connection.close()

    def update(self, new_value):
        update_query = self.user.update().values(value=77)
        self.connection.execute(update_query)

        search_ = db.select(self.user)
        con_execute = self.connection.execute(search_)
        print(con_execute.fetchall())


db1 = DataBaseManager()
db1.insert_one_arg(3)
db1.insert_two_args(2, 2)
db1.update(5)
