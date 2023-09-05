from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_pas = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
