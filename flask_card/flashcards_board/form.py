from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length


class FlashcardForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    answer = TextAreaField("Answer", validators=[DataRequired()])
    input_type = SelectField(u'Type', choices=[('text', 'Text'), ('markdown', 'Markdown')])
    submit = SubmitField("Create")

class FlashcardEditForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    answer = TextAreaField("Answer", validators=[DataRequired()])
    input_type = SelectField(u'Type', choices=[('text', 'Text'), ('markdown', 'Markdown')])
    submit = SubmitField("Change")