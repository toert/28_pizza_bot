from models import Pizza, PizzaChoice, base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv


engine = create_engine(getenv('DB_URI'))


def create_session(engine):
    session_maker = sessionmaker(bind=engine)
    return session_maker()


catalog = [
    {
        'title': 'Маргарита',
        'description': 'соус,сыр Моцарелла',
        'choices': [
            {
                'title': '30 см (450гр)',
                'price': 360,
            },
            {
                'title': '40 см (750гр)',
                'price': 460,
            }
        ],
    },
    {
        'title': 'Маргарита <Помидоро>',
        'description': 'соус,сыр Моцарелла,помидоры',
        'choices': [
            {
                'title': '30см (500гр)',
                'price': 400,
            },
            {
                'title': '40cм (850гр)',
                'price': 490,
            }
        ],
    },
    {
        'title': 'Грибная',
        'description': 'соус,сыр Моцарелла,шампиньоны',
        'choices': [
            {
                'title': '30см (500гр)',
                'price': 430,
            },
            {
                'title': '40см (870гр)',
                'price': 540,
            }
        ],
    },
    {
        'title': 'С ветчиной',
        'description': 'соус,сыр Моцарелла,ветчина',
        'choices': [
            {
                'title': '30см (500гр)',
                'price': 430,
            },
            {
                'title': '40см (870гр)',
                'price': 540,
            }
        ],
    },
    {
        'title': 'Ветчина с грибами',
        'description': 'соус,сыр Моцарелла,шампиньоны,ветчина',
        'choices': [
            {
                'title': '30см (580гр)',
                'price': 460,
            },
            {
                'title': '40см (930гр)',
                'price': 570,
            }
        ],
    },
    {
        'title': 'Салями',
        'description': 'соус,сыр Моцарелла,салями',
        'choices': [
            {
                'title': '30см (500гр)',
                'price': 450,
            },
            {
                'title': '40см (870гр)',
                'price': 560,
            }
        ],
    },
    {
        'title': 'Гавайская',
        'description': 'соус,сыр Моцарелла,ветчина,ананасы',
        'choices': [
            {
                'title': '30см (580гр)',
                'price': 470,
            },
            {
                'title': '40см (870гр)',
                'price': 580,
            }
        ],
    },
    {
        'title': 'Четыре сыра',
        'description': 'соус,сыр Моцарелла,сыр Гауда,сыр Эдам,сыр Дор-Блю',
        'choices': [
            {
                'title': '30см (600гр)',
                'price': 470,
            },
            {
                'title': '40см (870гр)',
                'price': 580,
            }
        ],
    },
    {
        'title': 'Пеперонни',
        'description': 'соус,сыр Моцарелла,пепперони,перец сладкий',
        'choices': [
            {
                'title': '30см (550гр)',
                'price': 470,
            },
            {
                'title': '40см (920гр)',
                'price': 600,
            }
        ],
    },
    {
        'title': 'С курицей',
        'description': 'соус,сыр Моцарелла,куриные грудки,помидоры,шампиньоны перец',
        'choices': [
            {
                'title': '30см (550гр)',
                'price': 500,
            },
            {
                'title': '40см (920гр)',
                'price': 610,
            }
        ],
    },
    {
        'title': 'Овощная',
        'description': 'соус,сырМоцарелла,перец,лук,шампиньоны,кукуруза,маслины',
        'choices': [
            {
                'title': '30см (600гр)',
                'price': 470,
            },
            {
                'title': '40см (920гр)',
                'price': 580,
            }
        ],
    },
    {
        'title': 'Четыре сезона',
        'description': 'соус,сыр Моцарелла,1/4 салями,1/4 мясная,1/4 ветчина грибы,1/4 четыре',
        'choices': [
            {
                'title': '30см (600гр)',
                'price': 500,
            },
            {
                'title': '40см (930гр)',
                'price': 620,
            }
        ],
    },
    {
        'title': 'Кальцоне',
        'description': 'соус, сыр Моцарелла, ветчина, грибы, чесночное масло, кунжут',
        'choices': [
            {
                'title': '30см (520гр)',
                'price': 440,
            },
            {
                'title': '40см (870гр)',
                'price': 530,
            }
        ],
    },
    {
        'title': 'С тунцом',
        'description': 'соус, сыр Моцарелла, тунец консервированный, помидоры, лук репчатый, маслины',
        'choices': [
            {
                'title': '30см (570гр)',
                'price': 470,
            },
            {
                'title': '40см (950гр)',
                'price': 570,
            }
        ],
    },
    {
        'title': 'С беконом',
        'description': 'соус,сыр,Моцарелла,бекон,помидоры,маслины',
        'choices': [
            {
                'title': '30см (570гр)',
                'price': 470,
            },
            {
                'title': '40см (950гр)',
                'price': 590,
            }
        ],
    },
]

if __name__ == '__main__':
    session = create_session(engine)
    for pizza in catalog:
        new_pizza = Pizza()
        new_pizza.title = pizza['title']
        new_pizza.description = pizza['description']
        for choice in pizza['choices']:
            new_choice = PizzaChoice()
            new_choice.size = choice['title']
            new_choice.price = choice['price']
            new_pizza.choices.append(new_choice)
        session.add(new_pizza)
    session.commit()