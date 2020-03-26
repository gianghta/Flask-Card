""" Application initialize """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """ Core app construction """
    app = Flask(__name__, instance_relative_config=False)

    # App configs
    app.config.from_object('config.Config')

    # Plugins
    Migrate(db, app)
    login_manager.init_app(app)

    with app.app_context():
        from . import auth
        from . import routes

        # Create Database Models
        db.create_all()

        return app