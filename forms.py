import re

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


def password_check(form, field):
    return None


class LoginForm(FlaskForm):
    pass


class RegistrationForm(FlaskForm):
    pass


class ChangePasswordForm(FlaskForm):
    pass