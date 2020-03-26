from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_card import db, login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    member_since = db.Column(db.DateTime, default=datetime.utcnow)
    collections = db.relationship('CardCollection', backref='user', lazy='dynamic')

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Username: {self.username}>'