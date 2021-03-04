from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    """ create_app() 
    creates a new flask app with all the plugins.
    """
    app = Flask(__name__, template_folder="templates")

    app.config.from_object("config.settings")

    return app

