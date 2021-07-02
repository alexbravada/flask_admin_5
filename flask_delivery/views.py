from flask import session, redirect, request, render_template
from .app import app
from .models import User, db, Dish, Category, Order, func

from .forms import RegistrationForm, AuthForm

from wtforms.validators import Required


@app.route('/')
def main():
    #cat = Category.query.get(1)
    sushi = db.session.query(Dish).filter_by(category_id=1).order_by(func.random()).limit(3).all()
    print(sushi)
    sushi_list = []
    for i in sushi:
        sushi_list.append(i.title)
        print(i.title)
    print(sushi_list)
    # for i in cat.meals:
    #     print(i.title)
    #print(cat.meals.func.random().all())
    #db.session.query(category).order_by(func.random()).limit(sample_num).all()
    return render_template("main.html", sushi=sushi)


# Добавление продуктов в корзину
@app.route('/addtocart/', methods=["GET", "POST"])
def add_to_cart():
    # Получаем либо значение из сессии, либо пустой список
    title = request.form.get('dish_title')
    cart = session.get("cart", [])
    cart.append(db.session.query(Dish).filter_by(title=title))
    session['cart'] = cart

    return session['cart']


@app.route('/cart/')
def cart():
    return render_template("cart.html")


@app.route('/account/')
def account():
    if session.get("is_auth"):
        return render_template("account.html")

    return redirect('/auth/')


@app.route('/auth/', methods=['GET', 'POST'])
def auth():
    msg_email = "mesaga test email"
    msg = "test msg"
    form = AuthForm()
    if session.get("is_auth"):
        return redirect("/account/")
    if request.method == "POST" and User.query.filter(User.mail == form.mail.data, User.password == form.password.data).first():
        session["is_auth"] = True
        print(session.get("is_auth"))
        return redirect('/account/')

    return render_template("auth.html", form=form, msg_email=msg_email, msg=msg)


@app.route("/register/", methods=["GET", "POST"])
def register():
    msg = ""
    msg_email = ""
    # if session.get("user_id"):
    #     return redirect("/")
    form = RegistrationForm()
    if request.method == "POST" and form.password.data == form.confirm_password.data:
        if form.validate_on_submit() and not User.query.filter(User.mail == form.mail.data).first():
            user = User(mail=form.mail.data, password=form.password.data)
            print(user.mail)
            print(user.password)
            db.session.add(user)
            db.session.commit()
            return render_template("reg_done.html", form=form, mail=user.mail, password=user.password)

        form.mail.errors.append("Такой пользователь уже существует")
        msg_email = "This email already registred"
        return render_template("register.html", form=form, msg_email=msg_email)
    else:
        msg = "Password doesn't match, try again "
        return render_template("register.html", form=form, msg=msg)
        # if form.validate_on_submit():
        #     user = User(mail=form.mail.data, password=form.password.data)
        #     db.session.add(user)
        #     db.session.commit()
        #     print(form.mail.data)
        #     return render_template("reg_done.html", form=form, mail=user.mail, password=user.password)
        # else:
        #     #msg = ('Invalid username or password')
        #     return render_template("register.html", form=form)

    return render_template("register.html", form=form)




@app.route('/logout/', methods=["GET", "POST"])
def logout():
    error_msg = ""
    if request.method == "GET" and session.get("is_auth"):
        session["is_auth"] = False
        return redirect('/')
    if not session.get("is_auth"):
        error_msg = "Войдите в аккаунт"
        print(error_msg)
        return redirect('/auth/')

    #return render_template("logout.html", error_msg=error_msg)


@app.route('/ordered/', methods=["POST"])
def ordered():
    error_msg = ""

    return render_template("ordered.html", error_msg=error_msg)














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