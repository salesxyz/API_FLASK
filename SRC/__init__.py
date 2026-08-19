from flask import Flask
from connection import db, config
from flask_marshmallow import Marshmallow
from flask_restful import Api

ma = Marshmallow()
api = Api()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    @app.get('/')
    def home():
        return {"mensagem": "API Flask Funcionando"}, 200

    return app
