import os

# Для указания пути к файлу БД воспользумся путем до текущего модуля
# - Текущая папка
current_path = os.path.dirname(os.path.realpath(__file__))
# - Путь к файлу БД в данной папке
db_path = "sqlite:///" + current_path + "/flsk_deliver.db"


class Config:
    DEBUG = True
    SECRET_KEY = "secret_key"
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = "flask_delivery"
    # SQLALCHEMY_ECHO = True
