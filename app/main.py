from flask import Flask
from .extensions import api, db
from .resources import ns
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
    # app.config['secretkey'] = "Vasvari12"

    api.init_app(app)
    db.init_app(app)

    api.add_namespace(ns)

    with app.app_context():
        db.create_all()
    return app


app = create_app()

if __name__ == "__main__":
    # Indítsd el a Flask szerveret
    app.run()
