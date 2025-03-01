from api.src.portfolio_management.database.models.model_conversion import PositionModelConversion
from src.portfolio_management.database.models.db_models import PositionSchema
from src.portfolio_management.database.models.pydantic_model_map import Position
import uuid
import datetime

def test_POSITION_sqlalchemy_to_pydantic():
    position_data = PositionSchema(
        id=uuid.uuid4(),
        ticker="AAPL",
        quantity=10,
        total_purchase_price=1500.0,
        purchase_date="01-11-2023"
    )
    
    position = PositionModelConversion.sqlalchemy_to_pydantic(position_data)
    
    assert position.id == position_data.id
    assert position.ticker == position_data.ticker
    assert position.quantity == position_data.quantity
    assert position.total_purchase_price == position_data.total_purchase_price
    assert position.purchase_date == position_data.purchase_date

def test_POSITION_pydantic_to_sqlalchemy():
    position = Position(
        id=uuid.uuid4(),
        ticker="AAPL",
        quantity=10,
        total_purchase_price=1500.0,
        purchase_date="12-30-1999"
    )
    
    position_schema = PositionModelConversion.pydantic_to_sqlalchemy(position)
    
    assert position_schema.id == position.id
    assert position_schema.ticker == position.ticker
    assert position_schema.quantity == position.quantity
    assert position_schema.total_purchase_price == position.total_purchase_price
    assert position_schema.purchase_date == position.purchase_date