from typing import Union, Annotated
import json
from fastapi import FastAPI, Header
from class_model import Flower
from database.connection import add_flower, fet_flower, delete_flower

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/show")
def show(id: Annotated[int | None, Header()] = None):
    return fet_flower(id=id - 1)


@app.post("/add_flower")
def add_flwoer(flower: Flower):
    add_flower(dict(flower))
    return flower


@app.delete("/delet_flower")
def delete_flow(id: int):
    return delete_flower(id=id)


# TODO
# 1. CRUD // CREATE READ UPDATE DELETE for flowers || create done, read done, delete done,
# 1.1 Make pytest test for CRUD
# 1.2 Auto-Update next/last flower watering
# 1.2 Google calendar reminders
# 2. Login (oauth)
# 3. UserPanel // views
# --python testing with pytest, second edition
