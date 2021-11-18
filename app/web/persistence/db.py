'''
Creates db object containing db config + model (entities)

  Testing:
    0. eval "$(pdm --pep582)" && python
    1. from flask import Flask
       app = Flask(__name__)
    2. import entities
    3. db.create_all()

    import importlib
    importlib.reload(entities)
'''
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
