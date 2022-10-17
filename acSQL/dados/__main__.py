from datetime import date

from .person import Person
from ..ambiente.base import session_factory


def create_people():
    session = session_factory()
    gustavo = Person("Gustavo Lopes", date(2003, 4, 11), 183, 70)
    beatriz = Person("John Doe", date(2008, 9, 26), 152, 30)
    session.add(gustavo)
    session.add(beatriz)
    session.commit()
    session.close()


def get_people():
    session = session_factory()
    people_query = session.query(Person)
    session.close()
    return people_query.all()


if __name__ == "__main__":
    people = get_people()
    if len(people) == 0:
        create_people()
    people = get_people()

    for person in people:
        print(f'{person.name} was born in {person.date_of_birth}')