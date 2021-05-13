from flask import Flask

from flask_admin_5w.config import Config

from flask_admin_5w.models import db, User


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  # Настраиваем соединение

from flask_admin_5w.views import *


SESSION_TYPE = 'memcache'

app.config["USERNAME"] = "test"
app.config["PASSWORD"] = "test"


if __name__ == "__main__":
    app.run(debug=True)
