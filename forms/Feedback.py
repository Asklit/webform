from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, SubmitField
from wtforms.validators import DataRequired


class FeedbackForm(FlaskForm):
    name = StringField('', validators=[DataRequired()])
    feedback = StringField('', validators=[DataRequired()])
    email = EmailField('', validators=[DataRequired()])
    submit = SubmitField('')
    russian = SubmitField('')
    spanish = SubmitField('')
    english = SubmitField('')
    chinese = SubmitField('')