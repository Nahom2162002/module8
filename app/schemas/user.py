from typing import Optional 
from uuid import UUID 
from datetime import datetime 
from pydantic import BaseModel, EmailStr, ConfigDict 

class UserRead(BaseModel):
    id: UUID 
    username: str 
    email: EmailStr 
    password: str 
    created_at: datetime 

    model_config = ConfigDict(from_attributes=True)

class CalculationRead(BaseModel):
    a: int 
    b: int 
    type: str 

    model_config = ConfigDict(from_attributes=True)