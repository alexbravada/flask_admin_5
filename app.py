from flask import Flask, session, redirect, request, render_template

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SESSION_TYPE = 'memcache'


app.config["USERNAME"] = "test"
app.config["PASSWORD"] = "test"


@app.route('/home/')
def home():
    if not session.get('is_auth'):
        return redirect('/login/')
    return render_template("home.html")





@app.route("/login/", methods=["GET", "POST"])
def login():
    error_msg = ""  # Пока ошибок нет

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == app.config["USERNAME"] and password == app.config["PASSWORD"]:
            session['is_auth'] = True
            return render_template("success.html")

        else:
            error_msg = "Неверный логин или пароль"

    return render_template("login.html", error_msg=error_msg)


@app.route('/logout/', methods=["POST"])
def logout():
    if session.get("is_auth"):
        session.pop("is_auth")
    return redirect("/login/")

# @app.route('/add/<item>/')
# def add_to_cart(item):
#
#     # Получаем либо значение из сессии, либо пустой список
#     cart = session.get("cart", [])
#     # Добавлям элемент в список
#     cart.append(item)
#     # Записываем список обратно в сессию
#     session['cart'] = cart
#
#     return "Item {} added".format(item)

if __name__ == "__main__":
    app.secret_key = 'super secret key'



app.run(debug=True)
