from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID

class Position(BaseModel):
    id: UUID
    ticker: str = Field(..., max_length=10)
    quantity: float
    total_purchase_price: float
    purchase_date: datetime

    class Config:
        from_attributes = True  # Allows conversion from SQLAlchemy models
