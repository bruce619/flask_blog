import os
from dotenv import load_dotenv, find_dotenv


# load dotenv in the base root
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
load_dotenv(find_dotenv())


# https://stackoverflow.com/questions/57428277/correct-way-to-use-flask-configuration-from-object


class Config(object):
    """
        Parent Config class containing generic config settings.
    """
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    CSRF_ENABLED = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('EMAIL_USER')
    MAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('DEFAULT_EMAIL_SENDER')


class DevelopmentConfig(Config):
    """
        Config class settings for development
    """
    FLASK_ENV = 'development'
    DEBUG = True
    DEVELOPMENT = True
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_DEV')


class TestingConfig(Config):
    """
        Config class settings for Testing
    """
    FLASK_ENV = 'testing'
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_TEST')


class ProductionConfig(Config):
    """
        Config class settings for Production
    """
    FLASK_ENV = 'production'
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI_PROD')


config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
