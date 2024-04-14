from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

api = Api(title="vvri API", description="https://vvri.pythonanywhere.com/")
api.prefix = '/api'

db = SQLAlchemy()
