from sqlalchemy import insert, select, or_, and_
from models import User, Address
from db import engine, Base

Base.metadata.create_all(engine)


def insert_one_user():
    stmt = insert(User).values(
        name='Johny',
        fullname='john Carter'
    )
    with engine.connect() as conn:
        conn.execute(stmt)


def insert_many_users(values):
    stmt = insert(User)
    with engine.connect() as conn:
        conn.execute(stmt, values)


# insert_one_user()
# values = [
#     {'name': 'Anna', 'fullname': 'Anna Karenina'},
#     {'name': 'Guido', 'fullname': 'Guido van Rossum'}
# ]
# values_2 = [
#     {'name': 'Dima', 'fullname': 'Dima Ermolovich', 'age': 13, 'gender': 'male'},
#     {'name': 'Vasya', 'fullname': 'Vasya Filatov', 'age': 17, 'gender': 'male'}
# ]
# values_3 = [
#     {'name': 'Igor', 'fullname': 'Igor_1', 'age': 43, 'gender': 'male'},
#     {'name': 'Oleg', 'fullname': 'Oleg_2', 'age': 12, 'gender': 'male'},
#     {'name': 'Vladimir', 'fullname': 'Vladimir_3', 'age': 53, 'gender': 'male'},
#     {'name': 'Kira', 'fullname': 'Kira_4', 'age': 65, 'gender': 'male'},
#     {'name': 'Vika', 'fullname': 'Vika_5', 'age': 13, 'gender': 'female'},
# ]
# values_4 = [
#     {'name': 'Hgor', 'fullname': 'Hgor_1', 'age': 88, 'gender': 'male'},
#     {'name': 'Lleg', 'fullname': 'Lleg_2', 'age': 32, 'gender': 'male'},
#     {'name': 'Hladimir', 'fullname': 'Hladimir_3', 'age': 12, 'gender': 'male'},
#     {'name': 'Lira', 'fullname': 'Lira_4', 'age': 43, 'gender': 'male'},
# ]
#
# insert_many_users(values_4)
def select_users():
    stmt = (
        select(User)
            .where(User.gender == 'male')
            .filter(User.name.like('L%') | User.name.like('H%'))
            .order_by(User.age.desc())
            .limit(3)
    )
    with engine.connect() as conn:
        return list(conn.execute(stmt))


for row in select_users():
    print(f"{row.name} has fullname: {row.fullname} age = {row.age} gender = {row.gender}")
