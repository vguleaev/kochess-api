from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = [
    Item(text="item1", is_done=True),
    Item(text="item2", is_done=False),
    Item(text="item3", is_done=True),
]

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/items")
def create_item(item: Item) -> Item:
    items.append(item)
    return item

@app.get("/items", response_model=list[Item])
def get_items(limit: int = 10):
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    
    return items[item_id]