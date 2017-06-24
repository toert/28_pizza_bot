from os import getenv
from werkzeug.exceptions import HTTPException
from flask import Flask, Response, request
from sqlalchemy import create_engine
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import Pizza, PizzaChoice
from fill_db import create_session

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
admin = Admin(app, name='PizzaAdmin', template_mode='bootstrap3')
engine = create_engine(getenv('DB_URI'))
session = create_session(engine)


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            'Need authentication to get access to the page', 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


class AuthView(ModelView):
    def check_auth(self, username, password):
        return username == getenv('login') and password == getenv('password')

    def is_accessible(self):
        auth = request.authorization
        if not auth or not self.check_auth(auth.username, auth.password):
            raise AuthException('Not authenticated')
        return True


class PizzaView(AuthView):
    column_display_pk = True
    column_hide_backrefs = False
    form_columns = ('title', 'description')


class ChoiceView(AuthView):
    column_display_pk = True
    column_hide_backrefs = False
    column_exclude_list = ['choices', 'id']
    form_columns = ('pizza', 'size', 'price')


if __name__ == '__main__':
    admin.add_view(PizzaView(Pizza, session))
    admin.add_view(ChoiceView(PizzaChoice, session))
    app.run()
