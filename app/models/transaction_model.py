from dataclasses import dataclass

from sqlalchemy import (BigInteger, Boolean, Column, DateTime, Float,
                        ForeignKey, Integer, String)
from sqlalchemy.orm import backref, relationship

from app.configs.database import db


@dataclass
class TransactionModel(db.Model):

    transaction_id: int
    account_id: int
    value: float
    transaction_date: DateTime

    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True)
    value = Column(Float, nullable=False)
    transaction_date = Column(DateTime, nullable=False)

    account_id = Column(Integer, ForeignKey("accounts.account_id"), nullable=False)
