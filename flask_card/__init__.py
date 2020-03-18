from flask import Flask

from flask_card.config import Configs
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object(Configs)

db = SQLAlchemy(app)
Migrate(app, db)

# Login configuration
login_manager = LoginManager()
login_manager.init_app(app)