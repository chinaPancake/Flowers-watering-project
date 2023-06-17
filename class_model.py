from pydantic import BaseModel


class Flower(BaseModel):
    name: str
    description: str
    frequency: int
    amount: int
    last_watering: str


class User(BaseModel):
    name: str
    password: str
    email: str
