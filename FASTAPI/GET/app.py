from fastapi import FastAPI

main = FastAPI()


@main.get("/din")
def read_root():
    return {"Hello": "World"}


@main.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}