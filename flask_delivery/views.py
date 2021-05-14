from flask import session, redirect, request, render_template

from flask_delivery import app, User, db, Dish, Category, Order

from forms import RegistrationForm

from wtforms.validators import Required

@app.route("/registration/", methods=["GET", "POST"])
def registration():
    if session.get("user_id"):
        return redirect("/")

    # Создаем форму
    form = RegistrationForm()

    if request.method == "POST":

        # создаем пользователя
        user = User()
        user.username = form.username.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()

        return render_template("registration_success.html", form=form)

    return render_template("registration.html", form=form)




















###################################### Delete below ######################################


# @app.route('/home/')
# def home():
#     if not session.get('is_auth'):
#         return redirect('/login/')
#     return render_template("home.html")
#
#
# @app.route("/login/", methods=["GET", "POST"])
# def login():
#     error_msg = ""  # Пока ошибок нет
#
#     if request.method == "POST":
#
#         username = request.form.get("username")
#         password = request.form.get("password")
#
#         if username == app.config["USERNAME"] and password == app.config["PASSWORD"]:
#             session['is_auth'] = True
#             return render_template("success.html")
#
#         else:
#             error_msg = "Неверный логин или пароль"
#
#     return render_template("login.html", error_msg=error_msg)
#
#
# @app.route('/logout/', methods=["POST"])
# def logout():
#     error_msg = ""
#     if session.get("is_auth"):
#         session.pop("is_auth")
#     if not session.get("is_auth"):
#         error_msg = "Войдите в аккаунт"
#     return render_template("login.html", error_msg=error_msg)