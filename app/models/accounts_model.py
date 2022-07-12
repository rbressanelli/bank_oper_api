from dataclasses import dataclass

from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import backref, relationship

from app.configs.database import db


@dataclass
class AccountModel(db.Model):

    account_id: int
    user_id: int
    balance: float
    daily_withdraw_limit: float
    is_active: bool
    account_type: int
    created_at: DateTime

    __tablename__ = "accounts"

    account_id = Column(Integer, primary_key=True)
    balance = Column(Float, nullable=True)
    daily_withdraw_limit = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    account_type = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=True)

    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False, unique=True)

    user = relationship("UserModel", backref=backref("account", uselist=False))

    transactions = relationship("TransactionModel", backref="account", uselist=True)
