from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
async def read_root():
    return {"message": "FastAPI POST example is running! Go to /docs to test it."}

@app.post("/items/")
async def create_item(item: Item):
    return {"message": "Item created successfully", "item": item}
