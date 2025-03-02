from pydantic import BaseModel
import json

class StockData(BaseModel):
    ticker: str
    buy_price: float
    today_price: float
    quantity: float

def convert_portfolio_data_to_string(portfolio_data: list[StockData]) -> str:
    return json.dumps([data.model_dump() for data in portfolio_data], indent=4)
