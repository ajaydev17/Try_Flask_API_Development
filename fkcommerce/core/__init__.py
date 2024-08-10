from flask import Flask


def create_app():
    """
        creates a flask app server
    """

    app = Flask(__name__)
    return app
    