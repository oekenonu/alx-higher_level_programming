#!/usr/bin/python3
"""Print state object with name passed arg"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for data in session.query(State).order_by(State.id):
        print(data.id, data.name, sep=": ")
        for city_data in data.cities:
            print(f"{city_data.id:>5}: {city_data.name}")
