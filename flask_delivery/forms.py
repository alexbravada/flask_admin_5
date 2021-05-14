import re

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


def password_check(form, field):
    return None


class LoginForm(FlaskForm):
    pass


# Форма регистрации
class RegistrationForm(FlaskForm):

    # Добавляем поле имени пользователя
    username = StringField("Имя")

    # Добавляем поле пароля
    password = PasswordField("Пароль")



class ChangePasswordForm(FlaskForm):
    pass