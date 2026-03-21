from fastapi import FastAPI

app = FastAPI()


items = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Smartphone", "price": 499.99}
}

@app.get("/")
async def read_root():
    return {"message": "FastAPI DELETE example is running! Go to /docs to test it."}

@app.get("/items/")
async def read_items():
    return items

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in items:
        deleted_item = items.pop(item_id)
        return {"message": "Item deleted successfully", "deleted_item": deleted_item}
    return {"error": "Item not found"}
