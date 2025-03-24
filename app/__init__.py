from flask import Flask
from .api import api_init

def create_app(config_name='development'):
    app = Flask(__name__)
    app.register_blueprint(api_init)

    return app