"""Flashcard Collection form"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length


class FlashcardCollectionForm(FlaskForm):
    name = StringField("Collection name", validators=[DataRequired()])
    category = StringField("Category", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[Length(min=10, max=256)])
    submit = SubmitField("Create")


class FlashcardCollectionEditForm(FlaskForm):
    name = StringField("Collection name", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[Length(min=10, max=256)])
    submit = SubmitField("Save")


class FlashcardForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    answer = TextAreaField("Answer", validators=[DataRequired()])
    input_type = SelectField(u'Type', choices=[('text', 'Text'), ('markdown', 'Markdown')])
    submit = SubmitField("Create")
