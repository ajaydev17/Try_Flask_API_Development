import os
from flask import Flask
from dotenv import load_dotenv

# load data from .env file
load_dotenv()


def create_app(config_type=os.getenv('CONFIG_TYPE')):
    """
        creates a flask app server
    """

    app = Flask(__name__)
    app.config.from_object(config_type)
    return app
