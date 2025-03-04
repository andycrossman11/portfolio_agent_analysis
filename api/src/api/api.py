import uuid
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
from shared.database import DB_OPS, Position, Analysis
from datetime import datetime
import os
from pydantic import BaseModel, field_validator
from apscheduler.schedulers.background import BackgroundScheduler
import time
from publish import publish_message
from metrics import track_request, get_request_metrics
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from starlette.requests import Request
from starlette.responses import JSONResponse

class StockPurchase(BaseModel):
    ticker: str
    quantity: float
    purchase_share_price: float
    purchase_date: str

    @field_validator("purchase_date", mode="before")
    def validate_date_format(cls, value):
        if isinstance(value, datetime):
            return value.strftime("%m-%d-%Y")
        try:
            return datetime.strptime(value, "%m-%d-%Y").strftime("%m-%d-%Y")
        except ValueError:
            raise ValueError("Date must be in MM-DD-YYYY format")


app = FastAPI()
scheduler = BackgroundScheduler()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET", "PUT", "POST", "DELETE"],
    allow_headers=["*"],
)

@app.middleware("http")
async def prometheus_middleware(request: Request, call_next):
    # Call the next middleware or endpoint
    response = await call_next(request)
    
    # Track the request AFTER the endpoint executes
    track_request(request.method, request.url.path)
    
    return response

@app.on_event("startup")
def start_scheduler():
    scheduler.add_job(publish_message, "interval", hours=24)
    scheduler.start()
    print("Portfolio Analysis Scheduler started")

@app.on_event("shutdown")
def shutdown_scheduler():
    scheduler.shutdown()
    print("Portfolio Analysis Scheduler stopped")

@app.get("/health")
def get_health():
    return {"status": "app running"}

@app.get("/performance/endpoint_metrics")
async def get_metrics():
    metrics = get_request_metrics()
    return JSONResponse(content=metrics)

@app.put('/positions/{id}', response_model=dict)
async def update_position(id: uuid.UUID, body: StockPurchase):
    success = DB_OPS.update_position(id, **body.model_dump())
    if not success:
        raise HTTPException(status_code=404, detail="Position not found")
    return {"message": "Position updated successfully"}

@app.delete('/positions/{id}', response_model=dict)
async def delete_position(id: uuid.UUID):
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

@app.get('/analysis', response_model=list[Analysis])
async def get_analysis():
    analysis = DB_OPS.get_all_daily_analysis()
    return analysis

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

