from fastapi import FastAPI

"""
Can run from terminal using:
fastapi run ./api_/async_api.py
"""


app = FastAPI()


@app.get("/")
async def read_root():
    return "Hello, world!"


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}