from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.accounts_model import AccountModel
    from app.models.user_model import UserModel
    from app.models.transaction_model import TransactionModel
