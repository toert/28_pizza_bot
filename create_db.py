from os import getenv
from sqlalchemy import create_engine
from models import base


engine = create_engine(getenv('DB_URI'))
base.metadata.create_all(engine)
