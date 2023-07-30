from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    
@app.get("/")
async def root():
    return {"message": "Hello i'm gaurav's AI"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items")
async def read_item(payload:Item):
    return {"payload": payload}