from pydantic import BaseModel, EmailStr, Field, ConfigDict, ValidationError, model_validator
from typing import Optional 
from uuid import UUID 
from datetime import datetime 

class UserBase(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: EmailStr = Field()
    username: str = Field(min_length=3, max_length=50)

    model_config = ConfigDict(from_attributes=True)

class PasswordMixin(BaseModel):
    password: str = Field(min_length=6, max_length=128)

    @model_validator(mode="before")
    @classmethod 
    def validate_password(cls, values: dict) -> dict:
        password = values.get("password")
        if not password:
            raise ValidationError("Password is required", model=cls)
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")
        if not any(char.isupper() for char in password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")
        return values 

class UserCreate(UserBase, PasswordMixin):
    username: str = UserBase.username 
    password: str = PasswordMixin.password 

class CalculationBase(BaseModel):
    a: int = Field(max_length=10)
    b: int = Field(max_length=10)
    type: str = Field(max_length=8)

class CalculationCreate(CalculationBase):
    a: int = CalculationBase.a 
    b: int = CalculationBase.b 
    type: str = CalculationBase.type 
