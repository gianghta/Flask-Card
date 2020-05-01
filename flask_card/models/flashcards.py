from .. import db


class Flashcard(db.Model):
    __tablename__ = "flashcard"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    collection_id = db.Column(db.Integer, db.ForeignKey("collection.id"))

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return f"<Flashcard: {self.id}"
