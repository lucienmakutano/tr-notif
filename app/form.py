from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired


class AddTeacherForm(FlaskForm):
    code = StringField(
        "Teacher's code",
        validators=[DataRequired()]
    )
    phone = StringField(
        "Teacher's phone number",
        validators=[DataRequired()]
    )
    submit = SubmitField("Add a teacher")


class NotifyForm(FlaskForm):
    code = StringField(
        "Teacher's code",
        validators=[DataRequired()]
    )
    msg = TextField(
        "Message",
        validators=[DataRequired()]
    )
    submit = SubmitField("Notify")
