from .. import db


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    collections = db.relationship("Collection", backref="category", lazy="dynamic")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Category: {self.name}>"
