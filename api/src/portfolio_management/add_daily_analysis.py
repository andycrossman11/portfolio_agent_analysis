from .llm.llm_inference import LLM, StockData
from .database import DB_OPS, Position
from .stock_market import get_stock_price
import datetime

def add_daily_analysis() -> None:
    positions: list[Position] = DB_OPS.get_all_positions()
    stock_data = convert_positions_to_stock_data(positions)
    analysis = LLM.get_portfolio_analysis(stock_data)
    DB_OPS.create_daily_analysis(analysis, datetime.datetime.now())

def convert_positions_to_stock_data(positions: list[Position]) -> list[StockData]:
    stock_data_list: list[StockData] = []
    for position in positions:
        today_price = get_stock_price(position.ticker)
        stock_data = StockData(ticker=position.ticker, buy_price=position.total_purchase_price / position.quantity, today_price=today_price, quantity=position.quantity)
        stock_data_list.append(stock_data)
    return stock_data_list