from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from enum import Enum
#from .database import Base

class ModelName(str, Enum):
	alexnet = "alexnet"
	resnet = "resnet"
	lenet = "lenet"

app = FastAPI()



@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
	if model_name == ModelName.alexnet:
		return {"model_name": model_name, "message": "Deep Learning FTW!"}

	if model_name.value == "lenet":
		return {"model_name": model_name, "message": "LeCNN all the images"}

	return {"model_name": model_name, "message": "Have some residuals"}

"""
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
"""
"""
@app.get("/")
def read_root():
	return {"Hello": "World"}

"""

"""
@app.post("/items/")
async def create_item(item: Item):
    return item
"""

"""
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
"""