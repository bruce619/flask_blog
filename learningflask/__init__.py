# pip install flask-bcrypt (for hashing password)
# pip install flask
# pip install flask-sqlalchemy
# pip install flask-login
# pip install flask-mail
# pip install flask_wtf
# pip install email_validator
# pip install python-dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from learningflask.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from learningflask.users.routes import users
    from learningflask.posts.routes import posts
    from learningflask.main.routes import main
    from learningflask.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

