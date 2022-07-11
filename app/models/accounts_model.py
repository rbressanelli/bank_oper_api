from sqlalchemy import Column, Float, String, DateTime, Integer, Boolean
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class AccountModel(db.Model):

    id
    account_id: int
    user_id: int
    balance: float
    daily_withdraw_limit: float
    is_active: bool
    account_type: int
    created_at: DateTime

    __tablename__ = "accounts"

    id = Column(String(100), primary_key=True)
    account_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    balance = Column(Float, nullable=True)
    daily_withdraw_limit = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    account_type = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=True)
