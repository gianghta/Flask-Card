from .. import db


class Flashcard(db.Model):
    __tablename__ = "flashcard"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    right_answered = db.Column(db.Boolean, default=False)
    wrong_answered = db.Column(db.Boolean, default=False)
    collection_id = db.Column(db.Integer, db.ForeignKey("collection.id"))

    def __repr__(self):
        return f"<Flashcard: {self.id}"
