from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


items = {
    1: {"name": "Laptop", "price": 999.99, "is_offer": False}
}

@app.get("/")
async def read_root():
    return {"message": "FastAPI PUT example is running! Go to /docs to test it."}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return items.get(item_id, {"error": "Item not found"})

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    items[item_id] = item.dict()
    return {"message": "Item updated successfully", "item_id": item_id, "updated_item": item}
