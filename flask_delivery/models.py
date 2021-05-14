from datetime import datetime  # Под вопросом... !!!

from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

# Настройки соединения сделаем позже в модуле приложения
db = SQLAlchemy()


# Описываем модель пользователя
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    orders = db.Column(db.String(512))  # добавить отношение один к многим


class Dish(db.Model):
    __tablename__ = 'dishes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text(512))
    picture = db.Column(db.String(512))
    category = db.Column(db.String(32)) # отношение с категориями


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False, unique=True)
    meals = db.Column(db.Integer)  # отношение с Dish.category


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total = db.Column(db.Integer, nullable=False, default=0)
    status = db.Column(db.String(32))
    mail = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(512), nullable=False)
    order_list = db.Column(db.Text(512)) # (можно через запятую, можно many2many)

