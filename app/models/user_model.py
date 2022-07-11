from sqlalchemy import Column, Float, String, DateTime, Integer, Boolean
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class UserModel(db.Model):
    
    user_id: int
    name: str
    cpf: int
    birthDate: DateTime
    
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    cpf = Column(Integer, nullable=False, unique=True)
    birthDate = Column(DateTime, nullable=False)
    