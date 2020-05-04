""" Application initialize """
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def page_not_found(e):
    return render_template("404page.html"), 404


def create_app():
    """ Core app construction """
    app = Flask(__name__, instance_relative_config=False)

    # Register error page
    app.register_error_handler(404, page_not_found)

    # App configs
    app.config.from_object("config.Configs")

    # Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():
        from . import auth
        from . import main

        app.register_blueprint(auth.auth)
        app.register_blueprint(main.main)

        return app
