from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()
FAVICON_PATH = 'favicon.ico'


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(FAVICON_PATH)


@app.get("/")
def root():
    return {"message": "hello"}


@app.get("/items/{item_id}")
def items_detail(item_id: int, q: Union[str, None] = None):
    return {"message": f"this is {item_id}", "q": q}
