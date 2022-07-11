from sqlalchemy import Column, Float, ForeignKey, String, DateTime, Integer, Boolean
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref

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
    
    
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    
    users = relationship("UserModel", backref=backref("user", useList=False))
    
    transactions = relationship("TransactionModel", backref=backref("accounts", useList=True))
    