"""Flashcard Collection form"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length


class FlashcardCollectionForm(FlaskForm):
    name = StringField("Collection name", validators=[DataRequired()])
    category = StringField("Category", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[Length(max=256)])
    submit = SubmitField("Create")


class FlashcardCollectionEditForm(FlaskForm):
    name = StringField("Collection name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[Length(max=256)])
    submit = SubmitField("Save")
