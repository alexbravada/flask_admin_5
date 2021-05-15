from flask import Flask

from flask_migrate import Migrate

from .config import Config

from .models import db
from .forms import csrf

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)  # Настраиваем соединение
csrf.init_app(app)
from .views import *


migrate = Migrate(app, db)


SESSION_TYPE = 'memcache'

app.config["USERNAME"] = "test"
app.config["PASSWORD"] = "test"


if __name__ == "__main__":
    app.run(debug=True)