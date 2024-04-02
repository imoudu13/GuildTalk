from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask import jsonify
from DatabaseConnections import DatabaseConnect

db = DatabaseConnect()

class UniqueUsername(object):
    # Validate that the username is unique on registering a new account
    def __init__(self, message="Username already exists. Please choose a different one."):
        self.message = message

    def __call__(self, form, field):
        user = db.retrieve_document(field.data, "User")
        if user:
            raise ValidationError(self.message)

class RegistrationForm(FlaskForm):
    # This is to validate the user info is correclty entered on the registration form
    firstname = StringField('Firstname', validators=[DataRequired(), Length(min=2, max=50)], default='')

    lastname = StringField('Lastname', validators=[DataRequired(), Length(min=2, max=50)], default='')

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20), UniqueUsername()], default='')

    email = StringField('Email',
                        validators=[DataRequired(), Email()], default='')

    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)], default='')

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')], default='')

    SubmitField = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    # This is to validate the user info is correclty entered on the login form
    username = StringField('Username',
                           validators=[DataRequired()], default='')

    password = PasswordField('Password', validators=[DataRequired()], default='')

    SubmitField = SubmitField('Login')


class ResetForm(FlaskForm):
    # This is to validate the user info is correclty entered on the form to reset your password
    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    SubmitField = SubmitField('Reset')


def get_user(username):
    # Fetch userinfo from username
    user = db.retrieve_document(username, "User")
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
    db.insert_into_user(user_info)
    return jsonify({'success': True})
