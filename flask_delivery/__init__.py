from flask import Flask

from flask_delivery.config import Config

from flask_delivery.models import db, User, Dish, Category, Order


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  # Настраиваем соединение

from flask_delivery.views import *


SESSION_TYPE = 'memcache'

app.config["USERNAME"] = "test"
app.config["PASSWORD"] = "test"


if __name__ == "__main__":
    app.run(debug=True)
