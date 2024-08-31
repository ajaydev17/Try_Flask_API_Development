import os

from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from apifairy import APIFairy

# load data from .env file
load_dotenv()

database = SQLAlchemy()
db_migrate = Migrate()
marshmallow = Marshmallow()
apifairy = APIFairy()


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
    marshmallow.init_app(app)
    apifairy.init_app(app)

    import core.models  # noqa: F401


def register_blueprint(app):
    from . import inventory_api
    app.register_blueprint(inventory_api.inventory_category_api_blueprint, url_prefix='/api')
    app.register_blueprint(inventory_api.inventory_product_api_blueprint, url_prefix='/api')
