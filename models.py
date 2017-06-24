from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

base = declarative_base()


class Pizza(base):
    __tablename__ = 'pizzas_types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    choices = relationship('PizzaChoice')

    def __repr__(self):
        return '{}'.format(self.title)


class PizzaChoice(base):
    __tablename__ = 'prices'
    id = Column(Integer, ForeignKey('pizzas_types.id'), primary_key=True)
    size = Column(String, primary_key=True)
    price = Column(Integer)
    pizza = relationship('Pizza')

    def __repr__(self):
        return '{} {} {}'.format(self.pizza, self.size, self.price)

