from sqlalchemy import BigInteger, Column, Float, ForeignKey, String, DateTime, Integer, Boolean
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref

from app.configs.database import db


@dataclass
class TransactionModel(db.Model):
    
    transaction_id: int
    value: float
    transaction_date: DateTime
    
    __tablename__ = "transactions"
    
    
    transaction_id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    transaction_date = Column(DateTime, nullable=False)
    
    account_id = Column(Integer, ForeignKey('accounts.account_id'), nullable=False)
    
    account = relationship("AccountModel", backref=backref("user", useList=False))
    