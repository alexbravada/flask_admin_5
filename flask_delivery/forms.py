import re
from flask_delivery import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect(app)

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
    # Добавляем поле подтверждения пароля
    confirm_password = PasswordField("повторите пароль")



class ChangePasswordForm(FlaskForm):
    pass