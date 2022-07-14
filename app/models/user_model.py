from dataclasses import dataclass

from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, String

from app.configs.database import db


@dataclass
class UserModel(db.Model):

    user_id: int
    name: str
    cpf: str
    birthDate: DateTime

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    cpf = Column(String(100), nullable=False, unique=True)
    birthDate = Column(DateTime, nullable=False)
