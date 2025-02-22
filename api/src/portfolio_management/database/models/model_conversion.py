from .db_models import PositionSchema
from .pydantic_model_map import Position

def pydantic_to_sqlalchemy(position: Position) -> PositionSchema:
    return PositionSchema(
        id=position.id,
        ticker=position.ticker,
        quantity=position.quantity,
        total_purchase_price=position.total_purchase_price,
        purchase_date=position.purchase_date,
    )

def sqlalchemy_to_pydantic(position_data: PositionSchema) -> Position:
    return Position(
        id=position_data.id,
        ticker=position_data.ticker,
        quantity=position_data.quantity,
        total_purchase_price=position_data.total_purchase_price,
        purchase_date=position_data.purchase_date,
    )
