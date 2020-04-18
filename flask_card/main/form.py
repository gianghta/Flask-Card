"""Flashcard Collection form"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class FlashcardCollectionForm(FlaskForm):
    name = StringField('Collection name', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Create')