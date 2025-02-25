from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from uuid import UUID

class Position(BaseModel):
    id: UUID
    ticker: str = Field(..., max_length=10)
    quantity: float
    total_purchase_price: float
    purchase_date: str

    class Config:
        from_attributes = True  # Allows conversion from SQLAlchemy models

    @field_validator("purchase_date", mode="before")
    def validate_date_format(cls, value):
        if isinstance(value, datetime):
            return value.strftime("%m-%d-%Y")
        try:
            return datetime.strptime(value, "%m-%d-%Y").strftime("%m-%d-%Y")
        except ValueError:
            raise ValueError("Date must be in MM-DD-YYYY format")
