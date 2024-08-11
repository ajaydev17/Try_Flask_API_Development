import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    FLASK_ENV = os.getenv('FLASK_ENV')
    DEBUG = os.getenv('DEBUG')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
