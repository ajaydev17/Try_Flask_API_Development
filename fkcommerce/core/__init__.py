import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# load data from .env file
load_dotenv()

database = SQLAlchemy()


def create_app(config_type=os.getenv('CONFIG_TYPE')):
    """
        creates a flask app server
    """

    app = Flask(__name__)
    app.config.from_object(config_type)
    initialize_extension(app)
    return app


def initialize_extension(app):
    database.init_app(app)
