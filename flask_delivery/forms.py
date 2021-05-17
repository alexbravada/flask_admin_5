import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()


def password_check(form, field):
    return None


class LoginForm(FlaskForm):
    pass


# Форма регистрации
class RegistrationForm(FlaskForm):

    # Добавляем поле имени пользователя
    mail = StringField("Электронная почта", [Email(message="Это не похоже на почту, попробуйте еще раз!"),
                                             InputRequired(message="Введите что-нибудь")])
    # Добавляем поле пароля
    password = PasswordField("Пароль", [InputRequired(message="Введите что-нибудь"), Length(min=3, message="Слишком короткая строка")])
    # Добавляем поле подтверждения пароля
    confirm_password = PasswordField("повторите пароль")



class ChangePasswordForm(FlaskForm):
    pass