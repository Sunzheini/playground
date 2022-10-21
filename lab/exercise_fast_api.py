from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

appz = FastAPI()


# example get
# -----------------------------------------------------------------------
# @appz.get("/")
# def home():
#     return {"Data": "Testing"}
#
#
# # run in terminal
# # D:\Study\Projects\PycharmProjects\playground\lab>uvicorn exercise_fast_api:appz --reload
#
#
# @appz.get("/about")
# def about():
#     return {"Data": "About"}

# -----------------------------------------------------------------------
# example get with variable

# inventory = {
#     1: {
#         "name": "Milk",
#         "price": 3.99,
#         "brand": "Regular"
#     }
# }
#
# @appz.get("/get-item/{item_id}/{name}")
# def get_item(item_id: int, name: str):
#     return inventory[item_id]

# -----------------------------------------------------------------------
# /w query params


inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular",
    }
}
# http://localhost:8000/get-item/1
@appz.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The id...")):
    return inventory[item_id]


# http://localhost:8000/get-by-name?name=Milk
@appz.get("/get-by-name")
def get_item(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not Found!"}

# -----------------------------------------------------------------------
# /w post


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


@appz.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}

    inventory[item_id] = {
        "name": item.name,
        "price": item.price,
        "brand": item.brand,
    }
    return inventory[item_id]




