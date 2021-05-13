from flask import Flask

from config import Config

from models import db, User


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  # Настраиваем соединение

from views import *


SESSION_TYPE = 'memcache'

app.config["USERNAME"] = "test"
app.config["PASSWORD"] = "test"


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
    app.run(debug=True)
