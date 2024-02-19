from fastapi import FastAPI
from pydantic import BaseModel
from src.Controllers.Capstone_Controller import router as capstone_router

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/", tags=["Items"])
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}

@app.get("/getAll", tags=["Iiot"])
async def read_root():
    return {"Hello": "World"}

# Include the Capstone router
app.include_router(capstone_router, prefix="/capstone")