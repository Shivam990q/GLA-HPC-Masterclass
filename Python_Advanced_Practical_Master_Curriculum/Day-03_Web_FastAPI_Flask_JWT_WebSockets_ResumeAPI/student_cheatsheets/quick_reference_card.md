# Day 3 Cheatsheet: FastAPI & REST Quick Reference

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
async def create_item(item: Item):
    return {"message": "Created", "item": item}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id > 100:
        raise HTTPException(status_code=404, detail="Not Found")
    return {"id": item_id}

# Run: uvicorn main:app --reload
```
