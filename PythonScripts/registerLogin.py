from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask import jsonify
import app


class RegistrationForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired(), Length(min=2, max=50)], default='')

    lastname = StringField('Lastname', validators=[DataRequired(), Length(min=2, max=50)], default='')

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)], default='')

    email = StringField('Email',
                        validators=[DataRequired(), Email()], default='')

    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], default='')

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], default='')

    SubmitField = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()], default='')

    password = PasswordField('Password', validators=[DataRequired()], default='')

    SubmitField = SubmitField('Login')


class ResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    SubmitField = SubmitField('Reset')


def get_user(username):
    # Fetch userinfo from username
    user = app.db.retrieve_from_user(username)
    if user is None:
        return []
    print(user)
    return user


def create_user(firstname, lastname, username, email, password):
    # create a new user in the database
    user_info = {
        "_id": username,
        "password": password,
        "first": firstname,
        "last": lastname,
        "email": email,
    }
    # insert user information into the database
    app.db.insert_into_user(user_info)
    return jsonify({'success': True})


def validate_username(self, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('Username already in use.')
