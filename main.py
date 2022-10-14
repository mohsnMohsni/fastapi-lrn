from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


app = FastAPI()
FAVICON_PATH = 'favicon.ico'


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(FAVICON_PATH)


@app.get('/')
def root():
    return {'message': 'hello'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'message': f'this is {item_id}', 'q': q}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item name': item.name, 'item id': item_id}
