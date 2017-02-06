from models import Pizza, Price, catalog, base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import environ, getenv


engine = create_engine(getenv('DB_URI'))


def create_session(engine):
    session_maker = sessionmaker(bind=engine)
    return session_maker()


if __name__ == '__main__':
    session = create_session(engine)
    for pizza in catalog:
        new_pizza = Pizza()
        new_pizza.title = pizza['title']
        new_pizza.description = pizza['description']
        for choice in pizza['choices']:
            new_choice = Price()
            new_choice.size = choice['title']
            new_choice.price = choice['price']
            new_pizza.choices.append(new_choice)
        session.add(new_pizza)
        session.commit()