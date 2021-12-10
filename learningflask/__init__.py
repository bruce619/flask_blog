# pip install flask-bcrypt (for hashing password)
# pip install flask
# pip install flask-sqlalchemy
# pip install flask-login
# pip install flask-mail
# pip install flask_wtf
# pip install email_validator
# pip install flask-marshmallow
# instead of using set FLASK_APP = run.py, try $env:FLASK_APP = "run.py"
# flask db init
# flask db migrate -m "Initial Migration"
# flask db upgrade

from flask import Flask
from sqlite3 import Connection as SQLite3Connection
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from learningflask.config import config
from flask_migrate import Migrate


# configure sqlite3 to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name or 'default'))
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    from learningflask.routes.v1.user import users
    from learningflask.routes.v1.post import posts
    from learningflask.routes.v1.main import main
    from errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

