from datetime import datetime
from .. import db


class Collection(db.Model):
    __tablename__ = 'collection'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    flashcards = db.relationship('Flashcard', backref='collection', lazy='dynamic')

    def __repr__(self):
        return f'<Flashcard Collection: {self.name}>'