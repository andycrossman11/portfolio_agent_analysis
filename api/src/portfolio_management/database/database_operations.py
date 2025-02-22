from typing import List, Optional
from uuid import UUID
from datetime import datetime
from .models.pydantic_model_map import Position
from .models.db_models import PositionSchema
from .models.model_conversion import pydantic_to_sqlalchemy, sqlalchemy_to_pydantic
from .database_connection import DatabaseSessionFactory

class DatabaseOperations:
    def __init__(self, db_session_factory: DatabaseSessionFactory):
        self.db_session_factory: DatabaseSessionFactory = db_session_factory

    def create_position(self, ticker: str, quantity: float, total_purchase_price: float, purchase_date: datetime) -> Position:
        """Create a new position and add it to the database."""
        with self.db_session_factory.get_session() as session:
            position = PositionSchema(
                ticker=ticker,
                quantity=quantity,
                total_purchase_price=total_purchase_price,
                purchase_date=purchase_date,
            )
            session.add(position)
            session.commit()
            session.refresh(position)

            pydantic_position = sqlalchemy_to_pydantic(position)
            return pydantic_position

    def get_position(self, position_id: UUID) -> Optional[Position]:
        """Retrieve a position by ID."""
        with self.db_session_factory.get_session() as session:
            postion: PositionSchema = session.query(PositionSchema).filter(PositionSchema.id == position_id).first()
            pydantic_position = sqlalchemy_to_pydantic(postion)
            return pydantic_position

    def get_all_positions(self) -> List[Position]:
        """Retrieve all positions."""
        with self.db_session_factory.get_session() as session:
            position_entries: list[PositionSchema] = session.query(PositionSchema).all()
            positions = [sqlalchemy_to_pydantic(position) for position in position_entries]
            return positions

    def update_position(self, position_id: UUID, ticker: str, quantity: float, total_purchase_price: float, purchase_date: datetime) -> Optional[Position]:
        """Update an existing position."""
        with self.db_session_factory.get_session() as session:
            position = session.query(PositionSchema).filter(PositionSchema.id == position_id).first()
            if not position:
                return None

            position.ticker = ticker
            position.quantity = quantity
            position.total_purchase_price = total_purchase_price
            position.purchase_date = purchase_date

            session.commit()
            session.refresh(position)
            pydantic_position = sqlalchemy_to_pydantic(position)
            return pydantic_position

    def delete_position(self, position_id: UUID) -> bool:
        """Delete a position by ID."""
        with self.db_session_factory.get_session() as session:
            position = session.query(PositionSchema).filter(PositionSchema.id == position_id).first()
            if not position:
                return False

            session.delete(position)
            session.commit()
            return True
