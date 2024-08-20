import os

from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# load data from .env file
load_dotenv()

database = SQLAlchemy()
db_migrate = Migrate()


def create_app(config_type=os.getenv('CONFIG_TYPE')):
    """
        creates a flask app server
    """

    app = Flask(__name__)
    app.config.from_object(config_type)
    initialize_extension(app)
    register_blueprint(app)
    return app


def initialize_extension(app):
    database.init_app(app)
    db_migrate.init_app(app, database)

    import core.models  # noqa: F401


def register_blueprint(app):
    import core.inventory_api
    app.register_blueprint(core.inventory_api.inventory_category_api_blueprint, url_prefix='/api')
