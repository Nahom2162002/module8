from datetime import datetime, timedelta 
import uuid 
from typing import Optional, Dict, Any 

from sqlalchemy import Column, String, DateTime, Boolean 
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from jose import JWTError, jwt 
from pydantic import ValidationError

from app.schemas.base import UserCreate 
from app.schemas.user import UserRead 


Base = declarative_base() 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = 'users'

    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    @staticmethod 
    def hash_password(password_hash: str) -> str:
        return pwd_context.hash(password_hash)

    def verify_password(self, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, self.password_hash)

class Calculation(Base):
    id = Column(int(10), unique=True, nullable=False)
    a = Column(int(10), unique=True, nullable=False)
    b = Column(int(10), unique=True, nullable=False)
    type = Column(String(8), nullable=False)
    result = Column(Any(10), nullable=False)