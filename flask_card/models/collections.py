from datetime import datetime
from .. import db


class Collection(db.Model):
    __tablename__ = "collection"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String, index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    right_answer = db.Column(db.Integer, default=0)
    wrong_answer = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    flashcards = db.relationship(
        "Flashcard", cascade="all,delete", backref="collection", lazy="dynamic"
    )

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Flashcard Collection: {self.name}>"
