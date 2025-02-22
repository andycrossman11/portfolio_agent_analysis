import uuid
import uvicorn
from fastapi import FastAPI, HTTPException
from src.portfolio_management.database import DB_OPS, Position
from pydantic import BaseModel
from datetime import datetime

class StockPurchase(BaseModel):
    ticker: str
    quantity: float
    total_purchase_price: float
    purchase_date: datetime

app = FastAPI()


@app.put('/positions/{id}', response_model=dict)
async def update_position(id: uuid.UUID, body: StockPurchase):
    success = DB_OPS.update_position(id, **body.model_dump())
    if not success:
        raise HTTPException(status_code=404, detail="Position not found")
    return {"message": "Position updated successfully"}

@app.delete('/positions/{id}', response_model=dict)
async def udelete_position(id: uuid.UUID):
    success = DB_OPS.delete_position(id)
    if not success:
        raise HTTPException(status_code=404, detail="Position not found")
    return {"message": "Position deleted successfully"}

@app.get('/positions', response_model=list[Position])
async def get_positions():
    positions = DB_OPS.get_all_positions()
    return positions

@app.post('/positions', response_model=Position)
async def create_position(body: StockPurchase):
    position = DB_OPS.create_position(**body.model_dump())
    return position

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

