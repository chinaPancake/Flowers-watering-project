from pydantic import BaseModel
from typing import Optional


class Flower(BaseModel):
    name: str
    description: Optional[str]
    frequency: int
    amount: int
    last_watering: str


class User(BaseModel):
    name: str
    password: str
    email: str
