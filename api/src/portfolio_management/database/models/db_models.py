from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class PositionSchema(Base):
    __tablename__ = "position"
    
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    ticker = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    purchase_share_price = Column(Float, nullable=False)
    purchase_date = Column(DateTime, default=lambda: datetime.now().strftime('%m-%d-%Y'), nullable=False)


class AnalysisSchema(Base):
    __tablename__ = "analysis"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default="gen_random_uuid()")
    llm_summary = Column(String, nullable=False)
    analysis_date = Column(DateTime, default=lambda: datetime.now().strftime('%m-%d-%Y'), nullable=False)
