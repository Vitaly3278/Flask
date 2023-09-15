from datetime import datetime
from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(min_length=3)


class UserRead(BaseModel):
    id: int
    name: str = Field(max_length=32)
    surname: str = Field(max_length=32)
    email: str = Field(max_length=128)
    password: str = Field(min_length=3)


class ProductCreate(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=300)
    price: int = Field(default=0)


class ProductRead(BaseModel):
    id: int
    title: str = Field(max_length=50)
    description: str = Field(max_length=300)
    price: int = Field(default=0)


class OrderCreate(BaseModel):
    user_id: int
    prod_id: int
    date: datetime = Field(default=datetime.now())
    status: str = Field(default="created")


class OrderRead(BaseModel):
    id: int
    user_id: int
    prod_id: int
    date: str
    status: str = Field(default="created")