from shared.database.models.model_conversion import PositionModelConversion
from shared.database.models.db_models import PositionSchema
from shared.database.models.pydantic_model_map import Position
import uuid
import datetime

def test_POSITION_sqlalchemy_to_pydantic():
    position_data = PositionSchema(
        id=uuid.uuid4(),
        ticker="AAPL",
        quantity=10,
        purchase_share_price=1500.0,
        purchase_date="01-11-2023"
    )
    
    position = PositionModelConversion.sqlalchemy_to_pydantic(position_data)
    
    assert position.id == position_data.id
    assert position.ticker == position_data.ticker
    assert position.quantity == position_data.quantity
    assert position.purchase_share_price == position_data.purchase_share_price
    assert position.purchase_date == position_data.purchase_date

def test_POSITION_pydantic_to_sqlalchemy():
    position = Position(
        id=uuid.uuid4(),
        ticker="AAPL",
        quantity=10,
        purchase_share_price=1500.0,
        purchase_date="12-30-1999"
    )
    
    position_schema = PositionModelConversion.pydantic_to_sqlalchemy(position)
    
    assert position_schema.id == position.id
    assert position_schema.ticker == position.ticker
    assert position_schema.quantity == position.quantity
    assert position_schema.purchase_share_price == position.purchase_share_price
    assert position_schema.purchase_date == position.purchase_date