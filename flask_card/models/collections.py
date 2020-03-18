from datetime import datetime
from flask_card import db


class Collection(db.Model):
    __tablename__ = 'cardcollection'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    flashcards = db.relationship('Flashcard', backref='collection', lazy='dynamic')

    def __repr__(self):
        return f'<Flashcard Collection: {self.name}>'