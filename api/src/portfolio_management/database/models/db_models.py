from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class PositionSchema(Base):
    __tablename__ = "position"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    ticker = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    total_purchase_price = Column(Float, nullable=False)
    purchase_date = Column(DateTime, server_default="NOW()", nullable=False)
