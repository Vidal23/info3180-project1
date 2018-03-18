from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class ProfileForm(FlaskForm):
    firstname = StringField('Username', validators=[InputRequired()])
    lastname = StringField('Password', validators=[InputRequired()])
    gender = SelectField(label='Gender', choices=[("Male", "Male"), ("Female", "Female")])
    email = StringField('Password', validators=[InputRequired()])
    location = StringField('Password', validators=[InputRequired()])
    bio = StringField('Password', validators=[InputRequired()])
    photo= FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg','png','Images Only!'])
    ])